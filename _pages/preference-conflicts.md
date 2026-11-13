---
layout: archive
title: "When Preferences and Scores Disagree"
permalink: /notes/preference-conflicts/
redirect_from:
  - /research/preference-conflicts/
author_profile: true
---

{% include base_path %}

<style>
.pc { --ink:#1f2a44; --muted:#5b6478; --line:#e6e9f0; --al:#5b4fc9; --al-soft:#f3f1ff; --ps:#d9822b; --ps-soft:#fff4e2; --co:#7c3aed; --co-soft:#f4eefe; --ok:#0e8a83; --bad:#c2410c; font-size:0.95em; line-height:1.7; color:var(--ink); }
.pc * { box-sizing:border-box; }
.pc-hero { background:linear-gradient(120deg,#4b3fb5 0%,#6a4fd1 50%,#d9822b 100%); color:#fff; border-radius:16px; padding:2.2em 2.2em 2em; margin:0.5em 0 2.4em; box-shadow:0 10px 30px rgba(60,48,150,0.18); }
.pc-hero .k { text-transform:uppercase; letter-spacing:0.14em; font-size:0.72em; opacity:0.85; margin:0 0 0.6em; }
.pc-hero h2 { color:#fff; border:0; margin:0 0 0.5em; padding:0; font-size:1.55em; line-height:1.3; }
.pc-hero p { margin:0 0 1.2em; opacity:0.95; max-width:44em; }
.pc-jump { display:flex; flex-wrap:wrap; gap:0.7em; }
.pc-jump a { color:#fff !important; text-decoration:none !important; border:1px solid rgba(255,255,255,0.55); background:rgba(255,255,255,0.12); padding:0.45em 1.1em; border-radius:999px; font-size:0.85em; }
.pc-jump a:hover { background:rgba(255,255,255,0.25); }
.pc-sec { border:1px solid var(--line); border-radius:18px; padding:1.9em 2em 1.5em; margin:0 0 2.6em; }
.pc-sec.al { background:linear-gradient(180deg,var(--al-soft) 0%,#fff 220px); border-top:5px solid var(--al); }
.pc-sec.ps { background:linear-gradient(180deg,var(--ps-soft) 0%,#fff 220px); border-top:5px solid var(--ps); }
.pc-sec.co { background:linear-gradient(180deg,var(--co-soft) 0%,#fff 220px); border-top:5px solid var(--co); }
.pc-head { display:flex; align-items:center; gap:0.9em; margin-bottom:0.9em; }
.pc-num { font-size:2.2em; font-weight:800; line-height:1; opacity:0.25; }
.al .pc-num, .al .pc-tag { color:var(--al); } .ps .pc-num, .ps .pc-tag { color:var(--ps); } .co .pc-num, .co .pc-tag { color:var(--co); }
.pc-head h2 { margin:0; border:0; padding:0; font-size:1.38em; line-height:1.25; }
.pc-tag { display:block; font-size:0.62em; font-weight:600; text-transform:uppercase; letter-spacing:0.12em; margin-bottom:0.35em; }
.pc-sec p { max-width:48em; }
.pc-sec h3 { font-size:0.92em; text-transform:uppercase; letter-spacing:0.1em; color:var(--muted); margin:1.6em 0 0.7em; border:0; padding:0; }
.pc-fig { margin:1.2em 0 1.4em; background:#fff; border:1px solid var(--line); border-radius:14px; padding:1em; box-shadow:0 4px 18px rgba(31,42,68,0.06); }
.pc-fig img, .pc-fig svg { width:100%; height:auto; display:block; border-radius:8px; }
.pc-pair { display:grid; grid-template-columns:1fr 1fr; gap:1em; width:100%; }
.pc-pair svg { width:100% !important; max-width:none !important; height:auto; }
@media (max-width: 760px) { .pc-pair { grid-template-columns:1fr; } }
.pc-fig figcaption { margin-top:0.8em; font-size:0.82em; color:#4a5368; line-height:1.55; }
.pc-fig figcaption b { color:var(--ink); }
.pc-eq { background:#fff; border:1px solid var(--line); border-left:4px solid var(--ps); border-radius:10px; padding:0.8em 1.1em; margin:0.8em 0 1.1em; font-family:"Times New Roman",Georgia,serif; font-size:1.05em; overflow-x:auto; }
.pc-eq .row { white-space:nowrap; line-height:1.9; }
.pc-steps { list-style:none; counter-reset:s; margin:0.6em 0 1em; padding:0; }
.pc-steps li { counter-increment:s; position:relative; padding:0.15em 0 0.65em 2.4em; margin:0; max-width:48em; }
.pc-steps li::before { content:counter(s); position:absolute; left:0; top:0.2em; width:1.7em; height:1.7em; border-radius:50%; background:var(--c,var(--al)); color:#fff; font-size:0.8em; font-weight:700; display:flex; align-items:center; justify-content:center; }
.ps .pc-steps { --c:var(--ps); } .co .pc-steps { --c:var(--co); }
.pc-res { display:grid; grid-template-columns:repeat(3,1fr); gap:0.9em; margin:0.6em 0 1.2em; }
.pc-stat { background:#fff; border:1px solid var(--line); border-radius:12px; padding:0.9em 1em; }
.pc-stat .lab { font-size:0.78em; color:var(--muted); display:block; line-height:1.4; }
.pc-stat .val { font-size:1.15em; font-weight:700; display:block; margin-top:0.25em; }
.pc-stat .val .from { color:var(--muted); font-weight:500; }
.pc-stat .val .to { color:var(--ps); }
.pc-pills { display:flex; flex-wrap:wrap; gap:0.6em; margin:0.4em 0 1.2em; }
.pc-pill { background:#fff; border:1px solid var(--line); border-radius:999px; padding:0.35em 0.95em; font-size:0.85em; }
.pc-pill b { color:var(--co); }
.pc-paper { display:flex; gap:1em; align-items:flex-start; background:#fff; border:1px solid var(--line); border-radius:12px; padding:0.85em 1em; margin:1.4em 0 0.4em; }
.pc-venue { flex:0 0 7.2em; text-align:center; font-size:0.72em; font-weight:700; color:#fff; border-radius:6px; padding:0.35em 0.3em; line-height:1.3; }
.pc-paper .t { font-weight:600; display:block; line-height:1.4; }
.pc-paper .a { color:var(--muted); font-size:0.86em; display:block; margin-top:0.15em; }
.pc-paper .l a { display:inline-block; margin-top:0.35em; font-size:0.78em; padding:0.1em 0.7em; border-radius:999px; border:1px solid currentColor; text-decoration:none; }
.ps .pc-paper .l a { color:var(--ps); } .co .pc-paper .l a { color:var(--co); }
.pc-tw { overflow-x:auto; margin:0.6em 0 1.2em; }
.pc-tbl { width:100%; border-collapse:separate; border-spacing:0; font-size:0.86em; background:#fff; border:1px solid var(--line); border-radius:12px; overflow:hidden; display:table; }
.pc-tbl th, .pc-tbl td { padding:0.7em 0.9em; border-bottom:1px solid var(--line); vertical-align:top; text-align:left; line-height:1.5; }
.pc-tbl tr:last-child td { border-bottom:0; }
.pc-tbl thead th { background:#f8f9fc; font-size:0.92em; }
.pc-tbl thead th.ps { color:var(--ps); } .pc-tbl thead th.co { color:var(--co); }
.pc-tbl td:first-child { font-weight:600; color:var(--muted); width:22%; }
.pc-take { display:grid; grid-template-columns:repeat(3,1fr); gap:0.9em; margin:0.6em 0 0.4em; }
.pc-card { background:#fff; border:1px solid var(--line); border-radius:12px; padding:1em 1em 0.9em; font-size:0.9em; line-height:1.55; }
.pc-card i { color:var(--al); font-size:1.15em; display:block; margin-bottom:0.45em; }
.pc-card b { display:block; margin-bottom:0.25em; }
.co .pc-eq { border-left-color:var(--co); }
.pc-evo { position:relative; margin:1.2em 0 0.4em; padding-left:2.6em; }
.pc-evo::before { content:""; position:absolute; left:0.95em; top:1em; bottom:1em; width:3px; border-radius:2px; background:linear-gradient(180deg,var(--ps) 0%,var(--co) 30%,var(--co) 100%); }
.pc-step { position:relative; background:#fff; border:1px solid var(--line); border-radius:12px; padding:0.85em 1.1em 0.3em; box-shadow:0 3px 12px rgba(31,42,68,0.05); }
.pc-step::before { content:""; position:absolute; left:-2.15em; top:1em; width:1.15em; height:1.15em; border-radius:50%; background:var(--dot); border:3px solid #fff; box-shadow:0 0 0 1px var(--dot); }
.pc-step.s-ps { --dot:var(--ps); border-left:4px solid var(--ps); } .pc-step.s-co { --dot:var(--co); border-left:4px solid var(--co); } .pc-step.s-next { --dot:#9aa3b8; border-left:4px solid #9aa3b8; border-style:dashed solid dashed solid; }
.pc-step .who { display:inline-block; font-size:0.68em; font-weight:700; letter-spacing:0.12em; text-transform:uppercase; color:var(--dot); }
.pc-step h4 { margin:0.1em 0 0.4em; font-size:1.02em; border:0; padding:0; }
.pc-step p { margin:0 0 0.7em; font-size:0.95em; }
.pc-q { margin:0.55em 0 0.55em; font-style:italic; color:var(--al); font-weight:600; font-size:0.92em; }
.pc-q i { font-style:normal; margin-right:0.35em; opacity:0.8; }
.pc-more { border:2px dashed var(--al); border-radius:18px; min-height:7em; display:flex; align-items:center; justify-content:center; margin:0 0 2.6em; color:var(--al); font-weight:700; font-size:1.2em; letter-spacing:0.04em; }
.pc-back { font-size:0.88em; margin:0 0 2em; }
@media (max-width: 760px) {
  .pc-hero { padding:1.6em 1.3em; } .pc-sec { padding:1.4em 1.1em; }
  .pc-res, .pc-take { grid-template-columns:1fr; }
  .pc-evo { padding-left:1.9em; } .pc-evo::before { left:0.6em; } .pc-step::before { left:-1.75em; } .pc-step { padding:0.8em 0.9em 0.2em; }
  .pc-paper { flex-direction:column; gap:0.5em; } .pc-venue { flex:none; padding:0.3em 0.8em; }
}
</style>

<div class="pc">

<div class="pc-hero">
<p class="k">Research note · Verifiable Rewards, Alignment, and Agents</p>
<h2>From PSDPO to CoDPO: preference optimization under conflicting signals</h2>
<p>Preference optimization learns from pairwise judgments: of two outputs, which one is better. The same models are also judged by pointwise criteria: is this video faithful to its prompt, is this answer correct, is it safe. This line of work began with PSDPO, which found that in text-to-video generation the physically preferred video is often the one less faithful to the prompt, and proposed a way to train on such data. CoDPO followed and asked the same question for direct preference optimization in general: when do conflicting pairs make training drift, and can we tell before training starts?</p>
<div class="pc-jump"><a href="#psdpo"><i class="fas fa-film"></i>&nbsp; PSDPO: where it started</a><a href="#codpo"><i class="fas fa-chart-line"></i>&nbsp; CoDPO: the general problem</a><a href="#compare"><i class="fas fa-route"></i>&nbsp; How one led to the other</a></div>
</div>

<div class="pc-sec ps" id="psdpo">
<div class="pc-head"><div class="pc-num">01</div><h2><span class="pc-tag">Where it started · Text-to-video generation · ACM MM 2026, Oral</span>PSDPO: physical preferences meet semantic constraints</h2></div>
<p>Preference optimization can make generated videos more physically plausible, but it often makes them less faithful to the prompt. PSDPO traces this to how the two signals are obtained. Physical plausibility is judged by comparing the dynamics of two videos, so it is a pairwise signal. Prompt fidelity is checked one video at a time against its prompt, so it is a pointwise signal. In our training data, the physically preferred video was the less faithful one in 51.5% of pairs. A typical case: the prompt asks for a lemon slice, and the physically more convincing video shows a whole lemon. Training on such a pair rewards the model for drifting away from the prompt.</p>
<p>Direct preference optimization (DPO) trains on pairs. For a prompt <i>x</i>, one output <i>y</i><sub>w</sub> is preferred over another output <i>y</i><sub>l</sub>, and the update raises the likelihood of <i>y</i><sub>w</sub> relative to <i>y</i><sub>l</sub>. PSDPO separates two kinds of pairs. In a <b>matching pair</b>, the physically preferred video is also at least as faithful to the prompt. In a <b>conflict pair</b>, it is less faithful. Standard DPO applies the same update to both kinds, so on a conflict pair it raises the likelihood of the less faithful video and moves the model away from the prompt. With conflict pairs making up about half of the data, these updates accumulate, which explains why prompt fidelity drops even as physical plausibility improves.</p>

<figure class="pc-fig">
<div class="pc-pair"><svg viewBox="0 0 360 230" role="img" aria-label="Matching pair">
<rect x="1" y="1" width="358" height="228" rx="14" fill="#f2fbf9" stroke="#bfe7e2"/>
<text x="180" y="30" text-anchor="middle" font-size="17" font-weight="700" fill="#0e8a83">Matching pair</text>
<text x="60" y="60" text-anchor="middle" font-size="13" fill="#1f2a44">preferred y<tspan baseline-shift="sub" font-size="10">w</tspan></text>
<text x="290" y="60" text-anchor="middle" font-size="13" fill="#1f2a44">rejected y<tspan baseline-shift="sub" font-size="10">l</tspan></text>
<rect x="35" y="70" width="50" height="40" rx="8" fill="#5b4fc9"/><text x="60" y="96" text-anchor="middle" font-size="13" fill="#fff">y<tspan baseline-shift="sub" font-size="10">w</tspan></text>
<rect x="265" y="70" width="50" height="40" rx="8" fill="#9aa3b8"/><text x="290" y="96" text-anchor="middle" font-size="13" fill="#fff">y<tspan baseline-shift="sub" font-size="10">l</tspan></text>
<line x1="92" y1="90" x2="255" y2="90" stroke="#5b4fc9" stroke-width="2"/><polygon points="92,90 102,85 102,95" fill="#5b4fc9"/>
<text x="175" y="83" text-anchor="middle" font-size="12" fill="#5b4fc9">preferred</text>
<text x="180" y="140" text-anchor="middle" font-size="12" fill="#5b6478">prompt-fidelity score</text>
<rect x="35" y="150" width="240" height="16" rx="4" fill="#e6e9f0"/><rect x="35" y="150" width="201" height="16" rx="4" fill="#0e8a83"/>
<rect x="35" y="174" width="240" height="16" rx="4" fill="#e6e9f0"/><rect x="35" y="174" width="120" height="16" rx="4" fill="#9aa3b8"/>
<text x="285" y="163" font-size="12" fill="#1f2a44">y<tspan baseline-shift="sub" font-size="10">w</tspan></text><text x="285" y="187" font-size="12" fill="#1f2a44">y<tspan baseline-shift="sub" font-size="10">l</tspan></text>
<text x="180" y="215" text-anchor="middle" font-size="12.5" fill="#0e8a83">DPO pushes toward the higher score</text>
</svg><svg viewBox="0 0 360 230" role="img" aria-label="Conflict pair">
<rect x="1" y="1" width="358" height="228" rx="14" fill="#fff4ee" stroke="#f6d3bf"/>
<text x="180" y="30" text-anchor="middle" font-size="17" font-weight="700" fill="#c2410c">Conflict pair</text>
<text x="60" y="60" text-anchor="middle" font-size="13" fill="#1f2a44">preferred y<tspan baseline-shift="sub" font-size="10">w</tspan></text>
<text x="290" y="60" text-anchor="middle" font-size="13" fill="#1f2a44">rejected y<tspan baseline-shift="sub" font-size="10">l</tspan></text>
<rect x="35" y="70" width="50" height="40" rx="8" fill="#5b4fc9"/><text x="60" y="96" text-anchor="middle" font-size="13" fill="#fff">y<tspan baseline-shift="sub" font-size="10">w</tspan></text>
<rect x="265" y="70" width="50" height="40" rx="8" fill="#9aa3b8"/><text x="290" y="96" text-anchor="middle" font-size="13" fill="#fff">y<tspan baseline-shift="sub" font-size="10">l</tspan></text>
<line x1="92" y1="90" x2="255" y2="90" stroke="#5b4fc9" stroke-width="2"/><polygon points="92,90 102,85 102,95" fill="#5b4fc9"/>
<text x="175" y="83" text-anchor="middle" font-size="12" fill="#5b4fc9">preferred</text>
<text x="180" y="140" text-anchor="middle" font-size="12" fill="#5b6478">prompt-fidelity score</text>
<rect x="35" y="150" width="240" height="16" rx="4" fill="#e6e9f0"/><rect x="35" y="150" width="105" height="16" rx="4" fill="#c2410c"/>
<rect x="35" y="174" width="240" height="16" rx="4" fill="#e6e9f0"/><rect x="35" y="174" width="206" height="16" rx="4" fill="#9aa3b8"/>
<text x="285" y="163" font-size="12" fill="#1f2a44">y<tspan baseline-shift="sub" font-size="10">w</tspan></text><text x="285" y="187" font-size="12" fill="#1f2a44">y<tspan baseline-shift="sub" font-size="10">l</tspan></text>
<text x="180" y="215" text-anchor="middle" font-size="12.5" fill="#c2410c">DPO pushes toward the lower score</text>
</svg></div>
<figcaption><b>Two kinds of preference pairs.</b> In both pairs <i>y</i><sub>w</sub> is the physically preferred video, so standard DPO raises its likelihood. In a matching pair this also favors the video that follows the prompt better. In a conflict pair it favors the video that follows the prompt worse. CoDPO later studies the same picture with any pointwise criterion in place of prompt fidelity.</figcaption>
</figure>
<figure class="pc-fig"><img src="{{ base_path }}/images/research/psdpo.jpg" alt="Comparison between vanilla DPO and PSDPO"><figcaption><b>Vanilla DPO versus PSDPO.</b> Adding semantic feasibility to physical preference optimization preserves prompt semantics and stabilizes preference learning.</figcaption></figure>

<h3>Method</h3>
<ol class="pc-steps">
<li><b>Two signals per pair.</b> A physical commonsense evaluator built on Qwen3-VL, with optical-flow and depth cues, decides which of two videos is physically better. ViCLIP scores each video separately for agreement with the prompt, and the semantic gap is &Delta;<i>S</i> = <i>S</i><sub>sem</sub>(<i>y</i><sub>w</sub>, <i>x</i>) &minus; <i>S</i><sub>sem</sub>(<i>y</i><sub>l</sub>, <i>x</i>).</li>
<li><b>Soft down-weighting of conflict pairs.</b> Each pair's DPO term is multiplied by a weight that stays at 1 for matching pairs and decays with the size of the conflict:
<div class="pc-eq"><div class="row"><i>W</i>(&Delta;<i>S</i>) = 1 &nbsp;&nbsp; if &Delta;<i>S</i> &ge; 0, &nbsp;&nbsp;&nbsp;&nbsp; <i>W</i>(&Delta;<i>S</i>) = exp(&Delta;<i>S</i> / &tau;) &nbsp;&nbsp; if &Delta;<i>S</i> &lt; 0</div></div>
The temperature &tau; sets how strongly conflicts are discounted. As &tau; approaches 0, conflict pairs are discarded; as &tau; grows, the objective returns to vanilla DPO. A mild conflict therefore still contributes part of its physical signal, while a severe one contributes almost nothing.</li>
<li><b>Staged training.</b> The model first trains on matching pairs only, then continues on all pairs with the weights above. The early stage establishes physical preferences that do not cost prompt fidelity before the discounted conflict pairs enter.</li>
</ol>

<h3>Selected results</h3>
<p>Wan 1.3B fine-tuned with LoRA on 10K preference pairs built from WISA-80K captions. The two VBench scores compare PSDPO with vanilla DPO trained on the same data; the VideoPhy-2 score compares it with the base model.</p>
<div class="pc-res">
<div class="pc-stat"><span class="lab">VBench total score</span><span class="val"><span class="from">82.790</span> &rarr; <span class="to">84.130</span></span></div>
<div class="pc-stat"><span class="lab">VBench semantic score</span><span class="val"><span class="from">77.010</span> &rarr; <span class="to">78.250</span></span></div>
<div class="pc-stat"><span class="lab">VideoPhy-2 hard subset</span><span class="val"><span class="from">0.039</span> &rarr; <span class="to">0.078</span></span></div>
</div>

<div class="pc-paper"><span class="pc-venue" style="background:#0f766e">ACM MM 2026</span><div><span class="t">When Physical Preferences Meet Semantic Constraints: Physical and Semantic Direct Preference Optimization for Text-to-Video Generation</span><span class="a">Siwei Meng, Yawei Luo, Shu Zhang, <b>Ping Liu</b><sup>†</sup> · Oral presentation</span><span class="l"><a href="https://arxiv.org/abs/2607.16947">arXiv</a></span></div></div>
</div>

<div class="pc-sec co" id="codpo">
<div class="pc-head"><div class="pc-num">02</div><h2><span class="pc-tag">The general problem · Direct preference optimization · NeurIPS 2026</span>CoDPO: diagnosing and correcting constraint drift</h2></div>
<p>CoDPO studies direct preference optimization in general, wherever pairwise preferences come together with a pointwise criterion such as response length, answer correctness, or a safety score. Following PSDPO, a pair is a conflict pair when the preferred output scores worse on the criterion. Such pairs are common: the preferred response is the longer one in 57% of HelpSteer2 pairs, and it is the incorrect one in 71% of GSM8K pairs and 58% of ARC pairs. Training on them raises the expected cost on the criterion. We call this <b>constraint drift</b>; it is the general counterpart of the semantic drift that PSDPO found in video.</p>

<h3>Drift as a balance</h3>
<p>For small updates, the change in expected constraint cost at each DPO step is a balance between two groups of pairs. Conflict pairs push the cost up and matching pairs pull it down. At the start of training this balance can be estimated from the cost gaps in the data alone, which gives a pre-alignment diagnostic:</p>
<div class="pc-eq"><div class="row">&rho;*<sub>eq</sub> = (1 &minus; <i>p</i><sub>c</sub>) &middot; mean |&Delta;<i>c</i>| over matching pairs &nbsp;/&nbsp; ( <i>p</i><sub>c</sub> &middot; mean &Delta;<i>c</i> over conflict pairs )</div></div>
<p>Here <i>p</i><sub>c</sub> is the conflict rate and &Delta;<i>c</i> is the cost of the preferred output minus the cost of the rejected one. The numerator is the total cost reduction across matching pairs, and the denominator is the total cost increase across conflict pairs. A value of at least 1 says the dataset corrects itself, and CoDPO then reduces to plain DPO. A value below 1 says the dataset needs intervention. The estimate assumes that, per unit of cost gap, learning a conflict pair moves the expected cost about as much as learning a matching pair.</p>

<h3>Method: two levels of control</h3>
<ol class="pc-steps">
<li><b>Coarse level: set the weights before training.</b> Matching pairs keep weight 1. A conflict pair with score gap &Delta;<i>s</i> &lt; 0 receives
<div class="pc-eq"><div class="row"><i>w</i>(&Delta;<i>s</i>) = exp( &minus;( |&Delta;<i>s</i>| / &tau; )<sup><i>p</i></sup> )</div></div>
With <i>p</i> = 1 this is PSDPO's weight. CoDPO uses <i>p</i> = 8, so the weight stays high for mild conflicts and drops sharply for severe ones. The temperature &tau; is not tuned: it is found by bisection so that the average weight on conflict pairs equals &rho;*<sub>eq</sub>, the point at which conflict-side pressure no longer exceeds matching-side repair to first order. This step uses dataset statistics only and needs no gradient computation.</li>
<li><b>Fine level: shift the margin during training.</b> The balance moves as the model leaves the reference model, so some drift can remain under fixed weights. CoDPO adds &lambda;&Delta;<i>c</i> to each pair's DPO margin, so conflict pairs are pushed less and matching pairs are pushed more. This is implemented by tilting the reference model against high-cost outputs, which leaves the DPO loss itself unchanged. The constraint risk is estimated on the training pairs every 500 steps. Whenever the estimate rises, &lambda; is raised by a fixed step, up to a cap computed from the data.</li>
</ol>
<div class="pc-eq"><div class="row"><i>L</i><sub>CoDPO</sub> = &minus; mean over the batch of &nbsp;<i>w</i><sub>i</sub> &middot; log &sigma;( &beta; <i>r&#770;</i><sub>i</sub> + &beta; &lambda; &Delta;<i>c</i><sub>i</sub> )</div></div>

<h3>Evaluation</h3>
<div class="pc-pills">
<span class="pc-pill"><b>6</b> domains: 5 conflict-dominated, 1 self-correcting control</span>
<span class="pc-pill"><b>4</b> base models</span>
<span class="pc-pill"><b>3</b> further preference losses: IPO, SimPO, KTO</span>
<span class="pc-pill"><b>5</b> recent baselines, plus hard filtering</span>
</div>
<p>The main model is Qwen2.5-7B-Instruct trained with LoRA. The conflict-dominated domains are HelpSteer2 and TL;DR, where the criterion is length, and GSM8K, ARC, and Math-Calc, where it is answer correctness. PKU-SafeRLHF, with a safety score as the criterion, is the control. On all five conflict-dominated domains, drift grows steadily as more weight is kept on conflict pairs, and &rho;*<sub>eq</sub> is below 1. On PKU-SafeRLHF, &rho;*<sub>eq</sub> is at least 1 and drift stays negligible. Removing conflict pairs altogether suppresses drift but costs most of the preference learning: hard filtering keeps only 7% to 41% of vanilla DPO's gain on four domains, and on TL;DR it falls below the base model.</p>
<div class="pc-tw">
<table class="pc-tbl">
<thead><tr><th>Domain</th><th>Drift: vanilla DPO &rarr; <span style="color:var(--co)">CoDPO</span></th><th>P(chosen): vanilla DPO &rarr; <span style="color:var(--co)">CoDPO</span></th></tr></thead>
<tbody>
<tr><td>HelpSteer2</td><td>+59.000 &rarr; <b>+18.700</b> characters</td><td>0.566 &rarr; <b>0.640</b></td></tr>
<tr><td>GSM8K</td><td>+0.129 &rarr; <b>+0.082</b></td><td>0.453 &rarr; <b>0.551</b></td></tr>
<tr><td>ARC</td><td>+0.055 &rarr; <b>+0.046</b></td><td>0.532 &rarr; <b>0.622</b></td></tr>
<tr><td>Math-Calc</td><td>+0.071 &rarr; <b>+0.066</b></td><td>0.652 &rarr; <b>0.757</b></td></tr>
</tbody>
</table>
</div>
<p>Drift is the change in expected constraint cost relative to the base model: response length on HelpSteer2 and the probability of an incorrect answer on the other three domains. P(chosen) is the probability the model assigns to the preferred output within a pair and measures preference learning. Lower drift and higher P(chosen) are better. Methods that enforce a constraint on the expected cost, such as SafeDPO and PD-DPO, lower drift further, but their P(chosen) stays near or below that of the base model. Among all compared methods and settings with drift comparable to or below CoDPO's, CoDPO has the highest P(chosen) on all four domains. On HelpSteer2, an LLM judge (JudgeLM-13B) rates CoDPO and vanilla DPO as tied in 75.5% of comparisons, so the lower drift comes without a quality loss that this judge can detect.</p>

<div class="pc-paper"><span class="pc-venue" style="background:#7c3aed">NeurIPS 2026</span><div><span class="t">When Scores Conflict with Preferences: Pre-Alignment Diagnosis and Adaptive Correction of Constraint Drift in DPO</span><span class="a"><b>Ping Liu</b>, Yan Yan</span><span class="l"><a href="https://arxiv.org/abs/2611.07375">arXiv</a></span></div></div>
</div>

<div class="pc-more">More will be coming</div>

<div class="pc-sec al" id="compare">
<div class="pc-head"><div class="pc-num">03</div><h2><span class="pc-tag">From one paper to the next</span>How PSDPO led to CoDPO</h2></div>
<p>CoDPO keeps PSDPO's core idea: keep matching pairs at full weight, and discount conflict pairs instead of discarding them. What changed is that each part of CoDPO answers a question PSDPO raised but did not settle. The steps below follow that sequence.</p>

<div class="pc-evo">
<div class="pc-step s-ps"><span class="who">PSDPO</span><h4>The observation</h4><p>In text-to-video training data, the physically preferred video was the less faithful one in 51.5% of pairs, and DPO trained on these pairs drifted away from the prompt. PSDPO split the data into matching and conflict pairs and down-weighted conflict pairs by the size of their semantic gap, with a temperature &tau; chosen as a hyperparameter.</p></div>
<div class="pc-q"><i class="fas fa-arrow-down"></i> Is this a quirk of video generation?</div>
<div class="pc-step s-co"><span class="who">CoDPO</span><h4>The same structure appears elsewhere</h4><p>The conflict did not come from video itself. It came from the form of the supervision: a pairwise preference next to a criterion that scores each output on its own. Language-model alignment has the same form with length, correctness, or safety as the criterion. CoDPO therefore keeps PSDPO's definition of conflict pairs, replaces prompt fidelity with any pointwise criterion, and finds conflict rates of similar size, such as 57% on HelpSteer2 and 71% on GSM8K.</p></div>
<div class="pc-q"><i class="fas fa-arrow-down"></i> Why do conflict pairs cause drift, and do they always?</div>
<div class="pc-step s-co"><span class="who">CoDPO</span><h4>From conflict pairs alone to a balance</h4><p>PSDPO's analysis bounded the gradient contributed by conflict pairs and showed that the bound shrinks under stronger down-weighting. That justified down-weighting, but it looked at conflict pairs only. CoDPO instead follows the effect of each update on the constraint cost, and this brings the matching pairs into view: they pull the cost down while conflict pairs push it up. Drift therefore depends on the balance between the two groups, not on the conflict rate alone. Because the balance can be estimated from the data, the question of whether a dataset needs any correction can be answered before training. The resulting diagnostic, &rho;*<sub>eq</sub>, gave the right decision on all six domains tested.</p></div>
<div class="pc-q"><i class="fas fa-arrow-down"></i> How much down-weighting is enough?</div>
<div class="pc-step s-co"><span class="who">CoDPO</span><h4>Strength from the data, not from tuning</h4><p>The balance also says where to stop. Once the average weight on conflict pairs falls below a critical value, the pressure they exert is smaller than the repair from matching pairs, and the cost stops rising to first order. CoDPO keeps PSDPO's exponential weight, adds a sharpness parameter (PSDPO's weight is the case <i>p</i> = 1), and sets &tau; so that the average conflict weight equals &rho;*<sub>eq</sub>. The temperature that PSDPO had to tune is now computed.</p></div>
<div class="pc-q"><i class="fas fa-arrow-down"></i> What about drift that builds up during training?</div>
<div class="pc-step s-co"><span class="who">CoDPO</span><h4>From a fixed schedule to feedback</h4><p>&rho;*<sub>eq</sub> describes the balance at the start of training, and the balance moves as the model changes. During vanilla DPO training on HelpSteer2, the balance point went from 0.710 at the start to 0.603 later on. PSDPO handled drift during training with a fixed schedule: matching pairs first, conflict pairs later. CoDPO replaces the schedule with feedback. It measures the constraint risk on the training pairs as training runs and strengthens a margin shift only when that risk rises.</p></div>
</div>
</div>


<p class="pc-back"><a href="{{ base_path }}/notes/"><i class="fas fa-arrow-left"></i>&nbsp; All research notes</a></p>

</div>
