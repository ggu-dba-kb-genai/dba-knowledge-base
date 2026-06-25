---
type: Session
resource: https://www.youtube.com/watch?v=hDR1TvYE8Xo
title: 'Session 07: AI Sourcing Strategy — Build vs. Buy vs. Partner vs. Platform'
description: An executive-level exploration of strategic sourcing models, architectural
  trade-offs, fine-tuning mechanics like LoRA, and the construction of risk-adjusted
  decision matrices for AI project design.
tags:
- ai-sourcing
- build-vs-buy
- fine-tuning
- lora
- risk-management
- tco
- ip-defensibility
timestamp: '2026-04-25'
---

This session guides students from the superficial excitement of polished, controlled vendor demos to the structured, pragmatic judgment required of executive decision-makers. It centers on the strategic "how to build" question rather than the "what to build," introducing four main sourcing configurations: **Build** (in-house development), **Buy** (packaged SaaS capabilities), **Partner** (external consultants/integrators working on your behalf), and **Platform** (managed cloud ecosystems with pay-as-you-go consumption models). Each route represents a different operating logic with distinct cost structures, ownership boundaries, and operational risks.

To bridge the technical and business domains, the lecture provides a structural breakdown of model adaptation, explaining why full retraining leads to *catastrophic forgetting* by overwriting all learned weights across a model's network. The session details parameter-efficient methods, specifically **LoRA** (Low-Rank Adaptation), which freezes the base model's weights and appends tiny auxiliary layers (<1% parameter growth) to preserve general reasoning while safely embedding domain-specific intelligence. Students explore evaluation criteria such as 3-year Total Cost of Ownership (TCO), IP and defensibility (focusing on custom workflows, prompt engineering assets, and synthetic data rather than generic base algorithms), and construct a board-ready *Risk-Adjusted Decision Matrix* aligned with prominent industry standards.

Finally, the class explores real-world consulting pain points and solutions. These include bridging pure-play data science with domain expertise to prevent "spurious correlations," bypassing enterprise data privacy restrictions through the generation of pattern-resembling dummy datasets, and implementing Human-in-the-Loop auditing tools to measure active refinement versus blind developer acceptance in AI-assisted development lifecycles.

# Key Concepts

- **Strategic Sourcing Models** — The core executive decision matrix evaluating Build (high control, custom IP, slower time-to-value), Buy (fast deploy, limited flexibility, vendor lock-in), Partner (external execution, diluted accountability, complex knowledge transfer), and Platform (managed scale, consumption-based, platform/roadmap dependency).
- **Retraining vs. Fine-Tuning** — A structural distinction where full retraining overwrites all parameters in [Neural Network Architectures](../concepts/neural-network-architectures.md), resulting in catastrophic forgetting of general reasoning capabilities. Conversely, [Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md) (particularly LoRA) freezes base parameters and introduces low-rank adapters (<1% parameter growth) to safely merge general intelligence with specific domain contexts.
- **Enterprise Wrappers** — Proxies hosted on corporate servers that intercept, filter, log, and audit prompts and token usage. The professor explicitly notes that this wrapper/firewall setup is structurally separate from [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md).
- **IP & Defensibility** — Framework for identifying patentable and proprietary AI assets, focusing on custom workflows, proprietary evaluation benchmarks, specialized prompt assets, and synthetic data generation techniques rather than pure generic model weights.
- **Risk-Adjusted Decision Matrix** — A board-ready evaluation tool designed under [AI Governance and Compliance](../concepts/ai-governance-compliance.md) principles to systematically score sourcing choices against competing organizational priorities (e.g., speed, control, cost, scalability, and compliance).
- **Domain vs. Data Science Gap** — A practical critique of pure-play data science pipelines, emphasizing the critical role of domain experts (e.g., in pharma, HR, finance, or automotive) to prevent spurious correlations during [Model Evaluation and Validation](../concepts/model-evaluation-validation.md).
- **Dummy and Synthetic Data** — Utilizing [Generative Modeling](../concepts/generative-modeling.md) to craft high-fidelity proxy datasets that replicate organizational data patterns, resolving legacy enterprise privacy and data-sharing constraints.
- **Human-in-the-Loop (HITL) Software Auditing** — Auditing developer interaction with generative systems by tracking metrics (e.g., direct submit clicks vs. active modification of AI-generated requirements) to establish robust [Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md).

# Topics Covered

1. **The Impressive Demo Trap** — Why polished vendor demos look exceptional in controlled settings but obscure down-the-line integration burdens, compliance gaps, lack of customization, and rising scaling costs.
2. **Parameters & Neural Network Scaling** — A step-by-step walkthrough calculating parameters (45 weights and biases) for a toy 10-node neural network to contrast with the complexity of managing trillion-parameter foundation models.
3. **The Four Sourcing Logics** — Structural comparison of Build, Buy, Partner, and Platform models across hosting environments, capability fits, lock-in risks, and total costs.
4. **The Sourcing Evaluation Lenses** — Defining 3-year TCO projections (development vs. scaling), lock-in metrics, defensibility (IP strength), speed vs. control trade-offs, and compliance constraints.
5. **Constructing the Risk-Adjusted Decision Matrix** — Practical breakout exercise applying weighted scoring to common use cases: Enterprise Knowledge Assistant, HR Policy Co-pilot, and Quality Inspection AI.
6. **Industry Risk and Governance Frameworks** — Introduction to external regulatory and architecture resources including the MIT AI Risk Index, NIST AI RMF, ISO/IEC 42001, OECD guidelines, Microsoft CAF, and AWS Well-Architected Generative AI Lens.
7. **Realities of AI Consulting** — Navigating data-sharing hurdles, dry runs, and using python-based data cleaning libraries to prep datasets before fine-tuning.

# Materials

- **Slides**: 
  - `Session 7 - (25 Apr 2026).pdf`
  - `Session07_Slides_2026-04-25.pdf`
- **Chat**: Present and active during live discussion.
- **Recording**: YouTube video with ID [hDR1TvYE8Xo](https://www.youtube.com/watch?v=hDR1TvYE8Xo).

# Related

- Part of the **[AI Project Design](../courses/c5-ai-project-design.md)** course.
- Sibling Sessions:
  - Prior Session: **[Session 06](c5-ai-project-design-session-06.md)**
  - Next Session: **[Session 08](c5-ai-project-design-session-08.md)**

# Citations

1. Video Recording: [https://www.youtube.com/watch?v=hDR1TvYE8Xo](https://www.youtube.com/watch?v=hDR1TvYE8Xo)
2. MIT AI Risk Repository, Massachusetts Institute of Technology.
3. NIST AI Risk Management Framework (NIST AI RMF 1.0 + NIST AI 600-1 GenAI Profile), National Institute of Standards and Technology. [NIST.AI.100-1](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) / [NIST.AI.600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
4. ISO/IEC 42001: Information Technology — Artificial Intelligence — Management System, International Organization for Standardization.
5. OECD Due Diligence Guidance for Responsible AI, Organisation for Economic Co-operation and Development.
6. Together AI Platform (together.ai).
7. Transformer Explainer, Polo Club of Data Science, Georgia Institute of Technology (poloclub.github.io/transformer-explainer/).
