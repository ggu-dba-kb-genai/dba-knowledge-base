---
type: Session
resource: https://www.youtube.com/watch?v=rHTJiADZnYw
title: 'Session 14: Generative AI (VAEs & GANs) & Introduction to Reinforcement Learning'
description: An introduction to generative image modeling using Variational Autoencoders
  (VAEs) and Generative Adversarial Networks (GANs), followed by foundational concepts
  of Reinforcement Learning (RL).
tags:
- generative-modeling
- variational-autoencoders
- generative-adversarial-networks
- reinforcement-learning
- q-learning
- deep-q-networks
timestamp: '2026-01-10'
---

This session represents the final lecture of the Deep Learning course, providing a foundational introduction to Generative AI (focusing on image generation) and Reinforcement Learning. 

In the first half of the lecture, the discussion centers on **[Generative Modeling](../concepts/generative-modeling.md)** in the **[Computer Vision](../concepts/computer-vision.md)** domain. Unlike discriminative models that identify boundaries to classify or cluster data, generative models capture the underlying probability distribution of high-dimensional datasets to synthesize entirely new samples. The professor illustrates this by explaining how images are flattened into vectors (e.g., $28 \times 28 = 784$ features for MNIST; $32 \times 32 \times 3 = 3072$ features for CIFAR-10) and mapped to a multi-dimensional feature space where a specific class of images (like dogs) occupies a specific region. Generating a new image is equivalent to sampling a random vector from this region and passing it through a decoder. Two primary generative architectures are compared: **Variational Autoencoders (VAEs)** (explicit probability density modeling) and **Generative Adversarial Networks (GANs)** (implicit probability density modeling).

To explain VAEs, the professor references biological face perception research. Humans do not store representations of every individual face they see; instead, the brain constructs an "average face" (or eigenface) and encodes individual faces as deviations from this average. Psychophysical studies show that these cognitive representations shift when individuals transition between monocultural and multicultural environments. Similarly, a VAE's encoder maps input images to a latent space parameterizing a probability distribution (outputting a mean $\mu$ and a standard deviation $\sigma$ for each latent dimension), samples from this distribution by incorporating a standard normal error ($\epsilon \sim N(0, I)$), and passes the sample to the decoder to reconstruct the original image. 

GANs utilize an adversarial game-theoretic framework. The professor uses the analogy of an art critic (the discriminator) and an art forger (the generator). The generator starts with a random noise vector ($z \sim p_z(z)$) and tries to generate realistic images without initially knowing what the real target images look like. The discriminator ($D$) is trained to distinguish between real images ($x \sim p_{\text{data}}(x)$) and fakes ($G(z)$). The adversarial relationship is optimized via the minimax objective:
$$\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{\text{data}}(x)}[\log D(x)] + \mathbb{E}_{z \sim p_z(z)}[\log (1 - D(G(z)))]$$
Backpropagation iteratively updates the discriminator to maximize classification accuracy, and then updates the generator to fool the discriminator. Over time, the generator learns to produce highly realistic images.

In the second half, the lecture introduces **Reinforcement Learning (RL)**, which is framed as an optimization technique rather than standard **[Supervised Learning Foundations](../concepts/supervised-learning-foundations.md)** or unsupervised learning. Drawing analogies to a baby learning to walk, the professor outlines the core agent-environment interaction loop: an **agent** observes a **state** ($s_t$), takes an **action** ($a_t$), receives a **reward** ($r_t$), and transitions to a new state ($s_{t+1}$). Using Neo from *The Matrix* as an example, the professor demonstrates how agents must look beyond immediate consequences to optimize cumulative discounted future rewards ($R_t$):
$$R_t = \sum_{i=t}^{\infty} \gamma^{i-t} r_i$$
A discount factor $\gamma \in (0, 1)$ is applied to prioritize immediate outcomes over distant ones, analogous to exponential smoothing in **[Time Series and Forecasting](../concepts/time-series-forecasting.md)**. The expected discounted future reward of an action in a given state is modeled via the **Q-Function**:
$$Q(s_t, a_t) = \mathbb{E}[R_t \mid s_t, a_t]$$
The agent's **policy** ($\pi$) dictates taking the action that maximizes this Q-value:
$$\pi(s_t) = \arg\max_{a_t} Q(s_t, a_t)$$
The lecture traces the progression of RL from brute-force game-tree search (like IBM's Deep Blue in chess) to modern Deep Reinforcement Learning (like DeepMind's AlphaGo) which use deep **[Neural Network Architectures](../concepts/neural-network-architectures.md)** to generalize across complex states. Practical applications include data packet routing across cellular networks (optimizing cell-tower transit times dynamically) and continuous learning in autonomous rovers (e.g., Martian or Lunar rovers adapting motion policies to different gravities).

