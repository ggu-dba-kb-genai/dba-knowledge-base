---
type: Session
resource: https://www.youtube.com/watch?v=RE2UX6rU-0I
title: 'Session 06: No-Code Deep Learning Pipeline on Azure ML Studio'
description: A hands-on session demonstrating how to build, train, and evaluate a
  PyTorch-based image classification pipeline using Azure Machine Learning Designer.
tags:
- Azure ML Studio
- No-Code AI
- PyTorch
- DenseNet
- Image Preprocessing
- Computer Vision
- Model Evaluation
timestamp: '2025-11-30'
---

In Session 06, Dr. Raj leads an end-to-end, hands-on session building a deep learning image classification pipeline using the **Azure Machine Learning Designer** (Classic pre-built components). The session begins with a theoretical orientation that situates Deep Learning as a subset of Machine Learning focused on unstructured data like images, audio, and video, contrasting it with traditional ML which typically handles structured tabular data. Using a visual, drag-and-drop workflow, students learn how raw unstructured data is converted, preprocessed, split, trained with a neural network, and evaluated, providing an intuitive, pipeline-centric understanding before transitioning to code-based deep learning in PyTorch and Google Colab in subsequent sessions.

The primary workflow utilizes a sample dataset containing 30 animal images (10 cats, 10 dogs, 10 frogs) to train an untrained **DenseNet** model powered by the **PyTorch** framework. The instructor demonstrates the precise sequence of components: translating raw storage files with *Convert to Image Directory*, splitting the partitions into training, validation, and testing sets, and defining spatial rules using *Init Image Transformation* (such as resizing to 256x256, center cropping to 224x224, random horizontal/vertical flips, and optional grayscale conversion). By applying these transformations, students learn how to structure data flows such that training data undergoes regular preprocessing while validation and test sets are reserved in "inference" mode.

The session concludes with an exploration of model performance metrics and critical resource management. Students learn to evaluate classification probabilities for individual test files via the *Score Image Model* and view aggregate performance in *Evaluate Model*. Dr. Raj also reviews the relationship between training and validation loss curves, explaining how a divergence in these losses indicates overfitting. Finally, students learn how to upload custom datasets (such as a zipped brain tumor binary classification dataset sourced from Kaggle) to the pipeline, illustrating its modularity, and are guided through deleting active compute resources in Azure to prevent student credit exhaustion.

# Key Concepts

- **[Computer Vision](../concepts/computer-vision.md)** — Enabling machines to extract semantic features from raw image directories using standard preprocessing, spatial resizing, and deep architectures.
- **[Neural Network Architectures](../concepts/neural-network-architectures.md)** — Utilizing DenseNet as an untrained base model structure comprised of input, hidden, and output layers, which learns patterns back and forth via PyTorch.
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)** — Reviewing metric summaries like micro and macro precision, micro and macro recall, confusion matrices, and understanding class-specific averages versus global aggregation.
- **[Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md)** — Diagnosing overfitting where a model memorizes raw training samples rather than generalizing patterns, which is identified when validation loss diverges from training loss.
- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — Structuring image files into distinct, labeled folders (e.g., positive vs. negative; cat, dog, frog) so that the classifier has clear mappings to train against.
- **[Model Compression and Optimization](../concepts/model-compression-optimization.md)** — Implementing early stopping (epoch patience) and grayscale transforms to reduce computational requirements and curb unnecessary credit consumption on cloud hardware.

# Topics Covered

- **AI, ML, and DL Hierarchy**: Differentiating AI (human-like reasoning) and Machine Learning (tabular, structured data patterns) from Deep Learning (unstructured imagery, text, or audio patterns processed via neural networks).
- **Azure ML Designer Workspace Setup**: Provisioning resource groups, creating workspaces, launching Azure ML Studio, and building a pipeline using classic pre-built visual components.
- **Image Directory Preprocessing & Split**:
  - *Convert to Image Directory*: Translating raw binary image blobs into formatted directory structures.
  - *Multi-Stage Splits*: Splitting 90% of the dataset for training/validation and 10% for testing. The 90% is split again (e.g., 90/10) to separate the training partition from the validation set (the mock exam used to update network weights).
- **Spatial Image Transformations**:
  - *Resize and Crop*: Standardizing image dimensions to 256x256 pixels and center cropping to 224x224 pixels.
  - *Data Augmentation*: Applying random horizontal and vertical flips to expand the variety of training samples.
  - *Grayscale Conversion*: Optionally removing color channels to reduce the computational burden.
  - *Modes*: Setting the transformation mode to "Training" for the train partition and "Inference" for the validation and test splits.
- **Hyperparameter Configuration in PyTorch**:
  - *Epochs*: The number of complete forward and backward propagation passes through the entire training set.
  - *Batch Size*: Partitioning datasets (e.g., in batches of 16) to fit hardware constraints.
  - *Learning Rate*: Controlling weight update velocity (configured at 0.001); slow rates prevent overfitting, whereas fast learning causes memorization of training instances.
  - *Patience (Early Stopping)*: Establishing a trial limit (number of epochs) to stop the job automatically once validation loss plateaus.
  - *Random Seed*: Setting a seed to randomize data allocation and prevent sequential learning bias.
- **Prediction Scoring and Metric Analysis**:
  - *Score Image Model*: Generating class-wise probabilities (dog, cat, frog) for each test image, assigning the label with the highest probability.
  - *Evaluate Model*: Reviewing the confusion matrix alongside micro vs. macro precision and recall averages.
- **Deploying a Custom Dataset**: Uploading a zipped Kaggle brain tumor classification dataset as a "file" type asset, demonstrating how to swap the input node of the pipeline while keeping the preprocessing and training logic intact.
- **Resource Decommissioning**: Step-by-step guidance on deleting compute clusters or deleting the entire resource group via the Azure portal to avoid exhausting student subscription credits.

# Materials

- **Workspace**: Azure Machine Learning Studio (Designer UI)
- **Built-in Dataset**: Animal Images Dataset (Cats, Dogs, Frogs from Open Image Dataset)
- **Custom Dataset**: Zipped Brain Tumor Classification Dataset (positive/negative labels sourced from Kaggle)
- **Interactive Chat**: Live discussions on selecting *Score Image Model* (for unstructured image pipelines) instead of the tabular *Score Model* component, and how to verify student credit balances under Cost Management / Education subscription.
- **Recording**: Video session 06 is available (`RE2UX6rU-0I`).

# Related

- **Parent Course**: [Deep Learning](../courses/c3-deep-learning.md)
- **Previous Session**: [Session 05](c3-deep-learning-session-05.md) (2025-11-29) — Deep Learning Theory & Foundations
- **Next Session**: [Session 07](c3-deep-learning-session-07.md) (2025-12-06) — Code-Based Deep Learning & Optimization in Colab

# Citations

1. [Deep Learning Session 06 Video](https://www.youtube.com/watch?v=RE2UX6rU-0I) - Official lecture recording.
2. [Azure Machine Learning Designer Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/concept-designer) - Official guide on pre-built no-code pipelines.
3. [PyTorch Machine Learning Framework](https://pytorch.org/) - Open-source deep learning library.
