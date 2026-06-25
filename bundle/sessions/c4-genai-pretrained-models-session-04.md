---
type: Session
resource: https://www.youtube.com/watch?v=MaGIIepXZDg
title: 'Session 04: Prompt Engineering, Stateful API Architecture, and Enterprise
  Evaluation Metrics'
description: A deep dive into prompt engineering, stateful conversation architectures
  over stateless APIs, and methods for measuring LLM toxicity, hallucinations, and
  token cost economics.
tags:
- Prompt Engineering
- API Integration
- Temperature
- Statelessness
- BLEU
- ROUGE
- LLM-as-a-Judge
- Token Economics
- DSPy
timestamp: '2026-02-07'
---

This session transitions the study of large language models (LLMs) from back-end training pipelines to the frontend of engineering deployment, programmatic interaction, and systemic validation. The lecture establishes the corporate role of the **"translator"**—a conceptualized bridge introduced by Google to describe professionals who map business priorities to software limitations, converting engineering constraints (such as model latency, cost, and hallucination bounds) into commercial risk metrics. Anchored in probability theory, the session details how models output next-token distributions, how parameters manipulate these outputs, and how stateless REST APIs are engineered into stateful customer solutions. 

The lecture further details the strategic framework of prompt orchestration, comparing legacy translation metrics against modern semantic validation. In doing so, the instructor introduces Stanford's DSPy library for systematic prompt compilation and highlights the financial implications of token economics—specifically why output token processing costs up to eight times more than input token processing. The class concludes by illustrating runtime guardrails, prompt injection vulnerabilities, and real-world business outcomes, citing Klarna's customer service bot pilot as an enterprise case study of risk-adjusted return on investment (ROI).

# Key Concepts

- **The Corporate Translator**: A pivotal organizational role tasked with bridging the communication gap between business decision-makers and technical engineers. The translator converts ambiguous domain problems into machine learning constraints while translating system properties (like latency or toxicity) into compliance and commercial risk metrics.
- **LLMs as Probability Engines**: Under the hood, LLMs are next-token predictors that generate a probability distribution over a vocabulary of thousands of potential tokens. Rather than outputting "truth," they sample from this distribution. Deterministic "greedy" decoding (always choosing the highest probability) produces robotic and predictable text, necessitating probabilistic sampling to introduce diversity.
- **Inference Configuration Parameters**:
  - **Temperature**: Controls prediction entropy by scaling logit values before applying the softmax function. Setting a low temperature (approaching 0) concentrates the distribution into a deterministic peak, perfect for math or code. High temperatures (approaching 1) flatten the distribution, permitting lower-probability words to drive "creativity."
  - **Top-K Sampling**: A technique that limits token generation to only the top $K$ most probable tokens before probabilistic sampling, eliminating highly toxic or nonsensical low-probability tokens.
  - **Top-p (Nucleus) Sampling**: Samples from the smallest subset of tokens whose cumulative probability exceeds a threshold $p$, allowing the candidate pool to dynamically expand or shrink depending on prediction confidence.
  - **Max Tokens**: An administrative boundary that chops off output generation at a specified token count, acting as a critical financial safeguard against runaway generation bills.
- **[Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md)**: Rather than ad-hoc text manipulation, enterprise prompt engineering serves as a governance tool. Prompts define specific roles and boundaries to steer model outputs reliably:
  - **Zero-Shot Inference**: Requesting an answer directly from the model's pre-trained weights without providing any context exemplars.
  - **Multi-Shot Inference**: Embedding a small set of input-output exemplars inside the context to force specific schemas (e.g., instructing an LLM to generate raw SQL queries while suppressing chatty pleasantries).
  - **Chain-of-Thought (CoT)**: Instructing the model to trace its reasoning incrementally ("think step by step"). Showing mathematical or logical steps dramatically increases correctness on complex multi-step computations and serves as the foundation for modern reasoning models.
- **Programmatic Prompt Optimization (DSPy)**: Stanford's DSPy library programmatically compiles and optimizes declarative prompts, replacing manual heuristic prompt tweaking with structured, reproducible, and compile-ready software pipelines.
- **Stateful API Architectures**: While consumer interfaces feel stateful, LLM REST APIs are entirely stateless to maximize scalability. To build stateful applications (like chatbots), developers execute **prompt chaining**, explicitly managing a sequential array of messages and appending prior turns using three API roles: `system` (master guidelines governing safety and personality), `user` (end-user queries), and `assistant` (previous model outputs).
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)**:
  - **Legacy Translation Metrics**: Metrics like **BLEU** (Bilingual Evaluation Understudy, precision-focused for translation) and **ROUGE** (Recall-Oriented Understudy for Gisting Evaluation, recall-focused for summarization) fail for generative AI. They measure exact word-level overlaps and punish synonyms (e.g., scoring "weather is hot" low against a reference of "climate is warm"), and they are susceptible to "vibe check" failures—giving high scores to fluent but factually incorrect outputs.
  - **Modern Semantic Metrics**: Enterprise evaluation monitors functional parameters: factual accuracy, bias, toxicity, and safety scores. Toxicity is measured using classification models (e.g., `Detoxify` or packages like `langfair`) trained on human-annotated datasets like Jigsaw's Toxic Comment Classification.
  - **LLM-as-a-Judge**: A cost-efficient automated testing architecture where an offline, highly capable model (e.g., GPT-4 or Claude 3 Opus) evaluates the outputs of a cheaper, faster runtime model (e.g., GPT-4 Mini) against a validated, human-curated "golden set" of reference responses.
