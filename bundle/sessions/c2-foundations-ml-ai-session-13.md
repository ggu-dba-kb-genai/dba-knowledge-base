---
type: Session
resource: https://www.youtube.com/watch?v=f22btBYvTX8
title: 'Session 13: Clustering Algorithms & Ensemble Methods'
description: This session covers partitional (K-Means) and hierarchical clustering,
  cluster quality evaluation via silhouette coefficients, and introduces ensemble
  learning techniques including bagging, boosting, and Random Forests.
tags:
- clustering
- k-means
- hierarchical-clustering
- ensemble-methods
- bagging
- boosting
- random-forest
- adaboost
- xgboost
- silhouette-coefficient
timestamp: '2025-11-01T00:00:00Z'
date: '2025-11-01'
---

The lecture, delivered by Dr. Sridhar Pappu on November 1, 2025, transitions the class from unsupervised association rules and distance metrics to advanced clustering techniques and the foundations of ensemble learning. Dr. Pappu begins with a review of distance metrics (Euclidean, Manhattan, Hamming, Jaccard, Dice, Gower) and then dives deep into the partitional clustering algorithm **K-Means**, detailing its iterative execution, its convergence criteria based on minimizing the Sum of Squared Errors (SSE), and its limitations. To address outliers and categorical data, Dr. Pappu highlights robust variants including **K-Medians** (using Manhattan distance) and **K-Modes** (using Simple Matching Distance). The lecture then explores **Agglomerative Hierarchical Clustering (AHC)**, a bottom-up distance-based technique visualized through dendrograms, contrasting its four primary cluster proximity measures: Single Link (MIN), Complete Link (MAX), Group Average, and Ward's Method. An illustrative numeric walkthrough using a 9-city US distance matrix simulates the progressive merging of cities like Boston, New York, and Washington DC.

To quantify clustering quality, Dr. Pappu introduces internal evaluation metrics, highlighting cluster cohesion and separation, which are combined into the **Silhouette Coefficient** (ranging from $-1$ to $+1$). He also outlines cluster stability testing via repeated bootstrap subsampling. Moving back to supervised learning, the session introduces **Ensemble Methods**—namely **Bagging (Bootstrap Aggregating)** and **Boosting**. Bagging, exemplified by **Random Forests**, uses parallel, decorrelated, unpruned decision trees trained on bootstrap samples with randomized feature subsets at each split to mitigate the [bias-variance tradeoff](../concepts/bias-variance-tradeoff.md) by targeting high variance. Boosting, illustrated by **AdaBoost**, operates sequentially to minimize high bias by training weak learners (e.g., decision stumps) and dynamically re-weighting misclassified instances. Dr. Pappu wraps up with feature importance metrics (Mean Decrease in Impurity and Mean Decrease in Accuracy) and offers a forward-looking preview of neural networks and deep learning.

An engaging highlight of the session is an interactive demonstration by student Sanjay Gupta, who displays a custom HTML/JavaScript animation of K-Means and AHC algorithms built using Claude. This prompts a lively discussion on the evolving landscape of AI-assisted engineering, the use of agentic orchestration (e.g., GitHub Copilot, VS Code Agent mode), and the importance of maintaining analytical thinking rather than fully outsourcing cognitive tasks to generative models.

# Key Concepts

- **K-Means Clustering** — A partitional, distance-based algorithm that assigns data points to $K$ clusters by iteratively assigning points to the closest randomly initialized centroids, recomputing the centroids as cluster means, and repeating until convergence (i.e., minimal reassignment or minimal change in the Sum of Squared Error, SSE).
- **Agglomerative Hierarchical Clustering (AHC)** — A bottom-up clustering algorithm that begins with each data point as a singleton cluster and iteratively merges the two closest clusters based on a distance matrix. Proximity metrics between clusters include:
  - **Single Link (MIN)** — Measures the minimum distance between points in different clusters. It is capable of handling non-elliptical shapes but is sensitive to noise and outliers.
  - **Complete Link (MAX or CLIQUE)** — Measures the maximum distance between points in different clusters, favoring globular shapes and offering robustness to outliers.
  - **Group Average** — Computes the average pairwise distance between all points in different clusters.
  - **Ward's Method** — Defines proximity based on the increase in the squared error when two clusters are merged, mirroring the K-Means objective function.
- **Silhouette Coefficient** — A model-agnostic internal clustering validation metric that combines cohesion ($a_i$, average distance to other points in the same cluster) and separation ($b_i$, average distance to the nearest neighboring cluster) for each point $i$ using the formula:
  $$s_i = \frac{b_i - a_i}{\max(a_i, b_i)}$$
  The metric ranges from $-1$ to $+1$, where values near $+1$ represent strong cohesion, values near $0$ represent cluster boundary placement, and negative values indicate potential misclustering. This serves as a vital component in [Model Evaluation and Validation](../concepts/model-evaluation-validation.md).