The session concludes with an interactive Q&A discussing assignment extensions (Assignment 1 deadline extended to January 13, 2026, at 23:59 IST), the role of business leaders in managing technical AI teams, the upcoming course sequence (Pre-trained GenAI, AI Project Design & Execution, and Responsible AI), and the inclusion of **Liquid Neural Networks** (continuous learning systems that adapt on the go without separate pre/post training phases) as an approved group assignment topic.

# Key Concepts

- **[Generative Modeling](../concepts/generative-modeling.md)** — Unsupervised learning frameworks that estimate the probability distribution of high-dimensional data to synthesize novel, high-fidelity synthetic samples.
- **Variational Autoencoders (VAEs)** — An explicit generative approach that represents input data as a continuous latent distribution characterized by learned means ($\mu$) and standard deviations ($\sigma$) before decoding, drawing on cognitive analogies of human face perception and eigenface representation.
- **Generative Adversarial Networks (GANs)** — An implicit generative approach framing image generation as an adversarial minimax game between a generator producing synthetic samples and a discriminator classifying them as real or fake.
- **Reinforcement Learning (RL)** — An optimization framework where an agent learns an optimal policy of actions to maximize discounted future cumulative rewards within a dynamic environment.
- **Q-Function and Policy** — The Q-function represents the expected cumulative future reward of taking a specific action from a given state. The policy defines the action-selection rule ($\pi$) that maximizes the Q-value.
- **[Agentic AI and Autonomous Systems](../concepts/agentic-ai-autonomous-systems.md)** — Practical implementations of RL and continuous learning in autonomous robots (Boston Dynamics), vehicles (Tesla, Waymo), cellular network routing optimization, and celestial rovers navigating variable terrains.
- **[Neural Network Architectures](../concepts/neural-network-architectures.md)** — The structural design of networks utilized in both generative networks (VAEs, GANs) and deep Q-learning (Deep RL) to map high-dimensional states to optimal control values or image pixels.
- **[Computer Vision](../concepts/computer-vision.md)** — The domain governing the processing of multi-dimensional arrays (like MNIST or CIFAR-10) converted into low-dimensional representations for classification or generative synthesis.

# Topics Covered

- **Discriminative vs. Generative Paradigms**: Understanding data structure for classification/regression vs. learning distributions to synthesize new data.
- **Image Vectorization**: Flattening 2D/3D images (MNIST and CIFAR-10 datasets) and mapping features into multidimensional spaces.
- **Variational Autoencoders (VAEs)**: Mechanistic breakdown of probabilistic encoding, latent parameter estimation ($\mu$ and $\sigma$), normal distribution sampling, and biological face perception/eigenface cognitive shift analogies.
- **Generative Adversarial Networks (GANs)**: Critic-forger analogy, minimax mathematical formulation, iterative backpropagation loops for optimizing discriminative and generative weights, and feature space overlaps (e.g., dog faces vs. chocolate chip cookies).
- **Reinforcement Learning Foundations**: Definitions of Agent, Environment, State ($s_t$), Action ($a_t$), and Reward ($r_t$).
- **Discounting Future Rewards**: Mathematical integration of the discount factor ($\gamma$) to prioritize near-term feedback over distant horizons.
- **The Q-Function & Action Selection**: Calculating expected future rewards and formulating policies based on Q-value maximization.
- **Brute-Force vs. Deep RL**: Contrasting Deep Blue's algorithmic combinatorics in chess with AlphaGo's and Atari-playing agents' deep neural representation learning.
- **Continuous Learning & Generalization**: Exploring Mars/Lunar rover navigation constraints under variable gravities.
- **Administrative & Career Alignment Q&A**: Setting expectations for business-technical collaboration, details on upcoming strategic courses (AI Project Design), and discussion on Liquid Neural Networks.

# Materials

- **Slides**: 
  - `20260110_DL_C8S1_GAN.pdf`
  - `20260110_DL_C8S1_Reinforcement-Learning.pdf`
- **Chat**: Present (student discussions regarding chess engines, assignment deadline extensions, business expectations, and Liquid Neural Network applications).
- **Recording**: `https://www.youtube.com/watch?v=rHTJiADZnYw`

# Related

- Part of the **[Deep Learning](../courses/c3-deep-learning.md)** course.
- Sibling Sessions:
  - **[Session 13](c3-deep-learning-session-13.md)** (2026-01-04)
  - **[Session 15](c3-deep-learning-session-15.md)** (2026-01-11)

# Citations

1. Lecture Video Recording: `https://www.youtube.com/watch?v=rHTJiADZnYw`
2. Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., & Bengio, Y. (2014). *Generative Adversarial Nets*. Advances in Neural Information Processing Systems (NeurIPS).
3. Kingma, D. P., & Welling, M. (2013). *Auto-Encoding Variational Bayes*. arXiv preprint arXiv:1312.6114.
4. Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press.
