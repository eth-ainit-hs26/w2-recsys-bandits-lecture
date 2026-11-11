# CLAUDE.md : lecture-notes/

Lecture notes of the weekend 2 Friday blocks 08:15 to 12:00: the inner product, the nearest neighbor classifier,
the matrix product and matrix factorization. Asked for by Carlos on 2026-11-11: "Keep them terse and to the
point. You may also refer to the visualizations on the website." Four pages, A4.

## Files

| File | What it is |
|---|---|
| `nearest-neighbors-and-matrix-factorization.tex` | The source. Five sections: the inner product; the nearest neighbor classifier; the matrix product; matrix factorization (the problem, one number at a time, gradient descent, predicting unknown ratings); games and notebooks. |
| `nearest-neighbors-and-matrix-factorization.pdf` | The built notes, committed. |
| `generated/*.tex` | The tables and the two TikZ figures, written by the tool. Do not edit them. |
| `tools/notes_numbers.py` | Computes every number of the notes from copies of the games' data, checks the copies against `../../w2-cx-private` when that checkout is present, writes `generated/`, and with a PDF argument checks the built PDF. |

## Build

From inside this folder:

```bash
python3 -I tools/notes_numbers.py
```

```bash
pdflatex nearest-neighbors-and-matrix-factorization.tex && pdflatex nearest-neighbors-and-matrix-factorization.tex
```

```bash
python3 -I tools/notes_numbers.py nearest-neighbors-and-matrix-factorization.pdf
```

The last command fails when the PDF has an en or em dash or lacks one of the numbers in `EXPECTED` (the worked
examples). A number written in the prose of the .tex must be added to `EXPECTED` with its value from the tool.

## Where the content comes from

- The data and the worked examples are those of the games on the course site: Once Upon a Video Store
  (`w2-cx-private/01_nearest_neighbours`) and the Matchmaker's parts one, two, three and the optional part
  (`w2-cx-private/02_matrix_factorization`). The tool's docstring names the file behind each copy.
- The notation is the games' notation (`01_nearest_neighbours/source/game/NOTATION.md` and
  `02_matrix_factorization/source/game/NOTATION.md` in `w2-cx-private`): ratings from -2 to 2, stars minus 3; the textbook cross, Q above PQ and P on its left; the loss
  `(prediction - rating)^2` with the prediction on the left; part two's nudge of 0.01, its slope nabla and
  `w <- w - alpha nabla` with alpha 0.1; gradient descent with alpha 0.2 in the optional part.
- Part three's ratings are MovieLens ml-latest-small, cited in a footnote (Harper and Konstan, ACM TiiS 2015).
- The layout follows the "write dry" rule of Carlos's global CLAUDE.md for documents: black on white, one font,
  plain boxes and lines, a definition per item. The Codex plates deck style is for decks and is not used here.

## Gotchas

- Film names above a TikZ matrix: every head gets `text width=\headwidth`, where `\headwidth` is the width of the
  longest word of the figure's film names (set with `\settowidth` on a one-column tabular of the words), so the
  film columns are equally wide and no name is hyphenated. A `\strut` on the last line, `anchor=south` and
  `minimum height=0pt` put one-line and two-line names on one baseline. A `text depth` on such a head cuts the
  box after its first line (the text box is top-aligned), and the second line then hangs into the box of Q.
- `inner xsep` given in `column 1/.style` has no effect, because the matrix's `nodes={... inner sep=1pt}` wins.
  The customer names get it per cell, `|[inner xsep=4pt]| Sara`.
- The Colab addresses are wider than the text width even in `\scriptsize` (555pt in `\footnotesize` against
  455pt). Section 5 therefore prints the course site addresses in full and, for the notebooks, the repository
  address, with the words student and solutions linked to Colab. In a ragged table cell `\url` broke the
  addresses after `https:`.

## Publication

- The PDF is in this public repository, so a push also serves it from GitHub Pages.
- On the course site since 2026-11-11 (AINIT-PAGE `8bf143b`), with Carlos's request that day for one ZIP of the
  weekend: `public/slides/we2/ainit-hs26-lecture-notes-nearest-neighbors-and-matrix-factorization.pdf`, since
  AINIT-PAGE `9e0be17` the last chip of the Friday 11:00 row, "10 Lecture notes, nearest neighbors and matrix
  factorization" (the number comes from the agenda), the same in the Materials list and in the weekend's ZIP. After
  a rebuild, copy the PDF over that file, push AINIT-PAGE, and the next deploy rebuilds the ZIP.

## Maintenance contract

- This file is the working memory for this folder. After any major change here, meaning a new section, a
  changed build or check, new data or a changed data format, or a change of where the notes are published,
  UPDATE THIS FILE IN THE SAME COMMIT.
- Every subdirectory that holds work of its own carries its own CLAUDE.md, and that file must itself carry this
  same maintenance contract, including this propagation rule. When you create a subdirectory, create its
  CLAUDE.md at the same time.
- Keep it concrete: real file names, real identifiers, real commands. Record the gotchas that cost someone an
  hour. Do not restate what the code already says plainly.
