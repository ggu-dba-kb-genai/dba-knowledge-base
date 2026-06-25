---
type: Session
resource: https://www.youtube.com/watch?v=QrcwRu9MFXo
title: 'Session 06: Core Prompting Techniques & Security Breaker Exercises'
description: A hands-on session exploring core prompt engineering techniques, API
  implementation, and interactive red-teaming exercises via Gandalf and Agent Breaker.
tags:
- prompt-engineering
- in-context-learning
- ai-security
- red-teaming
- chain-of-thought
- fermi-estimate
- agentic-ai
timestamp: '2026-04-19'
---

This session provides a comprehensive, hands-on exploration of [Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md), emphasizing how variations in generative model outputs are driven by the precision of human instructions rather than the model itself. Bridging from the previous lecture's discussion on requirements and uncertainties, the instructor connects "why outputs are weak" to "why thinking is weak," positioning structured prompting as a core execution skill. Large Language Models (LLMs) process inputs as token sequences and recognize mathematical patterns, making structured prompts essential to close the "intent-context gap." Without specific instructions, roles, and constraints, models typically make assumptions to fill context gaps, which often leads to hallucinations or suboptimal responses.

To address these shortcomings, the class reviews six core prompting techniques: zero-shot, few-shot, Chain-of-Thought (CoT), role-based, iterative refinement, and reusable prompt templates. The lecture demonstrates how complex tasks can be decomposed using structured instructions, using techniques like the Fermi estimate to reveal the model's step-by-step reasoning pathway rather than relying on inconsistent web search lookups. A practical walkthrough using a Python notebook features OpenAI's GPT-4 Mini and Llama-3 (8B) via Groq APIs, demonstrating how developer tools allow programmatic execution, custom roles, and deterministic settings (such as setting the temperature parameter to zero).

The second half of the session is dedicated to gamified ethical hacking and red-teaming exercises to understand [AI Security and Robustness](../concepts/ai-security-robustness.md). Students engage with Lakera's "Gandalf" password disclosure game, tricking an LLM into revealing hidden passwords across multiple levels of increasing defense sophistication. They also explore the "Agent Breaker" playground to experiment with prompt injection attacks targeting [Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md) (e.g., trying to trick automated customer agents, CEO email bots, and trip planners into executing unauthorized actions like leaking internal tools or sending unapproved emails). These security challenges highlight why robust runtime boundaries and [Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md) are critical for enterprise-grade deployments.

# Key Concepts
- [Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md) — The core focus of the lecture, exploring how structural prompt design, explicit rules, and in-context examples align model generations with human intent.
- [AI Security and Robustness](../concepts/ai-security-robustness.md) — Examined through hands-on red-teaming, analyzing vulnerability to prompt injection, jailbreaking, and security fallback protocols.
- [Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md) — Demonstrated through "Agent Breaker," where students attempt to exploit functional agents (such as trip planners, code reviewers, and CEO email assistants) into bypassing boundaries or executing unauthorized commands.
- [Human-AI Collaboration and Guardrails](../concepts/human-ai-collaboration-guardrails.md) — Highlighted as a defensive necessity, emphasizing why developers must specify explicit runtime limits, fallbacks, and human-in-the-loop validation rather than letting models guess intentions.
- [Explainable AI (XAI)](../concepts/explainable-ai.md) — Discussed in the context of prompting models to output their step-by-step reasoning paths (e.g., using Chain-of-Thought or Fermi estimates) so decisions are auditable.
- **Fermi Estimate** — A step-by-step estimation technique used in prompting to make models break down complex numerical estimation questions (e.g., estimating the number of car mechanics in Hyderabad, India) into clear, logical, and auditable calculations.
- **Chain of Thought (CoT) vs. Tree of Thought (ToT)** — CoT represents a sequential, step-by-step linear chain of thoughts where each step feeds into the next. ToT allows parallel branches of reasoning or multiple hypotheses to be explored simultaneously under the same base platform or context.

# Topics Covered
- **The Intent-Context Gap:** Understanding how unstructured prompts force models to fill context gaps with assumptions, and how to remediate this with clear boundaries.
- **Six Core Prompting Techniques:**
  - *Zero-shot Prompting:* Standard tasks (e.g., summarization or classification) with direct instruction but no examples.
  - *Few-shot Prompting / In-Context Learning:* Providing high-quality input-output examples (usually 2 to 5 examples) to establish tone, schema, and edge-case handling.
  - *Chain-of-Thought (CoT):* Guiding step-by-step reasoning for debugging, planning, or mathematical questions.
  - *Role-based Prompting:* Assigning professional personas, domain contexts, and seniority levels to establish specialized tones and rules.
  - *Iterative Refinement:* Engaging in multi-turn conversational loops with self-criticism, rubric-based evaluation (Meets/Partially/Does Not Meet), and constrained revision commands.
  - *Reusable Prompt Templates:* Standardizing templates across enterprise teams to enforce consistent inputs, constraints, and success criteria.
- **Hands-on API and Notebook Walkthrough:** Accessing models like GPT-4 Mini and Llama 3 via Hugging Face or Groq APIs using API tokens and Google Colab secret environments.
- **Gamified Red-Teaming Exercises:**
  - *Gandalf Game:* Bypassing LLM defenses through levels 0 to 7 to extract a secret password using prompt injection and character-by-character extraction tricks.
  - *Agent Breaker:* Attempting to exploit agentic chatbots (e.g., CEO email assistant, shopping agent) to bypass their functional boundaries.

# Materials
- **Slides:**
  - `Session 6 - (19 Apr 2026).pdf`
  - `Session06_Slides_2026-04-19.pdf`
- **Interactive Notebook:** A Python Colab notebook demonstrating API setup (Hugging Face, Groq, OpenAI) and the six core prompting styles.
- **Recording:** Available on YouTube with ID [QrcwRu9MFXo](https://www.youtube.com/watch?v=QrcwRu9MFXo).
- **Chat:** The class session included active chat collaboration during the live hacking exercises.

# Related
- Part of the [AI Project Design](../courses/c5-ai-project-design.md) course.
- Sibling Sessions:
  - [Session 05](c5-ai-project-design-session-05.md) — Previous session on project requirements, shortcomings, and uncertainties.
  - [Session 07](c5-ai-project-design-session-07.md) — Subsequent session continuing the course curriculum.

# Citations
1. YouTube Video: [Session 6: AI Project Design - 19 Apr 2026](https://www.youtube.com/watch?v=QrcwRu9MFXo)
2. Gandalf AI Security Game by Lakera: [https://gandalf.lakera.ai/](https://gandalf.lakera.ai/) (discussed and played live in the session)
3. Agent Breaker Security Playground: (discussed and played live in the session)
