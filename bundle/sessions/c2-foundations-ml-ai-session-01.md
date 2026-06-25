---
type: Session
resource: https://www.youtube.com/watch?v=KrV0BeHhNSc
title: 'Session 01: Introduction to AI, Symbolic AI, and Machine Learning Foundations'
description: An introduction to AI paradigms, detailing symbolic AI, expert systems,
  supervised and unsupervised learning, linear regression, gradient descent, and spurious
  regression.
tags:
- supervised-learning-foundations
- time-series-forecasting
- explainable-ai
- agentic-ai-autonomous-systems
- linear-regression
- gradient-descent
- symbolic-ai
timestamp: '2025-09-20'
---

This session marks the beginning of the "Foundations of ML and AI" course ([Foundations of Machine Learning and Artificial Intelligence](../courses/c2-foundations-ml-ai.md)), led by Dr. Sridhar Pappu. The lecture establishes the foundational baseline by defining and organizing the core artificial intelligence paradigms: symbolic AI, classical machine learning, deep learning, and generative AI. Dr. Pappu uses a real-world Japanese e-commerce fraud detection case study to contrast purely prompt-based [Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md) with traditional machine learning models. Through this comparative analysis, he illustrates why purely LLM-driven workflows are frequently less efficient, more expensive, and less accurate than classical mathematical classifiers when handling structured data, especially due to severe class imbalances.

