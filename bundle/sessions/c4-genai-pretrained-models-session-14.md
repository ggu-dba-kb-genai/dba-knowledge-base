---
type: Session
resource: https://www.youtube.com/watch?v=cPQQk6xrNfs
title: 'Session 14: Applied GenAI Capstone Presentations (Contracts, Social Welfare,
  Loyalty, and ESG)'
description: A project defense session where student teams present enterprise-grade
  Generative AI capstone solutions ranging from legal contract reasoning to specialized
  welfare access, loyalty prediction, and ESG compliance.
tags:
- capstone
- contract-intelligence
- graph-rag
- loyalty-analytics
- esg-compliance
- saudi-arabia
- social-impact
timestamp: '2026-03-28'
---

This session represents Day 1 of the Capstone Project presentations for the *GenAI Pretrained Models* course. Rather than a traditional lecture, this session serves as a project defense where student teams present end-to-end business solutions leveraging generative AI, specialized retrieval architectures, and hybrid modeling. The presentations are evaluated live by both the course professor (60% weight) and peer groups (40% weight) across four core rubrics: business value, technical approach, metrics & validation, and defense of approach.

The session showcases four major project proposals, demonstrating how advanced generative AI techniques can be applied to real-world industrial and social problems:
*   **Credentia** (Group 7): An AI-powered contract intelligence platform tailored for small and medium-sized enterprises (SMEs) to parse complex legal agreements, detect hidden liabilities, and conduct cross-clause semantic reasoning.
*   **Summer School** (Group 6): A social impact system that matches children with special needs (CWSN) in India to eligible government welfare schemes using a hybrid Graph RAG pipeline.
*   **Loyalty Intelligence Platform** (Group 9): A customer-retention ecosystem for D2C brands that combines classical machine learning for churn prediction with generative agents for personalized customer engagement.
*   **ESG Compliance Intelligence Layer** (Second Group 9): A carbon footprint and sustainability reporting platform designed for GCC-based enterprises to automate audit-grade regulatory disclosures.

# Key Concepts

*   **Cross-Clause Semantic Reasoning** — Highlighted in the *Credentia* project as a core technological differentiator. Unlike standard tools that analyze legal clauses in isolation, Credentia uses its proprietary *ACRA (Adaptive Contract Risk Agent)* engine to evaluate how different clauses interact (for example, verifying if an indemnity clause overrides or conflicts with a limitation of liability cap).
*   [Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md) — Used extensively across the projects to ground LLMs in authoritative documents. For example, the ESG compliance tool utilizes over 5,000 vector representations of international standards to eliminate hallucinations during disclosure drafting.
*   [Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md) — Implemented as orchestrators and task-specific reasoning agents. Credentia relies on multi-agent collaboration to route tasks like clause extraction, classification, and risk evaluation to specialized underlying models.
*   [Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md) — Showcased via Credentia's *Dynamic Prompt Composition* layer, which assembles complex prompts at runtime by combining industry templates, customer policy rules, jurisdictional guidelines, and risk taxonomies based on document metadata.
*   **Graph RAG** — Adopted by the *Summer School* team to handle highly complex, multi-variable constraint filtering. By marrying a Neo4j Graph Database (for precise eligibility matching on age, state, disability type, and family income) with a vector-based RAG pipeline, the system achieves perfect factual grounding without hallucinating eligibility status.
*   [Explainable AI (XAI)](../concepts/explainable-ai.md) — Utilized by the *Loyalty Intelligence Platform* team. They implement SHAP (SHapley Additive exPlanations) and LIME (Local Interpretable Model-agnostic Explanations) to provide product managers with clear transparency regarding why the supervised model flagged a specific customer as a high churn risk.
*   [Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md) — Designed as safety nets across all student architectures. These include human-in-the-loop escalation paths for high-risk legal contract reviews, real-time prompt guardrails, and deterministic mathematical blocks to prevent models from generating inaccurate metrics.
*   [Model Evaluation and Validation](../concepts/model-evaluation-validation.md) — Explored through the validation strategies of generative pipelines, ensuring high alignment with professional human outputs prior to production deployment.
*   [Embeddings and Vector Representations](../concepts/embeddings-and-representations.md) — Applied to transform unstructured compliance PDFs, policy papers, and legal textbooks into search-ready vector databases.
*   [AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md) — Utilized by the *Loyalty Intelligence Platform* team for tracking and analytics using MLflow to measure token costs, latency, and data drift.
*   [AI Governance and Compliance](../concepts/ai-governance-compliance.md) — The central focus of the *ESG Compliance Intelligence Layer* to automate environmental, social, and governance reporting aligned with regulatory standards.

