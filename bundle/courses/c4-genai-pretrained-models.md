---
type: Course
title: 'C4: GenAI Pretrained Models'
description: A comprehensive course on generative artificial intelligence, exploring
  pretrained models, transformers, LLM training, prompt engineering, RAG, stable diffusion,
  and multi-agent workflows.
tags:
- generative-ai
- transformers
- llm
- prompt-engineering
- rag
- diffusion
- agents
timestamp: '2026-06-20T05:55:31+00:00'
---

This course provides an in-depth exploration of **Generative Artificial Intelligence (GenAI)**, focusing on the architectural foundations, training pipelines, evaluation methodologies, and practical implementation of state-of-the-art pre-trained models. Designed for leaders, practitioners, and technology translators, the course bridges the gap between deep technical theory and high-impact enterprise execution. 

Students progress from the basic limitations of classical sequential architectures like RNNs and LSTMs to the revolutionary [Attention Mechanisms and Transformers](../concepts/attention-and-transformers.md) that power modern Foundation Models. The course thoroughly unpacks the lifecycle of Large Language Models (LLMs)—including self-supervised pre-training, supervised fine-tuning (SFT), and Reinforcement Learning with Human Feedback (RLHF)—before diving into major enterprise applications. Key paradigms such as [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md), [Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md), stable diffusion for image generation, and System 2 reasoning architectures are studied alongside rigorous cost, latency, and observability-driven [AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md) frameworks. The curriculum culminates in student group pitches of fully realized AI enterprise products designed to solve real-world industry pain points.

# Sessions

*   **[Session 01](../sessions/c4-genai-pretrained-models-session-01.md) (2026-01-24) — Introduction to Generative AI & the Gartner Hype Cycle**
    An introductory exploration of the GenAI landscape, distinguishing between discriminative and generative modeling paradigms, and evaluating current industry maturity, pilot failure rates, and value realities using the Gartner Hype Cycle.
*   **[Session 02](../sessions/c4-genai-pretrained-models-session-02.md) (2026-01-25) — From RNNs and LSTMs to Attention Mechanisms and Transformers**
    A technical review of sequential NLP modeling, examining the architectural bottlenecks of RNNs and LSTMs (such as vanishing gradients and parallelization constraints) and introducing self-attention as the core engine of the transformer architecture.
*   **[Session 03](../sessions/c4-genai-pretrained-models-session-03.md) (2026-02-01) — Deep Dive into Transformers, BERT, GPT, and RLHF Training**
    An architectural deep dive into encoder-only (BERT), decoder-only (GPT), and encoder-decoder frameworks, demonstrating the mechanics of pre-training, supervised fine-tuning, and alignment via Proximal Policy Optimization (PPO) in RLHF.
*   **[Session 04](../sessions/c4-genai-pretrained-models-session-04.md) (2026-02-07) — API Access, Prompt Engineering, and Performance Metrics**
    A practical guide to programmatic interaction with LLMs via APIs, demonstrating stateless conversational engineering, parameter tuning (temperature, Top-K, Top-P, penalties), and evaluating performance across word-level, LLM-as-a-judge, and enterprise-level metrics.
*   **[Session 05](../sessions/c4-genai-pretrained-models-session-05.md) (2026-02-14) — Hands-on Lab: Deploying Chatbots & RAG on Azure OpenAI Service**
    A laboratory session led by Dr. Yogesh focusing on setting up resource groups, configuring system variables, deploying model instances, and integrating initial knowledge-base documents into Azure OpenAI playgrounds.
*   **[Session 06](../sessions/c4-genai-pretrained-models-session-06.md) (2026-02-15) — Parameter-Efficient Fine-Tuning (PEFT) and Retrieval-Augmented Generation (RAG)**
    An evaluation of knowledge integration strategies, contrasting the high-compute footprint of PEFT/LoRA against the dynamic retrieval pipelines of in-context learning and semantic chunking within vector databases.
*   **[Session 07](../sessions/c4-genai-pretrained-models-session-07.md) (2026-02-21) — Image Generation with Diffusion Models and Vision Transformers**
    An investigation into multi-modal synthesis, unpacking the mechanics of stable diffusion (forward and reverse processes in latent space) alongside Contrastive Language-Image Pre-training (CLIP) and Vision Transformers (ViTs).
