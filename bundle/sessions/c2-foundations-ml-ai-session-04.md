---
type: Session
resource: https://www.youtube.com/watch?v=MKcLXbQIAK0
title: 'Session 04: Exploratory Data Analysis & Linear Regression Foundations'
description: A hands-on laboratory exploring exploratory data analysis (EDA) using
  Microsoft PowerBI on the mtcars dataset, supplemented by theoretical foundations
  of simple linear regression and diagnostics.
tags:
- EDA
- PowerBI
- mtcars
- Linear Regression
- Model Evaluation
- Model Diagnostics
- Outlier Detection
timestamp: '2025-09-28'
---

In this session, students engage in a hands-on laboratory exploring Exploratory Data Analysis (EDA) using Microsoft PowerBI, led by guest instructor Dr. Raj Kumar. The lab uses the classic `mtcars` vehicle performance dataset to demonstrate structured data exploration, feature categorization, and interactive dashboarding. Students learn to import local data, manage schema properties in PowerBI, and construct interconnected visualizations—including donut charts, stacked column graphs, line plots, and scatter plots—leveraging PowerBI's dynamic cross-filtering capabilities. This practical laboratory bridges raw data preprocessing with predictive modeling, enabling students to establish an intuitive understanding of dataset features, distributions, and multi-variable relationships.

Alongside the hands-on lab, the session's prepared materials (compiled by Dr. Srinivasa Varadharajan Lakshminarasimhan) establish the mathematical foundations of Simple Linear Regression (Ordinary Least Squares) and model diagnostics. The theoretical framework details how to leverage correlation and bivariate analysis to construct predictive models, evaluate overall performance using metrics like $R^2$ and Adjusted $R^2$, and conduct hypothesis testing on model parameters. Additionally, it outlines the core assumptions of linear regression—such as linearity, homoscedasticity, normality of residuals, and independence of errors—and introduces diagnostic metrics like Tukey's Ladder of Powers, Leverage, Studentized Residuals, and Cook's Distance to identify outliers and non-linear patterns.

# Key Concepts

- **Exploratory Data Analysis (EDA)** — The foundational process of investigating a dataset to summarize its main characteristics, often using visual methods. In this session, EDA serves as a precursor to implementing [supervised learning foundations](../concepts/supervised-learning-foundations.md).
- **Continuous vs. Discrete Variables** — Clarifying the mathematical and physical distinction between continuous variables (e.g., mileage `MPG`, displacement `disp`, and weight `wt`, which can take any fractional value) and countable discrete variables (e.g., cylinders `cyl` and gears `gear`).
- **Categorical vs. Numeric Context** — Recognizing that numeric columns like `cyl` or `gear` are often better treated as nominal or ordinal categorical variables when mathematical operations on them (e.g., calculating an average engine cylinder count) lack physical meaning.
- **Labeled Data & Binary Encoding** — Using numeric labels to represent categorical binary classes (e.g., transmission type `am` where 0 denotes manual and 1 denotes automatic; engine configuration `vs` where 0 is V-shaped and 1 is straight/inline).
- **Semantic Data Modeling** — Creating automated data pipelines and managing table schemas (such as star or snowflake schemas) to handle multiple interconnected data sources, setting business intelligence tools apart from traditional spreadsheets.
- **PowerBI Cross-Filtering & Interactivity** — The mechanism where individual visuals dynamically filter one another upon selection, allowing users to select a specific category (e.g., three-gear vehicles) and instantly observe its distribution and trend across all other charts on the canvas.
- **Simple Linear Regression (OLS)** — A linear approach to modeling the relationship between a dependent target variable ($y$) and a single independent predictor variable ($x$):
  $$\hat{y} = \beta_0 + \beta_1 x$$
  where the coefficients are solved to minimize the Sum of Squared Errors ($SSE$):
  $$\beta_1 = \rho \frac{s_y}{s_x}, \quad \beta_0 = \bar{y} - \beta_1 \bar{x}$$
- **Goodness-of-Fit Metrics** — Evaluation criteria to determine model efficacy, representing [model evaluation and validation](../concepts/model-evaluation-validation.md):
  - **Sum of Squared Total ($SST$):** Measures total variance in the target: $SST = \sum (y_i - \bar{y})^2$
  - **Sum of Squared Errors ($SSE$):** Measures unexplained residual variance: $SSE = \sum (y_i - \hat{y}_i)^2$
  - **Sum of Squared Regression ($SSR$):** Measures variance explained by the model: $SSR = \sum (\hat{y}_i - \bar{y})^2$, where $SST = SSE + SSR$
  - **R-squared ($R^2$):** The proportion of total variance explained by the model: $R^2 = 1 - \frac{SSE}{SST}$
  - **Adjusted R-squared ($R^2_{adj}$):** Penalizes the addition of non-informative predictors using degrees of freedom: $R^2_{adj} = 1 - \frac{SSE / (n - k - 1)}{SST / (n - 1)}$