The session traces the historical trajectory of artificial intelligence, starting from the 1956 Dartmouth Conference where John McCarthy, Marvin Minsky, and Herbert Simon established the field. The lecture details the rise and eventual limits of rule-based Expert Systems (such as Stanford's MYCIN in the 1970s), highlighting how rule-based translation failures (e.g., translating "the spirit is willing, but the flesh is weak" to Russian and back as "the vodka is good, but the meat is rotten") triggered the first AI Winter. Professor Pappu contrasts these expert systems with the robust predictive power of simple statistical equations, citing Robin Dawes' seminal 1979 paper on the robust beauty of improper linear models. This establishes the transition to modern machine learning, where the computer extracts patterns and formulas directly from data rather than relying on hand-coded rules.

Focusing on [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md), the lecture introduces linear regression mechanics using an airline fuel burn optimization (Cost of Weight) dataset. Dr. Pappu explains how gradient descent acts as an optimization framework to iteratively find the line of best fit by minimizing the squared errors. R-squared ($R^2$) is introduced as a measure of variance explained. The session concludes with a critical analysis of spurious regressions (using examples like steps walked vs. global COVID cases or associate degrees vs. breweries) to warn against confusing correlation with causation. This serves as a transition to explain when to use [Time Series Forecasting](../concepts/time-series-forecasting.md) models like ARIMA instead of classical linear regression.

# Key Concepts

- **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** — Core machine learning paradigm where the algorithm learns the mapping from input predictor variables to historical target labels. It splits into *regression* (predicting continuous numerical outputs) and *classification* (predicting discrete behavior or classes).
- **[Time Series Forecasting](../concepts/time-series-forecasting.md)** — A specialized modeling approach required when observations are sequential and time-dependent. While linear regression assumes independent observations, time series models like ARIMA (AutoRegressive Integrated Moving Average) capture temporal trends and seasonal variations without falling prey to spurious regressions.
- **[Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md)** — Systems designed with goal-driven behavior using LLMs. The lecture analyzes a fraud detection use case comparing purely LLM-based agentic workflows versus Composite AI (combining rules, machine learning, and LLMs). Purely agentic workflows struggle with structured data analysis, proving more expensive, slower, and lower-performing.
- **[Explainable AI (XAI)](../concepts/explainable-ai.md)** — The transparency of decision-making paths. Symbolic AI and Expert Systems are explainable by design (e.g., MYCIN's "why" command allowing the user to trace hardcoded rules), whereas complex machine learning models trade explainability for predictive performance, creating a need for post-hoc validation.
- **Symbolic AI (Expert Systems)** — Early AI paradigm based on codifying definitive human domain knowledge into deterministic "if-then" rule engines. While highly explainable and deterministic, it is labor-intensive to construct, fragile under edge cases, and vulnerable to the "commonsense knowledge problem" where conflicting rules or linguistic nuances cause failures.
- **Gradient Descent** — A fundamental optimization algorithm used in linear models and [Neural Network Architectures](../concepts/neural-network-architectures.md) to find the parameters (weights/biases) that minimize a loss function (error). It starts with random parameter initializations and iteratively updates them down the gradient of a convex error curve until a global minimum error is achieved.
- **Spurious Regression** — A statistical phenomenon where two completely independent variables show a misleadingly high correlation (such as Sridhar Pappu's walking steps correlating with global COVID cases at $R^2 = 85\%$ or US breweries correlating with math degrees at $R^2 = 99.1\%$). This usually occurs because time is a lurking variable affecting both trends, violating the regression assumption of independent data points.
- **Vibe Coding** — A term coined by Andrej Karpathy to describe coding primarily through high-level English prompts where AI tools (such as Claude 3.5 Sonnet, ChatGPT, Cline, and DeepSeek) generate the entire executable script. While excellent for rapid prototyping, it can produce unoptimized or buggy code and is not a substitute for robust production-ready software engineering.

# Topics Covered

- **Introduction and Leadership Ground Rules**: Course timeline, expectations of punctual attendance, and the role of DBA candidates as leaders in AI transformation.
- **The "Vibe Coding" Paradigm**: Building a complete, running prototype (including Streamlit UI) in 1.5 hours using English prompts and Cline/DeepSeek APIs.
- **The Fraud Detection Problem**: Case study of a Japanese e-commerce fraud system. Why a target of "99% accuracy" is meaningless for highly imbalanced datasets where fraud is rare (e.g., 1%), as a dummy model predicting "no fraud" achieves 99% accuracy but fails to catch any fraud. This emphasizes the need for [Model Evaluation and Validation](../concepts/model-evaluation-validation.md) metrics like precision, recall, and F1 score.
- **The Building Blocks of AI**: Distinguishing symbolic AI, machine learning, deep learning, and generative AI.
- **History and Vision of AI**: The 1956 Dartmouth Conference, Marvin Minsky's definition, Herbert Simon's prediction for 1985, and John McCarthy's concept of precise simulation. The first AI Winter triggered by rule-based translation failures (the 1966 ALPAC report).
- **Expert Systems**: In-depth review of Stanford's MYCIN system (1970s), rule structures (Rule 160), antibiotic dosage recommendation, and the reasoning explanation engine ("why" command).
- **Robust Beauty of Improper Linear Models**: Analysis of Robin Dawes' 1979 work demonstrating that mathematical models with equal weights outperform human domain experts in bankruptcy prediction and patient survival rates because humans fail to process multi-variable (10+ variables) interconnections.
- **Data Modalities**: Differentiating between structured data (spreadsheets, relational database models, matrices, data frames) and unstructured data (text, images, video, audio, graphs).
- **Linear Regression Mechanics**: The linear equation ($\hat{y} = \beta_0 + \beta_1 x$), parameters (intercept $\beta_0$, slope $\beta_1$), error squared minimization, and R-squared ($R^2$) as a goodness-of-fit metric.
- **Cost of Weight (COW)**: Industry airline fuel efficiency case study showing landing weight vs. fuel burn. Real-world weight-cutting measures (United Airlines magazine paper weight reduction, Indonesia Airlines cabin oven removal, Indigo serving cold food).
- **Spurious Regression Mechanics**: Examining why independent time-dependent series yield misleadingly high correlation and high R-squared values, and detailing Clive Granger's contribution (Granger Causality).
- **Time Series Forecasting Introduction**: Differentiating simple regression from forecasting when time is a lurking variable, introducing ARIMA models.
- **Supervised Use Cases**: Differentiating regression use cases (customer lifetime value, supply chain demand forecasting, software development cost estimation, salary estimation) from classification use cases (customer churn, predictive maintenance, spam/phishing detection, employee sentiment analysis, ad click prediction).
- **Textbook and Literature Selection**: Recommended literature including Provost & Fawcett (*Data Science for Business*), Hyndman (*Forecasting*), Mitchell (*Artificial Intelligence*), Tan, Steinbach & Kumar (*Introduction to Data Mining*).

# Materials

- **Slides**:
  - `Session 01 - (20 Sep 2025).pdf`
  - `Session01_Slides_2025-09-20.pdf`
- **Recording**: Available via YouTube identifier `KrV0BeHhNSc`.
- **Chat**: Not recorded for this session.

# Related

- Sibling Session: [Session 02: Classification Algorithms and Logistic Regression](c2-foundations-ml-ai-session-02.md)
- Sibling Session: [Session 03: Decision Trees and Ensemble Methods](c2-foundations-ml-ai-session-03.md)
- Parent Course: [Foundations of Machine Learning and Artificial Intelligence](../courses/c2-foundations-ml-ai.md)

# Citations

1. Hyndman, R. J., & Athanasopoulos, G. (2018). *Forecasting: Principles and Practice*. OTexts.
2. Provost, F., & Fawcett, T. (2013). *Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking*. O'Reilly Media.
3. Dawes, R. M. (1979). *The robust beauty of improper linear models in decision making*. American Psychologist, 34(7), 571–582.
4. Shortliffe, E. H. (1976). *Computer-Based Medical Consultations: MYCIN*. Elsevier.
5. Recorded lecture: `https://www.youtube.com/watch?v=KrV0BeHhNSc`.
