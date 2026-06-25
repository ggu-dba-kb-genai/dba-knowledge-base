# Contributing

Thanks for helping improve the DBA Knowledge Base. This is an open knowledge project —
corrections, enrichments, and new content are all welcome.

## Ways to contribute

- **Report an error or gap** — open an [issue](https://github.com/ggu-dba-kb-genai/dba-knowledge-base/issues)
  describing the file and what's wrong or missing.
- **Improve content** — open a pull request editing files under `bundle/`.
- **Add a concept, session, or reference** — follow the OKF structure (below) and link it
  into the graph.

## Editing content

All knowledge lives under `bundle/` as markdown with YAML front-matter. A typical node:

```markdown
---
type: Concept            # Course | Session | Concept | Reference
title: Supervised Learning Foundations
description: One-sentence summary.
tags:
  - supervised-learning
  - regression
---

The body, in markdown. Link to other nodes by **relative path**, e.g.
[Time Series and Forecasting](../concepts/time-series-forecasting.md).
Math is written in LaTeX: inline `$R^2$` or display `$$ \hat{y} = \mathbf{w}^T\mathbf{x} $$`.
```

Guidelines:

- Keep `type`, `title`, and `description` accurate — they drive the graph and the map.
- Cross-link generously, using **relative paths** to other `.md` files in the bundle.
- Prefer clarity over volume. This is a study resource.
- Don't paste verbatim copyrighted material (e.g. third-party slides or transcripts).
  Contribute your own synthesis, summaries, and explanations.

## After editing

If you changed `bundle/` and want to preview the interactive map locally:

```bash
python3 tools/gen_viz_v2.py
```

You don't need to commit the regenerated `docs/map.html` in your PR — note in the PR that
content changed and a maintainer will regenerate it.

## Licensing of contributions

By contributing you agree that:

- contributions to `bundle/` (content) are licensed under **CC BY 4.0**;
- contributions to code/tooling are licensed under **MIT**;
- you have the right to contribute the material and it is your own work or properly attributed.
