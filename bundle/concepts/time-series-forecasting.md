---
type: Concept
title: Time Series and Forecasting
description: Statistical and deep learning models designed to analyze sequential,
  time-dependent observations to identify patterns and predict future values.
tags:
- time-series
- forecasting
- ARIMA
- exponential-smoothing
- recurrent-neural-networks
- LSTM
timestamp: '2026-01-04'
---

Time series forecasting is the science and methodology of analyzing sequential, time-dependent observations to identify underlying patterns—such as trend, seasonality, and randomness—and predict future values. Unlike cross-sectional snapshot data where observations are assumed to be independent and identically distributed (i.i.d.), time series data possesses a chronological order and an internal correlation structure (autocorrelation) that must be respected. Consequently, model validation cannot rely on random splits (e.g., standard 80/20 train/test splits); instead, it requires chronological validation (temporal splitting) to prevent data leakage and evaluate real-world out-of-sample performance accurately.

Within this program, time series forecasting is explored across a progression from classical statistical baselines (smoothing and regression on time) to advanced parametric models (ARIMA/SARIMA) and modern deep learning architectures (Recurrent Neural Networks and LSTMs) capable of capturing high-dimensional, nonlinear temporal dependencies.

# Core Sub-Concepts & Methodologies

## Time Series Components
A typical time series is decomposed into three distinct elements:
* **Trend:** The long-term upward, downward, or stationary movement in the level of the data (e.g., the steady growth of US air carrier traffic over decades).
* **Seasonality:** Periodic, recurring fluctuations occurring at regular intervals (e.g., drop in travel during February due to fewer calendar days, spikes during summer and holiday periods, or weekly reporting drops in health data due to weekend testing delays).
* **Randomness (Noise):** Unpredictable, irregular fluctuations. A fundamental goal in modeling is to avoid overfitting to this noise; the residuals of an optimal model must be completely random, exhibiting no remaining temporal patterns.

## Regression on Time
When a strong trend is present, multiple linear or polynomial regression can serve as a robust baseline:
* **Trend Modeling:** A synthetic independent variable $time = 1, 2, 3, \dots, T$ is created. To capture curvature, polynomial terms like $time^2$ can be introduced.
* **Seasonality via Dummy Variables:** Seasonal factors are handled by treating the seasonal periods (e.g., months or quarters) as categorical variables and creating $k-1$ dummy indicators (e.g., Q2, Q3, Q4 with Q1 as the reference).
* **Decomposition-based Seasonal Factors:** Instead of dummy variables, seasonal factors can be calculated by comparing actual values to the trend line ($y_{hat}$):
  * **Additive Seasonality:** Applied when the amplitude of seasonal peaks and troughs remains constant over time regardless of the trend level ($y = Trend + Seasonal + Residual$).
  * **Multiplicative Seasonality:** Applied when seasonal fluctuations scale proportionally with the overall trend level ($y = Trend \times Seasonal \times Residual$). The seasonal factors are averaged across matching historical periods (e.g., averaging all January deviations) and applied back to the trend forecast.

## Smoothing Techniques
When there is no clear trend or seasonality but significant noise, smoothing methods can provide stable short-term forecasts:
* **Simple Moving Average (SMA):** Computes a rolling average of the most recent $K$ observations, giving equal weight to each.
* **Weighted Moving Average (WMA):** Assigns weights that decrease linearly as observations go further into the past.
* **Exponential Smoothing (ETS):** Assigns exponentially decaying weights, prioritizing the most recent observations while utilizing the entire history. The forecasting formula updates dynamically:
  $$\hat{y}_{t+1} = \hat{y}_t + \alpha (y_t - \hat{y}_t)$$
  where $\alpha \in [0,1]$ is the smoothing parameter. Setting $\alpha = 1$ yields the **Naive / Random Walk Model**, where tomorrow's forecast is simply today's actual value—a standard baseline in highly unpredictable domains like financial markets.

