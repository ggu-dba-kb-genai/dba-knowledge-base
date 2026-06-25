---
type: Session
resource: https://www.youtube.com/watch?v=604-j9tdQQQ
title: 'Session 11: Convolutional Neural Networks, Pooling, and Classic Architectures'
description: An in-depth study of Convolutional Neural Networks (CNNs), covering mathematical
  convolutions, stride, padding, pooling layers, and landmark architectures like LeNet,
  AlexNet, and VGG.
tags:
- Convolutional Neural Networks
- Computer Vision
- CNN Architectures
- Pooling
- Data Augmentation
timestamp: '2025-12-20'
---

This session provides an in-depth, graduate-level study of **Convolutional Neural Networks (CNNs)** and their central role in [Computer Vision](../concepts/computer-vision.md). The lecture begins by contrasting traditional, expert-driven, rule-based image processing with modern deep representation learning. Traditional approaches relied heavily on hardcoded mathematical rules and expert-defined feature extractors, which were brittle to perspective shifts (e.g., a circle looking like an ellipse when viewed from an angle) and failed to scale. In contrast, modern CNNs learn hierarchical features automatically via backpropagation. The ultimate proving ground for validating these systems is the **ImageNet** dataset, a massive crowdsourced benchmark initiated by Fei-Fei Li at Stanford containing over 14 million annotated images across 20,000+ categories.

The core mechanics of CNNs are systematically disassembled, beginning with the **convolution operation** where an input matrix and a kernel (filter) are combined via element-wise multiplication and summation to output a scalar value. Key hyperparameters that govern the spatial dimensions of output feature maps are analyzed: input dimension ($W$), filter size ($F$), stride ($S$), and padding ($P$). The output dimension calculation formula is defined as:
$$\text{Output Width} = \frac{W - F + 2P}{S} + 1$$
Crucially, CNNs achieve dramatic parameter reduction compared to fully connected Multi-Layer Perceptrons (MLPs) through two principles: **weight sharing** (applying the same filter parameters across different spatial regions because a feature detector is translation-invariant) and **sparse connectivity** (connecting output units only to localized receptive fields in the input).

