# CLAUDE.md : cold-intro-and-cases, the opening PDF of each block of weekend 2

Since 2026-11-12 (Carlos: "always put the cold intro with the business on top at the beginning before the rest of the
material ... make that for each block the first chip") the course site opens the Friday 08:15, 14:00 and 16:00 blocks
of weekend 2 with one PDF each: the block's cold intro (`../cold-intro-deck/`), then its business cases
(`../cases-deck/`). The 16:00 PDF ends with the clusters deck (`../clusters-deck/`) since AINIT-PAGE `5c1a936`, the
same day (Carlos: "Notice the slides on large-scale computing and computing clusters. Merge them, I meant"; his order
that morning: "large-scale computing cold intro with business case, LinkedIn ads, then computing clusters"). `merge.py`
makes the three PDFs here by concatenating the built decks page by page; nothing here is LaTeX. `README.md` has the
table of files, sources, site files and chips.

## Build

```bash
python3 -I merge.py
```

Run it after a rebuild of any source deck, commit the three PDFs, then copy them to the course site
(`README.md`). It exits with an error when a page of an output differs in size or text from its source page, or when a link to a
page of the file lands elsewhere than on the page its own deck meant.

## Traps

1. **pypdf prints "Annotation sizes differ: 1 vs. 0"** once per page that holds a link. The links are copied: each
   merged page has the same link annotations as its source page (checked on 2026-11-12, 69 links in the 16:00 PDF).
   Since 2026-11-12 the source line of every case frame is a link to its paper or post (`../cases-deck/README.md`,
   section "Links to the sources"), so the warning also comes from the case pages, with the number of their links.
   `merge.py` rewrites only internal links (GoTo); after a merge,
   `python3 ../cases-deck/tools/check_links.py block1-nearest-neighbors.pdf block3-bandits.pdf block4-large-scale-computing.pdf`
   checks that every source line kept its link (21, 14 and 7 citations on 2026-11-12).
2. **The decks' own bookmarks and page labels are dropped.** Beamer labels its pages, and the second deck's labels
   would start again at 1 in the middle of the file. The output has one bookmark per deck and no labels, so a viewer
   counts 1 to N. The page numbers printed on the case frames are the case deck's own.
3. **The 16:00 block's cold intro is `block5-computing-clusters.pdf`** (named for the Saturday block it opened until
   2026-11-11) and its case deck is `block4-parallelized-mf.pdf`; the output takes the block's name,
   `block4-large-scale-computing.pdf`. Its third deck is the clusters deck, `block5-computing-clusters.pdf` of
   `../clusters-deck/`, the same file name as the cold intro in another folder.
4. **The Friday 11:00 block has no cold intro.** Its case deck (`../cases-deck/block2-matrix-factorization.pdf`, the
   chip "Business case, Spotify") is the first chip of its row on its own, with no file here.
5. **Beamer names its link targets after the page number** ("Navigation2" is page 2 of every deck), and a
   concatenation keeps the first deck's target for each name. In the files of AINIT-PAGE `c01c44e` the section title
   on a divider page of a case deck therefore jumped into the cold intro (block 1: page 18 to page 2, page 30 to page
   14). Since AINIT-PAGE `5c1a936` `merge.py` rewrites every such link to point at its own page directly and checks
   where each one lands.

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
