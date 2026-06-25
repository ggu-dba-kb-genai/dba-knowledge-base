---
type: Session
resource: https://www.youtube.com/watch?v=ySFUr8Ux8xE
title: 'Session 09: CNNs from Scratch & Transfer Learning with Keras'
description: A hands-on session on building custom CNNs, deploying interactive web
  interfaces with Gradio, and implementing Transfer Learning using pre-trained models
  like MobileNet and VGG16 in Google Colab.
tags:
- Computer Vision
- Convolutional Neural Networks
- Keras
- TensorFlow
- Transfer Learning
- Gradio
- Google Colab
- Overfitting
- Image Classification
timestamp: '2025-12-13'
---

This session, led by Dr. Raj, transitions students from the drag-and-drop interface of Azure ML Designer Studio (used in [Session 08](c3-deep-learning-session-08.md)) to code-based deep learning workflows in Google Colab using TensorFlow and Keras. The previous session's PyTorch-based pipeline on Azure felt like a "black box" to some students, as they lacked visibility and direct control over individual layers. This hands-on session focuses on giving developers fine-grained control over model design, hyperparameter tuning, and regularization techniques. The core practical task is binary image classification to identify brain tumors from a dataset of brain MRI scans.

The class first reviews Google Colab's cloud environment, mounting Google Drive (`drive.mount('/content/drive')`) to persist data across virtual machine (VM) sessions, and unzipping datasets locally in the VM. The dataset is extremely small (approximately 50 MRI images total, with 20 negative/normal and 30 positive/tumor cases), creating a realistic scenario for analyzing training challenges. Students implement image preprocessing, utilizing Pillow/PIL to load and resize images to 128x128 pixels, converting image lists to NumPy arrays, and scaling pixel intensities. Label preprocessing is completed using one-hot encoding via Scikit-Learn (`OneHotEncoder`).

To classify the processed MRIs, Dr. Raj demonstrates building a custom Convolutional Neural Network (CNN) from scratch using `keras.Sequential`. The architecture chains three convolution blocks (32, 64, and 128 filters respectively) interleaved with Batch Normalization, Max Pooling, and a final classification head consisting of a Flatten layer, a Dense layer, a Dropout layer, and a Sigmoid activation output. Due to the small size of the dataset (only 40 images used for training and 10 for validation under an 80/20 split), the custom CNN exhibits rapid overfitting, reaching near 100% training accuracy within a few epochs while validation accuracy drops or remains low (~40%). This overfitting sparks a robust classroom discussion on regularization, tuning dropout rates (e.g., reducing the rate from 0.5 to 0.3 for such a small network), and optimization with the Adam optimizer.

To overcome dataset constraints and minimize computational overhead, the lecture introduces Transfer Learning. Students learn to load a pre-trained base model, specifically MobileNet (and VGG16), freeze the learned weights and biases (`base_model.trainable = False`), and attach their own binary classification output head. Because the base model already possesses generic feature-extraction capabilities (identifying edges, gradients, and shapes), it significantly reduces the training computational footprint. The resulting transfer learning pipeline converges quickly, delivering stable and aligned training and validation performance (~80% validation accuracy). Finally, students deploy their models interactively using Gradio, running real-time image inference on uploaded MRI scans directly inside Colab or in an external web interface. The session also highlights utilizing Google Colab's built-in AI assistant (Gemini integration) to explain code segments, suggest syntax adjustments, and generate entire templates from conversational prompts.

# Key Concepts

- **[Computer Vision](../concepts/computer-vision.md)** — Preprocessing and classifying digital brain MRI scans, handling image dimensions (width, height, channels), and using spatial feature-extraction blocks.
- **[Neural Network Architectures](../concepts/neural-network-architectures.md)** — Custom CNN construction consisting of sequential blocks of `Conv2D`, `BatchNormalization`, `MaxPooling2D`, `Flatten`, `Dense`, and output activations.
- **[Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md)** — Leveraging pre-trained networks (MobileNet and VGG16) with frozen base parameters (`trainable = False`) to utilize pre-trained weights/biases for specialized downstream binary classification.
- **[Dimensionality Reduction and Feature Extraction](../concepts/dimensionality-reduction.md)** — Max pooling downsamples spatial dimensions, decreasing the computational parameters while retaining essential structural features.
- **[Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md)** — Observing extreme overfitting during custom CNN training on a tiny 50-image dataset and correcting it using regularization techniques like Dropout.
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)** — Partitioning data using an 80% training / 20% validation split, using validation cross-entropy loss, and tracking epoch-by-epoch accuracy metrics.
- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — Standard training workflow of forward passes and backpropagation optimization using Adam to map binary inputs to categorical labels.

# Topics Covered

- **Google Colab IDE Navigation:** Allocating VM resources (RAM/Disk limits), handling cell modes (code vs. markdown/text), and utilizing Google Drive mounting to prevent session-based data loss.
- **Image Dataset Preprocessing:** Unzipping MRI image directories, traversing folder structures, resizing images to uniform dimensions (128x128 pixels), converting list data to NumPy arrays, and formatting binary classification target labels.
- **Custom CNN Architecture Assembly:** Chaining hidden layers dynamically using Keras, configuring `Conv2D` filter counts (32 -> 64 -> 128), and applying batch normalization on hidden layer outputs.
- **Overfitting Diagnostics:** Analyzing training logs to spot divergence between high training accuracy (100%) and low validation performance (40%), and adjusting dropout rates (0.5 to 0.3) to regularize the network.
- **Transfer Learning Implementations:** Initializing pre-trained MobileNet and VGG16 base models, freezing pre-trained weights to avoid retraining feature extractors, and appending customized output classifier heads.
- **Model Training and Evaluation:** Setting up training fits using Adam optimizer, cross-entropy loss functions, setting validation splits, configuring batch sizes (32), and tracking epoch convergence.
- **Interactive Web App Deployment:** Creating interactive diagnostic applications using Gradio, setting up file upload inputs, and displaying probability-based confidence classifications.
- **AI-Assisted Coding Workflows:** Utilizing built-in Colab AI tools to explain block mechanics, debug file pathing conflicts, and generate transfer learning modules from plain English prompts.

# Materials

- **Video Recording:** [YouTube Link (ySFUr8Ux8xE)](https://www.youtube.com/watch?v=ySFUr8Ux8xE)
- **Chat Transcript:** Yes (stored in the knowledge base)
- **Slides:** Not provided for this session

# Related

- Part of the **[Deep Learning](../courses/c3-deep-learning.md)** course.
- Previous Session: **[Session 08](c3-deep-learning-session-08.md)**
- Next Session: **[Session 10](c3-deep-learning-session-10.md)**

# Citations

1. University Course Lecture: [Session 09 Recording (ySFUr8Ux8xE)](https://www.youtube.com/watch?v=ySFUr8Ux8xE).
2. Keras Documentation on Transfer Learning and Fine-tuning: [Keras Developer Guides](https://keras.io/guides/transfer_learning/).
3. Howard, A. G., et al. (2017). "MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications." [arXiv:1704.04861](https://arxiv.org/abs/1704.04861).
4. Simonyan, K., & Zisserman, A. (2014). "Very Deep Convolutional Networks for Large-Scale Image Recognition" (VGG16). [arXiv:1409.1556](https://arxiv.org/abs/1409.1556).
