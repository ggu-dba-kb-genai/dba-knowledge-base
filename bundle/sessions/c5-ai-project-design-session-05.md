---
type: Session
resource: https://www.youtube.com/watch?v=f8z5eR-1XDY
title: 'Session 05: Agile AI, Dual-Track Discovery, and Managing Uncertainty'
description: This session introduces the Agile AI framework, proposing a dual-track
  engine (Discovery and Delivery) to manage the inherent probabilistic uncertainty
  of machine learning projects.
tags:
- agile-ai
- project-management
- dual-track-agile
- model-drift
- stage-gates
- validation-gates
timestamp: '2026-04-18'
---

Traditional software engineering requirements focus primarily on reducing **ambiguity**—clarifying *what* features to build. In AI project design, however, even a perfect requirements document (as structured in [Session 04](c5-ai-project-design-session-04.md)) cannot eliminate **uncertainty**. Because AI systems are inherently probabilistic, they are subject to inconsistent outputs, model behavior anomalies, and data dependencies. To address this mismatch, this session introduces **Agile AI**, a project management framework structured to manage uncertainty rather than merely tracking feature velocity. 

The core of Agile AI is a dual-track engine that separates learning from scaling:
1. **The Discovery Track** uses an *Experiment Backlog* to answer the fundamental question: *Should we build this?* This phase is heavily hypothesis-driven and focuses on validating data usability, designing prompt structures, and evaluating model performance constraints without heavy coding.
2. **The Delivery Track** uses an *Implementation Backlog* to address *How do we build this?* Once discovery yields a validated, high-confidence prototype, the delivery track scales the solution, managing systems integration, access control, logging, rollout, and user training.

To coordinate these tracks and manage client commitments, projects must pass through sequential **Stage Gates** (Discovery Feasibility Gate, Pilot Adoption Gate, and Production Business Value Gate) supported by evidence. The session also addresses the challenges of traditional client contracts in IT services—proposing outcome-based engagement models or co-investment discovery phases to mitigate financial risk before signing deterministic SLAs for probabilistic systems. Finally, the class discusses post-deployment maintenance, highlighting how to leverage audit logging to detect **Model Drift** and distinguishing between model retraining and diagnostic rerunning.

# Key Concepts

- **[AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md)** — The framework governing the transition from a research-focused discovery track to scalable production systems, including feedback loops that feed real-world user metrics back into discovery.
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)** — Establishing concrete evaluation rubrics, tracking metrics (precision, recall, F1, and accuracy), and identifying model-specific failure rates during the experiment backlog.
- **[Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)** — Highlighted as a solution to reduce model hallucinations and keep responses grounded in facts, which is especially critical in highly regulated environments like pharmaceutical assistants.
- **[Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md)** — Described as a "thinking-heavy, low-code" activity in the discovery track, where system prompts are designed, tested, and potentially structured as JSON prompts to ensure stable outputs.
- **[Bias, Fairness, and Alignment](../concepts/bias-fairness-alignment.md)** — Emphasized through real-world edge cases where facial search features discriminated or misaligned when presented with unexpected inputs (e.g., chimpanzee images uploaded to a human matrimonial facial match system).
- **[Computer Vision](../concepts/computer-vision.md)** — Relevant to the deep learning and image-processing pipelines in both matrimonial lookup systems and automotive manufacturing defect inspection models.
- **[AI Governance and Compliance](../concepts/ai-governance-compliance.md)** — Critical for region-specific rules (such as European Union vs. Indian compliance frameworks) and medical-grade data auditing standards.
- **[Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md)** — Designing fallback options, human-in-the-loop overrides, and safety thresholds to protect against catastrophic AI failures.
- **[Dimensionality Reduction and Feature Extraction](../concepts/dimensionality-reduction.md)** — Explored as a pre-processing method when executing feature selection, using methods like Principal Component Analysis (PCA) and Variance Inflation Factor (VIF) to assess data readiness.
- **[Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md)** — Discussed in the context of data sufficiency checks to avoid model overfitting or underfitting when clients provide limited records.
- **[Generative Modeling](../concepts/generative-modeling.md)** — Evaluated as an approach to produce synthetic data when real-world production datasets are scarce or highly proprietary.
- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — Explores the baseline requirements for model training, including evaluating quantity and quality of features before progressing past the discovery gate.

# Topics Covered

- **Traditional Agile vs. Agile AI**: Contrast feature velocity with learning velocity. Sprint shifts from "output" to "learning + output". Backlogs change from feature-driven to hypothesis-driven. "Done" transitions from "working feature" to "validated behavior".
- **The Dual-Track Architecture**:
  - **Discovery Track (Experiment Backlog)**: Focuses on "Should we build this?". Hypothesis testing, data feasibility, prompt engineering, evaluation metrics, and edge-case identification.
  - **Delivery Track (Implementation Backlog)**: Focuses on "How do we build this?". Technical integration, security/access, operational readiness, and human adoption/readiness.
