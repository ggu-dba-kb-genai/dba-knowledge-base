---
type: Session
resource: https://www.youtube.com/watch?v=Rjsmve7sc54
title: 'Session 03: Prototyping, Hypothesis Testing, and Piloting in AI Projects'
description: A deep dive into managing AI project risk by defining structured hypotheses,
  designing scientific prototype tests, and building functional pilots before enterprise
  coding.
tags:
- prototyping
- hypothesis-testing
- piloting
- prompt-engineering
- deduplication
- embeddings
- explainable-ai
- project-design
- bias
timestamp: '2026-04-11'
---

The third session of the **AI Project Design** course marks a critical transition in the [AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md) from executive-level strategy and prioritization to tactical project execution. While the first two sessions focused on high-level strategy formulation, readiness assessments, and prioritization frameworks (SVP/CXO domain), this session focuses on the senior or general managers responsible for leading development. The instructor details how to bridge the gap between a prioritized business problem and formal software development by utilizing **Prototypes** to challenge core assumptions (failing fast) and **Pilots** to secure user acceptance.

To demonstrate these methodologies, the session centers on a bottom-up AI Idea Management System designed for a CIO. While top-down executive planning is common, bottom-up systems allow employees to pitch high-value, day-to-day operational improvements (e.g., automating manual PDF-to-Excel translations). However, traditional enterprise intake systems fail because employees refuse to fill out tedious, 50-question forms. To eliminate this friction, the proposed system uses an LLM to digest unstructured, vague employee descriptions (or audio transcripts) and guide users through structuring their ideas. This concept is systematically decomposed into four distinct business and operational hypotheses, with structured experiments designed to validate each before writing enterprise code.

An extensive pharmaceutical R&D analogy illustrates the economic power of failing fast. Out of a $5 billion drug development budget, $4.5 billion is typically spent on failures, and only $500 million on successes. Consequently, a 10% improvement in identifying failures early saves $450 million—nearly double the return of doubling successful trials. This scientific discipline is exemplified by the shape-memory alloy kidney tube case study: the first four years of research isolated the physiological tolerance and side effects of the physical tube in animal and human trials rather than medical efficacy, since a failure in patient tolerance would immediately kill the product. The lecture argues that AI project leads must adopt this scientific mindset, systematically identifying and testing high-risk assumptions through creative, low-cost experiments before investing in full-scale implementation.

# Key Concepts

