---
type: Session
resource: https://www.youtube.com/watch?v=tLWt6TajUYU
title: 'Session 02: Machine Learning Algorithms, Unsupervised Learning, and Deep Learning
  Foundations'
description: An overview of core supervised and unsupervised algorithms, the transition
  to deep learning and neural networks, vector representations of text, and data scale
  classification.
tags:
- supervised-learning
- unsupervised-learning
- classification
- deep-learning
- natural-language-processing
- vector-embeddings
- transfer-learning
- data-types
timestamp: '2025-09-21'
---

This session provides a comprehensive conceptual bridge between traditional machine learning foundations and deep learning architectures, analyzing the shift from expert-codified rules to data-driven probabilistic learning. The lecture explores classification paradigms—including logistic regression, decision trees, K-nearest neighbors, Naive Bayes, and random forests—and contrasts them with unsupervised approaches such as clustering and association rule mining. It then transitions to the history and mechanics of neural networks, illustrating how modern models leverage continuous vector spaces and high-dimensional embeddings to process unstructured image and text data.

The lecture also features a practical demonstration of transfer learning, showing how a 50-layer convolutional neural network (ResNet-50) trained on generic images can be fine-tuned to classify medical chest X-rays with high accuracy. The class concludes by introducing data-type classifications—categorizing variables as quantitative (discrete vs. continuous) or qualitative (nominal vs. ordinal)—and discussing the enduring role of human business intuition, feature engineering, and ethical alignment in increasingly automated machine learning pipelines.

# Key Concepts

- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — Explores classification and regression algorithms, including distance-based metrics, probabilistic mappings, and ensemble models to predict target variables.
- **[Explainable AI (XAI)](../concepts/explainable-ai.md)** — Discusses the inherent trade-off between model interpretability and predictive accuracy, contrasting highly interpretable rule-based decision trees with opaque ensemble models like Random Forests.
- **[Generative Modeling](../concepts/generative-modeling.md)** — Introduced via Naive Bayes, which estimates joint probability distributions of features to classify and simulate new data points, contrasting with discriminative models that focus on linear boundary separation.
- **[Computer Vision](../concepts/computer-vision.md)** — Examines multi-layered feature detection where early layers isolate low-level geometric lines and deeper layers construct high-level semantic shapes to classify images.
- **[Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md)** — Demonstrated by adapting a pre-trained ResNet-50 model (trained on consumer images) to categorize chest X-rays into normal, COVID-19, and seasonal flu classes by tuning only the final weights.
- **[Embeddings and Vector Representations](../concepts/embeddings-and-representations.md)** — Details how text is mapped into continuous vector spaces (e.g., Word2Vec) to capture semantic relationships, supporting algebraic formulas like $King - Man + Woman = Queen$.
- **[Bias, Fairness, and Alignment](../concepts/bias-fairness-alignment.md)** — Explores how downstream models inherit sociological biases present in raw training data, demonstrated via occupational vector associations (e.g., mapping women away from "programmer" toward "nurse").
- **[Time Series and Forecasting](../concepts/time-series-forecasting.md)** — Addresses the risk of applying static regression models to time-dependent data, illustrating how spurious correlations arise from unadjusted trending variables.
- **[AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md)** — Discusses the limits of automated pipelines, emphasizing that expert feature engineering, context monitoring, and business alignment remain uniquely human roles.
- **[Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md)** — Explores how models can overfit to training data, capturing noise instead of generalizable patterns when model capacity is too high or training is excessive.
- **[Neural Network Architectures](../concepts/neural-network-architectures.md)** — Details biological neuron analogies and structural layers where connections are represented as layered linear regressions modulated by non-linear activation functions (e.g., ReLU).

# Topics Covered

