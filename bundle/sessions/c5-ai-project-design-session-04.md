---
type: Session
resource: https://www.youtube.com/watch?v=zedlWnMwGpI
title: 'Session 04: Requirements Engineering for AI Projects'
description: A comprehensive guide on transitioning from vague AI ideas to structured,
  verifiable requirements using the ISO 29148 standard and managing outcomes under
  uncertainty.
tags:
- requirements-engineering
- brd
- prd
- outcomes-under-uncertainty
- iso-29148
- non-functional-requirements
- metrics
- validation
timestamp: '2026-04-12'
---

This lecture, delivered by Dr. Vinay Chowdary, bridges the critical gap between traditional software requirements engineering and the distinct realities of AI project execution. It examines why AI projects frequently stall or fail in the transition from initial prototype/demonstration to full production deployment. The core thesis is that traditional software requirements define deterministic features, whereas AI requirements specify **outcomes under uncertainty**. Because machine learning models are probabilistic, data-dependent, and contextually bound, managing their delivery requires a structured, metrics-driven methodology.

The session walks through the psychological development cycle of an AI project—transitioning from demo-induced illusion and confidence, through operational breakdown and team/vendor friction, to the realization of AI's unique requirements, and finally to controlled confidence. To build this control, Dr. Chowdary introduces the **ISO 29148** standard to establish a shared language across business and technical teams, resolve ambiguities, enforce verifiability, and implement rigorous governance.

The lecture concludes with a collaborative workshop where students apply these structured principles to three industrial use cases (Insurance, Mining, and Education), dissecting vague goals and rebuilding them into complete, traceable Project Charters, Business Requirement Documents (BRDs), and Product Requirement Documents (PRDs).

# Key Concepts

