# CLAUDE.md — the demos (games) in `visualizations/`

The interactive demos the lecture links from the root `index.html`. The repository's own CLAUDE.md
has the lecture, the scene map and the palette; this file holds the rules every demo page follows.
Set on 2026-11-03 at the request of the TA running the HS26 iteration.

## Navigation: one tab, always a way back

- **Demos open in the same tab.** No `target="_blank"` on the cards or the bonus links in
  `index.html`. Only links that leave the site (the SML FS26 pages) open a new tab, and they carry
  `↗` so the reader knows.
- **Two ways back to the index, on every demo:** the `← All demos` button in the header,
  `href="../index.html"` (never `href="../"`: from a `file://` copy that opens a folder listing
  instead of the page), and the browser's back arrow, which works because nothing opens a new tab.
- No pop-up when a demo is finished: a "Back to all demos" bar (`shared/nav.js`) was tried on
  2026-11-05 and removed at the TA's request.

## Demo 1: the block-diagonal score (changed 2026-11-04)

The score is neighbour agreement: adjacent readers earn the dot product of their rating rows,
floored at 0, and the same for adjacent books, divided by the best total any order reaches (280,
found at load by trying every order of the 8 distinct reader rows and 7 distinct book columns;
annealing found nothing higher). Any block order scores the same; the data-file order scores 87%;
a random shuffle about 28%, rarely above 50%.

The earlier score compared every cell with the data-file order. It punished correct play: Tessa
next to her twin Alice dropped it from 100% to 15%, and clean blocks in another order scored 51%,
short of the 85% line. Do not go back to a fixed answer key.

Rows and columns move with pointer events, not HTML5 drag-and-drop, which does not fire on most
phones and tablets.

## Demo 2: MovieLens (changed 2026-11-05)

- Loads `shared/movielens_subset.js` (`window.MOVIELENS`) with a `<script>` tag, not `fetch()`
  of the `.json`: fetch fails from `file://`.
- Rebuild in two steps, from the repo root:
  1. `python data/build_movielens_subset.py` (needs numpy and the raw MovieLens 100K in
     `data/movielens/ml-100k/`, git-ignored; download
     https://files.grouplens.org/datasets/movielens/ml-100k.zip and unzip there);
  2. `node data/seriate_movielens_subset.js` (seeded, ~15 s, same output every run).
  Step 1 alone leaves the weak k-means order.
- Movies are quality-matched: 7 per genre, every one rated 3.65 to 3.95 on average. The first
  version paired acclaimed dramas (Schindler's List 4.47) with weak comedies (Liar Liar 3.16),
  and every group "preferred drama": quality, not taste. Users: rated at least 18 of the 28,
  then the 40 whose genre averages differ most. The page does not mention these choices.
- Step 2 orders people and, within each genre, movies by Demo 1's neighbour score, cuts the
  people into four runs, and orders the runs so each group's favourite genre is on the
  diagonal. Result: sorted scores 90% (a shuffle about 25%); three groups each prefer one
  genre (action 53%, family 47%, comedy 45% liked), the fourth likes most things.
- Deep links: `#reveal` (sorted), `#averages`.

## Demo 3: Spectral microscope (rewritten 2026-11-06)

- The real table and the copy from the first *k* dimensions side by side, with reader and book
  names; the slider runs 0 to 6, not 0 to 16: the table has rank 4 (σ = 9.9, 8.9, 1.4, 0.9, then
  0), so everything past 4 was dead range. Opens at k = 1 so the elbow is found, not given.
- The readout counts ratings (the 181 ✅/❌ cells) that the copy gives back under
  `RECSYS.ratingSign`: 0, 100, 180, 180, 181 for k = 0 to 4. The one miss at k = 2 is Ursula's
  Borges; dimension 3 is Samir, dimension 4 is Ursula. The per-k notes in `NOTES` state this,
  so a change to `RATINGS` in `shared/data.js` must re-check them. Wrong cells are not marked in
  the copy (outlines, then dots, were tried and removed at the TA's request on 2026-11-06).
- The bar chart (σ² as a share of the total: 54%, 44%, 1%, 0.4%) is the plain view. The maths
  (A_k formula, σ table, the ‖A − A_k‖_F curve with its elbow at k = 2, Eckart–Young and the
  citation) sits under a "Show the math" button below the explainer, a `<details>` that opens
  without JS and follows the slider. Deep links: `#k=2`, `#math` (opens the maths).
- A "What is a dimension?" box opens the card (added after the TA did not get the word): one
  hidden taste question, a score per reader and per book, the copy multiplies them, with
  Alice × Potter / Alice × Kant / Eleni × any book as the worked example. SVD's dimension 1 is
  light fiction ↔ demanding nonfiction (Commuters vs Scholars), dimension 2 demanding fiction ↔
  light nonfiction: the diagonals of the slides' fiction and light axes, not the axes themselves.

## Every page works on every screen

Text and visuals must read well on a projector, a laptop, a tablet and a phone, in Chrome,
Safari, Firefox and Edge.

- Sizes that scale with the viewport: `clamp()` for headings and lead text, `min(Npx, 100%)` inside
  grid `minmax()`, flex-wrap rows. No fixed `width`/`min-width` in pixels that can exceed a 360 px
  screen.
- 16 px minimum side gutter on phones, no horizontal page scroll.
- The intro (`.lede`) under each demo title spans the full width (`max-width: none`, overriding
  the 70ch in `shared/style.css`), at `clamp(1.05rem, 1rem + 0.4vw, 1.2rem)`; done for Demos 1–3.
- Hover effects inside `@media (hover: hover)`, so touch screens do not get stuck hover states;
  a visible `:focus-visible` style on everything clickable; animations off under
  `prefers-reduced-motion`.
- Touch targets at least ~40 px tall; floating UI respects `env(safe-area-inset-bottom)`.
- Lead text on the index is full width and unboxed (the `.lede` block), larger than body text,
  with the "When a slide says Demo N" cue as the largest line (`.lede-cue`).
- No italic (cursive) text on the index: `em` is set upright, emphasis comes from weight or colour.
- On the index, titles and headings are EB Garamond; the demo cards and the "More material"
  descriptions use the same system sans-serif as the demos.
- The index groups the cards by act, one centred row each (four across, two across below
  1080 px, one on phones). The bright act colours (`--act1` …) are for stripes only; as text
  they fail contrast (2.3–3.4:1), so numbers and act labels use the `--*-ink` shades (≥ 5.5:1).
- Load the fonts a page names (the index loads EB Garamond from Google Fonts). A font that is
  only named shows up on the author's machine and as Times New Roman on most others.
- Check a change at 375 px and 1366 px before calling it done; headless Chrome does this:
  `google-chrome --headless=new --window-size=375,1100 --screenshot=out.png file://$PWD/index.html`.


## Maintenance contract

- This file is the working memory for this directory. After any major change here, meaning a new
  demo, a renamed or moved file, or a changed shared script, UPDATE THIS FILE
  IN THE SAME COMMIT.
- Every subdirectory that holds work of its own carries its own CLAUDE.md, and that file must itself
  carry this same maintenance contract, including this propagation rule. When you create a
  subdirectory, create its CLAUDE.md at the same time.
- Keep it concrete: real file names, real identifiers, real commands. Record the gotchas that cost
  someone an hour. Do not restate what the code already says plainly.
