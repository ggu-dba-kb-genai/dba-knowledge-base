---
type: Session
resource: https://www.youtube.com/watch?v=IHBq-ZO2MIo
title: 'Session 03: Backpropagation & Optimization'
description: A deep dive into the mathematical foundation of backpropagation, gradient
  descent optimization, and various weight update strategies such as online, batch,
  and mini-batch learning.
tags:
- deep-learning
- backpropagation
- gradient-descent
- optimization
- mini-batch
- vanishing-gradients
- explainability
timestamp: '2025-11-22'
---

This session bridges the conceptual foundations of multi-layer perceptrons (MLPs) with the mathematical mechanics of network optimization. Led by Dr. Srinivasa Varadharajan Lakshminarasimhan, the lecture details the core mathematics of backpropagation, where partial derivatives of a cost function (such as Sum of Squared Errors) are calculated layer-by-layer, moving backward from the output layer to update weights and biases using gradient descent. The instructor establishes a rigorous layer-wise notation to track transfer functions ($z^l_j$), activations ($a^l_j$), biases ($b^l_j$), and weights ($w^l_{jk}$), explaining how local derivatives propagate error backwards via the calculus chain rule.

The session contrasts three major training regimes used to update model parameters in practice: online (stochastic), batch, and mini-batch gradient descent. The discussion highlights the trade-offs of each approach regarding convergence speed, computational overhead, and stochastic noise. The lecture wraps up by outlining the primary challenges of deep architectures—particularly the "vanishing gradient" problem caused by successive compounding of fractional derivatives when using sigmoid activations in hidden layers, and the issue of model explainability, noting that tools like LIME and SHAP only offer approximate post-hoc explanations for what is fundamentally a "black box."

# Key Concepts

- **[Neural Network Architectures](../concepts/neural-network-architectures.md)** — The structural design of fully connected feed-forward networks, where layer outputs serve as inputs to successive layers, and parameters (weights and biases) are iteratively optimized.
- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — The optimization paradigm where a network's parameters are systematically tuned to minimize an objective cost function $J$ over a training dataset.
- **Backpropagation** — The backward pass algorithm that uses the calculus chain rule to compute the partial derivative of the cost function with respect to every weight and bias in the network.
- **Gradient Descent** — The optimization algorithm that updates parameters in the direction opposite to the gradient of the cost function, scaled by a learning rate ($\eta$):
  $$p_{new} = p_{old} - \eta \nabla J$$
- **Weight Update Strategies**:
  - *Online Update (Stochastic)*: Updates parameters after processing each individual training record; highly noisy but computationally lightweight per step.
  - *Batch Update*: Computes errors across the entire dataset before making a single parameter update; highly stable but computationally prohibitive for large datasets.
  - *Mini-Batch Update*: Updates parameters using randomly selected small subsets (typically of size 64 to 512); balances computational stability with stochastic convergence benefits.
- **Epoch** — A single complete training pass where the neural network has processed every record in the training dataset once.
- **[Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md) & Overfitting** — The risk of a network with excessive parameters perfectly memorizing training data (achieving near-zero training error) while losing generalization capability on unseen datasets.
- **Vanishing Gradients** — A major issue in deep networks using sigmoid activations, where successive multiplication of small derivatives (less than 1, since the maximum derivative of the sigmoid is $0.25$) during backpropagation drives early layer gradients toward zero, halting learning.
- **[Explainable AI (XAI)](../concepts/explainable-ai.md)** — Explores the difficulty of tracing and interpreting individual weights or neurons, which makes deep networks "black boxes." Dr. Lakshminarasimhan notes that tools like LIME and SHAP provide approximate post-hoc explanations rather than exact interpretations of weight significance.

# Topics Covered

- **Theoretical Capacity & Guidelines**: 
  - The Universal Approximation Theorem shows that two hidden layers are sufficient to represent any non-linear function for structured data, provided there are enough neurons.
  - Deep neural networks (more than 2 hidden layers) are primarily suited for unstructured data (images, text, audio, video).
- **Backpropagation Mathematics**:
  - Establishing notation for multi-layer tracking: $w^l_{jk}$ represents the weight to neuron $j$ in layer $l$ from neuron $k$ in layer $l-1$.
  - Expressing transfer functions ($z^l_j$) and activations ($a^l_j$):
    $$z^l_j = b^l_j + \sum_k w^l_{jk} a^{l-1}_k$$
    $$a^l_j = \sigma(z^l_j)$$
  - Formulating the gradient via the calculus chain rule:
    $$\frac{\partial J}{\partial w^l_{jk}} = \frac{\partial J}{\partial a^l_j} \cdot \frac{\partial a^l_j}{\partial z^l_j} \cdot \frac{\partial z^l_j}{\partial w^l_{jk}}$$
  - Solving individual component derivatives (e.g., sigmoid derivative $\frac{\partial a}{\partial z} = a(1-a)$, and $\frac{\partial z^l_j}{\partial w^l_{jk}} = a^{l-1}_k$).
- **Comparison of Optimization Regimes**: Detailed analysis of online, batch, and mini-batch weight updates, highlighting the epoch-to-iteration relationships. For datasets smaller than 2,000 samples, batch gradient descent is recommended, whereas mini-batch (sizes of 64–512) is preferred for larger datasets.
- **Toy Dataset Case Study**: Discussion of flattening small image datasets (such as the CIFAR-10 dataset, which contains 10 classes of objects like aeroplanes, birds, cats, etc., but was colloquially referred to in class as "emnest") into structured columns ($32 \times 32 = 1024$ features) to show how shallow networks can easily overfit if capacity is unrestricted.

# Materials

- **Slides**: 
  - `Session 03 - (22 Nov 2025).pdf`
  - `Session03_Slides_2025-11-22.pdf`
- **Lecture Recording**: YouTube video ID [IHBq-ZO2MIo](https://www.youtube.com/watch?v=IHBq-ZO2MIo)
- **Class Chat Log**: Yes, interactive discussion included in the session archive.

# Related

- Parent Course: [Deep Learning](../courses/c3-deep-learning.md)
- Sibling Sessions:
  - [Session 01: Introduction to Deep Learning](c3-deep-learning-session-01.md)
  - [Session 02: Introduction to Neural Networks & MLPs](c3-deep-learning-session-02.md)
  - [Session 04: Mitigating Vanishing Gradients & Overfitting](c3-deep-learning-session-04.md)
  - [Session 05: Optimizers and Learning Rate Scheduling](c3-deep-learning-session-05.md)

# Citations

1. Course Lecture: Session 03 (22 Nov 2025). YouTube video ID: [IHBq-ZO2MIo](https://www.youtube.com/watch?v=IHBq-ZO2MIo).
2. Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). *Learning representations by back-propagating errors*. Nature, 323(6088), 533-536.
3. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
