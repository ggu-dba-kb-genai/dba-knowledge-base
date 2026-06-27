/*
 * Contribution proxy — Cloudflare Worker (Phase 2, account-free submissions).
 *
 * Accepts a Turnstile-gated JSON POST from the contribution form and logs the
 * submission into a PRIVATE inbox repo (issue + any raw file via the Git Data API),
 * then returns a reference ID. Nothing anonymous is exposed publicly.
 *
 * Secrets (wrangler secret put):  GH_TOKEN, TURNSTILE_SECRET
 * Vars (wrangler.toml [vars]):    ALLOWED_ORIGIN, INBOX_REPO, INBOX_BRANCH,
 *                                 RATE_MAX_DAY, RATE_MAX_MIN
 * KV binding:                     RATE_LIMIT
 *
 * Security posture: Turnstile is the hard gate (fails CLOSED). CORS is not a security
 * control — it only governs browser cross-origin. Tokens/content are never logged.
 */

const TYPES   = ["Session Notes", "Assignment", "Worksheet", "Session PDF", "Other"];
const COURSES = ["C1", "C2", "C3", "C4", "C5", "C6", "General"];
const MAX_TEXT = 200_000;
const MAX_FILE = 2 * 1024 * 1024;
const MAX_BODY = 3 * 1024 * 1024;   // JSON envelope ceiling (2 MB file ≈ 2.7 MB base64 + fields)
const FILE_EXT = ["md", "txt", "pdf"];

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    const cors = corsHeaders(env);

    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors });
    if (request.method !== "POST")    return json({ error: "Method not allowed" }, 405, cors);

    // Reject oversized bodies before parsing. Cheap DoS guard for honest clients;
    // CF platform limits + validate() below are the real bounds (a client may omit
    // Content-Length, so this is defense-in-depth, not the primary control).
    const clen = parseInt(request.headers.get("Content-Length") || "0", 10);
    if (clen > MAX_BODY) return json({ error: "Payload too large." }, 413, cors);

    // CORS allow-list (browser origin). Not a security boundary on its own.
    if (env.ALLOWED_ORIGIN && origin && origin !== env.ALLOWED_ORIGIN) {
      return json({ error: "Origin not allowed" }, 403, cors);
    }

    let body;
    try { body = await request.json(); }
    catch { return json({ error: "Malformed request" }, 400, cors); }

    // 1) Honeypot — pretend success, do nothing (don't tip off bots).
    if (body.website) return json({ ok: true, refid: "—" }, 200, cors);

    // 2) Turnstile — fail CLOSED.
    const ip = request.headers.get("CF-Connecting-IP") || "";
    const human = await verifyTurnstile(body.turnstileToken, ip, env.TURNSTILE_SECRET);
    if (!human) return json({ error: "Captcha verification failed. Please retry." }, 403, cors);

    // 3) Rate limit (soft — KV is eventually consistent; Turnstile is the hard gate).
    const rl = await rateLimit(env, ip);
    if (!rl.ok) return json({ error: rl.msg }, 429, cors);

    // 4) Validate + sanitize.
    const v = validate(body);
    if (v.error) return json({ error: v.error }, 422, cors);
    const c = v.clean;

    // 5) Persist to the private inbox repo.
    const refid = makeRefId();
    try {
      let fileLink = null;
      if (c.file) fileLink = await commitFile(env, refid, c.file);
      const issue = await createIssue(env, refid, c, fileLink);
      return json({ ok: true, refid, issueNumber: issue.number }, 200, cors);
    } catch (e) {
      // Never leak token/content. Map GitHub rate-limit to 503.
      const status = e && e.ghStatus === 429 ? 503 : 502;
      return json({ error: "Could not record your contribution right now. Please try again later." }, status, cors);
    }
  },
};

/* ── CORS / JSON ─────────────────────────────────────────────────────────── */
function corsHeaders(env) {
  return {
    "Access-Control-Allow-Origin":  env.ALLOWED_ORIGIN || "*",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age":       "86400",
    "Vary": "Origin",
  };
}
function json(obj, status, headers) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { "Content-Type": "application/json", ...(headers || {}) },
  });
}

