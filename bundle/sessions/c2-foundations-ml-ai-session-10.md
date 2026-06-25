---
type: Session
resource: https://www.youtube.com/watch?v=Vc9XApUUn88
title: 'Session 10: Decision Tree Regularization and K-Nearest Neighbors'
description: This lecture covers regularization and pruning strategies for decision
  trees, alongside an in-depth exploration of the K-Nearest Neighbors (KNN) algorithm,
  its computational and dimensionality issues, and modern hybrid applications.
tags:
- decision-trees
- k-nearest-neighbors
- pruning
- regularisation
- normalization
- curse-of-dimensionality
- lazy-learning
- condensed-nearest-neighbors
- credit-card-fraud
timestamp: '2025-10-19'
---

This session delves into the final regularisation and tuning mechanisms for decision trees, followed by an in-depth treatment of the K-Nearest Neighbors (KNN) algorithm. Moving from the foundations of decision trees, the instructor explains how Ross Quinlan addressed the mathematical bias of Information Gain toward high-cardinality splits (such as a unique Customer ID) by introducing the Gain Ratio in C4.5 and C5.0. This metric normalises Information Gain by dividing it by the attribute's internal Information Content ($H(A) = -\sum p_i \log_2 p_i$). This approach is contrasted with Leo Breiman's Classification and Regression Trees (CART) algorithm, which relies on the Gini Index ($1 - \sum p_i^2$) and enforces binary splits. The session highlights the "greedy" nature of decision tree construction, noting that while highly inexpensive and fast, it can trap models in local minima and lead to high-variance overfitting. To counteract this, two primary forms of regularisation are explored: pre-pruning (early stopping using hyperparameters like maximum tree depth, minimum instances per node, or information gain thresholds) and post-pruning (specifically Cost-Complexity Pruning, where the tree is penalised using $J(T, S) = \text{TrainingErrorRate}(T, S) + \alpha |T|$).

The second half of the lecture details K-Nearest Neighbors (KNN), introducing it as a non-parametric, instance-based "lazy learner." Because KNN builds no global model during training (acting as a "model-free" method), it defers all mathematical calculations to prediction time, where it computes local approximations based on distance. The instructor details Euclidean distance ($D = \sqrt{\sum (x_i - y_i)^2}$) and demonstrates why feature scaling—either via Min-Max Normalisation ($\frac{x - x_{min}}{x_{max} - x_{min}}$) or Z-score Standardization ($\frac{x - \mu}{\sigma}$)—is a non-negotiable step to prevent features with larger scales from dominating the distance calculations. The lecture addresses critical limitations of KNN, including the "curse of dimensionality," where an exponential increase in feature dimensions makes data points highly sparse and equidistant, rendering distance metrics meaningless. To illustrate, covering 20% of a feature range requires 20% of the training data in 1D, 45% in 2D ($0.45^2 \approx 0.2$), and 59% in 3D ($0.59^3 \approx 0.2$). Solutions such as Wilson Editing (Edited Nearest Neighbors) to remove class outliers and Hart's Condensed Nearest Neighbors (CNN) algorithm to filter training datasets down to essential "prototypes" are examined as methods to control overfitting and reduce computational and storage complexity.

The session concludes with a real-world European credit card fraud detection case study. Operating on a highly imbalanced dataset (284,807 transactions, with only 492 frauds or 0.17%), the class walks through data preprocessing—incorporating stratified splits and PCA-transformed variables—and utilizes KNN ($K=3$) to achieve a 91.01% Precision, 82.65% Recall, and an Area Under the ROC Curve (AUC) of 93%. Finally, the instructor explores modern hybrid architectures that merge traditional machine learning with Generative AI. By transforming complex text (such as support tickets or patient medical histories) into high-dimensional vector embeddings, organizations can perform rapid KNN searches in vector databases to retrieve nearest-neighbor historical context, cost-effectively grounding Large Language Models (LLMs) and significantly minimizing hallucinations.

# Key Concepts
- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — Decision trees and K-Nearest Neighbors represent core non-linear algorithms used for classification and regression, relying on axis-parallel partitioning and local instance calculations respectively.
- **[Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md)** — The critical tension in ML where unregularised decision trees and very low values of $K$ in KNN overfit (low bias, high variance), while heavily pruned trees or very high values of $K$ underfit (high bias, low variance).
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)** — Crucial frameworks for tuning hyperparameters, such as using K-fold cross-validation to find the optimal complexity parameter $\alpha$ for cost-complexity pruning or the optimal neighbor count $K$ in KNN.
- **[Explainable AI (XAI)](../concepts/explainable-ai.md)** — Shallow decision trees provide highly transparent, rule-based systems that are easy to interpret, whereas deep trees or instance-based models like KNN act as black boxes with lower direct interpretability.
- **[Dimensionality Reduction and Feature Extraction](../concepts/dimensionality-reduction.md)** — The process of pruning features or projecting them (e.g., via PCA) to combat the curse of dimensionality, which degrades the distance calculations central to KNN.
- **[Embeddings and Vector Representations](../concepts/embeddings-and-representations.md)** — High-dimensional continuous vectors that represent discrete text tokens, used in modern systems alongside KNN semantic search to fetch relevant context files for LLMs.

