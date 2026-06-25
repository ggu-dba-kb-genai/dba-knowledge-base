---
type: Session
resource: https://www.youtube.com/watch?v=yidgwHk8RnM
title: 'Session 09: AI Readiness & Execution Diagnostics'
description: This session covers frameworks and strategies for evaluating organizational,
  data, and workflow readiness before deploying AI systems, highlighting common hidden
  blockers and real-world failure modes.
tags:
- ai-readiness
- data-readiness
- workflow-maturity
- hidden-blockers
- guardrails
- lora-adapters
- bhashini
- failure-analysis
timestamp: '2026-05-02'
---

This session focuses on evaluating AI readiness and conducting execution diagnostics. Moving beyond pure model accuracy and impressive demos, AI readiness is defined as the ability to convert an AI model's output into concrete business action. The lecture outlines how to conduct a readiness diagnostic across six core dimensions (Data Readiness, Process Maturity, Integration Dependency, Stakeholder Ownership, Capability Readiness, and Operating Risk) to produce recommendations classified into three states: **Ready Now**, **Ready with Conditions**, or **Not Ready Yet**. It dispels the myth that data abundance equals data readiness, emphasizing usability and alignment with business processes over sheer data volume.

Additionally, the session explores specialized engineering topics through a lively classroom discussion. These include Parameter-Efficient Fine-Tuning (PEFT) using Low-Rank Adaptation (LoRA) for enterprise platforms, sovereign Indian language models, and guardrails for generative applications. The professor outlines how domain-specific adapters representing less than 1% of base model parameters can be attached to small, open-weight models (1B to 10B parameters) to enable low-latency, secure, and cost-effective local hosting. The class also discusses the Universal Language Contribution API (ULCA), the Param Bharat Hugging Face repositories, and India's Bhashini translation mission to handle multilingual code-switching and Indian English in conversational agents.

The lecture illustrates critical readiness failures through several real-world and hypothetical case studies. These include McDonald's AI drive-thru test with IBM (which struggled with accents and noisy environment integrations), Zillow's algorithmic home-buying program (which broke under operational and market realities), Google Flu Trends (overfitting to search query correlation rather than causation), IBM Watson for Oncology (trained on synthetic cases rather than real patient data), and Air Canada's chatbot tribunal case (highlighting missing policy grounding and output guardrails). Finally, the class analyzes an ongoing project from the Center for Brain Research (CBR) at IISc Bangalore on Alzheimer's early detection and an Internet of Medical Things (IoMT) ecosystem to highlight the necessity of end-to-end input and output guardrails, human-in-the-loop validation, and continuous post-deployment observability.

# Key Concepts

- **[AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md)** — The structured evaluation of AI readiness forms the transition phase between pilot prototyping and scaling within production environments, requiring continuous post-deployment observability to manage model drift and behavior changes.
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)** — Assessing data quality through metrics (consistency, completeness, uniqueness) and evaluating real-world validation data rather than relying solely on synthetic or training datasets.
- **[Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md)** — Designing input/output validation, fallback mechanisms, human oversight, and safety filters to prevent hallucinations and jailbreaking (e.g., prompt injection bypasses).
- **[Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md)** — Leveraging Parameter-Efficient Fine-Tuning (PEFT) techniques like Low-Rank Adaptation (LoRA) to train lightweight domain adapters (representing <1% of base model parameters) on specialized enterprise data (SOPs, logs) for local hosting and low-latency execution.
- **[Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)** — Grounding models using curated policy databases to prevent hallucinations and ensure accurate factual retrieval (e.g., policy updates, customer support information).
- **[Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md)** — Coordinating multi-agent frameworks and self-monitoring data pipelines to detect system failures or network anomalies in complex IoMT (Internet of Medical Things) ecosystems.
- **[AI Governance and Compliance](../concepts/ai-governance-compliance.md)** — Applying risk management frameworks (e.g., NIST AI RMF, ISO 23894) to ensure auditability, safety, and regulatory compliance.
- **[AI Security and Robustness](../concepts/ai-security-robustness.md)** — Managing runtime vulnerabilities, preventing model output jailbreaks (such as creative roleplay bypasses), and securing critical backend pipelines.