## ARIMA & Box-Jenkins Methodology
For stationary time series (where mean, variance, and autocorrelation remain constant over time), the Box-Jenkins methodology provides a powerful modeling framework:
* **Differencing ($d$):** Non-seasonal differencing ($y_t - y_{t-1}$) and seasonal differencing ($y_t - y_{t-s}$) are applied to eliminate trend and seasonality, transforming non-stationary series into stationary ones. Log transformations are often used beforehand to stabilize non-constant variance (heteroscedasticity).
* **Autocorrelation Function (ACF) & Partial Autocorrelation Function (PACF):** Correlation plots of the series against its own lagged values, used to detect remaining patterns and identify the appropriate model orders.
* **Auto-Regressive (AR) Component ($p$):** Predicts values using a linear combination of its own past values.
* **Moving Average (MA) Component ($q$):** Predicts values using a linear combination of past forecast errors.
* **SARIMA (Seasonal ARIMA):** Adds seasonal terms $(P, D, Q)_M$ to handle periodic cycles of length $M$ (e.g., $M=12$ for monthly data).
* **AutoARIMA:** An algorithmic optimization process that automatically searches over combinations of $p, d, q, P, D, Q$ to minimize information criteria (such as AIC or BIC).

## Recurrent Neural Networks & LSTMs
When temporal relationships are highly nonlinear or rely on complex multi-variable (exogenous) inputs—such as weather forecasting with dozens of climate factors or hour-of-day bike rentals—deep learning sequence models are used:
* **Recurrent Neural Networks (RNNs):** Share a single set of weights across all time steps and feed back the hidden state of the previous step as an input to the current step, creating a dynamic "state representation" of the past. RNNs often struggle with vanishing or exploding gradients when training over long sequences.
* **Long Short-Term Memory (LSTM):** Solves the vanishing gradient problem by splitting sequence processing into parallel pathways: a long-term cell state ($C_t$) that flows through the sequence with minimal modification, and a short-term hidden state ($h_t$). LSTMs regulate this flow using three sigmoid-activated gates:
  * **Forget Gate ($f_t$):** Decides what information to discard from the long-term cell state.
  * **Input Gate ($i_t$):** Decides what new processed inputs to write into the cell state.
  * **Output Gate ($o_t$):** Decides what parts of the updated cell state should be output as the next hidden state.

# Where It Appears

* **Courses:**
  * [Foundations of Machine Learning and AI](../courses/c2-foundations-ml-ai.md) — Establishes the mathematical framework of time series decomposition, regression on time, exponential smoothing, and Box-Jenkins ARIMA/SARIMA models.
  * [Deep Learning](../courses/c3-deep-learning.md) — Explores sequential modeling, backpropagation through time, RNN architectures, and LSTM gated networks.
  * [AI Project Design](../courses/c5-ai-project-design.md) — Integrates forecasting models into enterprise workflows, balancing business constraints with accuracy and explainability requirements.

* **Sessions:**
  * [Session 15: Time Series Forecasting](../sessions/c2-foundations-ml-ai-session-15.md) — Classical forecasting methods, trend and seasonality decomposition, additive vs. multiplicative models, exponential smoothing, and SARIMA modeling on aviation and housing data.
  * [Session 13: Recurrent Neural Networks and LSTMs](../sessions/c3-deep-learning-session-13.md) — Transition from classical linear baselines to neural sequence networks, covering feedback states, gradient issues, and the structural design of LSTM gates.

# Citations
1. Hyndman, R.J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.). OTexts. (Free online reference resource cited in the curriculum).
2. Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). *Time Series Analysis: Forecasting and Control* (5th ed.). John Wiley & Sons. (Authoritative text on Box-Jenkins methodology).
3. Hochreiter, S., & Schmidhuber, J. (1997). Long Short-Term Memory. *Neural Computation*, 9(8), 1735-1780. (The foundational paper introducing LSTM networks).