- **Bagging (Bootstrap Aggregating)** — A parallel ensemble method in [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md) designed to reduce variance by training independent base classifiers (like unpruned decision trees) on bootstrap samples (drawn with replacement) and aggregating their predictions via majority voting (classification) or averaging (regression).
- **Random Forest** — An extension of bagging that decorrelates individual trees by randomly selecting a subset of $p$ features at each node split (where $p \approx \sqrt{m}$ for classification or $p \approx m/3$ for regression, from a total of $m$ features), mitigating the [bias-variance tradeoff](../concepts/bias-variance-tradeoff.md) by averaging out highly unstable individual trees.
- **Boosting** — A sequential ensemble technique in [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md) that targets high bias by iteratively training weak learners (such as decision stumps—decision trees split at only one node) and adjusting sample weights dynamically. AdaBoost re-weights misclassified instances exponentially, whereas Gradient Boosting models (e.g., XGBoost, LightGBM, CatBoost) optimize loss gradients sequentially.
- **Feature Importance & Explainability** — Since ensembles sacrifice raw interpretability, methods like Mean Decrease in Impurity (MDI, Gini/entropy reduction per feature split) and Mean Decrease in Accuracy (MDA / Permutation Importance, measuring validation accuracy drop when a feature is shuffled) are leveraged to achieve post-hoc [Explainable AI (XAI)](../concepts/explainable-ai.md).
- **Deep Learning Foundations** — An introduction to [Neural Network Architectures](../concepts/neural-network-architectures.md) mapping a forward pass (stacking millions of linear regressions $W^T X + b$ with non-linear activation functions like Sigmoid or ReLU) and backpropagation (using error gradients to update weight vectors in reverse), which form the backbone of advanced [Computer Vision](../concepts/computer-vision.md).

# Topics Covered

- **Clustering Foundations & K-Means Mechanics**:
  - Partitional clustering setup and centroid-based partitioning.
  - Iterative update cycle: random seed initialization, assignment to closest centroids, centroid recomputation, and convergence.
  - Convergence stopping criteria: zero/minimum reassignment, centroid stabilization, or minimum decrease in Sum of Squared Error (SSE):
    $$SSE = \sum_{k=1}^K \sum_{\mathbf{x} \in C_k} dist(\mathbf{c}_k, \mathbf{x})^2$$
  - Addressing K-Means limitations: tuning $K$ via the Elbow (Scree) Plot, mitigating outliers using **K-Medians** with Manhattan distance and Sum of Absolute Errors (SAE):
    $$SAE = \sum_{k=1}^K \sum_{\mathbf{x} \in C_k} dist(\mathbf{x}, \mathbf{median}_k)$$
    and clustering categorical data using **K-Modes** with Simple Matching Distance.
- **Agglomerative Hierarchical Clustering (AHC)**:
  - Bottom-up nested clustering algorithm, progressing from $N$ singleton clusters to a single comprehensive cluster.
  - Utilizing dendrograms to visualize merge heights and slicing them to determine final cluster counts.
  - Proximity metrics (Single Link, Complete Link, Group Average, Ward's Method).
  - Numeric simulation of AHC on a 9-city US distance matrix (BOS, NY, DC, MIA, CHI, SEA, SF, LA, DEN) using the Single Link (MIN) criterion.
- **Cluster Quality Evaluation**:
  - Mathematical definitions of Cohesion and Separation.
  - Calculating, interpreting, and averaging Silhouette Coefficients.
  - Evaluating cluster stability using repeated random bootstrap subsampling.
- **Ensemble Learning Paradigms**:
  - Core philosophy: Combining multiple weak classifiers/regressors to reduce variance (Bagging) or bias (Boosting).
  - Bootstrap sampling mechanics (sampling with replacement, out-of-bag validation).
  - **AdaBoost** mathematical workflow: equal weight initialization $w_i = \frac{1}{n}$, training a weak learner (decision stump), computing weighted error $\epsilon_t$, calculating learner weight $\alpha_t = \frac{1}{2} \ln \left(\frac{1 - \epsilon_t}{\epsilon_t}\right)$, exponentially updating instance weights ($w_i \leftarrow w_i \exp(\alpha_t)$ if misclassified, $w_i \leftarrow w_i \exp(-\alpha_t)$ if correct), normalizing weights, and final sign-based voting.
  - Gradient boosting variants: LightGBM, XGBoost, and CatBoost.
  - **Random Forest** construction: unpruned decision trees, random feature subsets ($p < m$), majority voting, and feature importance (MDI and Permutation Importance).
  - Python-based hyperparameter tuning using Grid Search with 10-fold cross validation.
- **Interactive Student Demo & AI Engineering Discussion**:
  - Showcase of Sanjay Gupta's student-developed HTML/JS interactive clustering animation constructed using Claude.
  - Classroom exchange on agentic orchestration (GitHub Copilot, VS Code Agent mode, Claude) and the critical need for engineers to maintain analytical reasoning instead of over-relying on automated generation.
  - Assignment logistics: Deadline discussion with GGU grades due December 5, 2025.
- **Deep Learning Preview**:
  - Stacking millions of linear regressions with non-linear activation functions (ReLU: if $>0$ keep, if $<0$ make $0$; Sigmoid).
  - Hierarchical feature learning from low-level edges to high-level facial features (eyes, nose, ears).
  - Forward and backward passes (backpropagation) to find optimal weights.

# Materials

- **Slides**:
  - `Session 13 - (01 Nov 2025).pdf`
  - `Session13_Slides_2025-11-01.pdf`
- **Video Recording**: [YouTube f22btBYvTX8](https://youtube.com/watch?v=f22btBYvTX8)
- **Chat**: Present and active, featuring a student-built HTML interactive animation of K-Means and Agglomerative Hierarchical clustering utilizing Claude.

# Related

- Part of the [Foundations ML AI](../courses/c2-foundations-ml-ai.md) course.
- Preceded by [Session 12](c2-foundations-ml-ai-session-12.md).
- Followed by [Session 14](c2-foundations-ml-ai-session-14.md).

# Citations

1. Foundations ML AI, Session 13 lecture video (`https://www.youtube.com/watch?v=f22btBYvTX8`).
2. Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5-32.
3. Freund, Y., & Schapire, R. E. (1997). A decision-theoretic generalization of on-line learning and an application to boosting. *Journal of Computer and System Sciences*, 55(1), 119-139.