- **Outcomes Under Uncertainty** — AI requirements must specify acceptable probabilistic behaviors rather than exact deterministic features. This includes defining confidence intervals, acceptable ranges, and failover pathways when predictions fall outside thresholds. (Cross-link: [Model Evaluation and Validation](../concepts/model-evaluation-validation.md))
- **ISO 29148 Standard** — A global engineering standard applied to AI projects to ensure requirements are necessary, feasible, unambiguous, verifiable, complete, consistent, and traceable. (Cross-link: [AI Governance and Compliance](../concepts/ai-governance-compliance.md))
- **The Requirements Chain** — A structured hierarchy mapping high-level business goals down to precise technical proof:
  1. *Project Charter*: Why does the project exist and how will it be executed? (Defines scope, high-level risks, timeline, budget, and governance).
  2. *Business Requirement Document (BRD)*: What business outcomes must be achieved? (Quantifies return on investment (ROI) and target business metrics without mentioning specific algorithms).
  3. *Project Requirement Document (PRD)*: What must the system do? (Defines functional inputs/outputs and workflow integrations).
  4. *User Stories*: How do users interact with the system? (Drafted from a user's perspective, mapping out specific outcome-driven interactions).
  5. *Acceptance Criteria*: How do we prove it works? (Specific technical benchmarks representing "done means done").
- **Non-Functional Requirements (NFRs) in AI** — Essential system constraints that bound performance. Key AI-specific NFRs include explainability, security, bias mitigation, data quality, latency (real-time vs. batch), drift monitoring, and cost per inference (e.g., token consumption). (Cross-links: [Explainable AI (XAI)](../concepts/explainable-ai.md), [AI Security and Robustness](../concepts/ai-security-robustness.md), and [AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md))
- **Contestability & Override** — Establishing the right of the development team, vendors, and end-users to override AI decisions when performance degrades, ensuring robust human-in-the-loop governance. (Cross-link: [Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md))
- **Generative AI Requirements & Prompt Worsening** — Managing specific risks in generative models, such as undefined guardrails, lack of evaluation rubrics, hallucination thresholds, and the necessity for prompt versioning as systems scale. (Cross-link: [Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md))

# Topics Covered

### 1. The AI Project Cycle: From Illusion to Control
- **Phase 1: Illusion** — High confidence and excitement when a prototype works in a controlled demonstration, leading to executive approval.
- **Phase 2: Breakdown** — Disconnects emerge in production due to lack of metrics, workflows, clear data ownership, or vendor alignment, causing frustration.
- **Phase 3: Realization** — Shifting the team’s mindset to view requirements as outcomes under uncertainty rather than static features.
- **Phase 4: Fixing** — Introducing rigor through the Requirements Chain (BRD, PRD, User Stories, and Acceptance Criteria) to regain controlled confidence.

### 2. Case Studies of Deconstructed AI Failures
- **Zillow Offers (2021)**: Massive losses driven by overestimating predictive model capability. A failed BRD lacked risk guardrails, the PRD prioritized prediction over profit, and the Charter omitted constraints or killswitch governance.
- **Air Canada Chatbot (2024)**: Legal liability resulting from a hallucinated customer support response. The project lacked legal risk framing (BRD), controlled outputs (PRD), and escalation procedures (Charter).
- **Lemonade AI Claims (2022–24)**: Public trust and regulatory friction from opaque AI processing. The system lacked fairness metrics (BRD), interpretable model requirements (PRD), and human review triggers (Charter).

### 3. Implementing the ISO 29148 Standard
- **Necessity**: Determining whether the problem truly requires AI or can be resolved with simpler, deterministic rule-based systems.
- **Feasibility**: Evaluating available data quality, training/inference GPU infrastructure, skilled engineering teams, and realistic development timelines.
- **Traceability Checklist**: Testing that every requirement maps directly from **Business Goal → User Story → Acceptance Metric** to support audits and compliance.

### 4. Interactive Group Exercise: Writing BRD/PRD-Lite Packs
Students collaborated to reconstruct vague requirements (e.g., "We need AI to automate claims") into precise, structured outcome packs based on three enterprise use cases:
- **Use Case 1: Insurance Claims Triage (NA + Gulf)**
  - *Business Outcome*: Reduce triage time from 48 hours to <4 hours.
  - *System Behavior*: Ingest claims documents, output risk score and priority label, integrate with Claims Management System.
  - *User Story*: "As a claims officer, I want high-risk claims flagged within minutes so I can prioritize investigation."
  - *Acceptance Criteria*: Precision $\ge$ 90% for fraud detection, Latency $\le$ 3 seconds, False Positives $\le$ 5%.
  - *Constraints*: Latency < 3 sec, Cost < $0.05 per claim (OpEx constraint), mandatory human override.
- **Use Case 2: Mining Safety Detection (Australia + Southern Africa)**
  - *Business Outcome*: Reduce delayed safety hazard detection from 30 minutes to <2 minutes.
  - *System Behavior*: Ingest raw video feeds and sensor telemetry, output incident alerts on safety dashboard. (Cross-link: [Computer Vision](../concepts/computer-vision.md))
  - *User Story*: "As a safety officer, I want hazards detected in real time so I can intervene immediately."
  - *Acceptance Criteria*: Recall $\ge$ 95%, False alarms < 10/day, Latency < 10 seconds.
  - *Constraints*: Latency < 10 sec, GPU-optimized cost, manual confirmation override.
- **Use Case 3: Education Admissions Support (Middle East + South Asia)**
  - *Business Outcome*: Reduce application decision time from 2–3 weeks to <48 hours.
  - *System Behavior*: Ingest applications and transcripts, output recommendation scores.
  - *User Story*: "As an admissions officer, I want applications prioritized so I can focus on strong candidates."
  - *Acceptance Criteria*: Accuracy $\ge$ 85% compared to human decisions, processing time < 2 minutes/applicant, bias metrics continuously monitored.
  - *Constraints*: Latency < 2 min, scalable OpEx per applicant, strict bias/fairness constraints, mandatory human review.

# Materials

- **Slides**:
  - `Session 4 - (12 Apr 2026).pdf`
  - `Session04_Slides_2026-04-12.pdf`
- **Classroom Chat**: Active collaboration around rewriting weak statements, defining human-in-the-loop escalation paths, and debating unit-level OpEx constraints.
- **Video Recording**: YouTube recording ID [zedlWnMwGpI](https://www.youtube.com/watch?v=zedlWnMwGpI) (available under `https://www.youtube.com/watch?v=zedlWnMwGpI`).

# Related

- **Parent Course**: [AI Project Design](../courses/c5-ai-project-design.md)
- **Previous Session**: [Session 03: Case Study - LLMs in Enterprise](c5-ai-project-design-session-03.md)
- **Next Session**: [Session 05: Prompt Engineering](c5-ai-project-design-session-05.md)

# Citations

1. `https://www.youtube.com/watch?v=zedlWnMwGpI` — "Session 04: Requirements Engineering for AI Projects" Lecture Recording.
2. ISO/IEC/IEEE 29148:2018 — Systems and software engineering — Life cycle processes — Requirements engineering.
3. Google Research — "Mind Evolution: Evolving Deeper LLM Thinking" (Concept on iterating over generation loops to refine response quality, discussed by Dr. Chowdary in the context of prompt latency tradeoffs).
