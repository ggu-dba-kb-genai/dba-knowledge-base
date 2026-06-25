---
type: Session
resource: https://www.youtube.com/watch?v=E00kuZEXgzU
title: 'Session 08: Hardware Scaling Limits, System 2 Reasoning, DSPy, and Graph RAG'
description: An in-depth exploration of the transition from hardware-driven scaling
  to inference-time reasoning, introducing Process Reward Models, the DSPy compilation
  framework, and Graph RAG.
tags:
- GPUs
- CUDA
- TPUs
- System 2 Reasoning
- Process Reward Models
- DSPy
- Graph RAG
timestamp: '2026-02-22'
---

The eighth session of the **GenAI Pretrained Models** course explores the paradigm shift from training-time scale (capital expenditure) to inference-time logical reasoning (operational expenditure). The lecture begins with a historical retrospective on how hardware has driven algorithmic breakthroughs. It traces the journey of Graphic Processing Units (GPUs) from specialized 3D spatial transformers executing parallel coordinate transformations (such as rotating vectors and translating camera perspectives) to General-Purpose GPUs (GPGPUs) powered by Nvidia's CUDA architecture, and finally Google's Tensor Processing Units (TPUs) designed specifically as Application-Specific Integrated Circuits (ASICs) for deep learning. The session explains how neural network processes are fundamentally memory-bandwidth-limited, making highly parallel vector computation architectures indispensable for modern AI.

With empirical neural scaling laws hitting economic and physical constraints, the AI ecosystem is shifting toward "System 2" thinking. Rooted in Daniel Kahneman's psychological framework of fast, intuitive "System 1" thinking versus slow, methodical "System 2" reasoning, this approach leverages inference-time compute. Giving a model a "scratchpad" (Chain of Thought tokens) to search, verify, and correct intermediate steps before committing to a final answer yields massive performance gains—equivalent to a 100,000x increase in training compute for logical tasks. The session details how these models are trained using Process Reward Models (PRMs) evaluated by auxiliary critic models, rather than standard Outcome Reward Models (ORMs).

To address the fragility of handcrafted prompts and mitigate the "hallucination snowball" (where cascading error propagation decays 95% step-accuracy down to 35% over 20 steps), the course introduces two engineering solutions: **DSPy** and **Graph RAG**. Through a financial sentiment analysis demo, the instructor illustrates how the DSPy programming framework compiles declarative task signatures into optimized few-shot prompts, reducing the performance gap between proprietary models (like GPT-4) and open-source models (like Llama) from 9% to 0%. The session concludes by comparing standard semantic chunk-based RAG with Graph RAG, demonstrating how constructing pre-computed Knowledge Graphs allows models to reliably perform complex, multi-hop relational reasoning.

# Key Concepts

- **[Attention Mechanisms and Transformers](../concepts/attention-and-transformers.md)** — The architectural mechanism that enables parallel processing across a massive context window, moving away from sequential RNN limitations and aligning perfectly with parallel hardware.
- **[Neural Network Architectures](../concepts/neural-network-architectures.md)** — The structure of neural networks uses dense linear algebra (matrix-vector and matrix-matrix multiplications) which maps perfectly onto thousands of parallel cores on GPUs and ASICs.
- **[Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md)** — Traditional handcrafted prompts are compared with the DSPy programmatic paradigm, which uses labeled training examples to optimize prompts and compile modular, testable pipelines.
- **[Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)** — Standard semantic document chunk retrieval is contrasted with Graph RAG, which retrieves structured, pre-computed relational subgraphs to support multi-hop reasoning.
- **[AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md)** — Incorporating automated prompt optimization frameworks like DSPy into the development lifecycle enables robust versioning and seamless model migration, mimicking traditional ML retraining.
- **[Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md)** — Combining internal reasoning models with external tools allows autonomous systems to transition from mere planning (thinking) to executing sequences of actions in the real world (doing).
- **[Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md)** — Using process reward signals and structured pipelines serves as a critical corporate governance tool to ensure auditable, testable, and compliant model outputs.

# Topics Covered

- **Change Management & Systems Integration**:
  - Parallels of introducing AI to corporate environments.
  - The Mars Climate Orbiter disaster: a classic engineering integration and change management failure where a contractor used Imperial units (pound-seconds) while NASA used Metric units (newton-seconds), leading to a spacecraft crash due to mismatched assumptions.
