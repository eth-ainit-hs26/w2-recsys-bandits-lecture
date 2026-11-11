# CLAUDE.md : cold-intro-deck, the cold intros of weekend 2

Beamer, lualatex, three passes, from this folder. Two decks. `block1-nearest-neighbors.tex`, "Birds with
the same wings", the cold intro of weekend 2, shown before the Friday 08:15 block (the inner product and nearest
neighbors), built on 2026-11-10. `block5-computing-clusters.tex`, "Dividing a computation, 1793", shown before the
Saturday 08:15 block (computing clusters), built on 2026-11-10: section "Block 5" below. `README.md` has the frames,
the sources, the history and the open items of each.

The frames are the ones Carlos dictated on 2026-11-10, after the first build: the title frame (the Chinese with the
English under it, the one frame he called beautiful), a context frame (the book, the court, the people), the king's
question and Kun's answer as his English text, one paragraph per frame, the key sentence in lavender, and a closing
frame on representation learning, the theme of the weekend. The quotations carry no Chinese and there is no
mapping of story words to course terms. Change the wording of the quotations only on his say.
On the course site since 2026-11-11 (AINIT-PAGE commit `dc80aeb`, the Friday 08:15 row): after a rebuild, copy the
PDF and the handout there again under their site names (`README.md`, section "On the course site").

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
block5-*, make_images_block5.py, img/b5-*.jpg    the cold intro of block 5, section "Block 5" below
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

## Block 5: Dividing a computation, 1793

Ported on 2026-11-10 from the FDD section "Dividing a computation, 1793"
(`git_fdd/projects/weekend-07-large-scale/carlos-lectures/slides/w7-cost-slides.tex`, lines 143 to 349) into the
form of block 1: the French on the title frame only, Smith's English with the key sentence in lavender, no mapping
frame, a closing frame on computing clusters. Carlos asked to leave out the FDD frames "One parcel, many triangles,
one each" and "One side, two angles, and a table of logarithms". The closing frame uses only the facts of the lecture
deck `../clusters-deck/` that the coordinating session pinned: change them only together with that deck.
On the course site since 2026-11-10 (AINIT-PAGE commit `a498851`): after a rebuild, copy the PDF and the handout
there again under their site names (`README.md`, section "History of block 5").

```
block5-computing-clusters.tex   the deck, 5 frames, 10 pages, a "Say" comment per frame
make_images_block5.py           cuts and grades img/b5-*.jpg from four originals (URLs, sizes, SHA-1 in its docstring)
img/b5-*.jpg                    title, half-wire, bg-map, half-room, bg-close
block5-computing-clusters.pdf, block5-computing-clusters-handout.pdf    the deliverables, rebuild and recommit together
```

Traps of block 5:

1. **`fade("up", a, b, s)` counts from the bottom.** To veil the top 22 percent of a page, write
   `fade("up", 0.78, 1.0, s)`. Block 1's `make_images.py` writes `fade("up", 0.0, 0.14, 0.40)` for its title, which
   veils everything above the bottom 14 percent at 40 percent; that look was approved and is left as it is.
2. **The Internet Archive item `RecueildeplanchIVDide` numbers its jp2 files one above its leaves.** Leaf n102
   (plate II) is `RecueildeplanchIVDide_0103.jp2`, leaf n98 (plate I) is `_0099.jp2`. Its `page/n102_w6000.jpg`
   returns the full size JPEG whatever the width asked.
3. **Gallica (BnF) answers curl and the built-in browser with a Cloudflare challenge, HathiTrust with 403.** Prony's
   1824 notice could not be read in the original; `README.md` lists what was checked instead.
4. **Positions in the originals**, for new crops: plate II, the workshop x 79 to 6241, y 439 to 2081 (its bottom
   rule at y 2093); plate I, the workshop x 174 to 3282, y 537 to 2213, the wire drawer x 1820 to 2230; the map,
   Paris at x 5710, y 2025 on the meridian line; the Harvard photograph, 1920 by 1502, the standing computer at
   x 770 to 1030.
5. **The context frame of block 5 sits one line higher than block 1's** (title at 42 mm, paragraph at 57.4 mm, map
   faded from 0.35 to 0.46): it has four lines of text. Move the fade in `make_images_block5.py` with the text.
6. **Superscripts** (`10\textsuperscript{12}`) lower the first baseline of a statement by about 0.3 mm. The closing
   statements keep block 1's rhythm: next top = previous top + 5.8 mm per line + 5.7 mm.

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
