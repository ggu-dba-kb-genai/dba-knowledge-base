# DBA Knowledge Base

> An open, AI-augmented knowledge base for a **Doctor of Business Administration (DBA)** program — six graduate courses on emerging digital technologies, machine learning, deep learning, generative AI, AI project design, and responsible AI — expressed in the **Open Knowledge Format (OKF)** and published as a navigable knowledge graph.

**🌐 Live site:** https://ggu-dba-kb-genai.github.io/dba-knowledge-base/
**🗺️ Knowledge map:** https://ggu-dba-kb-genai.github.io/dba-knowledge-base/map.html

---

## What this is

A structured, version-controlled corpus of doctoral-level AI/ML curriculum, modelled as a
knowledge graph. Every course, session, concept, and reference is a markdown file with
structured front-matter and cross-links — portable, diff-able, and readable both by humans
and by tooling.

| | Count |
|---|---|
| Courses | 6 |
| Sessions | 73 |
| Core concepts | 23 |
| Reference guides | 5 |
| Graph connections | ~1,044 |

### The six courses

| | Course | Focus |
|---|--------|-------|
| **C1** | Emerging Digital Technologies | IoT, cloud & HPC, neuromorphic computing, AR/VR, RPA, digital twins, blockchain |
| **C2** | Foundations of ML & AI | Classical ML, regression, clustering, time-series, model evaluation |
| **C3** | Deep Learning | Neural networks and modern deep architectures |
| **C4** | Generative AI & Pretrained Models | LLMs, pretraining/fine-tuning, transformers |
| **C5** | AI Project Design | Scoping and delivering AI initiatives in a business context |
| **C6** | Responsible AI | Fairness, accountability, transparency, security, governance |

---

## Repository layout

```
dba-knowledge-base/
├─ bundle/              The OKF knowledge base (source of truth)
│   ├─ courses/         Six DBA courses (C1–C6)
│   ├─ sessions/        Session syllabi & notes
│   ├─ concepts/        Cross-cutting concepts
│   ├─ references/      Technical reference guides
│   └─ index.md
├─ docs/                GitHub Pages site (served from main /docs)
│   ├─ index.html       Landing page
│   ├─ map.html         Interactive knowledge map
│   ├─ vision.html      Project vision one-pager
│   └─ okf-explained.html
├─ tools/
│   └─ gen_viz_v2.py    Generator: builds the interactive map from bundle/
├─ PRODUCT_VISION.md    Direction, workstreams, roadmap
├─ LICENSE              MIT (code & tooling)
└─ LICENSE-CONTENT.md   CC BY 4.0 (knowledge-base content)
```

---

## Browse the knowledge base

- **Online (recommended):** open the [knowledge map](https://ggu-dba-kb-genai.github.io/dba-knowledge-base/map.html) — click a course to expand its sessions, click any node for its full content (with typeset math).
- **In the repo:** read the markdown directly under [`bundle/`](bundle/), starting from [`bundle/index.md`](bundle/index.md).

## Open Knowledge Format

The corpus uses [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog), Google's
portable markdown schema for knowledge bases. Each node carries typed front-matter
(`type`, `title`, `description`, `tags`) and links to related nodes by relative path.
See [`docs/okf-explained.html`](https://ggu-dba-kb-genai.github.io/dba-knowledge-base/okf-explained.html)
for an overview.

## Regenerating the interactive map

The map (`docs/map.html`) is generated from `bundle/`:

```bash
python3 tools/gen_viz_v2.py
```

The page loads Cytoscape.js, marked.js, and KaTeX from CDN — an internet connection is
required to view it.

---

## Contributing

Corrections, enrichments, and new content are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).
Open an issue for errors or gaps; open a PR to add or improve content under `bundle/`.

## License

This project uses a split license:

- **Code & tooling** (everything under `tools/`, `docs/*.html` scaffolding, generators) —
  [MIT](LICENSE).
- **Knowledge-base content** (everything under `bundle/`) —
  [Creative Commons Attribution 4.0 (CC BY 4.0)](LICENSE-CONTENT.md). Reuse freely with attribution.

The OKF SDK used to build this corpus is © Google LLC, licensed under Apache 2.0, and is
**not** vendored here — see [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog).
