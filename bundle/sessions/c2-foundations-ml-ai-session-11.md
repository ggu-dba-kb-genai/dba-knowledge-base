---
type: Session
resource: https://www.youtube.com/watch?v=ogHKdZeb-XM
title: 'Session 11: Hands-on Classification Pipelines & Time Series Foundations'
description: A hands-on lab session building binary classification pipelines in Azure
  ML Designer, with reference to the prepared Time Series Forecasting lecture materials.
tags:
- classification
- azure-ml
- logistic-regression
- data-preprocessing
- stratified-split
- data-leakage
- confusion-matrix
- time-series
- arima
- exponential-smoothing
timestamp: '2025-10-25'
---

The session on October 25, 2025, serves a dual purpose in the course curriculum. In the live recorded portion, Dr. Srinivasa Varadharajan Lakshminarasimhan (Dr. Raj) conducts an intensive hands-on lab in **Azure Machine Learning Studio (ML Designer)**, guiding students through the process of building, executing, and evaluating a machine learning pipeline for binary classification. Utilizing the *Adult Census Income dataset*, the lab demonstrates data ingestion, feature selection, missing data handling, stratified train-test splitting, feature normalization, and model comparison. Two parallel pipeline branches are implemented—one incorporating the census final weight (`FNLWGT`) statistical feature and the other excluding it—to explore feature engineering impacts, decision thresholds, and performance evaluation.

Simultaneously, the session's prepared slide materials introduce the theoretical foundations of **[Time Series and Forecasting](../concepts/time-series-forecasting.md)**, bridging classical predictive modeling with chronological sequential analysis. The prepared slides detail structural decomposition (trend, seasonality, noise), stationarity transformations, time-based regression, and smoothing techniques (Simple, Weighted, and Exponential Moving Averages). Furthermore, the deck explores parametric forecasting architectures, specifically the identification of Autoregressive (AR) and Moving Average (MA) parameters using Autocorrelation (ACF) and Partial Autocorrelation (PACF) plots, leading to the construction of ARIMA, Seasonal ARIMA (SARIMA), and ARIMAX models.

# Key Concepts

- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — Mapping input features to a categorical binary target (`<=50K` or `>50K`) rather than predicting a continuous numeric value as in regression.
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)** — Evaluating predictions on a held-out test set (30% split) and examining the resulting confusion matrix, precision, recall, and F1-score.
- **Stratified Split** — A sampling method used to mitigate class imbalance. By designating `income` as the stratification key, both training and testing datasets retain the original 75:25 class distribution, preventing the model from becoming biased towards the majority class.
- **Data Leakage** — The risk of test set information leaking into the training phase. Normalizing data (such as calculating the mean and standard deviation for Z-score) *before* splitting results in leakage because the test set characteristics contribute to the training features' scale. Performing normalization post-split is the robust machine learning practice.
- **[Explainable AI (XAI)](../concepts/explainable-ai.md)** — Utilizing Azure ML's "Model Explanation" parameter within the Train Model component to understand feature weights and contributions to the target class predictions.
- **[AI Lifecycle and MLOps](../concepts/ai-lifecycle-and-mlops.md)** — Deploying a validated pipeline into production, exposing scoring models via API endpoints, and establishing external data ingestion pathways.
- **[Time Series and Forecasting](../concepts/time-series-forecasting.md)** — Statistical modeling of chronological sequential data to capture underlying trends, seasonal patterns, and irregular/random fluctuations.
- **Stationarity** — The condition where a time series has constant statistical properties (mean, variance, autocorrelation) over time, which is essential for accurate parametric forecasting.
- **ACF and PACF** — Diagnostic correlation plots used to identify model parameters: the Autocorrelation Function (ACF) identifies Moving Average $MA(q)$ orders, while the Partial Autocorrelation Function (PACF) identifies Autoregressive $AR(p)$ orders.

# Topics Covered

- **Azure ML Designer Pipeline Assembly** — Drag-and-drop orchestration connecting `Select Columns in Dataset`, `Clean Missing Data`, `Split Data`, `Normalize Data`, `Two-Class Logistic Regression`, `Train Model`, `Score Model`, and `Evaluate Model`.
- **Feature Selection & Redundancy** — Dropping redundant columns (such as `education` in favor of pre-encoded `education-num`), evaluating sparse numeric columns like `capital-gain` and `capital-loss`, and assessing whether to include the census final weight (`FNLWGT`) statistical feature.
- **Handling Missing Values** — Using listwise deletion ("Remove entire row") on columns with missing values (`workclass`, `occupation`, and `native-country`) when the overall missingness ratio falls under the critical threshold.
- **Z-Score Normalization** — Rescaling numeric variables (`age`, `education-num`, and `hours-per-week`) to a uniform range to eliminate magnitude dominance, ensuring features with larger scales do not disproportionately influence model coefficients.
- **Confusion Matrix Analysis** — Deconstructing True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN) using a default classification threshold of `0.5` to calculate Accuracy (~83%), Precision (~67%), Recall (~56.6%), and F1-score (~62%).
- **External Data Ingestion** — Step-by-step upload of custom CSV datasets to Azure ML from a local machine, configuring storage destinations (Azure Blob storage), and parsing schemas.
- **Time Series Foundations (Slides)**:
  - **Decomposition**: Splitting series into Trend ($T$), Seasonality ($S$), and Random component / Noise ($I$) using additive or multiplicative models.
  - **Smoothing Methods**: Simple Moving Average (SMA), Weighted Moving Average (WMA), and Exponential Weighted Moving Average (EMA/Exponential Smoothing).
  - **Model Architectures**: Parametric model building including $AR(p)$, $MA(q)$, $ARMA(p, q)$, $ARIMA(p, d, q)$, $SARIMA(p, d, q)(P, D, Q)_m$, and $ARIMAX$ (ARIMA with exogenous variables based on quasi-causality).
  - **Tractor Sales Case Study**: Applying log transformations and differencing to stabilize non-constant mean and variance (heteroscedasticity) before executing Auto ARIMA.

# Materials

- **Slides** — `Session_13_20251025_TimeSeries.pdf` (Focuses on Time Series Forecasting theory, formulas, and case study details).
- **Chat** — Present and active during the session (discussing Azure setup, credit usage, and pipeline configuration troubleshooting).
- **Recording** — [ogHKdZeb-XM](https://www.youtube.com/watch?v=ogHKdZeb-XM) (Hands-on classification lab and pipeline execution in Azure ML Studio).

# Related

- Parent Course: **[Foundations ML AI](../courses/c2-foundations-ml-ai.md)**
- Sibling Sessions:
  - **[Session 10](c2-foundations-ml-ai-session-10.md)** (Previous Session)
  - **[Session 12](c2-foundations-ml-ai-session-12.md)** (Next Session)

# Citations

1. [Azure Machine Learning Lab Session 11 Video](https://www.youtube.com/watch?v=ogHKdZeb-XM)
2. [Adult Census Income Dataset](https://archive.ics.uci.edu/dataset/2/adult) (UCI Machine Learning Repository)
3. [Azure Machine Learning Designer Documentation](https://learn.microsoft.com/en-us/azure/machine-learning/concept-designer)
