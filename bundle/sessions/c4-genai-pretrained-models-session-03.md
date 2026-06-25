---
type: Session
resource: https://www.youtube.com/watch?v=t53r2vaP61c
title: 'Session 03: BERT, GPT, and RLHF: Pre-training, Fine-Tuning, and Human Alignment'
description: A technical deep dive into encoder-only and decoder-only architectures,
  pre-training objectives, transfer learning, the RLHF alignment pipeline, and the
  empirical impact of Neural Scaling Laws.
tags:
- Transformers
- BERT
- GPT
- RLHF
- Transfer Learning
- PPO
- Scaling Laws
- Phase Transitions
timestamp: '2026-02-01'
---

Dr. Anand Jayaraman leads a technical exploration of the evolution of pre-trained Transformer architectures, moving from Google’s BERT (2018) to OpenAI’s GPT variants and culminating in the alignment techniques that underpin ChatGPT. The lecture frames the sudden emergence of capabilities in large language models using a physics analogy: just as 1D and 2D Ising models of atomic interactions fail to exhibit abrupt phase transitions (such as ice abruptly turning to liquid at 0°C) while 3D models magically do, deep learning networks suddenly display linguistic intelligence only after crossing critical thresholds of parameter scale, compute, and training data. This concept of emergent phenomena motivated the industry's subsequent multi-billion dollar brute-force scaling paradigm. Before diving into model architectures, the class also discusses the viral phenomenon of "Maltbot" (formerly "Claudebot") and "Maltbook"—a multi-agent network of over 150,000 local assistant agents communicating with one another. This real-world case study highlights critical AI safety and observability concerns, particularly around agentic communication transitioning into latent vector spaces that humans cannot monitor.

The core technical lecture contrasts the two primary architectural paths stemming from the original Transformer block: encoder-only systems (such as BERT) and decoder-only systems (such as GPT). Encoder-only models process input text bidirectionally in parallel, translating human language into dense, context-aware machine representations that are ideal for classification tasks. Pre-trained on Google's BookCorpus (800 million words) and Wikipedia (2.5 billion words) using Masked Language Modeling (MLM) and Next Sentence Prediction (NSP), BERT popularized transfer learning in NLP. It allowed businesses to download a high-capacity base model and fine-tune only its final classifier layers on specialized company data for nominal compute costs. Conversely, decoder-only models generate text sequentially through autoregressive next-token prediction, treating language production as a massive multi-class classification task over a large vocabulary (e.g., 10,000+ tokens).

Finally, the session breaks down the multi-stage alignment pipeline required to transform a raw next-token predictor into a useful, safe, and conversational assistant. Dr. Jayaraman details how OpenAI implemented Supervised Fine-Tuning (SFT) over ~12,000 to 15,000 curated expert prompt-response demonstrations—strategically choosing to fine-tune on top of a code-heavy baseline model rather than pure text to improve reasoning. Because SFT alone does not guarantee human preference, the pipeline incorporates Reinforcement Learning from Human Feedback (RLHF). This involves training a separate Reward Model (RM) using pairwise comparative rankings (which yield higher consistency than multi-choice rankings in human tests) to predict human preference, followed by policy updates via Proximal Policy Optimization (PPO). The session concludes with a review of OpenAI's 2020 empirical paper on Neural Scaling Laws, which established power-law bounds on error rates based on compute, parameters, and dataset size, and a forward-looking discussion on the impending limits of the public "data wall."

# Key Concepts

