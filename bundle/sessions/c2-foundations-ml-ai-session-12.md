---
type: Session
resource: https://www.youtube.com/watch?v=fCEwlBFQ3eg
title: 'Session 12: Association Rule Mining & Distance Metrics'
description: An introduction to unsupervised learning focusing on Association Rule
  Mining, the Apriori algorithm, and distance metrics for clustering.
tags:
- unsupervised-learning
- association-rules
- apriori-algorithm
- distance-metrics
- cosine-similarity
- jaccard-index
- gowers-distance
timestamp: '2025-10-26'
---

This session marks a transition in the [Foundations ML AI](../courses/c2-foundations-ml-ai.md) curriculum from [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md) to unsupervised learning techniques. Dr. Sridhar Pappu contrasts supervised column-mapping tasks with unsupervised pattern recognition, dividing the latter into column-oriented relationships (such as Association Rule Mining) and row-oriented relationships (such as clustering and nearest neighbors). The lecture details the mechanics of discovering latent patterns in multi-dimensional transactional and categorical datasets, highlighting real-world applications in retail, medical diagnostics, IT clickstream analysis, insurance fraud detection, and credit risk management.

The first half of the lecture establishes the framework for Association Rule Mining (ARM), tracing its origins in retail "Market Basket Analysis" to contemporary digital recommendation engines. Dr. Pappu explains the combinatorial challenge of rule generation, demonstrating how the space of potential rules grows exponentially as the item count increases, governed by the formula $R = 3^d - 2^{d+1} + 1$. To handle this combinatorial explosion, the statistical metrics of support, confidence, and lift are introduced as "interestingness measures" to filter out trivial or unhelpful rules. The Apriori algorithm is presented as a computationally elegant solution that utilizes the downward-closure property—where any subset of a frequent itemset must also be frequent—to aggressively prune infrequent itemsets from database scans. Dr. Pappu explores famous business applications, including Walmart's hurricane-season strawberry pop-tart sales spike (a positive lift of 7), time-lagged association rules (buying camcorders 3–4 months after purchasing a VHS player), and actionable rules (such as placing Dove soap and Barbie dolls together, or far apart to encourage impulsive browsing).

The second half of the session shifts focus to distance and similarity metrics, which serve as the foundation for clustering and K-Nearest Neighbors. The lecture explores mathematical formulations across different data modalities: continuous variables (Euclidean, Manhattan, and Minkowski distances), categorical and binary data (Hamming distance, Simple Matching Distance, Jaccard distance, and Sørensen-Dice index), text/document corpora (Cosine Similarity via word-frequency vector spaces), and mixed-type attributes (Gower's distance). Special emphasis is placed on the mandatory role of standardization (Z-score scaling) in preventing variables with larger absolute scales (e.g., income in thousands vs. age in years) from dominating distance calculations. The session concludes with interactive Q&A regarding linear regression assignment submissions, model diagnostics (leverage and Cook's distance), and the dramatic productivity gains when transitioning from proprietary drag-and-drop interfaces to code-based execution in Jupyter notebooks utilizing LLMs for rapid prototyping.

# Key Concepts

- **Unsupervised Learning Foundations** — Pattern discovery in datasets without a pre-existing target label. It is conceptually split into analyzing column-based relationships (finding which features/items co-occur) and row-based relationships (finding which observations/samples are similar). It stands in contrast to [supervised learning](../concepts/supervised-learning-foundations.md) foundations.
- **Association Rule Mining (ARM)** — A framework for discovering relationships between items in large transactional datasets, represented as implication rules of the form "If Antecedent ($X$), then Consequent ($Y$)."
- **Support, Confidence, and Lift** — The three fundamental metrics used to evaluate and filter association rules:
  - **Support**: The proportion of total transactions containing the combined itemset, representing joint probability: $P(X \cap Y) = \frac{\text{Count}(X \cap Y)}{N}$.
  - **Confidence**: The conditional probability that a transaction contains the consequent given that it contains the antecedent: $P(Y | X) = \frac{P(X \cap Y)}{P(X)}$.
  - **Lift**: A measure of the strength of a rule over random co-occurrence under statistical independence: $\text{Lift} = \frac{\text{Confidence}(X \rightarrow Y)}{\text{Support}(Y)} = \frac{P(X \cap Y)}{P(X) \times P(Y)}$. A lift of 1 indicates independence; lift $> 1$ indicates a positive association; lift $< 1$ indicates a negative/substitutive association.
- **The Apriori Principle** — A mathematical heuristic for pruning rule generation: if an itemset is frequent, all of its subsets must also be frequent. Conversely, if an itemset is infrequent, all of its supersets are guaranteed to be infrequent and can be safely ignored without scanning the database.
- **Standardization & Scale Sensitivity** — The mandatory process of standardizing variables (using Z-scores or normalization) before running distance-based algorithms. Variables with larger absolute scales (e.g., income in thousands vs. age in years) will artificially dominate distance calculations unless mapped to a uniform scale.
- **Text Vectors & Cosine Similarity** — Representing text documents as numerical word-frequency count vectors within [embeddings and vector representations](../concepts/embeddings-and-representations.md). Cosine Similarity measures the cosine of the angle ($\theta$) between these vectors: $\cos \theta = \frac{A \cdot B}{\|A\|_2 \|B\|_2}$. It evaluates orientation similarity rather than absolute magnitude, rendering document length irrelevant.
- **Categorical and Binary Distance Metrics** — Distance formulations tailored to non-numeric structures:
  - **Hamming Distance**: The count of mismatched categorical features between two observations.
  - **Simple Matching Distance (SMD)**: Dissimilarity metric representing the proportion of mismatches over the total number of attributes, symmetric in handling both joint presence and joint absence ($0-0$ matches): $\text{SMD} = \frac{b+c}{a+b+c+d}$.
  - **Jaccard Distance**: Dissimilarity metric that ignores joint absences ($0-0$ matches), crucial when the shared absence of an attribute does not imply similarity: $\text{Jaccard Distance} = \frac{b+c}{a+b+c}$.
  - **Sørensen-Dice Index**: Gives double weight to the common presence of attributes while ignoring joint absences: $\text{Dice Index} = \frac{2a}{2a+b+c}$ (mathematically equivalent to the F1-score).
