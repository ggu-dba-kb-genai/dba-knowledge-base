---
type: Session
resource: https://www.youtube.com/watch?v=Uyok-nwbURo
title: 'Session 02: RLHF, Reasoning Models, and the Darwin Framework'
description: An in-depth exploration of reinforcement learning innovations, model
  compression techniques like LoRA and quantization, agentic workflows, and the introduction
  of the Darwin framework for responsible AI deployment.
tags:
- Reinforcement Learning
- RLHF
- Reasoning Models
- LoRA
- Model Compression
- Quantization
- Agentic AI
- RAG
- Darwin Framework
timestamp: '2026-06-07'
---

This lecture bridges deep-learning systems optimization with the administrative and ethical realities of enterprise AI deployment. It begins by examining recent reinforcement learning innovations, specifically how reasoning models are trained step-by-step using deterministic fields (mathematics and software development) to trigger emergent self-reflection (the "aha moment" where a model flags its own mistakes and re-evaluates). Crucially, these reasoning behaviors act as transferable skills that generalize to non-deterministic fields like philosophy.

The lecture then transitions to practical architecture and optimization patterns, contrasting rigid, predictable hardcoded AI workflows with highly autonomous, orchestrator-led multi-agent systems. To connect models to external knowledge efficiently and prevent vendor lock-in, the professor highlights the Model Context Protocol (MCP) as an emerging open middleware standard. The session also details parameter-efficient fine-tuning via Low-Rank Adaptation (LoRA) to prevent catastrophic forgetting, alongside compression techniques such as integer quantization (e.g., INT8) and teacher-student knowledge distillation.

Finally, the course shifts fully into the paradigm of responsible AI through the introduction of the **Darwin Framework**—a comprehensive system managing Data, Architecture, Responsibility, Workflow Integration, Infrastructure, and Security. Real-world case studies illustrate these principles: Klarna's customer support automation failure highlights the need for human-centric deployment planning to manage resistance, while a competitor intelligence summarization tool for CHS and a failure-prediction pipeline demonstrate that project success relies on rigorous business-defined features, performance benchmarks, and deployment realities over mere model selection.

# Key Concepts

* **Reasoning Models and Self-Reflection** — Explores how modern models (such as DeepSeek) use Reinforcement Learning from Human Feedback (RLHF) and AI Feedback (RLAIF) on highly deterministic fields like math and code execution. Rather than predicting next-tokens end-to-end blindly, reasoning models are rewarded for step-by-step logic, enabling emergent self-reflection (e.g., catching errors and re-evaluating, referred to as the "aha moment"). These logical reasoning capabilities function as a transferable skill, generalizing to non-deterministic subjects such as philosophy.
* **[Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md)** — Differentiates between a single **Agent** (an LLM equipped with tools like calculators, calendars, and web search to execute a single task) and **Agentic AI** (a multi-agent orchestrator or director agent coordinating multiple task-specific LLM instances). Multi-agent systems are contrasted with hardcoded **AI Workflows**, which provide strict developer control, reduce token costs, and guarantee predictability in production compared to fully autonomous planning.
* **Model Context Protocol (MCP)** — An open middleware protocol designed to standardize communication between LLMs and external tools. Similar to how REST/JSON unifies web architectures, MCP sits beneath the LLM, decoupling the model from proprietary tool APIs and allowing developers to register tools with a common protocol server, avoiding vendor lock-in.
* **[Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)** — A technique that connects an LLM to an external vector database of specialized institutional knowledge, serving as a dynamic domain expert without requiring parameter retraining. This grounds model responses in private, up-to-date data (e.g., HR policy manuals) to prevent hallucinations.
* **[Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md)** — Evaluates methods to embed deep knowledge into a model. Since full parameter fine-tuning risks **catastrophic forgetting** (where a model forgets general fields like chemistry or history after specialized training), **Low-Rank Adaptation (LoRA)** is introduced. LoRA freezes base weights and trains low-rank adapter matrices across every network layer (typically representing 1/500th of the original parameters), allowing selective backpropagation through only the newly added connections. The lecture advises that enterprise solutions should combine both methodologies (*LoRA + RAG*).
* **[Model Compression and Optimization](../concepts/model-compression-optimization.md)** — Detailed pipeline to shrink open-weight models (like LLaMA or DeepSeek) for edge or local deployment:
  * **Knowledge Distillation**: A teacher-student model where a smaller student model is trained to mimic the top-K probability outputs of a larger teacher model rather than learning from raw data.
  * **Integer Quantization**: Converting high-precision floating-point weights (FP16/FP32) into lower-precision integers (typically INT8, spanning values from -128 to 127). This decreases storage size by up to 50% and dramatically speeds up inference because integer matrix multiplications are much more efficient, with minimal (1-2%) loss in accuracy.