- **Regression vs. Classification**: Review of regression (predicting continuous numeric outputs by minimizing squared error loss on a convex bowl) and the introduction of classification (categorizing data into discrete labels).
- **Supervised Classification Algorithms**:
  - *Logistic Regression*: A linear model mapping inputs to binary class probabilities. Showcased using the historical Framingham Risk Score study (1948) for predicting coronary heart disease.
  - *Decision Trees*: A highly intuitive model utilizing axis-parallel feature splits to generate legible rules. Mention of "oblique decision trees" proposed by Dr. Srirama Murthy (1993) to merge logistic linear separations with tree hierarchies.
  - *K-Nearest Neighbors (KNN)*: A non-parametric "lazy algorithm" (proposed in 1951) that skips formal model building and classifies points based on distance metrics from neighboring records.
  - *Naive Bayes*: A generative technique mapping joint probabilities under conditional independence assumptions, rooted in Thomas Bayes' 1763 work.
  - *Random Forests*: An ensemble model (proposed in 2001) that builds multiple randomized decision trees and aggregates their votes to optimize predictive accuracy over explainability.
- **Unsupervised Learning & Pattern Discovery**:
  - *Association Rule Mining*: Mapping relationship rules between variables/columns. Discussed via the A Priori algorithm (1994), the classic "diapers and beer" retail correlation, and Walmart’s discovery of a 7x increase in strawberry pop-tart purchases ahead of hurricanes.
  - *Clustering (K-Means)*: Grouping rows based on spatial distances (proposed in 1957). Showcased through behavioral customer segmentations (e.g., high-spending businessmen vs. low-spending retirees) that can later be labeled to seed supervised pipelines.
  - *Anomaly Detection*: Utilizing Isolation Forests (2008) to separate outliers by measuring the structural path length required to isolate a data point in random splits.
- **Optimization Challenges**: Analyzed through the Traveling Salesman Problem (TSP). Demonstrates how a 48-city journey requires navigating $10^{60}$ potential tours, solved using greedy heuristics or genetic algorithms.
- **The Evolution of Deep Learning**:
  - Review of historical milestones, starting from John McCarthy's 1956 Dartmouth vision, the biological neuron analogy, Jeffrey Hinton's 1985 backpropagation mathematics, the 2012 ImageNet breakthrough, and the rise of modern trillion-parameter models.
  - Structural layers: Neural network connections represented as layered linear regressions modulated by non-linear activation bounds (such as thresholds or rectified linear units).
- **Text Representation and Natural Language Processing**:
  - The evolution from sparse, high-dimensional one-hot encodings to dense continuous vector spaces (Word2Vec's 300 dimensions to modern GPT architectures utilizing over 12,000 dimensions).
  - Character and sub-word tokenization methods that handle typographical mistakes and dynamic vocabularies by analyzing pieces of words.
- **Variable Classification and Scales of Measurement**:
  - *Qualitative (Categorical) Scales*: Nominal variables (unordered groupings, e.g., gender, city, ZIP code) vs. Ordinal variables (ordered rankings with non-equal intervals, e.g., movie ratings, corporate ranks).
  - *Quantitative (Numeric) Scales*: Discrete variables (countable values, e.g., products sold) vs. Continuous variables (measurable values containing infinite potential fractions, e.g., height, weight).

# Materials

- **Slides**:
  - `Session 02 - (21 Sep 2025).pdf`
  - `Session02_Slides_2025-09-21.pdf`
- **Recording**: YouTube video (ID: `tLWt6TajUYU`)
- **Chat**: No chat logs are available on disk for this session.

# Related

- Sibling Sessions:
  - [Session 01: Introduction to AI and Regression Foundations](c2-foundations-ml-ai-session-01.md)
  - [Session 03: Basic Statistics and Exploratory Data Analysis](c2-foundations-ml-ai-session-03.md)
- Parent Course: [Foundations ML AI](../courses/c2-foundations-ml-ai.md)

# Citations

1. Foundations ML AI, Session 02, YouTube Video: `https://www.youtube.com/watch?v=tLWt6TajUYU`.
2. Srirama V. Murthy, "On Growing Better Decision Trees from Data," PhD Dissertation, Johns Hopkins University, Department of Computer Science (1993).
3. Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean, "Efficient Estimation of Word Representations in Vector Space," arXiv preprint arXiv:1301.3781 (2013).
4. Thomas Bayes, "An Essay towards solving a Problem in the Doctrine of Chances," Philosophical Transactions of the Royal Society of London (1763).
5. Leo Breiman, "Random Forests," Machine Learning, Vol. 45, pp. 5–32 (2001).
6. K. He, X. Zhang, S. Ren, and J. Sun, "Deep Residual Learning for Image Recognition," IEEE Conference on Computer Vision and Pattern Recognition (2016).