/* ── Turnstile (fail closed) ─────────────────────────────────────────────── */
async function verifyTurnstile(token, ip, secret) {
  if (!token || !secret) return false;
  try {
    const form = new URLSearchParams();
    form.set("secret", secret);
    form.set("response", token);
    if (ip) form.set("remoteip", ip);
    const res = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
      method: "POST", body: form,
    });
    if (!res.ok) return false;
    const data = await res.json();
    return data.success === true;
  } catch {
    return false; // any error → reject
  }
}

/* ── Rate limit (KV, soft) ───────────────────────────────────────────────── */
async function rateLimit(env, ip) {
  if (!env.RATE_LIMIT || !ip) return { ok: true };
  const maxDay = parseInt(env.RATE_MAX_DAY || "5", 10);
  const maxMin = parseInt(env.RATE_MAX_MIN || "2", 10);
  const day = new Date().toISOString().slice(0, 10);
  const min = Math.floor(Date.now() / 60000);
  const dayKey = `d:${ip}:${day}`;
  const minKey = `m:${ip}:${min}`;
  const [d, m] = await Promise.all([env.RATE_LIMIT.get(dayKey), env.RATE_LIMIT.get(minKey)]);
  if (parseInt(d || "0", 10) >= maxDay) return { ok: false, msg: `Daily limit reached (${maxDay}). Please continue tomorrow.` };
  if (parseInt(m || "0", 10) >= maxMin) return { ok: false, msg: "Too many submissions in a short time. Please wait a minute." };
  await Promise.all([
    env.RATE_LIMIT.put(dayKey, String(parseInt(d || "0", 10) + 1), { expirationTtl: 86400 }),
    env.RATE_LIMIT.put(minKey, String(parseInt(m || "0", 10) + 1), { expirationTtl: 120 }),
  ]);
  return { ok: true };
}

/* ── Validation / sanitization ───────────────────────────────────────────── */
function validate(b) {
  const name = String(b.name || "").trim();
  if (!name || name.length > 100) return { error: "Name is required (≤100 characters)." };

  const email = String(b.email || "").trim();
  if (email && (email.length > 200 || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)))
    return { error: "Email address looks invalid." };

  const type = String(b.type || "").trim();
  if (!TYPES.includes(type)) return { error: "Invalid content type." };

  const course = String(b.course || "").trim();
  if (!COURSES.includes(course)) return { error: "Invalid course." };

  const title = String(b.title || "").trim();
  if (!title || title.length > 200) return { error: "Title is required (≤200 characters)." };

  const session = String(b.session || "").trim().slice(0, 200);
  const other   = String(b.other || "").trim().slice(0, 300);

  const contentText = b.contentText != null ? String(b.contentText) : "";
  if (contentText.length > MAX_TEXT) return { error: "Content is too long (≤200,000 characters)." };

  let file = null;
  if (b.file && b.file.b64) {
    const fname = basename(String(b.file.name || "file"));
    const ext = fname.split(".").pop().toLowerCase();
    if (!FILE_EXT.includes(ext)) return { error: "File must be .md, .txt, or .pdf." };
    const b64 = String(b.file.b64).replace(/\s+/g, "");
    if (!/^[A-Za-z0-9+/]+={0,2}$/.test(b64)) return { error: "File payload is not valid base64." };
    const pad = b64.endsWith("==") ? 2 : b64.endsWith("=") ? 1 : 0;
    const bytes = Math.floor(b64.length * 3 / 4) - pad;
    if (bytes > MAX_FILE) return { error: "File exceeds the 2 MB limit." };
    file = { name: fname, b64 };
  }

  if (!contentText.trim() && !file) return { error: "Provide content text or attach a file." };
  if (contentText.trim() && contentText.trim().length < 50 && !file)
    return { error: "Content is too short (≥50 characters)." };

  if (!b.attribution) return { error: "Attribution must be confirmed." };

  const piiFlag = scanPII(contentText).length > 0;
  return { clean: { name, email, type, course, title, session, other, contentText: contentText.trim(), file, piiFlag } };
}

function basename(p) {
  return p.replace(/\\/g, "/").split("/").pop().replace(/[^\w.\- ]/g, "_").slice(0, 120) || "file";
}
function scanPII(text) {
  const hits = [];
  if (/[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}/i.test(text)) hits.push("email");
  if (/(?:\+?\d[\s-]?){10,}/.test(text)) hits.push("phone");
  if (/\b\d{7,}\b/.test(text)) hits.push("long-id");
  return hits;
}
// Escape a value for a single markdown table cell.
function cell(s) {
  return String(s).replace(/\|/g, "\\|").replace(/[\r\n]+/g, " ").trim();
}

