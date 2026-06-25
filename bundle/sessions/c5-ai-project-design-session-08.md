---
type: Session
resource: https://www.youtube.com/watch?v=cT1GhSzseNg
title: 'Session 08: RAG Architecture - Chunking, Vector Space, and Evaluation Metrics'
description: A deep dive into Retrieval-Augmented Generation (RAG) backend mechanics,
  comparing chunking strategies, embeddings, and establishing quantitative evaluation
  frameworks for accuracy, latency, and maintainability.
tags:
- RAG
- Chunking
- Sentence-Transformers
- Vector-Databases
- Model-Evaluation
- Latency
- Maintainability
- Explainable-AI
timestamp: '2026-04-26'
---

This session, led by Dr. Veena, serves as an in-depth exploration of the architectural backend and comprehensive evaluation frameworks for [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md). The lecture shifts focus from high-level orchestrator design to concrete implementation steps, addressing document preprocessing, chunking and splitting strategies, vector database storage, and similarity search. Through practical Python demonstrations using Hugging Face's `sentence-transformers` and Chroma DB, the session contrasts the performance of grounded RAG against direct language model generation, illustrating how retrieval context mitigates model hallucination and guides domain-specific behavior.

A major portion of the lecture is dedicated to formalizing a robust, multi-dimensional evaluation framework for RAG systems. Dr. Veena categorizes the necessary metrics into three distinct pillars: Accuracy (including retrieval metrics like Hit@5, Recall, Precision, MRR, and NDCG), Latency/Cost (tracking median and 95th percentile delays, prompt/completion token consumption, and caching performance), and Maintainability/Reliability (monitoring document drift, duplicate chunking ratios, and pipeline health). Additionally, the session highlights the trade-offs between different RAG typologies—Simple, Hybrid, and Agentic—demonstrating that while hybrid configurations (dense vector search combined with BM25 keyword matching and reranking) introduce significant latency overhead, they are mathematically justified when querying messy, large-scale, and heterogeneous corporate datasets.

Finally, the session bridges theory and industry practice by discussing real-world failure modes of non-audited AI systems (such as biased HR screening tools and unmaintained, toxic chatbots) and introducing transformer explainability techniques. The session concludes with details for an upcoming individual assignment where students act as evaluators of fictional vendor demo scripts, developing custom evaluation rubrics to assess technical feasibility, potential operational risks, and overall project alignment.

# Key Concepts

- **Document Splitting and Chunking Strategies** — The process of dividing continuous corpus documents into smaller, digestible segments (chunks) to respect LLM context constraints and ensure precise retrieval. Strategies include:
  - *Character Splitting:* Simple, arbitrary division based on raw character count; easy but risks cutting sentences abruptly and breaking semantic context.
  - *Recursive Character Splitting:* A structural splitter that hierarchically segments text using a sequence of delimiters (such as double newlines `\n\n`, single newlines `\n`, spaces, and individual characters) to keep related paragraphs together.
  - *Token Splitting:* Segmenting text based on exact token counts to tightly manage model context windows.
  - *Semantic Chunking:* An embedding-driven strategy where split boundaries are determined by analyzing changes in semantic meaning across sentences using [Embeddings and Vector Representations](../concepts/embeddings-and-representations.md).
  - *Document-Specific Splitting:* Custom rules mapping hierarchical formats (JSON, HTML, PDF tables, CSVs) directly into logical blocks without flattening their structure.
- **The Role of Overlap** — The practice of repeating a small percentage of trailing characters/tokens from the preceding chunk at the start of the next chunk. This carries over and preserves context across boundaries. Dr. Veena recommends keeping overlap small (ideally under 1% of the chunk size, e.g., less than 5 characters for a 500-character chunk).
- **Sizing Chunks vs. Context Length** — A structural rule of thumb: ensure that the underlying LLM's context window can accommodate at least 3 to 5 chunks at a time. For instance, with a model context length of 1024 tokens, individual chunks should not exceed 300 tokens to ensure the model has a multi-perspective view of the retrieval space.
- **Embeddings and Similarity Search** — Chunks are converted into dense, high-dimensional vector representations. Using the Hugging Face model `all-MiniLM-L6-v2`, chunks are mapped to 384-dimensional dense vectors stored in databases like Chroma or Pinecone. Similarity searches are executed via vector dot products or cosine similarity. To analyze these relationships visually, [Dimensionality Reduction](../concepts/dimensionality-reduction.md) techniques (specifically Principal Component Analysis or PCA) are applied to project the high-dimensional vector clusters onto a 2D plane.
- **RAG Evaluation Triad** — Standardizing RAG pipeline assessments across three critical dimensions:
  - **Accuracy & Retrieval Quality:** Quantified via retrieval metrics such as *Hit at 5 (Hit@5)* (ensuring at least one gold passage appears in the top 5 results; target: 0.80–0.90), *Recall* (relevance completeness; target: >0.80), *Precision* (relevance purity; target: >0.80), *Mean Reciprocal Rank (MRR)* (evaluating how early the correct document is found; target: >0.80), and *NDCG@5* (ranking quality). Generation metrics like groundedness, factual consistency, and faithfulness are tracked using specialized libraries like Ragas or DeepEval under the larger umbrella of [Model Evaluation and Validation](../concepts/model-evaluation-validation.md).
  - **Latency and Cost:** Tracking median (p50) and 95th percentile (p95) system response times (targeting p95 latency < 1 second). Financial cost is tracked per query by measuring input/completion tokens, embedding generator calls, and indexing/reranking operations, offset by caching efficiency.
  - **Maintainability and Reliability:** Monitoring system degradation over time by measuring duplicate chunking ratios, metadata coverage (date, versioning, PII flags), retrieval drift, and pipeline rebuild times.
