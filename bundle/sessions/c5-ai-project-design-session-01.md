---
type: Session
resource: https://www.youtube.com/watch?v=Vxo95A60u-o
title: 'Session 01: Moving from AI Crush to AI Strategy'
description: An introduction to AI project planning, contrasting vague AI hype with
  structured business strategies, decision models, and workflow integrations.
tags:
- ai-strategy
- business-value
- workflow-integration
- fermi-estimation
- change-management
timestamp: '2026-04-04'
---

This session marks the beginning of the **AI Project Design** course, taught by Dr. Dakshina Murthy V. Kolluru ("Morty"). Transitioning from a technical or scientific perspective to a "boardroom mindset," the lecture centers on transforming "AI crush"—the superficial excitement over cool demos—into sound, executable business strategy. Dr. Murthy, drawing on his background as an NIT Trichy metallurgy graduate, a Carnegie Mellon materials science PhD, an Agni missile program defense scientist, and an AI entrepreneur, emphasizes that 60–65% of enterprise AI failures occur at the problem selection and planning stage, whereas execution problems account for only 25%. To prevent these failures, organizations must rigorously define their business strategy first before choosing AI as a tool.

The structured planning framework presented involves a four-step cascade: defining a Strategy, deriving specific Decisions, designing Workflow Integration, and constructing a clear Value Hypothesis. For any initiative, planners must answer: **Who** is targeted, **which decision** is being improved, **in which workflow** does it sit, and **using what lever** is the intervention delivered. The lesson emphasizes that great AI systems are useless unless they map to the right decision, moment, owner, and action in a real-world workflow, noting that AI does not fix fundamentally broken business processes.

These concepts are illustrated through several real-world case studies from Dr. Murthy's consulting and entrepreneurial career. These include *sparLM*, an LLM-based document analysis tool for portfolio managers highlighting inconsistencies and novel insights; a rude customer call detection system for a manufacturing firm; a clinical trial patient-swapping fraud detector in pharmaceuticals; and a hospital patient readmittance prevention program. Through these examples, the session explains **Fermi analysis** for calculating financial ROI, the importance of change management over pure training, and when to favor simple rule-based systems or mathematical formulas over complex neural networks. Additionally, the lecture introduces the concept of **knowledge distillation** as a mechanism to train smaller models using probabilistic outputs rather than binary labels.

# Key Concepts

- **AI Strategy over "AI Crush"** — Moving beyond vague ambitions or superficial excitement to clear, structured business problems. Good strategy is not AI; it is business.
- **The Strategic Scoping Framework** — Defining the target customer segment (*Who*), the decision being automated or supported (*Which decision*), the integration point (*In which workflow*), and the business intervention (*Using what lever*). This maps directly to the initial phase of the [AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md).
- **Workflow Integration** — Designing predictions to deliver the right decision, at the right moment, to the right owner, leading to a clear action. AI cannot fix broken workflows.
- **Value Hypothesis & Fermi Analysis** — Using step-by-step mathematical estimations of known and unknown factors to quantify the direct financial impact of solving a problem, bridging technical features with business outcomes. This aligns directly with [Model Evaluation and Validation](../concepts/model-evaluation-validation.md).
- **Simple Rule-Based Systems vs. Complex AI** — Prioritizing symbolic logic, simple business rules, or basic mathematical averages when they provide stability and lower implementation pain. This connects directly to **[Explainable AI](../concepts/explainable-ai.md)**.
- **Augmentation vs. Automation** — Deciding whether AI should support human decision-making (augmentation) or run autonomously, which maps to **[Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md)**.
- **Knowledge Distillation** — Training smaller models by feeding them probabilistic output distributions of larger, pre-trained models (e.g., 70% juice, 20% soda) rather than binary indicators, improving efficiency under [Model Compression and Optimization](../concepts/model-compression-optimization.md).
- **Change Management & Adoption Readiness** — Recognizing that organizational readiness, cultural buy-in, and operational workflow adjustments are harder to solve than technical modeling.

# Topics Covered

- **Course & Instructor Introduction**: Dr. Murthy's background (Carnegie Mellon PhD, metallurgy at NIT Trichy, Agni missile defense scientist, and entrepreneur) and transitioning from a scientific to a "boardroom" mindset.
- **The Failure Modes of Enterprise AI**: Analyzing why 90% of AI projects fail, putting 60–65% of the blame on problem selection and 25% on execution.
- **The AI Strategy Framework**: Defining the core questions (Who, Which decision, Workflow, and Lever) to avoid vague ambitions.
- **Decision Scoping and Workflow Integration**: Mapping out where predictions occur, when they occur, who owns them, and what actions are taken.
- **The Value Hypothesis (Fermi Analysis)**: Step-by-step ROI modeling using manufacturing call routing and clinical trial fraud examples.
- **Case Study: sparLM**: Resolving workflow conflicts between analysts seeking speed and bosses seeking depth in document review.
- **Case Study: Hospital Readmittance Prevention**: How a 93% accurate model failed to deploy due to doctor and nurse workflow interference, and how a dedicated tele-calling service solved the process gap.
- **Rule-Based Systems**: When to avoid AI in favor of simple rules or mathematical formulas.
- **AI Portfolio Scoping (Workshop Prep)**: Framing the homework for Session 02 to prioritize five problems by assessing pain vs. gain.

# Materials

- **Slides**: `Class01.pdf` (with auxiliary materials in `Class01+02.pdf`)
- **Chat Log**: Present
- **Video Recording**: Available on YouTube (ID: [Vxo95A60u-o](https://www.youtube.com/watch?v=Vxo95A60u-o))

# Related

- Part of the [AI Project Design](../courses/c5-ai-project-design.md) course.
- Next session: [Session 02: Portfolio Prioritization & Prototyping](c5-ai-project-design-session-02.md).

# Citations

[1] https://www.youtube.com/watch?v=Vxo95A60u-o
