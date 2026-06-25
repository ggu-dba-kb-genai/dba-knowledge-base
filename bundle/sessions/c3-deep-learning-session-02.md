---
type: Session
resource: https://www.youtube.com/watch?v=94fP72quLp8
title: 'Session 02: Multi-Layer Perceptrons & Optimization Foundations'
description: An in-depth exploration of Multi-Layer Perceptrons (MLPs), mathematical
  notations, linear/logistic regression equivalences, the XOR non-linearity challenge,
  and optimization via Maximum Likelihood Estimation and Gradient Descent.
tags:
- multi-layer-perceptron
- linear-regression
- logistic-regression
- gradient-descent
- maximum-likelihood-estimation
- convex-optimization
- xor-gate
- hyperparameters
timestamp: '2025-11-16'
---

This session bridges the theoretical foundations of single-unit perceptrons with the mathematical structures of Multi-Layer Perceptrons (MLPs) and modern optimization. The lecture, taught by Dr. Srinivasa Varadharajan Lakshminarasimhan, begins with a formalization of artificial neurons, standardizing vector notations for inputs and weights, scalar dot products, and the bias term ($b$), which biologically models background neuronal noise. The instructor establishes that a perceptron equipped with an identity activation function operates identically to a linear regression model. To reinforce this connection, the session reviews linear regression's statistical assumptions—including population normality of $y$ for a given $x$, predictions targeting the mean of the distribution, homoscedasticity (equal variance of residuals), independent and identically distributed (IID) measurements, and outlier diagnostics—contrasting simple linear regression's closed-form analytical calculus solutions for parameters $\beta_0$ and $\beta_1$ with multiple linear regression's reliance on numerical optimization.

The core limitation of single-layer perceptrons is explored through the classic XOR gate challenge. Because a single perceptron acts as a linear separator, it cannot resolve non-linearly separable relationships where identical inputs yield $0$ and differing inputs yield $1$ ($y = x_1 \neg x_2 + \neg x_1 x_2$). Solving the XOR boundary mathematically necessitates introducing a hidden layer containing at least two perceptrons whose outputs are logically combined. This transition to Multi-Layer Perceptrons drastically increases mathematical complexity, as nested activation functions compound non-linearities into highly complex compositions (e.g., $y_{21}$ nesting the sigmoid output of $y_{11}$). Due to this analytical tractability limit, MLPs and deep architectures must be solved numerically rather than analytically.

