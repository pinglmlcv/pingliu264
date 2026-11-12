---
layout: archive
title: "When Preferences and Scores Disagree"
permalink: /research/preference-conflicts/
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
.pc-back { font-size:0.88em; margin:0 0 2em; }
@media (max-width: 760px) {
  .pc-hero { padding:1.6em 1.3em; } .pc-sec { padding:1.4em 1.1em; }
  .pc-res, .pc-take { grid-template-columns:1fr; }
  .pc-paper { flex-direction:column; gap:0.5em; } .pc-venue { flex:none; padding:0.3em 0.8em; }
}
</style>

<div class="pc">

<div class="pc-hero">
<p class="k">Research note · Verifiable Rewards, Alignment, and Agents</p>
<h2>Two papers, one problem: PSDPO and CoDPO</h2>
<p>Preference optimization learns from pairwise judgments: of two outputs, which one is better. The same models are also judged by pointwise criteria: is this video faithful to its prompt, is this answer correct, is it safe. Two of our papers study what happens when these two signals point in opposite directions. PSDPO addresses it in text-to-video generation, where physical preferences conflict with prompt fidelity. CoDPO analyzes it for direct preference optimization in general and asks whether the conflict will hurt before training starts.</p>
<div class="pc-jump"><a href="#problem"><i class="fas fa-random"></i>&nbsp; The shared problem</a><a href="#psdpo"><i class="fas fa-film"></i>&nbsp; PSDPO</a><a href="#codpo"><i class="fas fa-chart-line"></i>&nbsp; CoDPO</a><a href="#compare"><i class="fas fa-columns"></i>&nbsp; How they relate</a></div>
</div>

<div class="pc-sec al" id="problem">
<div class="pc-head"><div class="pc-num">01</div><h2><span class="pc-tag">The shared problem</span>Pairwise preferences and pointwise scores</h2></div>
<p>Direct preference optimization (DPO) trains on pairs. For a prompt <i>x</i>, one output <i>y</i><sub>w</sub> is preferred over another output <i>y</i><sub>l</sub>, and the update raises the likelihood of <i>y</i><sub>w</sub> relative to <i>y</i><sub>l</sub>. Separately, each output can be scored on its own by a pointwise criterion <i>s</i>(<i>y</i>): semantic agreement with the prompt, length, correctness, or safety.</p>
<p>The two signals usually agree, but not always. We call a pair a <b>matching pair</b> when the preferred output also scores at least as well, <i>s</i>(<i>y</i><sub>w</sub>) &ge; <i>s</i>(<i>y</i><sub>l</sub>), and a <b>conflict pair</b> when the preferred output scores worse. Standard DPO applies the same update to both kinds. On a conflict pair, that update raises the likelihood of the lower-scoring output, so it moves the model toward outputs that score worse on the criterion. When conflict pairs make up a large share of the data, these updates accumulate, and the pointwise criterion can degrade even while the model fits the preferences better.</p>

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
<text x="180" y="140" text-anchor="middle" font-size="12" fill="#5b6478">pointwise score s(y)</text>
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
<text x="180" y="140" text-anchor="middle" font-size="12" fill="#5b6478">pointwise score s(y)</text>
<rect x="35" y="150" width="240" height="16" rx="4" fill="#e6e9f0"/><rect x="35" y="150" width="105" height="16" rx="4" fill="#c2410c"/>
<rect x="35" y="174" width="240" height="16" rx="4" fill="#e6e9f0"/><rect x="35" y="174" width="206" height="16" rx="4" fill="#9aa3b8"/>
<text x="285" y="163" font-size="12" fill="#1f2a44">y<tspan baseline-shift="sub" font-size="10">w</tspan></text><text x="285" y="187" font-size="12" fill="#1f2a44">y<tspan baseline-shift="sub" font-size="10">l</tspan></text>
<text x="180" y="215" text-anchor="middle" font-size="12.5" fill="#c2410c">DPO pushes toward the lower score</text>
</svg></div>
<figcaption><b>Two kinds of preference pairs.</b> In both pairs the preferred output is <i>y</i><sub>w</sub>, so standard DPO raises its likelihood. In a matching pair this also favors the output with the higher pointwise score. In a conflict pair it favors the output with the lower score, which is the source of the degradation both papers address.</figcaption>
</figure>
</div>

<div class="pc-sec ps" id="psdpo">
<div class="pc-head"><div class="pc-num">02</div><h2><span class="pc-tag">Text-to-video generation · ACM MM 2026, Oral</span>PSDPO: physical preferences meet semantic constraints</h2></div>
<p>Preference optimization can make generated videos more physically plausible, but it often makes them less faithful to the prompt. PSDPO traces this to how the two signals are obtained. Physical plausibility is judged by comparing the dynamics of two videos, so it is a pairwise signal. Prompt fidelity is checked one video at a time against its prompt, so it is a pointwise signal. In our training data, the physically preferred video was the less faithful one in 51.5% of pairs. A typical case: the prompt asks for a lemon slice, and the physically more convincing video shows a whole lemon. Training on such a pair rewards the model for drifting away from the prompt.</p>

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
<div class="pc-head"><div class="pc-num">03</div><h2><span class="pc-tag">Direct preference optimization · NeurIPS 2026</span>CoDPO: diagnosing and correcting constraint drift</h2></div>
<p>CoDPO studies the same tension without tying it to one domain. Preference data is routinely paired with pointwise criteria such as response length, correctness, or safety scores, and standard DPO does not distinguish pairs that help a criterion from pairs that hurt it. We call the resulting failure <b>constraint drift</b>. Conflict pairs push the criterion's cost up and matching pairs push it down, so whether a training run drifts depends on the balance between the two groups.</p>

