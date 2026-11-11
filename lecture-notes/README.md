# Lecture notes: nearest neighbors, matrix product, matrix factorization

AI in Industry, ETH Zurich, HS26, weekend 2, Friday 13 November 2026, 08:15 to 12:00.

- `nearest-neighbors-and-matrix-factorization.pdf`: the notes, four pages.
- `nearest-neighbors-and-matrix-factorization.tex`: the source.
- `tools/notes_numbers.py`: computes every number of the notes from the games' data and writes `generated/`.

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

The games are on the course site, https://eth-ainit-hs26.github.io/AINIT-PAGE/ (weekend 2).