# Topics Covered

*   **Capstone Defense Setup & Peer Grading**
    *   Explanation of the 10-point evaluation sheet template.
    *   Distribution of the grading weight: 60% professor-led, 40% peer-led.
    *   Explanation of the grading metrics: Business Value, Technical Approach, Metrics & Validation, and Defense of Approach.
*   **Credentia: SME Contract Intelligence Platform (Group 7)**
    *   *The Business Challenge*: SME resource gaps, operational delays in contract reviews (taking 2 to 5 days), and hidden multi-clause liabilities resulting in average revenue leakage of 9%.
    *   *ACRA Reasoning Layer*: Moving beyond simple semantic clause matching to contract-level interaction mapping (e.g., matching a broad indemnity clause with a limited liability cap).
    *   *System Architecture*: Model orchestration (routing specialized tasks to models), RAG vectors (jurisdictional policies, guidelines), application backend/UI, and hybrid human-in-the-loop escalation for complex or high-risk contracts.
    *   *Local Privacy Agent*: Implementing a local client-side agent to mask and filter sensitive contract data before routing metadata to the cloud, addressing corporate compliance and data leakage concerns.
    *   *Product Road Map*:
        *   Phase 1 (Year 1): Basic generative models and multi-RAG integration for company policy rules.
        *   Phase 2 (Year 2): Jurisdictional awareness (comparing rules across geographies) and negotiation tip engines.
        *   Phase 3 (Year 3): Multilingual support (specifically Arabic and English dual-contract alignment) and risk dashboards.
    *   *Financial and ROI Modeling*:
        *   Primary review savings: From 2 hours down to 1 hour per contract. At an average of 300 contracts annually and $40/hour labor cost, this saves $12,000.
        *   Secondary legal escalation: 20% of contracts escalated (60 contracts). Reducing external legal fees by 30% saves $4,500.
        *   Total annual savings: $16,500 against an annual subscription of $8,000, yielding a **106.25% SME ROI**.
        *   Developer economics: Targeting 50 subscription sales annually to generate $400k revenue against $180k operating expenses, achieving a $220k margin.
    *   *Live MVP Demo*: Software service agreement reviewed live. Changing the jurisdiction from Ontario, Canada to England dynamically updates the contract risk score from 5 to 6 out of 10 and highlights regulatory conflicts.
