---
type: Session
resource: https://www.youtube.com/watch?v=MNcMPaV01Tc
title: 'Session 09: Hands-On with Open-Source LLMs, Diffusion, and RAG (with Reasoning
  & Efficiency Frameworks)'
description: A comprehensive session bridging reasoning models, DSPy pipelines, and
  GraphRAG theory with hands-on open-source LLM, Ollama, Stable Diffusion, and RAG
  deployment.
tags:
- Open-Source LLMs
- Ollama
- Gradio
- Stable Diffusion
- RAG
- FAISS
- Hugging Face
- Groq Cloud
- DSPy
- GraphRAG
- Reasoning Models
timestamp: '2026-02-28'
---

Session 09 is a unique, dual-faceted session in the course. It bridges high-level theoretical limits of model scaling and reasoning architectures with an interactive, hands-on lab exploring open-source deployment. The session consists of two parallel tracks: a conceptual curriculum prepared by Dr. Anand Jayaraman focusing on "The Intelligence Frontier: Reasoning & Efficiency," and a practical live coding laboratory led by Dr. Yogesh demonstrating the programmatic orchestration of open-source models (including Qwen-32B and FLAN-T5) via cloud APIs (Groq Cloud) and local environments (Ollama), alongside diffusion-based image synthesis.

On the theoretical side, the session details how AI is transitioning from "Capital Expenditure" (training increasingly massive neural network models) to "Operational Expenditure" (spending compute at inference time to let models "think"). It covers the mechanics of reasoning, the distinction between System 1 (fast retrieval) and System 2 (slow, step-by-step computation) behaviors, Chain of Thought (CoT), Process Reward Models (PRMs), DSPy modular architectures, and the deployment of Knowledge Graphs (GraphRAG) to keep reasoning chains factually anchored.

On the practical side, the hands-on lab transitions students from closed-source, proprietary APIs to open-source alternatives. Students learn how to securely manage Groq API credentials in Google Colab, track inference parameters (such as token metrics), deploy lightweight models locally with Ollama, run Stable Diffusion for text-to-image generation via Hugging Face’s `diffusers` library, and assemble a localized [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) pipeline with Facebook AI Similarity Search (FAISS) to query user-uploaded PDFs.

# Key Concepts

