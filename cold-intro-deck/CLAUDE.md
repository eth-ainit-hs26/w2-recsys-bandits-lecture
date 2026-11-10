# CLAUDE.md : cold-intro-deck, the cold intros of weekend 2

Beamer, lualatex, three passes, from this folder. One deck so far: `block1-nearest-neighbors.tex`, "Birds with
the same wings", the cold intro of weekend 2, shown before the Friday 08:15 block (the inner product and nearest
neighbors), built on 2026-11-10. `README.md` has the frames, the sources, the history and the open items.

The frames are the ones Carlos dictated on 2026-11-10, after the first build: the title frame (the Chinese with the
English under it, the one frame he called beautiful), a context frame (the book, the court, the people), the king's
question and Kun's answer as his English text, one paragraph per frame, the key sentence in lavender, and a closing
frame on representation learning, the theme of the weekend. The quotations carry no Chinese and there is no
mapping of story words to course terms. Change the wording of the quotations only on his say.

The look is the Title sequence of the course cold intro (`w1-lecture-material/cold-intro/intro-slides/`, chosen by
Carlos on 2026-10-14): a picture on every frame, Futura, lavender only for the highlighted sentence and the term of
the closing frame. Carlos rejected a Codex plates cold intro as looking "like a technical report", and a struck or
muted row in a mapping as unaesthetic. Keep both out.

## Layout

```
block1-nearest-neighbors.tex   the deck, 5 frames, a "Say" comment per frame
cold-intro-kit.tex             the macros (a reduced copy of intro-kit.tex, plus \tshalf, and \tsrow, unused since the rebuild)
make_images.py                 cuts and grades img/ from the original painting (URL and SHA-1 in its docstring)
img/                           the five pictures, committed so that a build needs no network
tools/check_overlays_any.py    the no-jump check for dark pages
block1-nearest-neighbors.pdf, block1-nearest-neighbors-handout.pdf    the deliverables, rebuild and recommit together
```

## Traps

1. **Futura and Songti TC are macOS fonts, loaded by name.** Loading Songti by path picks the simplified face,
   which lacks some traditional characters.
2. **The dark under the type is baked into each picture** by `make_images.py`. `fade("down", a, b, s)` is clear
   above the fraction a of the height and s black below b; "up", "left" and "right" run the other way. Move a text
   and the fade may have to move with it.
3. **The positions of the painting in the original**, for new crops: the painting is x 5990 to 8640, y 25 to
   1830 of the scroll; the flock flies at y 100 to 930; the standing cranes are at x 6930 to 7090 and 7700 to
   7790, y 940 to 1180; the ridge is at y 1290 to 1330; the eaves end at x 6420 and 8230, y 1540.
4. **The house overlay check is blind on dark pages.** `../style/tools/check_overlays.py` counts only ink darker
   than the ground. Use `tools/check_overlays_any.py`.
5. **pdftotext also returns the rows not yet shown**, because `visible on` makes them transparent. Count the words
   of a frame on its last page.
6. **Chinese text has no break points.** TeX cannot wrap it, so a Chinese block carries an explicit `\\`.
7. **Credits are anchored at their bottom left** and grow upwards. At 6.6 pt the painting credit needs 70 mm for
   two lines; the text credit carries a `\\` after "Qi 3.".
8. **The write hook** rejects Unicode dashes, `----` in a comment and "X, not Y" sentences. Use `====`.

## Maintenance contract

- This file is the working memory for this folder. After any major change here, meaning a deck or frame added,
  removed or replaced, a changed picture or wording, a changed build procedure, or a change in who owns the work,
  UPDATE THIS FILE AND `README.md` IN THE SAME COMMIT.
- Every subdirectory that holds work of its own carries its own CLAUDE.md, and that file must itself carry this
  same maintenance contract, including this propagation rule. When you create a subdirectory, create its
  CLAUDE.md at the same time.
- Keep it concrete: real file names, real identifiers, real commands. Record the gotchas that cost someone an
  hour. Do not restate what the code already says plainly.
- House style, from `/Users/carloscotrini/Documents/git_ainit/CLAUDE.md`: ASCII punctuation only in authored
  prose (no em dashes, no en dashes, never `--` as a dash).
