---
type: Session
resource: https://www.youtube.com/watch?v=URwbBTEL4NE
title: 'Session 02: From Word Embeddings & RNNs to the Transformer Architecture'
description: An in-depth exploration of language modeling foundations, tracing the
  evolution from rules-based NLP and sequential RNNs/LSTMs to the parallelizable self-attention
  mechanism of Transformers.
tags:
- natural-language-processing
- tokenization
- word-embeddings
- word2vec
- recurrent-neural-networks
- lstm
- attention-mechanism
- transformers
- multi-headed-attention
timestamp: '2026-01-25'
---

In the second session of the *GenAI Pretrained Models* course, the class transitions from a high-level conceptual landscape into the technical foundations of natural language processing (NLP). The lecture explores the fundamental problem of language comprehension: how to represent the rich context and semantic associations of human speech in a form that computers can compute. The evolution of language modeling is traced through its major historical milestones, starting with rules-based dictionary parsers and progressing to continuous vector spaces and deep learning sequences.

A major focus of the session is Google’s seminal 2013 Word2Vec breakthrough, which showed that words could be converted into high-dimensional vector spaces. By learning positions based on surrounding words in a large text corpus, these embeddings encode semantic relationships geometrically, enabling word-level vector arithmetic (such as subtracting country contexts from capital cities, e.g., `Paris - France + England = London`). The lecture also details why early sequential architectures, namely Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks, faced inherent bottlenecks. Due to vanishing gradients and sequential dependency, these architectures lost context over long passages and resisted hardware parallelization on GPUs, rendering internet-scale training impossible.

The lecture culminates in the introduction of the Transformer architecture, derived from Google’s landmark 2017 paper *"Attention Is All You Need"*. By abandoning recurrent steps entirely in favor of self-attention mechanisms, Transformers compute relationships between all words in a context window simultaneously. Multi-headed attention is explained as multiple "specialist" departments analyzing a document in parallel (such as syntax, grammar, or liability). This paradigm shift completely altered the economics of model training, laying the mathematical foundation for today’s large language models (LLMs) and context windows that span from hundreds of tokens to millions.

# Key Concepts

- **Subword Tokenization** — The practice of breaking text down into meaningful subword components (roots, prefixes, and suffixes) rather than full words or individual characters. Modern models like GPT use this approach to handle spelling variations, rare vocabulary, and misspellings while maintaining a compact vocabulary dictionary.
- **[Embeddings and Vector Representations](../concepts/embeddings-and-representations.md)** — Mapping discrete tokens to continuous high-dimensional vector spaces (such as Google’s 512-dimension Word2Vec vectors) where geometric proximity reflects semantic similarity. The concept of mapping unstructured relationships to vectors is also applied widely in industrial recommendation models (e.g., Spotify's song embeddings or Netflix's movie recommendations).
- **Recurrent Neural Networks (RNNs)** — Early [Neural Network Architectures](../concepts/neural-network-architectures.md) designed for sequential data by maintaining an internal running state. While sequential step-by-step nature caused gradient problems, struggled with context beyond 100–200 words, and could not be parallelized.
- **Long Short-Term Memory (LSTMs)** — An engineering fix to RNN memory loss, introducing a "Long-Term Memory Lane" along with complex gating mechanisms (Forget, Input, and Output gates). While LSTMs succeeded in extending memory, their sequential bureaucracy made them extremely slow and computationally expensive to train on internet-scale text.
- **Encoder-Decoder Translation Model** — A sequence-to-sequence structure where an encoder RNN/LSTM compresses input sentences into a static context vector bottleneck before a decoder reconstructs the translated output token-by-token.
- **[Attention Mechanisms and Transformers](../concepts/attention-and-transformers.md)** — The architecture that processes an entire context window at one shot rather than sequentially. The self-attention block serves as a dynamic context finder, modifying a word's vector representation (e.g., pushing the ambiguous word "Apple" closer to "fruit" or "technology") depending on adjacent words.
- **Multi-Headed Attention** — A system of multiple attention heads operating in parallel. Each head acts as a specialist analyzing distinct textual attributes, such as mapping adjectives to nouns, aligning subjects with objects, or tracking narrative timelines.
- **[Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md)** — Designing input contexts to direct generative outputs. Since self-attention maps the entire prompt in a single parallel operation, introductory framing (e.g., "You are a professional writer") directly influences the vector representations of all subsequent tokens processed within that context.

# Topics Covered

- **The Problem of Language Understanding** — Transitioning from rules-based dictionaries (NLTK) to continuous mathematical representations of meaning.
- **Machine Learning for Text Classification** — Bag-of-words representation, binary matrix codification, and limitations of cold, tabular sparse arrays (lack of semantics, failure with synonyms).
- **Vector Space Mathematics** — Performing vector addition and subtraction with semantic constructs (e.g., `Paris - France + England = London` or finding chess players via subtraction and addition of countries).
- **Behavioral and Product Embeddings** — Translating word-vector logic to Spotify (behavior2vec/song2vec), Netflix (movie2vec), and Amazon product recommendations.
- **Sequential Context Bottlenecks** — The mathematical constraints of RNNs and LSTMs, sequential message decay (the "telephone game"), and vanishing gradient challenges.
- **Encoder-Decoder Translation Models** — How sequential architectures compress input strings into static bottleneck context vectors before reconstructing them word-by-word into target languages.
- **The Self-Attention Breakthrough** — Moving from sequential dependencies to universal matrix-vector operations, unlocking parallel GPU training economics.
- **Scaling Context Windows** — The trajectory of model capacities from 512 tokens in 2017 to modern multi-million token context windows.

# Materials

- **Slides**:
  - `2026-01-25 Lecture.pdf`
  - `Session02_Lecture_2026-01-25.pdf`
- **Chat**: Present (student-instructor chat log of live session questions and answers).
- **Recording**: Available via YouTube with video ID [URwbBTEL4NE](https://www.youtube.com/watch?v=URwbBTEL4NE).

# Related

- Sibling Sessions:
  - [Session 01: Course Introduction & Generative AI Landscape](c4-genai-pretrained-models-session-01.md)
  - [Session 03](c4-genai-pretrained-models-session-03.md)
- Part of the course: [GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md)

# Citations

1. YouTube Session Recording: `https://www.youtube.com/watch?v=URwbBTEL4NE`
2. Word2Vec Breakthrough: Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). *Efficient Estimation of Word Representations in Vector Space*. arXiv preprint arXiv:1301.3781.
3. Transformer Architecture: Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). *Attention Is All You Need*. Advances in Neural Information Processing Systems, 30.