<h3>Method</h3>
<ol class="pc-steps">
<li><b>Diagnose before training.</b> A first-order analysis of DPO's updates yields a closed-form quantity, &rho;*<sub>eq</sub>, computed from dataset statistics. It indicates whether a dataset will correct itself during training or needs intervention, so the decision can be made before any compute is spent on alignment.</li>
<li><b>Down-weight conflict pairs.</b> Conflict pairs receive a per-sample control whose strength is set from the diagnostic. This control carries the main part of the drift regulation.</li>
<li><b>Correct the residual.</b> An adaptive margin shift during training corrects the residual drift that the per-sample control does not cover.</li>
</ol>

<h3>Evaluation</h3>
<div class="pc-pills">
<span class="pc-pill"><b>6</b> domains</span>
<span class="pc-pill"><b>4</b> base-model architectures</span>
<span class="pc-pill">several preference losses</span>
<span class="pc-pill">baselines: hard filtering, constrained and multi-objective methods</span>
</div>
<p>Across these settings, drift grows with exposure to conflict pairs, the diagnostic tracks where drift appears in practice, and CoDPO reduces drift while keeping most of the preference learning of vanilla DPO. Its trade-off between drift and preference performance is better than that of hard filtering and recent constrained and multi-objective baselines.</p>

<div class="pc-paper"><span class="pc-venue" style="background:#7c3aed">NeurIPS 2026</span><div><span class="t">When Scores Conflict with Preferences: Pre-Alignment Diagnosis and Adaptive Correction of Constraint Drift in DPO</span><span class="a"><b>Ping Liu</b>, Yan Yan</span><span class="l"><a href="https://arxiv.org/abs/2611.07375">arXiv</a></span></div></div>
</div>

<div class="pc-sec al" id="compare">
<div class="pc-head"><div class="pc-num">04</div><h2><span class="pc-tag">Connection and difference</span>How the two papers relate</h2></div>
<p>Both papers start from the same observation: a preference pair is not equally trustworthy when a pointwise criterion disagrees with it, and treating all pairs alike lets that disagreement leak into the trained model. They differ in scope and in how the correction is set. PSDPO is a method for one important setting, physically plausible video generation, where the conflict rate is high and the semantic signal is available for every video. CoDPO steps back to direct preference optimization in general, explains when conflict pairs cause drift, and uses that explanation to decide in advance how much correction a dataset needs.</p>
<div class="pc-tw">
<table class="pc-tbl">
<thead><tr><th></th><th class="ps">PSDPO</th><th class="co">CoDPO</th></tr></thead>
<tbody>
<tr><td>Setting</td><td>Text-to-video generation</td><td>Direct preference optimization across domains</td></tr>
<tr><td>Pairwise signal</td><td>Physical plausibility, judged by comparing two videos</td><td>Preference labels in the training data</td></tr>
<tr><td>Pointwise criterion</td><td>Prompt fidelity, scored per video by ViCLIP</td><td>Criteria such as length, correctness, or safety</td></tr>
<tr><td>Treatment of conflict pairs</td><td>Exponential down-weighting by the size of the semantic gap</td><td>Per-sample control plus an adaptive margin shift</td></tr>
<tr><td>How strong the correction is</td><td>Set by the temperature &tau;</td><td>Set by the pre-alignment diagnostic &rho;*<sub>eq</sub></td></tr>
<tr><td>During training</td><td>Matching pairs first, then all pairs with weights</td><td>Margin adjusted during training for residual drift</td></tr>
<tr><td>Prediction before training</td><td>Not part of the method</td><td>Central: whether the data self-corrects or needs intervention</td></tr>
<tr><td>Evaluation</td><td>Wan 1.3B on VBench, VideoPhy-2, and PhyGenBench</td><td>Six domains, four architectures, several preference losses</td></tr>
</tbody>
</table>
</div>

<h3>What the two papers share</h3>
<div class="pc-take">
<div class="pc-card"><i class="fas fa-search"></i><b>Measure the conflict</b>Both papers separate matching pairs from conflict pairs before deciding how to train, rather than assuming the preference labels and the criterion agree.</div>
<div class="pc-card"><i class="fas fa-sliders-h"></i><b>Discount, do not discard</b>Both keep conflict pairs in training at reduced weight, so the useful part of their preference signal is not thrown away with the conflicting part.</div>
<div class="pc-card"><i class="fas fa-check-double"></i><b>Check the signal itself</b>Both treat the training signal as something to verify, which is the theme of our work on <a href="{{ base_path }}/research/#alignment">verifiable rewards and alignment</a>.</div>
</div>
</div>

<p class="pc-back"><a href="{{ base_path }}/research/"><i class="fas fa-arrow-left"></i>&nbsp; Back to Research</a></p>

</div>
