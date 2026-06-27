#!/usr/bin/env python3
"""
tools/promote.py — Phase 3 promotion agent.

Turn an APPROVED contribution in the private inbox repo into a structured, cross-linked
OKF node in bundle/, regenerate the graph + map, and open a PR on the public repo for
final human approval. The agent drafts; you merge. See tools/PROMOTE.md.

    python tools/promote.py <refid> [--dry-run | --no-pr]

Env: GEMINI_API_KEY (or GEMINI_KEY / GOOGLE_API_KEY); optional INBOX_REPO, PUBLIC_REPO, MODEL.
Deps: PyYAML + stdlib; `gh` CLI authed for the inbox + public repos.
"""
import sys, os, re, json, base64, subprocess, datetime, urllib.request, urllib.error
import yaml

HERE        = os.path.dirname(os.path.abspath(__file__))
ROOT        = os.path.dirname(HERE)
BUNDLE_DIR  = os.path.join(ROOT, "bundle")
BUNDLE_JSON = os.path.join(HERE, "bundle.json")
KB_DATA     = os.path.join(ROOT, "docs", "kb-data.json")
MAP_HTML    = os.path.join(ROOT, "docs", "map.html")

INBOX_REPO  = os.environ.get("INBOX_REPO",  "ggu-dba-kb-genai/dba-kb-contrib-inbox")
PUBLIC_REPO = os.environ.get("PUBLIC_REPO", "ggu-dba-kb-genai/dba-knowledge-base")
MODEL       = os.environ.get("MODEL", "gemini-3.5-flash")
KEY         = os.environ.get("GEMINI_API_KEY") or os.environ.get("GEMINI_KEY") or os.environ.get("GOOGLE_API_KEY")

# submission content-type → (OKF type, bundle subdir)
TYPE_MAP = {
    "Assignment":    ("Assignment", "assignments"),
    "Session Notes": ("Session",    "sessions"),
    "Session PDF":   ("Session",    "sessions"),
    "Worksheet":     ("Reference",  "references"),
    "Other":         ("Reference",  "references"),
}
TRACKED = ["bundle", "tools/bundle.json", "docs/kb-data.json", "docs/map.html"]


def die(msg, code=1):
    print(f"✗ {msg}", file=sys.stderr); sys.exit(code)

def sh(args, check=True, **kw):
    r = subprocess.run(args, capture_output=True, text=True, **kw)
    if check and r.returncode != 0:
        die(f"command failed: {' '.join(args)}\n{r.stderr.strip()}")
    return r

def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return re.sub(r"-{2,}", "-", s) or "contribution"

def fix_escapes(s):
    """Some model outputs escape newlines/tabs as LITERAL backslash sequences inside the
    JSON string. Repair only the pathological case (literal \\n dominates real newlines),
    so well-formed output is left untouched."""
    s = s or ""
    if "\\n" in s and s.count("\n") < s.count("\\n"):
        s = s.replace("\\r\\n", "\n").replace("\\n", "\n").replace("\\t", "\t")
    return s


# ── 1 · fetch the approved submission from the private inbox repo ────────────────
def fetch_submission(refid):
    out = sh(["gh", "issue", "list", "--repo", INBOX_REPO, "--state", "all",
              "--limit", "200", "--json", "number,title,body"]).stdout
    issues = json.loads(out)
    issue = next((i for i in issues if f"[{refid}]" in i["title"]), None)
    if not issue:
        die(f"no inbox issue with [{refid}] in its title (repo {INBOX_REPO})")

    body = issue["body"] or ""
    def field(name):
        m = re.search(rf"^\|\s*{re.escape(name)}\s*\|\s*(.+?)\s*\|\s*$", body, re.M | re.I)
        return m.group(1).strip() if m else ""
    contributor = re.sub(r"\s*\(.*?\)\s*$", "", field("Contributor")) or "Anonymous"
    ctype_raw   = field("Type").split("—")[0].strip()
    course      = field("Course")
    title       = field("Title")
    mc = re.search(r"^###\s+Content\s*$(.+)", body, re.M | re.S)
    content_text = mc.group(1).strip() if mc else ""

    # any committed file under inbox/<refid>/ (via Git Data blobs API → robust to >1MB)
    file_name = file_bytes = None
    lr = sh(["gh", "api", f"repos/{INBOX_REPO}/contents/inbox/{refid}"], check=False)
    if lr.returncode == 0:
        try:
            entries = [e for e in json.loads(lr.stdout) if e.get("type") == "file"]
        except Exception:
            entries = []
        if entries:
            e = entries[0]
            blob = json.loads(sh(["gh", "api", f"repos/{INBOX_REPO}/git/blobs/{e['sha']}"]).stdout)
            file_bytes = base64.b64decode(blob["content"])
            file_name  = e["name"]

    if ctype_raw not in TYPE_MAP:
        die(f"unknown submission type '{ctype_raw}' (expected one of {list(TYPE_MAP)})")
    if not (content_text or file_bytes):
        die("submission has neither inline content nor an attached file")

    return dict(refid=refid, issue=issue["number"], contributor=contributor,
                ctype=ctype_raw, course=course, title=title,
                content_text=content_text, file_name=file_name, file_bytes=file_bytes)


