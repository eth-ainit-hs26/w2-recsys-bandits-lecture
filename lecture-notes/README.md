# Lecture notes, weekend 2, Friday

AI in Industry, ETH Zurich, HS26, weekend 2, Friday 13 November 2026.

08:15 to 12:00, nearest neighbors, matrix product, matrix factorization:

- `nearest-neighbors-and-matrix-factorization.pdf`: the notes, four pages.
- `nearest-neighbors-and-matrix-factorization.tex`: the source.
- `tools/notes_numbers.py`: computes every number of the notes from the games' data and writes `generated/`.

14:00 and 16:00, bandits and large-scale computing:

- `bandits-and-large-scale-computing.pdf`: the notes, four pages.
- `bandits-and-large-scale-computing.tex`: the source.
- `tools/afternoon_numbers.py`: computes every number of the notes from the games' data and the computing clusters
  deck, and writes `generated/bandits-*.tex` and `generated/computing-grid.tex`.

Build, from this folder:

```bash
python3 -I tools/notes_numbers.py
```

```bash
pdflatex nearest-neighbors-and-matrix-factorization.tex && pdflatex nearest-neighbors-and-matrix-factorization.tex
```

```bash
python3 -I tools/notes_numbers.py nearest-neighbors-and-matrix-factorization.pdf
```

The afternoon notes the same way, with `tools/afternoon_numbers.py` and `bandits-and-large-scale-computing`.

The games are on the course site, https://eth-ainit-hs26.github.io/AINIT-PAGE/ (weekend 2).