*   **[Session 08](../sessions/c4-genai-pretrained-models-session-08.md) (2026-02-22) — Hardware Acceleration, System 2 Reasoning, and Knowledge Graphs (Graph RAG)**
    An exploration of hardware scaling constraints (GPUs/TPUs) and the shift toward inference-time compute using Process Reward Models (PRMs), prompt-compilers like DSPy, and structured knowledge graphs for multi-hop reasoning.
*   **[Session 09](../sessions/c4-genai-pretrained-models-session-09.md) (2026-02-28) — Hands-on Lab: Multi-Modal and Open-Source Models on Hugging Face and Google Colab**
    A practical hands-on session demonstrating how to pull, test, and run open-source text and image generation models locally or in cloud-hosted Jupyter environments.
*   **[Session 10](../sessions/c4-genai-pretrained-models-session-10.md) (2026-03-01) — Multi-Agent AI, Autonomous Workflows, and Enterprise Governance**
    An introduction to agentic architecture design patterns, demonstrating single and multi-agent coordination, Model Context Protocol (MCP) integrations, custom tool calling, and critical enterprise cost, observability, and safety guardrails.
*   **[Session 11](../sessions/c4-genai-pretrained-models-session-11.md) (2026-03-07) — Enterprise AI Deployment, MLOps, and Model Routing**
    A session covering the operationalization of generative models, focusing on hybrid cloud infrastructures, API gateways, system latency optimization, and cost-efficient model routing architectures.
*   **[Session 12](../sessions/c4-genai-pretrained-models-session-12.md) (2026-03-14) — Ethical AI, Bias Mitigation, and Governance Frameworks**
    A review of corporate compliance and safety standards, examining the detection and correction of model bias, data privacy mandates, and the design of automated evaluation suites.
*   **[Session 13](../sessions/c4-genai-pretrained-models-session-13.md) (2026-03-15) — Case Studies: AI Transformation in Banking and Healthcare**
    An analysis of real-world enterprise deployments of agentic workflows and specialized LLMs in highly scrutinized, high-security sectors like wealth management, diagnostics, and clinical documentation.
*   **[Session 14](../sessions/c4-genai-pretrained-models-session-14.md) (2026-03-28) — Capstone Presentations Day 1: Project Pitches & Defense**
    The first round of the final group capstone presentations, where student teams pitch their AI-native business products to a panel of peers and instructors.
*   **[Session 15](../sessions/c4-genai-pretrained-models-session-15.md) (2026-03-29) — Capstone Presentations Day 2: Group Project Pitches & Course Wrap-up**
    The final round of product defenses—featuring innovative designs like Aegis, Cidris, and Giu AI—and a course wrap-up summarizing the transition from task execution to goal-driven agentic autonomy.

# Assignments

- [Assignment 1: RAG-Based GenAI Solution Design](../assignments/c4-genai-pretrained-models-assignment-1.md) — Individual; design a retrieval-augmented GenAI solution for a knowledge-work task (25 marks).
- [Group Assignment: Business Problem Solved with Generative AI](../assignments/c4-genai-pretrained-models-group-assignment.md) — Group; vision, solution proposition, product roadmap, and ROI for a GenAI product (50 marks).

# Citations

1. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). *Attention Is All You Need*. arXiv preprint arXiv:1706.03762.
2. Radford, A., Narasimhan, K., Salimans, T., & Sutskever, I. (2018). *Improving Language Understanding by Generative Pre-Training*. OpenAI Technical Report.
3. Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*. arXiv preprint arXiv:1810.04805.
4. Lewis, P., Perez, E., Piktus, A., Petroni, F., Lewis, V., Riedel, S., & Kiela, D. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. Advances in Neural Information Processing Systems, 33, 9459-9458.
5. Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
6. Khattab, O., Singh, S., Maheshwari, S., Blalock, A., Vardula, S., Musuvathi, M., ... & Matei, I. (2023). *DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines*. arXiv preprint arXiv:2310.03714.
