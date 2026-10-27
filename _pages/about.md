---
layout: archive
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% include base_path %}

<style>
.hm { --ink:#1f2a44; --muted:#5b6478; --line:#e6e9f0; line-height:1.65; color:var(--ink); }
.hm * { box-sizing:border-box; }
.hm-hero { background:linear-gradient(120deg,#3b3fb5 0%,#4b6fd1 45%,#14a098 100%); color:#fff; border-radius:16px; padding:2em 2.2em 1.8em; margin:0.3em 0 2.4em; box-shadow:0 10px 30px rgba(43,58,140,0.18); }
.hm-hero h1 { color:#fff; margin:0 0 0.15em; padding:0; border:0; font-size:2.1em; line-height:1.15; }
.hm-hero .role { font-size:1.02em; opacity:0.95; margin:0 0 0.9em; }
.hm-hero .tag { font-size:0.98em; opacity:0.95; margin:0 0 1.2em; max-width:40em; font-style:italic; }
.hm-btns { display:flex; flex-wrap:wrap; gap:0.6em; }
.hm-btns a { color:#fff !important; text-decoration:none !important; border:1px solid rgba(255,255,255,0.55); background:rgba(255,255,255,0.12); padding:0.4em 1.05em; border-radius:999px; font-size:0.82em; }
.hm-btns a:hover { background:rgba(255,255,255,0.25); }
.hm-h { display:flex; align-items:center; gap:0.7em; margin:0 0 1em; }
.hm-h .ic { width:2.2em; height:2.2em; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#fff; flex:none; }
.hm-h h2 { margin:0; padding:0; border:0; font-size:1.3em; }
.hm-sec { margin:0 0 2.6em; }
.hm-about { background:#fff; border:1px solid var(--line); border-radius:16px; padding:1.3em 1.5em 0.4em; box-shadow:0 4px 16px rgba(31,42,68,0.05); }
.hm-about p { margin:0 0 0.9em; }
.hm-dirs { display:grid; grid-template-columns:repeat(3,1fr); gap:1em; margin:0 0 1em; }
.hm-dir { display:block; background:var(--bg); border:1px solid var(--line); border-top:4px solid var(--c); border-radius:14px; padding:1.1em 1.1em 1em; color:var(--ink) !important; text-decoration:none !important; transition:transform .15s, box-shadow .15s; }
.hm-dir:hover { transform:translateY(-2px); box-shadow:0 8px 20px rgba(31,42,68,0.1); }
.hm-dir i { color:var(--c); font-size:1.3em; display:block; margin-bottom:0.5em; }
.hm-dir b { display:block; line-height:1.3; margin-bottom:0.35em; }
.hm-dir span { font-size:0.85em; color:var(--muted); line-height:1.5; display:block; }
.hm-note { font-size:0.88em; color:var(--muted); margin:0; }
.hm-note a { font-weight:600; }
.hm-news { list-style:none; margin:0; padding:0; border-left:2px solid #dfe3ee; }
.hm-n { position:relative; display:flex; gap:0.8em; align-items:baseline; padding:0.55em 0 0.55em 1.2em; margin:0; }
.hm-n:before { content:""; position:absolute; left:-0.42em; top:1.05em; width:0.7em; height:0.7em; border-radius:50%; background:#fff; border:2px solid #9aa3c7; }
.hm-d { flex:0 0 5.2em; font-size:0.82em; font-weight:700; color:#4b4fc9; white-space:nowrap; }
.hm-k { flex:0 0 5.6em; text-align:center; font-size:0.66em; font-weight:700; color:#fff; border-radius:5px; padding:0.12em 0.5em; letter-spacing:0.04em; text-transform:uppercase; position:relative; top:-1px; }
.hm-t { font-size:0.92em; line-height:1.5; }
.hm-ln { display:inline-block; margin-left:0.3em; font-size:0.78em; padding:0 0.6em; border-radius:999px; border:1px solid #4b4fc9; color:#4b4fc9 !important; text-decoration:none !important; }
.hm-more { display:none; }
.hm-news.open .hm-more { display:flex; }
.hm-toggle { margin:0.9em 0 0 1.2em; border:1px solid var(--line); background:#f3f5f9; color:var(--ink); border-radius:999px; padding:0.35em 1.1em; font-size:0.82em; cursor:pointer; }
@media (max-width: 900px) { .hm-dirs { grid-template-columns:1fr; } }
@media (max-width: 760px) { .hm-hero { padding:1.5em 1.3em; } .hm-n { flex-wrap:wrap; gap:0.4em; } .hm-d { flex:none; } .hm-t { flex-basis:100%; } }
.hm-open { background:linear-gradient(135deg,#fff8ec 0%,#fff 70%); border:1px solid #f3dcb5; border-left:5px solid #d9822b; border-radius:14px; padding:1.1em 1.3em; }
.hm-open ul { list-style:none; margin:0; padding:0; }
.hm-open li { display:flex; gap:0.75em; align-items:flex-start; margin:0 0 0.7em; font-size:0.93em; line-height:1.55; }
.hm-open li:last-child { margin-bottom:0; }
.hm-open li i { color:#d9822b; width:1.2em; text-align:center; margin-top:0.3em; flex:none; }
</style>

<div class="hm">
<div class="hm-hero">
<h1>Ping Liu</h1>
<p class="role">Assistant Professor, Department of Computer Science and Engineering, University of Nevada, Reno</p>
<p class="tag">Controllable, verifiable, and physically grounded generative AI.</p>
<div class="hm-btns"><a href="{{ base_path }}/research/"><i class="fas fa-flask"></i>&nbsp; Research</a><a href="{{ base_path }}/publications/"><i class="fas fa-book"></i>&nbsp; Publications</a><a href="{{ base_path }}/cv/"><i class="fas fa-id-card"></i>&nbsp; CV</a><a href="{{ site.author.googlescholar }}"><i class="ai ai-google-scholar"></i>&nbsp; Google Scholar</a><a href="mailto:pingl@unr.edu"><i class="fas fa-envelope"></i>&nbsp; Email</a></div>
</div>

<div class="hm-sec">
<div class="hm-h"><div class="ic" style="background:#3a7bd5"><i class="fas fa-user"></i></div><h2>About</h2></div>
<div class="hm-about">
<p>Ping Liu is a Tenure-Track Assistant Professor in the Department of Computer Science and Engineering at the University of Nevada, Reno (UNR), where he has been since March 2024. From 2020 to 2024 he was a Scientist and then Senior Scientist II at the Centre for Frontier AI Research (CFAR), Institute of High Performance Computing (IHPC), A*STAR, Singapore. Before that, he was a Research Fellow and Lecturer at the University of Technology Sydney, a Research Scientist at the JD.com US Research Center, and a Senior Applied Research Engineer at the Sony US Research Center.</p>
<p>He received his Ph.D. in Computer Science and Engineering from the University of South Carolina, his M.Eng. from Huazhong University of Science and Technology, and his B.Eng. from Wuhan University of Technology. He is an IEEE Senior Member.</p>
</div>
</div>

<div class="hm-sec">
<div class="hm-h"><div class="ic" style="background:#4b4fc9"><i class="fas fa-flask"></i></div><h2>Research</h2></div>
<p style="margin:0 0 1em">His research develops methods that diagnose what a generative model has learned, intervene on it selectively, and verify the result. Current work follows three directions.</p>
<div class="hm-dirs">
<a class="hm-dir" href="{{ base_path }}/research/#erasure" style="--c:#4b4fc9;--bg:#f5f6ff"><i class="fas fa-eraser"></i><b>Concept Erasure and Machine Unlearning</b><span>Removing targeted concepts, including motion, from image and video generative models.</span></a>
<a class="hm-dir" href="{{ base_path }}/research/#physics" style="--c:#0e8a83;--bg:#f1faf9"><i class="fas fa-atom"></i><b>Physically Grounded Text-to-Video Generation</b><span>Making generated motion physically consistent while faithful to the prompt.</span></a>
<a class="hm-dir" href="{{ base_path }}/research/#deepfake" style="--c:#be185d;--bg:#fdf4f8"><i class="fas fa-user-secret"></i><b>Deepfake Detection and Media Forensics</b><span>Detecting forgeries that generalize to unseen generators and modalities.</span></a>
</div>
<p class="hm-note">His research is supported by the National Science Foundation, including an NSF Major Research Instrumentation award for a large-scale GPU cluster for AI research at UNR. <a href="{{ base_path }}/research/">Read more about his research &rarr;</a></p>
</div>

<div class="hm-sec">
<div class="hm-h"><div class="ic" style="background:#d9822b"><i class="fas fa-handshake"></i></div><h2>Collaboration and Openings</h2></div>
<div class="hm-open"><ul>
<li><i class="fas fa-handshake"></i><span>He welcomes research collaborations with academic and industry partners.</span></li>
<li><i class="fas fa-user-graduate"></i><span>Prospective Ph.D. students are encouraged to apply to the UNR CSE Ph.D. program and mention his name.</span></li>
</ul></div>
</div>

<div class="hm-sec">
<div class="hm-h"><div class="ic" style="background:#be185d"><i class="fas fa-bullhorn"></i></div><h2>News</h2></div>
<ul class="hm-news" id="hm-news">
<li class="hm-n"><span class="hm-d">Oct 2026</span><span class="hm-k" style="background:#3a7bd5">Release</span><span class="hm-t">The project page and code for PhyMetric (NeurIPS 2026) are now available. PhyMetric diagnoses which physical laws text-to-video models violate, using 8,920 scene-grounded yes/no questions over 1,115 scenes in 50 physical categories. <a class="hm-ln" href="https://mengsiwei.github.io/PhyMetric/">Project page</a> <a class="hm-ln" href="https://github.com/mengsiwei/PhyMetric/tree/phymetric">Code</a></span></li>
<li class="hm-n"><span class="hm-d">Oct 2026</span><span class="hm-k" style="background:#0e8a83">Talk</span><span class="hm-t">Invited talk at UC Merced: "Intervene and Verify: Toward Controllable Generative Models and World Models."</span></li>
<li class="hm-n"><span class="hm-d">Sep 2026</span><span class="hm-k" style="background:#4b4fc9">Paper</span><span class="hm-t">"PhyMetric: Diagnosing Physical Plausibility in Text-to-Video Generation via Scene-Level QA," led by Ph.D. student Siwei Meng, accepted to NeurIPS 2026, Evaluations and Datasets Track (corresponding author). <a class="hm-ln" href="https://mengsiwei.github.io/PhyMetric/">Project page</a> <a class="hm-ln" href="https://github.com/mengsiwei/PhyMetric/tree/phymetric">Code</a></span></li>
<li class="hm-n"><span class="hm-d">Sep 2026</span><span class="hm-k" style="background:#4b4fc9">Paper</span><span class="hm-t">"Calibrated Drift Control for Heterogeneous DPO" accepted to NeurIPS 2026 (first author).</span></li>
<li class="hm-n"><span class="hm-d">Sep 2026</span><span class="hm-k" style="background:#4b4fc9">Paper</span><span class="hm-t">"DOME: Drift-Adaptive On-Policy Motion Erasure in Video Diffusion Transformers" accepted to NeurIPS 2026 (first author).</span></li>
<li class="hm-n"><span class="hm-d">Aug 2026</span><span class="hm-k" style="background:#4b4fc9">Paper</span><span class="hm-t">"MUTE: Motion Concept Unlearning in Video Diffusion Models" accepted to ACM Multimedia 2026 (first author). <a class="hm-ln" href="https://arxiv.org/abs/2609.36832">arXiv</a></span></li>
<li class="hm-n"><span class="hm-d">Aug 2026</span><span class="hm-k" style="background:#4b4fc9">Paper</span><span class="hm-t">"When Physical Preferences Meet Semantic Constraints: Physical and Semantic Direct Preference Optimization for Text-to-Video Generation," led by Ph.D. student Siwei Meng, accepted to ACM Multimedia 2026 and selected for an oral presentation (corresponding author). <a class="hm-ln" href="https://arxiv.org/abs/2607.16947">arXiv</a></span></li>
<li class="hm-n"><span class="hm-d">Jul 2026</span><span class="hm-k" style="background:#d9822b">Service</span><span class="hm-t">Co-organizing the workshop "MIRAI Driving: Multimodal Intelligence and Reasoning for Autonomous and Intelligent Driving" at ACCV 2026, Osaka, Japan. <a class="hm-ln" href="https://mengsiwei.github.io/MIRAI_ACCV_Workshop/">Workshop website</a></span></li>
<li class="hm-n hm-more"><span class="hm-d">Jun 2026</span><span class="hm-k" style="background:#d9822b">Service</span><span class="hm-t">Invited to serve as Senior PC Member for AAAI 2027.</span></li>
<li class="hm-n hm-more"><span class="hm-d">Jun 2026</span><span class="hm-k" style="background:#4b4fc9">Paper</span><span class="hm-t">"PhyMAGIC: Physical Motion-Aware Generative Inference with Confidence-Guided VLM," led by Ph.D. student Siwei Meng, accepted to ECCV 2026 (co-corresponding author). <a class="hm-ln" href="https://mengsiwei.github.io/MAGIC/">Project page</a></span></li>
<li class="hm-n hm-more"><span class="hm-d">Jun 2026</span><span class="hm-k" style="background:#4b4fc9">Paper</span><span class="hm-t">"RIGI: Rectifying Image-to-3D Generation Inconsistency via Uncertainty-aware Learning" accepted to IEEE Transactions on Image Processing (co-corresponding author).</span></li>
<li class="hm-n hm-more"><span class="hm-d">May 2026</span><span class="hm-k" style="background:#4b4fc9">Paper</span><span class="hm-t">"Where Concept Erasure Should Occur: Concept–Layer Alignment in Text-to-Video Diffusion Models" accepted to ICML 2026 (co-corresponding author).</span></li>
<li class="hm-n hm-more"><span class="hm-d">Apr 2026</span><span class="hm-k" style="background:#4b4fc9">Paper</span><span class="hm-t">"ABCDE: Agentic-Based Controlled Dynamic Erasure for Intent-Aware Safety Reasoning" accepted to Transactions on Machine Learning Research (first author).</span></li>
<li class="hm-n hm-more"><span class="hm-d">Mar 2026</span><span class="hm-k" style="background:#b91c1c">Preprint</span><span class="hm-t">"PROBE: Diagnosing Residual Concept Capacity in Erased Text-to-Video Diffusion Models" released on arXiv (co-corresponding author). <a class="hm-ln" href="https://arxiv.org/abs/2603.21547">arXiv</a></span></li>
<li class="hm-n hm-more"><span class="hm-d">Feb 2026</span><span class="hm-k" style="background:#d9822b">Service</span><span class="hm-t">Invited to serve as Area Chair for ACM MM 2026.</span></li>
<li class="hm-n hm-more"><span class="hm-d">Feb 2026</span><span class="hm-k" style="background:#4b4fc9">Paper</span><span class="hm-t">"Closed-Form Concept Erasure via Double Projections" accepted to CVPR 2026 (corresponding author). <a class="hm-ln" href="https://arxiv.org/abs/2604.10032">arXiv</a></span></li>
<li class="hm-n hm-more"><span class="hm-d">Feb 2026</span><span class="hm-k" style="background:#d9822b">Service</span><span class="hm-t">Workshop proposal "SynthIR: The First Workshop on Synthetic Content in Information Retrieval Ecosystems" accepted at SIGIR 2026.</span></li>
<li class="hm-n hm-more"><span class="hm-d">Jan 2026</span><span class="hm-k" style="background:#d9822b">Service</span><span class="hm-t">Invited to serve as Senior PC Member for IJCAI 2026.</span></li>
</ul>
<button class="hm-toggle" id="hm-toggle">Show all news</button>
</div>
</div>

<script>
(function(){var b=document.getElementById('hm-toggle'),l=document.getElementById('hm-news');if(!b||!l)return;b.addEventListener('click',function(){var o=l.classList.toggle('open');b.textContent=o?'Show fewer':'Show all news';});})();
</script>

<div id="clustrmaps-widget">
<script type="text/javascript" id="clustrmaps" src="//clustrmaps.com/map_v2.js?d=oXRv4M63JdtwBIkQ5oKu8c-q64iduHv6EuXiZlADu50&cl=ffffff&w=a"></script>
</div>
