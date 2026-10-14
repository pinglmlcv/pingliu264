---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

<style>
.rs { --ink:#1f2a44; --muted:#5b6478; --line:#e6e9f0; --er:#4b4fc9; --er-soft:#eef0ff; --ph:#0e8a83; --ph-soft:#e5f6f4; --amber:#e39a2d; font-size:0.95em; line-height:1.7; color:var(--ink); }
.rs * { box-sizing:border-box; }
.rs-hero { background:linear-gradient(120deg,#3b3fb5 0%,#4b6fd1 45%,#14a098 100%); color:#fff; border-radius:16px; padding:2.2em 2.2em 2em; margin:0.5em 0 2.6em; box-shadow:0 10px 30px rgba(43,58,140,0.18); }
.rs-hero .rs-kicker { text-transform:uppercase; letter-spacing:0.14em; font-size:0.72em; opacity:0.85; margin:0 0 0.6em; }
.rs-hero h2 { color:#fff; border:0; margin:0 0 0.5em; font-size:1.55em; line-height:1.3; padding:0; }
.rs-hero p { margin:0 0 1.3em; opacity:0.95; max-width:42em; }
.rs-jump { display:flex; flex-wrap:wrap; gap:0.7em; }
.rs-jump a { color:#fff !important; text-decoration:none !important; border:1px solid rgba(255,255,255,0.55); background:rgba(255,255,255,0.12); padding:0.45em 1.1em; border-radius:999px; font-size:0.85em; }
.rs-jump a:hover { background:rgba(255,255,255,0.25); }
.rs-h3 { font-size:1.05em; text-transform:uppercase; letter-spacing:0.1em; color:var(--muted); margin:0 0 1.1em; border:0; padding:0; }
.rs-flow { display:flex; align-items:stretch; gap:0.6em; margin:0 0 3em; }
.rs-step { flex:1; background:#fff; border:1px solid var(--line); border-radius:14px; padding:1.2em 1.1em; box-shadow:0 2px 10px rgba(31,42,68,0.05); }
.rs-step .rs-ic { width:2.3em; height:2.3em; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#fff; margin-bottom:0.7em; }
.rs-step b { display:block; font-size:1.02em; margin-bottom:0.25em; }
.rs-step span { color:var(--muted); font-size:0.88em; line-height:1.55; display:block; }
.rs-arrow { display:flex; align-items:center; color:#b4bacb; font-size:1.3em; }
.rs-sec { border-radius:18px; padding:2em 2em 1.6em; margin:0 0 2.8em; border:1px solid var(--line); }
.rs-sec.er { background:linear-gradient(180deg,var(--er-soft) 0%,#fff 220px); border-top:5px solid var(--er); }
.rs-sec.ph { background:linear-gradient(180deg,var(--ph-soft) 0%,#fff 220px); border-top:5px solid var(--ph); }
.rs-head { display:flex; align-items:center; gap:0.9em; margin-bottom:1em; }
.rs-num { font-size:2.2em; font-weight:800; line-height:1; opacity:0.25; }
.er .rs-num, .er .rs-accent { color:var(--er); }
.ph .rs-num, .ph .rs-accent { color:var(--ph); }
.rs-head h2 { margin:0; border:0; padding:0; font-size:1.4em; line-height:1.25; }
.rs-head .rs-tag { display:block; font-size:0.62em; font-weight:600; text-transform:uppercase; letter-spacing:0.12em; margin-bottom:0.35em; }
.rs-lead { margin:0 0 1.6em; max-width:46em; }
.rs-qs { display:grid; grid-template-columns:repeat(3,1fr); gap:0.9em; margin:0 0 2em; }
.rs-q { background:#fff; border-radius:12px; padding:1em 1em 0.9em; border:1px solid var(--line); font-size:0.88em; line-height:1.5; }
.rs-q i { font-size:1.15em; margin-bottom:0.5em; display:block; }
.er .rs-q i { color:var(--er); } .ph .rs-q i { color:var(--ph); }
.rs-fig { margin:0 0 1.8em; background:#fff; border:1px solid var(--line); border-radius:14px; padding:1em; box-shadow:0 4px 18px rgba(31,42,68,0.06); }
.rs-fig img { width:100%; display:block; border-radius:8px; }
.rs-fig figcaption { margin-top:0.8em; font-size:0.82em; color:var(--muted); line-height:1.55; font-family:inherit; }
.rs-fig figcaption b { color:var(--ink); }
.rs-pubs { display:flex; flex-direction:column; gap:0.75em; margin:0.8em 0 0; padding:0; list-style:none; }
.rs-pub { display:flex; gap:1em; align-items:flex-start; background:#fff; border:1px solid var(--line); border-radius:12px; padding:0.85em 1em; margin:0; }
.rs-venue { flex:0 0 7.2em; text-align:center; font-size:0.72em; font-weight:700; color:#fff; border-radius:6px; padding:0.35em 0.3em; letter-spacing:0.03em; line-height:1.3; }
.v-cvpr{background:#2f6fd6;} .v-iclr{background:#7a4cc2;} .v-icml{background:#c2410c;} .v-neurips{background:#7c3aed;} .v-mm{background:#0f766e;} .v-tmlr{background:#475569;} .v-arxiv{background:#b91c1c;} .v-eccv{background:#1d4ed8;} .v-ijcai{background:#a16207;}
.rs-pub .t { font-weight:600; display:block; line-height:1.4; }
.rs-pub .a { color:var(--muted); font-size:0.86em; display:block; margin-top:0.15em; }
.rs-pub .l a { display:inline-block; margin-top:0.35em; font-size:0.78em; padding:0.1em 0.7em; border-radius:999px; border:1px solid currentColor; text-decoration:none; }
.er .rs-pub .l a { color:var(--er); } .ph .rs-pub .l a { color:var(--ph); }
.rs-note { color:var(--muted); font-size:0.85em; margin-top:0.5em; }
@media (max-width: 760px) {
  .rs-hero { padding:1.6em 1.3em; } .rs-sec { padding:1.4em 1.1em; }
  .rs-flow { flex-direction:column; } .rs-arrow { justify-content:center; transform:rotate(90deg); }
  .rs-qs { grid-template-columns:1fr; } .rs-pub { flex-direction:column; gap:0.5em; } .rs-venue { flex:none; align-self:flex-start; padding:0.3em 0.8em; }
}
</style>

<div class="rs">
<div class="rs-hero">
<p class="rs-kicker">Research · University of Nevada, Reno</p>
<h2>Controllable, verifiable, and physically grounded generative AI</h2>
<p>Generative models can now produce realistic images and videos, but we still have limited ability to remove what they should not generate or to make what they generate obey the physical world. Our group develops methods that diagnose what a model has learned, intervene on it selectively, and verify the result.</p>
<div class="rs-jump"><a href="#erasure"><i class="fas fa-eraser"></i>&nbsp; Concept Erasure</a><a href="#physics"><i class="fas fa-atom"></i>&nbsp; Physics-Aware Video Generation</a></div>
</div>

<h3 class="rs-h3">Our approach</h3>
<div class="rs-flow">
<div class="rs-step"><div class="rs-ic" style="background:#4b4fc9"><i class="fas fa-search"></i></div><b>Diagnose</b><span>Locate where a concept or a physical behavior is represented inside the model, across layers and denoising steps.</span></div>
<div class="rs-arrow"><i class="fas fa-chevron-right"></i></div>
<div class="rs-step"><div class="rs-ic" style="background:#3a7bd5"><i class="fas fa-sliders-h"></i></div><b>Intervene</b><span>Edit the model or its sampling with closed-form, training-free, or preference-based updates that change only what is targeted.</span></div>
<div class="rs-arrow"><i class="fas fa-chevron-right"></i></div>
<div class="rs-step"><div class="rs-ic" style="background:#0e8a83"><i class="fas fa-check-double"></i></div><b>Verify</b><span>Test whether the change holds: probe for residual concepts and score physical plausibility at the scene level.</span></div>
</div>

<div class="rs-sec er" id="erasure">
<div class="rs-head"><div class="rs-num">01</div><h2><span class="rs-tag rs-accent">Direction one</span>Concept Erasure and Machine Unlearning</h2></div>
<p class="rs-lead">Text-to-image and text-to-video models can generate content that should be removed after deployment, such as copyrighted styles, specific objects, or violent actions. Concept erasure removes a target concept from a pretrained model while leaving everything else intact. We extend erasure from static concepts in images to motion concepts in videos.</p>
<div class="rs-qs">
<div class="rs-q"><i class="fas fa-calculator"></i>Can erasure be done in closed form or at inference time, without retraining the model?</div>
<div class="rs-q"><i class="fas fa-layer-group"></i>Where inside the network should erasure happen, and how does this differ for motion in video models?</div>
<div class="rs-q"><i class="fas fa-redo-alt"></i>After erasure, how much of the concept can still be recovered, and how do we measure it?</div>
</div>
<figure class="rs-fig"><img src="{{ base_path }}/images/research/dp.jpg" alt="Concept erasure via Double Projections"><figcaption><b>Double Projections (CVPR 2026).</b> Closed-form erasure of "Cassette Player": the target concept disappears while nine other concepts are preserved.</figcaption></figure>
<figure class="rs-fig"><img src="{{ base_path }}/images/research/mute.jpg" alt="Overview of MUTE"><figcaption><b>MUTE (ACM MM 2026).</b> Erasing a motion concept such as "kicking" from a video diffusion transformer at inference time, without retraining and without an external detector.</figcaption></figure>
<h3 class="rs-h3">Representative papers</h3>
<ul class="rs-pubs">
<li class="rs-pub"><span class="rs-venue v-cvpr">CVPR 2026</span><div><span class="t">Closed-Form Concept Erasure via Double Projections</span><span class="a">Chi Zhang, Jingpu Cheng, Zhixian Wang, <b>Ping Liu</b><sup>†</sup></span><span class="l"><a href="https://arxiv.org/abs/2604.10032">arXiv</a></span></div></li>
<li class="rs-pub"><span class="rs-venue v-iclr">ICLR 2026</span><div><span class="t">Machine Unlearning under Retain–Forget Entanglement</span><span class="a">Jingpu Cheng, <b>Ping Liu</b>, Qianxiao Li, Chi Zhang</span></div></li>
<li class="rs-pub"><span class="rs-venue v-icml">ICML 2026</span><div><span class="t">Where Concept Erasure Should Occur: Concept–Layer Alignment in Text-to-Video Diffusion Models</span><span class="a">Yiwei Xie, <b>Ping Liu</b><sup>†</sup>, Zheng Zhang<sup>†</sup></span></div></li>
<li class="rs-pub"><span class="rs-venue v-mm">ACM MM 2026</span><div><span class="t">MUTE: Motion Concept Unlearning in Video Diffusion Models</span><span class="a"><b>Ping Liu</b>, Chi Zhang</span><span class="l"><a href="https://arxiv.org/abs/2609.36832">arXiv</a></span></div></li>
<li class="rs-pub"><span class="rs-venue v-neurips">NeurIPS 2026</span><div><span class="t">DOME: Drift-Adaptive On-Policy Motion Erasure in Video Diffusion Transformers</span><span class="a"><b>Ping Liu</b>, Chi Zhang, Meng Tang</span></div></li>
<li class="rs-pub"><span class="rs-venue v-tmlr">TMLR 2026</span><div><span class="t">ABCDE: Agentic-Based Controlled Dynamic Erasure for Intent-Aware Safety Reasoning</span><span class="a"><b>Ping Liu</b>, Chi Zhang</span></div></li>
<li class="rs-pub"><span class="rs-venue v-arxiv">arXiv 2026</span><div><span class="t">PROBE: Diagnosing Residual Concept Capacity in Erased Text-to-Video Diffusion Models</span><span class="a">Yiwei Xie, Zheng Zhang<sup>†</sup>, <b>Ping Liu</b><sup>†</sup></span><span class="l"><a href="https://arxiv.org/abs/2603.21547">arXiv</a></span></div></li>
</ul>
</div>

<div class="rs-sec ph" id="physics">
<div class="rs-head"><div class="rs-num">02</div><h2><span class="rs-tag rs-accent">Direction two</span>Physically Grounded Text-to-Video Generation</h2></div>
<p class="rs-lead">Current video generators produce visually realistic results that often violate basic physics: objects pass through one another, motion ignores mass and material, and dynamics drift over time. We work on making generated motion physically consistent while keeping it faithful to the prompt.</p>
<div class="rs-qs">
<div class="rs-q"><i class="fas fa-cube"></i>How can a model infer physical properties, such as mass and material, that a single image does not reveal?</div>
<div class="rs-q"><i class="fas fa-balance-scale"></i>How do we align video generators with physical commonsense without sacrificing semantic fidelity?</div>
<div class="rs-q"><i class="fas fa-ruler-combined"></i>How do we measure physical plausibility at the level of individual scenes?</div>
</div>
<figure class="rs-fig"><img src="{{ base_path }}/images/research/magic.jpg" alt="Overview of PhyMAGIC"><figcaption><b>PhyMAGIC (ECCV 2026).</b> Probe videos generated by an image-to-video model let a vision-language model refine low-confidence physical parameters before simulation.</figcaption></figure>
<figure class="rs-fig"><img src="{{ base_path }}/images/research/psdpo.jpg" alt="Comparison between vanilla DPO and PSDPO"><figcaption><b>PSDPO (ACM MM 2026, Oral).</b> Adding semantic feasibility to physical preference optimization preserves prompt semantics and stabilizes preference learning.</figcaption></figure>
<h3 class="rs-h3">Representative papers</h3>
<ul class="rs-pubs">
<li class="rs-pub"><span class="rs-venue v-eccv">ECCV 2026</span><div><span class="t">PhyMAGIC: Physical Motion-Aware Generative Inference with Confidence-Guided VLM</span><span class="a">Siwei Meng, Yawei Luo<sup>†</sup>, <b>Ping Liu</b><sup>†</sup></span><span class="l"><a href="https://mengsiwei.github.io/MAGIC/">Project page</a></span></div></li>
<li class="rs-pub"><span class="rs-venue v-mm">ACM MM 2026<br>Oral</span><div><span class="t">When Physical Preferences Meet Semantic Constraints: Physical and Semantic Direct Preference Optimization for Text-to-Video Generation</span><span class="a">Siwei Meng, Yawei Luo, Shu Zhang, <b>Ping Liu</b><sup>†</sup></span><span class="l"><a href="https://arxiv.org/abs/2607.16947">arXiv</a></span></div></li>
<li class="rs-pub"><span class="rs-venue v-neurips">NeurIPS 2026</span><div><span class="t">PhyMetric: Diagnosing Physical Plausibility in Text-to-Video Generation via Scene-Level QA</span><span class="a">Siwei Meng, Xuerou Cai, Rui Hu, <b>Ping Liu</b><sup>†</sup> · Evaluations and Datasets Track</span><span class="l"><a href="https://mengsiwei.github.io/PhyMetric/">Project page</a></span></div></li>
<li class="rs-pub"><span class="rs-venue v-ijcai">IJCAI 2025</span><div><span class="t">Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC</span><span class="a">Siwei Meng, Yawei Luo<sup>†</sup>, <b>Ping Liu</b><sup>†</sup> · Survey Track</span></div></li>
</ul>
</div>

<p class="rs-note"><sup>†</sup> corresponding or co-corresponding author. The full list is on the <a href="{{ base_path }}/publications/">Publications</a> page.</p>
</div>