Finally, the lecture details the mathematical mechanics of deep learning optimization. It formalizes Maximum Likelihood Estimation (MLE), mathematically differentiating probability distributions from likelihood functions, and derives the convex Negative Log-Likelihood (NLL) cost function for binary classification: $-\ln(L[\theta]) = -\sum [y_i \ln(\hat{y}_i) + (1 - y_i) \ln(1 - \hat{y}_i)]$. The mechanics of Gradient Descent are systematically presented: calculating the vector gradient of partial derivatives ($\nabla f$) to find the direction of steepest incline, flipping the sign, scaling by the learning rate hyperparameter ($\alpha$), and iteratively updating parameters via the update rule $\theta_{new} = \theta_{old} - \alpha \nabla f(\theta)$. High-level training strategies are outlined, advising starting with overparameterized models and pruning them down to find the optimal trade-off between model capacity and generalization, alongside practical heuristics such as uniform activation functions across hidden layers (Occam's razor).

# Key Concepts

- **Multi-Layer Perceptron (MLP)**: Extending single-unit perceptrons to networks with hidden layers, enabling the model to learn non-linear decision boundaries. Read more on [Neural Network Architectures](../concepts/neural-network-architectures.md).
- **Linear and Logistic Equivalences**: A single perceptron maps to classical regression models based on its activation function: an identity function results in linear regression, whereas a sigmoid function maps to logistic regression. Read more on [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md).
- **Gradient Descent & Convex Optimization**: The numerical method used to optimize weights and biases according to the update rule $\theta_{new} = \theta_{old} - \alpha \nabla f(\theta)$. For binary classifications, the Negative Log-Likelihood cost function is convex, guaranteeing a unique global minimum. Read more on [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md).
- **Maximum Likelihood Estimation (MLE)**: An optimization framework that adjusts network parameters to maximize the statistical likelihood of observing the training dataset's actual labels, flipping the distribution perspective to search for parameter values ($\theta$).
- **The XOR Challenge**: A classic problem demonstrating that single linear classifiers cannot solve non-linearly separable datasets, proving the historical and theoretical necessity of multi-layer architectures.
- **Overfitting & Pruning**: The training methodology of starting with an overparameterized deep neural network and iteratively pruning weights, layers, or connections to find the ideal point on the [Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md).

# Topics Covered

- **Hebbian Learning and Biological Neurons**: Modeling dendrites, cell bodies, axons, and synaptic strengthening where inputs that consistently result in an output selectively strengthen the associated weights.
- **Formal Vector Notation**: Expressing inputs $x$ and weights $w$ as vectors, implementing the scalar product ($w \cdot x$), introducing the transfer function $z = b + \sum w_i x_i$, and augmenting vectors to include bias succinctly ($z = w \cdot x$ by prepending $1$ to input and $b$ to weights).
- **Linear Regression Assumptions**: Population normality, predictions targeting the distribution mean, homoscedasticity (equal residual variance), independent and identically distributed (IID) measurements, and diagnostics (residual plots for homoscedasticity/linearity/independence, Q-Q plots for normality, Cook's distance, leverage, and studentized residuals for outlier detection).
- **Analytical vs. Numerical Solutions**: Solving simple linear regression analytically using partial derivatives ($\beta_1 = \rho \frac{s_y}{s_x}$ and $\beta_0 = \bar{y} - \beta_1 \bar{x}$) vs. multiple linear regression's reliance on numerical methods (Gradient Descent) due to algebraic complexity.
- **Sigmoid Activations**: The mathematical formulation of the S-curve logistic function ($\phi(z) = \frac{1}{1 + e^{-z}}$) and its application to binary classification using the Motor Trend car dataset (MT cars) to determine transmission type (automatic vs. manual).
- **Solving XOR Non-Linearity**: Visualizing decision boundaries, creating two separate perceptron decision planes, and joining their outputs with a logical OR layer.
- **Multi-Layer Mathematical Intractability**: Expanding the algebraic expressions of deep hidden layers to illustrate the exponential nesting of sigmoids, rendering direct analytical calculus intractable.
- **Deriving Likelihood Functions**: Formulating binomial probability distributions, flipping variables to establish the likelihood function, and applying logarithms to transform products into sums, resulting in the convex Negative Log-Likelihood cost function.
- **Gradient Descent and Learning Rates**: Calculating partial derivatives, defining physical vector gradients, analyzing step-size impacts (overshooting vs. slow convergence), and reviewing hyperparameter search.
- **Practical Network Heuristics**: Keeping activation functions uniform across hidden layers (Occam's razor), starting with default learning rates (e.g., $10^{-3}$, $10^{-4}$, or $0.1$), and introducing specialized weight initializations (e.g., He initialization).

# Materials

- **Lecture Slides**: `20251116_DL_C8S1_Multi-Layer-Perceptron.pdf`
- **Class Chat**: Present (Zoom chat session involving live discussions on learning rates, mathematics, and business applications)
- **Video Recording**: `https://www.youtube.com/watch?v=94fP72quLp8`

# Related

- Sibling Sessions:
  - Previous: [Session 01: Introduction to Neurons and Perceptrons](c3-deep-learning-session-01.md)
  - Next: [Session 03: Backpropagation & Optimizers](c3-deep-learning-session-03.md)
- Part of Course: [Deep Learning](../courses/c3-deep-learning.md)

# Citations

1. Lecture Recording: `https://www.youtube.com/watch?v=94fP72quLp8`
2. Recommended Textbook: Ian Goodfellow, Yoshua Bengio, and Aaron Courville, *Deep Learning*, MIT Press.
3. Recommended Video Series: Josh Starmer, *StatQuest with Josh Starmer* on YouTube.