# ── 2 · catalogue of existing nodes (the only ids the model may link to) ─────────
def load_catalogue():
    data = json.load(open(BUNDLE_JSON, encoding="utf-8"))
    nodes = [n["data"] for n in data["nodes"]]
    cat   = {d["id"]: {"label": d["label"], "type": d["type"]} for d in nodes}
    return data, cat


# ── 3 · Gemini: structure the raw submission into a node (strict JSON) ───────────
SCHEMA = {
    "type": "object",
    "properties": {
        "title":        {"type": "string"},
        "description":  {"type": "string"},
        "tags":         {"type": "array", "items": {"type": "string"}},
        "body_markdown":{"type": "string"},
        "related_ids":  {"type": "array", "items": {"type": "string"}},
    },
    "required": ["title", "description", "tags", "body_markdown", "related_ids"],
}

def build_prompt(sub, cat):
    lines = [f"{cid} | {v['type']} | {v['label']}" for cid, v in cat.items()]
    catalogue = "\n".join(lines)
    return f"""You are structuring a community contribution into ONE node of an existing knowledge graph (the "Open Knowledge Format") for a Doctor of Business Administration program on emerging tech, ML, deep learning, generative AI, AI project design and responsible AI.

Return a JSON object with these fields:
- title: a clear, specific node title (<= 90 chars).
- description: ONE sentence (<= 240 chars) summarising the node.
- tags: 3 to 6 lowercase-hyphenated topic tags.
- body_markdown: a well-structured Markdown body. **SYNTHESISE and SUMMARISE the source in your own words — do NOT reproduce the source text verbatim.** This is published to a public CC-BY repository, so for assignment briefs, worksheets or any copyrighted material you must paraphrase and condense, never copy. Use clear `##` section headings. Capture the substance: what it is, the key points, and (if an assignment) the deliverables and grading/rubric in summary form, and the main takeaways. Do NOT add a "Related" section or any links — those are generated separately.
- related_ids: 2 to 6 ids of the EXISTING nodes most related to this contribution, chosen ONLY from the catalogue below, using the exact id strings. Always include the parent course for the stated course. Never invent ids.

SUBMISSION
  type: {sub['ctype']}
  course: {sub['course']}
  contributor: {sub['contributor']}
  proposed title: {sub['title']}
{'(the source is the attached PDF)' if sub['file_bytes'] else 'RAW CONTENT follows below.'}

CATALOGUE (id | type | label):
{catalogue}
"""

def call_gemini(sub, cat):
    if not KEY:
        die("no Gemini key — set GEMINI_API_KEY (or GEMINI_KEY / GOOGLE_API_KEY)")
    parts = [{"text": build_prompt(sub, cat)}]
    if sub["file_bytes"] and (sub["file_name"] or "").lower().endswith(".pdf"):
        parts.append({"inline_data": {"mime_type": "application/pdf",
                                      "data": base64.b64encode(sub["file_bytes"]).decode()}})
    elif sub["file_bytes"]:
        parts[0]["text"] += "\n\nRAW CONTENT:\n" + sub["file_bytes"].decode("utf-8", "replace")
    else:
        parts[0]["text"] += "\n\nRAW CONTENT:\n" + sub["content_text"]

    payload = {
        "contents": [{"role": "user", "parts": parts}],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseSchema": SCHEMA,
            "temperature": 0.3,
        },
    }
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}"
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            resp = json.load(r)
    except urllib.error.HTTPError as e:
        die(f"Gemini HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:400]}")
    try:
        text = resp["candidates"][0]["content"]["parts"][0]["text"]
        obj = json.loads(text)
    except Exception as e:
        die(f"could not parse Gemini JSON output: {e}")
    for k in SCHEMA["required"]:
        if k not in obj:
            die(f"Gemini output missing required field: {k}")
    return obj


