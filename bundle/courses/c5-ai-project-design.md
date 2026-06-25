---
type: Course
resource: null
title: 'C5: AI Project Design'
description: A strategic course bridging the gap between algorithmic technicalities
  and business execution, detailing AI project strategy, prioritisation, requirements
  engineering, sourcing, and operational economics.
tags:
- AI Strategy
- Project Management
- Requirements Engineering
- Agile AI
- RAG Evaluation
- Prompt Engineering
- MLOps
- Cost Optimization
- AI Governance
timestamp: '2026-04-04'
---

A comprehensive, strategic course on the end-to-end planning, execution, and economic governance of artificial intelligence systems in enterprise environments. Designed specifically for senior managers, product leaders, and prospective doctoral candidates, the course bridges the gap between scientific model development and boardroom value realization.

## Course Overview

The curriculum is structured around the transition from a scientific, model-centric mindset to an executive, boardroom-ready mindset. Rather than focusing on coding algorithms, the course covers how to systematically align AI projects with business strategy, write rigorous requirements under probabilistic uncertainty, design rapid-learning agile workflows, choose optimal sourcing models (build vs. buy), evaluate complex retrieval architectures, diagnose data and workflow readiness, and enforce strict release quality controls and economic governance.

The instructional arc begins with defining good business-centric AI strategies and moves progressively through:
- **Prioritization and Prototyping:** Evaluating gain vs. pain via Fermi analysis and designing scientific experiments to validate critical assumptions before writing code.
- **Requirements and Agile Workflows:** Applying global requirements standards (ISO 29148) to probabilistic systems and managing uncertainty via dual-track Agile (separating Discovery and Delivery).
- **Core Engineering Patterns:** Masterclass sessions on [prompt engineering and in-context learning](../concepts/prompt-engineering-context-learning.md) (Zero-Shot, Few-Shot, CoT, ToT) and multi-dimensional [retrieval-augmented generation (RAG)](../concepts/retrieval-augmented-generation.md) evaluation.
- **Readiness and Release Governance:** Conducting deep diagnostics of data and legacy integrations, establishing layer-wise QA test plans under adversarial/stress conditions, and analyzing [AI lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md) economics, including total cost of ownership (TCO), unit economics, and AI ESG metrics.

---

## Sessions

