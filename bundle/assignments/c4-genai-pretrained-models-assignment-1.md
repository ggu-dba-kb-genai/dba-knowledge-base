---
type: Assignment
resource: null
title: 'C4 Assignment 1 — RAG-Based GenAI Solution Design'
description: Individual assignment to pick one knowledge-work task, judge how far GenAI
  can help, and conceptually design a RAG-based solution (knowledge base, prompts,
  components) with explicit limitations.
tags:
- genai-pretrained-models
- individual-assignment
- retrieval-augmented-generation
- prompt-engineering
- solution-design
timestamp: '2026-06-01'
---

**Course:** Generative AI & Pretrained Models (C4) · **Type:** Individual ·
**Total Marks:** 25 · **Length:** 1–7 pages (+ up to 3 pages of screenshots)

## Summary

The brief lists ten common jobs, each with one specific task and an associated curated
**knowledge base (KB)** and sample query (e.g., a legal assistant finding similar past
cases, a bank executive answering account questions, an insurance underwriter spotting
information gaps). Students pick **one** job/task and assess: *Can GenAI help — fully
(100%), mostly (≥80%), partly (≥40%), or hardly (<20%)?* They then explain **what GenAI
can and cannot do** for that task and how to build the solution (from scratch vs
fine-tuning vs prompting vs RAG), foreseeing problems of relying on GenAI versus a human.

The core task is to **conceptually design and architect prompts and a RAG-based GenAI
solution**, making explicit, defensible choices for tools and components such that the
solution can answer the sample queries from the KB, and stating all known limitations
(e.g., total cost of ownership, response time).

## Deliverable

A lucid note (1–7 pages) addressing the points above, optionally plus up to 3 pages of
solution/code screenshots. Content beyond the 7 + 3 page limit is not graded.

## Score distribution (20% each)

Detailing of KB and sample-query format · overall GenAI solution design · prompt and RAG
effectiveness enhancement · identification of solution limitations · effort to try the
solution on a platform (e.g., Azure OpenAI / ChatGPT / other).

## Rubric

| Criterion (out of 5) | Good (5–4) | Satisfactory (3–2) | Needs Improvement (1) | Did not address (0) |
| --- | --- | --- | --- | --- |
| Detailing of KB and sample-query format | Clear description of the KB and queries. | General background presented but specific KB/query not clearly stated. | Neither KB nor query specifics clearly stated. | — |
| Overall GenAI solution design | Approach clearly described, plus a clear method of estimating success. | Either the approach or the success-evaluation method is unclear. | Neither approach nor evaluation method clearly described. | — |
| RAG effectiveness enhancement | Technically correct solution. | Some gaps in the technical evaluation. | Solution is not technically correct. | — |
| Identification of solution limitations | Clearly stated limitations. | Satisfactory. | Basic level. | — |
| Effort to try the solution on a platform | Significant. | Medium. | Basic solution. | — |

## Related

- **Parent Course**: [GenAI & Pretrained Models](../courses/c4-genai-pretrained-models.md)
- **Follow-on**: [C4 Group Assignment — Business Problem Solved with GenAI](c4-genai-pretrained-models-group-assignment.md)
- **Concepts**: [Retrieval-Augmented Generation](../concepts/retrieval-augmented-generation.md), [Prompt Engineering and Context Learning](../concepts/prompt-engineering-context-learning.md), [Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md)
