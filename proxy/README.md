# Contribution Proxy — account-free submissions (Phase 2)

A tiny Cloudflare Worker that lets anyone submit a contribution **without a GitHub
account**. The browser form POSTs to this Worker; the Worker (holding one scoped
GitHub token) logs the submission into a **private inbox repo** — issue + any raw
file — and hands the contributor a **reference ID**. Nothing anonymous is exposed
publicly until the maintainer reviews it and the OKF pipeline promotes it.

```
Browser (contribute.html on GitHub Pages)
   │  Turnstile-gated POST (JSON, file as base64)
   ▼
Cloudflare Worker ── GitHub API (one token, PRIVATE inbox repo only) ──►
        • Issue  (labels: contribution, needs-review)          ← review queue
        • File   committed via Git Data API → inbox/<refid>/<file>
   │
   └─ returns { refid }   (no public link — private until approved)
```

The static site keeps working with **no proxy** (it falls back to the Phase-1
prefilled-issue flow). The account-free path turns on only once you set `PROXY_URL`
+ `TURNSTILE_SITEKEY` in `docs/contribute.html`.

---

## Why this shape

| Decision | Choice | Reason |
|---|---|---|
| Host | Cloudflare Workers | Free 100k req/day, native **Turnstile** CAPTCHA, **KV** rate-limit, no cold starts. |
| Bot defense | Turnstile + per-IP rate limit + honeypot | Public write path using *our* token. CAPTCHA is the real gate; rate-limit + size caps bound abuse. |
| Where content lands | **Private** inbox repo (issue + file) | Nothing anonymous is public until you approve. Honours the form's "private until reviewed" promise; keeps contributor email out of any public surface. |
| File commits | **Git Data / blobs API** | The documented path for files >1 MB (the Contents API can 422 above ~1 MB). Robust to our 2 MB cap. |

### Token isolation — one token, zero reach into `main`

Because the issue lives in the **private inbox repo** (not public `main`), the Worker
needs exactly **one** fine-grained PAT, scoped to **the inbox repo only**:

- **`GH_TOKEN`** — fine-grained PAT, repo access: *only* `dba-kb-contrib-inbox`,
  permissions **Issues: R/W** + **Contents: R/W**.

A GitHub fine-grained PAT cannot be scoped to a branch — but here it doesn't matter:
the token can't see `main`'s repo at all. Blast radius if it leaks = junk in a
disposable private repo (deletable). The published knowledge base is unreachable.

