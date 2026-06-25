---
type: Session
resource: https://www.youtube.com/watch?v=_dv6HxbIngc
title: 'Session 07: Unsupervised Representation Learning — Autoencoders & Principal
  Component Analysis (PCA)'
description: An in-depth session introducing unsupervised representation learning
  via Autoencoders and classical Principal Component Analysis (PCA), exploring their
  mathematical foundations, cross-modal generative AI applications, and dimensionality
  reduction trade-offs.
tags:
- autoencoders
- pca
- dimensionality-reduction
- eigenvalue-decomposition
- regularization
- embeddings
- generative-modeling
- computer-vision
timestamp: '2025-12-06'
---

Session 07 of the [Deep Learning](../courses/c3-deep-learning.md) course delivers an in-depth transition from deep learning optimization techniques to unsupervised representation learning methods, focusing specifically on **Autoencoders** and classical **Principal Component Analysis (PCA)**. The session opens with crucial academic guidance for Doctor of Business Administration (DBA) students, emphasizing high-level business problem-solving, qualitative research frameworks, and expert validation (such as qualitative interviews with CEOs or CTOs) over deep engineering and code implementation. The instructor then conducts a comprehensive retrospective of deep learning optimization and regularization foundations. This review covers weight and bias parameter mechanics, backpropagation, and how activation functions like sigmoids trigger the vanishing gradient problem. He reviews how the Rectified Linear Unit (ReLU) activation function alleviates this, and explains optimization enhancements such as mini-batch gradient descent, momentum (smoothing gradients using exponential moving averages), RMSProp (normalizing learning rates with variance models), and Adam (adaptive momentum). Parameter initialization via the Javier/Glorot method is highlighted alongside overfitting mitigations, contrasting dropout regularization (preventing co-adaptation) with batch normalization (standardizing activations across layers to stabilize learning scales).

The lecture then introduces the core mechanics of unsupervised [Generative Modeling](../concepts/generative-modeling.md) and [Dimensionality Reduction](../concepts/dimensionality-reduction.md) using Autoencoders. These architectures utilize mirror symmetry to reconstruct original inputs at the output layer. By squeezing high-dimensional data through a central, lower-dimensional bottleneck layer, autoencoders extract low-dimensional [embeddings](../concepts/embeddings-and-representations.md). The instructor demonstrates how autoencoders serve as a stepping stone toward generative AI; by decoupling and mixing encoders and decoders across modalities, models can achieve cross-modal translation (e.g., combining an English text encoder with a French decoder, or combining a text encoder with an image decoder to perform text-to-image synthesis). Additional applications include image denoising, auto-filling, anomaly detection, and semantic object segmentation (e.g., SegNet). 

To contrast neural-network-based approaches with classical techniques, the session details the mathematical foundation of Principal Component Analysis (PCA). PCA addresses multi-collinearity by rotating feature space coordinates to project high-dimensional numerical inputs onto uncorrelated, orthogonal axes called principal components. This is mathematically formulated as an eigenvalue decomposition problem ($Ax = \lambda x$) on the dataset's symmetric covariance matrix, where eigenvectors represent principal directions of variance and eigenvalues represent the magnitude of variance (stretching) along those directions. Using a chemical analysis of wine dataset as a case study (13 features across Barolo, Grignolino, and Barbara wines), the instructor details implementation in R, comparing the faster `princomp` function (covariance-based) with the SVD-based, numerically stable `prcomp` function. The lecture concludes by evaluating the trade-off between PCA's linear combinations and the non-linear manifold learning capabilities of autoencoders, highlighting how non-linear neural networks achieve lower reconstruction errors at the expense of direct mathematical explainability.

# Key Concepts

- **[Dimensionality Reduction and Feature Extraction](../concepts/dimensionality-reduction.md)**: Simplifying high-dimensional feature spaces while preserving maximum data variance. The session contrasts linear projection via PCA with the non-linear compression capabilities of neural bottleneck layers.
- **Autoencoders**: Symmetric [Neural Network Architectures](../concepts/neural-network-architectures.md) consisting of an encoder and a decoder. They are trained to reconstruct their inputs, forcing the network to learn compact, lower-dimensional representations at the central bottleneck layer.
- **[Embeddings and Vector Representations](../concepts/embeddings-and-representations.md)**: Continuous, low-dimensional vectors generated at the bottleneck of an autoencoder. They capture semantic features of inputs and can be connected across different models to perform cross-modal tasks such as text-to-image generation or machine translation.
- **Principal Component Analysis (PCA)**: A classical, unsupervised technique that projects correlated variables into a set of orthogonal, uncorrelated variables called principal components, ordered by descending variance.
- **Eigenvalue Decomposition**: The mathematical foundation of PCA, where the covariance matrix ($A$) of numerical features is decomposed to solve $Ax = \lambda x$. The eigenvectors ($x$) represent orthogonal principal directions, and the eigenvalues ($\lambda$) denote the variance magnitude along those directions.
- **[Generative Modeling](../concepts/generative-modeling.md)**: Unsupervised frameworks that learn underlying data distributions. The modular coupling of encoders and decoders serves as a fundamental building block for generative AI applications.
- **[Explainable AI (XAI)](../concepts/explainable-ai.md)**: The structural trade-off between model capacity and interpretability. While PCA components are linear combinations of original variables (making them mathematically traceable through loadings), they remain difficult to interpret in physical domain terms. Autoencoders capture complex, non-linear manifolds but offer even less direct explainability.
- **[Computer Vision](../concepts/computer-vision.md) and Image Reconstruction**: Unsupervised spatial feature extraction. The session highlights compressing MNIST handwritten digits (784 dimensions down to a 32-element bottleneck vector), image denoising (reconstructing original inputs from corrupted or zero-masked versions), and object segmentation (e.g., SegNet).
- **Batch Normalization and Dropout**: Regularization methodologies. Dropout prevents co-adaptation by randomly zeroing out a fraction of activations during training, whereas Batch Normalization standardizes activations across mini-batches at each hidden layer to stabilize training when inputs possess highly disparate scales.