- **[Session 01: AI Crush vs. AI Strategy](../sessions/c5-ai-project-design-session-01.md) (2026-04-04)** — Transitioning from an algorithmic to a boardroom mindset, learning to formulate robust business strategies instead of chasing vague AI hype ("crushes"). Focuses on the four-element strategy formula: identifying who you target, which decision is made, in what workflow, and using what business lever.
- **[Session 02: Prioritizing AI Initiatives](../sessions/c5-ai-project-design-session-02.md) (2026-04-05)** — Formulating value hypotheses by quantitatively estimating financial gain via Fermi analysis. Establishes the gain vs. pain rubric, assessing technology, data, and change readiness, while clarifying the boundaries between prototyping (hypothesis testing), piloting (working model), and Minimum Viable Products (MVPs).
- **[Session 03: Prototyping & Rapid Learning](../sessions/c5-ai-project-design-session-03.md) (2026-04-11)** — Deep dive into prototyping as a method to fail fast and learn rapidly. Focuses on isolating critical business, operational, and user acceptance assumptions, and designing scientific, reproducible experiments to validate them prior to software engineering.
- **[Session 04: AI Requirements Engineering](../sessions/c5-ai-project-design-session-04.md) (2026-04-12)** — Applying the ISO 29148 global standard to write rigorous requirements for non-deterministic AI systems. Details how traditional deterministic "features" translate into "outcomes under uncertainty," and covers drafting Business Requirement Documents (BRDs), Project Requirement Documents (PRDs), User Stories, and AI-specific Non-Functional Requirements (NFRs) like latency, cost per inference, [explainable AI (XAI)](../concepts/explainable-ai.md), and drift monitoring.
- **[Session 05: Agile AI: Discovery vs. Delivery](../sessions/c5-ai-project-design-session-05.md) (2026-04-18)** — Reframing Agile for AI projects by running dual-track pipelines. The *Discovery Track* focuses on reducing risk and resolving uncertainty (experiments, prompt design, initial evaluation), while the *Delivery Track* focuses on engineering, scaling, and deployment. Introduces separate experiment and implementation backlogs, with explicit feasibility, adoption, and value gates.
- **[Session 06: Prompt Engineering & In-Context Learning](../sessions/c5-ai-project-design-session-06.md) (2026-04-19)** — Understating [prompt engineering and in-context learning](../concepts/prompt-engineering-context-learning.md) as structured thinking and next-token optimization. Covers Zero-Shot, Few-Shot (with edge cases), Chain of Thought (CoT), Tree of Thoughts (ToT), Role-Based, and Reusable Prompt Templates, concluding with hands-on adversarial testing (prompt injection, jailbreaking) via Gandalf and Agent Breaker tools.
- **[Session 07: Sourcing Decisions: Build, Buy, Partner, or Platform](../sessions/c5-ai-project-design-session-07.md) (2026-04-25)** — Evaluating the trade-offs in AI sourcing operating models. Compares foundation models (wrappers) against [transfer learning and fine-tuning](../concepts/transfer-learning-fine-tuning.md) (LoRA, QLoRA, SFT) and proprietary in-house builds. Maps choices to executive criteria: Total Cost of Ownership (TCO), vendor lock-in, IP defensibility, speed, control, and regulatory compliance.
- **[Session 08: RAG Pipelines & Multi-Dimensional Evaluation](../sessions/c5-ai-project-design-session-08.md) (2026-04-26)** — Designing and evaluating [retrieval-augmented generation (RAG)](../concepts/retrieval-augmented-generation.md) systems. Compares Simple, Hybrid, and Agentic RAG models and tests chunking strategies (recursive, semantic) and overlaps. Evaluates pipelines across three core dimensions: Accuracy/Trust (Hit@5, MRR, Recall, Precision, Groundedness), Latency/Cost, and Maintainability/Reliability (frequently using frameworks like Ragas and DeepEval).
- **[Session 09: Readiness Diagnostics & Blocker Analysis](../sessions/c5-ai-project-design-session-09.md) (2026-05-02)** — Establishing readiness diagnostics to classify projects as "Ready Now," "Ready with Condition," or "Not Ready Yet." Examines data readiness (relevance and accessibility vs. simple abundance), workflow process maturity, legacy technical integrations (APIs, system access, legacy system overhead), and stakeholder capability. Evaluates real-world case studies (Zillow, McDonald's AI drive-thru, Google Flu Trends).
- **[Session 10: Release Readiness & Layer-Wise QA](../sessions/c5-ai-project-design-session-10.md) (2026-05-03)** — Structuring test strategies and checkpoints for probabilistic AI systems. Details layer-wise testing across the Model Layer (accuracy, F1-score, [bias, fairness, and alignment](../concepts/bias-fairness-alignment.md), [AI security and robustness](../concepts/ai-security-robustness.md)), System Layer (API reliability, latency), and Workflow Layer (business value, human review, fallback, rollback). Focuses on scenario-based testing, [human-AI collaboration and guardrails](../concepts/human-ai-collaboration-guardrails.md) (HITL, input/output validation, safe default responses), and post-release drift monitoring.
- **[Session 11: AI Cost Structures & Unit Economics](../sessions/c5-ai-project-design-session-11.md) (2026-05-10)** — Analyzing total cost of ownership (TCO) and unit economics of running enterprise AI. Highlights hidden operating costs (token economics, excessive context, repeated retries, verbose outputs), scaling bottlenecks, and value realization metrics. Discusses the environmental and social impacts of AI computing via AI ESG (Environmental, Social, Governance) scoring and carbon emissions modeling (CO2 per kilowatt-hour).

---

## Citations

1. **ISO/IEC/IEEE 29148:2018** — *Systems and software engineering — Life cycle processes — Requirements engineering*. This international standard defines the constructs of necessity, feasibility, unambiguity, verifiability, and traceability in requirement documentation, serving as the foundational reference for Session 04's requirements framework.
2. **MIT AI Risk Repository** — A comprehensive, curated database of artificial intelligence risks across technological, societal, and operational layers, used as a structural source for Session 09 and Session 10's adversarial and readiness diagnostic assessments.
3. **AWS Generative AI Lens** — *AWS Well-Architected Framework*. Provides guidelines on architectural pillars, data prep, cost structures, and operational reliability for GenAI systems, directly referencing the unit economics, token multipliers, and TCO layers detailed in Session 11.
4. **NIST AI Risk Management Framework (AI RMF 1.0)** — National Institute of Standards and Technology guidance on managing risks to individuals, organizations, and society, heavily referencing the model verification, fairness, bias mitigation, and observability patterns in Session 10.
5. **Microsoft Cloud Adoption Framework for Azure** — Guidance on landing zones, governance controls, and wrappers used as a reference point for corporate connect and platform-level wrapper options in Session 07 and Session 09.
6. **Bhashini (National Language Translation Mission)** — India’s open-source indic language datasets and model repository (ULCA / Param Bharat) referenced in Session 11 for localization, sovereign AI, and multilingual scaling considerations.
