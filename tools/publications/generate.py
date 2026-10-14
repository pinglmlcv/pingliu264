#!/usr/bin/env python3
"""Regenerate _pages/publications.md from publications.yaml and template.html.

Usage (from the repository root or from this folder):
    pip install pyyaml
    python3 tools/publications/generate.py
"""
import os
import sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA = os.path.join(HERE, "publications.yaml")
TEMPLATE = os.path.join(HERE, "template.html")
OUTPUT = os.path.join(ROOT, "_pages", "publications.md")

# Badge colors by venue short name; anything not listed uses DEFAULT_COLOR.
COLORS = {
    "NeurIPS": "#7c3aed", "ICML": "#c2410c", "ICLR": "#7a4cc2",
    "CVPR": "#2f6fd6", "ICCV": "#1e40af", "ECCV": "#1d4ed8",
    "ACM MM": "#0f766e", "ICME": "#0e8a83",
    "AAAI": "#b45309", "IJCAI": "#a16207",
    "TPAMI": "#9f1239", "IJCV": "#9f1239", "TMLR": "#475569",
    "arXiv": "#b91c1c",
}
DEFAULT_COLOR = "#64748b"
VALID_TYPES = {"conference", "journal", "preprint"}


def card(p, data_type):
    color = COLORS.get(p["badge"], DEFAULT_COLOR)
    tags = ""
    if p.get("oral"):
        tags += '<span class="pb-flag">Oral</span>'
    if p.get("award"):
        tags += f'<span class="pb-flag gold">{p["award"]}</span>'
    links = "".join(f'<a href="{l["url"]}">{l["name"]}</a>' for l in p.get("links", []))
    links = f'<span class="pb-links">{links}</span>' if links else ""
    return (
        f'<li class="pb-item" data-type="{data_type}">'
        f'<span class="pb-badge" style="background:{color}">{p["badge"]}<em>{p["year"]}</em></span>'
        f'<div class="pb-body"><span class="pb-t">{p["title"]}</span>{tags}'
        f'<span class="pb-a">{p["authors"]}</span>'
        f'<span class="pb-v">{p["venue"]}</span>{links}</div></li>'
    )


def main():
    data = yaml.safe_load(open(DATA, encoding="utf-8"))
    pubs = data["publications"]
    for p in pubs:
        for key in ("title", "authors", "venue", "year", "type", "badge"):
            if key not in p:
                sys.exit(f"Missing '{key}' in entry: {p.get('title', p)}")
        if p["type"] not in VALID_TYPES:
            sys.exit(f"Unknown type '{p['type']}' in: {p['title']}")

    by_title = {p["title"]: p for p in pubs}
    selected = []
    for t in data.get("selected", []):
        if t not in by_title:
            sys.exit(f"Selected title not found in publications: {t}")
        selected.append(by_title[t])

    # Newest year first; within a year keep the order in the YAML file.
    ordered = sorted(pubs, key=lambda p: -int(p["year"]))
    body, year = [], None
    for p in ordered:
        if p["year"] != year:
            if year is not None:
                body.append("</ul>")
            year = p["year"]
            body.append(f'<div class="pb-year" data-year="{year}"><span>{year}</span></div><ul class="pb-list">')
        body.append(card(p, p["type"]))
    body.append("</ul>")

    page = open(TEMPLATE, encoding="utf-8").read()
    page = page.replace("%%SEL%%", "".join(card(p, "selected") for p in selected))
    page = page.replace("%%ALL%%", "\n".join(body))
    open(OUTPUT, "w", encoding="utf-8").write(page)

    counts = {t: sum(p["type"] == t for p in pubs) for t in sorted(VALID_TYPES)}
    print(f"Wrote {OUTPUT}: {len(selected)} selected, {counts}")


if __name__ == "__main__":
    main()
