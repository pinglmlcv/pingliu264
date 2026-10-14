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
.rs-res { display:grid; grid-template-columns:1fr 1fr; gap:1.1em; margin:0 0 2.4em; }
.rs-card { display:flex; flex-direction:column; background:#fff; border:1px solid var(--line); border-radius:14px; padding:1.3em 1.3em 1.1em; box-shadow:0 4px 18px rgba(31,42,68,0.06); border-left:5px solid var(--c); }
.rs-card .rs-ic { width:2.4em; height:2.4em; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#fff; background:var(--c); margin-bottom:0.8em; }
.rs-card b { font-size:1.02em; line-height:1.35; }
.rs-card span { color:var(--muted); font-size:0.87em; line-height:1.55; margin:0.45em 0 0.9em; flex:1; }
.rs-card .rs-gh { align-self:flex-start; display:inline-flex; align-items:center; gap:0.45em; font-size:0.8em; padding:0.3em 0.9em; border-radius:999px; background:var(--c); color:#fff !important; text-decoration:none !important; }
.rs-card .rs-meta { display:flex; align-items:center; gap:0.7em; flex-wrap:wrap; }
.rs-callout { display:flex; align-items:center; gap:0.8em; background:#fff; border:1px dashed var(--er); border-radius:12px; padding:0.8em 1em; margin:0 0 2em; font-size:0.88em; }
.rs-callout i { color:var(--er); font-size:1.2em; }
.rs-callout a { color:var(--er) !important; font-weight:600; }
@media (max-width: 760px) { .rs-res { grid-template-columns:1fr; } }
.rs-fig.f-dp { background:#eef0ff; border-color:#c9ccf5; border-left:5px solid #4b4fc9; }
.rs-fig.f-mute { background:#f7eefc; border-color:#e3cdf3; border-left:5px solid #8b3fc6; }
.rs-fig.f-magic { background:#e6f6f4; border-color:#bfe7e2; border-left:5px solid #0e8a83; }
.rs-fig.f-psdpo { background:#fff4e2; border-color:#f6dcae; border-left:5px solid #d9822b; }
.rs-fig.f-dp figcaption b { color:#3b3fb5; } .rs-fig.f-mute figcaption b { color:#7a2fb5; }
.rs-fig.f-magic figcaption b { color:#0b6f69; } .rs-fig.f-psdpo figcaption b { color:#b5651d; }
.rs-fig img { background:#fff; }
.rs-fig figcaption { color:#4a5368; }
.rs-sec.df { background:linear-gradient(180deg,#fdf2f6 0%,#fff 220px); border-top:5px solid #be185d; }
.df .rs-num, .df .rs-accent { color:#be185d; }
.df .rs-q i { color:#be185d; } .df .rs-pub .l a { color:#be185d; }
.rs-callout.ph-c { border-color:#0e8a83; } .rs-callout.ph-c i, .rs-callout.ph-c a { color:#0e8a83 !important; }
.rs-callout.df-c { border-color:#be185d; } .rs-callout.df-c i, .rs-callout.df-c a { color:#be185d !important; }
.rs-fig.f-deepfake { background:#fdf2f6; border-color:#f6c9d9; border-left:5px solid #be185d; }
.rs-fig.f-npr { background:#f3efff; border-color:#ddd2fb; border-left:5px solid #6d28d9; }
.rs-fig.f-deepfake figcaption b { color:#9d174d; } .rs-fig.f-npr figcaption b { color:#5b21b6; }
.v-aaai{background:#b45309;} .v-wifs{background:#64748b;} .v-mmw{background:#0f766e;}
.rs-res { grid-template-columns:repeat(3,1fr); }
@media (max-width: 900px) { .rs-res { grid-template-columns:1fr; } }
.rs-other { display:grid; grid-template-columns:1fr 1fr; gap:1.1em; margin:0 0 2.8em; }
.rs-ob { background:#f8fafc; border:1px solid var(--line); border-top:4px solid var(--k); border-radius:16px; padding:1.3em 1.3em 1em; }
.rs-ob h3 { margin:0 0 0.2em; padding:0; border:0; font-size:1.12em; color:var(--ink); display:flex; align-items:center; gap:0.5em; }
.rs-ob h3 i { color:var(--k); }
.rs-ob .sub { font-size:0.72em; text-transform:uppercase; letter-spacing:0.12em; color:var(--k); font-weight:700; }
.rs-ob p { font-size:0.9em; color:var(--muted); margin:0.6em 0 0.9em; }
.rs-ob ul { list-style:none; margin:0; padding:0; }
.rs-ob li { font-size:0.86em; line-height:1.45; padding:0.55em 0; border-top:1px dashed var(--line); margin:0; }
.rs-ob li .vn { display:inline-block; font-size:0.78em; font-weight:700; color:#fff; background:var(--k); border-radius:5px; padding:0.05em 0.5em; margin-right:0.45em; }
.rs-ob li .tt { font-weight:600; color:var(--ink); }
.rs-ob li .au { display:block; color:var(--muted); font-size:0.95em; }
.rs-ob li a { font-size:0.9em; }
@media (max-width: 900px) { .rs-other { grid-template-columns:1fr; } }
</style>

<div class="rs">
<div class="rs-hero">
<p class="rs-kicker">Research · University of Nevada, Reno</p>
<h2>Controllable, verifiable, and physically grounded generative AI</h2>
<p>Generative models can now produce realistic images and videos, but we still have limited ability to remove what they should not generate or to make what they generate obey the physical world, and forged media are increasingly hard to tell apart from real content. Our group develops methods that diagnose what a model has learned, intervene on it selectively, and verify the result.</p>
<div class="rs-jump"><a href="#erasure"><i class="fas fa-eraser"></i>&nbsp; Concept Erasure</a><a href="#physics"><i class="fas fa-atom"></i>&nbsp; Physics-Aware Video Generation</a><a href="#deepfake"><i class="fas fa-user-secret"></i>&nbsp; Deepfake Detection</a></div>
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
<div class="rs-callout"><i class="fab fa-github"></i><div>We maintain <a href="https://github.com/pinglmlcv/Awesome-Concept-Erasure">Awesome-Concept-Erasure</a>, a curated and continuously updated list of papers on concept erasure and unlearning in generative models.</div></div>
<figure class="rs-fig f-dp"><img src="{{ base_path }}/images/research/dp.jpg" alt="Concept erasure via Double Projections"><figcaption><b>Double Projections (CVPR 2026).</b> Closed-form erasure of "Cassette Player": the target concept disappears while nine other concepts are preserved.</figcaption></figure>
<figure class="rs-fig f-mute"><img src="{{ base_path }}/images/research/mute.jpg" alt="Overview of MUTE"><figcaption><b>MUTE (ACM MM 2026).</b> Erasing a motion concept such as "kicking" from a video diffusion transformer at inference time, without retraining and without an external detector.</figcaption></figure>
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
<div class="rs-callout ph-c"><i class="fab fa-github"></i><div>Our group maintains <a href="https://github.com/mengsiwei/Awesome-Physical-AIGC-lists">Awesome-Physical-AIGC-lists</a>, a curated list of physics-aware AIGC works, companion to our IJCAI 2025 survey.</div></div>
<figure class="rs-fig f-magic"><img src="{{ base_path }}/images/research/magic.jpg" alt="Overview of PhyMAGIC"><figcaption><b>PhyMAGIC (ECCV 2026).</b> Probe videos generated by an image-to-video model let a vision-language model refine low-confidence physical parameters before simulation.</figcaption></figure>
<figure class="rs-fig f-psdpo"><img src="{{ base_path }}/images/research/psdpo.jpg" alt="Comparison between vanilla DPO and PSDPO"><figcaption><b>PSDPO (ACM MM 2026, Oral).</b> Adding semantic feasibility to physical preference optimization preserves prompt semantics and stabilizes preference learning.</figcaption></figure>
<h3 class="rs-h3">Representative papers</h3>
<ul class="rs-pubs">
<li class="rs-pub"><span class="rs-venue v-eccv">ECCV 2026</span><div><span class="t">PhyMAGIC: Physical Motion-Aware Generative Inference with Confidence-Guided VLM</span><span class="a">Siwei Meng, Yawei Luo<sup>†</sup>, <b>Ping Liu</b><sup>†</sup></span><span class="l"><a href="https://mengsiwei.github.io/MAGIC/">Project page</a></span></div></li>
<li class="rs-pub"><span class="rs-venue v-mm">ACM MM 2026<br>Oral</span><div><span class="t">When Physical Preferences Meet Semantic Constraints: Physical and Semantic Direct Preference Optimization for Text-to-Video Generation</span><span class="a">Siwei Meng, Yawei Luo, Shu Zhang, <b>Ping Liu</b><sup>†</sup></span><span class="l"><a href="https://arxiv.org/abs/2607.16947">arXiv</a></span></div></li>
<li class="rs-pub"><span class="rs-venue v-neurips">NeurIPS 2026</span><div><span class="t">PhyMetric: Diagnosing Physical Plausibility in Text-to-Video Generation via Scene-Level QA</span><span class="a">Siwei Meng, Xuerou Cai, Rui Hu, <b>Ping Liu</b><sup>†</sup> · Evaluations and Datasets Track</span><span class="l"><a href="https://mengsiwei.github.io/PhyMetric/">Project page</a></span></div></li>
<li class="rs-pub"><span class="rs-venue v-ijcai">IJCAI 2025</span><div><span class="t">Grounding Creativity in Physics: A Brief Survey of Physical Priors in AIGC</span><span class="a">Siwei Meng, Yawei Luo<sup>†</sup>, <b>Ping Liu</b><sup>†</sup> · Survey Track</span><span class="l"><a href="https://arxiv.org/abs/2502.07007">arXiv</a></span></div></li>
</ul>
</div>

<div class="rs-sec df" id="deepfake">
<div class="rs-head"><div class="rs-num">03</div><h2><span class="rs-tag rs-accent">Direction three</span>Deepfake Detection and Media Forensics</h2></div>
<p class="rs-lead">The same generative models also make it easy to forge faces, voices, and text-guided edits. We build detectors that generalize to forgeries from generators never seen during training, by targeting the traces that generators leave behind, and we study how detection is moving from single-modal to multi-modal settings.</p>
<div class="rs-qs">
<div class="rs-q"><i class="fas fa-random"></i>How can a detector recognize forgeries from generators it has never seen during training?</div>
<div class="rs-q"><i class="fas fa-wave-square"></i>Which traces do generators leave behind, in the frequency domain and in their up-sampling layers?</div>
<div class="rs-q"><i class="fas fa-photo-video"></i>How should detection extend from images to audio-visual and text-visual deepfakes?</div>
</div>
<div class="rs-callout df-c"><i class="fab fa-github"></i><div>Our group maintains <a href="https://github.com/qiqitao77/Awesome-Comprehensive-Deepfake-Detection">Awesome-Comprehensive-Deepfake-Detection</a>, a curated list of deepfake detection papers and datasets, companion to our survey.</div></div>
<figure class="rs-fig f-deepfake"><img src="{{ base_path }}/images/research/deepfake.jpg" alt="Overview of deepfake detection research"><figcaption><b>Overview.</b> Forgeries from face swapping, GAN and diffusion synthesis, audio-visual and text-guided manipulation leave traces in spatial, frequency, up-sampling, and cross-modal cues, which detectors exploit to decide real or fake.</figcaption></figure>
<figure class="rs-fig f-npr"><img src="{{ base_path }}/images/research/npr.jpg" alt="Neighboring Pixel Relationships for deepfake detection"><figcaption><b>Neighboring Pixel Relationships (CVPR 2024).</b> Up-sampling layers in GAN and diffusion generators leave local correlations between neighboring pixels, which a classifier uses to detect images from unseen generators.</figcaption></figure>
<h3 class="rs-h3">Representative papers</h3>
<ul class="rs-pubs">
<li class="rs-pub"><span class="rs-venue v-wifs">WIFS 2025</span><div><span class="t">ADD: An Automated Neural Architecture Search Baseline for Deepfake Detection</span><span class="a"><b>Ping Liu</b>, Yuewei Lin, Jingen Liu, Yunchao Wei, Joey Tianyi Zhou</span></div></li>
<li class="rs-pub"><span class="rs-venue v-mmw">ACM MM 2024<br>Workshop</span><div><span class="t">Robust Deepfake Detection by Addressing Generalization and Trustworthiness Challenges: A Short Survey</span><span class="a"><b>Ping Liu</b>, Qiqi Tao, Joey Tianyi Zhou · Best Paper Award (Survey)</span></div></li>
<li class="rs-pub"><span class="rs-venue v-cvpr">CVPR 2024</span><div><span class="t">Rethinking the Up-Sampling Operations in CNN-based Generative Network for Generalizable Deepfake Detection</span><span class="a">Chuangchuang Tan, Yao Zhao, Shikui Wei, Guanghua Gu, <b>Ping Liu</b>, Yunchao Wei</span><span class="l"><a href="https://openaccess.thecvf.com/content/CVPR2024/html/Tan_Rethinking_the_Up-Sampling_Operations_in_CNN-based_Generative_Network_for_Generalizable_CVPR_2024_paper.html">Paper</a></span></div></li>
<li class="rs-pub"><span class="rs-venue v-aaai">AAAI 2024</span><div><span class="t">Frequency-Aware Deepfake Detection: Improving Generalizability through Frequency Space Domain Learning</span><span class="a">Chuangchuang Tan, Yao Zhao, Shikui Wei, Guanghua Gu, <b>Ping Liu</b>, Yunchao Wei</span></div></li>
<li class="rs-pub"><span class="rs-venue v-arxiv">arXiv 2024</span><div><span class="t">Evolving from Single-modal to Multi-modal Facial Deepfake Detection: A Survey</span><span class="a"><b>Ping Liu</b>, Qiqi Tao, Joey Tianyi Zhou</span><span class="l"><a href="https://arxiv.org/abs/2406.06965">arXiv</a></span></div></li>
</ul>
</div>

<h3 class="rs-h3">Other directions</h3>
<div class="rs-other">
<div class="rs-ob" style="--k:#475569">
<span class="sub">Efficient learning</span>
<h3><i class="fas fa-compress-arrows-alt"></i>Dataset Distillation</h3>
<p>We also study dataset distillation, which compresses a large training set into a small synthetic one that preserves what models learn from it, with attention to efficiency, robustness, and pre-trained vision models.</p>
<ul>
<li><span class="vn">NeurIPS 2026</span><span class="tt">Closed-Form Linear-Probe Dataset Distillation for Pre-trained Vision Models</span> <a href="https://arxiv.org/abs/2605.07194">[arXiv]</a><span class="au">Bincheng Peng, Guang Li, <b>Ping Liu</b>, Takahiro Ogawa, Miki Haseyama</span></li>
<li><span class="vn">ICLR 2025</span><span class="tt">Breaking Class Barriers: Efficient Dataset Distillation via Inter-Class Feature Compensator</span><span class="au">Xin Zhang, Jiawei Du, <b>Ping Liu</b>, Joey Tianyi Zhou</span></li>
<li><span class="vn">TIP 2025</span><span class="tt">DD-RobustBench: An Adversarial Robustness Benchmark for Dataset Distillation</span><span class="au">Yifan Wu, Jiawei Du<sup>♠</sup>, <b>Ping Liu</b><sup>♠</sup>, Yuewei Lin, Wenqing Chen, Wei Xu</span></li>
<li><span class="vn">ICLR 2023</span><span class="tt">Meta Knowledge Condensation for Federated Learning</span><span class="au"><b>Ping Liu</b><sup>♠</sup>, Xin Yu<sup>♠</sup>, Joey Tianyi Zhou</span></li>
</ul>
</div>
<div class="rs-ob" style="--k:#8b5e34">
<span class="sub">Earlier work</span>
<h3><i class="fas fa-smile"></i>Facial Expression Analysis</h3>
<p>Earlier work, beginning with Ping Liu's Ph.D. research, developed deep and sparse representation methods for facial expression recognition and facial action analysis.</p>
<ul>
<li><span class="vn">CVPR 2014</span><span class="tt">Facial Expression Recognition via a Boosted Deep Belief Network</span><span class="au"><b>Ping Liu</b><sup>♠</sup>, Shizhong Han<sup>♠</sup>, Zibo Meng, Yan Tong</span></li>
<li><span class="vn">ECCV 2014</span><span class="tt">Feature Disentangling Machine: A Novel Approach of Feature Selection and Disentangling in Facial Expression Analysis</span><span class="au"><b>Ping Liu</b>, Joey Tianyi Zhou, Ivor Tsang, Zibo Meng, Shizhong Han, Yan Tong</span></li>
<li><span class="vn">FG 2017</span><span class="tt">Identity-Aware Convolutional Neural Network for Facial Expression Recognition</span><span class="au">Zibo Meng<sup>♠</sup>, <b>Ping Liu</b><sup>♠</sup>, Jie Cai, Shizhong Han, Yan Tong</span></li>
<li><span class="vn">TCYB 2021</span><span class="tt">Point Adversarial Self Mining: A Simple Method for Facial Expression Recognition</span><span class="au"><b>Ping Liu</b>, Yuewei Lin, Zibo Meng, Lu Lu, Weihong Deng, Joey Tianyi Zhou, Yi Yang</span></li>
</ul>
</div>
</div>

<h3 class="rs-h3">Open resources</h3>
<div class="rs-res">
<div class="rs-card" style="--c:#4b4fc9"><div class="rs-ic"><i class="fas fa-eraser"></i></div><b>Awesome-Concept-Erasure</b><span>A curated list of papers on concept erasure and machine unlearning for text-to-image and text-to-video generative models, maintained by our group.</span><div class="rs-meta"><a class="rs-gh" href="https://github.com/pinglmlcv/Awesome-Concept-Erasure"><i class="fab fa-github"></i> GitHub</a></div></div>
<div class="rs-card" style="--c:#0e8a83"><div class="rs-ic"><i class="fas fa-atom"></i></div><b>Awesome-Physical-AIGC-lists</b><span>A curated list of physics-aware AIGC works, companion to our IJCAI 2025 survey (<a href="https://arxiv.org/abs/2502.07007">arXiv:2502.07007</a>). Maintained by our group.</span><div class="rs-meta"><a class="rs-gh" href="https://github.com/mengsiwei/Awesome-Physical-AIGC-lists"><i class="fab fa-github"></i> GitHub</a><img src="https://img.shields.io/github/stars/mengsiwei/Awesome-Physical-AIGC-lists?style=social" alt="GitHub stars"></div></div>
<div class="rs-card" style="--c:#be185d"><div class="rs-ic"><i class="fas fa-user-secret"></i></div><b>Awesome-Comprehensive-Deepfake-Detection</b><span>A curated list of deepfake detection papers and datasets, the companion repository to our survey on facial deepfake detection (<a href="https://arxiv.org/abs/2406.06965">arXiv:2406.06965</a>). Maintained by our group.</span><div class="rs-meta"><a class="rs-gh" href="https://github.com/qiqitao77/Awesome-Comprehensive-Deepfake-Detection"><i class="fab fa-github"></i> GitHub</a><img src="https://img.shields.io/github/stars/qiqitao77/Awesome-Comprehensive-Deepfake-Detection?style=social" alt="GitHub stars"></div></div>
</div>

<p class="rs-note"><sup>†</sup> corresponding or co-corresponding author; <sup>♠</sup> equal contribution. The full list is on the <a href="{{ base_path }}/publications/">Publications</a> page.</p>
</div>
