---
type: Session
resource: https://www.youtube.com/watch?v=MoPTsD21hO8
title: 'Session 10: Human Vision, Image Processing & Introduction to Convolutions'
description: An introduction to computer vision and the mechanics of 2D convolution,
  bridging biological visual perception with artificial neural network architectures.
tags:
- computer-vision
- neural-network-architectures
- image-processing
- convolutions
- biology
timestamp: '2025-12-14'
---

This session marks the transition in the [Deep Learning](../courses/c3-deep-learning.md) course from general neural networks to specific spatial applications, bridging the history, biology, and mathematical foundations of [Computer Vision](../concepts/computer-vision.md) with modern convolutional networks. The class opens with an interactive, student-driven discussion on modern generative AI, focusing on cognitive fatigue from rapid model releases, organizational vendor lock-in, and the rise of "vibe coding" as a paradigm that democratizes software development while introducing severe risks like prompt injection. These topics are analyzed through classic economic concepts, including the Jevons Paradox (where efficiency gains drive up total resource consumption), the Lump of Labor fallacy, and student-led debates on Gandhian economic decentralization versus centralized cloud monopolies.

The core lecture details how human visual perception operates as an eye-brain system rather than a direct sensory intake, with up to 60–80% of brain processing power dedicated to visual data. By studying retinal and cortical prosthetics (such as visual implants from Johns Hopkins and neural interfaces like Neuralink), the lesson illustrates that we see with our brain, not our eyes. Biological vision relies on photoreceptors—low-light intensity rods and color-perceiving cones (sensitive to red, green, and blue wavelengths)—and cortical receptive fields. Within the temporal cortex, simple cells (S-cells) detect localized orientations and motion, passing their signals to complex cells (C-cells) to extract shapes, curves, and contours. This visual hierarchy served as the direct inspiration for Kunihiko Fukushima's Neocognitron (a precursor to modern CNNs used to recognize broken Japanese characters) and underpins modern [Neural Network Architectures](../concepts/neural-network-architectures.md). The biology of vision is further explored through perceptual illusions, including bistable processing (the saxophone/woman face), Kanizsa contours, and cognitive face optimization, where the brain stores individual faces as deviations from an "average face" baseline that dynamically recalibrates when relocating to new cultural environments.

The technical portion of the session connects biological principles with digital storage and classical image processing. Digital images are represented as 2D coordinate matrices $f(x, y)$ quantized to 8-bit channels (values 0 to 255) for Red, Green, and Blue. Traditional image manipulation historically relied on handcrafted mathematical operations (rotation, translation, and mirror inversion ($f(-x, y)$) using manually designed matrices). This transitions into the mathematical mechanics of 2D convolutions, defined as the summation of the element-wise product of an input image and a sliding filter (or kernel) to produce a scalar output. By walking through a cell-by-cell numerical example convolving a 3x3 filter over a binary arrow matrix, the class demonstrates how directional edge detection filters (horizontal and vertical edge extractors) isolate spatial gradients. This classical handcrafted filter paradigm sets the stage for modern deep learning, where networks automatically learn optimal feature-extracting filters via backpropagation.

# Key Concepts

- **[Computer Vision](../concepts/computer-vision.md)** — The study of enabling digital systems to process, analyze, and extract semantic meaning from visual signals, extending capabilities beyond biological constraints (such as leveraging ultraviolet, infrared, or hyperspectral imaging).
- **[Neural Network Architectures](../concepts/neural-network-architectures.md)** — Hierarchical network designs modeled on visual cortical cells, historically starting with Fukushima’s Neocognitron and evolving into Convolutional Neural Networks (CNNs).
- **[Dimensionality Reduction and Feature Extraction](../concepts/dimensionality-reduction.md)** — The process of extracting localized, invariant features (such as edges, curves, and orientations) from high-dimensional raw pixel grids, compressing spatial dimensions while preserving core visual properties.
- **[AI Security and Robustness](../concepts/ai-security-robustness.md)** — Analyzed in the context of democratized software creation ("vibe coding"), where automated code generation from plain English instructions introduces critical security holes and prompt injection vulnerabilities.
- **[Prompt Engineering and In-Context Learning](../concepts/prompt-engineering-context-learning.md)** — Covered during discussions on the transition from syntax-heavy coding to plain English prompting as a programming paradigm.
- **[Bias, Fairness, and Alignment](../concepts/bias-fairness-alignment.md)** — Addressed during organizational debates on using API gateways to manage model bias, inaccuracies, and vendor lock-in across multiple foundation models like OpenAI and Anthropic.

# Topics Covered

