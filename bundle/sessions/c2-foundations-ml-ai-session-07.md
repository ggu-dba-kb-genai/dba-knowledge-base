---
type: Session
resource: https://www.youtube.com/watch?v=MrsQVsTNIbM
title: 'Session 07: Logistic Regression & Classification Metrics'
description: An in-depth exploration of logistic regression as a binary classification
  algorithm, the mathematical concept of odds, and a comprehensive breakdown of evaluation
  metrics like the confusion matrix and ROC-AUC.
tags:
- logistic-regression
- classification
- confusion-matrix
- precision-recall
- roc-auc
- evaluation-metrics
timestamp: '2025-10-11'
---

The session transitions the course from regression models to classification frameworks, exploring **logistic regression** as the foundational binary classification algorithm within [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md). The instructor, Dr. Sridhar Pappu, recaps linear regression and explains why its direct application to classification tasks fails. Specifically, linear regression's output spans from $-\infty$ to $+\infty$, which cannot represent probabilities, and its decision boundaries are highly susceptible to shifting under extreme outliers (influential observations). To address these issues, the S-shaped sigmoid (or logistic) function is introduced to constrain outputs between $0$ and $1$, yielding a conditional probability. To linearize the model, the concepts of **odds** ($\frac{P}{1-P}$) and **log of odds (logit)** are introduced, allowing a linear combination of predictors to map directly to the log-odds of a class.

The practical applications of logistic regression are explored through three distinct datasets. First, the **Auto Club Flyer Response** case study demonstrates prediction using a single independent variable (Age), leading to the logit equation $\ln S = -20.40782 + 0.42592 \times Age$. Setting $\ln S = 0$ identifies a critical threshold age of $47.9$ years old, above which members are classified as likely to respond. Second, the **`mtcars` Automatic/Manual Transmission** dataset uses weight ($wt$) and horsepower ($hp$) to build the fit equation $\ln S = 18.8663 - 8.080348 \times wt + 0.03636 \times hp$. For a vehicle weighing 2,800 lbs with 120 hp, this resolves to a $64.7\%$ probability of manual transmission. Third, the **Framingham Heart Study** dataset (4,240 observations, 15 predictors) introduces clinical predictive modeling. Dr. Pappu highlights data transformations (logarithmic scales) and interaction terms (e.g., combining smoking status and age via multiplication) to model 10-year risk of cardiovascular disease. The case emphasizes identifying controllable, actionable risk factors (such as smoking, total cholesterol, blood pressure, and glucose) versus non-actionable risk factors (such as age and gender).

The second half of the lecture details [Model Evaluation and Validation](../concepts/model-evaluation-validation.md) through the **confusion matrix**. The instructor underscores that accuracy is a highly deceptive metric for imbalanced datasets (such as the 15% positive rate in the Framingham cohort), as a naive model predicting only the majority class can yield deceptively high accuracy while missing all actual positive cases. Consequently, the class dissects domain-specific performance trade-offs among **Recall (Sensitivity)**, **Precision**, and the **$F_1$-score** (harmonic mean). Recall is prioritized in clinical settings (like coronary disease risk) to minimize life-threatening false negatives. Precision is highlighted in spam filtering to avoid blocking important communications (such as one-time passwords). The $F_1$-score is used when both types of operational errors carry equal weight, such as flight delay predictions. The lecture concludes with a walkthrough of the **Receiver Operating Characteristic (ROC)** curve and **Area Under the Curve (AUC)** metrics. Dr. Pappu demonstrates how plotting varying decision thresholds yields an ROC curve, with a rule of thumb classifying an AUC of $0.70 - 0.80$ as fair, and how the "elbow" method is used to determine the optimal threshold, paving the way for future discussions on the [Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md).

# Key Concepts