* **[AI Governance and Compliance](../concepts/ai-governance-compliance.md) & [AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md)** — Introduced via the **Darwin Framework** (Data, Architecture, Responsibility, Workflow Integration, Infrastructure, Security) to guide ethical, safe deployment. It emphasizes that features and performance benchmarks must be established by business analysts who understand domain problems, rather than data scientists.
* **[Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md)** — Highlights the importance of user adoption. If deployment planning fails to address psychological impacts (as seen in Klarna's customer support announcement where employees feared job losses), users actively resist the system. Leaders must frame AI as a collaborative efficiency enhancer rather than a replacement tool.

# Topics Covered

* **LLM Refresher and Next-Token Loop**: Contrasting a search engine with an LLM's autoregressive loop (predicting next-token recursively, feeding outputs back as inputs) and tokenization.
* **Reinforcement Learning Breakthroughs**: Binary feedback systems (RLHF/RLAIF) and the step-by-step reward training methodology of DeepSeek's reasoning models.
* **Tool Use and Skills**: Equipping LLMs with external code execution, calculators, and calendars to reduce energy-intensive and error-prone token calculations.
* **Model Context Protocol (MCP)**: Middleware positioning and standardization between LLMs and APIs.
* **AI Workflows vs. Agentic Orchestration**: Multi-agent design, anchor/director agents, and hardcoded control versus autonomous planning.
* **LoRA and Fine-Tuning Mechanics**: Catastrophic forgetting, parameter-efficient adapters, and freezing base weights during backpropagation.
* **Model Compression Methods**: Floating-point normalization, INT8 integer quantization, and teacher-student knowledge distillation.
* **The Darwin Framework**: The six pillars of responsible AI deployment (Data, Architecture, Responsibility, Workflow Integration, Infrastructure, Security) and its execution order.
* **Case Study: CHS Competitor Intelligence**: Constructing a 4.5-day prototype using Whisper transcription, persona-mapping LLMs, and summary-generation layers to analyze competitor general meetings.
* **Case Study: Failure-Prediction Pipeline**: Analyzing a French midsize company's predictive model where leakage of the last 30 days of data ($n - 29$ to $n$) ruined real-world inference, and how limiting training data to $n - 30$ resolved it.
* **Case Study: Klarna's Customer Support**: The consequences of announcing massive automation layoffs on user resistance and model adoption.
* **The Law of Demand for Complementary Goods**: The economic principle illustrating how easier model development increases the demand for governance, verification, testing, and deployment monitoring.

# Materials

* **Video Recording**: Available on YouTube (see citations).
* **Class Chat**: Present and active during the session.
* **Slides**: Distributed to students following the lecture.

# Related

* Part of the [Responsible AI](../courses/c6-responsible-ai.md) course.
* Sibling Session: [Session 01: Foundations of LLMs & Responsible AI](c6-responsible-ai-session-01.md)

# Citations

1. [Responsible AI Session 02 Recording](https://www.youtube.com/watch?v=Uyok-nwbURo)
2. "Reasoning in LLMs," *Nature* (referenced during the discussion on self-reflection and step-by-step reinforcement learning).
