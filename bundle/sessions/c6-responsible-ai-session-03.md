---
type: Session
resource: null
title: 'Session 03: A = Algorithm — Product Ideation & Prototyping (AI Success Planning)'
description: The third Responsible AI session opens the Darwin framework's "A = Algorithm"
  pillar, reframing prototyping as business-case validation. It covers why most AI
  initiatives stall, what makes a good prototype, time-boxing builds to days in the
  AI era, and a structured Translation-Ideation method for turning a business problem
  into a testable prototype.
tags:
- responsible-ai
- darwin-framework
- prototyping
- product-ideation
- mvp
- business-metrics
- agentic-ai
timestamp: '2026-06-21'
---

The third live session of the **Responsible AI** course (delivered 21 June 2026) begins the practical, build-oriented half of the Darwin framework with its **A = Algorithm** pillar — *Architecture and Algorithms: prototypes and MVPs*. Rather than starting from model selection, the lecture reframes the earliest engineering act as **business-case validation**: a prototype exists to test whether an idea delivers value, not to prove that a technology works. This continues the course's central thesis that AI initiatives fail for organizational and economic reasons far more often than technical ones.

The session situates prototyping inside the full Darwin execution order — **A → D → In → R → W** (Architecture/Algorithms, then Data, then Infrastructure & Security, then Responsibility, then Workflow Integration) — and motivates it with industry outcome data: only a thin slice (commonly cited as 5–15%) of AI initiatives deliver real value, while the majority stall at the prototype stage and a further band fails at the product stage by being unable to justify ROI. A worked example (a customer-call "tonality" / bad-call detection system) is used to show how a vague business aspiration is translated, through a structured ideation document, into a small set of falsifiable hypotheses and a quick, disposable prototype.

# Key Concepts

- **The Darwin "A = Algorithm" Pillar** — Architecture and Algorithms covers the rapid construction of prototypes and MVPs. In the framework's execution order (A → D → In → R → W), building a quick prototype comes *first*, ahead of heavy data engineering, infrastructure, responsibility/economics, and workflow integration — because the cheapest way to learn whether an initiative is worth pursuing is to build a throwaway version of it.
- **Prototype vs. MVP (the "prototype mantra")** — A prototype is a *quick-and-dirty* working model of an idea; it is explicitly **not** an MVP. Its purpose is to **validate the business case, not the technology**. A good prototype should fail fast when the core value hypothesis is wrong, help optimize the eventual infrastructure and deployment plan, communicate outcomes convincingly to clients, and include ample feedback mechanisms.
- **What makes a good prototype** — Fast to build (hours or days, not weeks); **focused** on one or two key hypotheses; **imperfect by design** (mock data, limited functionality, or manual "wizard-of-oz" work behind the scenes is acceptable); **cheap** (avoid production-scale infrastructure or polished UI); and **disposable** (a learning tool, not the foundation of the final product).
- **[AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md)** — Why AI projects stall: most never escape the prototype stage, and many that do fail at the product stage because they cannot justify ROI. Prototyping is positioned as the lifecycle's first stage-gate — the point at which a continue / pause / kill decision should be made cheaply.
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)** — Prototypes must declare both **business metrics** and **technical metrics** up front. The worked example tests business hypotheses (does intervention convert unhappy customers? is immediate intervention better than next-day?) rather than chasing model accuracy.
- **[Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md)** — A reference prototype architecture for a market-intelligence "copilot" uses an implicit **agent orchestrator** coordinating LLM tools: audio transcription (e.g., a Whisper-style speech-to-text tool), role-specific aspect gathering, relevant-point extraction, and summarization, iterating over target roles to produce role-specific summaries.
- **[Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md)** — Many prototypes deliberately keep a human in the loop. In the call-tonality example, a human expert listens to flagged calls and intervenes; the prototype's job is to test whether that human intervention helps at all before any model is trusted to act autonomously.
- **Translation-Ideation Method** — A structured worksheet that turns a business problem into a prototype plan across six sections: (1) nature of the problem (and whether it even needs AI), (2) end users and expected workflow, (3) business and ROI evaluation, (4) data and integration details, (5) deployment and compliance considerations, and (6) a priority-computation score. The first four sections are completed by whoever proposes the project and become the foundation for every later Darwin step. This worksheet is the required input for the course's first assignment.

# Topics Covered

- **AI Success Planning & the Darwin recap**: The five pillars — **D**ata (bias, completeness, governance), **A**rchitecture & Algorithms (prototypes and MVPs), **R**esponsibility (economics, compliance, application governance, stakeholder definitions, positioning), **W**orkflow integration (performance metrics, explainability, consumability), and **In**frastructure + Security (green metrics) — and the execution order A → D → In → R → W.
- **"Prototypes fail — is it a worry?"**: Industry outcome data showing only a small fraction of AI projects deliver value; the rest stall at prototype or fail to justify ROI at the product stage.
- **A sample idea**: A copilot for market intelligence that listens to annual-general-meeting (AGM) audio and produces role-based summaries (illustrated with a CHS earnings example), and its agent-orchestrated prototype plan.
- **How much time to spend (in the AI era)**: Time-to-a-single-digital-prototype should compress to **1–2 days** by reusing pre-trained models and APIs (e.g., OpenAI, Hugging Face) or mock outputs instead of training from scratch. Focus on user experience, workflow, and decision quality rather than model performance — *prototype speed is the competitive advantage; clarity comes from quick builds, not endless planning.*
- **Worked example — call-tonality / bad-call detection** (summarized): A large customer-service operation handles a high daily volume of recorded calls but has limited visibility into interaction quality, so customer-experience issues go undetected until customers churn or complain. The objective is to detect poor experiences (negative tone/sentiment) and surface near-real-time flags on a stakeholder dashboard.
- **From problem to hypotheses**: Using the Translation-Ideation document to define value (proactively, quickly, and economically detect bad calls and convert unhappy customers), state assumptions (AI is faster/better/cheaper than a human; intervention actually helps), and design a small experiment — e.g., have a human expert listen to a sample of bad calls and intervene immediately versus the next day, to test whether intervention helps and whether timing matters.
- **What to prototype first**: Whether intervention even makes sense (a manual mock-up), whether audio can be diarized (split by speaker), whether LLMs can judge sentiment from audio quickly without tagging or fine-tuning, and which step is the slowest and how much faster it must become for the system to be viable.

# Materials

- **Slides**: *AI Success Planning — Product Ideation* (Darwin "A = Algorithm" pillar).
- **Worksheet**: *Translation-Ideation* document (six-section ideation template; basis for Assignment 1).
- **Video Recording**: Not available for this session (slides-based notes).

# Related

- **Parent Course**: [Responsible AI](../courses/c6-responsible-ai.md)
- **Previous Session**: [Session 02: RLHF, Reasoning Models, and the Darwin Framework](c6-responsible-ai-session-02.md)
- **Assignment**: [C6 Assignment 1 — Ideation, Prototype & Data](../assignments/c6-responsible-ai-assignment-1.md)

# Citations

1. Sunkad, V. *AI Success Planning — Product Ideation* (Responsible AI, Session 03 lecture slides, 21 June 2026).
2. *Translation-Ideation* worksheet (Responsible AI course material, June 2026).