- **Logistic (Sigmoid) Function** — The S-shaped mathematical function ($P = \frac{1}{1 + e^{-y}}$) used to constrain model outputs between $0$ and $1$, mapping predictors to conditional probabilities.
- **Odds and Logit (Log of Odds)** — Odds represent the ratio of success probability to failure probability ($\frac{P}{1-P}$). Taking the natural log of the odds yields the logit ($\ln S = \beta_0 + \beta_1 x_1 + \dots$), which restores a linear relationship with independent variables and enables [Explainable AI (XAI)](../concepts/explainable-ai.md) through coefficient interpretation.
- **Confusion Matrix** — A structural $2 \times 2$ grid mapping actual vs. predicted outcomes to identify True Positives, True Negatives, False Positives, and False Negatives, forming the foundational tool for [Model Evaluation and Validation](../concepts/model-evaluation-validation.md).
- **Recall (Sensitivity)** — The fraction of actual positive cases correctly identified by the model ($\frac{TP}{TP + FN}$). Highly critical in healthcare domains where false negatives represent severe risk.
- **Precision** — The fraction of predicted positive cases that are truly positive ($\frac{TP}{TP + FP}$). Highly critical in applications like spam filtering, where false positives (e.g., blocking legitimate one-time passwords) degrade user experience.
- **$F_1$-Score** — The harmonic mean of precision and recall ($2 \times \frac{Precision \times Recall}{Precision + Recall}$), acting as a balanced evaluation metric when both false positives and false negatives carry equal operational weight.
- **ROC-AUC** — The Receiver Operating Characteristic curve plots the True Positive Rate against the False Positive Rate across all threshold values, while the Area Under the Curve (AUC) measures the model's overall discriminative capacity.
- **Data Transformation & Interaction Terms** — Enhancements to the linear predictor portion of logistic regression, using log transformations (e.g., total cholesterol) and interaction terms (e.g., combining age and smoking status via multiplication) to capture complex, non-linear biological patterns.

# Topics Covered

- **Limitations of Linear Regression in Classification**: Boundless prediction ranges ($[-\infty, \infty]$) and sensitivity of decision boundaries to outliers (influential observations).
- **Mathematics of Logistic Regression**: Derivation of the S-shaped sigmoid function, definition of Odds ($\frac{p}{1-p}$), and conversion of non-linear probability to linear log-odds (logit).
- **Interpretation of Python/R Outputs**: Reading coefficients, calculating conditional probabilities, and examining Log-Likelihood Ratio (LLR) and p-values for model significance.
- **Auto Club Flyer Response Case Study**: Calculating log-odds and finding the critical threshold age boundary of $47.9$ years old.
- **`mtcars` Transmission Case Study**: Modeling automatic vs. manual transmission using weight and horsepower; setting the boundary line $18.8663 - 8.080348 \times wt + 0.03636 \times hp = 0$.
- **Framingham Heart Study Analysis**: Demographics and clinical features of 4,240 participants, stratified 70/30 splits to manage 15% class imbalance, data transformations, and identifying actionable medical markers.
- **Deceptive Nature of Accuracy**: Demonstrating why accuracy fails as a key metric on imbalanced datasets through imbalanced classification scenarios.
- **Confusion Matrix Unpacked**: Standard formulas and business trade-offs of Precision, Recall, Specificity, and $F_1$-score across spam filtering, healthcare, and aviation delay management.
- **ROC-AUC and Threshold Selection**: Understanding the Receiver Operating Characteristics curve, rule of thumb for AUC values ($0.70-0.80$ is fair), and utilizing the "elbow" method for finding optimal decision thresholds.
- **Transition to Future Topics**: Brief introduction of the [Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md) in machine learning.

# Materials

- **Slides**: `20251011_LogisticRegression_ClassificationMetrics.pdf` (Introduction to Classification with Logistic Regression; Classification Metrics)
- **Chat Log**: Discussion and live interactions are present in the classroom logs.
- **Video Recording**: YouTube recording available at `https://www.youtube.com/watch?v=MrsQVsTNIbM` (C2 Session 07).

# Related

- Part of [Foundations of ML and AI](../courses/c2-foundations-ml-ai.md)
- Previous Session: [Session 06](c2-foundations-ml-ai-session-06.md)
- Next Session: [Session 08](c2-foundations-ml-ai-session-08.md)

# Citations

1. Lecture Recording: `https://www.youtube.com/watch?v=MrsQVsTNIbM`
2. Framingham Heart Study: Historically initiated in 1948 in Framingham, Massachusetts. [Framingham Heart Study Official Site](https://www.framinghamheartstudy.org/)
3. Motor Trend Car Road Tests (`mtcars` dataset): Henderson and Velleman (1981), Building Multiple Regression Models Interactively. *Biometrics*, 37, 391–411.
