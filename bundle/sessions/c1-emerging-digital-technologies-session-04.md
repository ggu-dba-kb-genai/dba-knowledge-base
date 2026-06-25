---
type: Session
resource: https://www.youtube.com/watch?v=clkvlg9ImSc
title: 'Session 04: Cloud, Edge & Cloud Native Computing'
description: An in-depth exploration of cloud architectures (from Virtualization to
  Cloud Native), the paradigm shift to Edge AI, and real-world industrial deployments.
tags:
- cloud-computing
- edge-ai
- cloud-native
- microservices
- kubernetes
- virtualization
- edge-computing
- model-compression
timestamp: '2025-07-20'
---

Dr. Pethuru Raj of Reliance Jio Platforms Limited presents a comprehensive class on Cloud and Edge Computing within the digital transformation paradigm. He distinguishes between "digitization"—the conversion of physical, mechanical, and electrical systems into data-producing digital elements using sensors and IoT—and "digitalization"—the transformation of raw digital data into actionable business insights using cloud-based analytics. Tracing the history of cloud computing back to Amazon's humble beginnings selling books in 1992, Dr. Raj outlines how seasonal peaks in December forced massive infrastructure scaling that sat idle in January. This operational challenge led to the commercialization of underutilized capacity as "elastic computing," establishing the utility model of modern on-demand cloud services.

The lecture maps the technological progression from Cloud 1.0 through Cloud 3.0. Cloud 1.0 introduced hypervisor-based virtualization, improving server utilization from a baseline of 15% to 40–50% by running multiple isolated virtual machines (VMs) on a single physical host. Cloud 2.0 evolved into Software-Defined Clouds, where compute, storage (Software-Defined Storage or SDS), and networks (Software-Defined Networking or SDN) are fully virtualized and programmatically controlled via Network Function Virtualization (NFV). Cloud 3.0 represents the modern era of Cloud Native Computing, driven by microservices architectures, lightweight containers that launch in seconds, and Kubernetes orchestration to automate deployment, self-healing, and scaling. Within this paradigm, Dr. Raj highlights the roles of DevOps (facilitated by CI/CD pipelines) and Site Reliability Engineering (SRE) in maintaining continuous availability (targeting 99.999% uptime) and monitoring system health, contrasting these highly resilient systems with legacy physical architectures.

Transitioning to Edge Computing and Edge AI, the session examines why centralized clouds are insufficient for real-time operations due to network latency constraints. For example, transmitting data 1,000 km between Bangalore and Mumbai incurs an approximate 14-millisecond round-trip delay, which is unacceptable for instantaneous decision-making in safety-critical systems like traffic lights or remote surgery. While there are only about 2 million centralized cloud servers globally across roughly 500 datacenters, the global edge contains billions of smart devices with rapidly closing resource gaps. Dr. Raj presents two real-world, patented case studies from Reliance Jio: first, a local edge-based access control system using Raspberry Pi controllers that run access databases offline in nanoseconds, eliminating dependencies on the Navi Mumbai geocloud; and second, the integration of a face recognition AI model to enable keyless, offline biometric access. The session concludes with a discussion of model compression techniques (pruning, quantization, and knowledge distillation) and the sustainability challenges of training Large Language Models (LLMs) on massive GPU-equipped clouds, driving the industry toward energy-efficient chips and local Small Language Models (SLMs).

# Key Concepts

