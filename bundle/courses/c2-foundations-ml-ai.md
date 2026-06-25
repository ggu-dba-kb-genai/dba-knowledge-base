---
type: Course
resource: null
title: 'C2: Foundations of ML & AI'
description: A comprehensive technical foundation in classical machine learning and
  statistical modeling for executive decision-making.
tags:
- machine-learning
- supervised-learning
- unsupervised-learning
- linear-regression
- logistic-regression
- clustering
- time-series
- azure-ml
timestamp: '2025-09-20'
---

This course, **C2: Foundations of ML & AI**, serves as the core technical pillar of the Doctor of Business Administration (DBA) program. Designed specifically for working professionals and corporate executives, the course bridges the gap between raw statistical theory and strategic decision-making. The curriculum guides students through the transition from classical, expert-driven [Symbolic AI](../concepts/explainable-ai.md) rule-based systems to modern data-driven paradigms. It establishes a rigorous understanding of [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)—including linear and logistic regressions—alongside unsupervised patterns such as clustering and association rules, concluding with [Time Series and Forecasting](../concepts/time-series-forecasting.md).

Throughout the 15 sessions, students engage in both theoretical discussions and hands-on laboratory workshops. These labs utilize enterprise-grade business intelligence and cloud-native machine learning platforms, specifically Microsoft PowerBI and Azure Machine Learning Studio, to implement end-to-end data pipelines. Key themes emphasize managing the [Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md), validating model assumptions through detailed residuals and leverage diagnostics (such as Cook's Distance), and selecting appropriate [Model Evaluation and Validation](../concepts/model-evaluation-validation.md) metrics (like precision, recall, F1-score, and ROC/AUC) to align technological capabilities with high-stakes corporate strategic outcomes.

# Sessions

*   **[Session 01: Introduction to AI History, Symbolic AI, and Vibe Coding](../sessions/c2-foundations-ml-ai-session-01.md) (2025-09-20)** — Explores the evolution of AI from the 1956 Dartmouth Conference to modern LLM-driven "vibe coding," contrasting rule-based expert systems (e.g., MYCIN) with modern statistical learning.
*   **[Session 02: Supervised and Unsupervised Learning Foundations](../sessions/c2-foundations-ml-ai-session-02.md) (2025-09-21)** — Establishes core taxonomy including structured vs. unstructured data, classification vs. regression, and unsupervised pattern mining (association rules and clustering).
*   **[Session 03: Basic Statistics, Central Tendencies, and Measures of Variability](../sessions/c2-foundations-ml-ai-session-03.md) (2025-09-27)** — Covers the foundational statistics of machine learning, focusing on central tendencies (mean, median, mode), measures of spread (IQR, standard deviation), and z-score standardization.
*   **[Session 04: Hands-On Lab: Exploratory Data Analysis (EDA) with PowerBI](../sessions/c2-foundations-ml-ai-session-04.md) (2025-09-28)** — A hands-on laboratory utilizing PowerBI to inspect, clean, and visualize multi-variable car performance data to uncover hidden trends.
*   **[Session 05: Linear Regression, Correlation, and Residuals Analysis](../sessions/c2-foundations-ml-ai-session-05.md) (2025-10-04)** — Dives deep into simple and multiple linear regression, Pearson correlation ($R$), and the mathematical definition of $R^2$ and Adjusted $R^2$.
*   **[Session 06: Multi-dimensional Outliers, Leverage, and Cook's Distance](../sessions/c2-foundations-ml-ai-session-06.md) (2025-10-05)** — Investigates "check number four" of linear regression (testing model assumptions of linearity, homoscedasticity, and normal error distributions) and identifying influential outliers using Cook's Distance.
*   **[Session 07: Logistic Regression and Classification Performance Metrics](../sessions/c2-foundations-ml-ai-session-07.md) (2025-10-11)** — Covers binary classification using the logistic S-curve, the concept of odds and log-odds (logit), and model significance testing.
*   **[Session 08: Hands-On Lab: Building a Machine Learning Pipeline in Azure ML](../sessions/c2-foundations-ml-ai-session-08.md) (2025-10-12)** — A guided lab session establishing cloud-native machine learning workspaces, storage containers, and end-to-end regression pipelines in Azure ML Studio.
*   **[Session 09: Bias-Variance Tradeoff, Overfitting, and K-Fold Cross-Validation](../sessions/c2-foundations-ml-ai-session-09.md) (2025-10-18)** — Analyzes underfitting vs. overfitting, how model complexity influences training and testing errors, and how to tune models using K-fold cross-validation.
*   **[Session 10: Decision Trees and K-Nearest Neighbors (KNN)](../sessions/c2-foundations-ml-ai-session-10.md) (2025-10-19)** — Details recursive partitioning algorithms (ID3, C4.5, CART) using entropy, gain ratio, and Gini impurity, alongside non-parametric lazy learning with K-Nearest Neighbors (KNN).
*   **[Session 11: Hands-On Lab: Classification Algorithms in Azure ML](../sessions/c2-foundations-ml-ai-session-11.md) (2025-10-25)** — Hands-on deployment of classification models in Azure ML, highlighting data leakage, class imbalance handling via stratification, and data normalization.
*   **[Session 12: Unsupervised Learning: Association Rule Mining and Distance Metrics](../sessions/c2-foundations-ml-ai-session-12.md) (2025-10-26)** — Transitions to unsupervised techniques, covering market basket analysis via the Apriori algorithm (support, confidence, lift) and various distance metrics (Euclidean, Manhattan, Jaccard, Cosine similarity).
*   **[Session 13: K-Means, Hierarchical Clustering, and Ensemble Methods](../sessions/c2-foundations-ml-ai-session-13.md) (2025-11-01)** — Covers partitioning (K-Means) and agglomerative hierarchical clustering (single, complete, average linkage) evaluated using silhouette coefficients, plus an introduction to ensemble bagging and boosting.
*   **[Session 14: Hands-On Lab: Unsupervised Clustering Pipelines in Azure ML](../sessions/c2-foundations-ml-ai-session-14.md) (2025-11-02)** — A practical lab for constructing and evaluating unsupervised clustering pipelines, handling multi-dimensional outliers, and managing Azure ML compute resources.
*   **[Session 15: Time Series Analysis, Forecasting, and Program Wrap-Up](../sessions/c2-foundations-ml-ai-session-15.md) (2025-11-08)** — Explores forecasting techniques (regression on time, additive and multiplicative seasonality, exponential smoothing, and ARMA models) and wraps up the course with program-level connections.

# Assignments

- [Assignment 1: Linear Regression Modeling & Analysis](../assignments/c2-foundations-ml-ai-assignment-1.md) — Individual; build and interpret a linear regression model on self-generated data (50 marks).
- [Final Assignment: AI/ML Algorithm Playbook by Industry](../assignments/c2-foundations-ml-ai-final-assignment.md) — Group; map business problems to classical algorithms with KPIs, metrics, and validation (70% group / 30% individual).

# Citations

1. Provost, F., & Fawcett, T. (2013). *Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking*. O'Reilly Media.
2. James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning: with Applications in R*. Springer.
3. Hyndman, R. J., & Athanasopoulos, G. (2018). *Forecasting: Principles and Practice* (2nd ed.). OTexts.
4. Tan, P.-N., Steinbach, M., Karpatne, A., & Kumar, V. (2018). *Introduction to Data Mining* (2nd ed.). Pearson.
