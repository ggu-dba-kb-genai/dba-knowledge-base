---
type: Assignment
resource: null
title: 'C3 Assignment 1 — Conceptual Deep Learning Architecture Design'
description: Individual non-coding executive report that designs a conceptual deep
  learning architecture for a complex business problem — justifying network design,
  optimization, regularization, and representation choices.
tags:
- deep-learning
- individual-assignment
- architecture-design
- regularization
- autoencoders
timestamp: '2026-06-01'
---

**Course:** Deep Learning & its Variants (C3) · **Type:** Individual ·
**Deliverable:** Executive report, 1,000–2,500 words

## Summary

The objective is to demonstrate a **deep, non-coding understanding** of fundamental deep
learning architectures and optimization techniques by applying them to a complex,
non-linear business problem. Students choose a domain problem warranted for a deep learning
approach, with data mixing structured and unstructured/semi-structured signals and a single
outcome variable (continuous, binary, multi-class, or a recommendation), then **design a
conceptual architecture** to predict it.

The executive report must systematically address:

1. **Problem description & justification** — the problem, the data, expected model behaviour, and why a simple perceptron or linear model is insufficient.
2. **Architectural design (MLP/DNN)** — necessity and conceptual design (number and width of layers, hidden-layer activation choices); output-layer activation and how weights connect inputs to the final prediction.
3. **Optimization & training strategy** — the role of gradient descent and back-propagation; technique for fast convergence (learning-rate / gradient optimization); handling vanishing or exploding gradients.
4. **Taming complexity & generalization** — justify two regularization techniques (Dropout vs Batch Normalization, or both, and their ordering/placement) and how each prevents overfitting.
5. **Feature & data representation** — whether autoencoders (encoder/decoder) are used for dimensionality reduction, and whether categorical embeddings are used, with justification.

## Rubric

| Criteria | Excellent (20–16) | Good (15–11) | Satisfactory (10–6) | Poor (5–0) |
| --- | --- | --- | --- | --- |
| 1. Problem Description & Justification | Business problem well described; data, features, and challenges detailed; DNN justification well documented. | Problem well described; data/features detailed; DNN justification weak. | Problem described but data/features not clear; justification weak. | Fails to clearly describe the problem, data, and justification. |
| 2. Architectural Design (MLPs/DNNs) | All aspects of the design explained clearly. | One aspect (activation, layers, autoencoder need, etc.) unclear. | Many parts of the design poorly described. | Section reads like a confused mess. |
| 3. Optimization & Training Strategy | Clear reasoning on gradient descent (online/batch/mini-batch), learning-rate/gradient optimization, back-propagation. | Techniques described but justification weak. | Only some techniques described; justification weak. | No clear justification for chosen methods. |
| 4. Taming Complexity & Generalization | Regularization described well and clearly justified. | Regularization described well but justification weak. | Description/justification not well written. | — |
| 5. Feature & Data Representation | Autoencoders clearly described and justified; correct variables and encoding type identified. | Autoencoders described and justified; correct encoding type missing. | Autoencoders described but justification missing; incorrect encoding. | No justification for use or non-use of autoencoders. |

## Related

- **Parent Course**: [Deep Learning](../courses/c3-deep-learning.md)
- **Follow-on**: [C3 Group Assignment — Evolution of a Deep Learning Technique](c3-deep-learning-group-assignment.md)
- **Concepts**: [Neural Network Architectures](../concepts/neural-network-architectures.md), [Transfer Learning and Fine-Tuning](../concepts/transfer-learning-fine-tuning.md), [Dimensionality Reduction](../concepts/dimensionality-reduction.md), [Model Evaluation and Validation](../concepts/model-evaluation-validation.md)
