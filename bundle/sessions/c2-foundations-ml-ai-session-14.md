---
type: Session
resource: https://www.youtube.com/watch?v=pOGWGLEqPZQ
title: 'Session 14: Unsupervised Clustering Pipelines on Azure ML'
description: A hands-on workshop focused on building, evaluating, and iterating unsupervised
  K-Means clustering pipelines using Azure Machine Learning Studio with a real-world
  e-commerce shoppers dataset.
tags:
- unsupervised-learning
- clustering
- k-means
- azure-ml-studio
- data-preprocessing
- outlier-handling
- model-evaluation
timestamp: '2025-11-02'
---

This session is a comprehensive, hands-on workshop focused on building and evaluating unsupervised clustering pipelines using the classic Microsoft Azure Machine Learning (Azure ML) Studio. The lecture begins by contrasting unsupervised clustering with [Supervised Learning Foundations](../concepts/supervised-learning-foundations.md). While supervised techniques rely on predefined target labels to train models, clustering requires the algorithm to discover latent structures and similarities within the dataset independently. The instructor highlights that working with unsupervised data is increasingly vital today because unlabeled data is cheap and abundant, whereas generating high-quality labeled datasets is a costly bottleneck.

The core of the session guides students through the process of uploading, profiling, preprocessing, and model-fitting using the *Online Shoppers Purchasing Intention* dataset from the UCI Machine Learning Repository. Students learn how to configure the Azure ML Designer canvas, spin up a compute cluster (`standard_ds3_v2`) to profile datasets containing more than 10,000 rows, and implement critical preprocessing steps. The exploratory data analysis (EDA) phase reveals that several features (`informational`, `informational_duration`, `page_values`, and `special_day`) have zero variance across 75% of the data, leading to a decision to drop them. Outliers in session duration variables are handled via percentile clipping, and the mixed dataset types are cast into categorical formats.

Finally, the class explores the training, scoring, and evaluation of a K-Means clustering model. The instructor emphasizes qualitative assessment through the analysis of intra-cluster and inter-cluster distances in the **Evaluate Model** results. Students run parallel experiments by duplicating their pipelines on the canvas to compare two-cluster ($K=2$) and three-cluster ($K=3$) configurations. To address the visual limitations of high-dimensional datasets, the class discusses the necessity of [Dimensionality Reduction and Feature Extraction](../concepts/dimensionality-reduction.md) techniques like Principal Component Analysis (PCA). The session concludes with a detailed walk-through of cloud cost management, demonstrating how to delete deployed compute clusters and resource groups to avoid credit exhaustion.

# Key Concepts

- **Unsupervised Clustering vs. Classification** — In clustering, there are no predefined target labels. To treat the e-commerce dataset as a true unsupervised problem, the target `revenue` column must be dropped. Otherwise, the clustering algorithm will be heavily biased by this target label, resulting in label leakage and causing the clustering model to behave like a classifier.
- **Data Profiling at Scale** — By default, Azure ML profiles only the first 10,000 rows of a dataset. For larger datasets (such as the 12,330-row shoppers dataset), users must spin up an Azure compute cluster to run a full profile job to generate accurate descriptive statistics across all rows.
- **Outlier Trimming (Clip Values)** — Real-world web browsing session duration values (e.g., `administrative_duration` and `product_related_duration`) often contain massive outliers. The **Clip Values** component allows users to clip peak values above a certain percentile (e.g., 80th percentile) and substitute them with the column median.
- **Alternative Outlier Strategy** — Rather than substituting outliers with the median, users can configure **Clip Values** to replace outliers with "missing" values, and then insert a **Clean Missing Data** component set to "Remove entire row" to completely prune extreme outliers from the dataset.
- **Data Leakage in Normalization** — Data leakage occurs when statistics from the test partition (like mean or standard deviation used in Z-score normalization) influence the training set. While Z-score normalization is critical for distance-based clustering, performing Z-score scaling after splitting the data is an industry best practice to prevent this leakage.
- **K-Means Evaluation Metrics** — Evaluated under [Model Evaluation and Validation](../concepts/model-evaluation-validation.md) paradigms using intra-cluster distance (average distance to own center, which should be minimized) and inter-cluster distance (average distance to other centers, which should be maximized).
- **High-Dimensional Visualization** — Scatter plots are limited to two or three dimensions. Visualizing the 13-dimensional shoppers dataset requires [Dimensionality Reduction and Feature Extraction](../concepts/dimensionality-reduction.md) techniques like Principal Component Analysis (PCA) to project the clusters onto a 2D or 3D coordinate space, which is typically implemented in Python or KNIME.

