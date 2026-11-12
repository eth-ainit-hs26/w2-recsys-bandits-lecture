# CLAUDE.md : clusters-deck, the computing clusters block of weekend 2

Beamer, lualatex, three passes, from this folder. One deck: `block5-computing-clusters.tex`, "Computing clusters",
the Saturday 14 November 2026 08:15 block of AINIT HS26 until 2026-11-11, when Carlos merged computing clusters with
parallelized matrix factorization: since then an item of the Friday 13 November 16:00 block "Large-scale
computing" (AINIT-PAGE `5ab848e`; the title page reads Friday 13 November 2026), since AINIT-PAGE `c01c44e`
(2026-11-12) after the block's opening PDF (its cold intro, then the case LinkedIn's ads, `../cold-intro-and-cases/`)
and before Matchmaker on a Grid. Built on 2026-11-10 as a port into Codex plates of the
first block of FDD weekend 7, "The cost of computation and supercomputers"
(`/Users/carloscotrini/Documents/git_fdd/projects/weekend-07-large-scale/carlos-lectures/slides/w7-cost-slides.tex`,
commit `b296f78`), with the cuts and changes Carlos dictated that day. `README.md` has the frame map against FDD's
slide numbers, the slides not ported with his reason, the changes made without asking and the open items. The
cold intro of the block, FDD's section "Dividing a computation, 1793", is a deck of `../cold-intro-deck/`.

## Layout

```
block5-computing-clusters.tex      the deck: 5 sections, 21 frames; a comment above each names its FDD slide
alps-platform-frame.tex            the two platform frames (a cabinet, a chassis, a blade; the blade types)
clusters-kit.tex                   styles and macros; its header maps FDD's style names to Codex plates
img/human-computers-1949.jpg       the photograph of slide 2; img/SOURCES.md
tools/check_port.py                every number on the slides is FDD's or a listed added fact
block5-computing-clusters.pdf, block5-computing-clusters-handout.pdf    the deliverables, rebuild and recommit together
```

## Build and check

```bash
../style/tools/build.sh block5-computing-clusters.tex
../style/tools/check.sh block5-computing-clusters.pdf
python3 ../style/tools/check_overlays.py block5-computing-clusters.pdf
python3 tools/check_port.py
python3 ../style/tools/make_handout.py block5-computing-clusters.pdf block5-computing-clusters-handout.pdf
python3 ../style/tools/render_board.py block5-computing-clusters.pdf <outdir>
```

`render_board.py` writes the last click of each frame as a PNG and a contact sheet. Read every frame after a
change: the checks find no overlap of text.

## Traps

1. **"FDD slide N" is the number printed on FDD's slide.** It counts FDD's title page and its section dividers,
   and it is the number Carlos uses ("slide 17 about CSCS"). The count of `\begin{frame}` in FDD's source differs.
2. **Every number comes from FDD or from the list in `tools/check_port.py`.** A new number needs an FDD source or
   a new entry in `ADDED` with its source. pdftotext reads a power of ten as one number ("10^12" as "1012"); the
   script splits it again.
3. **The platform facts were checked against HPE and CSCS** (README.md, section Numbers). FDD's notes had a
   conflict on the GH200 per blade; HPE's QuickSpecs give two nodes of four. The header of
   `alps-platform-frame.tex` lists what was left out and why.
4. **A sheet whose last row holds two lines** needs `\renewcommand{\cxsheetextra}{3.8}` inside its picture
   (slide 2): `\cxsheet` makes every row the same height.
5. **Boxes wrap and hyphenate when narrow.** At `\normalsize` a `box` of 23 mm holds "one multiply" on one line;
   the boxes of slides 17 and 18 are 32 and 34 mm wide to stay on two lines. Render after any change of wording.
6. **pdftotext also returns the parts not yet shown**, because `visible on` makes them transparent. Count the
   words of a frame on its last page.
7. **The write hooks** reject Unicode dashes, a double hyphen used as a dash and the contrastive negations named
   in the House style of `git_ainit/CLAUDE.md`. TikZ paths use `to`.
8. **This repository is public and a push to main publishes it on GitHub Pages**, the PDFs included. The course
   site serves its own copies (README.md, section "On the course site"): after a rebuild, copy them there again.

## Maintenance contract

- This file is the working memory for this folder. After any major change here, meaning a frame added, removed or
  reworded, a changed number or source, a changed build or check procedure, or a new place where the deck is
  published, UPDATE THIS FILE AND `README.md` IN THE SAME COMMIT.
- Every subdirectory that holds work of its own carries its own CLAUDE.md, and that file must itself carry this
  same maintenance contract, including this propagation rule. When you create a subdirectory, create its
  CLAUDE.md at the same time.
- Keep it concrete: real file names, real identifiers, real commands. Record the gotchas that cost someone an
  hour. Do not restate what the code already says plainly.
- House style, from `/Users/carloscotrini/Documents/git_ainit/CLAUDE.md`: ASCII punctuation only in authored
  prose (no em dashes, no en dashes, never `--` as a dash).