- **Prototyping & Failing Fast** — A temporary, low-cost experiment designed strictly to challenge critical assumptions. It is not an early alpha version of the final software, but a diagnostic tool used to discover fatal flaws and redirect development.
- **Hypothesis Testing & Validation** — The systematic process of isolating high-risk assumptions, defining quantifiable metrics, and constructing scientific experiments (often leveraging golden datasets) to validate them. Covered under [Model Evaluation and Validation](../concepts/model-evaluation-validation.md).
- **Prompt Engineering for Extraction** — Creating robust meta-prompts that guide an LLM to accurately extract structural entities (decisions, actors, actions, and workflows) from unstructured text without inventing details or hallucinating. Covered under [Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md).
- **Canonical Vector Similarity & Deduplication** — Converting messy, variable-length text ideas into a standardized "canonical form" (such as `Actor + Decision + Action + Workflow`) and embedding it to compute cosine similarity, rather than comparing raw unstructured text which leads to high error rates. Covered under [Embeddings and Vector Representations](../concepts/embeddings-and-representations.md).
- **Explainable Scoring Rubrics** — Prioritizing rule-based, transparent scoring formulas over black-box machine learning models in early-stage deployments to ensure rejection decisions can be clearly explained to users, minimizing friction and fostering trust. Covered under [Explainable AI (XAI)](../concepts/explainable-ai.md).
- **Algorithmic Bias Mitigation** — Recognizing that complex machine learning models can inadvertently learn unwanted patterns and systemic prejudices from historical training data (such as Amazon's sexist recruiting algorithm or unexplainable credit card rejections by Indian banks). Covered under [Bias, Fairness, and Alignment](../concepts/bias-fairness-alignment.md).
- **Wipe Coding (Incremental Development)** — An incremental programming workflow where a developer generates, tests, and verifies code file-by-file (e.g., login, extractor, similarity engine) within a pre-defined directory spec, rather than building complex multi-file systems blindly.
- **Human-in-the-Loop Validation** — Ensuring human-AI collaboration where LLMs generate structural outlines, data requirements, and feasibility parameters, while humans override, verify, and input final contextual scores. Covered under [Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md).

# Topics Covered

### 1. Pivoting from Strategy to Tactical Execution
- Transitioning ownership of prioritized projects from senior executives to general/senior managers.
- Comparing top-down central planning with bottom-up, employee-driven AI ideas aimed at localized operational bottlenecks.
- Overcoming user adoption hurdles: replacing tedious 50-question forms with interactive, AI-driven guidance.

### 2. The Science of Prototyping: The Shape-Memory Alloy Kidney Tube Analogy
- Detailed analysis of pharmaceutical R&D spending showing the massive economic leverage of identifying failures early.
- Case Study: A shape-memory alloy kidney tube designed to bend under local body temperature, resist rejection, and spray medicine for two weeks. 
- Early trial protocols: isolating and validating the physical tolerance of the shape-memory alloy in rats, rabbits, and humans before evaluating medical efficacy.

### 3. Case Study: Bottom-Up AI Idea Management System
Decomposing the enterprise system into four testable business and operational hypotheses:
- **Hypothesis 1 (Strategic Assumption):** *Does presenting ideas in a structured strategic format actually improve the decision correctness of the evaluating panel?*
  - *The Test:* Construct a "golden dataset" of 50 ill-formed ideas and 50 corresponding structured ideas. Run a blind A/B test with human evaluators using a strict rubric to measure and quantify decision accuracy (e.g., validating a target 33% improvement).
- **Hypothesis 2 (User Acceptance & LLM Extraction):** *Can an LLM reliably guide a user to transform a vague description into a well-defined structured format without inventing facts or altering the idea's core direction?*
  - *The Test:* Engineering a meta-prompt (incorporating chain-of-thought and few-shot examples) that extracts actor, decision, action, and workflow, while explicitly penalizing buzzwords ("optimize", "enhance"). Evaluate extraction accuracy against the golden dataset.
- **Hypothesis 3 (Operational Performance):** *Can we accurately and efficiently identify duplicate ideas among thousands of employee submissions to prevent redundant evaluations?*
  - *The Test:* Compare plain text embedding cosine similarity against embedding a *canonical form* of the idea. Task an ML engineer with finding the optimal similarity threshold to establish system limitations.
- **Hypothesis 4 (Explainable Scoring):** *Can we use a human-driven, rule-based explainable rubric to score and prioritize ideas, rather than a complex black-box machine learning model?*
  - *The Test:* Develop a multi-dimensional weighted rubric (Strategic Alignment, Decision Clarity, Business Impact, Data Readiness, Feasibility, and Usage Frequency). Perform action research to align weights with expert consensus and generate clear, explainable feedback for accepted/rejected proposals.

### 4. Piloting and Code Generation
- Definition of a Pilot: A functional working model built to capture workflow feedback, secure user acceptance, and validate interface behaviors.
- Constructing functional specifications with LLMs: defining root directories, subdirectories, routes, and functional blocks.
- Demonstrating incremental file-by-file code generation and manual verification ("wipe coding") to maintain complete architectural control.

### 5. Practical Breakout Session Exercises
- **Group 9 (ESG Compliance Reporting Tool):** Developing an AI-powered tool for ESG compliance across multiple frameworks.
  - *Hypothesis:* Reducing ESG reporting time from 6 weeks to 5 days directly improves customer retention.
  - *The Test:* Pitching existing clients a 5-day turnaround for a 20% price premium. If they agree to pay, it validates actual business value and skin-in-the-game demand before writing code.
- **Group 10 (Hospitality Booking No-Show Reduction):** Identifying high-risk bookings via historic scheduling data.
  - *Hypothesis:* One-tap, interactive WhatsApp/SMS actions outperform fixed generic reminder schedules.
  - *The Test:* Deploying low-cost interactive button simulations to a sample of 100 users via WhatsApp to measure click-through and confirmation rates before building custom backend features.

# Materials

- **Video Recording:** [AI Project Design - Session 03 (2026-04-11)](https://www.youtube.com/watch?v=Rjsmve7sc54)
- **Chat Log:** Present and integrated into session files.
- **Slides:** Presented on-screen during the lecture, illustrating the prototyping frameworks, hypothesis-testing models, and weighted prioritization rubrics.

# Related

- **Parent Course:** [AI Project Design](../courses/c5-ai-project-design.md)
- **Previous Session:** [Session 02: AI Readiness and Prioritizing AI Problems](c5-ai-project-design-session-02.md) (2026-04-05)
- **Next Session:** [Session 04: AI Lifecycle and Managing Project Complexity](c5-ai-project-design-session-04.md) (2026-04-12)

# Citations

1. Lecture Video: [AI Project Design - Session 03](https://www.youtube.com/watch?v=Rjsmve7sc54).
2. Action Research Methodology: Cited in the design of weighted multi-criteria scoring rubrics to align expert decision-making with automated algorithms.
3. Amazon Sexist Recruiter Case Study: Cited as an empirical warning of how black-box ML models replicate historical bias by learning hidden features.
4. Shape-Memory Alloy Kidney Delivery Systems: Anecdotal medical research case study illustrating physiological tolerance testing as an absolute prerequisite to efficacy evaluation.