# Topics Covered

- **Introduction**: Unsupervised learning vs. supervised learning; the cost-efficiency of working with unlabeled data; structured vs. unstructured data; self-learning in neural networks (CNNs/RNNs/LLMs).
- **Dataset Exploration**: UCI Repository introduction; Online Shoppers Purchasing Intention dataset description (12,330 records, session features, and the `revenue` label).
- **Azure ML Environment Setup**: Creating a resource group and workspace; launching ML Studio; constructing a canvas with the classic Designer.
- **Full Data Profiling**: Creating a compute cluster (`standard_ds3_v2` with 4 cores, 14 GB RAM, 28 GB storage); generating and analyzing descriptive statistics for datasets exceeding 10,000 records.
- **Exploratory Data Analysis (EDA)**: Identifying low-variance columns (`informational`, `informational_duration`, `page_values`, `special_day`) and deciding to drop them; detecting outliers in session durations.
- **Data Cleansing & Preprocessing**:
  - Dropping selected columns (including `revenue`) using **Select Columns in Dataset**.
  - Trimming outliers above the 80th percentile using **Clip Values** (percentile approach, replacing peaks with the median).
  - Explicitly formatting categorical columns (`operating_system`, `browser`, `region`, `traffic_type`, `visitor_type`, `weekend`, `month`) using the **Edit Metadata** component.
  - *Troubleshooting Pipeline Mismatch*: Resolving metadata conversion errors in Azure ML by using "by name" selection or placing Edit Metadata in the correct sequence relative to Clip Values.
- **Normalization and Train-Test Split**:
  - Normalizing features using Z-score normalization under the **Normalize Data** component.
  - Discussion on the mechanics of data leakage (normalizing before vs. after splitting).
  - Splitting dataset (70% train / 30% test) with **Stratified Split** set to `False` due to the lack of a target variable.
- **Model Training and Prediction**:
  - Utilizing the **Train Clustering Model** and **K-Means Clustering** components.
  - Configuring $K=2$ centroids and analyzing the Euclidean distance-based allocation.
  - Deploying the **Assign Data to Clusters** component (which acts as the scoring step in clustering) for test inference.
- **Evaluation and Parallel Iteration**:
  - Reviewing the **Evaluate Model** output (comparing average distance to other centers against average distance to its own center).
  - Replicating the pipeline via copy-paste on the canvas to evaluate $K=3$ clusters.
  - Analyzing skewed cluster distributions and discussing the elbow method.
- **Alternative Outlier Pruning Iteration**: Replacing outliers with missing values using **Clip Values** and removing those rows entirely with the **Clean Missing Data** component.
- **Cloud Administration & Resource Cleanup**: Locating cost management, viewing credit balances, deleting compute clusters, and destroying resource groups in the Azure Portal to prevent unexpected billing.

# Materials

- **Recording**: Video resource available via `https://www.youtube.com/watch?v=pOGWGLEqPZQ`.
- **Dataset**: Online Shoppers Purchasing Intention CSV dataset sourced from the UCI Machine Learning Repository.
- **Chat**: Present (student interactions and troubleshooting are logged in the session transcript).
- **Slides**: None.

# Related

- Parent Course: [Foundations ML AI](../courses/c2-foundations-ml-ai.md)
- Sibling Sessions:
  - [Session 13](c2-foundations-ml-ai-session-13.md)
  - [Session 15](c2-foundations-ml-ai-session-15.md)

# Citations

1. Microsoft Azure Machine Learning Studio, Lecture Video: `https://www.youtube.com/watch?v=pOGWGLEqPZQ`
2. UCI Machine Learning Repository, "Online Shoppers Purchasing Intention Dataset": [UCI Repository Link](https://archive.ics.uci.edu/)
3. KNIME Analytics Platform (Open-source visual programming environment mentioned as an alternative tool for clustering and visual workflows): [KNIME Official Website](https://www.knime.com/)
