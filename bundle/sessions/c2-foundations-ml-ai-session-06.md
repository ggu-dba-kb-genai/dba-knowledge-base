---
type: Session
resource: https://www.youtube.com/watch?v=21KaSuYb9Ts
title: 'Session 06: Regression Diagnostics, Transformations, and Multi-collinearity'
description: A comprehensive lecture on linear regression diagnostics, including residual
  analysis, Cook's distance, data transformations, dummy variables, multi-collinearity,
  and evaluation metrics.
tags:
- linear-regression
- model-diagnostics
- cooks-distance
- data-transformation
- dummy-variables
- multi-collinearity
- regression-metrics
timestamp: '2025-10-05'
---

In this sixth session of the course, Dr. Sridhar Pappu guides the class through a deep dive into multiple linear regression diagnostics, data transformations, categorical variables, and multi-collinearity. The lecture bridges the gap between simple model fitting and rigorous validation, teaching students how to look beyond high $R^2$ values to evaluate whether model assumptions actually hold. Through diagnostic residual analysis, students learn to inspect linear relationships, verify homoscedasticity, ensure error normality, and systematically separate outliers from high-leverage influential observations.

The session also addresses practical solutions when linear regression assumptions are violated. Students are introduced to mathematical data transformations (such as logarithmic, square root, and inverse scales) and Tukey’s Ladder of Powers to correct non-linearity and stabilize variance. Furthermore, the lecture explains how to represent categorical predictors using indicator (dummy) variables, showing how intercept and coefficients represent mean comparisons with an omitted reference group. Finally, the session explores multi-collinearity—quantifying its impact via Variance Inflation Factors (VIF) and showing how step-by-step feature pruning can restore model interpretability without sacrificing predictive accuracy, concluding with a detailed review of standard regression evaluation metrics. A unique aspect of Dr. Pappu's lecturing style is his use of quote-driven slides to introduce key concepts and provide pedagogical pauses.

# Key Concepts

- **Residual Diagnostics** — A core part of [Model Evaluation and Validation](../concepts/model-evaluation-validation.md) used to test the four primary assumptions of linear regression: linearity, independence of errors, homoscedasticity (constant residual variance), and normal distribution of residuals.
- **Influential Observations vs. Outliers** — Outliers are points far from the regression line (large residuals), while influential observations drastically twist the regression line. They are quantified using **Cook's Distance (Cook's D)**, which combines a point's leverage (distance from the predictor mean) and its studentized residual. A Cook's D $> 1.0$ designates a highly influential point, while points exceeding $3 \times \text{average Cook's D}$ warrant detailed sensitivity analysis.
- **Data Transformations** — Procedures like taking the square root ($\sqrt{y}$ for moderate positive skewness, index $0.5$ to $1.0$) or natural log ($\ln y$ for heavy positive skewness, index $> 1.0$) to stabilize variance and straighten non-linear relationships. Tukey's Ladder of Powers provides a quadrant guide for straightening curves, while automated techniques like Box-Cox (for transforming $y$) and Box-Tidwell (for transforming $x$) find optimal power parameters.
- **Dummy Variables (Indicator Coding)** — Methods within [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md) to represent categorical predictors in a linear model. For $n$ category levels, $n-1$ dummy variables are introduced to prevent the "dummy variable trap" (perfect multi-collinearity). The intercept represents the mean target value of the omitted reference category, while coefficients represent the mean difference between each category and that reference.
- **Multi-collinearity & VIF** — High correlation among independent variables that inflates the standard errors of coefficients, flips coefficient signs, and masks individual feature significance. It is quantified via the **Variance Inflation Factor (VIF)**, defined as $VIF_i = 1 / (1 - R_i^2)$. Mitigating multi-collinearity is vital for [Explainable AI (XAI)](../concepts/explainable-ai.md), though it has minimal impact if the sole goal is pure prediction.
- **Regression Evaluation Metrics** — Standard error measures used in [Model Evaluation and Validation](../concepts/model-evaluation-validation.md) to evaluate generalization and diagnose overfitting. These include Mean Absolute Error (MAE/L1 loss), Mean Squared Error (MSE/L2 loss), Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE), and Huber Loss (a robust estimator combining L1 and L2 behaviors).

# Topics Covered

