# DBA Knowledge Base — Product Vision (Capture v0.1)

> **Status:** Capture v0.2 from whiteboard sketch (2026-06-25). Faithful read-back of the
> hand-drawn mind-map, **with direction decided** (see §9). Items marked `?` are
> illegible/uncertain in the source image — confirm or correct.
>
> **Important framing:** The sketch is a *brainstorm mind-map*, not a prioritized spec.
> Turning it into a "proper project" requires decisions the sketch does not make
> (priorities, phases, ownership, scope boundaries). Capturing ≠ committing to build all of it.

---

## 1. The Core Idea

A pipeline that turns **DBA course material** (from UpGrad / GitHub) into a structured,
AI-augmented, **open knowledge base** published to a public GitHub organization — with
quality controls, a usable UI/UX, a contributor community, and a marketing/teaching layer
around it.

Mental model — a three-stage pipeline with cross-cutting workstreams:

```
   SOURCE  ───────▶  PROCESSING  ───────▶  DESTINATION
 (ingest raw)      (enrich + structure)   (publish + engage)
        ▲                  │                     │
        └──── FEEDBACK LOOPS ◀────────────────────┘
   (collaboration · quality · marketing · teaching run across all three)
```

The system at the center: **AI + DBA Knowledge Base**, expressed in **OKF**
(Open Knowledge Format).

---

## 2. Colour Legend (inferred from the sketch)

| Colour | Meaning (inferred) |
|--------|--------------------|
| **Pink** boxes | Major pipeline stages — SOURCE, PROCESSING, DESTINATION, STRUCTURE |
| **Yellow** highlight | Cross-cutting workstreams — Collaboration, Feedback Loops, Explorations, Marketing, Teaching, Assets |
| **Purple** highlight | Personas / Quality — Persona, Quality |
| **Blue** | Core system — AI · DBA · Knowledge Base |

---

## 3. SOURCE — Ingest raw material

**Inputs**
- → UpGrad content
- → GitHub
  - → Sources folders (raw)
  - → Processed content

**Content TYPES**
1. Transcripts
2. Slides, PDFs
3. YouTube videos
4. References
5. `?` (5th type — illegible; possibly Notes / Assignments)

**ENRICHMENT**
- ✓ Cohort-8 — Slot-1
- Cohort-8 — Slot-2
- `?` (a faint hand-drawn grid/matrix sits here — possibly an enrichment-tracking table per cohort/slot)
- → produces **ASSETS**

**COLLABORATION** (workstream)
1. Source content
2. GitHub — open-source project

**FEEDBACK LOOPS** (workstream)
- `?` (called out as its own box; mechanism not detailed in sketch)

---

## 4. PROCESSING — Enrich, structure, control quality

- ■ **Dedupe**

**ORCHESTRATION**
- Loop routine (a repeatable processing loop / batch routine)

**TECHNOLOGIES**
- **OKF** (Open Knowledge Format) — the canonical schema/destination
- **AI · DBA · Knowledge Base** (blue core box) — the AI layer over the DBA corpus
- Cohort-8 Slot-1 / Slot-2 (the working dataset)

**QUALITY** (purple)
- Evals
- UI / UX

**EXPLORATIONS** (workstream — experimental, likely not committed scope)
- ■ Google Agent / Web-Agents
- ■ AIR `?`
- Website — interactive
  - Email → Prompt injection `?` (a risk/technique to handle, not a feature?)
  - PR

---

## 5. DESTINATION — Publish & engage

**STRUCTURE** (pink — the published knowledge graph shape)
- Courses
- Sessions
- Concepts
- References
- → Assignments
- → Submissions

**Publishing target**
- GitHub **Organization** (public/open-source home)

**PERSONA** (purple)
- User
- Contributor

**MARKETING** (workstream)
- ■ Engagement
- → Audiences → DBA Cohorts

**Asset / deliverable roadmap** (right-edge list — order as drawn)
- → Train
- → Hyperframes `?`
- → ElevenLabs (audio / podcast generation)
- → README
- → Architecture
- → OKF
- → **Teaching** (highlighted — teaching materials as an output)

---

## 6. Personas

