---
type: Concept
title: AI Security and Robustness
description: Protecting AI pipelines from adversarial attacks, data poisoning, model
  extraction, prompt injection, and ensuring overall runtime security.
tags:
- ai-security
- adversarial-ml
- data-poisoning
- prompt-injection
- model-drift
- cia-triad
- guardrails
timestamp: '2026-05-03T00:00:00Z'
---

AI Security and Robustness is a core cross-cutting discipline concerned with protecting machine learning pipelines, datasets, and deployed models from exploit, failure, and operational degradation. As artificial intelligence moves from sandboxed research environments to critical production domains, ensuring that systems behave safely under adversarial conditions and retain their integrity over time has become a principal business and engineering requirement. AI-specific security spans classical cybersecurity goals (Confidentiality, Integrity, and Availability) while addressing net-new vulnerabilities native to machine learning architectures, such as model theft, adversarial input spoofing, training data corruption, and semantic jailbreaking.

In this program, the study of security and robustness is deeply practical. It focuses on the physical and network limitations of secure edge-computing and Internet of Things (IoT) architectures, the technical taxonomy of modern adversarial attacks, the application of machine learning methods to build defensive wrappers, and the governance frameworks required to secure high-risk, low-risk-appetite deployments (such as in banking, healthcare, and infrastructure).

## Where It Appears

This concept is covered extensively across the following courses and program sessions:

* **[Responsible AI](../courses/c6-responsible-ai.md)** — Serves as the overarching framework for safety, ethical compliance (including GDPR, CCPA, and India's emerging data security regulations), and system guardrails across the development and operational phases.
* **[Emerging Digital Technologies](../courses/c1-emerging-digital-technologies.md)**:
  * **[Session 02: IoT Architecture & Core Infrastructure](../sessions/c1-emerging-digital-technologies-session-02.md)** — Taught by Prof. Venkatesh, this session positions security as a business and leadership challenge. The curriculum introduces an organizational security framework categorized into *Organizational Policies*, *Physical Security* (locks, perimeters, surveillance, and tamper-proofing), and *Digital Security* (data backups, anti-malware, firewalls, network policies, port blocking, and secure boot). The session explores the real-world engineering trade-off where increased security adds computational latency and operational complexity.
  * **[Session 03: Communication Protocols, Edge, and Digital Twins](../sessions/c1-emerging-digital-technologies-session-03.md)** — Taught by Dr. Parag Mantri, this session focuses on the physical limitations of security in the electromagnetic spectrum (where Bluetooth, Wi-Fi, LoRa, and Zigbee operate). It details how wireless transmission cannot be secured at the physical layer, requiring robustness at the network and software/firmware levels. The session highlights security vulnerabilities in autonomous vehicles and digital twin simulations of heavy industrial machinery.
  * **[Session 11: AI in Cyber Security — Defenders and Weapons](../sessions/c1-emerging-digital-technologies-session-11.md)** — Taught by Dr. Habibi, this session explores the dual role of AI as both a defensive shield and an offensive target. It introduces the **CIA Triad** (Confidentiality, Integrity, Availability) and examines key attack vectors, including ransomware (e.g., the Colonial Pipeline crisis), phishing scams, API-level exposures of PII and PCI data, and insider threat patterns caused by human error (such as public API key exposure). It dissects **Adversarial AI** methods, including data poisoning (injecting malicious data into training feeds), model jailbreaking (prompt engineering exploits), and deepfakes (synthetic audio/video). Defensively, the session covers ML-driven intrusion detection using CNNs/RNNs, packet analysis via regression models, and the use of the IBM Adversarial Robustness Toolbox (ART).
* **[AI Project Design](../courses/c5-ai-project-design.md)**:
  * **[Session 10: Release Readiness and Observability](../sessions/c5-ai-project-design-session-10.md)** — This session links security to the "Definition of Ready," defining it as a state where risks are systematically controlled, rather than striving for an impossible zero-error standard. It outlines a structured scenario-based testing methodology (depth and width) that addresses edge cases, context sensitivity, and adversarial inputs. The curriculum covers the **Triangulation Method** (evaluating and tabulating outputs across three distinct LLMs), active input/output filtering, and human-in-the-loop (HITL) review loops. It also introduces techniques to monitor post-release model drift (data, concept, and behavioral drift) and discusses high-profile AI output failures (e.g., service chatbots producing inappropriate content post-update and launch-day promotional hallucinations).

## Citations

1. **NIST Artificial Intelligence Risk Management Framework (NIST AI RMF 1.0)** — National Institute of Standards and Technology. A foundational framework for managing safety, security, and trustworthiness in AI system design and deployment.
2. **ISO/IEC 42001:2023 (Information technology — Artificial intelligence — Management system)** — International Organization for Standardization. The international standard specifying requirements for establishing, implementing, and continually improving an AI Management System (AIMS).
3. **IBM Adversarial Robustness Toolbox (ART)** — An open-source developer library used to test, evaluate, and defend machine learning models against adversarial threats such as evasion, poisoning, extraction, and inference attacks.
4. **OWASP Top 10 for Large Language Model Applications** — Open Worldwide Application Security Project. A consensus list of the most critical security vulnerabilities often found in LLM deployments, including prompt injection, insecure output handling, and training data poisoning.
