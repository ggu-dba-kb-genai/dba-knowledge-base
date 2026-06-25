---
type: Session
resource: https://www.youtube.com/watch?v=F9omQ_TmI4w
title: 'Session 15: Time Series Forecasting & Course Wrap-Up'
description: An in-depth exploration of time series forecasting techniques including
  regression-on-time, smoothing methods, and the ARIMA family, combined with a comprehensive
  course wrap-up.
tags:
- time-series
- forecasting
- regression-on-time
- arima
- exponential-smoothing
- model-validation
- machine-learning-workflow
timestamp: '2025-11-08'
---

This session serves as the final lecture of the [Foundations of ML and AI](../courses/c2-foundations-ml-ai.md) course, shifting focus to the domain of [time series forecasting](../concepts/time-series-forecasting.md). The instructor, Dr. Sridhar Pappu, details how time series modeling reframes standard regression by using historical values of a target variable as its own predictors ($y_{t+1} = f(y_t, y_{t-1}, \dots)$). Through three distinct families of models—Regression on Time, Smoothing Methods, and Auto-Regressive Integrated Moving Average (ARIMA) models—the lecture illustrates how trend, seasonality, and random noise can be mathematically modeled to project future trends. Key industry metrics, such as Revenue Passenger Miles (RPM) for air carrier traffic, are introduced as primary case studies to demonstrate model application on real-world industry data spanning 17 years of training data (1996–2012) and 3 years of testing data (2013–2015).

Beyond simple regression baselines, the class covers decomposition methods utilizing additive and multiplicative seasonality adjustments depending on whether the amplitude of seasonal fluctuations is constant or proportional to the trend. It explores smoothing paradigms including Simple, Weighted, and Exponential Smoothing (such as Single Exponential Smoothing and the Holt-Winters framework). The session goes deep into the Box-Jenkins methodology for ARIMA/SARIMA model building, explaining crucial concepts like Autocorrelation Functions (ACF), lags, weak stationarity, and the roles of differencing and log-transformations to address heteroscedasticity.

The lecture concludes with a comprehensive review of the end-to-end machine learning pipeline, emphasizing the [bias-variance tradeoff](../concepts/bias-variance-tradeoff.md), [model evaluation](../concepts/model-evaluation-validation.md), and [explainable AI (XAI)](../concepts/explainable-ai.md). Additionally, the cohort discusses practical matters including academic and entrepreneurial pathways for their upcoming doctoral dissertations, and how statistical modeling, Monte Carlo simulations, and Fermi estimation can address business challenges such as predicting agile sprint velocities.

# Key Concepts

- **[Time Series and Forecasting](../concepts/time-series-forecasting.md)** — The core framework of analyzing sequential, time-dependent observations to identify patterns and predict future values.
- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — The foundational class of machine learning algorithms mapping input features to labeled targets, which maps to regression-on-time approaches where time is the predictor.
- **[Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md)** — The tension between underfitting and overfitting, highlighted during curve-fitting approaches like high-degree polynomial regression.
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)** — Protocols used to assess forecasting performance, illustrated using hold-out testing data (2013–2015 RPM data) evaluated via Mean Absolute Percentage Error (MAPE).
- **[Explainable AI (XAI)](../concepts/explainable-ai.md)** — The tradeoff between easily interpretable models (such as simple linear regression with seasonal dummies) and complex, high-accuracy statistical or neural network architectures.
- **Three Components of Time Series** — Trend (long-term upward or downward progression), Seasonality (periodic, predictable cycles over fixed intervals), and Random Noise (unpredictable, residual fluctuations).
- **Additive vs. Multiplicative Seasonality** — Additive seasonality models seasonal variations using constant absolute differences ($y - \hat{y}$), suitable for stable amplitudes. Multiplicative seasonality models variations as ratios ($y / \hat{y}$), suitable when the amplitude scales proportionally with the trend.
- **Exponential Smoothing (EMA / SES)** — A smoothing method that weights past values with exponentially decaying weights. Formulated as $\hat{y}_{t+1} = \hat{y}_t + \alpha(y_t - \hat{y}_t)$, where $\alpha \in [0, 1]$ acts as a hyperparameter. 
- **Naive / Random Walk Model** — A specific case of exponential smoothing where $\alpha = 1$, setting tomorrow's forecast equal to today's actual value ($y_{t+1} = y_t$). This model serves as a strong baseline in highly random domains like stock forecasting.
- **Stationarity** — A critical condition for ARIMA modeling where weak stationarity requires a constant mean, constant variance, and constant autocorrelation over time.
- **Differencing and Log Transformations** — Differencing ($y_t - y_{t-1}$) is a form of calculus used to stabilize a non-constant mean. Log transformations are applied to stabilize non-constant variance (heteroscedasticity).
- **ARIMA / SARIMA Models** — Statistical frameworks combining Auto-Regressive ($p$), Integrated ($d$), and Moving Average ($q$) parameters, extended with seasonal parameters $(P, D, Q)_m$ with a seasonal period $m$ (e.g., $m=12$ for monthly data).

