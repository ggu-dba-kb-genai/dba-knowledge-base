---
type: Session
resource: https://www.youtube.com/watch?v=PbKPV88qQP8
title: 'Session 03: Descriptive Statistics & Linear Regression Foundations'
description: This session covers fundamental descriptive statistics including central
  tendencies, variability, and box plots, followed by an introduction to ordinary
  least squares linear regression.
tags:
- statistics
- mean
- median
- mode
- variance
- standard-deviation
- z-score
- box-plot
- linear-regression
- OLS
timestamp: '2025-09-27'
---

This lecture serves as a practical bridge from high-level AI paradigms to concrete, mathematically grounded machine learning models. The instructor begins by recapping the three major eras of AI: Symbolic AI (knowledge engineering utilizing codified expert rules), classical machine learning (learning statistical rules or equations over structured tabular columns), and deep learning (utilizing multi-layered [Neural Network Architectures](../concepts/neural-network-architectures.md) to automatically extract abstract representations from unstructured data). To illustrate, a brief recap of [Computer Vision](../concepts/computer-vision.md) is provided, demonstrating how [Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md) allows a deep learning model pre-trained on animal images to achieve superhuman accuracy classifying chest X-rays with minimal layer modifications. After comparing supervised learning (with historical labels) to unsupervised learning (finding patterns in unlabeled columns, such as clustering), the session dives into basic descriptive statistics as the fundamental baseline for exploratory data analysis (EDA).

The first core portion of the session focuses on descriptive statistics, highlighting central tendencies and measures of variability from an intuitive decision perspective. The arithmetic mean, median, and mode are defined and examined under optimization lenses. Through a simulated airline overbooking exercise (predicting no-shows for an American Airlines flight from El Paso, TX to San Jose, CA), the instructor demonstrates that the choice of average is mathematically dictated by the business penalty function: the mode minimizes exact binary misclassifications, the median minimizes absolute errors (linear penalties), and the mean minimizes squared errors (quadratic penalties). Moving to spread metrics, the lecture defines range, interquartile range (IQR), variance, and standard deviation—illustrating how variance squared units (e.g., squared coughs in the COVID-19 dataset) are brought back to the original units via standard deviation to measure consistent variation around the mean. The standard score or z-score ($Z = \frac{x - \mu}{\sigma}$) is introduced as a metric representing the number of standard deviations a data point lies from the mean, establishing the statistical basis for data standardization in machine learning pipelines.

The second half of the session explores visual data distributions and introduces [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md) via Ordinary Least Squares (OLS) linear regression. The box and whisker plot is shown to be an elegant, five-point summary tool (comprising the minimum, $Q1$, median, $Q3$, and maximum) designed to identify statistical outliers beyond the upper and lower fences ($Q3 + 1.5 \times \text{IQR}$ and $Q1 - 1.5 \times \text{IQR}$). The instructor presents the historical 1949 UK gestation lawsuit (*Hadlum v. Hadlum*) and daily N95 mask versus hand sanitizer sales as case studies for outlier detection. Transitioning to simple linear regression ($\hat{y} = \beta_0 + \beta_1 x$), the instructor explains how to find the optimal intercept ($\beta_0$) and slope ($\beta_1$, calculated as rise/run or $\Delta y / \Delta x$). Using real-world aircraft fuel flow data relative to landing weight, the OLS model is introduced as an algorithm designed to minimize the sum of squared residuals ($y - \hat{y}$). Because OLS minimizes squared error deviations, linear predictions mathematically represent conditional expectations (the mean), setting the stage for subsequent [Model Evaluation and Validation](../concepts/model-evaluation-validation.md) discussions.