- **Inference-Time Compute & System 2 Reasoning** — Shifting intelligence gains from capital-intensive training to runtime operational compute. Standard LLMs rely on fast, intuitive associative next-token retrieval (System 1). Reasoning models buy precision at runtime by exploring multiple solution paths, verifying intermediate steps, and backtracking when necessary (System 2 logical computation).
- **Process Reward Models (PRMs) vs. Outcome Reward Models (ORMs)** — Unlike ORMs that evaluate only the final output (which can encourage lucky guesses or shortcuts), PRMs grade and reward each individual step of reasoning. This process-level reinforcement learning (such as OpenAI's "Let's Verify" technique) encourages robust, auditable logic.
- **The Hallucination Snowball & Failure Modes** — Long reasoning chains suffer from exponential decay in accuracy (e.g., 95% step accuracy drops to 35% after 20 steps). Reasoning models without factual grounding can collapse into overthinking loops, display sycophantic behavior (post-hoc justification of expected answers), or suffer from context poisoning where early errors corrupt the entire reasoning chain.
- **DSPy (Programming, Not Prompting)** — A framework that treats LLM pipelines like software programs rather than fragile, hand-written prompt templates. It implements composable, testable, and model-agnostic modules (e.g., separating pipelines into `RiskIdentifier`, `RiskClassifier`, and `MitigationSuggester`) to prevent reasoning errors from propagating, acting as an [AI Governance and Compliance](../concepts/ai-governance-compliance.md) tool.
- **Knowledge Graphs & GraphRAG** — Grounding reasoning steps by retrieving verified factual entity relationships (networks of meaning) rather than simple unstructured text passages. This is crucial for multi-hop enterprise reasoning.
- **Open-Source vs. Closed-Source LLMs** — Open-source LLMs (e.g., Alibaba's Qwen-32B, Google's FLAN-T5) make weight files and architectures transparent, enabling local hosting via Ollama, [Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md), and granular control over [AI Security and Robustness](../concepts/ai-security-robustness.md) and data privacy, contrasting with closed-source proprietary APIs.
- **Diffusion-Based [Generative Modeling](../concepts/generative-modeling.md)** — A form of image generation that synthesizes realistic visuals from random noise via iterative denoising, governed by hyperparameters like *inference steps* (detailing level) and *guidance scale* (adherence to prompt vs. model creativity).
- **Local & Cloud-API Open-Source Orchestration** — Running high-speed inference of hosted open-source models using Groq Cloud API, or deploying them completely locally on consumer hardware via Ollama for absolute privacy.
- **Retrieval-Augmented Generation (RAG)** — Grounding language models by indexing private documents into vector databases (such as FAISS) via [Embeddings and Vector Representations](../concepts/embeddings-and-representations.md) to enable contextual document search and limit hallucinations.
- **Safety Alignment and Guardrails** — Enforcing [Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md) at the model level (e.g., Qwen-32B refusing to answer politically controversial or sensitive medical queries).

# Topics Covered

- **The Shift in Scaling Laws:** How GPUs escaped graphics processing to drive linear algebra in deep learning; the memory movement bottleneck over raw clock speed; moving from CapEx (training) to OpEx (inference).
- **Mechanics of LLM Reasoning:**
  - Chain of Thought (CoT) and the "scratchpad" mechanism as the model's short-term memory.
  - Training System 2 using Process Reward Models (PRM) and Critic Models to grade intermediate steps.
  - Failures of reasoning: Reasoning collapse/overthinking, sycophancy, and context poisoning.
- **DSPy - Programming Reasoning:**
  - The fragility of manual prompt engineering (the "spaghetti code" of GenAI).
  - Designing composable, testable, and model-agnostic pipelines (e.g., `RiskIdentifier` -> `RiskClassifier` -> `MitigationSuggester`).
- **GraphRAG and Grounding:**
  - Standard RAG (document text chunks) vs. GraphRAG (verified factual entity-relation networks).
  - Grounding reasoning steps with Knowledge Graph queries to halt the hallucination snowball.
- **Open-Source Software & Model Architecture:**
  - Open-source governance (PR reviews, Linux/VLC/Chromium) vs. closed-source (Windows/Chrome).
  - Open-source LLM benefits: Auditability, parameter transparency, zero subscription fees, and data privacy.
- **Hands-On 1: Cloud Inference with Groq Cloud & Google Colab:**
  - Securely managing API keys via `getpass` in Python.
  - Invoking Qwen-32B programmatically and analyzing response metadata (completions, token count, execution metrics).
- **Hands-On 2: Chatbot Creation with Gradio:**
  - Integrating Groq completions into a web chatbot within Colab.
  - Tuning UI parameters (e.g., `lines=20` for output window size).
  - Observing safety alignment and guardrails in action.
- **Hands-On 3: Local LLMs via Ollama:**
  - Deploying lightweight models (such as Qwen-4B) directly on local consumer hardware.
- **Hands-On 4: Stable Diffusion Image Synthesis:**
  - Running text-to-image pipelines on a Colab T4 GPU.
  - Exploring the behavior of *inference steps* and *guidance scale* hyperparameters.
- **Hands-On 5: Local RAG Pipeline:**
  - Parsing uploaded PDFs, converting chunks to embeddings, storing them in a FAISS vector database, and querying them using Google's FLAN-T5 base model.

# Materials

- **Slides:** `2026-02-28 Lecture.pdf` and `Session09_Lecture_2026-02-28.pdf` (covering reasoning, DSPy, and GraphRAG)
- **Chat:** Chat was present during this live interactive lecture.
- **Recordings:** Video session available via video ID `MNcMPaV01Tc`

# Related

- Parent Course: [GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md)
- Sibling Sessions:
  - [Session 08: Evaluation Metrics and Benchmarking](c4-genai-pretrained-models-session-08.md)
  - [Session 10: Advancing RAG & Vector Storage](c4-genai-pretrained-models-session-10.md)

# Citations

1. YouTube Video: [Session 09: Hands-On with Open-Source LLMs, Diffusion, and RAG](https://www.youtube.com/watch?v=MNcMPaV01Tc)
2. DSPy Framework Documentation: [DSPy: Programming, not Prompting](https://github.com/stanfordnlp/dspy)
3. Groq Cloud Developer Portal: [Groq Cloud Console](https://console.groq.com)
4. Ollama Local Framework: [Ollama Website](https://ollama.com)
5. Gradio Documentation: [Gradio](https://gradio.app)
6. Hugging Face Models Hub: [Hugging Face](https://huggingface.co)