- **RAG Typology Trade-offs (Simple vs. Hybrid vs. Agentic)** — Choosing the correct RAG architecture based on data complexity:
  - *Simple RAG:* Extremely fast (~24ms latency) and accurate on clean, homogenous textual documents.
  - *Hybrid RAG:* Integrates BM25 keyword matching with dense vector embeddings and reranking. It introduces substantial latency (~200ms) but is highly justified on large-scale (12,000+ docs), noisy, or heterogeneous datasets where exact keyword match and typo-tolerance are required to preserve precision.
  - *Agentic RAG:* Uses [Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md) to dynamically route queries and execute tool calls (such as external APIs), introducing higher costs and loop latency but offering maximum flexibility.
- **RAG vs. Fine-Tuning Decision Rules** — Determining when to use [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) versus [Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md) based on enterprise requirements:
  - *External/Dynamic Data:* RAG or API-based grounding is heavily preferred because fine-tuning cannot easily keep pace with private or rapidly changing external sources.
  - *Domain Adaptation:* Fine-tuning is preferred to internalize domain phrasing, tone, and logic (which can be combined with RAG for complex domain-specific Q&A).
  - *Hallucination Mitigation:* RAG reduces hallucinations by grounding responses in exact facts, whereas fine-tuning only teaches the model patterns and associations.
  - *Transparency:* RAG is highly explainable because retrieved chunks are traceable, whereas fine-tuning internalizes knowledge in a black-box parameter space.
  - *Latency:* Fine-tuning has lower inference latency because there is no retrieval step, whereas RAG adds latency overhead.
  - *Compute Constraints:* Parameter-Efficient Fine-Tuning (PEFT) like LoRA/QLoRA is effective for adapting models under constraint but lacks the live retrieval capabilities of RAG.
- **Model Explainability** — A brief review of [Explainable AI (XAI)](../concepts/explainable-ai.md) techniques such as SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) applied to transformer architectures to trace token-level attribution and explain why specific generation decisions are made.

# Topics Covered

- **Visualizing Chunking and Splitting:** Reviewing interactive visualizations (using chunk.com) to compare character, recursive character, and token-based splitting strategies.
- **Vector Space and Dimensionality Reduction:** Demonstrating how dense embeddings (384-dimensional vectors via `sentence-transformers`) are mapped, stored, and visualized in 2D space using PCA to verify semantic clustering.
- **RAG vs. No RAG Walkthrough:** Code demo of a grounded document processing pipeline (loading medical advice PDFs into Chroma DB, querying top-$k$ chunks, and feeding context to `TinyLlama-1.1B`) versus a zero-context model run to show how RAG prevents hallucination.
- **The Triad of RAG Metrics:** Detailed breakdown of formulas, targets, and acceptable bounds for Accuracy, Latency, Cost, and Maintainability.
- **Failure Modes of Untested AI:** Case studies of unmonitored AI systems, including biased recruitment tools (e.g., Amazon's historical hiring tool penalizing women's resumes), racist hardware sensors (soap dispensers failing dark skin tones), and toxic conversational agents (Microsoft Tay).
- **RAG Architecture Trade-offs at Scale:** Experimental results comparing Simple, Hybrid, and Agentic RAG under clean, noisy, and large-scale synthetic document corpuses.
- **Explainability in Transformers:** Brief code review of global and local feature importance via SHAP waterfall diagrams.
- **End-to-End Chatbot Demos:** Streamlining local document QA (with Gradio GUIs and Groq APIs) and demonstrating crawling and routing on external university NLP websites.
- **Evaluation Assignment Briefing:** Introduction to the individual assignment evaluating vendor demo scripts (e.g., AI HR co-pilot) using the learned evaluation metrics and establishing custom assessment rubrics.

# Materials

- **Chat Transcript:** A text chat log of student-instructor interactions, containing real-time questions regarding chunk overlaps, MongoDB vector searches, and custom evaluation libraries (DeepEval vs. Ragas).
- **Video Recording:** A YouTube recording of the live session (video ID: [cT1GhSzseNg](https://www.youtube.com/watch?v=cT1GhSzseNg)).
- *Note: No external slide deck or Jupyter Notebook files are registered in this session's metadata.*

# Related

- **Parent Course:** [AI Project Design](../courses/c5-ai-project-design.md)
- **Previous Session:** [Session 07: Vendor Evaluation & LLM System Integration](c5-ai-project-design-session-07.md)
- **Next Session:** [Session 09: System Performance Optimization & LLM Monitoring](c5-ai-project-design-session-09.md)

# Citations

1. Upgrad Course Lecture: *AI Project Design - Session 08*, April 26, 2026. Recording: `https://www.youtube.com/watch?v=cT1GhSzseNg`.
2. Reimers, N., & Gurevych, I. (2019). *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks*. arXiv preprint arXiv:1908.10084. (Introduces the Sentence-Transformers library used for the `all-MiniLM-L6-v2` dense embedding model).
3. Robertson, S., & Zaragoza, H. (2009). *The Probabilistic Relevance Framework: BM25 and Beyond*. Foundations and Trends in Information Retrieval, 3(4), 333-389. (Details the BM25 retrieval scoring model used in Hybrid RAG).
4. Shahul, E., et al. (2023). *Ragas: Automated Evaluation of Retrieval Augmented Generation*. arXiv preprint arXiv:2309.15217. (Defines the metrics used to measure RAG accuracy, groundedness, and faithfulness).
