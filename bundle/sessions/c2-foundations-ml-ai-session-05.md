---
type: Session
resource: https://www.youtube.com/watch?v=-WB-j4R4Y7g
title: 'Session 05: Linear Regression, Model Evaluation, and Residual Diagnostics'
description: This session introduces the fundamentals of linear regression, exploring
  model evaluation metrics like R-squared, P-values, and model significance alongside
  a deep dive into residuals analysis for validating core assumptions.
tags:
- linear-regression
- r-squared
- p-values
- residuals-analysis
- homoscedasticity
- qq-plot
- statistics
- model-evaluation
timestamp: '2025-10-04'
---

This session provides a rigorous foundation in linear regression modeling, transitioning from basic descriptive statistics to a robust, four-step evaluation pipeline for parametric models. Dr. Sridhar Pappu emphasizes that while linear regression is mathematically straightforward, model builders must look far beyond R-squared ($R^2$) to avoid building invalid or spurious models. The lecture begins with a review of central tendency and dispersion, highlighting the outsized impact outliers can have on Pearson's correlation coefficient ($r$). Through a case study analyzing COVID-19 viral loads from nasal vs. throat swabs (from Leung et al., *Nature Medicine*, 2020), the instructor demonstrates how removing a single extreme outlier patient (Participant B10260) shifts the correlation from a promising positive $0.67$ down to a completely uncorrelated $-0.178$. This case study underscores the critical importance of performing exploratory data analysis and visualization (e.g., box plots and scatter plots) rather than blindly trusting numerical summaries.

The core of the lecture outlines a structured framework for model diagnostics. **Check 1** examines goodness of fit through $R^2$ and Adjusted $R^2$. The instructor explains the sum of squares framework ($SST = SSR + SSE$), demonstrating that Adjusted $R^2$ is necessary to penalize model complexity (the addition of non-significant variables) by incorporating degrees of freedom ($n - k - 1$). To illustrate the hazard of relying solely on R-squared, several spurious regression examples are analyzed, including a dataset showing that $85.2\%$ of global COVID-19 cases could be explained by Dr. Pappu's daily step count ($\text{Cases} = -5076223.9 + 9.3 \times \text{Steps}$). **Checks 2 and 3** leverage hypothesis testing to evaluate the significance of individual regression slopes ($\beta_i$) and the overall model. Under the null hypothesis ($H_0: \beta_i = 0$), a standard p-value threshold of $0.05$ is used to determine statistical significance, though Dr. Pappu highlights that domain expertise can—and should—override statistical tests when business experience justifies retaining a variable.

**Check 4** focuses on residuals analysis ($e_i = y_i - \hat{y}_i$), which is used to validate the four foundational assumptions of ordinary least squares (OLS) regression: linearity, independence of errors, homoscedasticity (constant error variance), and normality of error distribution. The instructor explains that while higher-dimensional datasets cannot be easily visualized, residuals can always be plotted in a two-dimensional space (Predicted Values $\hat{y}$ vs. Residuals $y - \hat{y}$) to diagnose violations of OLS assumptions. A case study utilizing stopping distance data from the American Automobile Association (AAA) demonstrates the real-world safety implications of diagnostic failures: a simple linear model yields a high Adjusted $R^2$ of $87.3\%$, but exhibits visible non-linearity and heteroscedasticity in its residuals, leading to an unsafe underprediction of stopping distance at high speeds ($120\text{ feet}$ vs. $150\text{ feet}$ at $45\text{ mph}$). Applying a kinematics-based transformation ($\text{Speed} \propto \sqrt{\text{Distance}}$, derived from the physics equation $v^2 - u^2 = 2as$) corrects these violations, improving the Adjusted $R^2$ to $92.3\%$ and producing random, homoscedastic residual patterns.

# Key Concepts

- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — Ordinary least squares (OLS) linear regression represents the foundational parametric approach to predicting continuous numeric targets from one (simple) or more (multiple) independent variables.
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)** — Quantitative evaluation of regression goes beyond $R^2$ to require a four-step check: Adjusted $R^2$ penalization, coefficient p-values, overall significance F, and visual residuals analysis.
- **[Explainable AI (XAI)](../concepts/explainable-ai.md)** — The mathematically transparent formulation of linear regression coefficients provides intuitive slopes and directions, which allow domain experts to validate, interpret, or even override the model's parameters.
- **[Time Series and Forecasting](../concepts/time-series-forecasting.md)** — The assumption that residuals are independent is critical; when data is sequentially ordered (such as time-series datasets), autocorrelation often violates this assumption, requiring specialized forecasting methodologies instead of simple OLS.
- **[Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md)** — The mathematical tension of model capacity is discussed in the context of multi-variable regression: adding too many non-significant features artificially inflates $R^2$ (overfitting to noise) but degrades model generalization on unseen testing data.

# Topics Covered

- **AI Taxonomy & administrative notes**: Contextualizing traditional machine learning alongside symbolic AI, deep learning, and generative AI; clarification on assignments, grading flexibility, and strict final grading deadlines in GGU.
- **Pearson's Correlation Coefficient ($r$)**: Mathematical bounds ($-1$ to $+1$), strength, and direction; standard rule of thumb ($r \ge 0.7$ for reasonable correlation); dependency on domain standards (e.g., psychology vs. transaction data).
- **Goodness of Fit ($R^2$ vs. Adjusted $R^2$)**: The Sum of Squares mathematical identity ($SST = SSR + SSE$); how Adjusted $R^2$ scales with sample size ($n$) and variable count ($k$) to penalize useless features; the danger of spurious regressions.
- **Hypothesis Testing for Slopes (Check 2)**: Formulating the null hypothesis ($H_0: \beta_i = 0$); interpreting individual p-values against the default $0.05$ threshold; evaluating when to override statistics using clinical or business domain expertise.
- **Overall Model Significance (Check 3)**: Using Significance F (overall p-value) to evaluate the global null hypothesis ($H_0: \beta_1 = \beta_2 = \dots = \beta_k = 0$).
- **Residual Diagnostics (Check 4 - OLS Assumptions)**:
  - *Linearity*: Checking for curvature trends around the zero-residual line.
  - *Independence*: Visualizing sequence or spatial correlation (critical for time-ordered data).
  - *Homoscedasticity*: Ensuring constant variance of residuals across all predicted values ($\hat{y}$) to prevent heteroscedasticity (varying error variance).
  - *Normality*: Assessing the normal distribution of residuals via bell curves and Normal Q-Q (Quantile-Quantile) plots.
- **Data Transformations**: Applying non-linear transformations (such as square root of stopping distance derived from the kinematic equation $v^2 - u^2 = 2as$) to linearize physical relationships, resolve heteroscedasticity, and improve prediction accuracy.

# Materials

- **Slides**: `20251004_LinearRegression.pdf`
- **In-Class Chat**: Active discussion on interpreting negative intercepts, statistical vs. practical significance, and the logistical timeline of course grading.
- **Recording**: Video ID [-WB-j4R4Y7g](https://www.youtube.com/watch?v=-WB-j4R4Y7g) (accessible via `https://www.youtube.com/watch?v=-WB-j4R4Y7g`).

# Related

- Sibling Session: [Session 04](c2-foundations-ml-ai-session-04.md) (2025-09-28)
- Sibling Session: [Session 06](c2-foundations-ml-ai-session-06.md) (2025-10-05)
- Parent Course: [Foundations ML AI](../courses/c2-foundations-ml-ai.md)

# Citations

1. Lecture recording: `https://www.youtube.com/watch?v=-WB-j4R4Y7g` (Session 05 of Course 2: Foundations ML AI).
2. Leung, N.H.L., Chu, D.K.W., Shiu, E.Y.C. et al. "Respiratory virus shedding in exhaled breath and efficacy of face masks." *Nature Medicine* (2020). [https://doi.org/10.1038/s41591-020-0843-2](https://doi.org/10.1038/s41591-020-0843-2).
3. Spurious Correlations database, referenced for the science spending vs. suicide rates and breweries vs. math degrees examples.
4. Kinematic Equations of Motion ($v^2 - u^2 = 2as$), referenced for OLS stopping distance transformations.
