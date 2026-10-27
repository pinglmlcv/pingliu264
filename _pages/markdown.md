---
layout: archive
permalink: /markdown/
title: "Mentoring and Service"
author_profile: true
redirect_from: 
  - /md/
  - /markdown.html
---

{% include base_path %}

<style>
.sv { --ink:#1f2a44; --muted:#5b6478; --line:#e6e9f0; --a:#4b4fc9; --b:#0e8a83; font-size:0.95em; line-height:1.65; color:var(--ink); }
.sv * { box-sizing:border-box; }
.sv-stats { display:grid; grid-template-columns:repeat(4,1fr); gap:0.9em; margin:0.4em 0 2.6em; }
.sv-stat { border-radius:14px; padding:1.1em 1em; color:#fff; box-shadow:0 8px 22px rgba(31,42,68,0.12); }
.sv-stat .n { font-size:2em; font-weight:800; line-height:1; display:block; }
.sv-stat .l { font-size:0.8em; opacity:0.92; display:block; margin-top:0.45em; line-height:1.35; }
.sv-h { display:flex; align-items:center; gap:0.7em; margin:0 0 1.1em; }
.sv-h .ic { width:2.3em; height:2.3em; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#fff; flex:none; }
.sv-h h2 { margin:0; padding:0; border:0; font-size:1.3em; }
.sv-sec { margin:0 0 2.8em; }
.sv-students { display:grid; grid-template-columns:1fr 1fr; gap:1em; }
.sv-stu { background:#fff; border:1px solid var(--line); border-radius:14px; padding:1.2em; box-shadow:0 4px 16px rgba(31,42,68,0.06); display:flex; gap:1em; }
.sv-av { width:3.2em; height:3.2em; border-radius:50%; flex:none; display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700; font-size:1.05em; }
.sv-stu b { font-size:1.05em; display:block; }
.sv-stu .yr { font-size:0.8em; color:var(--muted); display:block; margin-bottom:0.5em; }
.sv-stu .ed { font-size:0.86em; color:var(--muted); display:block; line-height:1.5; }
.sv-chips { display:flex; flex-wrap:wrap; gap:0.4em; margin-top:0.6em; }
.sv-chip { font-size:0.74em; padding:0.2em 0.65em; border-radius:999px; background:#eef0ff; color:#3b3fb5; font-weight:600; white-space:nowrap; }
.sv-tl { position:relative; margin:0; padding:0 0 0 1.4em; list-style:none; }
.sv-tl:before { content:""; position:absolute; left:0.42em; top:0.4em; bottom:0.4em; width:2px; background:linear-gradient(180deg,var(--a),var(--b)); border-radius:2px; }
.sv-tl li { position:relative; background:#fff; border:1px solid var(--line); border-radius:12px; padding:0.8em 1em; margin:0 0 0.75em; }
.sv-tl li:before { content:""; position:absolute; left:-1.32em; top:1.05em; width:0.75em; height:0.75em; border-radius:50%; background:#fff; border:3px solid var(--a); }
.sv-tl .yr { display:inline-block; font-size:0.72em; font-weight:700; color:#fff; background:var(--a); border-radius:6px; padding:0.1em 0.55em; margin-right:0.5em; }
.sv-tl .role { font-size:0.78em; font-weight:600; color:var(--b); text-transform:uppercase; letter-spacing:0.06em; }
.sv-tl .t { display:block; font-weight:600; margin-top:0.25em; line-height:1.4; }
.sv-tl .v { display:block; font-size:0.86em; color:var(--muted); }
.sv-grid2 { display:grid; grid-template-columns:1fr 1fr; gap:1em; }
.sv-box { background:#fff; border:1px solid var(--line); border-radius:14px; padding:1.1em 1.2em; box-shadow:0 4px 16px rgba(31,42,68,0.05); border-top:4px solid var(--k); }
.sv-box h3 { margin:0 0 0.7em; padding:0; border:0; font-size:0.85em; text-transform:uppercase; letter-spacing:0.1em; color:var(--k); }
.sv-row { display:flex; justify-content:space-between; gap:1em; padding:0.45em 0; border-bottom:1px dashed var(--line); font-size:0.9em; }
.sv-row:last-child { border-bottom:0; }
.sv-row .y { color:var(--muted); white-space:nowrap; font-size:0.92em; }
.sv-tags { display:flex; flex-wrap:wrap; gap:0.45em; }
.sv-tag { font-size:0.8em; padding:0.3em 0.8em; border-radius:8px; background:#f3f5f9; border:1px solid var(--line); }
.sv-tag.conf { background:#e5f6f4; border-color:#bfe7e2; color:#0b5f5a; font-weight:600; }
.sv-tag small { color:var(--muted); font-weight:400; margin-left:0.4em; }
.sv-sub { font-size:0.8em; text-transform:uppercase; letter-spacing:0.1em; color:var(--muted); margin:1.2em 0 0.6em; }
.sv-ws { border:1px solid #e2e8f0; border-left:3px solid #B4C7E7; border-radius:4px; background:#fff; margin:0 0 1.4em; overflow:hidden; }
.sv-ws-top { display:grid; grid-template-columns:150px 1fr; gap:1.2em; padding:1.1em 1.2em; background:color-mix(in srgb, #DAE3F3 45%, white); align-items:center; }
.sv-ws-top img { width:100%; border-radius:3px; border:1px solid #e2e8f0; background:#fff; display:block; }
.sv-ws-tag { display:inline-block; font-size:0.75em; font-variant:small-caps; letter-spacing:0.06em; color:#7a6214; border:1px solid #FFD966; border-radius:2px; padding:0 0.5em; margin-bottom:0.35em; background:#fff; }
.sv-ws-top b.tt { display:block; font-size:1.05em; line-height:1.35; margin-bottom:0.3em; }
.sv-ws-top .m { display:block; color:var(--muted); font-size:0.88em; line-height:1.5; }
.sv-ws-links { margin-top:0.55em; display:flex; flex-wrap:wrap; gap:0.45em; }
.sv-ws-links a { font-size:0.8em; border:1px solid #B4C7E7; border-radius:2px; padding:0.1em 0.75em; text-decoration:none !important; background:#fff; }
.sv-ws-body { padding:0.9em 1.2em 1em; font-size:0.9em; }
.sv-ws-body p { margin:0 0 0.6em; }
.sv-ws-body .k { font-variant:small-caps; letter-spacing:0.06em; color:#5f8389; font-weight:600; margin-right:0.4em; }
@media (max-width: 760px) { .sv-ws-top { grid-template-columns:1fr; } .sv-ws-top img { max-width:160px; } }
@media (max-width: 760px) { .sv-stats { grid-template-columns:1fr 1fr; } .sv-students, .sv-grid2 { grid-template-columns:1fr; } }
</style>

<div class="sv">
<div class="sv-sec">
<div class="sv-h"><div class="ic" style="background:#4b4fc9"><i class="fas fa-user-graduate"></i></div><h2>Ph.D. Students</h2></div>
<div class="sv-students">
<div class="sv-stu"><div class="sv-av" style="background:linear-gradient(135deg,#4b4fc9,#14a098)">SM</div><div><b>Siwei Meng</b><span class="yr">Ph.D. student, Fall 2024 to present</span><span class="ed">Bachelor's degree, South China University of Technology; Master's degree, Shenzhen University</span><div class="sv-chips"><span class="sv-chip">NeurIPS 2026</span><span class="sv-chip">ECCV 2026</span><span class="sv-chip">ACM MM 2026 Oral</span><span class="sv-chip">IJCAI 2025</span></div></div></div>
<div class="sv-stu"><div class="sv-av" style="background:linear-gradient(135deg,#d9822b,#c2410c)">XH</div><div><b>Xinyu Hu</b><span class="yr">Ph.D. student, Fall 2026 to present</span><span class="ed">Bachelor's degree, Duke Kunshan University</span></div></div>
</div>
</div>

<div class="sv-sec">
<div class="sv-h"><div class="ic" style="background:#0e8a83"><i class="fas fa-users"></i></div><h2>Workshop and Challenge Organization</h2></div>
<div class="sv-ws">
<div class="sv-ws-top">
<img src="{{ base_path }}/images/workshops-mirai-logo.jpg" alt="MIRAI Driving workshop logo">
<div>
<span class="sv-ws-tag">Upcoming · Co-Organizer</span>
<b class="tt">MIRAI Driving: Multimodal Intelligence and Reasoning for Autonomous and Intelligent Driving</b>
<span class="m">ACCV 2026 Workshop · Monday, 15 December 2026, afternoon</span>
<span class="m">Grand Cube Osaka (Osaka International Convention Center), Room 1007, Osaka, Japan</span>
<div class="sv-ws-links"><a href="https://mengsiwei.github.io/MIRAI_ACCV_Workshop/">Workshop website</a><a href="https://accv2026.org/workshops/">ACCV 2026 workshops</a></div>
</div>
</div>
<div class="sv-ws-body">
<p>An invited half-day workshop on multimodal perception, foundation models, and world models for autonomous driving, with keynotes, invited talks, and a panel bringing together academia and industry.</p>
<p><span class="k">Keynotes</span>Ziran Wang (Purdue University), Runsheng Xu (Waymo), Heye Huang (KAIST), Takahiro Ogawa (Hokkaido University)</p>
</div>
</div>
<ul class="sv-tl">
<li><span class="yr">2026</span><span class="role">Co-Organizer</span><span class="t">SynthIR: The First Workshop on Synthetic Content in Information Retrieval Ecosystems</span><span class="v">SIGIR 2026 Workshop</span></li>
<li><span class="yr">2026</span><span class="role">Co-Organizer</span><span class="t">Physics-Driven AIGC: Physically-Consistent Video, 4D Scene, and World Generation</span><span class="v">ICME 2026 Workshop</span></li>
<li><span class="yr">2026</span><span class="role">Program Committee</span><span class="t">DFX: Explainable Deepfake Detection Challenge</span><span class="v">ACM Multimedia 2026 Grand Challenge</span></li>
<li><span class="yr">2024</span><span class="role">Co-Organizer</span><span class="t">Efficient Learning for Face Analysis</span><span class="v">WACV 2024 Workshop</span></li>
<li><span class="yr">2022</span><span class="role">Co-Organizer</span><span class="t">Learning with Limited Data for Face Analysis</span><span class="v">ACCV 2022 Workshop</span></li>
</ul>
</div>

<div class="sv-sec">
<div class="sv-h"><div class="ic" style="background:#d9822b"><i class="fas fa-gavel"></i></div><h2>Conference Leadership</h2></div>
<div class="sv-grid2">
<div class="sv-box" style="--k:#4b4fc9"><h3>Area Chair</h3>
<div class="sv-row"><span>ACM Multimedia (MM)</span><span class="y">2022-2026</span></div>
<div class="sv-row"><span>International Joint Conference on Neural Networks (IJCNN)</span><span class="y">2026</span></div>
<div class="sv-row"><span>International Joint Conference on Artificial Intelligence (IJCAI)</span><span class="y">2025</span></div>
<div class="sv-row"><span>IEEE Conference on Multimedia Information Processing and Retrieval (MIPR)</span><span class="y">2022</span></div>
<div class="sv-row"><span>Asian Conference on Machine Learning (ACML)</span><span class="y">2021</span></div>
</div>
<div class="sv-box" style="--k:#0e8a83"><h3>Senior PC Member / Meta Reviewer</h3>
<div class="sv-row"><span>AAAI Conference on Artificial Intelligence</span><span class="y">2021, 2023-2027</span></div>
<div class="sv-row"><span>International Joint Conference on Artificial Intelligence (IJCAI)</span><span class="y">2026</span></div>
</div>
</div>
</div>

<div class="sv-sec">
<div class="sv-h"><div class="ic" style="background:#c2410c"><i class="fas fa-university"></i></div><h2>University Service, University of Nevada, Reno</h2></div>
<div class="sv-grid2">
<div class="sv-box" style="--k:#c2410c"><h3>Department Committees</h3>
<div class="sv-row"><span>Graduate Committee, Computer Science and Engineering</span><span class="y">2025-present</span></div>
<div class="sv-row"><span>Annual Evaluation Committee, Computer Science and Engineering</span><span class="y">2025-present</span></div>
</div>
<div class="sv-box" style="--k:#d9822b"><h3>Ph.D. Proposal Defense Committees</h3>
<div class="sv-row"><span>Khalid Rafiq</span><span class="y">2026</span></div>
<div class="sv-row"><span>Jiahao Xu</span><span class="y">2026</span></div>
<div class="sv-row"><span>Zikai Zhang</span><span class="y">2025</span></div>
</div>
</div>
</div>

<div class="sv-sec">
<div class="sv-h"><div class="ic" style="background:#5b6478"><i class="fas fa-search"></i></div><h2>Reviewing</h2></div>
<div class="sv-sub">Conferences</div>
<div class="sv-tags">
<span class="sv-tag conf">CVPR<small>2019-2022, 2024</small></span>
<span class="sv-tag conf">ICCV<small>2017-2023</small></span>
<span class="sv-tag conf">ECCV<small>2020-2024</small></span>
<span class="sv-tag conf">ICML<small>2018-2022, 2024, 2026</small></span>
<span class="sv-tag conf">NeurIPS<small>2016-2023</small></span>
<span class="sv-tag conf">ICLR<small>2018, 2020-2025, 2027</small></span>
<span class="sv-tag conf">AAAI<small>2017-2018, 2020</small></span>
</div>
<div class="sv-sub">Journals</div>
<div class="sv-tags">
<span class="sv-tag">IJCV</span><span class="sv-tag">IEEE TPAMI</span><span class="sv-tag">IEEE TIP</span><span class="sv-tag">IEEE TMM</span><span class="sv-tag">IEEE TCSVT</span><span class="sv-tag">IEEE TNNLS</span><span class="sv-tag">IEEE TAFFC</span><span class="sv-tag">IEEE TCYB</span><span class="sv-tag">IEEE TAI</span><span class="sv-tag">IEEE TIE</span><span class="sv-tag">IEEE TCE</span><span class="sv-tag">IEEE TETCI</span><span class="sv-tag">IEEE SPL</span><span class="sv-tag">Artificial Intelligence</span><span class="sv-tag">Neural Networks</span><span class="sv-tag">Machine Learning</span><span class="sv-tag">Pattern Recognition</span><span class="sv-tag">Pattern Recognition Letters</span><span class="sv-tag">Image and Vision Computing</span><span class="sv-tag">Knowledge-Based Systems</span>
</div>
</div>
</div>
