---
type: Session
resource: https://www.youtube.com/watch?v=SgfRzxPdZv4
title: 'Session 13: Enterprise GenAI Deployment, LLM Ops, and the Wedge Strategy'
description: A comprehensive guide on deploying generative AI in enterprises, covering
  cost optimization, LLM Ops, the wedge strategy, containerization, and real-world
  failure analyses.
tags:
- Enterprise Deployment
- LLM Ops
- Wedge Strategy
- Cost Optimization
- Semantic Caching
- Containerization
- Model Drift
timestamp: '2026-03-15'
---

This session, led by Dr. Anand Jayaraman, explores the pragmatic realities of operationalizing, architecting, and deploying reliable Generative AI solutions within enterprise settings. Highlighting the stark "deployment gap"—where Gartner reports that over 80% of traditional AI proof-of-concepts (PoCs) fail to reach production, a number that rises to 95% for GenAI pilots—the lecture focuses on mitigating these failure rates. To bridge this gap, the instructor introduces the "Wedge Strategy," which champions starting small by identifying a single, painful, narrow workflow to achieve a quick win with "hero users" (early adopters). This bottom-up, iterative approach is contrasted with highly complex, top-down comprehensive enterprise AI platforms, which frequently stall due to heavy governance and cross-team dependencies.

Central to this operationalization is the role of the "AI Translator," a senior role that bridges the gap between business sponsors and deep technical engineers. Translators translate corporate objectives into concrete technology choices, evaluating options such as deterministic rule-based engines, traditional machine learning models, Small Language Models (SLMs) for local environments, and premium Large Language Models (LLMs) for complex reasoning. A retail "Messy Inbox" customer support email triaging system receiving 30,000 emails per month is analyzed to illustrate a full production-grade architecture, comparing external API integration (via routers like Open Router) with cloud self-hosting and on-premise deployments.

The session also covers critical production infrastructure, explaining how Docker containerization solves dependency clashes across environments and how Kubernetes orchestrates these containers to manage auto-scaling, load-balancing, and cost. To curb ballooning model costs, techniques like semantic caching (using embedding similarity to serve repeated queries without hitting the LLM) and model routing are detailed. Finally, the lecture analyzes notable real-world failures, including the Air Canada chatbot lawsuit, Zillow’s $500M algorithmic real estate losses, and the Snap FTC complaint, to emphasize the vital roles of guardrails, LLM Ops versioning, and continuous model drift monitoring.

# Key Concepts

- **The Wedge Strategy** — An iterative, bottom-up deployment framework where developers focus on a single painful workflow to build a highly reliable, early-adopter-supported solution, scaling smart rather than attempting a high-risk, multi-year organizational transformation from day one.
- **The AI Translator** — A senior organizational role that sits between the business users and technical programmers, focusing on "cost per outcome" and ROI rather than raw "cost per token," and guiding architecture, model choice, and cloud strategies.
- **Model Drift & Observability** — The phenomenon where a deployed model's input distribution or environment behavior shifts over time (e.g., due to seasonality, macroeconomic factors, or silent API updates from vendors), necessitating continuous monitoring and feedback loops as part of [AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md).
- **Semantic Caching** — A critical cost-saving infrastructure layer that embeds incoming queries and checks for semantic similarity against a database of previous queries. If a match exceeds a threshold (e.g., 95% similarity), the cached response is served, completely bypassing expensive LLM calls.
- **Containerization & Orchestration** — Using Docker to package code and its exact dependencies into lightweight, isolated sandboxes, and Kubernetes to automatically scale these containers up during traffic spikes to maintain strict SLAs and keep costs low.
- **Human-in-the-Loop & Safety Guardrails** — Structuring human agent verification, especially for sensitive transactions or financial/policy claims, and enforcing safety/compliance layers to avoid brand liability and hallucinated commitments. Detailed frameworks can be found in [Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md) and [AI Governance and Compliance](../concepts/ai-governance-compliance.md).
- **Model Routing** — Dynamically switching models based on task complexity (e.g., using rule-based filters first, then SLMs for structured extraction/classification, and escalating to LLMs only for complex reasoning). Real-world solutions like Dyna Route by Vijura show savings of 70–75%.

# Topics Covered

- **The GenAI Deployment Gap**: Analysis of why 95% of GenAI proof-of-concepts fail to reach production due to costs, latency, and system complexity.
- **The Wedge Strategy vs. Top-Down Planning**: Evaluating centralized top-down governance versus bottom-up, iterative pilot programs.
- **AI Technology Selection Matrix**: Choosing between rules-based engines (deterministic logic), classical machine learning (classification), Small Language Models (SLMs) (1–8B parameters), and Large Language Models (LLMs) (70B+ parameters) based on task needs.
- **Step-by-Step Production Architecture**: End-to-end design walking through ingestion, pre-processing (PII redaction, deduplication, threading), intent classification, policy checks, draft generation, compliance filters, human-in-the-loop review, and CRM updates.
- **Hosting Strategies & Cost Comparison (for 15M tokens/month)**:
  - *LLM API (gpt-4o-mini)*: ~$450/month. Easiest to deploy, but data leaves the environment.
  - *Managed SLM API (Groq / Together AI / Open Router)*: ~$300/month. Mid-level privacy, open-source model pricing, zero GPU ops burden.
  - *Self-Hosted SLM (Mistral 7B on A100)*: ~$2,500–$4,000/month (before engineering time). High GPU ops burden, 16–26 weeks to production. Break-even only begins above ~500M tokens/month. Self-hosting is a data sovereignty decision first, a cost decision second.
- **Containerization and Orchestration**: Practical demonstrations of Dockerfiles, pushing code versions via Git/GitHub, automatic deployment onto Render.com with environment keys, and scaling using Kubernetes.
- **LLM Ops and Cost Management**: Implementing semantic caching, prompt version control, model routers, and observability frameworks.
- **Case Study Analysis**:
  - *Air Canada Chatbot (2024)*: Chatbot hallucinating bereavement policies, showcasing the need for grounding with [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) and strict policy tools to avoid legal liability (*Moffatt v. Air Canada*, 2024 BCCRT 149).
  - *Zillow Zestimate*: Highlighting catastrophic losses exceeding $500M and winding down of "Zillow Offers" due to unmonitored model drift when a pre-COVID pricing model failed in the volatile post-COVID real estate market.
  - *Snap FTC Complaint*: Highlighting unsafe responses to minors and the need for age-specific safety alignment, tiered safety architectures (Safety → Policy → Model), topic detection, and pre-release red-team testing.

# Materials

- **Slides**: `2026-03-15 Lecture.pdf`, `Session13_Lecture_2026-03-15.pdf`
- **Chat**: Present (Active discussion on startup challenges, enterprise risk appetites, and India's GPU infrastructure expansion)
- **Video Recording**: `https://www.youtube.com/watch?v=SgfRzxPdZv4`

# Related

- Part of [GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md)
- Preceded by [Session 12](c4-genai-pretrained-models-session-12.md)
- Followed by [Session 14](c4-genai-pretrained-models-session-14.md)

# Citations

1. Lecture recording: `https://www.youtube.com/watch?v=SgfRzxPdZv4`
2. British Columbia Civil Resolution Tribunal, *Moffatt v. Air Canada*, 2024 BCCRT 149 (the landmark chatbot liability ruling).
3. Zillow Group Public Announcement on Winding Down "Zillow Offers" (November 2021).
4. O'Reilly Radar, *Think Smaller: The Counterintuitive Path to AI Adoption*, 2024. `https://www.oreilly.com/radar/think-smaller-the-counterintuitive-path-to-ai-adoption/`
