---
type: Session
resource: https://www.youtube.com/watch?v=puYS_L_LAxo
title: 'Session 07: Introduction to Neuromorphic Computing'
description: An introduction to brain-inspired neuromorphic hardware architectures,
  spiking neural networks, and their emerging applications in ultra-low-power edge
  computing.
tags:
- Neuromorphic Computing
- Spiking Neural Networks
- In-Memory Computing
- Edge AI
- Hardware Acceleration
timestamp: '2025-08-02'
---

This session introduces the paradigm of **Neuromorphic Computing**—computer hardware architectures designed to mimic the human brain's processing efficiency. Led by guest speaker Dr. S UmaMahesh, co-founder of the Netherlands-based chip design company Innatera Nanosystems, the lecture outlines the physical and physical limits of classical computer architectures (such as Von Neumann and Harvard bottlenecks) when executing modern deep learning workloads. It explores how brain-inspired computing can achieve orders-of-magnitude improvements in energy efficiency, latency, and spatial footprints directly at the edge where sensory data is generated.

The course covers the biological structure of brains—focusing on neurons, axons, dendrites, and synapses—and maps them to physical analog-mixed-signal silicon chips. A strong emphasis is placed on Spiking Neural Networks (SNNs), which process data in asynchronous temporal "spikes" rather than continuous arithmetic operations, drastically reducing active power. Additionally, Dr. UmaMahesh walks the class through Innatera’s proprietary "Pulsar" neuromorphic microcontroller, which integrates SNN arrays with a conventional CNN accelerator and a RISC-V housekeeping core, enabling developer tools built on PyTorch and Python.

The lecture concludes with a discussion of future enterprise paradigms, such as Large Action Models (LAMs) that predict actions rather than words, agentic frameworks, "Living Intelligence" (converging biotechnology, sensors, and AI), and administrative updates regarding Golden Gate University (GGU) coursework, Turnitin evaluations, and research publishing opportunities.

# Key Concepts

- **[Neuromorphic and Hardware Acceleration](../concepts/neuromorphic-and-hardware-acceleration.md)** — Brain-inspired processing designed to replace clock-driven serial logic with asynchronous, parallel, event-driven in-memory architectures to eliminate the classic Von Neumann memory bottleneck.
- **Spiking Neural Networks (SNNs)** — Hardware-aligned networks that utilize discrete temporal spikes to trigger computing nodes, operating only when thresholds are reached, rather than executing continuous matrix math.
- **[Neural Network Architectures](../concepts/neural-network-architectures.md)** — A comparative study of network topologies including Recurrent Neural Networks (RNNs) for voice recognition, Convolutional Neural Networks (CNNs) for structured grids, and hybrid SNNs for analog sensory processing.
- **[Model Compression and Optimization](../concepts/model-compression-optimization.md)** — Strategies to run highly accurate models within strict power budgets (sub-milliwatt range) at the "deep edge," contrasting large foundational models with local or small language models (SLMs).
- **[Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md)** — The rise of Large Action Models (LAMs) and multi-agent frameworks (e.g., CrewAI, LangChain) that orchestrate distinct models to execute goal-driven actions in physical or software environments.
- **[Computer Vision](../concepts/computer-vision.md)** — Utilizing local sensors (cameras, radar, lidar) coupled with neuromorphic processing to execute instant gesture and object detection tasks.
- **[Time Series and Forecasting](../concepts/time-series-forecasting.md)** — Applying sequential temporal networks like RNNs and LSTMs for real-time environment tracking and weather forecasting.
- **[AI Security and Robustness](../concepts/ai-security-robustness.md)** — Edge-device vulnerability management, detailing how local, in-memory computing acts as a physical security barrier by preventing communication interceptions.
- **[Attention Mechanisms and Transformers](../concepts/attention-and-transformers.md)** — Sequence-processing frameworks that use self-attention to dynamically analyze tokens, where the transformer acts as a core data extractor for natural language processing.

# Topics Covered

- **Digital Transformation Context**: Moving from static servers to the "Deep Edge" characterized by trillions of interconnected sensors.
- **The Classical Bottleneck**: Exploring Von Neumann and Harvard CPU limitations, instruction set architectures, and the open RISC-V standard.
- **The AI/ML/DL Hierarchy**: Defining the progressive relationship from general AI down to Deep Learning, Large Language Models (LLMs), and localized Small Language Models (SLMs).
- **Deep Dive into Neural Networks**: Functional overviews of Recurrent (RNN), Generative Adversarial (GAN), Feed-Forward, Radial Basis, Deep Belief, and Convolutional (CNN) networks.
- **Biological Mapping**: Structuring artificial neural systems in direct parallel to human brain cells (neurons and synapses).
- **Innatera "Pulsar" Case Study**: Analysis of a 2.8 $mm^2$ silicon analog-mixed-signal neuromorphic microcontroller offering over 500x power efficiency improvements and 100x latency reductions.
- **Software Stack Integration**: Deploying SNN algorithms on hardware using familiar python/PyTorch frameworks, compiling weights/biases directly into the processor arrays.
- **Privacy-First Sensing**: Implementing radar and lidar-based occupancy/human detection to allow smart systems (e.g., fire alarms) to identify humans without taking identifiable video feeds.
- **Living Intelligence**: The prospective convergence of biotechnology, edge sensors, and neuromorphic processing to build responsive, biological-like systems.
- **DBA Program Session Administration**: Dr. Sumitra reviews coursework instructions, Turnitin parameters (permitting up to 20% AI-generated content in dissertations), GGU Worldwide publications, and the "Rise of AI Agents" book.

# Materials

- **Slides**: `Session07_Neuromorphic_Computing.pdf`
- **Video Recording**: YouTube link `https://www.youtube.com/watch?v=puYS_L_LAxo`
- **Chat Logs**: Present and archived.

# Related

- Sibling Session: [Session 06: Emerging Digital Technologies](c1-emerging-digital-technologies-session-06.md)
- Sibling Session: [Session 08: Emerging Digital Technologies](c1-emerging-digital-technologies-session-08.md)
- Parent Course: [Emerging Digital Technologies](../courses/c1-emerging-digital-technologies.md)

# Citations

1. Session Recording: `https://www.youtube.com/watch?v=puYS_L_LAxo`
2. Innatera Nano Systems, Pulsar Neuromorphic Microcontroller Hardware and Software Documentation (Delft, Netherlands).
3. "Rise of AI Agents" by GGU worldwide Prov. J & Dr. Sumitra (Golden Gate University Practitioner Book Series).
4. Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, L., & Polosukhin, I. (2017). "Attention Is All You Need." https://arxiv.org/pdf/1706.03762
5. "A Review of Spiking Neuromorphic Hardware Communication Systems." IEEE Access, September 2019.
6. Neurobench Benchmark Framework: https://neurobench.ai/
7. Stackpole, T. (Host). "Tech at Work" (Four-part series). HBR IdeaCast, Harvard Business Review.
