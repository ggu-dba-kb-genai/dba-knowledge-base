---
type: Session
resource: https://www.youtube.com/watch?v=kicCvqgr44U
title: 'Session 15: Capstone Project Presentations'
description: The final session of the GenAI Pretrained Models course featuring student
  capstone project presentations demonstrating agentic architectures across regulatory,
  debugging, healthcare, insurance, educational, and talent acquisition domains.
tags:
- Agentic AI
- Multi-Agent Systems
- RAG
- Explainability
- Regulatory Compliance
- Capstone Projects
- Healthcare AI
- EdTech
- MLOps
timestamp: '2026-03-29'
---

The final session of the **GenAI Pretrained Models** course represents the culmination of the program, featuring student capstone project presentations. Six groups pitched comprehensive product decks demonstrating the application of multi-agent workflows, Retrieval-Augmented Generation, and safety guardrails to highly specialized and historically manual enterprise domains. Rather than creating generic wrappers, the presentations combined state-of-the-art LLMs (including Claude, Codex, and Haiku) with deterministic validation checks, temporal knowledge graphs, and interactive human-in-the-loop protocols.

The presentations spanned regulatory compliance, runtime debugging, healthcare audits, insurance subrogation, adaptive learning, and talent acquisition. Aegis (Group 5) tackled multi-jurisdictional compliance, demonstrating how a central "diplomat" meta-agent can resolve opposing mandates between regulations like GDPR and the Bank Secrecy Act. Cidris (Group 4) introduced a cross-environment debugging framework that replicates runtime environments using Docker and evaluates logs, configurations, and dependency trees using a hierarchical agentic structure backed by a six-layer anti-hallucination defense. Group 10 addressed US healthcare fraud, waste, and abuse (FWA) by designing a deterministic-to-generative bridge to produce legally defensible, explainable audit trails, shifting the paradigm from "pay and chase" to prepayment prevention.

Subrogenius (Group 2) automated vehicle insurance subrogation using multimodal data fusion (photos, telematics, weather) and game-theoretic adversarial negotiation simulations to optimize settlement floors. GU.AI transformed K-12 education with curriculum-aligned content generation and a scaffolding engine that prompts logical thinking rather than feeding answers. Finally, Hired Or Get Hired (HOG, Group 1) proposed a dual-sided talent intelligence platform featuring specialized talent and career agents with explicit human handoff gates to ensure compliance with high-risk AI frameworks like the EU AI Act. Collectively, the session highlighted how multi-agent designs can be operationalized into production-grade, compliance-ready enterprise architectures.

# Key Concepts