- **Review of Regression Diagnostics**: Recapping $R^2$, variable $p$-values, overall F-statistic significance, and the four main residual assumptions (linearity, independence, homoscedasticity, and normality using Q-Q plots).
- **Outliers vs. Influential Points Simulation**:
  - *Case Study 1 (Eric McCoo's 1998 Rushing Yards)*: Rushing yards vs. Penn State's final score. Including a single record-setting game of 206 rushing yards against Michigan State yields an $R^2$ of 25%; excluding it drops $R^2$ to 8%, showing how one point can exert immense influence over the regression line.
  - *Case Study 2 (21-Point Simulated Dataset)*: Demonstrating four structural cases of an unusual Point #9:
    1. **Within X and Y Range (4, 40)**: Aligns with trend; Cook's D is $0.36$ (not influential).
    2. **Outlier in Y only (4, 100)**: Large residual but low leverage. Degrades $R^2$ from 97.32% to 39.47%, but Cook's D is $0.5$ (not influential on slope).
    3. **Outlier in X only (20, 40)**: High leverage and out-of-trend. Twists the slope significantly; Cook's D is $12.69$ (highly influential).
    4. **Outlier in X and Y (20, 100)**: High leverage but zero residual because it aligns with the trend. Cook's D is $0.73$ (not influential).
  - *Business Action*: Deciding whether to omit abnormal data (e.g., weather disruptions like cyclones), bound the model range, or transition to robust estimators.
- **Data Transformations**:
  - Calculating skewness using cubed $z$-scores ($\frac{\sum (x-\mu)^3 / n}{\sigma^3}$) to guide transformations.
  - Shifting zero or negative values by adding a constant before applying square roots or logarithms.
  - Curve-straightening via Tukey's Ladder of Powers (modeled as pulling the ends of a bent rubber pipe).
  - Automated power transformations using Box-Cox and Box-Tidwell, emphasizing rounding suggested exponents (e.g., $1.5678 \to 2.0$) to maintain model interpretability.
- **Handling Categorical Predictors**:
  - *HR Dataset Case Study*: Modeling `Pay Rate` using Age, Duration of Employment (Vintage), and Job Description (10 levels $\to$ 9 dummy variables).
  - *Omitted Reference Interpretation*: Omitting "Accountant I" sets the intercept to \$26.83 (exactly the mean pay of Accountant I). The Administrative Assistant coefficient of -\$7.31 means their mean pay is \$19.52 (\$26.83 - \$7.31).
  - *Level Merging*: Setting "Database Administrator (DBA)" as the reference level makes the Network Engineer coefficient non-significant ($p = 0.934$). Since their pay rates are not statistically different, Occam's Razor suggests merging them into a single "DBA + Network Engineer" job category to simplify the model.
- **Multi-collinearity and VIF**:
  - *Energy Consumption Case Study*: High correlation between US auto fuel rate and coal production ($0.968$) flips the auto fuel rate coefficient from positive (+0.7838 individually) to negative (-0.3934 combined).
  - *Diaper Design Analogy*: Multi-collinearity can flip the sign of a critical feature like "diaper softness" to negative, leading designers to make rough diapers that cause babies to cry.
  - *VIF Step-by-Step Feature Selection (`mtcars` dataset)*:
    1. **Initial Model (10 variables)**: Overall model highly significant ($p < 0.05$), but no individual feature is significant ($p > 0.05$). `disp` has the highest VIF ($21.62$). Remove `disp`.
    2. **Step 2**: Rebuild model. `cyl` has the highest remaining VIF ($14.28$). Remove `cyl`.
    3. **Step 3**: Rebuild model. All VIFs are now $< 10$. `gear` has the highest $p$-value ($0.613$). Remove `gear`.
    4. **Step 4**: `vs` has the highest $p$-value ($0.885$). Remove `vs`.
    5. **Step 5**: `hp` has the highest $p$-value ($0.463$). Remove `hp`.
    6. **Step 6**: `drat` has the highest $p$-value ($0.396$). Remove `drat`.
    7. **Step 7**: `carb` has the highest $p$-value ($0.256$). Remove `carb`.
    8. **Final Model**: Remaining variables `wt` (weight), `qsec` (1/4 mile time), and `am` (transmission) are all statistically significant with VIFs $\le 2.5$. Adjusted $R^2$ stabilizes at 83.36% (improved from the full model's 80.66%).
- **Evaluating Model Performance**:
  - Formulating MAE, MSE, RMSE, MAPE, and Huber Loss.
  - Using error metrics on training vs. testing datasets to diagnose overfitting (e.g., training MSE of 75 vs. testing MSE of 100), highlighting the [Bias-Variance Tradeoff](../concepts/bias-variance-tradeoff.md).
  - Sample use cases: MAE for delivery estimates, MAPE for monthly product returns, and Huber Loss for discount elasticity to avoid outlier price-sensitivity penalties.

# Materials

- **Slides**: `20251005_LinearRegression.pdf`
- **Chat**: Present in the session archive.
- **Recording**: YouTube Video ID [21KaSuYb9Ts](https://www.youtube.com/watch?v=21KaSuYb9Ts)

# Related

- Part of [Foundations ML AI](../courses/c2-foundations-ml-ai.md)
- Sibling Sessions:
  - [Session 05](c2-foundations-ml-ai-session-05.md) (2025-10-04) — Introduction to Linear Regression and Hypothesis Testing
  - [Session 07](c2-foundations-ml-ai-session-07.md) (2025-10-11) — Logistic Regression

# Citations

1. YouTube Lecture: [Session 06 Recording](https://www.youtube.com/watch?v=21KaSuYb9Ts)
2. Cook's Distance: Cook, R. Dennis (1977). "Detection of Influential Observation in Linear Regression". Technometrics.
3. Box-Cox Transformations: Box, G. E. P.; Cox, D. R. (1964). "An Analysis of Transformations". Journal of the Royal Statistical Society.
4. Tukey's Exploratory Data Analysis: Tukey, John W. (1977). Addison-Wesley.