# Topics Covered

- **DBA Program Philosophy & Dissertation Guidance**: Emphasizing manager-level problem-solving, qualitative research frameworks, and expert validation (qualitative interviews with CEOs, CTOs, and cyber security experts) over engineering and code implementation.
- **Deep Learning Retrospective**:
  - Parameters (weights as connection strengths, biases as baseline activities).
  - Backpropagation, sigmoids, and the vanishing gradient problem.
  - Alleviating vanishing gradients using Rectified Linear Unit (ReLU) activations.
  - Optimization frameworks: mini-batch training, step decay, exponential decay, momentum, RMSProp, and Adam.
  - Weight initialization via the Javier/Glorot uniform distribution.
- **Regularization & Activation Stabilization**: Mechanism of dropout regularization (and weight scaling by the presence probability $p$ at inference) versus batch normalization.
- **Autoencoders vs. Restricted Boltzmann Machines (RBM)**: A brief comparison of unsupervised models, noting that autoencoders operate in reconstruction space while RBMs operate in energy space.
- **Autoencoder Architecture & Cross-Modal Systems**:
  - Modular encoder-decoder structures with a low-dimensional bottleneck.
  - Swapping modules to bridge different modalities (English text encoder to French decoder, or text encoder to image/audio decoders).
  - MNIST reconstruction (28x28 grayscale pixels flattened to 784, compressed to 32 dimensions).
- **Principal Component Analysis (PCA) Mathematics**:
  - The role of standard deviation and variance in feature utility.
  - Multi-collinearity and coordinate axis rotation.
  - Constructing symmetric covariance matrices.
  - Solving the eigenvalue problem ($Ax = \lambda x$) to obtain orthogonal eigenvectors and eigenvalues.
  - Rotating data points into principal component coordinates via matrix multiplication.
- **Wine Dataset Case Study**: 
  - Chemical analysis of 13 numerical features across 178 wines (Barolo, Grignolino, and Barbara).
  - Feature scaling: why scaling is essential for variables of different units (e.g., weight vs. micronutrients) but should be skipped for variables of the same physical quantity.
  - Implementation in R comparing `princomp` (faster, covariance-eigenvalue-based) and `prcomp` (numerically stable, Singular Value Decomposition/SVD-based).
  - Selecting principal components using cumulative variance thresholds (e.g., 8 components explaining over 92% of variance) and the scree plot "elbow" rule of thumb.
  - Visualizing class separation and identifying outliers using 2D biplots.
- **Linear vs. Non-linear Dimensionality Reduction**: Contrasting linear coordinate rotation in PCA with non-linear activation functions in autoencoders to map curved data manifolds.

# Materials

- **Slides**: 
  - `20251129_DL_C8S1_AutoEncoders.pdf` (Autoencoders)
  - `20251206_DL_C8S1_PCA.pdf` (Principal Component Analysis)
- **Recording**: YouTube Video ID `_dv6HxbIngc`
- **Chat Present**: Yes

# Related

- **Parent Course**: [Deep Learning](../courses/c3-deep-learning.md)
- **Adjacent Sessions**:
  - [Session 06](c3-deep-learning-session-06.md) — Optimization and Regularization Fundamentals
  - [Session 08](c3-deep-learning-session-08.md) — Categorical Embeddings and Applications

# Citations

1. YouTube video recording: `https://www.youtube.com/watch?v=_dv6HxbIngc`
2. Glorot, X., & Bengio, Y. (2010). "Understanding the difficulty of training deep feedforward neural networks." *Proceedings of the Thirteenth International Conference on Artificial Intelligence and Statistics*.
3. Pearson, K. (1901). "On lines and planes of closest fit to systems of points in space." *Philosophical Magazine*, 2(11), 559-572.