| Persona | Need (inferred) |
|---------|-----------------|
| **User** | Study the DBA knowledge base — read, search, navigate, learn (the viz/UX we've been building) |
| **Contributor** | Add/enrich/correct content via the open-source GitHub project; feedback loops |

---

## 7. Open / Uncertain items (please confirm)

These are either illegible in the photo or under-specified in the sketch:

1. **5th content TYPE** — what is it?
2. **ENRICHMENT grid** — the faint table: what does it track (cohort × slot × asset?)
3. **FEEDBACK LOOPS** — what is the actual mechanism (issues/PRs? email? in-app?)
4. **"AIR"** — tool/concept under Explorations?
5. **"Hyperframes"** — deliverable on the right edge — what is it?
6. **Prompt injection** under Website/Email — a *threat to defend against*, or a *technique to use*?
7. **"Train"** — train what (a model? embeddings? fine-tune)?

---

## 8. From mind-map to managed project (recommendation — flagged as such)

The sketch maps cleanly onto **6 workstreams**. Proposed structure for long-term management:

| # | Workstream | Owns (from sketch) |
|---|-----------|--------------------|
| W1 | **Ingestion** | Source types, UpGrad/GitHub pull, raw→processed folders |
| W2 | **Enrichment & Processing** | Dedupe, orchestration loop, cohort/slot enrichment, assets |
| W3 | **Knowledge Base (OKF core)** | OKF schema, AI layer, structure (courses→submissions) |
| W4 | **Quality & UX** | Evals, UI/UX, the viz/website |
| W5 | **Community & Collaboration** | GitHub org, contributors, feedback loops |
| W6 | **Growth** | Marketing, engagement, teaching, audio/ElevenLabs |
| (X) | **Explorations** | Time-boxed experiments — Google agents, AIR, web-agents |

**Recommended formal artifacts** (to create once vision is confirmed):
- `PRODUCT_VISION.md` (this) — the why + the map
- `ARCHITECTURE.md` — the technical system (pipeline, OKF, AI layer)
- `ROADMAP.md` — phased plan across W1–W6
- `docs/` per-workstream specs
- GitHub: org structure, repo layout, `CONTRIBUTING.md`, issue/PR templates (feedback loops)

> **Counter-point (steelman against formalizing now):** this is still a solo research
> effort with a working corpus and a viz. Heavy project scaffolding (6 workstreams, org,
> contribution templates) can become overhead that outpaces the actual work. A leaner
> alternative: one `VISION.md` + one `ROADMAP.md` with a single prioritized next milestone,
> and add structure only when a second contributor actually appears. Decide based on whether
> the near-term goal is *building the corpus* or *building the community around it.*

---

## 9. Decisions (resolved 2026-06-25)

| Decision | Choice |
|----------|--------|
| **Primary near-term objective** | **Ship the public KB** — structure the OKF DBA knowledge base and publish it to a GitHub organization. Pipeline + structure first. |
| **Explorations scope** | **Parked** — Google agents, AIR, web-agents, interactive website kept as a backlog, *out* of the committed roadmap. Lean scope. |
| **Audience** | **Public / DBA cohorts from day one** — design every artifact public-ready. Shapes UX, marketing, licensing. |
| **Vision artifact** | **HTML one-pager** (Claude design system) + an embedded **roadmap**. Source of truth = this markdown; `vision.html` = shareable artifact. |

### Shipping roadmap (focused on the public KB)

- **Phase 0 — Foundation (done):** OKF DBA bundle (106 nodes), v2 knowledge-map viz.
- **Phase 1 — Harden the KB:** complete `courses → sessions → concepts → references → assignments → submissions`; dedupe; close content gaps (e.g. C6/C7); enrich Cohort-8 slots.
- **Phase 2 — Quality & UX:** evals on content; polish the viz/site for public use.
- **Phase 3 — Publish:** GitHub **org** + repo layout, `README`, `ARCHITECTURE`, `CONTRIBUTING`, license, OKF spec docs.
- **Phase 4 — Public launch:** site live for DBA cohorts; engagement/marketing; feedback loops (issues/PRs).
- **Parked backlog:** Explorations — Google agents, AIR, web-agents; plus ElevenLabs audio & teaching materials (revisit post-launch).