- [Model Compression and Optimization](../concepts/model-compression-optimization.md) — Methods such as pruning, quantization, and knowledge distillation that shrink model weights (e.g., compressing a 1GB model down to 10MB) to allow local inference on resource-constrained edge devices.
- [Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md) — The shift from predictive systems to generative and agentic workflows that autonomously process unstructured streams and trigger targeted downstream actions.
- [Computer Vision](../concepts/computer-vision.md) — Real-time visual processing deployed at the edge, exemplified by Jio's offline face recognition models embedded in IoT gateways and office access systems.
- [AI Security and Robustness](../concepts/ai-security-robustness.md) — Core design principles for mission-critical edge ecosystems, ensuring tamper-resistance, offline failover support, and secure local access control.
- [AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md) — Manifested in Cloud Native systems through DevOps (CI/CD) and Site Reliability Engineering (SRE) paradigms to enforce high availability, telemetry, and automated container orchestration.
- [Generative Modeling](../concepts/generative-modeling.md) — The paradigm shift from predictive AI (which handles classification and clustering) to generative AI (which synthesizes new text, images, and code via Large Language Models).
- [Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md) — Training massive foundation models on cloud GPUs and fine-tuning them for highly specialized downstream enterprise tasks before deploying them to production.
- **Cloud 1.0 (Virtualization)** — The foundational practice of using hypervisors (Virtual Machine Monitors) to partition physical hosts into multiple virtual machines (VMs) running isolated guest operating systems, pushing server utilization from 15% to 40–50%.
- **Cloud 2.0 (Software-Defined Cloud)** — An era where computing, storage (SDS), and networking (SDN) are entirely virtualized, enabling programmable configurations like Network Function Virtualization (NFV) to dynamically allocate bandwidth.
- **Cloud 3.0 (Cloud Native Computing)** — Building resilient and portable applications using microservices architecture (loosely coupled, modular), lightweight containers (which spin up in seconds), and Kubernetes for automated deployment, self-healing, and declarative scaling.
- **Edge & Fog Computing** — Performing compute and data processing locally on nearby edge nodes (e.g., CCTV cameras, Wi-Fi gateways, Raspberry Pi) to eliminate network round-trip latencies, critical for time-sensitive tasks. "Fog" represents intermediate edge servers (resource-intensive) that aggregate and process data, whereas "edge" typically refers to the low-power devices/sensors themselves.

# Topics Covered

- **Session Kickoff and Administrative Announcements**: Overview of the upcoming individual (Assignment 1) and group (Assignment 2) assignments, focusing on integrating emerging technologies and addressing real-world challenges.
- **Digital Transformation Framework**: The five strategic pillars of process excellence, architecture assimilation, infrastructure optimization, technology choice/leverage, and data mobilization.
- **Evolution of Cloud Architectures**:
  - **Virtualization (Cloud 1.0)**: VM orchestration, guest OS separation, hypervisors, and resource optimization.
  - **Software-Defined Architecture (Cloud 2.0)**: SDN, SDS, and Network Function Virtualization (NFV) for programmable bandwidth allocation.
  - **Cloud Native (Cloud 3.0)**: Microservices, containers, Kubernetes orchestration, immutable infrastructure, declarative APIs, and Site Reliability Engineering (SRE).
- **The Cloud of Things**: Convergence of IoT as data generators and centralized clouds as high-capacity storage and analytics engines.
- **Digitization vs. Digitalization**: Conceptual differences between converting physical systems to digital devices (digitization) and turning digital data into actionable business insights (digitalization).
- **Cloud AI & Sustainability**: The massive carbon footprint and energy overhead of training LLMs on centralized GPU clusters (requiring electricity equivalent to entire states) and the push for energy-efficient chips (Nvidia) and Small Language Models (SLMs).
- **Edge Computing & Latency Constraints**: Physical distance-driven latency (e.g., 14 milliseconds round-trip over 1,000 km between Bangalore and Mumbai) making centralized cloud processing unviable for real-time applications.
- **Jio Patented Case Studies**:
  - **Offline Access Control**: A local, Raspberry Pi-based edge controller holding employee databases to bypass central cloud or internet failures.
  - **Edge-Based Face Recognition**: Upgrading the edge controller with a local computer vision model to enable secure, biometric keyless access offline.
- **Model Compression Techniques**: Pruning, quantization, and knowledge distillation to shrink model sizes for on-device deployment.
- **Edge vs. Fog Computing**: Differentiating terminology from Cisco (fog computing) and IBM/industry (edge computing), outlining the hierarchy from raw sensors to intermediate edge servers.

# Materials

- **Recording**: A YouTube recording is available at `https://www.youtube.com/watch?v=clkvlg9ImSc`.
- **Slides**: No slide files are present in the session metadata.
- **Chat**: No chat records are preserved for this session.

# Related

- Sibling Session: [Session 03: Internet of Things](c1-emerging-digital-technologies-session-03.md)
- Sibling Session: [Session 05: Session 05](c1-emerging-digital-technologies-session-05.md)
- Parent Course: [Emerging Digital Technologies](../courses/c1-emerging-digital-technologies.md)

# Citations

1. Session Lecture Video: `https://www.youtube.com/watch?v=clkvlg9ImSc`
2. Dr. Pethuru Raj, *Cloud Native Computing*, IT Press / CRC Press.
3. IBM Watson Health, Oncology Case Study, Tokyo University Hospital.
