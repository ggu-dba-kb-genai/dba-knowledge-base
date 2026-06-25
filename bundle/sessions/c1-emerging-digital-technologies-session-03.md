---
type: Session
resource: https://www.youtube.com/watch?v=MahuEonWB14
title: 'Session 03: IoT Architectures, Edge vs. Cloud, and Digital Twins'
description: An in-depth exploration of the Internet of Things (IoT), mapping edge
  and cloud computing tradeoffs, evaluating cybersecurity layers, and exploring the
  industrial applications of digital twins.
tags:
- IoT
- Edge Computing
- Cloud Computing
- Digital Twins
- Cybersecurity
- Sustainability
- Moores Law
timestamp: '2025-07-19'
---

In this lecture, Dr. Parag Mantri introduces the foundational architecture of the Internet of Things (IoT), structuring the discussion around data collection, connection, computation, and communication. Grounded in his experience at Micron and GE, Dr. Mantri guides students through the three core layers of IoT—Perception (sensing/actuation), Network (transmission protocols), and Application (computation)—while emphasizing security and sustainability as critical cross-cutting layers. The session outlines the historical development of hardware, highlighting the foundational role of the transistor and Moore's Law, as well as the undersea submarine fiber-optic cables that connect global digital networks. 

The lecture focuses heavily on the engineering and business tradeoffs between edge and cloud computing. Dr. Mantri contrasts low-latency, real-time edge processing (such as a smartwatch providing heart rate warnings or a moving vehicle making local path corrections) with the centralized, expensive, and latency-prone computational power of cloud datacenters. The class also explores industrial IoT applications, such as remote wind farms and deep undersea oil rigs, where "digital twins" combine real-time sensor data, manual inspection records, and physics-based mathematical models to simulate and monitor physical assets with limited direct observability. Furthermore, the discussion touches on the environmental costs of massive cloud infrastructure, highlighting cooling innovations like Microsoft's undersea Project Natick and the rise of ultra-low-power "Ambient IoT" as sustainable pathways.

Finally, non-traditional IoT applications in finance, agriculture, and urban planning are explored to illustrate how physical sensors generate alternative data. Case studies include automated shrimp-feeding sensors and electric vehicle (EV) runtime tracking used to construct behavioral scoring models for dynamic credit scoring in supply chain financing. The class examines smart city projects in Singapore and Barcelona, showing how real-time traffic monitoring and adaptive street lighting can lower municipal energy costs. Throughout these examples, the session details how security vulnerabilities at the device, network, and software levels require robust, end-to-end encryption and caution when deploying predictive AI or large language models (LLMs) in critical industrial loops.

# Key Concepts