> You originally picked an inbox *branch* on the main repo. A branch can't hold
> **private** issues (issues inherit the repo's visibility), so it can't satisfy the
> "private until reviewed" promise the form already makes. A separate **private** repo
> does — and removes the main-repo token entirely. That's why this deviates to a repo.

---

## What the Worker enforces (every request)

1. **CORS allow-list** — only the Pages origin may call it from a browser (+ `OPTIONS` preflight).
2. **Honeypot** — hidden `website` field must be empty (else silent `200`, no action).
3. **Turnstile** — `turnstileToken` verified server-side via siteverify (+ client IP).
   **Fails closed**: any error/timeout/`success!==true` → rejected.
4. **Rate limit (KV)** — per IP: ≤ 2/min and ≤ 5/day (configurable). Soft bound
   (KV is eventually consistent) — Turnstile is the hard gate.
5. **Validation** — required fields; `type`/`course` whitelists; length bounds
   (title ≤ 200, name ≤ 100, text ≤ 200 000); file ext ∈ {md,txt,pdf}, ≤ 2 MB, base64 well-formed.
6. **Sanitization** — filename basename-only (no `..`/`/` traversal); metadata table
   cells escape `|`/newlines; tokens and content are never logged.

GitHub renders issue markdown sandboxed (no script execution); residual risk is
formatting, not XSS. Content is length-capped regardless.

---

## Deploy (one-time, ~15 min)

### 0. Prerequisites
- Cloudflare account (free) + `npm i -g wrangler` and `wrangler login`.
- Admin on the `ggu-dba-kb-genai` org (to create the inbox repo + token).

### 1. Create the **private** inbox repo
Create an empty **private** repo, e.g. `ggu-dba-kb-genai/dba-kb-contrib-inbox`, with a
`main` branch (one commit — a README is fine). This holds raw, unreviewed submissions
and the review-queue issues.

Then create the review-queue labels **in that repo** — GitHub silently drops labels
that don't exist in the target repo, so without this every submission lands unlabeled
and the `needs-review` queue won't filter:
```bash
gh label create contribution --repo ggu-dba-kb-genai/dba-kb-contrib-inbox --color 0e8a16 --description "Content contribution"
gh label create needs-review  --repo ggu-dba-kb-genai/dba-kb-contrib-inbox --color fbca04 --description "Awaiting maintainer review"
```

### 2. Create one fine-grained PAT
GitHub → Settings → Developer settings → **Fine-grained tokens**:
- Repo access: **only** `dba-kb-contrib-inbox`
- Permissions: **Issues: Read & Write** + **Contents: Read & Write**
- → this is `GH_TOKEN`.

### 3. Create a Turnstile widget
Cloudflare dash → **Turnstile** → Add site → mode **Managed**. Add your Pages domain
(`ggu-dba-kb-genai.github.io`). Note the **Site Key** (public → form) and **Secret Key**
(→ Worker).

### 4. Create the KV namespace
```bash
cd proxy
wrangler kv namespace create RATE_LIMIT
# paste the returned id into wrangler.toml (kv_namespaces.id)
```

### 5. Set Worker secrets
```bash
cd proxy
wrangler secret put GH_TOKEN            # the inbox-repo fine-grained PAT
wrangler secret put TURNSTILE_SECRET    # Turnstile secret key
```

### 6. Configure `wrangler.toml`
Set `[vars]`: `ALLOWED_ORIGIN`, `INBOX_REPO`, `INBOX_BRANCH`, and the rate-limit
numbers. Defaults are filled in.

### 7. Deploy
```bash
cd proxy
wrangler deploy
# → prints the Worker URL, e.g. https://dba-kb-contrib.<subdomain>.workers.dev
```

### 8. Turn on the account-free path
Edit `docs/contribute.html`, near the top of the app `<script>`:
```js
const PROXY_URL         = "https://dba-kb-contrib.<subdomain>.workers.dev";
const TURNSTILE_SITEKEY = "0x4AAAA...";   // Turnstile site key
```
Commit + push. Now the form submits account-free through the proxy and shows the
contributor a reference ID. Leave them empty to keep the Phase-1 prefilled-issue (login) flow.

---

## Local dev / test
```bash
cd proxy
wrangler dev    # http://localhost:8787
```
With Turnstile **testing keys** (always-pass) you can drive a full submission locally —
see <https://developers.cloudflare.com/turnstile/troubleshooting/testing/>. Without a
valid token the Worker returns `403` (fail-closed) — that's correct.

A no-token request should be rejected:
```bash
curl -i -X POST http://localhost:8787 \
  -H 'content-type: application/json' \
  -H 'origin: https://ggu-dba-kb-genai.github.io' \
  -d '{"name":"T","type":"Assignment","course":"C6","title":"x","contentText":"hello body","turnstileToken":""}'
# → HTTP 403  {"error":"Captcha verification failed..."}
```

---

## Cost & limits
- Workers free: 100k req/day · Turnstile: free · KV: 100k reads + 1k writes/day free —
  all far above expected contribution volume.
- Files committed via Git Data API (base64 blob → tree → commit → ref); fine to 2 MB.

## Operating it
- Review `contribution` + `needs-review` issues in the **private inbox repo**; raw files
  sit under `inbox/<refid>/`.
- Approve → run the OKF pipeline (`tools/build_bundle.py` → `gen_viz_v2.py`) to promote
  into the public bundle, crediting the contributor by name.
- Rotate `GH_TOKEN` before expiry (fine-grained max 1 year); revoke instantly if abused.
- Prune the inbox repo periodically.
- Concurrency: simultaneous file uploads race on the inbox branch ref; the loser gets a
  `502` and can simply retry. Harmless at cohort volume — not worth engineering around.

## Status note
This is real attack surface + operating burden (token rotation, inbox pruning,
Cloudflare + Turnstile accounts) built ahead of demonstrated external demand. Phase 1
(GitHub-login submission) already works for anyone with an account. Build-then-wait was
the deliberate choice; if external submissions don't materialise, this can sit dormant
(empty `PROXY_URL`) at zero cost.