# ── 4/5 · validate + assemble the bundle/*.md node ───────────────────────────────
def rel_link(target_id, new_dir_abs):
    target_abs = os.path.join(BUNDLE_DIR, target_id + ".md")
    return os.path.relpath(target_abs, new_dir_abs).replace(os.sep, "/")

def related_section(related_ids, cat, new_dir_abs):
    groups = {}
    for rid in related_ids:
        t = cat[rid]["type"]
        groups.setdefault(t, []).append(rid)
    order = ["Course", "Session", "Concept", "Assignment", "Reference"]
    heading = {"Course": "Parent Course", "Session": "Sessions", "Concept": "Concepts",
               "Assignment": "Assignments", "Reference": "References"}
    out = ["## Related", ""]
    for t in order:
        if t not in groups:
            continue
        links = ", ".join(f"[{cat[r]['label']}]({rel_link(r, new_dir_abs)})" for r in groups[t])
        out.append(f"- **{heading[t]}**: {links}")
    return "\n".join(out)

def assemble(sub, gen, cat):
    okf_type, subdir = TYPE_MAP[sub["ctype"]]
    related = [r for r in gen["related_ids"] if r in cat]          # drop any hallucinated id
    dropped = [r for r in gen["related_ids"] if r not in cat]
    if dropped:
        print(f"  · dropped {len(dropped)} unknown related id(s): {dropped}")

    title_slug  = slugify(gen["title"])
    course_slug = slugify(sub["course"]) if sub.get("course") else ""
    base = title_slug if (not course_slug or title_slug.startswith(course_slug)) else f"{course_slug}-{title_slug}"
    slug = base
    dir_abs = os.path.join(BUNDLE_DIR, subdir)
    if os.path.exists(os.path.join(dir_abs, slug + ".md")):        # never overwrite
        slug = f"{base}-{sub['refid']}"
        print(f"  · slug collision → suffixed with refid: {slug}")
    node_id = f"{subdir}/{slug}"

    fm = {
        "type": okf_type, "resource": None,
        "title": gen["title"].strip(),
        "description": gen["description"].strip(),
        "tags": [slugify(t) for t in gen["tags"]][:6],
        "timestamp": datetime.date.today().isoformat(),
        "contributor": sub["contributor"],
        "source_refid": sub["refid"],
    }
    fm_text = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=88).strip()
    rel = related_section(related, cat, dir_abs)
    body = fix_escapes(gen["body_markdown"]).strip()
    credit = f"---\n\n*Contributed by **{sub['contributor']}** · source ref `{sub['refid']}` · synthesised into OKF and reviewed before publication.*"
    text = f"---\n{fm_text}\n---\n\n{body}\n\n{rel}\n\n{credit}\n"
    return node_id, os.path.join(dir_abs, slug + ".md"), text, related


# ── git / rebuild helpers ────────────────────────────────────────────────────────
def assert_clean_tree():
    r = sh(["git", "-C", ROOT, "status", "--porcelain", "--"] + TRACKED)
    if r.stdout.strip():
        die("working tree has uncommitted changes in build paths "
            "(bundle/, tools/bundle.json, docs/kb-data.json, docs/map.html). "
            "Commit or stash them first, then re-run.")

def edge_set(data):
    return {(e["data"]["source"], e["data"]["target"]) for e in data["edges"]}

def rebuild_and_check(node_id, before):
    sh(["python3", os.path.join(HERE, "build_bundle.py")])
    after = json.load(open(BUNDLE_JSON, encoding="utf-8"))
    n0, n1 = len(before["nodes"]), len(after["nodes"])
    if n1 != n0 + 1:
        die(f"node delta is {n1 - n0}, expected exactly +1 — aborting (dirty rebuild?)")
    ids_after = {n["data"]["id"] for n in after["nodes"]}
    if node_id not in ids_after:
        die(f"new node '{node_id}' not found after rebuild")
    new_edges = edge_set(after) - edge_set(before)
    stray = [e for e in new_edges if node_id not in e]
    if stray:
        die(f"{len(stray)} new edge(s) do not touch the new node — aborting: {stray[:5]}")
    # sync the served copy + regenerate the map
    with open(KB_DATA, "w", encoding="utf-8") as f:
        json.dump(after, f, ensure_ascii=False)
    sh(["python3", os.path.join(HERE, "gen_viz_v2.py")])
    return n1, len(new_edges)


