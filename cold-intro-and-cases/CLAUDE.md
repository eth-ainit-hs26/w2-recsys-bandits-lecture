# CLAUDE.md : cold-intro-and-cases, the opening PDF of each block of weekend 2

Since 2026-11-12 (Carlos: "always put the cold intro with the business on top at the beginning before the rest of the
material ... make that for each block the first chip") the course site opens the Friday 08:15, 14:00 and 16:00 blocks
of weekend 2 with one PDF each: the block's cold intro (`../cold-intro-deck/`), then its business cases
(`../cases-deck/`). `merge.py` makes the three PDFs here by concatenating the built decks page by page; nothing here is
LaTeX. `README.md` has the table of files, sources, site files and chips.

## Build

```bash
python3 -I merge.py
```

Run it after a rebuild of any source deck, commit the three PDFs, then copy them to the course site
(`README.md`). It exits with an error when a page of an output differs in size or text from its source page.

## Traps

1. **pypdf prints "Annotation sizes differ: 1 vs. 0"** once per page that holds a link (five pages). The links are
   copied: each merged page has the same link annotations as its source page (checked on 2026-11-12).
2. **The decks' own bookmarks and page labels are dropped.** Beamer labels its pages, and the second deck's labels
   would start again at 1 in the middle of the file. The output has one bookmark per deck and no labels, so a viewer
   counts 1 to N. The page numbers printed on the case frames are the case deck's own.
3. **The 16:00 block's cold intro is `block5-computing-clusters.pdf`** (named for the Saturday block it opened until
   2026-11-11) and its case deck is `block4-parallelized-mf.pdf`; the output takes the block's name,
   `block4-large-scale-computing.pdf`.
4. **The Friday 11:00 block has no cold intro.** Its case deck (`../cases-deck/block2-matrix-factorization.pdf`, the
   chip "Business case, Spotify") is the first chip of its row on its own, with no file here.

## Maintenance contract

- This file is the working memory for this folder. After any major change here, meaning a new or removed output, a
  changed source deck or order, a changed build, or a new place where the PDFs are published, UPDATE THIS FILE AND
  `README.md` IN THE SAME COMMIT.
- Every subdirectory that holds work of its own carries its own CLAUDE.md, and that file must itself carry this
  same maintenance contract, including this propagation rule. When you create a subdirectory, create its
  CLAUDE.md at the same time.
- Keep it concrete: real file names, real identifiers, real commands. Record the gotchas that cost someone an
  hour. Do not restate what the code already says plainly.
- House style, from `/Users/carloscotrini/Documents/git_ainit/CLAUDE.md`: ASCII punctuation only in authored
  prose (no em dashes, no en dashes, never `--` as a dash).