- **Token Economics**: Production LLM providers separate billing into input tokens (read cost) and output tokens (generation cost). Output tokens are $3\times$ to $8\times$ more expensive (e.g., $1.70 vs. $14.00 per million tokens) because inputs are processed in parallel in a single forward pass, whereas outputs require recurrent, iterative forward passes through the [neural network architecture](../concepts/neural-network-architectures.md) for every generated token.
- **[Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md)**: Deploying generative models requires runtime guardrails. These include structural guardrails (enforcing JSON outputs via Pydantic or Guardrails.ai), moderation APIs (pre-filtering toxic user inputs and post-filtering toxic assistant outputs), and robust prompt injection defenses (sanitizing user inputs to prevent attackers from overriding system-role instructions, as seen in the early Bing Chat "Sydney" prompt leaks).

# Topics Covered

1. **Course Arc Recap**: Reviewing tokenization, word embeddings, sequence bottlenecks in RNNs/LSTMs, BERT encoders, GPT decoders, SFT, and RLHF.
2. **The Translator Role**: Concept origin at Google, mapping business goals to software constraints, and managing system risks.
3. **Generative Probability Mechanics**: Token output vocabulary distributions, greedy selection vs. probabilistic next-token sampling.
4. **Hyperparameter Selection**: Thermodynamic analogies of Temperature, Top-K and Top-p (Nucleus) mechanics, and Max Token budget barriers.
5. **Stateful Chat Over Stateless APIs**: Appending conversation lists, role-based API schemas (`system`, `user`, `assistant`), and prompt chaining memory limitations.
6. **Prompt Engineering Typology**: Zero-shot inference, Multi-shot formatting (e.g., SQL output enforcement), and Chain-of-Thought step-by-step reasoning.
7. **Compiled Prompt Pipelines**: Stanford's DSPy library and compiling declarative prompt flows.
8. **Legacy NLP Evaluation Limits**: Precision-based BLEU and Recall-based ROUGE; exact word-match failures and synonym penalties.
9. **Modern GenAI Quality Metrics**: Toxicity tracking using BERT classifiers (e.g., Detoxify) and measuring demographics bias via [Bias, Fairness, and Alignment](../concepts/bias-fairness-alignment.md) paired prompt tests.
10. **The LLM-as-a-Judge Pattern**: Golden reference sets, offline evaluation pipelines, and runtime model validation.
11. **Token Economics & Computational Asymmetry**: Why input tokens are cheap (parallelized encoding) and output tokens are expensive (sequential generation loops).
12. **Enterprise Case Study**: Analyzing Klarna's customer service bot deployment (deflecting two-thirds of support traffic, replacing 700 agents, and driving $40M in profits) as a case study in risk-adjusted ROI.

# Materials

- **Lecture Video**: [Recording on YouTube (MaGIIepXZDg)](https://www.youtube.com/watch?v=MaGIIepXZDg)
- **Lecture Slides**:
  - `2026-02-07 Lecture.pdf`
  - `Session04_Lecture_2026-02-07.pdf`
- **Class Chat**: Present and active during discussions about API stateful management, prompt engineering budgets, and student travel logistics.

# Related

- Part of the **[GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md)** course.
- Sibling Sessions:
  - [Session 01: GenAI Overview & Gartner Hype Cycle](c4-genai-pretrained-models-session-01.md)
  - [Session 02: Tokenization, Word2Vec, and Transformers](c4-genai-pretrained-models-session-02.md)
  - [Session 03: BERT, GPT, and RLHF Model Training](c4-genai-pretrained-models-session-03.md)
  - [Session 05: Practical Retrieval-Augmented Generation (RAG) Architecture](c4-genai-pretrained-models-session-05.md)

# Citations

1. OpenAI API Documentation, [OpenAI Platform](https://platform.openai.com/docs).
2. Stanford NLP Group, "DSPy: Compiling Declarative Language Model Calls", [GitHub](https://github.com/stanfordnlp/dspy).
3. Papineni, K., Roukos, S., Ward, T., & Zhu, W. J. (2002). "BLEU: a Method for Automatic Evaluation of Machine Translation." *Proceedings of the 40th Annual Meeting of the Association for Computational Linguistics (ACL)*.
4. Lin, C. Y. (2004). "ROUGE: A Package for Automatic Evaluation of Summaries." *Text Summarization Branches Out*.
5. Klarna Press Release (2024), "Klarna AI Assistant Handles Two-Thirds of Customer Service Chats in Its First Month".