/* ── GitHub API ──────────────────────────────────────────────────────────── */
async function gh(env, path, method = "GET", payload) {
  const res = await fetch("https://api.github.com" + path, {
    method,
    headers: {
      "Authorization": `Bearer ${env.GH_TOKEN}`,
      "Accept": "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
      "User-Agent": "dba-kb-contrib-proxy",
      ...(payload ? { "Content-Type": "application/json" } : {}),
    },
    body: payload ? JSON.stringify(payload) : undefined,
  });
  if (!res.ok) {
    const err = new Error("github " + res.status);
    err.ghStatus = res.status;
    throw err;
  }
  return res.json();
}

// Commit a file to inbox/<refid>/<name> on INBOX_BRANCH via the Git Data API
// (blob → tree → commit → ref) — the documented path for files >1 MB.
async function commitFile(env, refid, file) {
  const repo = env.INBOX_REPO;
  const branch = env.INBOX_BRANCH || "main";
  const path = `inbox/${refid}/${file.name}`;

  const ref = await gh(env, `/repos/${repo}/git/ref/heads/${branch}`);
  const baseSha = ref.object.sha;
  const baseCommit = await gh(env, `/repos/${repo}/git/commits/${baseSha}`);

  const blob = await gh(env, `/repos/${repo}/git/blobs`, "POST", { content: file.b64, encoding: "base64" });
  const tree = await gh(env, `/repos/${repo}/git/trees`, "POST", {
    base_tree: baseCommit.tree.sha,
    tree: [{ path, mode: "100644", type: "blob", sha: blob.sha }],
  });
  const commit = await gh(env, `/repos/${repo}/git/commits`, "POST", {
    message: `inbox: ${refid} — ${file.name}`,
    tree: tree.sha,
    parents: [baseSha],
  });
  await gh(env, `/repos/${repo}/git/refs/heads/${branch}`, "PATCH", { sha: commit.sha });

  return `https://github.com/${repo}/blob/${branch}/${path.split("/").map(encodeURIComponent).join("/")}`;
}

async function createIssue(env, refid, c, fileLink) {
  const repo = env.INBOX_REPO;
  const issueTitle = `[${refid}] ${c.type}: ${c.title}`.slice(0, 250);

  let md = `## Contribution \`${refid}\`\n\n| Field | Value |\n|---|---|\n`;
  md += `| Contributor | ${cell(c.name)} |\n`;
  if (c.email)   md += `| Email | ${cell(c.email)} |\n`;          // private repo → OK
  md += `| Type | ${cell(c.type)}${c.type === "Other" && c.other ? " — " + cell(c.other) : ""} |\n`;
  md += `| Course | ${cell(c.course)} |\n`;
  if (c.session) md += `| Session | ${cell(c.session)} |\n`;
  md += `| Title | ${cell(c.title)} |\n`;
  md += `| Attribution | ✅ confirmed |\n`;
  if (c.piiFlag) md += `| ⚠ Auto-flag | possible personal data — reviewer please check |\n`;
  md += `\n---\n\n`;

  if (fileLink) md += `### File\n\n📎 [\`${cell(c.file.name)}\`](${fileLink})\n\n`;
  if (c.contentText) md += `### Content\n\n${c.contentText}\n`;

  return gh(env, `/repos/${repo}/issues`, "POST", {
    title: issueTitle,
    body: md,
    labels: ["contribution", "needs-review"],
  });
}

/* ── Reference ID:  YYYYMMDD-<6 hex> ─────────────────────────────────────── */
function makeRefId() {
  const d = new Date();
  const ymd = d.toISOString().slice(0, 10).replace(/-/g, "");
  const rnd = crypto.getRandomValues(new Uint8Array(3));
  const hex = Array.from(rnd, (b) => b.toString(16).padStart(2, "0")).join("");
  return `${ymd}-${hex}`;
}

/* Named exports for unit testing (Cloudflare uses only the default export). */
export { validate, scanPII, cell, basename, makeRefId };