- **Assumptions of Linear Regression** — Requirements for valid linear models, which relate to the [bias-variance tradeoff](../concepts/bias-variance-tradeoff.md):
  1. *Linearity:* Linear relationship between independent and dependent variables. Non-linear relationships can be addressed using Tukey's Ladder of Powers or Tukey's Four Quadrants.
  2. *Homoscedasticity:* Constant variance of residuals across predicted values $\hat{y}$. Discerned via residual plots and addressed via data transformations.
  3. *Normality of Residuals:* Residuals are normally distributed around zero, analyzed using Quantile-Quantile (Q-Q) Plots.
  4. *Independence of Errors:* Residuals are randomly scattered with no discernible patterns.
- **Outlier Diagnostics** — Methods to identify disproportionately influential data points:
  - **Leverage ($h_i$):** Evaluates the influence of an independent variable: $h_i = \frac{1}{n} + \frac{(x_i - \bar{x})^2}{\sum (x_j - \bar{x})^2}$. Points are leverage outliers if $h_i > 2\bar{h}$ (where $\bar{h} = p/n$).
  - **Studentized Residuals ($R_i$):** Quantifies residual size normalized by its standard error: $R_i = \frac{e_i}{\sqrt{MSE(1 - h_i)}}$. Points are outliers if $|R_i| > 2$.
  - **Cook's Distance ($D_i$):** Measures aggregate impact on all predicted values: $D_i = \frac{h_i}{1 - h_i} \frac{R_i^2}{p}$. Points are critical outliers if $D_i > 1.0$, or potential outliers if $D_i > 0.5$.

# Topics Covered

- **The `mtcars` Dataset Schema**: Detailed breakdown of attributes including `model`, miles per gallon (`MPG`), cylinders (`cyl`), displacement (`disp`), horsepower (`HP`), rear axle ratio (`drat`), weight (`wt` in pounds), quarter-mile time (`qsec`), engine shape (`vs`), transmission (`am`), gears (`gear`), and carburetors (`carb`).
- **PowerBI Environment Comparison**: Exploring differences and deployment workflows between PowerBI Desktop and the cloud-based PowerBI Online Service using university GGU credentials.
- **Power Query and Schema Configuration**: Importing local `.xlsx` files, promoting first rows as headers, and stripping default automatic summation properties (Sigma symbol, $\Sigma$) by setting "Summarize By" to "None" in the Model View/Properties pane.
- **Developing Visualizations in PowerBI**:
  - *Univariate Donut Chart:* Tracking the proportion of automatic versus manual transmissions (`am`).
  - *Univariate Stacked Column Chart:* Visualizing the frequency distribution of vehicle gears (`gear`).
  - *Bivariate Line Chart:* Plotting vehicle weight (`wt`) against average mileage (`MPG`), subsequently expanded to a multivariate chart by adding average horsepower (`HP`) to a secondary Y-axis.
  - *Multivariate Scatter Plot:* Mapping horsepower (X-axis) against MPG (Y-axis), using distinct colors for model labels and binding bubble sizing to average weight (`wt`) to uncover spatial vehicle clusters.
- **Linear Regression Mechanics**: Formalizing OLS estimation, the geometric interpretation of residual errors, and the decomposition of total errors ($SST = SSE + SSR$).
- **Statistical Model Evaluation**: F-tests on the overall model ($F = MSR/MSE$), t-tests on individual parameter coefficients ($\beta_j$), and the diagnostic importance of p-values (threshold of $\alpha = 0.05$).
- **Regression Diagnostics & Remediation**: Generating residual plots (residuals vs. $\hat{y}$), constructing theoretical vs. experimental Q-Q Plots, applying Tukey's Ladder of Powers for non-linear variables, and using Cook's D, Studentized Residuals, and Leverage for outlier screening.

# Materials

- **Slides**: `Session_6_20250928_Lin-Regr.pdf` (Covers Simple Linear Regression theory, model assumptions, hypothesis testing, and diagnostics).
- **Chat**: Present (student-instructor queries regarding PowerBI desktop access, file upload configurations, data type overrides, and chart interactivity).
- **Recording**: Available on YouTube with video ID [MKcLXbQIAK0](https://www.youtube.com/watch?v=MKcLXbQIAK0).

# Related

- Part of the [Foundations ML AI](../courses/c2-foundations-ml-ai.md) course.
- Previous Session: [Session 03](c2-foundations-ml-ai-session-03.md)
- Next Session: [Session 05](c2-foundations-ml-ai-session-05.md)

# Citations

1. YouTube recording of the session: `https://www.youtube.com/watch?v=MKcLXbQIAK0`
2. Montgomery, D. C., Peck, E. A., & Vining, G. G. (2021). *Introduction to Linear Regression Analysis* (6th ed.). Wiley.
3. Henderson, H. V., & Velleman, P. F. (1981). Building multiple regression models interactively. *Biometrics*, 37(2), 391-411.
4. Microsoft PowerBI Documentation: [https://learn.microsoft.com/en-us/power-bi/](https://learn.microsoft.com/en-us/power-bi/)
