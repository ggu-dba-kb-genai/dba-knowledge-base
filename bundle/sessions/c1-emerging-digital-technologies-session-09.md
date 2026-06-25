---
type: Session
resource: https://www.youtube.com/watch?v=AciwiIRi-pU
title: 'Session 09: Introduction to Robotic Process Automation (RPA) & Intelligent
  Automation'
description: An interactive introduction to Robotic Process Automation (RPA), contrasting
  rule-based bots with AI agents, analyzing attended vs. unattended models, and discussing
  enterprise automation ROI.
tags:
- Robotic Process Automation
- Intelligent Process Automation
- UiPath
- AI Agents
- Business Process Management
- Change Management
timestamp: '2025-08-10'
---

The session, led by Dr. Vin Chadri, provides a comprehensive introduction to Robotic Process Automation (RPA) and its evolution toward Intelligent Process Automation (IPA). Designed as a highly interactive, bidirectional exchange, the lecture uses a blank agenda to invite student input from diverse professional leadership backgrounds. The core theme revolves around understanding the operational boundaries of automation technologies: what they can do, what they cannot do, and how organizations must evaluate them from a strategic, financial, and operational standpoint.

The class actively decodes the concept of "software bots," clearing common misconceptions by defining them as computer-coded, autonomous software rather than physical, moving machinery. The historical evolution of RPA is traced back to memory macros and screen scraping, with modern platforms (such as UiPath and Automation Anywhere) serving as low-code or no-code drag-and-drop systems that consolidate cross-platform workflows. A major segment of the lecture is dedicated to contrasting rule-based RPA bots with LLM-driven AI agents, defining a spectrum of automation that spans from basic desktop scripts to cognitive, self-healing, and context-aware intelligent systems.

Enterprise implementation issues dominate the class discussions, particularly around Return on Investment (ROI), Full-Time Equivalent (FTE) savings, and change management. Students from banking and manufacturing sectors share real-world experiences with automation scaling limitations, including selector breaks from UI updates, high maintenance overhead due to shifting upstream/downstream environments, and the critical importance of secure enterprise access. The session wraps up with practical guidelines on setting up UiPath and Microsoft Power Automate for upcoming hands-on exercises.

# Key Concepts

* **[Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md)** — The class contrasts the "obedient clerk" nature of rule-based RPA bots with the goal-oriented, self-improving nature of AI agents that leverage real-time reasoning and LLMs. The integration of the two approaches forms Intelligent Process Automation (IPA).
* **[Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md)** — Explored through "prompting psychology," including positive reinforcement techniques (e.g., promising an LLM to mark it as a "top performer" for accurate outputs) and negative reinforcement (e.g., correcting an LLM error loop with a frustrated prompt).
* **[Computer Vision](../concepts/computer-vision.md)** — Explored as a key enabler for advanced IPA, allowing bots to parse semi-structured and unstructured data, such as scanning handwritten documents, conducting optical character recognition (OCR) on invoices, and extracting details from diverse UI screens.
* **[AI Governance and Compliance](../concepts/ai-governance-compliance.md)** — Discussed in the context of framing rules, ethical considerations for data handling, and deploying RPA operating models that adhere to enterprise-wide standards and auditing requirements.
* **[AI Security and Robustness](../concepts/ai-security-robustness.md)** — Examines the safety and data-exposure risks associated with granting third-party bots (e.g., UiPath) direct access to core Enterprise Resource Planning (ERP) databases, highlighting the need for secure virtual machine (VM) environments and service principal accounts.

# Topics Covered

## 1. Introduction and Learning Outcomes
* **Course Context**: Brief overview of the Emerging Digital Technologies course, target outcomes, credits, and the final practical project aimed at bringing tangible business benefits.
* **Instructor Profile**: Introduction to Dr. Vin Chadri's academic and industry background in AI, Internet of Things (IoT), and data science.
* **Blank Agenda Philosophy**: The rationale for maintaining an open agenda to foster bi-directional learning and custom-tailored industry discussions.

## 2. Decoding RPA: Software Bots and Macro Roots
* **Defining RPA**: Deconstructing "Robotic Process Automation" into rule-based process execution without human intervention.
* **The Concept of Micro/Macro**: Defining how modern RPA acts as a consolidated pipeline of multiple, cross-platform macros stored in memory to execute repetitive tasks.
* **No-Code vs. Low-Code**: The transition of automation tools from hardcoded script-based mechanisms to drag-and-drop orchestration interfaces.

