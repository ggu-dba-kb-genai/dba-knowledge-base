---
type: Session
resource: https://www.youtube.com/watch?v=ShXGVrn7yXI
title: 'Session 11: AI in Cyber Security — Defense, Weapon, and Vulnerabilities'
description: This session explores the dual role of artificial intelligence in cyber
  security as both an advanced shield for defense and a weapon for attackers, while
  detailing critical security concepts like the CIA triad, adversarial AI, and API
  security.
tags:
- Cyber Security
- Adversarial AI
- Ransomware
- Phishing
- API Security
- CIA Triad
- Deepfakes
- Zero Trust
- Generative AI
timestamp: '2025-08-24'
---

In this session, Dr. Habib Muhammad (PhD in AI and senior security architect) presents a comprehensive overview of how artificial intelligence is transforming the landscape of cybersecurity, operating both as an advanced shield for defenders and an automated weapon for attackers. The lecture frames cybersecurity as a critical, business-ending risk rather than a mere IT issue, noting that global cyber threats cost an estimated $10.5 trillion annually, and an average organizational breach costs $4.45 million. Dr. Habib details the mechanics of modern cyber threats—such as ransomware, phishing campaigns, insider threats, and supply chain vulnerabilities—while explaining how malicious actors increasingly deploy AI to mimic human behaviors, write convincing phishing emails, and automate credential stuffing.

To counter these threats, the lecture highlights the defender's perspective, introducing foundational concepts such as the CIA Triad (Confidentiality, Integrity, and Availability) and the Zero Trust architecture. It details how classical machine learning and deep learning (such as CNNs and RNNs) are utilized to identify anomalous behaviors, detect spam (with Gmail's filters blocking 100 million phishing emails daily), and perform forensically sound log analysis. Through live demonstrations of building a chatbot using Cursor AI and Gemini 2.0 Flash, Dr. Habib demonstrates the speed of modern software creation but warns against common developer oversights like exposing API keys and leaking sensitive PII/PCI data to public LLMs.

Finally, the lecture touches on advanced topics and emerging security challenges. These include adversarial AI (the cognitive fooling of machine learning models), data poisoning in public repositories, deepfake impersonations, security protocols for AR/VR and Digital Twins, and the looming impact of quantum computing on classical cryptographic systems such as RSA and Elliptic Curve Cryptography (ECC).

# Key Concepts

- **[AI Security and Robustness](../concepts/ai-security-robustness.md)** — Discussed extensively in the context of securing API endpoints, protecting PII (Personally Identifiable Information) and PCI (Payment Card Industry) data, and deploying tools like IBM's Adversarial Robustness Toolbox (ART) to defend machine learning models against adversarial attacks.
- **[Computer Vision](../concepts/computer-vision.md)** — Highlighted through examples of adversarial AI where vision models (such as ResNet) are fooled into misclassification (e.g., interpreting a sticker on a table as a banana or misinterpreting modified stop signs in autonomous driving systems).
- **[Generative Modeling](../concepts/generative-modeling.md)** — Covered through the lens of deepfakes and synthetic content generation, where attackers leverage generative AI to replicate human voices, create realistic phishing emails, or synthesize video calls for social engineering.
- **[Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md)** — Discussed in the context of no-code platforms like Cursor AI operating in agentic modes to construct directory structures and files autonomously, as well as decision-making systems in autonomous vehicles navigating traffic conditions.
- **[Retrieval-Augmented Generation (RAG)](../concepts/retrieval-augmented-generation.md)** — Briefly noted as a mechanism to minimize hallucinations by anchoring LLM outputs to verifiable corporate data, though highlighted as still vulnerable to data poisoning if input data is corrupted.
- **[AI Governance and Compliance](../concepts/ai-governance-compliance.md)** — Connected to the necessity of adhering to security and privacy standards such as GDPR, CCPA, and PCI-DSS to prevent major financial penalties and reputational collapse following data breaches.
- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — Explored through regression (modeling continuous packet parameters to identify anomalies) and classification (network attack detection such as scanning and spoofing, alongside spam filtering).
- **The CIA Triad** — The foundational framework of security consisting of *Confidentiality* (ensuring data is masked and authorized), *Integrity* (ensuring data is not altered or tampered with), and *Availability* (ensuring systems remain online and accessible, particularly during high-traffic events or under DoS/DDoS attacks).
- **Closed vs. Open LLMs** — A comparison of closed models (like ChatGPT/Claude) to an "Uber car" (high convenience, but data is captured for training, exposing sensitive resume CTC or personal data) versus open-source LLMs run locally via Ollama (like Mistral, DeepSeek, or Qwen) to a "personal car" (full data privacy and control).

# Topics Covered

- **Introduction and Statistics**: Framing cybersecurity as a business problem; discussing global cybercrime costs ($10.5T) and the frequency of phishing and ransomware.
- **Industry Impacts & Cases**:
  - *Finance*: The 2016 Bangladesh Bank heist ($81 million stolen due to lack of PCI/PII compliance and SWIFT fraud).
  - *E-Commerce*: The 2013 Target breach (40 million cards stolen); coping with DDoS attacks on peak days like Black Friday.
  - *Healthcare*: The 2017 ransomware attacks (WannaCry) forcing hospital shutdowns and surgery delays.
  - *Supply Chain*: The Colonial Pipeline shutdown and SolarWinds supply chain exploit.
- **The CIA Triad & Zero Trust**: Understanding Confidentiality, Integrity, and Availability alongside the Zero Trust approach to vendor risk management.
- **API Security and PII/PCI Masking**: The danger of uploading sensitive PII (Personally Identifiable Information) or PCI data to public/closed LLMs (e.g., ChatGPT/Claude) for resume editing or document summarization.
- **Insider Threats and Social Engineering**: How human error drives 90% of breaches; techniques like baiting, pre-texting, impersonation, and CEO fraud ("CEO stuck at airport").
- **Hands-on Demonstration with Cursor AI**: Building a chatbot using Gemini 2.0 Flash in Cursor; highlighting the security risks of hardcoding or exposing API keys via `.env` files.
- **AI in Defense vs. Offense**:
  - *Defense*: Regression models for packet parameter anomalies; classification for network attack detection; clustering for forensic analyses.
  - *Offense*: AI-guided credential stuffing, deepfake video calls, and adversarial ML attacks.
- **Securing AR/VR & Digital Twins**: Recommendations for openXR permissions, media telemetry behind TLS/mTLS, liveness testing, and validating payloads with JSON schemas.
- **Future Trends**: The vulnerability of classical RSA/ECC encryption to emerging quantum computing capabilities (prime factorization and discrete logarithm attacks).

# Materials

- **Slides**: No slides are associated with this session.
- **Chat**: Yes, student-instructor chat was present during this session.
- **Recording**: Available via YouTube at `https://www.youtube.com/watch?v=ShXGVrn7yXI`.

# Related

- **Parent Course**: [Emerging Digital Technologies](../courses/c1-emerging-digital-technologies.md)
- **Previous Session**: [Session 10: Emerging Digital Technologies - Session 10](c1-emerging-digital-technologies-session-10.md)
- **Next Session**: [Session 12: Emerging Digital Technologies - Session 12](c1-emerging-digital-technologies-session-12.md)

# Citations

1. YouTube Video: `https://www.youtube.com/watch?v=ShXGVrn7yXI`
2. Cyber Security Ventures: Global Cybercrime Cost Report
3. IBM: Adversarial Robustness Toolbox (ART)
