---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

My group develops methods to diagnose, control, and verify what generative models produce. Our current work follows two directions.

Concept Erasure and Machine Unlearning
======

Text-to-image and text-to-video models can generate content that should be removed after deployment, such as copyrighted styles, specific objects, or violent actions. Concept erasure removes a target concept from a pretrained model while leaving everything else intact. We study erasure methods that are closed-form or training-free, where inside the model erasure should take place, how to extend erasure from static concepts in images to motion concepts in videos, and how to diagnose whether an erased concept can still be recovered.

<figure>
  <img src="{{ base_path }}/images/research/dp.jpg" alt="Concept erasure via Double Projections on Stable Diffusion">
  <figcaption>Closed-form erasure of "Cassette Player" by Double Projections (CVPR 2026). The target concept is removed while the other nine concepts are preserved.</figcaption>
</figure>

<figure>
  <img src="{{ base_path }}/images/research/mute.jpg" alt="Overview of MUTE for motion concept unlearning">
  <figcaption>MUTE (ACM MM 2026) erases a motion concept such as "kicking" from a video diffusion transformer at inference time, without retraining and without an external detector.</figcaption>
</figure>

**Representative papers**

* Chi Zhang, Jingpu Cheng, Zhixian Wang, **Ping Liu**<sup>†</sup>. "Closed-Form Concept Erasure via Double Projections". *CVPR 2026*. [[arXiv](https://arxiv.org/abs/2604.10032)]
* Jingpu Cheng, **Ping Liu**, Qianxiao Li, Chi Zhang. "Machine Unlearning under Retain–Forget Entanglement". *ICLR 2026*.
* Yiwei Xie, **Ping Liu**<sup>†</sup>, Zheng Zhang<sup>†</sup>. "Where Concept Erasure Should Occur: Concept–Layer Alignment in Text-to-Video Diffusion Models". *ICML 2026*.
* **Ping Liu**, Chi Zhang. "MUTE: Motion Concept Unlearning in Video Diffusion Models". *ACM MM 2026*. [[arXiv](https://arxiv.org/abs/2609.36832)]
* **Ping Liu**, Chi Zhang, Meng Tang. "DOME: Drift-Adaptive On-Policy Motion Erasure in Video Diffusion Transformers". *NeurIPS 2026*.
* **Ping Liu**, Chi Zhang. "ABCDE: Agentic-Based Controlled Dynamic Erasure for Intent-Aware Safety Reasoning". *Transactions on Machine Learning Research*, 2026.
* Yiwei Xie, Zheng Zhang<sup>†</sup>, **Ping Liu**<sup>†</sup>. "PROBE: Diagnosing Residual Concept Capacity in Erased Text-to-Video Diffusion Models". [[arXiv](https://arxiv.org/abs/2603.21547)]

Physically Grounded Text-to-Video Generation
======

Current video generators produce visually realistic results that often violate basic physics: objects pass through one another, motion ignores mass and material, and dynamics drift over time. We study how to infer physical properties that a single image does not reveal, how to align video generators with physical commonsense without sacrificing semantic fidelity to the prompt, and how to measure physical plausibility at the level of individual scenes.

<figure>
  <img src="{{ base_path }}/images/research/magic.jpg" alt="Overview of PhyMAGIC">
  <figcaption>PhyMAGIC (ECCV 2026) generates probe videos with an image-to-video model and uses a vision-language model to refine low-confidence physical parameters before simulation.</figcaption>
</figure>

<figure>
  <img src="{{ base_path }}/images/research/psdpo.jpg" alt="Comparison between vanilla DPO and PSDPO">
  <figcaption>PSDPO (ACM MM 2026, Oral) incorporates semantic feasibility into physical preference optimization, which preserves prompt semantics and stabilizes preference learning.</figcaption>
</figure>

**Representative papers**

* Siwei Meng, Yawei Luo<sup>†</sup>, **Ping Liu**<sup>†</sup>. "PhyMAGIC: Physical Motion-Aware Generative Inference with Confidence-Guided LLM". *ECCV 2026*. [[Project page](https://mengsiwei.github.io/MAGIC/)]
* Siwei Meng, Yawei Luo, Shu Zhang, **Ping Liu**<sup>†</sup>. "When Physical Preferences Meet Semantic Constraints: Physical and Semantic Direct Preference Optimization for Text-to-Video Generation". *ACM MM 2026 (Oral)*. [[arXiv](https://arxiv.org/abs/2607.16947)]
* Siwei Meng, Xuerou Cai, Rui Hu, **Ping Liu**<sup>†</sup>. "PhyMetric: Diagnosing Physical Plausibility in Text-to-Video Generation via Scene-Level QA". *NeurIPS 2026, Evaluations and Datasets Track*.
* Siwei Meng, Yawei Luo<sup>†</sup>, **Ping Liu**<sup>†</sup>. "Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC". *IJCAI 2025, Survey Track*.

<sup>†</sup> corresponding or co-corresponding author. The full list is on the [Publications]({{ base_path }}/publications/) page.