# Topics Covered
- **Decision Tree Splits & Metrics**:
  - Quinlan's ID3 (Information Gain) vs. C4.5/C5.0 (Gain Ratio).
  - Normalising Information Gain using Information Content: $H(A) = -\sum_{i} p_i \log_2 p_i$.
  - Wordle analytics analogy: How information content measures bits of information gained.
  - Breiman's CART algorithm: Binary splitting using Gini Index ($\text{Gini} = 1 - \sum p_i^2$).
  - Regression Trees: Node splitting based on weighted variance reduction.
- **Tree Regularisation & Overfitting Mitigation**:
  - The greedy nature of axis-parallel splits and local minima trapping.
  - Pre-pruning (early stopping) parameters: maximum tree depth, minimum instances per node, and minimal gain threshold.
  - Post-pruning (Cost-Complexity Pruning): generalisation error minimisation using the formula $J(T, S) = \text{TrainingErrorRate}(T, S) + \alpha |T|$.
- **K-Nearest Neighbors (KNN) Mechanics**:
  - Lazy (instance-based/model-free) vs. Eager (model-based) learning paradigms.
  - Euclidean distance math: $D = \sqrt{\sum (x_i - y_i)^2}$ (L2 Norm) vs. Manhattan distance (L1 Norm).
  - The non-negotiable step of normalization (Min-Max) and standardization (Z-score) to resolve scale sensitivity.
  - Impact of adding/removing features on nearest neighbor boundaries.
- **KNN Challenges & Advanced Refinements**:
  - Resolving ties: odd $K$ configurations and Distance-Weighted KNN ($weight \propto \frac{1}{d^2}$).
  - Mitigating the Curse of Dimensionality: mathematical expansion of sparse feature space.
  - Wilson Editing (Edited Nearest Neighbors): smoothing boundaries by removing class outliers.
  - Data reduction using Hart's Condensed Nearest Neighbors (CNN): classifying dataset $X$ sequentially to extract a representative prototype set $U$ and eliminate absorbed points.
- **Credit Card Fraud Detection Case Study**:
  - Applying KNN to imbalanced European credit card transaction data (284,807 points, 0.17% fraud).
  - Stratified 80/20 train-test split, Z-score standardization, and testing values of $K$ from 3 to 30.
  - Achieving 91.01% Precision, 82.65% Recall, and 93% AUC using $K=3$.
- **Hybrid AI Systems**:
  - Coupling KNN vector databases with Large Language Models (LLMs) to construct low-cost, fact-grounded semantic search and RAG architectures.

# Materials
- **Slides**: `20251019_DecisionTrees-KNN.pdf` (Entropy, Gain Ratio, CART, Gini index, Pruning parameters, KNN issues, and Hart's CNN algorithm)
- **Chat**: Present (student discussions on Diwali, assignment completions, and bridge-building between technical teams and business leaders)
- **Video Recording**: [YouTube link (Vc9XApUUn88)](https://www.youtube.com/watch?v=Vc9XApUUn88)

# Related
- Sibling session: [Session 09: Decision Trees Foundations](c2-foundations-ml-ai-session-09.md)
- Sibling session: [Session 11: Clustering Foundations](c2-foundations-ml-ai-session-11.md)
- Parent course: [Foundations ML AI](../courses/c2-foundations-ml-ai.md)
- Next courses: [AI Project Design](../courses/c5-ai-project-design.md), [Responsible AI](../courses/c6-responsible-ai.md)

# Citations
1. Dr. Sridhar Pappu. (2025). *Session 10: Decision Tree Regularization and K-Nearest Neighbors*. Foundations ML AI. https://www.youtube.com/watch?v=Vc9XApUUn88.
2. Quinlan, J. R. (1993). *C4.5: Programs for Machine Learning*. Morgan Kaufmann Publishers.
3. Breiman, L., Friedman, J. H., Olshen, R. A., & Stone, C. J. (1984). *Classification and Regression Trees*. Wadsworth & Brooks.
4. Hart, P. (1968). The condensed nearest neighbor rule. *IEEE Transactions on Information Theory*, 14(3), 515-516.
5. Wilson, D. L. (1972). Asymptotic properties of nearest neighbor rules using edited data. *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-2(3), 408-421.