# Topics Covered

- **The Six Dimensions of Readiness**:
  1. *Data Readiness*: Usability, relevance, accessibility, currentness, structure, permissioning, and auditability rather than sheer data volume. "Data risk is the #1 killer of AI projects."
  2. *Process Maturity & Workflow*: Assessing whether existing workflows are stable and clearly defining where the AI output sits in the loop. "AI that doesn't enter a workflow is just a report."
  3. *Integration Dependencies*: Identifying complex backend requirements (APIs, logging, exception handling, data movement, legacy systems) behind simple user interfaces.
  4. *Stakeholder Ownership*: Mapping clear roles for business sponsors, data owners, workflow owners, and post-deployment support teams.
  5. *Capability Readiness*: Evaluating internal technical skills, managing change resistance, and contrasting transitional training with assembling new "AI native" teams.
  6. *Operating Risk & Controls*: Establishing active guardrails, fallback options, and continuous observability pipelines to manage edge cases.
- **Diagnostic Outcome States**: Defining the criteria for *Ready Now*, *Ready with Conditions* (which requires documented gap-fixation methods, risk assessments, and timelines), and *Not Ready Yet* (deferring implementation until blockers are resolved).
- **Failure Mode Case Studies**:
  - *McDonald's AI Drive-Thru (with IBM)*: Failed in real-world public deployment due to failure in capturing different accents and handling high ambient noise.
  - *Zillow Offers*: Real estate algorithmic buying failure driven by operational realities (delays in repairing/reselling homes) and underestimating market volatility.
  - *Google Flu Trends*: Overfitting search correlation data without integrating traditional surveillance data (causation) like CDC reports.
  - *IBM Watson for Oncology / MD Anderson*: Clinical system trained on limited synthetic cases instead of real patient data, producing unsafe treatment recommendations.
  - *Air Canada Chatbot*: Tribunal case triggered by a conversational agent hallucinating/giving incorrect bereavement policy details due to lack of groundings or guardrails.
- **Specialized Engineering & Platform Architectural Decisions**:
  - *Sovereign AI & Indian Language Models*: Utilizing India-centric open-source datasets (ULCA), Hugging Face repositories (Param Bharat), and translation models like Bhashini to handle multi-lingual code-switching.
  - *LoRA Adapters for Enterprise Platforms*: Building highly specific adapters (e.g., trained on medical device Standard Operating Procedures) attached to small, open-weight base models (1B to 10B parameters) to enable low-latency, secure, and cost-effective local hosting.
  - *Classroom Projects*: Discussion of early Alzheimer's detection using brain biomarkers (MRI scan hyperparameters) at the Center for Brain Research (CBR) at IISc Bangalore and an Internet of Medical Things (IoMT) ecosystem.

# Materials

- **Slides**: 
  - `Seesion9.pdf`
  - `Session 9 - (2 May 2026).pdf`
- **Chat**: Present and active (focusing on assignment details, peer support, and domain experience exchange).
- **Recording**: Available under ID `yidgwHk8RnM`.

# Related

- Part of **[AI Project Design](../courses/c5-ai-project-design.md)**
- Previous Session: **[Session 08: Build vs. Buy Decisions](c5-ai-project-design-session-08.md)**
- Next Session: **[Session 10: Budgeting & Cost of AI Projects](c5-ai-project-design-session-10.md)**

# Citations

1. Course Lecture Recording: `https://www.youtube.com/watch?v=yidgwHk8RnM` (Session 9, 2 May 2026).
2. Microsoft Corporation, "AI Planning Guidance & AI Readiness Assessment".
3. Amazon Web Services, "AWS Well-Architected Framework: Machine Learning Lens & Generative AI Lens".
4. ISO/IEC 23894:2023, "Information technology — Artificial intelligence — Guidance on risk management".
5. NIST, "AI Risk Management Framework (NIST AI RMF 1.0)".
6. Bhashini, "National Language Translation Mission of India (ULCA Language Data Sets)".