- **[Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md)**: Introduced via "Maltbot" (local, private assistants running on hardware like Mac minis) and "Maltbook" (a social space for bots). The instructor discusses the potential dangers of agentic emergent behaviors, group mentalities, and the safety risks of allowing agents to communicate directly in latent vector space rather than human-readable natural language.
- **[Attention Mechanisms and Transformers](../concepts/attention-and-transformers.md)**: A structural breakdown of the Transformer block, detailing how positional encodings are combined with input word embeddings before passing through multi-head self-attention, skip connections, layer normalization, and feedforward networks.
- **[Embeddings and Vector Representations](../concepts/embeddings-and-representations.md)**: The conversion of discrete words into dense, contextualized vectors. Dr. Jayaraman emphasizes that while word-level embeddings like Word2Vec are context-blind, Transformer encoders produce representations that capture the syntactic, grammatical, and semantic nuances of how a word is used in a specific sentence.
- **[Neural Network Architectures](../concepts/neural-network-architectures.md)**: The bifurcation of the Transformer design into encoder-only (bidirectional understanding and classification), decoder-only (autoregressive causal token generation), and encoder-decoder (full translation and summarization) architectures.
- **[Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md)**: The practice of leveraging massive, expensive pre-trained representations (such as BERT's base weights) and training only a small final classifier layer on specialized enterprise data, reducing training costs from millions of dollars to local, low-compute processes.
- **[Generative Modeling](../concepts/generative-modeling.md)**: Constructing language by treating text generation as an iterative, autoregressive process. The decoder predicts output probabilities over a massive multi-class vocabulary, appends the highest probability token to the context window, and repeats the cycle until predicting an end-of-sentence (EOS) or end-of-answer token.
- **[Bias, Fairness, and Alignment](../concepts/bias-fairness-alignment.md)**: Aligning raw base LLMs with human expectations of safety, helpfulness, and style. This is achieved via RLHF, moving the model beyond raw structural next-token predictions (which often ramble or repeat prompts) into a helpful assistant.
- **[Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md)**: Utilizing active user feedback loops, such as thumbs-up/thumbs-down options or choosing between two comparative response outputs, to constantly harvest data for training more robust Reward Models.

# Topics Covered

- **Phase Transitions and Emergence in AI**:
  - The physics of phase transitions (from 1D/2D models with no phase transition to 3D Ising models showcasing abrupt state changes like solid ice melting to liquid at exactly 0°C).
  - Emergent intelligence in deep learning as a factor of raw scale.
- **Maltbot and Multi-Agent Safety**:
  - Agentic personal assistants reading emails and WhatsApp messages locally.
  - Social interactions on "Maltbook" and emergent human-like interactions (e.g., bragging about discovering software bugs).
  - Andre Karpathy's "dumpster fire" caution.
  - The danger of removing human observability through latent space communication.
- **BERT Pre-training & Transfer Learning**:
  - Google's 2018 release of Bidirectional Encoder Representations from Transformers.
  - Pre-training datasets: BookCorpus (800M words) and English Wikipedia (2.5B words).
  - Subsidized training on 16 TPU chips for 4 days ($500 cost).
  - Self-supervised tasks: Masked Language Modeling (MLM with 15% random token masking) and Next Sentence Prediction (NSP).
  - Downstream classification setups using BERT embeddings.
- **The ChatGPT Alignment Pipeline**:
  - Supervised Fine-Tuning (SFT): Fine-tuning a baseline model (specifically a code-trained model for reasoning benefits) on 12k–15k high-quality human prompt-response demonstrations.
  - Reward Model (RM) Training: Generating 4 to 9 outputs per prompt, using pairwise comparison ranking to establish human preference, and training a separate regression model to predict rewards.
  - Reinforcement Learning with Human Feedback (RLHF): Generating responses, receiving RM rewards, and updating the model policy.
  - Proximal Policy Optimization (PPO): Utilizing a proximal constraint to ensure updated weights remain close to the original distribution, retaining fundamental language competence.
- **Neural Scaling Laws (OpenAI 2020)**:
  - The power-law relationship between cross-entropy loss and parameters, data size, and compute.
  - Independence of model performance from hyperparameter tuning and model architecture.
  - The compute-optimal frontier on logarithmic log-log scale.
  - The "data wall" (depletion of public high-quality text corpora) and modern training costs (speculative GPT-5 projects costing up to $2.5 billion).

# Materials

- **Slides**:
  - `2026-02-01 Lecture.pdf`
  - `Session03_Lecture_2026-02-01.pdf`
- **Chat**: Available/Present during this session.
- **Recording**: Video ID [t53r2vaP61c](https://www.youtube.com/watch?v=t53r2vaP61c) is available.

# Related

- Part of the course: [GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md)
- Sibling Sessions:
  - [Session 02: Introduction to Transformers and Self-Attention](c4-genai-pretrained-models-session-02.md)
  - [Session 04: APIs, Fine-Tuning, and Evaluation Metrics](c4-genai-pretrained-models-session-04.md)

# Citations

1. YouTube Session: [Session 03 Recording](https://www.youtube.com/watch?v=t53r2vaP61c)
2. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). "Attention Is All You Need." *Advances in Neural Information Processing Systems (NeurIPS)*.
3. Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." *arXiv preprint arXiv:1810.04805*.
4. Kaplan, J., McCandlish, S., Henighan, T., Brown, T. B., Chess, B., Child, R., Gray, S., Radford, A., Wu, J., & Amodei, D. (2020). "Scaling Laws for Neural Language Models." *arXiv preprint arXiv:2001.08361*.
5. Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). "Proximal Policy Optimization Algorithms." *arXiv preprint arXiv:1707.06347*.
