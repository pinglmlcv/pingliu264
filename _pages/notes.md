---
layout: archive
title: "Research Notes"
permalink: /notes/
author_profile: true
---

{% include base_path %}

<style>
.nt { --ink:#1f2a44; --muted:#5b6478; --line:#e6e9f0; --al:#5b4fc9; font-size:0.95em; line-height:1.7; color:var(--ink); }
.nt * { box-sizing:border-box; }
.nt-hero { background:linear-gradient(120deg,#3f3a9e 0%,#5b4fc9 60%,#7c6fe0 100%); color:#fff; border-radius:16px; padding:2em 2.2em 1.8em; margin:0.5em 0 2.2em; box-shadow:0 10px 30px rgba(60,48,150,0.16); }
.nt-hero h2 { color:#fff; border:0; margin:0 0 0.45em; padding:0; font-size:1.55em; }
.nt-hero p { margin:0; opacity:0.95; max-width:44em; }
.nt-list { display:grid; gap:1.2em; margin:0 0 2.4em; }
.nt-card { display:flex; gap:1.3em; align-items:stretch; background:#fff; border:1px solid var(--line); border-left:5px solid var(--c,var(--al)); border-radius:14px; padding:1.3em 1.5em; text-decoration:none !important; color:var(--ink) !important; box-shadow:0 4px 16px rgba(31,42,68,0.05); transition:box-shadow .15s, transform .15s; }
.nt-card:hover { box-shadow:0 8px 24px rgba(31,42,68,0.11); transform:translateY(-1px); }
.nt-no { font-size:2em; font-weight:800; line-height:1; color:var(--c,var(--al)); opacity:0.3; flex:0 0 1.6em; }
.nt-body { flex:1; }
.nt-k { display:block; font-size:0.68em; font-weight:700; text-transform:uppercase; letter-spacing:0.12em; color:var(--c,var(--al)); margin-bottom:0.3em; }
.nt-t { display:block; font-size:1.15em; font-weight:700; line-height:1.35; margin-bottom:0.4em; }
.nt-d { display:block; color:var(--muted); font-size:0.92em; line-height:1.6; }
.nt-tags { display:flex; flex-wrap:wrap; gap:0.45em; margin-top:0.7em; }
.nt-tags span { font-size:0.78em; border:1px solid var(--line); border-radius:999px; padding:0.12em 0.75em; background:#fafbfd; }
.nt-go { display:inline-block; margin-top:0.75em; font-size:0.86em; font-weight:600; color:var(--c,var(--al)); }
.nt-more { border:2px dashed var(--al); border-radius:14px; min-height:6.5em; display:flex; align-items:center; justify-content:center; color:var(--al); font-weight:700; font-size:1.2em; letter-spacing:0.04em; }
@media (max-width: 760px) { .nt-hero { padding:1.6em 1.3em; } .nt-card { padding:1.1em 1.1em; gap:0.8em; } .nt-no { font-size:1.5em; flex-basis:1.3em; } }
</style>

<div class="nt">

<div class="nt-hero">
<h2>How one paper leads to the next</h2>
<p>Each note follows one line of our work across papers: the question it started from, how later papers built on earlier ones, and where the line is heading.</p>
</div>

<div class="nt-list">
<a class="nt-card" style="--c:#7c3aed" href="{{ base_path }}/notes/preference-conflicts/">
<span class="nt-no">01</span>
<span class="nt-body">
<span class="nt-k">Verifiable rewards and alignment</span>
<span class="nt-t">From PSDPO to CoDPO: preference optimization under conflicting signals</span>
<span class="nt-d">When a preferred output scores worse on a pointwise criterion, preference optimization drifts away from that criterion. PSDPO found this in text-to-video generation; CoDPO explains when it happens in DPO and sets the correction from the data before training.</span>
<span class="nt-tags"><span>PSDPO · ACM MM 2026</span><span>CoDPO · NeurIPS 2026</span></span>
<span class="nt-go">Read the note &rarr;</span>
</span>
</a>
<div class="nt-more">More will be coming</div>
</div>

</div>
