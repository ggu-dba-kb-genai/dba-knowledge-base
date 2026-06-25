---
type: Session
resource: https://www.youtube.com/watch?v=nN65MraAtQQ
title: 'Session 01: Course Overview & Under the Hood of LLMs'
description: An introduction to the Responsible AI course curriculum, the Darvin framework,
  and a comprehensive technical walkthrough of how Large Language Models are built
  and fine-tuned.
tags:
- responsible-ai
- embeddings
- attention
- transformers
- supervised-fine-tuning
- perplexity
- darvin-framework
timestamp: '2026-06-06'
---

The first session of the **Responsible AI** course introduces the course syllabus, team project structure, and the "Darvin" (Data, Algorithms, Responsibility, Infrastructure) conceptual framework for project governance. To establish a robust baseline before exploring ethical constraints and deployment failures, the core of the lecture is a thorough, technical walkthrough of the construction, training, and fine-tuning pipeline of Large Language Models (LLMs). 

The technical breakdown covers the transition of text from raw characters to binary-encoded tokens, semantic vector spaces, and positional embeddings. The instructor outlines the critical role of self-attention mechanisms—specifically the Query, Key, and Value vector transformations introduced in the landmark 2017 transformer paper—and maps how these components combine inside a transformer architecture with normalizations and soft-max operations to perform probabilistic next-token predictions. Additionally, the class explores pragmatic project design through a sales-automation technology case study focusing on the friction between lightweight contact managers (CloudContact) and enterprise-level automation tools (Salevation).

# Key Concepts

- **Darvin Framework** — A project governance framework detailing critical elements required for successful AI deployments: Data, Algorithms, Responsibility, and Infrastructure.
- **Sub-word Tokenization** — Splitting text into variable-length character groups (tokens) to balance dictionary size and vocabulary reuse, visualized using OpenAI's public Tokenizer tool and byte-pair encoding.
- [Embeddings and Vector Representations](../concepts/embeddings-and-representations.md) — Converting token IDs into continuous, dense semantic vectors across high-dimensional space (e.g., GPT-4's 12,288 dimensions), utilizing math properties to maintain near-orthogonality ($e^{cn}$) for conceptual separation (e.g., Google's Word2Vec paper).
- [Attention Mechanisms and Transformers](../concepts/attention-and-transformers.md) — Dynamically calculating context weights through Query (Q), Key (K), and Value (V) matrix transformations to influence next-token predictions as introduced in Vaswani et al. (2017).
- [Model Evaluation and Validation](../concepts/model-evaluation-validation.md) — Scoring model accuracy and predictability using metrics such as Perplexity ($1/\text{probability}$), where lower values indicate more confident predictions.
- [Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md) — Adapting base pretrained models into instruction-following assistants via Supervised Fine-Tuning (SFT).
- [Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md) — Training models using structured datasets generated via custom labeling interfaces (like OpenAI's Tick Tokenizer) under guidelines of truthfulness, helpfulness, and harmlessness.
- [AI Governance and Compliance](../concepts/ai-governance-compliance.md) — Analyzing how international regulations (like GDPR or Canadian AI guidelines) translate to architectural constraints in corporate deployments.
- [Explainable AI (XAI)](../concepts/explainable-ai.md) — The necessity of unpacking the black-box nature of deep neural networks to explain automated outcomes (such as credit approval rejections).
- [Bias, Fairness, and Alignment](../concepts/bias-fairness-alignment.md) — Examining the risk of model output bias when training on scraped web data, and the compounding loop when biased AI-generated content is published and subsequently fed back into future model training cycles.

# Topics Covered

- **Course Logistics & Milestones**:
  - Review of grading criteria and the two presentation milestones.
  - **Milestone 1 (June 27/28)**: Initial Prototype and Product Plan (15-minute team presentation with strict cutoffs).
  - **Milestone 2 (July 25/26)**: Final comprehensive project evaluation (30-minute team presentation).
  - No class scheduled on **June 28** due to instructor travel.
- **Why AI Transformation Fails**: 
  - Industry data reveals that 70% of AI projects fail as prototypes and 20% fail as products, leaving only 10% (or as low as 5% according to MIT studies) delivering true business value.
  - Non-model root causes: poor data selection, lack of workflow integration, and failure to define objective business metrics.
- **Technology Case Study: "Appealing Automation"**:
  - Interactive discussion focusing on Sally Patterson (president of ContactWare) and the transition from lightweight contact management software (CloudContact) to robust sales-automation tools (Salevation).
  - Persona analysis of the Sales Director (consolidating territory pipelines) and the Sales Representatives (Gwen, balancing chaotic schedules and quota pressures).
  - Designing a grassroots adoption positioning statement for Gwen.
- **The LLM Pre-training Pipeline**:
  - Scraping, cleaning, and filtering web text.
  - Curation heuristics: URL filtering, personal identifiable information (PII) removal, and language quality thresholds (requiring at least 65% English content).
  - Image tokenization via pixel-patch tiling.
- **Word Embedding Algebra**: Word2Vec vector mathematical properties (e.g., $\vec{\text{Uncle}} - \vec{\text{Man}} + \vec{\text{Woman}} = \vec{\text{Aunt}}$).
- **Self-Attention Mechanics**: Unpacking Vaswani et al.'s (2017) transformer model and the Query-Key-Value calculation to dynamically extract context.
- **Transformer Architectural Layers**:
  - Embedding layers and positional vectors.
  - Layer normalization using Z-transform scaling to a $[-3, +3]$ distribution.
  - Soft-max projections and Temperature parameters (balancing randomness vs. peak probabilities from $0.0$ to $1.0$; default is $0.5$).
- **Supervised Fine-Tuning (SFT)**:
  - Curating instruction datasets using human labelers.
  - Deep-dive into OpenAI's InstructGPT (2022) methodology, guidelines (helpful, truthful, harmless), and labeler demographics.
  - The "Tick Tokenizer" format for chat formatting ($\text{<|im\_start|>user}$, $\text{<|im\_start|>assistant}$).
  - Transition to synthetic data: using LLMs to generate QA datasets (e.g., Hugging Face UltraChat).

# Materials

- **Slides**: `Pre-read Case Study.pdf` (ContactWare & Salevation Technology Case Study)
- **Other Files**: `Zoom Tips.pdf`
- **Chat Transcript**: Yes, Zoom class chat active.
- **Video Recording**: Video available on YouTube with ID `nN65MraAtQQ`.

# Related

- **Parent Course**: [Responsible AI](../courses/c6-responsible-ai.md)
- **Next Session**: [Session 02: RLHF, Guardrails & Explainability](c6-responsible-ai-session-02.md)

# Citations

1. Course Lecture Video: `https://www.youtube.com/watch?v=nN65MraAtQQ`
2. Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). *Efficient Estimation of Word Representations in Vector Space*. arXiv preprint arXiv:1301.3781. [Word2Vec]
3. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). *Attention Is All You Need*. Advances in Neural Information Processing Systems, 30. [Transformer Architecture]
4. Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P. F., Leike, J., & Lowe, R. (2022). *Training language models to follow instructions with human feedback*. Advances in Neural Information Processing Systems, 35, 27730-27744. [InstructGPT]
