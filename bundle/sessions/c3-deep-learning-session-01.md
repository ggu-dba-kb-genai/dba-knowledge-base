---
type: Session
resource: https://www.youtube.com/watch?v=wMFSkWTBGmQ
title: 'Session 01: Introduction to Deep Learning & Neural Foundations'
description: An introduction to the biological foundations of neural systems and their
  translation into the mathematical models of perceptrons and deep feed-forward networks.
tags:
- Neural Networks
- Perceptron
- Biological Foundations
- Activation Functions
- Hebbian Learning
timestamp: '2025-11-15'
---

This session opens Course 3, "Deep Learning and its Variants," with an introductory lecture by Rajan (Dr. Srinivasa Varadharajan Lakshminarasimhan). Rajan draws from his extensive academic background in physics, human ophthalmology, and visual psychophysics to contextualize the historical and biological motivations behind artificial neural networks. The lecture establishes the baseline administrative details of the 4-credit course, including its 15-session breakdown (comprising 12 lectures and 3 labs led by Dr. Rajkumar) and its evaluation scheme consisting of an individual midterm written submission (60% weightage) and a group final written submission (40% weightage).

The core technical content traces the paradigm of machine learning from biological mechanics to mathematical models. Rajan contrasts [supervised learning](../concepts/supervised-learning-foundations.md) (highlighting cognitive studies where pigeons generalize art styles of Monet and Chagall) with unsupervised learning (exemplified by a mouse solving a physical maze through pattern discovery). He details the biology of the human nervous system, highlighting how ~86 billion neurons communicate electrically along axons and chemically across ~1,000 trillion synapses via neurotransmitters like dopamine and GABA. Crucially, the lecture illustrates that intelligence is a function of synaptic network density (averaging 10,000 connections per neuron in humans) rather than raw neuron count, establishing the conceptual basis for Hebbian learning ("neurons that fire together, wire together").

The lecture transitions these biological concepts into their mathematical equivalents by defining the perceptron—the foundational artificial neuron. The perceptron models dendritic inputs as feature vectors, synaptic strengths as weights, and baseline neural firing as bias. It applies linear summation followed by an activation function (such as sigmoid, tanh, or Heaviside step) to generate an output. Rajan explains that while a single perceptron is constrained to linear classification, stacking multiple neurons into a hidden layer creates a Multi-Layer Perceptron (MLP) capable of handling non-linear boundaries. The session concludes with the Universal Approximation Theorem and a preview of dense, feed-forward deep neural networks (DNNs), bridging the gap between historical hardware limitations and modern scale.

# Key Concepts

- **Biological Neuron vs. Perceptron** — Dendrites receive signals modeled as inputs $X_i$, synaptic strengths are modeled as weights $W_i$, and background activity is represented as the bias $b$. The cell body performs a weighted linear summation, which is passed through an activation function to generate the output.
- **Hebbian Learning** — A biological learning theory stating that synapses strengthen when the presynaptic and postsynaptic neurons are repeatedly active together ("neurons that fire together, wire together"), modeled in artificial networks by adjusting weights.
- **Activation Functions** — Mathematical operators applied to the weighted sum to introduce non-linearity. Examples include the Sigmoid (logistic) function, Hyperbolic Tangent (tanh), Heaviside (step) function, Signum, and Identity (linear) functions.
- **Multi-Layer Perceptron (MLP)** — Stacking multiple perceptrons in a hidden layer to form a [Neural Network Architecture](../concepts/neural-network-architectures.md) capable of learning complex, non-linear boundaries that a single linear classifier cannot solve.
- **Universal Approximation Theorem** — States that a feed-forward network with a single hidden layer and a sufficient (though potentially very large) number of non-linear neurons can approximate any continuous function on compact subsets of $\mathbb{R}^n$.
- **Feed-Forward vs. Recurrent Networks** — In feed-forward networks, information routes strictly forward from input to output without cycles. Recurrent networks contain feedback loops where information can travel backward or sideways to process sequential data.
- **The Black-Box & Explainability Dilemma** — Because dense deep networks contain highly interconnected layers of high-dimensional parameter spaces, mapping individual feature importance becomes difficult, leading to the challenges addressed by [Explainable AI (XAI)](../concepts/explainable-ai.md).

# Topics Covered

- **Course Introduction and Administration**: Structure of the 4-credit, 7.5-week course, grading schema (60% individual midterm, 40% group final), and introduction of the instructors (Rajan and Dr. Rajkumar).
- **Paradigm of Machine Learning**: Systems figuring out input-to-output relationships without explicit recipes, compared to biological learning processes.
- **Anatomy of Biological Neural Systems**: Axons, dendrites, synapses, electrical potentials, and chemical neurotransmitters (dopamine, GABA).
- **Scale and Intelligence**: Comparative neuroanatomy across animal classes (C. Elegans, fruitflies, rodents, primates, and humans) focusing on synaptic density as the primary metric of processing capability.
- **The Perceptron Model**: Mathematical formulation of the single-neuron model, calculating linear weighted sums, and applying activation functions.
- **Activation Function Types**: Comparison of step, signum, linear, sigmoid, and tanh activations for classification versus regression tasks.
- **Architectural Scaling**: Moving from a single perceptron to multi-layered, dense, feed-forward deep neural networks (DNNs) to solve non-linear classification problems.
- **Parameterization in Deep Learning**: Distinguishing between neuron count and parameter count (weights and biases), illustrating that massive 10-billion parameter models are structurally comparable to the neural scale of a frog.

# Materials

- **Slides**: `20251115_DL_C8S1_Introduction.pdf` (Introduction slide deck covering biological systems and perceptrons)
- **Chat**: Yes, student-instructor chat was present during this live interactive session.
- **Recordings**: YouTube video ID [wMFSkWTBGmQ](https://www.youtube.com/watch?v=wMFSkWTBGmQ)

# Related

- Part of the [Deep Learning](../courses/c3-deep-learning.md) course.
- Next Session: [Session 02](c3-deep-learning-session-02.md)

# Citations

1. Golden Gate University, Deep Learning Course, Session 01 Video Recording (`https://www.youtube.com/watch?v=wMFSkWTBGmQ`).
2. Stanley I. Grossman, *Calculus*, Academic Press (referred to as a calculus reference).