- [Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md) — Multi-agent designs served as the foundation for all pitches. Aegis coordinated local jurisdictional agents via a central diplomat meta-agent; Cidris deployed log, environment, and security agents via LangGraph state machines; and Subrogenius modeled adversarial negotiation using game-theoretic agent simulations.
- [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — Applied across domains to ground outputs in factual evidence. FWA healthcare auditing utilized RAG to link case summaries back to medical codes; GU.AI deployed an ontological RAG system grounded in local Singapore/India curriculum guidelines to prevent syllabus drift; and Aegis retrieved country-specific legal statutes to resolve compliance conflicts.
- [Explainable AI (XAI)](../concepts/explainable-ai.md) — Critical for legal defensibility. Group 10 (Healthcare FWA) implemented trace-to-source claim audits; Aegis developed automated citation generation back to statutory codes; and Subrogenius introduced "Subro Audit" to maintain step-by-step transparency during legal negotiations.
- [AI Governance and Compliance](../concepts/ai-governance-compliance.md) — Addressed extensively in Aegis's multi-jurisdictional framework reconciling EU AI Act, GDPR, CCPA, BSA, and Indian DPDP mandates, and in HOG's fairness-aware orchestration designed to align with the high-risk categorization of recruitment tools under the EU AI Act.
- [AI Security and Robustness](../concepts/ai-security-robustness.md) — Addressed by Cidris’s six-layer anti-hallucination pipeline (comprising evidence-grounded prompting, tool-verified facts, JSON schemas, cross-agent validation, Docker validation dry runs, and human gates) to secure production code.
- [Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md) — Implemented as strict handoff boundaries across projects. GU.AI utilized age-calibrated response validation and safety filters, while HOG integrated explicit human-in-the-loop gates ensuring final hiring decisions and interviews remain strictly human-driven.
- [Computer Vision](../concepts/computer-vision.md) — Employed by Subrogenius to extract structural variables (such as angle of impact, vehicle damage, and tire depth) from accident photographs and dashcam feeds, fusing them with telematics data to mathematically model liability.
- [AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md) — Operationalized by Cidris to bridge the deployment gap from developer machines to production, automatically reproducing CI/CD, staging, and production environment configurations within Docker containers.

# Topics Covered

- **Course Culmination & Logistics**: Scheduling presentations and managing constraints to allow all six remaining student capstone groups to present.
- **Pitch 1: AEGIS (Adaptive Enterprise Governance Intelligence System) — Group 5**
  - *Problem Space*: Navigating the "compliance tax" of rapidly evolving global regulations (GDPR, EU AI Act, India's DPDP, CCPA). Penalties in 2024 reached $19.3 billion globally, with TD Bank fined $3 billion for unresolved regulatory conflicts. 70% of compliance staff time is lost to scanning websites and tracking updates.
  - *The Dilemma (Nova Pay)*: A Singapore-based credit scoring fintech operating globally across Germany, California, Texas, India, and Singapore. The system triggers conflicting mandates: EU AI Act requires model explainability, while Singapore protects trade secrets as IP; GDPR mandates data minimization, while the US Bank Secrecy Act (BSA) requires 5-year financial transaction retention; India mandates strict data localization.
  - *Technical Architecture*: Multimodal ingestion pipeline -> Knowledge Reasoning Layer (Entity Network Graph & Document Navigator Graph) -> Agentic Orchestration Layer (coordinating local jurisdictional agents through a central Diplomatic Meta-Agent) -> Decision Loop -> Human-in-the-Loop Governance.
  - *IP and Patents*: Three patentable claims identified: (1) Jurisdiction-Aware Agentic AI (central meta-agent detecting conflicts between local retrieval agents); (2) Temporal Knowledge Graph Versioning (metadata track for effective dates and sunset clauses for retrospective auditing); (3) Federated Compliance Orchestration (respecting data sovereignty by passing summaries instead of raw data).
  - *Commercials*: Projected 546% ROI over 3 years ($52.4 million net return on a $9.6 million investment) with a 4-month payback period. Stress-tested on Nova Pay ($800M firm, 35 compliance staff) showing a 577% ROI and an 8-month head start in new markets.
- **Pitch 2: CIDRIS (Cross Environment Intelligent Debugging and Runtime Intelligence System) — Group 4**
  - *Problem Space*: Mismatched environment behaviors ("it works on my machine"). An application passes local tests on macOS/Python 3.11, fails CI/CD on Ubuntu 22.04/Python 3.14, passes staging on Alpine Linux/Python 3.11, and crashes in production on Amazon Linux 2/Python 3.9. Traditional coding tools (Copilot, Claude) are blind to runtime contexts.
  - *Technical Architecture*: LangGraph-based state machine orchestrator. Deploying specialized swarms:
    - *Teal Agents (Data Collectors)*: Environment Profiler, Log Analyzer, Dependency Graph Analyzer.
    - *Red Agents (Infrastructure Security & Config)*: Inspects Helm charts, expired certificates, TLS configurations, and service principles.
    - *Purple Agent (Root Cause Detector)*: Powered by Claude Opus 4.6 (1-million-token window) to digest full-system log histories.
    - *Agentic Runtime*: Runs on Cloud Code to read files, execute shell commands, run tests, and interact with Git.
  - *Multi-Model Cost Optimization*: Straightforward profiling routed to Claude Haiku 4.5 (saving 75% on API costs), heavy-reasoning diagnostics routed to Claude Opus 4.6, and code patch generation routed to Codex 5.3.
  - *Six-Layer Anti-Hallucination Framework*: (1) Evidence-grounded prompting; (2) Tool-verified facts (runtime checks over memorized state); (3) Predefined JSON output schemas; (4) Cross-agent verification; (5) Automated validation pipeline (dry runs in replicated Docker environments); (6) Developer review gate (target < 5% false-positive rate).
  - *Commercials*: Modelled on an enterprise with 300 developers and 500 incidents/month. Diagnostic time reduced from 2–4 hours to 15 minutes, saving 1,300 developer hours/month. Payback within Year 1.
- **Pitch 3: Fraud, Waste, and Abuse (FWA) Healthcare Claims Audit — Group 10**
  - *Problem Space*: Global losses from business FWA reach $5 trillion annually (5% of revenue). US healthcare fraud accounts for $100 billion+ in annual leakage. Existing recovery relies on reactive "pay and chase" where 80% of recoveries occur after payment has left the door.
  - *The Solution (Deterministic-to-Generative Bridge)*: A pipeline shifting detection "left" into prepayment prevention.
    - *Data Ingestion*: Normalizes claims, pharmacy records, prior authorizations, and clinical notes PDFs using OCR.
    - *Multi-Agent Swarm*: Insight extractor, claim contradiction analyzer, clinical plausibility checker, and provider peer group comparison.
    - *Legally Defensible Audits*: Every agentic claim summary is grounded in an explainability layer, citing the exact claim ID or clinical medical note source.
  - *Commercials*: Modelled on 10,000 cases/year. Preparation time reduced from 6 hours to 2 hours. Over 10,000 cases, saves $3 million in labor and achieves a $7.5 million recovery uplift. Break-even occurs in 6 months with a 2x Year 1 return on the $5 million investment.
- **Pitch 4: Subrogenius — Group 2**
  - *Problem Space*: Insurance subrogation (recovering paid claim payouts from at-fault third parties). manual and slow processes result in carriers leaving $30–$40 billion on the table annually.
  - *Technical Architecture*: Pure B2B backend profit center.
    - *Inputs*: Multimodal data fusion (vehicle damage photos, dashcam videos, IoT telematics, geospatial data, weather precipitation records).
    - *Agent Swarm*: Evidence agent, liability agent, legal agent (queries state statutes and case laws via a custom SubroLegal Graph), and strategy/negotiation agents.
    - *Auditability*: Explainable AI tracing ("Subro Audit") logs every decision to ensure transparency.
  - *Patentable Innovations*:
    - *Subro Radar Fusion Scoring*: Fuses damage photos, dashcam footage, and telematics in a shared latent space to mathematically prove liability (e.g., proving a third party was driving too fast for rain conditions based on braking distance and tire depth).
    - *Adversarial Negotiation Simulation*: Pits a strategy agent against an adversarial defense attorney agent using game-theoretic Monte Carlo simulations to calculate the optimal settlement floor.
  - *Commercials*: Modelled on 3,000 subrogation claims/year. Pays back the $14.3 million all-in setup cost in 14 months, returning $47 million in net recoveries, $12 million in operational savings, and a 62% cycle-time reduction (total 239% ROI over 3 years).
- **Pitch 5: GU.AI — Group 3**
  - *Problem Space*: Traditional edtech is static and lacks personalization, while generic generative AI lacks pedagogical grounding and feeds kids direct answers. Teachers spend 15 hours/week on administrative preparation (60% of their time).
  - *Technical Architecture*:
    - *Ontological RAG*: Grounds content generation in local curriculum guidelines (such as MOE in Singapore or CBSE in India) to eliminate syllabus drift.
    - *Generative Pedagogical Scaffolding Engine*: Powered by Bloom's taxonomy, it provides step-by-step guided hints and partial explanations rather than direct answers to encourage independent thinking.
    - *Decision Intelligence Layer*: Features a Learner State Model, Instructional Strategy Engine, Adaptive Personalization Engine (calibrating difficulty dynamically), Scaffolding Engine, and Intervention Engine (escalating persistent struggles to teachers or parents via PDPA-compliant narratives).
  - *GTM & Commercials*: Dual-market strategy. Singapore premium market entry (addressing SGD 1.8 billion private tuition market with 420k students) followed by Indian market scaling (248 million students). Focuses initially on Math and Science curriculum, projected to deliver a 129% net ROI.
- **Pitch 6: Hired Or Get Hired (HOG) — Group 1**
  - *Problem Space*: Fragmented, broken hiring pipeline. Recruiters lose weeks context-switching with high candidate dropout rates; job seekers experience a 2–4% response rate. ATS systems are static databases.
  - *Technical Architecture (Dual-Sided Second Brain)*:
    - *Recruiter (Talent Agent)*: Manages sourcing, outreach, screening, and scheduling. Generates a Candidate Intelligence Brief containing verification flags (scanning GitHub/blogs), motivational signals, and conversation guides.
    - *Candidate (Career Agent)*: Handles matching, resume tailoring, 360-degree company and interviewer search briefs, live voice/text Interview Coaching, Negotiation Advisory, and Skill Mapping (recommending affiliate educational programs).
    - *Governance*: Integrates explicit handoff protocols to comply with high-risk categorization under the EU AI Act.
  - *Patentable Innovations*: Dual-sided offer intelligence negotiation coach, Candidate intelligence brief, Talent intelligence graph, and Fairness-aware orchestration.
  - *Commercials*: Recruiter seats ($650-800/month + 2.5-3% placement fee), Career Agent subscription ($29–$79/month), Staffing white-label ($5-20k/month). Series A path targets $850k ARR in Month 6, $4M ARR in Month 12, and $17.9M ARR in Month 18. Asking for $3.2 million in seed funding.
- **Course Conclusion & Instructor Farewell**: Closing remarks from the professor highlighting the depth of the capstone projects and the successful integration of multi-disciplinary technical and business skills.

# Materials

- **Video Recording**: [YouTube Stream (Session 15)](https://www.youtube.com/watch?v=kicCvqgr44U)
- **Chat Log**: Present in the archive.
- **Slides**: Group presentations were delivered live via screen-sharing; no standalone slides are attached in the archive.

# Related

- **Parent Course**: [GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md)
- **Previous Session**: [Session 14](c4-genai-pretrained-models-session-14.md)

# Citations

1. GenAI Pretrained Models, Course Lecture 15 Recording, [https://www.youtube.com/watch?v=kicCvqgr44U](https://www.youtube.com/watch?v=kicCvqgr44U).
2. EU Artificial Intelligence Act, Regulation (EU) 2024/1689 (referenced by Aegis and HOG).
3. General Data Protection Regulation, Regulation (EU) 2016/679 (referenced by Aegis for data minimization).
4. Bank Secrecy Act, 31 U.S.C. § 5311 et seq. (referenced by Aegis for data retention).
5. National Education Policy (NEP) 2020 India (referenced by GU.AI).
6. Personal Data Protection Act (PDPA) Singapore (referenced by GU.AI for parental app safety and data privacy).