The session also covers pooling operations (Max, Min, Average, and Sum pooling) used for [Dimensionality Reduction](../concepts/dimensionality-reduction.md) and local translational invariance. It highlights landmark [Neural Network Architectures](../concepts/neural-network-architectures.md), starting from the historical **LeNet-5** (Yann LeCun's 1998 digits recognizer utilizing $5\times5$ filters and sum pooling), transitioning to the breakthrough **AlexNet** (2012) which won the ILSVRC challenge by combining GPU acceleration, ReLU activations, dropout, and **data augmentation** techniques like cropping, stretching, color shifts, and mirroring. It introduces deep architectures like **VGG-16/19** (demonstrating the power of simple, stacked $3\times3$ filters with 1-pixel padding), Microsoft's **ResNet** (employing residual skip connections to scale depth up to 152 layers), and Google's **GoogLeNet** (introducing $1\times1$ bottleneck convolutions). The session concludes by showing downstream visual applications including [Transfer Learning](../concepts/transfer-learning-fine-tuning.md), image segmentation (Faster R-CNN), image annotation, video classification (Karpathy's multi-frame tracking), and depth map prediction (David Eigen's multi-scale networks).

# Key Concepts

- **Convolution Operation** — A mathematical combination of an input matrix and a kernel (filter) via element-wise multiplication and summation, generating a feature map.
- **Weight Sharing & Sparse Connectivity** — Structural principles that enforce parameter efficiency. Weight sharing slides identical filter weights across all spatial locations, while sparse connectivity limits receptive fields to localized neighborhoods instead of fully connected dense layers.
- **Padding ($P$)** — Adding border values (typically zeros) around the input matrix to preserve spatial resolution and retain crucial spatial features at the edges (e.g., classifying objects near image borders). Preserving spatial resolution for an $n \times n$ odd-sized filter requires $(n-1)/2$ padding.
- **Stride ($S$)** — The stepping rate at which a filter moves across the input matrix. Larger strides reduce output dimensions and save computation but risk losing intermediate spatial details.
- **Pooling Layers** — Sub-sampling operations (Max, Min, Average, Sum pooling) that reduce spatial map dimensions, saving computational cost and providing local translational invariance.
- **Data Augmentation** — Artificially inflating dataset scale and diversity by applying random geometric and color transformations to training images (e.g., vertical/horizontal mirroring, cropping, stretching, and color jittering).
- **Landmark Architectures**:
  - **LeNet-5 (1998)**: Yann LeCun's classic 5-layer digit recognition network for MNIST utilizing $5\times5$ filters and sum pooling, optimizing 60,000 parameters.
  - **AlexNet (2012)**: The 8-layer network by Krizhevsky et al. that breached the 20% ImageNet error barrier using ReLU, GPUs, dropout, and data augmentation.
  - **VGG-16 / VGG-19**: Oxford Visual Geometry Group's deep architectures proving that stacking small, uniform $3\times3$ filters with single-pixel padding is superior to larger filters.
  - **ResNet & GoogLeNet (Inception)**: Extreme deep networks. ResNet scales up to 152 layers via residual bypass learning, while GoogLeNet scales via multi-scale parallel filters and $1\times1$ bottleneck convolutions.
- **Knowledge Transfer & Downstream Vision** — Techniques utilizing a pre-trained backbone (e.g., ImageNet classification weights) and re-initializing/fine-tuning the classifier on small custom datasets ([Transfer Learning](../concepts/transfer-learning-fine-tuning.md)).

# Topics Covered

- **ImageNet Benchmark & Crowd-Sourcing** — Scale, 14 million annotations, 20,000+ categories, and Stanford's manual tagging effort led by Fei-Fei Li.
- **Traditional Computer Vision Limitations** — The brittle, mathematically heavy nature of hand-coded feature engineering and vulnerability to perspective distortions.
- **Biological Inspiration & The Neocognitron** — Fukushima's early neural system modeling visual S-cells (simple cells for edge detection) and C-cells (complex cells) to recognize incomplete Japanese characters.
- **The Mathematics of 2D Convolution** — Worked matrix calculation examples, spatial dimensions, and parameter counting.
- **Pooling Mechanisms & Hyperparameters** — Max, min, average, and sum pooling configurations and calculations.
- **Dimension Reduction Calculations** — Utilizing the formula $(W-F+2P)/S+1$ to determine the spatial size of output feature maps.
- **Classic CNN Topologies** — Detailed walkthroughs of LeNet-5, AlexNet, VGG models, ResNet, and GoogLeNet.
- **Downstream Computer Vision Applications** — Image segmentation (Faster R-CNN), image annotation, video classification (Andrej Karpathy's Stanford/Google work), depth map prediction (David Eigen), and artistic style transfer (Leon Gatys).
- **Administrative Session Q&A** — Reviewing the upcoming group assignment (non-technical, executive-style scoping report analyzing business problems).

# Materials

- **Slides**: 
  - `20251220_C8S1_CNN-1.pdf`
  - `20251220_C8S1_CNN-2.pdf`
- **Recording**: Video ID `604-j9tdQQQ` is available.
- **Chat**: Yes, student-professor discussions on crowdsourcing, filter sizing, and padding are captured.

# Related

- **Parent Course**: [Deep Learning](../courses/c3-deep-learning.md)
- **Previous Session**: [Session 10](c3-deep-learning-session-10.md)
- **Next Session**: [Session 12: Advanced Vision Architectures](c3-deep-learning-session-12.md)

# Citations

1. [Session Recording](https://www.youtube.com/watch?v=604-j9tdQQQ)
2. Fukushima, K. (1980). Neocognitron: A self-organizing neural network model for a mechanism of pattern recognition unaffected by shift in position. *Biological Cybernetics*, 36(4), 193-202.
3. LeCun, Y., Bottou, L., Bengio, Y., & Haffner, P. (1998). Gradient-based learning applied to document recognition. *Proceedings of the IEEE*, 86(11), 2278-2324.
4. Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). ImageNet classification with deep convolutional neural networks. *Advances in Neural Information Processing Systems*, 25, 1097-1105.
5. Simonyan, K., & Zisserman, A. (2014). Very deep convolutional networks for large-scale image recognition. *arXiv preprint arXiv:1409.1556*.
6. Karpathy, A., Toderici, G., Shetty, S., Leung, T., Sukthankar, R., & Li, F. F. (2014). Large-scale video classification with convolutional neural networks. *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 1725-1732.
7. Eigen, D., Puhrsch, C., & Fergus, R. (2014). Depth map prediction from a single image using a multi-scale deep network. *Advances in Neural Information Processing Systems*, 27, 2366-2374.
8. Gatys, L. A., Ecker, A. S., & Bethge, M. (2015). A neural algorithm of artistic style. *arXiv preprint arXiv:1508.06576*.
