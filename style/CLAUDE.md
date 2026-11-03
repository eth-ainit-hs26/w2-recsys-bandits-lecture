# CLAUDE.md : style/, the Codex plates deck style, copied for weekend 2

This folder is a COPY of the official HS26 deck style of AINIT, Codex plates, which Carlos chose on
2026-10-09 for every LaTeX deck of the run. The canonical copy, with the palette, all the rules, the
traps and a sample deck, is `style/` in the private repository `eth-ainit-hs26/w1-lecture-material`
(locally `/Users/carloscotrini/Documents/git_ainit/2026hs/w1-lecture-material/style/`). Its CLAUDE.md
is the full reference: read it before designing a new kind of figure.

The files here were copied on 2026-11-03 from commit `9792819` of that repository, and
`tools/make_handout.py` from its `llm-deck/tools/` at commit `34bce22`. The first line of each file
says where it came from.

## Files

| File | What it is |
|---|---|
| `ainit-preamble.tex` | The style: colours, fonts, the leaf, titles, gloss balloons, chips, hatching, `\treelink` |
| `ainit-course.tex` | The course facts: dates, titles, the three weekends frame |
| `deck-skeleton.tex` | The start of a new deck, already set to the slug "AI in Industry, weekend 2" and `\currentweekend{b}` |
| `tools/build.sh` | `build.sh deck.tex`: three lualatex passes run from the deck's own folder; prints pages, errors, missing glyphs |
| `tools/check.sh` | `check.sh deck.pdf`: counts em and en dashes (must be 0), lists the ALL CAPS words, finds build metadata, lists the fonts |
| `tools/check_overlays.py` | `check_overlays.py deck.pdf`: within a frame a click may only add; anything that moves between clicks fails |
| `tools/render_board.py` | `render_board.py deck.pdf outdir`: the last click of every frame as a PNG at 150 dpi, and a contact sheet |
| `tools/make_handout.py` | `make_handout.py deck.pdf handout.pdf`: one page per frame, its last click (needs pypdf) |

A deck lives in a sibling folder, for example `../opener-deck/`, and starts with
`\input{../style/ainit-preamble}` and `\input{../style/ainit-course}`. A device that only one deck
needs goes into that deck's own kit file (as `opener-deck/opener-kit.tex` does), so this folder
stays a clean copy of the canonical one.

## The rules that cost rework

- Fonts: EB Garamond, Garamond Math, Libertinus Mono, and Kefa III for the Ge'ez numerals of the
  balloons. Kefa III is a macOS font. Engine: lualatex, three passes, because the leaf and the
  balloons are placed with remember picture.
- The body is 61.1 mm tall. Keep a figure at or under 55 mm, and keep every title on one line.
- Notes go in gloss balloons beside a figure. Nothing goes under a diagram. A dashed outline marks
  what is refused, so draw a grouping circle solid.
- `chip strong` draws a hatched frame 1.25 mm inside its border. A label of two lines, or a wide
  one, needs `inner xsep=2.6mm, inner ysep=2.4mm`, or its text runs over the hatching.
- `\treelink` wants the chosen branch declared first.
- Reveal with `visible on=<n->`, so that nothing moves between clicks. `check_overlays.py` enforces it.
- The house write hooks reject em dashes, en dashes and a double hyphen, so TikZ paths in the deck
  files use `to` between points.

## Pulling a fix from the canonical copy

Nothing syncs the two copies. To pull a fix, diff the file against the w1 repository's copy, copy it
over, update its first line (date and commit), then rebuild every deck in this repository and read
its pages.

## Maintenance contract

- This file is the working memory for this folder. After any major change here, meaning a file
  recopied from the canonical style, a new tool, a changed build or check procedure, or a rule
  learned the hard way, UPDATE THIS FILE IN THE SAME COMMIT.
- Every subdirectory that holds work of its own carries its own CLAUDE.md, and that file must itself
  carry this same maintenance contract, including this propagation rule. When you create a
  subdirectory, create its CLAUDE.md at the same time.
- Keep it concrete: real file names, real identifiers, real commands. Record the gotchas that cost
  someone an hour. Do not restate what the code already says plainly.
