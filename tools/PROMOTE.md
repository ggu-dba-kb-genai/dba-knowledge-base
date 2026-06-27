# Promotion agent — approved submission → OKF node → PR (Phase 3)

`tools/promote.py` turns an **approved** contribution sitting in the private inbox repo
into a properly structured, cross-linked OKF node in `bundle/`, regenerates the graph +
map, and opens a **pull request** on the public repo for your final approval. You stay
the gate: the agent never merges — it drafts; you review the PR and merge.

```
private inbox repo                      tools/promote.py  (local, your machine)
  issue [<refid>] + inbox/<refid>/file
            │  gh api (read)
            ▼
   ┌───────────────────────────────────────────────────────────────┐
   │ 1 fetch submission (metadata + text and/or file bytes)         │
   │ 2 build catalogue of existing node ids/labels/types           │
   │ 3 Gemini 3.5-flash → STRICT JSON {title,description,tags,      │
   │     body_markdown, related_ids[]}   (PDF sent inline/multimodal)│
   │ 4 validate: json, type→dir, related_ids ⊆ catalogue, slug uniq │
   │ 5 assemble bundle/<dir>/<slug>.md  (front-matter + body +      │
   │     ## Related built from related_ids + contributor credit)    │
   │ 6 rebuild: build_bundle.py → bundle.json → kb-data.json;       │
   │            gen_viz_v2.py → map.html                            │
   │ 7 branch promote/<refid> → commit → push → open PR (public)    │
   └───────────────────────────────────────────────────────────────┘
            │
            ▼
   YOU review the PR (the structured node + graph diff) → merge → Pages rebuilds → live
```

## Why this shape
- **Local CLI, not a cloud Action.** Runs on demand under your control, reuses the
  existing local pipeline, needs no new cloud secrets — just your `gh` login and a
  Gemini key you already have. (A GitHub Action is a later, fully-autonomous option.)
- **PR is the human gate.** Matches "I approve before anything is added." The agent
  drafts; merging is yours.
- **PDFs go straight to Gemini (multimodal).** No brittle PDF-extraction step; Gemini
  reads the PDF and structures it. `pdftotext` is a fallback.

## Anti-hallucination (the real risk)
The known failure mode is an LLM inventing links to nodes that don't exist.

- The model may only **pick `related_ids` from a catalogue we provide** — it never
  writes paths. **We** convert each chosen id → the correct relative `../dir/slug.md`
  path, so a broken link is impossible by construction.
- Every returned id is checked against the live catalogue; unknown ids are dropped.
- Output must be **strict JSON** with required keys, else the run aborts (no partial write).
- The node carries **provenance** front-matter (`contributor`, `source_refid`) and a
  visible "Contributed by …" credit. Nothing is auto-published — you see it all in the PR.

## Type mapping (submission → OKF)
| Submission type | OKF `type` | dir |
|---|---|---|
| Assignment | Assignment | `bundle/assignments/` |
| Session Notes / Session PDF | Session | `bundle/sessions/` |
| Worksheet | Reference | `bundle/references/` |
| Other | Reference | `bundle/references/` |

(You can change the type in the PR before merging — it's one line of front-matter.)

## Usage
```bash
# from the repo root, with a Gemini key in the environment
export GEMINI_API_KEY=AIza...            # or GEMINI_KEY / GOOGLE_API_KEY

# dry run — fetch, structure, validate, print the proposed node. Writes nothing.
python tools/promote.py 20260627-6217b4 --dry-run

# real run — write the node, rebuild graph+map, open a PR on the public repo
python tools/promote.py 20260627-6217b4

# write the node + rebuild locally but do NOT push / open a PR (inspect first)
python tools/promote.py 20260627-6217b4 --no-pr
```
Defaults: `INBOX_REPO=ggu-dba-kb-genai/dba-kb-contrib-inbox`,
`PUBLIC_REPO=ggu-dba-kb-genai/dba-knowledge-base`, `MODEL=gemini-3.5-flash`
(override via env).

## After merge
The promoted node is live in the map + tutor. Then:
- Close the inbox issue (optionally label it `promoted`), and prune `inbox/<refid>/`.
- The contributor is credited by name in the node.

## Dependencies
PyYAML (already used by `build_bundle.py`) + Python stdlib (`urllib`) for the Gemini REST
call. `gh` CLI for inbox read + PR. No new packages.

## Limits / next
- One submission at a time; you review every PR. That's intentional for now.
- A future Action could trigger on an `approved` label and run this unattended — only
  worth it once the manual path is proven and volume justifies it.
