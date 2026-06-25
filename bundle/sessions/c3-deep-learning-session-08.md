---
type: Session
resource: https://www.youtube.com/watch?v=-tMyrY68zEM
title: 'Session 08: Autoencoders, Denoising, and Entity Embeddings'
description: An exploration of autoencoder architectures for denoising, segmentation,
  and cross-modal translation, followed by neural network-based entity embeddings
  for high-cardinality categorical data.
tags:
- Autoencoders
- Denoising Autoencoders
- Entity Embeddings
- High Cardinality
- Latent Space
- Image Segmentation
- SegNet
- Collaborative Filtering
timestamp: '2025-12-07'
---

This lecture covers advanced autoencoder architectures and representation learning, specifically focusing on denoising, image colorization, image inpainting, cross-modal translation, and semantic image segmentation, before transitioning into neural network-based entity embeddings for high-cardinality categorical data. The instructor begins by reviewing the symmetric structure of autoencoders, highlighting how their bottleneck activations serve as low-dimensional, non-linear alternatives to traditional Principal Component Analysis (PCA). The session also contrasts autoencoders with Restricted Boltzmann Machines (RBMs), explaining that while they can often be shown to be theoretically equivalent, autoencoders operate in reconstruction space whereas RBMs operate in energy space.

The second half of the lecture addresses **Entity Embeddings** for categorical data. When dealing with high-cardinality variables (such as cities, products, or users), standard one-hot encoding leads to sparse, extremely high-dimensional spaces, while sequential integer labeling can inadvertently impose arbitrary relationships (e.g., alphabetical ordering implying geographical proximity). Entity embeddings solve this by mapping discrete categories into a dense, low-dimensional continuous vector space optimized end-to-end via backpropagation. To demonstrate their power, the instructor presents a classic Kaggle competition case study (Rossmann Store Sales), where learned embeddings automatically captured actual geographical and spatial proximity of German states. The session concludes with an industrial overview of embedding-based collaborative filtering (e.g., Netflix and YouTube recommendation engines) and a student Q&A addressing the hybrid use of CNNs and RNNs for real-time edge processing in software-defined vehicles (SDVs).

# Key Concepts

- **Autoencoders vs. Restricted Boltzmann Machines (RBMs)**: Symmetric unsupervised models that can be shown to be equivalent under specific formulations. Autoencoders reconstruct inputs through a bottleneck layer, while RBMs model joint probability distributions over active units in energy space.
- **Non-linear PCA**: A vanilla autoencoder's capability to execute non-linear [dimensionality reduction](../concepts/dimensionality-reduction.md) on a bottleneck layer, allowing it to capture more complex data manifolds than linear techniques like Principal Component Analysis.
- **Denoising Autoencoders**: Networks trained by taking clean data, manually injecting noise, and computing the reconstruction loss of the noisy input against the *original, clean* data. This regularizes the network, preventing it from learning simple identity mappings.
- **Noise Corruption Schemes**: Methods used to corrupt inputs, including zero-mask noise (randomly setting features to zero), binomial pixel-flipping for binary images, and random grayscale noise selected via uniform or normal probability distributions.
- **Cross-Modal Translation**: Linking different media types (e.g., audio, text, or images) by sharing bottleneck layers in a Lego-like modular architecture. This enables translating English to French or reconstructing facial structures from speech clips.
- **Semantic Segmentation**: Pixel-level classification of images (e.g., distinguishing roads, vehicles, and pedestrians in autonomous driving scenes). The instructor reviews `SegNet`, a deep convolutional encoder-decoder model that operates on RGB input without depth modalities.
- **Entity Embeddings**: Projecting discrete categorical levels into a dense continuous space of a user-defined length (treated as a hyperparameter). The embedding weights are learned end-to-end, automatically capturing latent similarities and interactions.
- **High Cardinality**: Categorical fields containing a large number of unique categories (e.g., thousands of store IDs or cities), where traditional one-hot encoding fails due to dimensionality explosion and target encoding risks overfitting or information leakage.
- **Edge Computing & Software-Defined Vehicles (SDVs)**: The integration of low-latency, one-shot [Computer Vision](../concepts/computer-vision.md) (such as CNNs) on the edge with sequential context trackers (such as RNNs) to safely navigate complex, real-time traffic environments.

# Topics Covered

1. **Autoencoders & Dimensionality Reduction**
   - Review of symmetric autoencoder-decoder architectures and bottleneck activations.
   - Theoretical equivalence of autoencoders (reconstruction space) and RBMs (energy space).
   - Dimensionality reduction of the MNIST dataset from 784 dimensions (28x28 pixels) to a 32-dimensional latent space.
   - Conceptualizing autoencoders as non-linear equivalents of PCA.
2. **Denoising and Image Processing Applications**
   - Mechanics of Denoising Autoencoders: noise injection, forward pass, and backpropagation of error against original uncorrupted targets.
   - Noise distribution selection: uniform distributions (where every level is equally likely) versus normal distributions (where color levels near the mean are selected with higher probability).
   - Practical image restoration tasks: image colorization (grayscale-to-color) and photographic inpainting (autofilling missing or eroded patches).
   - Domain-specific training challenges (e.g., colorization models trained on natural scenes failing to reproduce urban sky blues).
