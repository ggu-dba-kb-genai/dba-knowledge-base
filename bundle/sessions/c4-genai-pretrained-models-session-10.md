---
type: Session
resource: https://www.youtube.com/watch?v=pPPTswRSiBs
title: 'Session 10: Agents, Agentic Loops, and Multi-Agent Orchestration'
description: An in-depth exploration of agentic AI architecture, distinguishing adaptive
  agentic loops from linear workflow automation, featuring demos of n8n and CrewAI,
  and introducing emerging communication protocols like MCP.
tags:
- AI Agents
- Agentic Loops
- Multi-Agent Orchestration
- MCP
- n8n
- CrewAI
- HITL
- Observability
timestamp: '2026-03-01'
---

This session, led by Dr. Anand Jayaraman, marks the transition from static, task-based Large Language Models (LLMs) to goal-driven, autonomous [Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md). Dr. Anand details the core architectural differences between standard workflow automation (which executes predictable, sequential steps like $A \rightarrow B \rightarrow C$) and agentic flows. While traditional workflows can integrate LLMs (such as using an LLM to summarize weather reports on a fixed schedule), true agentic flows employ an adaptive Plan $\rightarrow$ Act $\rightarrow$ Observe $\rightarrow$ Reflect loop to handle exceptions, make dynamic decisions on the fly, and prioritize overarching goal achievement over micro-step execution. Dr. Anand highlights a critical industry perspective: while pre-sales clients frequently demand advanced agentic solutions, approximately 90% of actual enterprise use cases are best solved using optimized, linear workflows powered by LLMs rather than fully autonomous loops.

To illustrate these principles, the lecture features two hands-on demonstrations showcasing both low-code and code-based implementations of multi-agent systems. First, Dr. Anand demonstrates **n8n** (referred to phonetically as "NA10" or "NAN" in the transcript due to speech-to-text transcription quirks), utilizing its visual builder to construct a simple chat model, a search-enabled agent, an intent-based triage switcher, and a multi-agent financial supervisor coordinating specialist agents. However, as complexity increases—especially when implementing advanced logic like critique loops—visual interfaces can become highly restrictive. To address this, Dr. Anand transitions to a pure-code framework using **CrewAI** to design a collaborative financial team (comprising Researcher, Financial Analyst, Drafter, and Critique agents) with an explicit critique/refinement feedback loop where a Critique agent reviews and refines a drafted financial report before final output.

Finally, the session dives into critical enterprise operational issues, including cost control, [AI Security and Robustness](../concepts/ai-security-robustness.md), and [AI Governance and Compliance](../concepts/ai-governance-compliance.md). Because agents are empowered with tools to act, their threat surface is dramatically expanded compared to passive chat models. The lecture covers threats such as prompt injection through OCR scanned invoice documents, context bloating due to excessive tool capability discovery, and runaway infinite loops (illustrated by a real-world $47,000 cost incident where two agents were stuck in an infinite argument loop). Dr. Anand reviews emergent protocols like Anthropic's Model Context Protocol (MCP) for tool capability discovery, Agent-to-Agent (A2A) protocols for cross-firm agent collaboration, and the absolute necessity of incorporating [Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md) (including Human-in-the-Loop checkpoints) to manage enterprise risks and maintain human critical thinking.

# Key Concepts

- **[Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md)** — The paradigm shift from task-based prompt execution to goal-oriented digital entities possessing a reasoning brain, memory, specialized tool access, and a coordination controller.
- **Agentic Loop (Plan-Act-Observe-Reflect)** — The iterative cycle where an agent formulates a strategy based on memory/context, executes actions using tools, gathers environment feedback, and reflects to self-correct and refine subsequent steps.
- **Model Context Protocol (MCP)** — An open ecosystem standard introduced by Anthropic that standardizes how agents discover and interact with tools, replacing hardcoded API contracts with on-the-fly capability discovery.
- **Agent-to-Agent (A2A) Protocol** — An emerging industry communication layer (co-developed by Google and partners) enabling independent, domain-specialist agents to coordinate, delegate tasks, and share context dynamically.
- **Context Bloating** — An architectural bottleneck occurring when an agent has access to too many tools (e.g., hundreds of schemas), forcing the LLM to ingest massive API descriptions before executing simple queries, which balloons token costs and increases latency.
- **[Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md)** — The deployment of safety filters, policy layers, rate limits, and Human-in-the-Loop (HITL) checkpoints to authorize high-risk actions (e.g., financial transfers) and prevent the erosion of human critical thinking.
- **[AI Security and Robustness](../concepts/ai-security-robustness.md) & Prompt Injection** — The vulnerability of active agents to malicious commands injected through data pipelines, such as hidden instructions in OCR scanned PDFs telling the model to bypass standard rules.
- **Observability Frameworks** — The continuous logging of agentic intermediate actions to trace errors, audit decisions, and monitor key metrics such as token consumption, execution failures, and Time to First Token (TTFT).
- **[Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md)** — The evolution from manual prompting steps to goal-oriented outcomes using specialized templates, frameworks, and Anthropic's "Skills" abstraction.

# Topics Covered

- **The Evolution of LLM Methodologies**: Charting the transition from [Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md) (2022) to [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) (2023), [Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md) (2024), and Agents (2025).
- **Workflow Automation vs. Agentic Flow**: Linear, predictable execution (e.g., airport check-in) compared to adaptive, non-linear reasoning (e.g., detective murder investigation).
- **Anatomy of an Agent**: Building the "digital employee" with a brain (LLM), memory (context/state), tools (APIs/apps), controller, reflection, and guardrails.
- **Hands-on Visual Builder Demo (n8n)**: Drag-and-drop orchestration using OpenAI, setting up an intent-based triage switcher, and building a multi-agent supervisor coordinating researcher and analyst agents (noting the phonetic transcript references of "NA10" and "NAN").
- **Hands-on Programmatic Demo (CrewAI)**: Coding role-based worker agents (Researcher, Financial Analyst, Drafter, Critique), setting up goals and backstories, and designing a multi-agent critique loop for document refinement.
- **Standardized Communication Protocols**: How MCP resolves tool discovery on-the-fly and how A2A coordinates agents across separate organizational domains (e.g., Flight Agent collaborating with Hotel Agent).
- **Enterprise Risks & Governance**: Preventing runaway API loops (the $47,000 billing case study), mitigating prompt injection, and auditing agent behaviors via observability tools.
- **Real-World Case Studies**:
  - *Bud Financial*: Autonomous banking agents saving an average of $500 annually per user.
  - *Darktrace*: Cyber AI Analyst automating 80% of routine tasks and reducing triage time by 90%.
  - *Multimodal*: Agentic lending document pipelines driving an 80% cost reduction and 20x faster approvals.
  - *Palo Alto Networks / Moveworks*: Agentic HR saving over 180,000 productivity hours.

# Materials

- **Slides**:
  - `2026-03-01 Lecture.pdf`
  - `Session10_Lecture_2026-03-01.pdf`
- **Chat**: Available
- **Recording**: YouTube video `pPPTswRSiBs` is available.

# Related

- Part of the course: [GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md)
- Sibling Sessions:
  - [Session 09: Reasoning Models and Fine-Tuning](c4-genai-pretrained-models-session-09.md)
  - [Session 11: Deployment, Production Architectures, and MLOps](c4-genai-pretrained-models-session-11.md)

# Citations

1. Session 10 video recording: `https://www.youtube.com/watch?v=pPPTswRSiBs`
2. Anthropic Model Context Protocol (MCP) documentation
3. CrewAI multi-agent framework documentation
