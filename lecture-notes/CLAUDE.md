# CLAUDE.md : lecture-notes/

Lecture notes of the weekend 2 Friday blocks, A4, four pages each:

- 08:15 to 12:00: the inner product, the nearest neighbor classifier, the matrix product and matrix factorization.
  Asked for by Carlos on 2026-11-11: "Keep them terse and to the point. You may also refer to the visualizations on
  the website."
- 14:00 and 16:00: multi-armed bandits (Once Upon a Mirror), computing clusters, and matrix factorization on a grid
  of computers (Matchmaker on a Grid). Asked for by Carlos on 2026-11-12: "dispatch an agent that produces lecture
  notes now for the bandits, and then the large scale computing part." Built the same day in the form of the
  morning notes.

## Files

| File | What it is |
|---|---|
| `nearest-neighbors-and-matrix-factorization.tex` | The source. Five sections: the inner product; the nearest neighbor classifier; the matrix product; matrix factorization (the problem, one number at a time, gradient descent, predicting unknown ratings); games and notebooks. |
| `nearest-neighbors-and-matrix-factorization.pdf` | The built notes, committed. |
| `bandits-and-large-scale-computing.tex` | The source of the afternoon notes. Eight sections: multi-armed bandits (the game, the probability p, the estimate, the rate, the Queen's mirror, strategy, the exploration-exploitation dilemma); Random; estimate then exploit; epsilon-greedy; UCB (with the real UCB and all the mirrors); computing clusters; matrix factorization on a grid of computers; games, notebooks and slides. |
| `bandits-and-large-scale-computing.pdf` | The built afternoon notes, committed. |
| `generated/*.tex` | The tables and the TikZ figures, written by the tools: `bandits-*.tex` and `computing-grid.tex` by `afternoon_numbers.py`, the others by `notes_numbers.py`. Do not edit them. |
| `tools/notes_numbers.py` | Computes every number of the notes from copies of the games' data, checks the copies against `../../w2-cx-private` when that checkout is present, writes `generated/`, and with a PDF argument checks the built PDF. |
| `tools/afternoon_numbers.py` | The same for the afternoon notes: copies of the Mirror's data and of its simulation (`sim.js` in Python), of the grid sketch's data and of the clusters deck's numbers. Compares the copies with `../../w2-cx-private`, the seasons with `sim.js` morning by morning when `node` is on the PATH, and `DECK_NUMBERS` with the deck's source. About 8 seconds (10,000 seasons for each n of the challenge round). |

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

The afternoon notes, the same way:

```bash
python3 -I tools/afternoon_numbers.py
```

```bash
pdflatex bandits-and-large-scale-computing.tex && pdflatex bandits-and-large-scale-computing.tex
```

```bash
python3 -I tools/afternoon_numbers.py bandits-and-large-scale-computing.pdf
```

The last command of each set fails when the PDF has an en or em dash or lacks one of the numbers in `EXPECTED` (the
worked examples). A number written in the prose of the .tex must be added to `EXPECTED` with its value from the tool.

## Where the content comes from

- The data and the worked examples are those of the games on the course site: Once Upon a Video Store
  (`w2-cx-private/01_nearest_neighbours`) and the Matchmaker's parts one, two, three and the optional part
  (`w2-cx-private/02_matrix_factorization`). The tool's docstring names the file behind each copy.
- The notation is the games' notation (`01_nearest_neighbours/source/game/NOTATION.md` and
  `02_matrix_factorization/source/game/NOTATION.md` in `w2-cx-private`): ratings from -2 to 2, stars minus 3; the textbook cross, Q above PQ and P on its left; the loss
  `(prediction - rating)^2` with the prediction on the left; part two's nudge of 0.01, its slope nabla and
  `w <- w - alpha nabla` with alpha 0.02; gradient descent with alpha 0.02 in the optional part.
- The loss of a guess is the total of the known ratings' losses since 2026-11-11, as in the games (Carlos that day:
  "replace ... the average loss with the total loss so that we stay consistent with the literature"); until then the
  average. Part three's run takes alpha 3/117 on the total, the same steps as alpha 3 on the average of its 117 known
  ratings. `FORBIDDEN` in the tool fails the PDF check while "average" is left in the notes.