## 1. Socio-Economic AI Debates & "Vibe Coding"
- **Model Proliferation & Vendor Lock-in**: The cognitive load on individuals keeping pace with rapid model iterations and organizational strategies to manage bias by routing queries through API gateways across multiple vendors.
- **Democratization of Programming**: How plain English prompting replaces syntax-heavy programming ("vibe coding"), introducing major security holes, runtime errors, and prompt injections.
- **Economic Decentralization**: Student debates on whether generative AI will drive Gandhian economic decentralization (one-person companies) or further consolidate wealth to hyperscalers who host these massive resources.
- **Automation Paradoxes**: Analyzing Jevons Paradox (efficiency boosts drive up total demand) and the Lump of Labor fallacy (the false premise of a fixed amount of work to be done in the world).

## 2. Biological vs. Artificial Visual Systems
- **Visual Dominance**: Over 60% of human brain processing power is devoted to vision, demonstrating that vision is an eye-brain system (evidenced by retinal implants and neural link prosthetics bypassing physical eyes).
- **Biological Photoreceptors**: The functional divide between light-intensity detecting rods and wavelength-selective cones (Red, Green, Blue).
- **Going Beyond Biology**: Designing artificial sensors unconstrained by human biology to process X-rays, gamma rays, infrared, ultraviolet, and hyperspectral bands, as well as artificial noses to detect molecules in hazardous settings.
- **Hierarchical Visual Cortex**: Simple cells (S-cells) extracting localized orientations and movements, and complex cells (C-cells) aggregating S-cell inputs over larger regions to isolate complex shapes and curves.
- **Kunihiko Fukushima's Neocognitron**: The biological precursor model to modern CNN architectures, utilizing S-cells and C-cells to reconstruct incomplete Japanese characters.
- **Cognitive and Perceptual Illusions**: Studying face recalibration (encoding individual faces as deviations from an "average face" baseline), bistable visual processing (the saxophone/woman illusion), Kanizsa contours, and upright versus inverted face configural expressions.

## 3. Digital Image Representation & Classical Image Processing
- **Matrix Quantization**: Representing digital light as 2D coordinates $f(x, y)$ utilizing 8-bit channels (0 to 255) for RGB colors.
- **Handcrafted Matrix Operators**: Traditional image manipulation (rotation, translation, binarization, mirror inversion $f(-x, y)$) using manually designed mathematical operations.

## 4. Introduction to Convolutions and Learned Filters
- **The Convolution Process**: Sliding a small filter/kernel window across an image, performing localized element-wise multiplications, and aggregating the result via summation to output a scalar.
- **2D Convolution Walkthrough**: A cell-by-cell mathematical example convolving a 3x3 filter over a binary arrow matrix to produce a convolved feature map.
- **Spatial Edge Detectors**: Designing specific horizontal and vertical filters to extract directional spatial gradients of light change (e.g., isolating a shoulder line versus a nose bridge).
- **Transition to CNNs**: Moving away from classical handcrafted filters (as seen in legacy image editing software) toward networks that automatically learn optimal feature-extracting filters via backpropagation.

# Materials

- **Slides**:
  - `20251214_C8S1_Intro-to-CV.pdf` — Explores human visual anatomy, biological perception, digital representations, and classical image-processing matrices.
  - `20251214_C8S1_CNN.pdf` — Introduces the mathematical mechanics of 2D convolutions, Neocognitron foundations, edge filters, and hierarchical feature learning.
- **Chat**: Present (student debates on Jevons paradox, Gandhian economic models, API gateways to manage model bias, and recommended denoising tools).
- **Recording**: Available on YouTube (Video ID: [MoPTsD21hO8](https://www.youtube.com/watch?v=MoPTsD21hO8)).

# Related

- **Parent Course:** [Deep Learning](../courses/c3-deep-learning.md)
- **Previous Session:** [Session 09](c3-deep-learning-session-09.md) — Focuses on autoencoders and image denoising.
- **Next Session:** [Session 11](c3-deep-learning-session-11.md) — Dives deeper into Convolutional Neural Network architectures, padding, stride, and multi-channel convolutions.

# Citations

1. Lecture Video: `https://www.youtube.com/watch?v=MoPTsD21hO8`
2. Fukushima, K. (1980). *Neocognitron: A self-organizing neural network model for a mechanism of pattern recognition unaffected by shift in position*. Biological Cybernetics, 36(4), 193-202.
3. Jevons, W. S. (1865). *The Coal Question; An Inquiry Concerning the Progress of the Nation, and the Probable Exhaustion of Our Coal-Mines*. London: Macmillan and Co.
