---
type: Session
resource: https://www.youtube.com/watch?v=HvRi5hVeIQM
title: 'Session 12: Visual RAG Pipelines with Langflow & Astra DB'
description: A hands-on workshop building, configuring, and deploying Retrieval-Augmented
  Generation (RAG) pipelines visually using Langflow, Astra DB, and Azure OpenAI.
tags:
- RAG
- Langflow
- Astra-DB
- Embeddings
- Azure-OpenAI
- Vector-Databases
- Ingestion
- Retrieval-Flow
timestamp: '2026-03-14'
---

This session is a hands-on, practical workshop led by Dr. Yogesh, focusing on the visual construction, configuration, and implementation of Retrieval-Augmented Generation (RAG) pipelines. Using the visual orchestration tool **Langflow** coupled with **DataStax Astra DB** as a cloud NoSQL vector database and **Azure OpenAI Service**, students build and deploy two distinct pipelines: a Data Ingestion flow and a Retrieval & Generation flow. This lab guides students from basic prompt configuration to a production-like RAG application that grounds model output in a custom knowledge base (such as a resume or document) to prevent model hallucinations.

In the Data Ingestion flow, raw documents (e.g., PDFs) are processed by a document loader, split into semantic chunks (using a text splitter with a chunk size of 1000 tokens and 200 overlap to maintain contextual continuity), and converted into 1536-dimensional vector representations using Azure OpenAI's `text-embedding-ada-002` model. These embeddings are then stored in Astra DB, which runs Apache Cassandra under the hood. In the Retrieval & Generation flow, user queries are embedded on-the-fly and queried against the vector database using cosine similarity. The retrieved chunks are formatted as a data frame, parsed into text, and fed into the context window of Azure's text generation model, grounding the response directly in the ingested knowledge.

The session concludes with an in-depth discussion on productionization and architectural trade-offs. While low-code platforms like Langflow are highly effective for rapid prototyping and debugging, the instructor explains that production systems are typically developed programmatically using frameworks like **LangGraph** to support complex state management, concurrent processing, and human-in-the-loop validation. They also address enterprise deployment patterns, such as offline on-premise RAG using **Ollama** for hosting local models, **Chroma** or containerized **MongoDB** as local vector stores, and the **Model Context Protocol (MCP)** as an emerging standard for exposing pipeline services as client endpoints.

# Key Concepts

- **[Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)** — An architecture connecting foundational LLMs to external, dynamic knowledge bases using vector search to ground model responses in custom document context and minimize hallucinations.
- **[Embeddings and Vector Representations](../concepts/embeddings-and-representations.md)** — The transformation of high-dimensional textual information into dense, low-dimensional vector spaces (such as the 1536-dimensional space of Azure OpenAI's `text-embedding-ada-002` model) to facilitate semantic similarity searches.
- **[Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md)** — Designing prompt templates, system instructions, and dynamic context windows to constrain generative model outputs based on custom reference documents.
- **[AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md)** — Transitioning pipelines from prototypes to production using containerization (Docker), infrastructure-as-code (Terraform), and package dependency pinning to ensure deployment robustness.
- **[Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md)** — Architecting reliable agentic workflows featuring human checkpoints, safety filters, and stateful tracking, typically implemented programmatically via LangGraph.

# Topics Covered

- **Initial Setup & Environment Configuration**
  - Provisioning Azure OpenAI resources under custom lab subscriptions (utilizing incognito browser modes to bypass corporate authenticator conflicts).
  - Deploying two primary Azure models: `text-embedding-ada-002` (for vector embeddings) and `gpt-4.1` (for text generation).
  - Setting up DataStax Astra DB (managed Apache Cassandra) serverless cloud instances and generating Database Administrator API tokens.
- **Flow 1: Basic Prompting Pipeline**
  - Connecting `Chat Input`, `Azure OpenAI Model`, and `Chat Output` components within Langflow.
  - Setting system prompt personas and testing endpoints with custom queries (e.g., "explain deep learning").
  - Verifying target URLs, API endpoints, deployment names, and managing API key configurations.
- **Flow 2: Data Ingestion (Vector Storage Flow)**
  - Uploading a knowledge base file (e.g., a PDF resume or curriculum vitae) to initiate document loading.
  - Splitting documents into chunks using a `Split Text` component (chunk size of 1000 characters, chunk overlap of 200 characters) to preserve context across boundaries.
  - Generating semantic embeddings and indexing them into a custom Astra DB collection with a defined dimension size of 1536.
- **Flow 3: Retrieval & Generation (RAG Flow)**
  - Transforming live user queries into embeddings on-the-fly.
  - Querying the Astra DB collection using cosine similarity and parsing retrieved documents from a data frame into textual context.
  - Injecting retrieved text context into the text generation model to generate grounded answers (e.g., extracting specific academic degrees or skills from a CV).
- **Production & On-Premise Considerations**
  - Comparing visual drag-and-drop builders to programmatic frameworks like **LangGraph** for enterprise robustness, concurrency, and complex state management.
  - Hosting local offline models using **Ollama** and deploying local vector databases (such as containerized **Chroma** or **MongoDB** via Docker).
  - Exposing visual pipelines programmatically via API keys or using the **Model Context Protocol (MCP)**.

# Materials

- **Recording**: The lecture was recorded live and is available as [HvRi5hVeIQM](https://www.youtube.com/watch?v=HvRi5hVeIQM).
- **Chat**: Present and active during visual pipeline troubleshooting and conceptual discussions.
- **Slides**: None officially shared; this was a fully interactive hands-on programming workshop.

# Related

- Sibling Session: **[Session 11](c4-genai-pretrained-models-session-11.md)**
- Sibling Session: **[Session 13](c4-genai-pretrained-models-session-13.md)**
- Parent Course: **[GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md)**

# Citations

1. Class Lecture Recording: [Session 12 (2026-03-14)](https://www.youtube.com/watch?v=HvRi5hVeIQM).
2. DataStax Astra DB Documentation: [https://docs.datastax.com/en/astra/home/astra.html](https://docs.datastax.com/en/astra/home/astra.html).
3. Langflow Getting Started Guide: [https://docs.langflow.org/](https://docs.langflow.org/).
4. LangGraph Documentation: [https://langchain-ai.github.io/langgraph/](https://langchain-ai.github.io/langgraph/).
5. Ollama Local LLMs: [https://ollama.com/](https://ollama.com/).