- **Hardware as the Hidden Driver of Intelligence**:
  - **Graphic Processing Units (GPUs)**: Escape from graphics (where millions of 3D coordinates are simultaneously transformed via matrix rotations) to general-purpose computing (GPGPU) in the early 2000s.
  - Nvidia's CUDA architecture: Providing complete, programmable hardware microcontrol to scientific researchers.
  - **CPUs vs. GPUs**: CPUs are optimized for sequential, single-core, branch-heavy logic; GPUs contain thousands of simpler cores optimized for massive parallelism and dense linear algebra.
  - **Memory Movement Bottleneck**: Modern deep learning is restricted by memory bandwidth (moving data in/out of cores) rather than raw clock speed.
  - **Google Tensor Processing Units (TPUs)**: ASICs optimized purely for deep learning 3D tensor computations, on which the Google Gemini models are entirely trained.
- **The Shift to Inference-Time Scale**:
  - The limitations of training-time scaling (exponential increase in CapEx for linear performance gains).
  - Shifting intelligence to runtime (Inference OpEx). Letting a model reason on poker (from Noam Brown's TED Talk) for just 20 seconds is equivalent to scaling up training compute by 100,000x.
  - **System 1 vs. System 2 Thinking**: Mapping Daniel Kahneman's psychological framework to AI. System 1 (standard next-token generation; fast, intuitive; e.g., "What is the capital of France?") vs. System 2 (search, verification, error correction; e.g., counting "R"s in "Strawberry").
- **Mechanics and Training of Reasoning Models**:
  - **The Scratchpad/Chain of Thought (CoT)**: Allowing the model short-term memory before committing to a final answer since a model "must speak to think."
  - **Outcome Reward Models (ORMs)** vs. **Process Reward Models (PRMs)**: "Grading the work, not just the final answer." ORMs encourage lucky guesses or shortcuts, while PRMs incentivize logical steps.
  - **Training Pipeline**:
    1. Generate reasoning traces from a base LLM using CoT prompts.
    2. Grade each partial step using a separate, lower-quality verifier/critic model.
    3. Assign step-level rewards.
    4. Train the model using process-level Reinforcement Learning (RL) to maximize cumulative rewards.
  - **The Hallucination Snowball**: Mathematical cascade of step errors ($0.95^{10} \approx 60\%$, $0.95^{20} \approx 35\%$), requiring structural pipelines and grounding.
- **DSPy Framework (Declarative Self-improving Language Programs)**:
  - Fragility of hand-crafted prompts ("the new spaghetti code") breaking upon model or task shifts.
  - Composable, model-agnostic software modules (inputs -> outputs) called Signatures.
  - Compiler optimization loops: automatically searching for and selecting the best few-shot training examples (e.g., finding the best 4 examples out of a pool of 50) and prompting phrasing to maximize validation scores.
  - Practical demo: Evaluating news sentiment classification (neutral news is the most difficult category). DSPy improved GPT-4 from 56% to 59%, and Llama from 47% to 59%, completely neutralizing the performance gap (reducing it from 9% to 0%) and enabling predictability.
- **Knowledge Graphs and Graph RAG**:
  - Representing information as structured networks of meaning (entities and relational edges).
  - Failure of standard chunk-based RAG in multi-hop, relational logic (e.g., retrieving managers of managers, or indirect drug interactions across multiple academic research documents).
  - **Graph RAG**: Pre-processing documents at ingestion time to extract relational entities and compile a mind map (hierarchical subgraphs of meaning) that models traverse during query inference.
  - Cost vs. Value: Graph RAG is computationally and financially expensive at ingestion time, but acts as a critical scaffolding to ground reasoning chains and prevent hallucinations.

# Materials

- **Slides**: `2026-02-22 Lecture.pdf`, `Session08_Lecture_2026-02-22.pdf`
- **Chat**: Yes, student-instructor chat was present and highly interactive.
- **Recording**: Available under YouTube stream ID `E00kuZEXgzU`

# Related

- Part of the **[GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md)** course.
- Sibling Sessions:
  - Prev: **[Session 07: Multimodal Models and Image Diffusion](c4-genai-pretrained-models-session-07.md)**
  - Next: **[Session 09: Tool Use and Agentic Workflows](c4-genai-pretrained-models-session-09.md)**

# Citations

- [1] `https://www.youtube.com/watch?v=E00kuZEXgzU` (Session Recording)
- [2] Daniel Kahneman, *Thinking, Fast and Slow* (Farrar, Straus and Giroux, 2011).
- [3] Stanford NLP Group, *DSPy: Declarative Self-improving Language Programs* (official framework documentation).
- [4] NASA, *Mars Climate Orbiter Mishap Investigation Board Phase I Report* (1999) - regarding metric/imperial mismatch.
- [5] Noam Brown, *Inference-Time Compute & System 2 Reasoning in Poker* (TED talk).
