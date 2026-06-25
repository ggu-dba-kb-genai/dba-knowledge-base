---
type: Reference
resource: https://developers.google.com/machine-learning/glossary/agent
title: Agentic Loop and Design Patterns
description: Core design patterns of agentic systems including the observe-reason-act-feedback
  loop, action spaces, autonomous vs. state machine agents, and specialized agent
  personas.
tags:
- Agentic AI
- Autonomous Systems
- Agentic Loop
- Design Patterns
- Multi-Agent Systems
timestamp: '2026-06-20T06:41:50+00:00'
---

**Agentic Loop & Design Patterns** describe the systematic processes, constraints, and organizational structures that transform a standard, stateless large language model into an autonomous or semi-autonomous agentic system. At the core of any agent is the **Agentic Loop**, which continuously iterates through four distinct operational phases until a defined termination condition is met:
1. **Observe**: The agent examines or evaluates its current state, progress, or output (such as running tests on newly generated code or parsing user inputs).
2. **Reason**: The agent determines the next logical action to take based on its observations (e.g., deciding to call a specific API, search a database, or ask the user for clarification).
3. **Act**: The agent executes the selected action (e.g., transmitting an API request, performing a calculation, or generating a draft).
4. **Feedback**: The agent receives and evaluates the outcome of its action (e.g., checking if the API call was successful or if the calculation raised an error).

An agent's operational boundaries are defined by its **Action Space**—the complete set of tools, APIs, databases, and system permissions it is authorized to utilize. Properly sizing the action space is a critical engineering challenge: an action space that is too small limits the agent's utility, whereas an excessively large action space increases cognitive load, cost, and the rate of execution errors. Depending on how rigidly this action space is navigated, systems are split between **Autonomous Agents** (which plan, act, and adapt dynamically without continuous human intervention) and **State Machine Agents** (which are tightly constrained by hardcoded state transition rules to minimize errors at the expense of general flexibility).

To solve complex multi-turn tasks, enterprise architectures employ specialized collaborative **Agent Personas**:
* **Router Agent**: A specialized classifier that analyzes user queries to route them to the most appropriate downstream domain agent or workflow.
* **Evaluator Agent (Critic)**: An agent tasked with assessing another agent's outputs against quality, style, or regulatory standards before finalization, providing a structured self-correction mechanism.
* **Manager Agent (Supervisor)**: A coordinator that manages, delegates, and consolidates tasks across multiple **sub-agents**, which are smaller models assigned narrow, specialized action spaces.

# Citations
1. Google for Developers. (2026). *Machine Learning Glossary: Agentic*. https://developers.google.com/machine-learning/glossary/agent