- **Moore's Law & Transistor Evolution:** The fundamental hardware driver enabling ubiquitous computing. Formulated as a hypothesis by Intel co-founder Gordon Moore, it predicted that the number of transistors on a microchip would double approximately every two years. Today, advanced manufacturing processes at companies like Micron pack over 100 billion transistors onto chips the size of a fingernail, though physical nanometer-scale limits introduce new design constraints.
- **Model Compression & Edge Processing:** Crucial for deploying intelligence onto resource-constrained edge hardware (e.g., microcontrollers like Arduino, Raspberry Pi, and NodeMCU) without draining battery life or exceeding memory capacity. This concept is explored further in [Model Compression and Optimization](../concepts/model-compression-optimization.md).
- **Edge vs. Cloud Computing Tradeoffs:** Edge computing excels in latency-critical scenarios requiring instant action (e.g., smartwatch cardiac alarms or autonomous vehicle navigation), whereas cloud computing offers massive, highly scalable processing at the cost of network latency, computational bills, and high energy usage.
- **Digital Twins:** Virtual, computerized replicas of physical assets (e.g., GE aircraft engines, oil rigs, or semiconductor manufacturing plants) that integrate real-time sensor streams, inspection reports, and governing physics equations to provide full observability over complex physical systems.
- **Universal Cameras & Computer Vision:** The shift toward using cameras as a "one-stop" universal sensor. Rather than installing multiple discrete proximity, infrared, and temperature sensors, a single video feed processed via [Computer Vision](../concepts/computer-vision.md) can reconstruct the environment, as seen in Tesla's pure camera-based Full Self-Driving (FSD) architecture over Waymo's LiDAR-based systems.
- **IoT Security Vulnerabilities:** Mitigating vulnerabilities across device pairing, network encryption (2FA, MFA), and software firmware updates. Because communications rely on the open electromagnetic spectrum (from radio to microwave frequencies), systems are highly susceptible to interception, prompting a need for robust [AI Security and Robustness](../concepts/ai-security-robustness.md).
- **Sustainability & Ambient IoT:** Addressing the massive environmental footprint of cloud datacenters and brute-force computing (such as inferencing LLMs). Solutions include undersea datacenter placement (e.g., Microsoft's Project Natick, Hainan subsea projects) and the development of **Ambient IoT**—devices that run on ultra-low-power chips and harvest environmental energy.
- **Autonomous Actuation Loops:** Deploying edge-computed intelligence (e.g., drones, autonomous vehicles, and planetary rovers) that collect environmental data and trigger mechanical actuators in a closed feedback loop with minimal human intervention, aligning with [Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md).

# Topics Covered

- **Historical Context of IT:** Connected networks from ARPANET and the World Wide Web to modern ubiquitous computing and large language models (LLMs).
- **Hardware and Physical Infrastructure:** Silicon fabrication, transistors, Moore's Law, and the intercontinental submarine fiber optic cables connecting global systems.
- **IoT Architectural Layers:**
  - *Perception/Hardware Layer:* Physical sensing (GPS, accelerometers, gyroscopes, ECG, temperature) and mechanical actuation.
  - *Network Layer:* Packets and protocols operating over the electromagnetic spectrum (Wi-Fi, Bluetooth, LoRa, Zigbee).
  - *Application/Compute Layer:* Edge vs. cloud computing models, latency, and operational cost structures.
  - *Security Layer:* Device-level vulnerabilities, network-level access control, and software/firmware integrity.
- **Case Studies & Applications:**
  - *Smartwatch Ecosystem:* Multi-sensor coordination (Bluetooth at 2.4 GHz) transmitting to mobile phones and the cloud.
  - *The Mobile Phone as a Consolidated IoT Device:* A single device encompassing sensing, communication, and application layers.
  - *Non-Traditional Finance & Agriculture:* Automated shrimp-feeding telemetry and EV tracking (run hours, stops, charge cycles) as alternative data for dynamic credit scoring in supply chain financing.
  - *Smart Cities:* Real-time traffic routing and adaptive street lighting reducing energy consumption by 30-50% in Singapore and Barcelona.
  - *Remote Wind Farming & Oil Rigs:* Real-time turbine monitoring, remote robotic maintenance, and digital twin state estimation in undersea or hard-to-reach physical locations.
- **Digital Twins & AI Integration:** Replicating physical assets using physics-based models vs. data-driven models, highlighting the caution required when introducing generative AI or LLMs into critical safety-critical industrial loops.

# Materials

- **Slides:** `Session03_Introduction.pdf`
- **Chat:** Student chat discussion present.
- **Video Recording:** YouTube video [MahuEonWB14](https://www.youtube.com/watch?v=MahuEonWB14)

# Related

- **Parent Course:** [Emerging Digital Technologies](../courses/c1-emerging-digital-technologies.md)
- **Adjacent Sessions:**
  - Previous Session: [Session 02: Introduction to IoT Devices and Sensors](c1-emerging-digital-technologies-session-02.md)
  - Next Session: [Session 04: Edge Computing & IoT Networks](c1-emerging-digital-technologies-session-04.md)

# Citations

1. Lecture recording: [YouTube video MahuEonWB14](https://www.youtube.com/watch?v=MahuEonWB14)
2. Gordon E. Moore, "Cramming more components onto integrated circuits" (1965), discussing Moore's Law.
3. Microsoft's Undersea Data Center Research Project: Project Natick.