## 3. RPA Bots vs. AI Agents
* **The Analogy**: RPA bots act like highly obedient office clerks following a step-by-step checklist. AI agents act like smart, proactive colleagues who understand high-level goals and adapt their path on the fly.
* **Data Paradigms**: RPA primarily manages structured data, while AI agents excel in analyzing highly unstructured data (e.g., screening resumes based on holistic profiles).
* **Coexistence**: Real-world examples of combining both technologies (e.g., using an RPA bot for initial rule-based filtering of candidate education, then feeding the candidates into an AI agent for qualitative profiling).
* **Financial and Environmental (ESG) Metrics**: Choosing RPA over AI agents for simple rule-based tasks reduces computing costs and fits environmental metrics better than running resource-heavy LLM queries.

## 4. Business Dynamics: ROI, Maintenance, and Workforce Repurposing
* **The FTE Sponsoring Debate**: Discussing how financial backing for automation projects often relies on demonstrating tangible FTE (Full-Time Equivalent) reductions.
* **Repurposing vs. Replacing**: Transitioning the corporate terminology from human "replacement" to "repurposing" and "upskilling" through change management.
* **Scalability and Maintenance Challenges**: Why RPA systems can be fragile and high-maintenance, as any upstream change in document formats, API contracts, or UI layouts can break the bot’s selectors.

## 5. Technical Classifications and Stages of Automation
* **Attended vs. Unattended Robots**:
  * *Attended Bots (RDA)*: Run on a local desktop, require user triggers, work alongside humans, and keep final decision-making in human hands.
  * *Unattended Bots (RPA)*: Run on central servers, run autonomously based on scheduling/triggers, and are monitored from a central control panel.
* **The Three Stages of Automation**:
  * *Basic*: Single macro, shell scripting, auto-formatting spreadsheets.
  * *Intermediate*: Workflow automation (RPA), structured data matching, automated chatbots with pre-recorded FAQs.
  * *Intelligent (IPA)*: RPA combined with AI, NLP, computer vision, sentiment/intent detection, and real-time reasoning.

## 6. Prompting Psychology and Real-Time Hallucinations
* **Negative vs. Positive LLM Prompts**:
  * Dr. Vin Chadri's anecdote about prompting GPT-5 with frustration to break an error loop.
  * Student J. Mahajan's recommendation of positive reinforcement (e.g., prompting the LLM with, *"I will mark you as a top performer in my team if you provide the correct format"*).
* **Real-time Hallucinations**: Analyzing Google’s AI Overview bot incorrectly calculating Saturdays for banking holidays as an example of LLM reasoning limitations.

## 7. Next Steps and Practical Preparation
* **UiPath Setup**: Instructions for downloading the UiPath free desktop edition and creating a cloud account for studio online.
* **Microsoft Power Apps & Power Automate**: Brief overview of using Power Automate online with student Microsoft credentials for cloud-based process modeling.

# Materials

* **Video Recording**: Accessible via YouTube link (`https://www.youtube.com/watch?v=AciwiIRi-pU`).
* **Slides**: Distributed by the instructor, containing comparative matrices of RDA vs. RPA vs. IPA and technical architecture diagrams.
* **Chat**: Active student participation discussing Selenium vs. UiPath, automated contract management in healthcare, and prompting methods.

# Related

* Part of the **[Emerging Digital Technologies](../courses/c1-emerging-digital-technologies.md)** course.
* Previous Session: **[Session 08: Foundations of Digital Automation](c1-emerging-digital-technologies-session-08.md)**
* Next Session: **[Session 10: Hands-On RPA with UiPath & Power Automate](c1-emerging-digital-technologies-session-10.md)**

# Citations

1. GGU Course 1: Emerging Digital Technologies, Session 09 Lecture Video (`https://www.youtube.com/watch?v=AciwiIRi-pU`).
2. UiPath Academic Alliance and Free Community Cloud Licensing Portal (`https://www.uipath.com/`).
3. Hugging Face AI Agent Repositories and Open-Source Frameworks (`https://huggingface.co/`).