# ── main ─────────────────────────────────────────────────────────────────────────
def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    if len(args) != 1:
        die("usage: python tools/promote.py <refid> [--dry-run | --no-pr]")
    refid = args[0]
    dry, no_pr = "--dry-run" in flags, "--no-pr" in flags

    print(f"▶ promoting {refid}  (model={MODEL}, dry_run={dry}, no_pr={no_pr})")
    if not dry:
        assert_clean_tree()   # fail fast before spending a Gemini call
    sub = fetch_submission(refid)
    print(f"  · {sub['ctype']} · course {sub['course']} · by {sub['contributor']}"
          + (f" · file {sub['file_name']}" if sub['file_name'] else ""))
    data, cat = load_catalogue()
    print(f"  · catalogue: {len(cat)} nodes")
    gen = call_gemini(sub, cat)
    node_id, path, text, related = assemble(sub, gen, cat)
    relpath = os.path.relpath(path, ROOT)

    print(f"\n──────── proposed node: {node_id} ────────")
    print(f"file: {relpath}")
    print(f"related → {related}")
    print("────────────────────────────────────────────")
    print(text)
    print("────────────────────────────────────────────")

    if dry:
        print("✓ dry run — nothing written."); return

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    n1, ne = rebuild_and_check(node_id, data)
    print(f"✓ wrote node + rebuilt: {n1} nodes, +{ne} edges")

    if no_pr:
        print("✓ --no-pr: changes left in working tree for inspection "
              "(git checkout -- . to discard, or commit/PR yourself)."); return

    branch = f"promote/{refid}"
    orig = sh(["git", "-C", ROOT, "rev-parse", "--abbrev-ref", "HEAD"]).stdout.strip()
    rel_lines = "\n".join(f"- [{cat[r]['label']}]({r}) ({cat[r]['type']})" for r in related)
    pr_body = (
        f"Promotes approved contribution `{refid}` (inbox issue #{sub['issue']}) into the knowledge base.\n\n"
        f"**Node:** `{node_id}`  ·  **Type:** {TYPE_MAP[sub['ctype']][0]}\n"
        f"**Title:** {gen['title']}\n"
        f"**Contributor:** {sub['contributor']}\n\n"
        f"**Description:** {gen['description']}\n\n"
        f"**Cross-links added:**\n{rel_lines}\n\n"
        f"Body was **synthesised** by the promotion agent (not copied) and is the review target — "
        f"regenerated `bundle.json` / `kb-data.json` / `map.html` are collapsed via `.gitattributes`.\n\n"
        f"Merging publishes the node (Pages rebuilds). Reject by closing this PR.\n\n"
        f"🤖 Generated with [Claude Code](https://claude.com/claude-code)"
    )
    # idempotent: drop any stale local branch left by a previous failed run
    sh(["git", "-C", ROOT, "branch", "-D", branch], check=False)
    try:
        sh(["git", "-C", ROOT, "checkout", "-b", branch])
        sh(["git", "-C", ROOT, "add", relpath, "tools/bundle.json", "docs/kb-data.json",
            "docs/map.html", ".gitattributes"])
        sh(["git", "-C", ROOT, "commit", "-q", "-m", f"Promote contribution {refid}: {gen['title']}"])
        sh(["git", "-C", ROOT, "push", "-u", "--force-with-lease", "origin", branch])
        existing = sh(["gh", "pr", "list", "--repo", PUBLIC_REPO, "--head", branch,
                       "--state", "open", "--json", "url", "--jq", ".[0].url"], check=False).stdout.strip()
        if existing:
            print(f"✓ branch updated; existing PR: {existing}")
        else:
            pr = sh(["gh", "pr", "create", "--repo", PUBLIC_REPO, "--base", "main", "--head", branch,
                     "--title", f"Promote {refid}: {gen['title']}", "--body", pr_body])
            print(f"✓ PR opened:\n{pr.stdout.strip()}")
    finally:
        # always return to the original branch so a PR-step failure never strands you on promote/<refid>
        sh(["git", "-C", ROOT, "checkout", orig], check=False)
        print(f"  (working tree restored to '{orig}')")


if __name__ == "__main__":
    main()
