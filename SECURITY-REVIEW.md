# Pipeline Review — security · functionality · performance · token usage

Date: 2026-06-27 · Scope: the end-to-end contribution pipeline
(`proxy/worker.js`, `tools/promote.py`, `docs/contribute.html`, `docs/kb-tools.js`,
`tools/build_bundle.py`, `tools/gen_viz_v2.py`).

**Verdict:** the system is well-built and safe to run as-is. It was already hardened
through earlier review passes (Turnstile fail-closed, least-privilege token on a private
inbox repo, anti-hallucination cross-linking, human gates at submission and merge). This
review found **no ship-blockers**. Three real, cheap improvements were applied; a handful
of marginal items were deliberately left alone with reasons. The dominant risk in a review
like this is *introducing a regression into a live system*, so changes were kept tight and
each was verified.

---

## What was checked, by dimension

**Security**
- Internet-facing worker: Turnstile is the hard gate and fails CLOSED; CORS is correctly
  treated as non-security; honeypot returns a silent 200; rate-limit is soft (KV) with
  Turnstile as the real control. Token (`GH_TOKEN`) is scoped to the **private** inbox repo
  only — even a full worker compromise cannot touch `main`. No secrets are logged; errors
  are mapped to generic messages.
- `promote.py` runs locally and shells out: all `subprocess` calls use **list args, no
  `shell=True`** → no shell injection. `refid` is operator-supplied (argv), not attacker-supplied.
- Untrusted-content handling: the contribution body is attacker-controlled (public form →
  private inbox → Gemini). `related_ids` are already filtered against the live catalogue
  (hallucinated/injected ids dropped) and the relative paths are built by us, so broken or
  forged links are impossible by construction. The human PR gate is the final backstop.
- Client form: PII soft-scan + honeypot + localStorage rate-limit are defense-in-depth; the
  server re-validates everything. Dedup output is `esc()`-escaped before `innerHTML`.

**Functionality**
- Worker → inbox → `promote.py` field contract is consistent (Type/Course/Title/`### Content`
  parsing matches what the worker writes; the file path `inbox/<refid>/…` matches both sides).
- `promote.py` invariants are strong: clean-tree fail-fast *before* spending a Gemini call,
  strict-JSON schema, `+1` node-delta assertion, "every new edge touches the new node," never
  overwrite (refid suffix on slug collision), crash-safe PR step (`finally` returns to the
  original branch), idempotent re-run.
- `build_bundle.py` reproduces the published cache exactly (parity gate: 118 nodes / 1,121
  edges, 0 body mismatches).

**Performance**
- Worker: a handful of sequential GitHub Data-API calls per file submission — fine at this
  volume (≤5/day per IP). KB search in the browser is O(nodes) over 118 nodes, debounced.
- `gen_viz_v2.py` produces a self-contained 1.2 MB map; acceptable for a single-page graph.

**Token usage (Gemini, `promote.py`)**
- One call per promotion, `temperature 0.3`, structured-JSON output. The catalogue is sent
  as `id | type | label` (≈118 short lines) — this is the minimum needed for related-id
  selection and trimming it would hurt link quality. PDFs go inline (multimodal), avoiding a
  brittle extraction step. Token usage is already lean for the current design.

---

## Changes applied (this review)

| # | File | Change | Severity | Status |
|---|------|--------|----------|--------|
| 1 | `tools/promote.py` | **Prompt-injection fencing.** Untrusted submission text is now wrapped in explicit `BEGIN/END SUBMITTED CONTENT (untrusted data)` markers, with a SECURITY instruction telling the model to treat all submission metadata + content (and the PDF) as **data, never instructions**. | LOW (human PR gate already backstops) | ✅ applied + tested locally |
| 2 | `tools/gen_viz_v2.py` | **XSS hardening on the public map.** `marked@12` does **not** sanitize HTML; raw HTML in a node body would execute on the live Pages site. Added DOMPurify (**fail-closed** fallback) and wrapped `marked.parse(...)` → `DOMPurify.sanitize(...)` before `innerHTML`. Regenerated `docs/map.html`. | MEDIUM (public site; the promotion pipeline is designed to ingest outside content into bodies) | ✅ applied + map regenerated |
| 3 | `proxy/worker.js` | **(a)** `Content-Length` guard (`MAX_BODY = 3 MB`) rejecting oversized bodies *before* `request.json()`; **(b)** base64 size estimate now subtracts padding so the 2 MB file bound is exact. | LOW | ✅ code applied; **needs `wrangler deploy` to go live** |

### Verification performed
- `promote.py`: `py_compile` clean; unit-tested `build_prompt` (fence present, catalogue
  embedded, PDF note correct), `assemble` (hallucinated id dropped, node well-formed, fence
  does not leak into the body), `fix_escapes` regression (literal-`\n` repaired, healthy
  output untouched).
- `gen_viz_v2.py`: build parity intact (118/1,121, 0 body diffs); `DOMPurify.sanitize(...)`
  call present in regenerated `map.html`; fallback is **fail-closed** (no sanitizer -> plain
  text, never raw HTML). The exact CDN file (`dompurify@3.1.6`) returns HTTP 200 and is the
  genuine library; its `sanitize()` was run on the supported backend and **strips** `onerror`,
  `<script>`, `javascript:` URLs and `<iframe>` while **preserving** legit markdown HTML
  (`<b>`/`<h2>`/`<code>`). Scanned all node bodies — **zero** real HTML tags / event handlers /
  `javascript:` URLs, so nothing legitimate is stripped (transparent for current content).
- `worker.js`: 21/21 inline regression tests pass against the named exports — including the
  exact 2 MB / 2 MB+1 base64 boundary, path-traversal stripping, PII flagging, and all reject
  paths.

---

## Deliberately left unchanged (with reasons)

- **Parallelize blob/ref in `commitFile`** — saves ~1 RTT but adds failure modes to a working
  flow on a live endpoint. Not worth it at this volume.
- **Rate-limit-before-Turnstile reorder** — marginal; current order is defensible and a
  rate-limited request costs only a Turnstile verify, not a write.
- **KV read-then-write race** — eliminating it needs Durable Objects; the limiter is
  documented as soft and Turnstile is the hard gate. Leave.
- **Full catalogue per Gemini call** — already minimal (`id | type | label`); trimming hurts
  related-id quality. Token usage is lean.
- **`Content-Length` guard is bypassable** (a client can omit the header) — it stops only
  honest oversized bodies; CF platform limits + `validate()` are the real bounds. Kept as
  cheap defense-in-depth, not a primary control.

---

## Scale caveat (honest scope note)

These conclusions are optimized for the **current low-volume, single-operator** design
(≤5 submissions/IP/day, manual `promote.py` per contribution). If volume grows materially,
the calculus changes and these become worth revisiting:
- catalogue-per-call tokens and one Gemini call per promotion (batch / cache the catalogue),
- sequential GitHub API calls in `commitFile` (parallelize / retry on ref races),
- KV soft rate-limit (move to Durable Objects for exactness),
- a GitHub Action to run `promote.py` unattended on an `approved` label.

Nothing here is needed today.

---

## To make change #3 live

The worker edits are in `proxy/worker.js` but only take effect after a redeploy:

```bash
cd proxy && npx wrangler deploy
```

Changes #1 (promote.py) and #2 (gen_viz_v2.py + regenerated map.html) are local; #2 publishes
to the live site on your next commit + push (Pages rebuilds).