# Key Concepts
- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — Mapping independent variables to a continuous, numeric target variable using optimization algorithms that fit linear equations to labeled historical datasets.
- **[Model Evaluation and Validation](../concepts/model-evaluation-validation.md)** — Grounded in residual analysis where residuals ($y - \hat{y}$) represent the unexplained deviations between the actual data points and the regression line predictions.
- **Central Tendencies and Mathematical Optimization** — Mean ($\mu$), median, and mode are not just descriptive terms, but optimization solutions: the mode minimizes exact classification errors, the median minimizes absolute deviations, and the mean minimizes squared deviations.
- **Z-Score and Standardization** — A dimensionless standard score ($Z = \frac{x - \mu}{\sigma}$) indicating how many standard deviations a value lies from the mean, widely used to standardize scale differences between independent variables in ML pipelines.
- **[Neural Network Architectures](../concepts/neural-network-architectures.md)** — Modern deep networks build upon linear formulas ($y = mx + c$) connected across thousands of layers to automatically learn hierarchical feature representations.
- **[Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md)** — Adapting pre-trained neural networks to specialized fields (e.g., diagnosing chest pathology via edge detection layers trained on animal classification) to achieve high-accuracy results on limited data.
- **Outliers and Box Plots** — Outliers are identified statistically when data points lie outside the fences defined by 1.5 times the Interquartile Range ($Q3 - Q1$). Outliers represent extreme deviations from average variations, but serve as vital messengers rather than errors to blindly discard.

# Topics Covered
- **The Course Arc and AI Paradigms** (Symbolic AI, Machine Learning, and Deep Feature Representation)
- **Central Tendencies & Optimization Metrics**
  - Mean minimizes quadratic loss (squared deviations)
  - Median minimizes linear loss (absolute deviations)
  - Mode minimizes exact classification errors
- **Airline Overbooking Case Study** (Optimizing statistical consultant income and airline seat overbooking under linear, quadratic, and exact penalty metrics)
- **Measures of Variability** (Range, IQR, Variance, Standard Deviation, and Consistency track-records)
- **Feature Standardization** (Derby vs. Hannah performance and the computation of Z-scores)
- **Box and Whisker Diagrams** (Five-point summaries, fence equations, and visual outlier detection)
- **Outlier Case Studies** (pregnancy gestation in *Hadlum v. Hadlum, 1949*, and daily N95 mask vs. hand sanitizer sales distributions)
- **Ordinary Least Squares (OLS) Linear Regression**
  - Formula: $\hat{y} = \beta_0 + \beta_1 x$
  - Slope ($\beta_1 = \frac{\Delta y}{\Delta x}$) and Constant/Intercept ($\beta_0$)
  - Minimizing the Cost Function: Sum of Squared Errors ($SSE = \sum (y_i - \hat{y}_i)^2$)
  - Aircraft fuel flow and landing weight dataset application

# Materials
- **Slides**: `20250927_BasicStatistics_LinearRegression.pdf`
- **Chat Present**: Yes (students discussed PowerBI analytical toolsets, Excel tools, six-sigma black-belt concepts, and process capability metrics such as $C_{pk}$)
- **Recording**: `https://www.youtube.com/watch?v=PbKPV88qQP8`

# Related
- Part of **[Foundations ML AI](../courses/c2-foundations-ml-ai.md)**
- Sibling Sessions:
  - **[Session 02: Classification, Regression, & Key AI Terms](c2-foundations-ml-ai-session-02.md)**
  - **[Session 04: Linear Regression Metrics & R-Square Validation](c2-foundations-ml-ai-session-04.md)**

# Citations
1. Golden Gate University, Foundations ML AI Course, Session 03 (2025-09-27) — `https://www.youtube.com/watch?v=PbKPV88qQP8`.
2. Leung, N.H.L., Chu, D.K.W., Shiu, E.Y.C. *et al.* Respiratory virus shedding in exhaled breath and efficacy of face masks. *Nat Med* (2020). [https://doi.org/10.1038/s41591-020-0843-2](https://doi.org/10.1038/s41591-020-0843-2).
3. *Hadlum v. Hadlum* (1949), High Court of Justice (UK) — Legal gestation outlier precedent.
