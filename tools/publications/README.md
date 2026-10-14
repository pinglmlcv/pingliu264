# Publications page generator

`_pages/publications.md` is generated. Do not edit it by hand; edit the data here and regenerate.

## Files

- `publications.yaml`: all publications, plus the list of titles shown under Selected Publications.
- `template.html`: page layout, styles, and the filter script.
- `generate.py`: reads the two files above and writes `_pages/publications.md`.

This folder is excluded from the Jekyll build in `_config.yml`, so nothing here is published.

## Add a paper

1. Add an entry under `publications:` in `publications.yaml`. Within the same year, entries appear in file order, so put new papers at the top of their year.

   ```yaml
   - title: 'Paper Title: With a Colon Needs Quotes'
     authors: First Author, <b>Ping Liu</b><sup>†</sup>
     venue: IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2027)
     year: 2027
     type: conference        # conference | journal | preprint
     badge: CVPR             # short name shown on the colored badge
     oral: true              # optional
     award: Best Paper Award # optional
     links:                  # optional
     - name: arXiv
       url: https://arxiv.org/abs/XXXX.XXXXX
   ```

2. To feature it, add its exact title to the `selected:` list.
3. Regenerate:

   ```bash
   pip install pyyaml
   python3 tools/publications/generate.py
   ```

Markup in `authors`: `<b>Ping Liu</b>` for bold, `<sup>†</sup>` for corresponding author, `<sup>♠</sup>` for equal contribution.

Badge colors are set in `COLORS` at the top of `generate.py`; badges not listed there are gray.
