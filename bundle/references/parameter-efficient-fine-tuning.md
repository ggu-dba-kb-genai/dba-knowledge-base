---
type: Reference
resource: https://huggingface.co/docs/transformers/peft
title: Parameter-Efficient Fine-Tuning (PEFT)
description: An advanced method to adapt pretrained models by training only a tiny
  fraction of weights, reducing memory overhead and allowing dynamic adapter hotswapping.
tags:
- PEFT
- fine-tuning
- adapters
- LoRA
- model-serving
- transformers
timestamp: '2026-06-20T06:41:30+00:00'
---

**Parameter-Efficient Fine-Tuning (PEFT)** is an advanced machine learning training methodology that adapts large pre-trained models to specialized downstream tasks by modifying or adding only a tiny fraction of the model's total parameters (often under 1%). Instead of performing full parameter fine-tuning—which requires updating and tracking gradients for billions of parameters—PEFT freezes the base model's weights and introduces lightweight auxiliary modules known as **adapters** (such as Low-Rank Adaptation [LoRA], IA3, or AdaLoRA). This optimization significantly reduces GPU memory overhead, limits storage requirements, and avoids the risk of **catastrophic forgetting**, where a model loses its original generalized capabilities during domain adaptation.

At an engineering level, PEFT enables highly flexible model serving and deployment. Because adapters are small (often only a few megabytes), a single base model can be loaded into memory and shared across multiple tasks. Systems can dynamically swap or enable different task-specific adapters in real time depending on the incoming user request (known as **hotswapping**). Hugging Face's PEFT integration leverages architectural patterns like `PeftAdapterMixin` to manage multiple adapters in memory. For compiled models utilizing `torch.compile`, advanced techniques such as setting a `target_rank` beforehand and calling `enable_peft_hotswap()` allow adapter weights to be swapped in-place without triggering expensive recompilations, enabling ultra-low-latency serving in production environments.

# Citations
1. Hugging Face Documentation. (2025). *Parameter-efficient fine-tuning*. https://huggingface.co/docs/transformers/peft