- **Data Sufficiency and Pre-Processing Checks**:
  - Identifying if a dataset is sufficient in both quantity (records) and quality (features).
  - Feature selection and dimensionality reduction techniques, such as Principal Component Analysis (PCA) and Variance Inflation Factor (VIF).
  - Managing overfitting and underfitting. When datasets are limited, developers can leverage open-source options (e.g., Kaggle) or utilize generative models to produce synthetic data.
- **Maturity Stages & Stage Gates**:
  - **Discovery Stage (Feasibility Gate)**: Technical validation. Proving model viability on small-scale/prototype data.
  - **Pilot Stage (Adoption Gate)**: Workflow validation. Real-world user trust, adoption, and system integration testing in a constrained environment.
  - **Production Stage (Business Value Gate)**: Scaling safely. Measuring actual KPI impact, defining SLAs, and implementing runtime guards.
- **Model Drift vs. Badly Trained Models**:
  - *Badly trained models* consistently give unexpected or poor answers right from deployment.
  - *Model drift* occurs post-deployment when the model's accuracy degrades or its hallucination rate climbs over time.
  - Detection relies on continuous audit logging and comparing metrics.
  - *Retraining* updates model weights based on new incoming data patterns.
  - *Rerunning* involves running the model on the same historical benchmark data for diagnostic audit validation.
- **Consulting Contracting Realities**:
  - Selling AI under traditional, rigid, deterministic fixed-price contracts vs. outcome-based pricing models.
  - Proposing alternative approaches: reducing sales travel budgets to self-fund an upfront, 1-month discovery/prototyping phase (minimizing delivery risk before final contract sign-off).
- **Case Studies & Breakout Exercises**:
  - **Pharma Medical Information Assistant**: Compliance risk in highly regulated domains, multilingual complexity (referencing the Microsoft Persian "vegetative electron microscopy" error), and the role of RAG in preventing hallucinations.
  - **Automotive Defect Inspection**: Handling accuracy risks, production-line sensor inconsistencies, and false positive/negative rates.
  - **Airline Disruption Assistant**: Real-time decision-making, handling traffic surges (volume peaks) during cancellations/delays, routing/rebooking logic, and minimizing system latencies.
  - **Matrimonial Photo Search**: Exploring edge-case alignment failures where a chimpanzee photograph output lookalike human profiles, highlighting testing gaps and discrimination risks.

### 3-Sprint Execution Plan Template

To put Agile AI into practice, students mapped out a 3-sprint execution plan combining both backlogs:

| Sprint | Stage | Experiment Backlog Work | Implementation Backlog Work | Objective | Metric | Decision |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Sprint 1** | Discovery | Test accuracy and hallucination rate | Setup minimal infrastructure and data pipelines | Validate technical feasibility of the model | Recall $\ge 95\%$ (or Accuracy $\ge 85\%$) | **Continue** if met; **Iterate** if close; **Kill** if unsafe/failed. |
| **Sprint 2** | Pilot | Real-world validation control experiments | Deploy and integrate with existing workflows (e.g., CRM or Factory line) | Test user adoption and operational workflow trust | User trust score / adoption rate $\ge 70\%$ | **Continue** to scale; **Iterate** on workflow UI; **Kill** if rejected. |
| **Sprint 3** | Production | Continuous drift monitoring | Deploy full scaling, audit logging, compliance gates | Scale system safely to production levels | Zero compliance violations; target business KPIs met | **Deploy** fully; **Iterate** on optimization; **Stop** if SLAs fail. |

# Materials

- **Slides**:
  - `Session 5 - (18 Apr 2026).pdf`
  - `Session05_Slides_2026-04-18.pdf`
- **Chat**: Present (including student discussions about Accenture's risk models, Microsoft's Persian translation bug, and synthetic data generation).
- **Video Recording**: YouTube Video `f8z5eR-1XDY`

# Related

- Part of [AI Project Design](../courses/c5-ai-project-design.md)
- Previous Session: [Session 04: Defining AI Requirements](c5-ai-project-design-session-04.md) — focused on converting vague project ideas into structured, measurable requirement documents.
- Next Session: [Session 06: Prompt Engineering](c5-ai-project-design-session-06.md) — focusing on writing system prompts, structured formats (like JSON prompts), and running diagnostic evaluations.

# Citations

1. Lecture Video: `https://www.youtube.com/watch?v=f8z5eR-1XDY`
2. The Scrum Guide (2020) - Official Scrum vocabulary, roles, events, and artifacts. https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf
3. Project Management Institute (PMI) - AI in Project Management guidance. https://www.pmi.org/standards/ai-in-projectmanagement
4. McKinsey & Company - "Most AI initiatives fail to scale due to lack of integration and adoption" reference on organizational alignment.
5. Harvard Business Review - "AI projects fail not because models don't work, but because organizations don't adapt" reference on technical vs. human readiness.