*   **Summer School: Social Welfare Scheme Navigator (Group 6)**
    *   *The Last-Mile Distribution Gap*: Over 2,000 crore rupees in government welfare budgets for children with special needs (CWSN) remains under-utilized in India due to massive systemic complexity (50 schemes, 21 disabilities, 28 states, 22 languages). 84% of eligible families are unaware of existing schemes, and 70% cannot apply due to a lack of foundational certificates.
    *   *Graph RAG Architecture*: Using Neo4j Graph DB with Cypher queries to handle strict constraint matching (e.g., Locomotor disability, 12 years old, Karnataka state, income < 15 lakhs) simultaneously. Traditional RAG fails to intersect these constraints without hallucinating eligibility. Uses Vector RAG (LangChain) to generate plain-text explanations, application steps, and document checklists.
    *   *Go-To-Market (GTM) Strategy*: Equipping District CWSN coordinators under the Samagra Shiksha program and partnering with local NGOs (e.g., Samarthanam Trust, CBm India) to distribute the tool. Distributed via WhatsApp (leveraging India's 500M+ WhatsApp user base), integrating English, Hindi, and voice assistants, with plans to scale using the Bhashini translation model.
    *   *Financial and Social ROI Modeling*: Unlocking government schemes (scholarships, assistive devices) yields an average of 3,200 INR per child annually. Unit economics: Query cost is 0.25 INR (25 paise), meaning **every rupee spent unlocks 12,800 INR of social value**. Year 1 budget of 41 lakhs (50 schools), scaling in Year 3 to 500 schools (2.1 CR investment, unlocking 6 CR value).
*   **Loyalty Intelligence Platform for SMEs (Group 9)**
    *   *The Business Challenge*: Transaction data fragmentation and customer drift leading to high churn, rising acquisition costs, and low conversion of generic marketing campaigns.
    *   *System Architecture*:
        *   *System A (Supervised ML)*: Weekly batch churn prediction on MySQL transactional data (using 2-3 years of data to limit variance). Deployed via Azure Data Factory with PowerBI dashboards and [Explainable AI (XAI)](../concepts/explainable-ai.md) (SHAP/LIME) to provide transparency on churn risks.
        *   *System B (Generative AI)*: React front-end, Redis caching (securing tenant IDs and reward points to prevent cross-tenant leaks), and Gremlin graph database on Azure (indexing policy PDFs via LLM Graph Transformers). Employs Azure AI Search for hybrid semantic/token queries (50/50 keyword and semantic search) with real-time guardrails and AKS (Azure Kubernetes Service) for scaling from 10k to 100k users.
        *   *System C (Data Management Dashboard)*: Management panel with JWT/Azure AD for product managers. Tracks MLOps metrics using MLflow (latency, LLM tokens) and features a "Loyalty Co-pilot" to support human agents during escalations.
    *   *Strategic Road Map & Projections*: Phased deployment starting narrow. Months 1-2 build the churn/campaign engine (System A) to deliver immediate ROI, with advanced systems layered progressively. Three-year build investment is $1.86 million, achieving break-even at 40 active "Growth" tier clients.
*   **ESG Compliance Intelligence Layer (Second Group 9)**
    *   *The Compliance Crisis*: Escalating complexity of international (GRI, SASB, TCFD) and regional (Saudi Exchange, Saudi CMA, GCC) sustainability disclosures.
    *   *Deterministic Hybrid Solution*: Decoupling narrative writing from mathematical calculations to completely eliminate hallucination.
        *   *Mathematics*: Handled by a deterministic Python execution layer that parses CSV/utility bills and computes greenhouse gas emissions (Scope 1, 2, and 3) using regulatory emission factors.
        *   *Narrative*: Handled by Claude 3.5 Sonnet to draft compliance narratives and gap analyses.
        *   *RAG & Vector Base*: 5,000+ vector representations of ESG frameworks (GRI, SASB, TCFD, Saudi CMA) in Pinecone via LangChain. Employs contextual retrieval (top 30 regulatory paragraphs) to ground prompt instructions in exact regulations.
    *   *Live MVP Demo*: Onboarding enterprise dashboard showing overall ESG scores. Features: Automatic onboarding, dynamic gap analysis (complete, partial, missing, high-risk items with remediation tips), benchmark comparison against industry averages, conversational ESG advisor, and multi-format reports (PDF, HTML, DOCX, XBRL) with Arabic language support.
    *   *Business Model & ROI*: Tiered subscription model ranging from 4,500 SAR/month (Starter) to 55,000 SAR/month (Advisory/Government). Year 1 revenue projected at 4.7 million SAR across 18 clients, scaling to 21 million SAR in Year 3 with a 74% margin. Total build investment is 12.4 million SAR, reaching break-even in 19 months with a 94% IRR.

# Materials

*   **Slides**: None explicitly attached to the metadata, though slide decks were presented live by all four teams.
*   **Chat Log**: Available on disk and utilized during evaluations.
*   **Recording**: YouTube video [cPQQk6xrNfs](https://www.youtube.com/watch?v=cPQQk6xrNfs) captures the complete presentation session and Q&A.

# Related

*   Part of the **[GenAI Pretrained Models](../courses/c4-genai-pretrained-models.md)** course.
*   Previous session: **[Session 13](c4-genai-pretrained-models-session-13.md)** (covering advanced deployment and API integrations).
*   Next session: **[Session 15](c4-genai-pretrained-models-session-15.md)** (representing Day 2 of the Capstone Project presentations).

# Citations

1.  **Primary Lecture Video**: Course 4, Session 14, recorded on March 28, 2026. Available at [https://www.youtube.com/watch?v=cPQQk6xrNfs](https://www.youtube.com/watch?v=cPQQk6xrNfs).
2.  **Rights of Persons with Disabilities Act (RPWD), India 2016**: Cited by the Summer School team as the legal foundation establishing rights and government welfare obligations for disabled citizens.
3.  **Global Reporting Initiative (GRI) Standards (2021)**: Cited by the ESG compliance team as the foundational reporting framework ingested into their compliance vector store.
4.  **Task Force on Climate-related Financial Disclosures (TCFD) Framework**: Utilized by the ESG team for structuring risk assessment and environmental disclosure output matrices.
5.  **Anthropic Claude 3.5 Sonnet**: Used as the primary generative narrative model for both the Credentia MVP and the ESG disclosure narrative generation engine.