# Topics Covered

- **Course Context & Time Series Fundamentals** — Positioning forecasting as the final block of the [Foundations of ML and AI](../courses/c2-foundations-ml-ai.md) curriculum.
- **Case Study: Revenue Passenger Miles (RPM)** — Modeling US air carrier traffic monthly data (Jan 1996 to Dec 2012) to forecast Jan 2013 to Dec 2015. Exploring real-world patterns in the data: summer peaks (July vacation seasonality), short-month drops (February), the 9/11 aviation shutdown (2001), and the Global Financial Crisis (2008).
- **Regression on Time (Curve Fitting)** — Creating time indices ($t$) and quadratic terms ($t^2$) for polynomial trend line modeling, and dummy-variable encoding ($Q1, Q2, Q3, Q4$ or Jan–Dec) to capture seasonality.
- **Classical Decomposition** — Implementing additive and multiplicative seasonal adjustments, calculating average historical seasonal errors, and applying seasonal multipliers to baseline regression predictions.
- **Smoothing Baselines** — Defining and computing Simple Moving Average (SMA), Weighted Moving Average (WMA), and Single Exponential Smoothing (SES).
- **Box-Jenkins ARIMA Methodology**:
  - Computing and plotting the Autocorrelation Function (ACF) to identify lags and signatures of trend, seasonality, and randomness.
  - Resolving non-stationarity via seasonal and non-seasonal differencing.
  - Resolving heteroscedasticity with log transformations (demonstrated using a Tractor Sales dataset).
  - Auto-ARIMA optimization and interpreting parameter outputs (e.g., explaining `SARIMA(3,0,0)(0,1,2)[12]`).
- **Forecasting Caveats & Over-reliance on Windowing** — Case study of US Housing Starts (1959–2007) illustrating how a 14-year sub-window (1991–2006) showed a misleading upward trend, while historical context indicated an imminent cyclical crash.
- **End-to-End Course Synthesis** — Consolidating the ML pipeline: business objectives, validation splits, class imbalance checks, preprocessing, feature engineering reference guides, and selecting appropriate models based on accuracy vs. interpretability.
- **Student Q&A & Research Pathways**:
  - Sprint velocity prediction on JIRA boards: discussing limitations of scope changes and utilizing Monte Carlo simulations or Fermi estimations for back-of-the-envelope modeling.
  - Doctoral dissertation guidelines: choosing between academic publication, executive books, or corporate business plans.

# Materials

- **Slides**: `TimeSeriesForecasting_Putting-it-all-together.pdf` (covering curve fitting, moving averages, exponential smoothing, and Box-Jenkins ARIMA modeling).
- **Chat**: Available and active throughout the interactive Q&A.
- **Video Recording**: YouTube link `https://www.youtube.com/watch?v=F9omQ_TmI4w` (duration: ~3 hours).

# Related

- **Parent Course**: [Foundations of ML and AI](../courses/c2-foundations-ml-ai.md)
- **Sibling Sessions**:
  - [Session 14: Neural Networks Introduction](c2-foundations-ml-ai-session-14.md)
- **Next Course**: [Deep Learning](../courses/c3-deep-learning.md)

# Citations

1. Session Recording: [Session 15: Time Series Forecasting & Course Wrap-Up](https://www.youtube.com/watch?v=F9omQ_TmI4w)
2. Rob J. Hyndman and George Athanasopoulos, *Forecasting: Principles and Practice*, OTexts (referenced as the primary textbook for auto-ARIMA algorithms and time series theory).
