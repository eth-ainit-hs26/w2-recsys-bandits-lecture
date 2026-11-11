# CLAUDE.md : cheat-sheet/

The semester of AI in Industry HS26 on one A3 landscape page, drawn as a mind map: the three weekends, their
concepts, and for each concept what it is, when to use it and its use in industry. Asked for by Carlos on
2026-11-11: "produce a cheat sheet that, if possible, acts as a mind map of all the concepts ... that are being
covered in the semester, and that acts as an orientation guide for the participants on when to use each technology
and what is the main use and application in industry."

## Files

| File | What it is |
|---|---|
| `cheat-sheet.tex` | The source: one TikZ picture on an A3 landscape page. |
| `cheat-sheet.pdf` | The built page, committed. |
| `SOURCES.md` | Where the concepts come from, and the source of every company, product and year on the page. |

## Build

From inside this folder:

```bash
../style/tools/build.sh cheat-sheet.tex
```

```bash
../style/tools/check.sh cheat-sheet.pdf
```

The build runs lualatex three times (the page is placed with `remember picture`) and prints the page count, the log
errors and any overfull box. The check must show 0 em dashes, 0 en dashes, only acronyms among the words in
capitals, no build metadata, and the fonts EB Garamond and Kefa III.

## How the page is built

- Coordinates are millimetres from the top left corner of the page, y downwards (the style `cx page`). The leaf
  rules sit at 10 and 11.6 mm from each edge, the pricking dots at x = 5.2.
- The root title is at the top centre. Violet arms lead to three heads: the Ge'ez numeral in a double ruled square,
  the dates, the title, one line on what the weekend is for, and the project.
- Five columns: two for weekend 1, two for weekend 2, one for weekend 3. Spines at x = 20, 93.8, 173.6, 247.4 and
  327.2; cards 6 mm right of their spine, 57.2 mm of text wide (weekend 3: 65.2 mm).
- `\cxcolumn` starts a column, `\cxgroup{node}{label}` adds a group, `\cxcard{node}{name}{what it is}{use it
  when}{in industry}` adds a card; an empty field drops its line. Every column ends with `\cxspine` and one
  `\cxmark{group node}` per group (the hatched square on the spine).
- Cards stack by themselves: 1.9 mm under the previous card, 3.9 mm before a group. A longer text pushes the rest of
  its column down.
- The bottom limit is the inner rule at 285.4 mm. On 2026-11-11 the longest columns (weekend 1, and weekend 2 after
  the Random card) ended at about 275 mm. After any change, render the page and look at the bottom of every column:
  `pdftoppm -r 60 -png cheat-sheet.pdf <scratch>/page`.
- The palette, the fonts and the hatching are copied from `../style/ainit-preamble.tex` (Codex plates). The preamble
  itself is not loaded, because it is a beamer theme for 160 x 90 mm frames.
- Card borders can look thicker at 150 dpi. That is the rasterizer: at 400 dpi every border is the same.

## Rules for the content

- The concepts are the lecture rows of the master spreadsheet's Syllabus tab and of the course site's
  `src/data/weekends.ts` (AINIT-PAGE), read on 2026-11-11. Weekend 3 (11 and 12 December) was not taught yet: its
  cards follow the Syllabus. When a weekend's rows change, change its cards.
- A card has three lines: what it is (one sentence), "Use it when" (a clause), "In industry" (a use). A company,
  product or year is named only with a source in `SOURCES.md`, and no case is older than five years (Carlos's
  rolling rule). A case says only what its source says: Amazon tested its bandit, so the card says "tested".
- Write dry: one sentence per item, no comments. ASCII punctuation: no em or en dashes, no double hyphen.
- The repository is public: the master spreadsheet's address stays out of this folder.

## State

2026-11-11: built, one page, 0 log errors, the check clean; 30 cards in 14 groups. Committed and pushed to `main`.
A push publishes the repository on GitHub Pages, so the PDF is reachable there.

On the course site since 2026-11-11, at Carlos's yes that day (AINIT-PAGE commit `ab95b28`): the copy
`public/slides/we2/ainit-hs26-cheat-sheet.pdf`, linked by the button "Semester cheat sheet (PDF)" beside the intro
deck on the home page (`src/pages/HomePage.tsx`) and by the group "Cheat sheet" at the top of weekend 2's Materials
list (`src/data/weekends.ts`). The live copy:
https://eth-ainit-hs26.github.io/AINIT-PAGE/slides/we2/ainit-hs26-cheat-sheet.pdf
After a change here, copy the new PDF over that file with the recipe of `w1-lecture-material/CLAUDE.md`, section
Publishing: clone AINIT-PAGE, copy, `npm ci && npm run build`, push, then curl the live file and `cmp` it with this one.

## Maintenance contract

- This file is the working memory for this folder. After any major change here, meaning a new card or group, a
  changed layout or build procedure, or a change in who owns the work, UPDATE THIS FILE IN THE SAME COMMIT.
- Every subdirectory that holds work of its own carries its own CLAUDE.md, and that file must itself carry this
  same maintenance contract, including this propagation rule. When you create a subdirectory, create its CLAUDE.md
  at the same time.
- Keep it concrete: real file names, real identifiers, real commands. Record the gotchas that cost someone an hour.
  Do not restate what the code already says plainly.