- Part three's ratings are MovieLens ml-latest-small, cited in a footnote (Harper and Konstan, ACM TiiS 2015).
- Afternoon notes, bandits: the story, the names, the notation and the seasons of `w2-cx-private/03_bandits`
  (`core.js`, `sim.js`, `sec1.js` to `sec5.js`). Every example is the race season (seed 103993, at Cinderella's,
  and at Rapunzel's in the table of all the mirrors): n = 20 for estimate then exploit, epsilon 0.2, the UCB board
  after 10 mornings; the challenge round of section 3 gives the best n (10,000 seasons, within 0.005 of the highest
  average rate). Each strategy is the game's numbered procedure: Initialize, Test, Highest estimate, Exploit;
  Initialize, Spin, Sample, Update; Initialize, Show the highest, Update, Repeat.
- Afternoon notes, large-scale computing: the clusters section takes its numbers from `../clusters-deck`
  (`DECK_NUMBERS` in the tool, each found in the deck's source, the frame named beside it). The grid section follows
  `w2-cx-private/02_matrix_factorization/grid-sketch` (`data.js`, `grid.html`): A computers hold the customers'
  slices, B computers the films', C computers the blocks of ratings; 15 computers of 21 places; the what-if on the
  Intouchables' first number (B2); alpha 0.014; the total loss.
- Left out of the afternoon notes, as briefed: the business cases and the cold intros (Graunt, Prony).
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
- A table beside its text: `\beside{table}{text}` in the afternoon notes measures the table with `\sbox` and gives
  the text the rest of the width, ragged right. Two minipages of fixed widths let a wide table run under the text
  beside it (the race table was 23pt wider than its minipage and printed over the words).
- The afternoon PDF check reads two extractions of the PDF: `pdftotext -layout` keeps a table's rows on one line but
  cuts a text set beside a table into the table's lines; `pdftotext -raw` keeps that text whole.
- A `\needspace` placed after a `\section` heading strands the heading at the foot of the page. Place it before the
  `\section`.
- In a justified paragraph a `\url` broke after `https:`, or ran 173pt into the margin when wrapped in an `\mbox`.
  The links paragraph of the afternoon notes is `\raggedright` with the address in an `\mbox`.
- In the grid figure, a box whose last line has a descender ("Apollo 13") sat 0.4 mm higher than its neighbours; a
  `\strut` at the end of each box's last line evens them.

## Publication

- The PDF is in this public repository, so a push also serves it from GitHub Pages.
- On the course site since 2026-11-11 (AINIT-PAGE `8bf143b`), with Carlos's request that day for one ZIP of the
  weekend: `public/slides/we2/ainit-hs26-lecture-notes-nearest-neighbors-and-matrix-factorization.pdf`, since
  AINIT-PAGE `9e0be17` the last chip of the Friday 11:00 row, "10 Lecture notes, nearest neighbors and matrix
  factorization" (the number comes from the agenda), the same in the Materials list and in the weekend's ZIP. Since
  AINIT-PAGE `c01c44e` (2026-11-12, Carlos: "put that next to download all slides and visualizations") off the
  agenda: a button beside the ZIP button, "Lecture notes, nearest neighbors and matrix factorization (PDF)", from
  `download.notes` of weekend 2 in `src/data/weekends.ts`, without a number, still in the Materials list and the
  ZIP. After a rebuild, copy the PDF over that file, push AINIT-PAGE, and the next deploy rebuilds the ZIP.
- The afternoon notes: in this repository since 2026-11-12, not on the course site that day.

## Maintenance contract

- This file is the working memory for this folder. After any major change here, meaning a new section, a
  changed build or check, new data or a changed data format, or a change of where the notes are published,
  UPDATE THIS FILE IN THE SAME COMMIT.
- Every subdirectory that holds work of its own carries its own CLAUDE.md, and that file must itself carry this
  same maintenance contract, including this propagation rule. When you create a subdirectory, create its
  CLAUDE.md at the same time.
- Keep it concrete: real file names, real identifiers, real commands. Record the gotchas that cost someone an
  hour. Do not restate what the code already says plainly.
