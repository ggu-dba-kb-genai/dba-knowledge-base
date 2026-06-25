---
type: Session
resource: https://www.youtube.com/watch?v=AjJsZKA9aKM
title: 'Session 15: Natural Language Processing Applications — Chatbots, RAG, and
  Named Entity Recognition'
description: A hands-on transition from computer vision to NLP applications, covering
  API-driven chatbots with Groq and LangChain, local PDF-based RAG pipelines using
  FLAN-T5 and FAISS, and Named Entity Recognition with spaCy.
tags:
- NLP
- Chatbots
- RAG
- Groq
- LangChain
- spaCy
- Gradio
- Named-Entity-Recognition
- Vector-Embeddings
- Transformers
timestamp: '2026-01-11'
---

This session serves as the concluding lecture of the [Deep Learning](../courses/c3-deep-learning.md) course, marking a transition from [computer vision](../concepts/computer-vision.md) into Natural Language Processing (NLP) and [generative modeling](../concepts/generative-modeling.md). The instructor recaps the program's progression—from data analytics and machine learning to deep learning models (such as DenseNet) implemented on PyTorch and Azure—before detailing the core NLP applications: chatbots, semantic search, sentiment analysis, text summarization, and named entity recognition. Rather than focusing solely on theory, this session is highly hands-on, guiding students through practical implementations in Google Colab to build local and API-driven systems.

The class covers three main practical implementations. First, students build a cloud-based text-to-text chatbot using the Groq inference platform, leveraging the LangChain framework to orchestrate API calls to open-source models like `Qwen`. Second, the session addresses enterprise-specific search and data privacy by constructing a local [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) application on a Colab T4 GPU runtime. This local pipeline processes PDF documents, breaks them into chunks, embeds them using a sentence transformer model, stores them in a FAISS vector database, and generates context-grounded answers using Google's `FLAN-T5` model via a Gradio interface.

Lastly, the session introduces Named Entity Recognition (NER), demonstrating how to build a web application using spaCy and Gradio to parse text and automatically label entities. The lecture highlights how context shapes entity extraction (e.g., identifying "Apple" as an organization versus a fruit) and previews how these foundational NLP mechanics undergird the subsequent course on [GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md).

# Key Concepts

- **[Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)** — An architecture that connects LLMs to external, dynamic knowledge bases (such as uploaded PDFs) via vector search to reduce hallucinations and ground model outputs in factual data.
- **Open-Source vs. Closed-Source LLMs** — Open-source models (like Qwen and FLAN-T5) allow users to inspect, clone, modify, and host weights locally for complete data privacy. Closed-source models (such as GPT-4 or Gemini) are proprietary services accessed via commercial APIs.
- **[Embeddings and Vector Representations](../concepts/embeddings-and-representations.md)** — The transformation of discrete, high-dimensional text chunks into dense, continuous low-dimensional vector spaces (such as using `all-MiniLM-L6-v2`) to capture semantic meaning and enable similarity search.
- **[Attention Mechanisms and Transformers](../concepts/attention-and-transformers.md)** — Sequence-processing architectures relying on self-attention to dynamically weigh relationships between tokens, forming the backbone of modern LLMs like FLAN-T5.
- **Named Entity Recognition (NER)** — An NLP sequence-labeling task that identifies and categorizes key entities (e.g., Person, Organization, Date, Location) in unstructured text, relying on contextual cues for semantic disambiguation.
- **Application Programming Interfaces (APIs)** — Acting as a bridge, APIs allow lightweight applications to interact with large hosted models (like those on Groq) without requiring local storage or heavy hardware resources.

# Topics Covered

- **Introduction to NLP & GenAI Course Alignment**
  - Review of the course trajectory (Analytics -> Machine Learning -> Deep Learning & Computer Vision -> NLP -> GenAI).
  - Introduction to core NLP applications: Chatbots, Semantic Search/RAG, Named Entity Recognition, Sentiment Analysis, and Text Summarization.
- **Lab 1: Building an API-Driven Chatbot with Groq and LangChain**
  - Creating, verifying, and storing API keys securely on the Groq Console.
  - Setting up environments in Google Colab using `getpass` to prompt for `GROQ_API_KEY`.
  - Instantiating the `ChatGroq` class and using `llm.invoke()` to request text completion from open-source models (e.g., Qwen).
  - Analyzing JSON completion outputs, token usage, and latency matrices.
- **Lab 2: Local PDF Q&A Chatbot via RAG**
  - Highlighting data privacy concerns and local hosting solutions.
  - Changing Colab runtimes to T4 GPU accelerators.
  - Installing dependencies: `gradio`, `pypdf`, `sentence-transformers`, and `faiss-cpu`.
  - The RAG pipeline workflow:
    1. Parsing PDFs using PyPDF.
    2. Text chunking and sentence-level segmentation.
    3. Generating dense embeddings using Hugging Face's `all-MiniLM-L6-v2`.
    4. Storing vectors and running Cosine Similarity search with FAISS.
    5. Contextual synthesis using `google/flan-t5-base` as the generator.
  - Creating an interactive, dual-input Gradio web interface for PDF uploads and text queries.
- **Lab 3: Named Entity Recognition (NER) Web Application**
  - Integrating python libraries `spacy` and `gradio` (specifically, `spacy-gradio`).
  - Leveraging AI coding assistants within Colab to generate boilerplates for model loading and entity extraction pipelines.
  - Interactive testing of NER contextual disambiguation (e.g., classifying "Apple" as an Organization in "Steve Jobs founded Apple" vs. "apple" as a noun/fruit in "Yesterday I ate an apple").

# Materials

- Google Colab notebooks for:
  - Groq & LangChain Chatbot.
  - Local Flan-T5 PDF RAG Application.
  - spaCy & Gradio Named Entity Recognition (NER).
- Class chat logs are preserved and active.
- Session recording available on YouTube.

# Related

- Part of [Deep Learning](../courses/c3-deep-learning.md) (Session 15 of 15).
- Sibling Session: [Session 14: Computer Vision Lab and Deployment](c3-deep-learning-session-14.md).
- Next Course: [GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md), starting with [Session 01: Introduction to Generative AI](c4-genai-pretrained-models-session-01.md).

# Citations

1. YouTube Session Recording. "Session 15: Natural Language Processing Applications." [https://www.youtube.com/watch?v=AjJsZKA9aKM](https://www.youtube.com/watch?v=AjJsZKA9aKM)
2. Groq Developer Portal. "Groq Console and API Reference." [groq.com](https://groq.com)
3. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). "Attention Is All You Need." Google Brain. [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)
4. Hugging Face Model Hub. "google/flan-t5-base Model Card." [huggingface.co/google/flan-t5-base](https://huggingface.co/google/flan-t5-base)
5. spaCy API Reference. "spaCy: Industrial-Strength Natural Language Processing in Python." [spacy.io](https://spacy.io)
