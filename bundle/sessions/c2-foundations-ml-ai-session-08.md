---
type: Session
resource: https://www.youtube.com/watch?v=HhmJ_2VHgG4
title: 'Session 08: End-to-End ML Pipeline in Azure Machine Learning Studio & Regression
  Foundations'
description: A hands-on workshop building a supervised machine learning pipeline in
  Azure ML Studio to predict automobile prices, accompanied by theory on regression,
  regularization, and classification.
tags:
- azure-ml
- linear-regression
- supervised-learning
- pipeline-design
- data-preprocessing
- bias-variance-tradeoff
- regularization
timestamp: '2025-10-12'
---

This session is a practical, hands-on workshop and theory lecture led by Dr. Raj, focusing on building an end-to-end machine learning pipeline using Azure Machine Learning Studio's Designer. Utilizing a low-code/no-code approach, students learn to drag and drop pre-built components to ingest data, cleanse it, train a linear regression model, and evaluate its performance. The primary hands-on lab centers on the pre-loaded **automobile price raw** dataset (consisting of 205 records and 26 features) to predict car prices. Students are guided through the creation of Azure resources (workspaces, resource groups, and compute clusters) and the complete pipeline lifecycle, ending with instructions to decommission resources to conserve student credits.

The workshop systematically walks through Exploratory Data Analysis (EDA) and data preprocessing in Azure. This includes selecting relevant columns and choosing to drop the `normalized losses` column because 20% of its data points (41 out of 205) are missing. Dr. Raj discusses strategies for handling missing values, explaining how numerical missing data is typically replaced with the mean or median, categorical missing data with the mode, and target variable missingness with row deletion. For the lab pipeline, students configure the `Clean Missing Data` module to remove any rows containing missing values (a valid approach when the missing ratio is under 5%). The final pipeline splits the cleaned dataset into a 70/30 training-to-testing ratio, trains a linear regression model targeting the case-sensitive `price` column, generates scored labels, and analyzes overall model performance.

The session's theoretical material bridges the gap between hands-on pipelines and fundamental ML optimization. It addresses the **[Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md)**—differentiating between underfitting (high bias, high training error) and overfitting (high variance, high generalization gap). To mitigate overfitting, Dr. Raj introduces regularization techniques: $L2$ (Ridge) regularization, which reduces coefficient magnitudes while retaining all variables, and $L1$ (Lasso) regularization, which drives irrelevant coefficients to absolute zero, aiding in feature selection. Additionally, the lecture introduces **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** for binary classification via Logistic Regression. Using datasets like *FlierResponse* and the *Framingham Heart Disease Study*, the class explores logistic functions, maximum likelihood estimation, and evaluation diagnostics including Confusion Matrices, Precision, Recall, Sensitivity, Specificity, F1-Score, and Receiver Operating Characteristic (ROC) curves with Area Under the Curve (AUC).

# Key Concepts

- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — Applied in two paradigms: predicting a continuous numerical target (`price`) using Linear Regression, and binary classification (predicting risk or choices) using Logistic Regression.
- **[Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md)** — The critical balance in machine learning between model simplicity (underfitting/high bias) and complexity (overfitting/high variance). The session outlines cross-validation and regularization to manage this tradeoff.
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)** — Implemented in Azure ML's `Evaluate Model` module using regression metrics like Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the Coefficient of Determination ($R^2$, achieving ~0.86 in the lab). For classification, it relies on Confusion Matrices, F1-score, and Area Under the ROC Curve (AUC).
- **Data Preprocessing & Imputation** — The systematic treatment of missing data. Continuous features are treated with mean/median values, and categorical features with the mode. High-missingness columns (like `normalized losses`) are dropped, while missing values in target columns demand row deletion.
- **L1 & L2 Regularization** — Optimization constraints added to cost functions to penalize model complexity. $L2$ (Ridge) penalizes squared weights to stabilize models under multi-collinearity, while $L1$ (Lasso) penalizes absolute weights to perform **[Dimensionality Reduction and Feature Extraction](../concepts/dimensionality-reduction.md)** by driving weights to zero.

# Topics Covered