- **Gower's Distance** — An aggregated similarity metric that standardizes and combines different distance metrics (such as normalized Manhattan for continuous variables, $0/1$ matching for binary nominal variables, and normalized ranks for ordinal variables) to handle mixed-type datasets on a uniform $[0, 1]$ scale.
- **Regression Diagnostics & [Model Validation](../concepts/model-evaluation-validation.md)** — Diagnostic parameters reviewed during student Q&A, identifying high-leverage observations and influential points using Cook's Distance ($D_i$), applying thresholds ($D_i > 1$ or $D_i > 3 \times \text{mean}(D)$) to evaluate how heavily individual points warp regression coefficients.

# Topics Covered

- **Introduction to Unsupervised Learning**: Comparing supervised column-mapping to unsupervised column-relationship (Association Rules) and row-relationship (Clustering) methodologies.
- **Market Basket Analysis & Rule Formulations**:
  - Definition of antecedent, consequent, rule length, and itemsets.
  - Mathematical proof of combinatorial explosion in rule generation: $R = 3^d - 2^{d+1} + 1$ (e.g., $d=2$ items yield $2$ rules, $d=10$ items yield $57,002$ rules, and $d=20$ items yield $3,484,687,250$ rules).
  - Evaluation of Support, Confidence, and Lift using probability tables (e.g., tea and coffee purchase combinations across independent, positive, and negative associations).
  - Business alignment and filtering: pruning trivial rules (e.g., shoes $\rightarrow$ socks), identifying inexplicable or actionable rules, and discussing retail shelf layouts and procurement strategies (e.g., Dove Soap and Barbie Dolls; Pop-Tarts during hurricane seasons).
- **The Apriori Algorithm**:
  - Walkthrough of candidate generation ($C_k$) and frequent itemset ($F_k$) identification.
  - Subgraph-like representation of candidate pruning.
  - High-level comparison with tree-based alternative algorithms (FP-Growth).
- **Clustering Foundations & Distance Mathematics**:
  - Distinguishing intracluster cohesion (compactness) from intercluster separation.
  - Continuous metrics: Euclidean ($L_2$ norm), Manhattan ($L_1$ / taxi cab / city block), and Minkowski distance.
  - Categorical/Binary metrics: Hamming distance, Simple Matching Distance (SMD), Jaccard distance, and Sørensen-Dice coefficient.
  - String/Text metrics: Word-count vector construction, dot product, Euclidean vector lengths, and Cosine Similarity (e.g., step-by-step calculation comparing Ronaldo and Serena document vectors, yielding $\cos \theta = 0.913$).
  - Ordinal metrics: Normalized rank mappings ($z = \frac{r - 1}{M - 1}$) and custom lookup tables (e.g., non-linear penalties for rating poor vs. very poor).
  - Mixed attributes: Gower's distance calculation.
- **Practical Workflow & Q&A**:
  - Assignment 1 logistical review: submitting PDF reports and Excel/CSV sheets using zip compression.
  - Regression diagnostics discussion: Cook's distance threshold rules of thumb and interpreting leverage vs. residual plots.
  - Industry practice shift: the transition from proprietary drag-and-drop interfaces to code-based execution in Jupyter notebooks utilizing LLMs for rapid prototyping and learning.

# Materials

- **Slides**: 
  - `Session 12 - (26 Oct 2025).pdf`
  - `Session12_Slides_2025-10-26.pdf`
- **Recording**: Video ID [fCEwlBFQ3eg](https://www.youtube.com/watch?v=fCEwlBFQ3eg) (Available on YouTube)
- **Chat**: Present (Active student participation regarding assignment submissions, leverage calculations, and coding environments)

# Related

- **Parent Course**: [Foundations ML AI](../courses/c2-foundations-ml-ai.md)
- **Previous Session**: [Session 11](c2-foundations-ml-ai-session-11.md)
- **Next Session**: [Session 13](c2-foundations-ml-ai-session-13.md)
- **Related Concepts**:
  - [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)
  - [Embeddings and Vector Representations](../concepts/embeddings-and-representations.md)
  - [Dimensionality Reduction and Feature Extraction](../concepts/dimensionality-reduction.md)
  - [Model Evaluation and Validation](../concepts/model-evaluation-validation.md)

# Citations

1. Video Lecture: https://www.youtube.com/watch?v=fCEwlBFQ3eg
2. Agrawal, R., & Srikant, R. (1994). *Fast algorithms for mining association rules*. Proceedings of the 20th International Conference on Very Large Data Bases (VLDB), 487-499.
3. Gower, J. C. (1971). *A general coefficient of similarity and some of its properties*. Biometrics, 27(4), 857-871.
4. Mahgoub, H. (2006). *Mining Association Rules from Unstructured Documents*. International Journal of Applied Mathematics and Computer Science, 1(4), 201-206.
5. Deshmukh, J., & Bhosle, Udhav. (2016). *Image Mining Using Association Rule for Medical Image dataset*. Procedia Computer Science, 85, 117-124.
6. Tanatorn, T., & Loetwiphut, P. (2023). *Association rule mining framework for financial credit-risk analysis in peer-to-peer lending platforms*. Financial Credit-Risk Analysis, 17, 1-12.