3. **Historical Context & Cross-Modal Experiments**
   - The *Lena* test image: historical background of Swedish Playboy model Lena Söderberg's photograph, scanned in the mid-1970s at a Kodak lab for a conference deadline and used as an accidental gold standard due to its rich textures, focal areas, and color variance.
   - Speech-to-Image models: the CVPR 2019 *Speech2Face* framework reconstructing speaker faces from 6 seconds of YouTube audio clips.
   - Demographic extraction: capturing gender, approximate age, and race from audio features, alongside [biases, fairness, and alignment](../concepts/bias-fairness-alignment.md) issues where underrepresented skin tones or facial shapes in the training set lead to poor reconstruction.
4. **Visual Scene Understanding & Semantic Segmentation**
   - Image segmentation vs. simple obstacle detection in self-driving cars (common-sense designs where knowing *something* is there to avoid bumping into is enough, versus full classification).
   - Analysis of `SegNet` (a deep convolutional encoder-decoder) classifying 37 different semantic classes.
   - Assistive devices for visually impaired individuals (wearable camera spectacles coupled with cloud-based semantic segmentation).
5. **Entity Embeddings for High-Cardinality Categorical Data**
   - Pitfalls of alphabetical sequential labeling (e.g., USA placed next to Uganda alphabetically but geographically distinct) and one-hot encoding (the curse of dimensionality).
   - Target encoding mechanics (replacing categories with target mean values), its overfitting risks, and vulnerability to information leakage during cross-validation.
   - Embedding categorical variables as learnable weight layers within the neural network, treating vector size as a model hyperparameter.
   - Case study: Rossmann Store Sales forecasting competition, showing how 10-dimensional store embeddings and 6-dimensional state embeddings capture geographical relationships (e.g., Saxony and Thuringia grouping together, Hamburg and Schleswig-Holstein grouping together in the latent space).
6. **Collaborative Filtering & Recommendation Engines**
   - Embedding millions of users and items (e.g., Netflix, YouTube) into joint continuous latent spaces (e.g., 64-element movie vectors and 128-element user vectors).
   - Combining dense vectors with numeric features to predict ratings, click-through rates, and customer engagement.
7. **Student Q&A, Edge Processing, & History of Science**
   - Comparison of sequential continuous integer numbering vs. vectorial representations (expanding the feature space by a square to capture unique semantic relationships).
   - Popularity of wavelets and Fourier analysis in the 1990s and their displacement by deep learning.
   - Discussion on the democratization of technology: scientific breakthroughs of the 1920s (Wolfgang Pauli's Exclusion Principle, Werner Heisenberg's Uncertainty Principle) and PhD-level 1990s denoising algorithms are now standard high school or classroom demonstration exercises.
   - Real-time processing in SDVs: hybrid CNN-RNN configurations ensuring rapid, low-latency obstacle evaluations on the edge.

# Materials

- **Slides**:
  - `20251207_DL_C8S1_AutoEncoders.pdf` (Autoencoders, Denoising, and SegNet)
  - `20251207_Entity-Embeddings.pdf` (Categorical Embeddings, Rossmann Sales, and Recommenders)
- **Class Chat**: Present
- **Video Recording**: YouTube Video ID [-tMyrY68zEM](https://www.youtube.com/watch?v=-tMyrY68zEM)

# Related

- Parent Course: [C3: Deep Learning](../courses/c3-deep-learning.md)
- Sibling Sessions:
  - [Session 07: Introduction to Autoencoders](c3-deep-learning-session-07.md)
  - [Session 09: Convolutional Neural Networks (CNNs)](c3-deep-learning-session-09.md)
- Cross-Cutting Concepts:
  - [Neural Network Architectures](../concepts/neural-network-architectures.md)
  - [Embeddings and Vector Representations](../concepts/embeddings-and-representations.md)
  - [Dimensionality Reduction and Feature Extraction](../concepts/dimensionality-reduction.md)
  - [Computer Vision](../concepts/computer-vision.md)
  - [Generative Modeling](../concepts/generative-modeling.md)
  - [Bias, Fairness, and Alignment](../concepts/bias-fairness-alignment.md)
  - [Time Series and Forecasting](../concepts/time-series-forecasting.md)

# Citations

1. Course Lecture Recording: `https://www.youtube.com/watch?v=-tMyrY68zEM`
2. Kamyshanska, H., & Memisevic, R. (2015). *The Potential Energy of an Autoencoder*. IEEE Transactions on Pattern Analysis and Machine Intelligence, 37(11), 2261-2273.
3. Badrinarayanan, V., Kendall, A., & Cipolla, R. (2017). *SegNet: A Deep Convolutional Encoder-Decoder Architecture for Image Segmentation*. IEEE Transactions on Pattern Analysis and Machine Intelligence, 39(12), 2481-2495.
4. Oh, T. H., Dobrygowski, T., Frruhstuck, C., Patel, W., Chang, F., Oprysko, J., & Freeman, W. T. (2019). *Speech2Face: Learning the Face Behind a Voice*. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR).
5. Guo, C., & Berkhahn, F. (2016). *Entity Embeddings of Categorical Variables*. arXiv preprint arXiv:1604.06737.
6. Covington, P., Adams, J., & Sargin, E. (2016). *Deep Neural Networks for YouTube Recommendations*. Proceedings of the 10th ACM Conference on Recommender Systems (RecSys).