- **Azure ML Studio Workspace and Resource Setup**: Navigating `portal.azure.com`, setting up Resource Groups, Workspaces, and allocating compute clusters (e.g., standard DS3 virtual machines with 4 cores, 14 GB RAM).
- **Azure ML Designer Canva**: Building low-code/no-code pipelines by dragging pre-built components for data loading, column selection, cleaning, splitting, training, and scoring.
- **Data Selection & Cleaning**:
  - Dropping `normalized losses` due to extreme missingness (~20%).
  - Utilizing the `Clean Missing Data` block to drop rows with missing values.
- **Dataset Splitting**: Allocating 70% of the data for training and 30% for testing using a random seed (e.g., 123) to guarantee reproducibility.
- **Linear Regression Model Training & Evaluation**:
  - Using Ordinary Least Squares (OLS) with the `Train Model` module, targeting the case-sensitive `price` column.
  - Generating prediction outputs as `scored labels` with the `Score Model` module.
  - Inspecting performance metrics in the `Evaluate Model` module: Mean Absolute Error (~$2,018), Root Mean Squared Error, and the Coefficient of Determination (~0.86).
- **Decommissioning Azure Resources**: Step-by-step instructions to delete resource groups inside the Azure Portal to avoid credit drain.
- **Bias-Variance Theory & Validation**:
  - Training, validation (72%/8%), and test (20%) splits.
  - K-fold Cross-Validation to evaluate standard deviation and mean of model errors.
  - Underfitting (high bias, high training error) vs. Overfitting (high variance, high generalization gap).
  - Regularization formulation:
    - **Ridge ($L2$ Norm)**: $J = \min_{\beta} \left[ \sum_{j=1}^{n} (y^{(j)} - \sum_{i=0}^m \beta_i x_i)^2 + \lambda \sum_{i=1}^m \beta_i^2 \right]$
    - **Lasso ($L1$ Norm)**: $J = \min_{\beta} \left[ \sum_{j=1}^{n} (y^{(j)} - \sum_{i=0}^m \beta_i x_i)^2 + \lambda \sum_{i=1}^m |\beta_i| \right]$
    - **Elastic Net**: $J_{EN} = \text{Loss} + \alpha L_1 + (1 - \alpha) L_2$ where $0 \le \alpha \le 1$.
- **Logistic Regression & Binary Classification**:
  - Logistic/sigmoid function mapping inputs to probabilities: $p = \frac{1}{1 + e^{-\mu}}$ where $\mu = \beta_0 + \beta_1 x$.
  - Maximum Likelihood Estimation (MLE) to minimize the negative log-likelihood function: $-\ln L = -\sum_{i=1}^{n} \left[ y_i \ln(\hat{y}_i) + (1-y_i) \ln(1-\hat{y}_i) \right]$.
  - Practical evaluation calculations:
    - *FlierResponse*: Logit equation $\ln(S) = -20.4078 + 0.4259 \times \text{Age}$. For a 50-year-old, $\ln(S) = 0.8872 \implies S = 2.4283 \implies p = \frac{S}{1+S} = 0.7083$ (positive response prediction).
    - *MTcars*: Dividing classification boundary ($\ln(S)=0$) is given by $\text{hp} = \frac{-18.8663}{0.03636} + \frac{8.080348}{0.03636} \times \text{wt}$.
  - Classification metrics: Precision, Recall (Sensitivity), Specificity, F1-Score, and Receiver Operating Characteristic (ROC) curves with Area Under the Curve (AUC).
  - Case study: 10-year heart attack risk prediction (*Framingham Heart Disease Study*) with 4,240 observations and 15 predictors.

# Materials

- **Slides**:
  - `Session_8_1_Bias-Variance-Tradeoff.pdf`
  - `Session_8_2_LogisticRegression.pdf`
- **Recording**: YouTube video `https://www.youtube.com/watch?v=HhmJ_2VHgG4`
- **Chat**: Student chat was present during this live workshop.

# Related

- Part of **[Foundations ML AI](../courses/c2-foundations-ml-ai.md)**
- Adjacent Sessions:
  - Previous: **[Session 07](c2-foundations-ml-ai-session-07.md)**
  - Next: **[Session 09](c2-foundations-ml-ai-session-09.md)**

# Citations

1. [Azure Machine Learning Session 08 Recording](https://www.youtube.com/watch?v=HhmJ_2VHgG4)
2. [Azure Machine Learning Designer Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/concept-designer)
