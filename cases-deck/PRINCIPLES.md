# Business-case decks: lessons and principles

Written 2026-11-06 after the Etsy, Spotify and Airbnb decks of this folder, for the next case decks (bandits,
advertising). Audience of the decks: managers with little formal math, 10 minutes after a lecture block.

## Lessons from the Etsy, Spotify and Airbnb decks

- **Ideas first.** Carlos stopped a build and asked for ideas only ("Don't build anything show me ideas and then we
  shape them"). Two paragraphs per case, the method and the value, let him choose. Then he dictated every slide.
- **His text is the content.** He dictates the words of each slide and says where a diagram helps ("for slides 2
  and 3 would be nice to have illustrative diagrams").
- **The first builds were too complicated.** His verdict: "This is too complicated for me ... Make them 25%
  simpler". The simplified decks have 344, 152 and 155 words (5, 3 and 3 frames): 50 to 70 words a slide, title
  and source line included.
- **What made them complicated:** sentences that repeated a diagram on the same slide (two funnels, a pair of
  bars), a worked ranking with 44 numbers, a graph of six items and eight links, two quotes and three version
  labels on one slide, a title that repeated the big number below it, source lines of 14 words.
- **The second read found no wrong number, but claims broader than their sources:** "used to come from keyword
  matching" without "only" (it still runs), "a hundred thousand homes" (popular places only), "one row per search
  that ended in a purchase" (the paper: positive interactions "such as" cart adds and purchases), a graph drawn
  with one kind of link (it has three), a blog's sentence next to a figure from the paper.
- **The checks pass on defects that only the rendered page shows:** arrow labels cutting the border of the box
  below, a lead sentence of 85 characters wrapping into the labels under it, labels running past the frame, a
  label touching a box.
- **Jargon left the slides:** list of numbers (embedding), two networks (two towers), shortlist (candidate set),
  clustered index (IVF), "share of the bought products found in the top 100" (recall@100).
- **A measure is named by what it counts.** On 2026-11-09 Carlos asked what a "site conversion" is. Etsy's
  measures became "visits that end in a purchase" and "searches that end in a purchase", Airbnb's "visits that end
  in a booking"; the papers' names (site-wide conversion rate, organic search purchase rate) stay in the talk track
  and README.md.
- **Each case's facts stay in its own section.** On 2026-11-09 Airbnb's words on its +0.31% gain went onto Etsy's
  value slide, as a scale for Etsy's +2.63%. On 2026-11-10 Carlos: "You cannot put Airbnb calls with 0.31% gain on
  the slides from Etsy. They need to go in the Airbnb part." They are on Airbnb frame 3.
- **"Follow the style of the slides for X" means: build without dictation, on the pattern of that deck.** For the
  bandit and advertising decks he chose the cases, then wrote "Produce the slides, follow the style from the slides
  for the matrix factorization part": they follow the Spotify case (`spotify-frames.tex`; the problem with a big number at the second click,
  the method as a diagram tied to the block's game, the value of an A/B test), and README.md says which deck was
  read as "the slides for X".
- **The second read of those decks found the same kind of claim:** "No pair beat the fixed page" (the post: it
  explored "most" of its pairs), a lift reported "currently" and "directionally" shown as a plain rise, a blog's
  advice ("train separately") told as what the company did, "accuracy" for a test AUC, "may vary" told as "change".

- **One deck per block.** On 2026-11-09 he asked for the cases of each block in one deck: "I want that you don't make
  like each case a separate slide deck. Simply for each block, put in one single deck all the slides with all the
  business cases." The six one-case decks were removed that day.

## Principles

### The case

- Published in the last five years (from 2021-11, as of 2026-11), by the company itself, with a measured result:
  an A/B test or numbers from production.
- The technique of the case is the technique of the block it follows, in that block's words and notation.
- Cite the published venue ("IEEE FMLDS 2024", "WWW 2024 Companion"); mark an arXiv paper "preprint"; name a blog
  post with its year.

### Working with Carlos

- Candidates in chat first, two paragraphs each; nothing built until he chooses.
- He dictates by voice: read garbled words from context ("then" for "them"); keep his words and his order, and
  shorten only to simplify.
- When his slide numbers skip (Etsy: 1, 2, 4, 5), read them from the content and record the reading.
- Every choice made without asking goes to README.md and into the closing message.
- After every build: send the PDFs, commit and push.

### The deck: 3 to 5 frames

1. The company and its problem: the scale, why the old way fails, one concrete example ("mothers day gift").
2. What the method learns from, when the case needs it.
3. The method as a picture in the course's terms, tied to the block's game ("In the matchmaker the numbers were
   learned directly").
4. The method at work, step by step, with clicks.
5. The value: test results as relative changes, and the cost.

Details cut from a slide go into the `% Say:` talk track above its frame.

### Words

- About 50 words a slide, 70 at most, title and source line included (count: `pdftotext` of the handout page).
- No sentence that repeats a diagram of the same slide.
- One quote a slide at most.
- A title never repeats a number shown large on the slide.
- Short source line: "Jha and others (Etsy), IEEE FMLDS 2024.", a link (section "Numbers and claims").
- "relative change" beside every percentage from a test.
- A measure says what it counts ("visits that end in a purchase"); a metric's name ("conversion rate") stays off the slide.
- Body text at `\normalsize` holds about 70 characters on the full 130 mm line and 40 in a 64 mm column.

### Pictures

- One idea a picture, few elements. A worked ranking: four items of three numbers at most (30 numbers).
- The inner product in the video store's notation (rows stacked, times signs, a rule, the products, plus signs,
  equals, the sum; `w2-cx-private/01_nearest_neighbours/source/game/NOTATION.md`), worked once; afterwards only
  inputs and results.
- Clicks only add (`visible on=<n->`); nothing moves; 2 to 4 steps a frame.
- Invented examples: small integers, "Invented" on the slide, generated by `tools/cases_numbers.py` with asserts on
  the story they tell (the necklace first, the gift wrap out of the top two).
- `\ncell` tints a number by its sign; `\hatchcells` draws a long list of numbers whose values stay unshown.

### Numbers and claims

- No number typed in a `.tex` file. `tools/cases_numbers.py` holds every number with its source sentence as a
  comment, writes `numbers.tex` and `tools/expected-<deck>.txt`, and `tools/check_numbers.py` reads the strings
  back from the PDF.
- Second read of every claim by an agent with the source texts (papers as text in the scratchpad). Check each
  finding in the source before changing a slide, and list the changes in README.md. Look for scope words (only,
  every, popular, most), which source says what (paper or blog), how often something runs (daily, at each visit),
  what a test compared, hedges (may, currently, directional: a lift not claimed as significant) and advice that a
  slide or a talk track tells as done.
- The source line is a link to the document behind its numbers: the source macro wraps the citation in
  `\weblink{<url>}{<citation>}` (violet), to the free full text that was read: the arXiv version for a paper, while
  the citation names the published venue; the post for a blog. Carlos, 2026-11-12: "put hyperlinks in the citations
  of the business cases so that if a participant is curious, they can click and find the paper". ACM and IEEE pages
  answer curl with 403 and 202, so a link to them cannot be checked by script.
- A number, quotation or source goes only on the slides of the company it belongs to, whatever slide the request
  came up on. A comparison across cases goes on a slide only when Carlos asks for that comparison.

### Checks before sending

- `build.sh`, `check.sh` (dashes, build words; it rejects "candidate"), `check_overlays.py`, `check_numbers.py`,
  `check_links.py` (every source line carries its link; also on the merged PDFs of `../cold-intro-and-cases/`),
  `make_handout.py`.
- Render every page at 150 dpi and read it: text past the frame, labels touching boxes, borders cut by labels.
- Grep each `<case>-frames.tex` for the names of the other companies: they may appear in comments, never in the
  text of a frame.

### Layout traps

- An `elab` arrow label between two `stage` chips cuts the lower chip's border when the gap is under about 5.5 mm:
  give it `inner sep=0.4pt`.
- A chip grows with its text: all chips of a pipeline get the same `minimum width`.
- A centred `\small` label of 30 characters is about 50 mm wide: near the frame's edge, break it into two lines.
- `shapes.geometric` is not loaded.
- A chip's `\small` text wraps earlier than the estimate above; break a short label by hand ("Home page\\ users")
  rather than let it break after the first word.
- A two-line `measure` label above a bar needs about 9 mm above the bar's top edge, or its second line touches the
  bar (Spotify's home page, frame 3).
- The headers of a table of numbers: `anchor=base` at one y, or a word with descenders ("Approved") sits higher than
  its neighbours.

## The blocks and their games

| Block, Friday 13 November 2026 (agenda of 2026-11-06, the 16:00 block merged and renamed on 2026-11-11) | Game (`w2-cx-private`) | Cases, in its block deck |
|---|---|---|
| 08:15 the inner product and nearest neighbors | Once Upon a Video Store, `01_nearest_neighbours/` | Etsy, Airbnb: `block1-nearest-neighbors.tex` |
| 10:00 and 11:00 matrix product and matrix factorization | Once Upon a Matchmaker, `02_matrix_factorization/`: part one at 10:00; parts two and three and the optional part at 11:00 | Spotify: `block2-matrix-factorization.tex` |
| 14:00 bandits | Once Upon a Mirror, `03_bandits/`: mirrors show one ad each morning, a tap is a click | Spotify's home page, Amazon Payments: `block3-bandits.tex` |
| 16:00 large-scale computing: computing clusters (`../clusters-deck/`, the Saturday 08:15 block until 2026-11-11), then parallelized matrix factorization | Matchmaker on a Grid, `02_matrix_factorization/grid-sketch/` | LinkedIn's ads (gradient descent at scale): `block4-parallelized-mf.tex` |

The course site carries each block deck on its block's row since 2026-11-09, and before that each case since
2026-11-06 (README.md, section "On the course site").
Before that day the blocks were 08:00, 10:00, 12:00, 14:00 (matrix factorization by gradient descent) and 16:00.

## Files and commands

- Folder `2026hs/w2-recsys-bandits-lecture/cases-deck/`, a public repository: a push publishes it on GitHub Pages;
  the course site links a deck only after Carlos's yes (the block decks and the weekend deck have it).
- A case is `<case>-frames.tex` (frames and talk track). Its block deck (`block1-nearest-neighbors.tex` to
  `block4-parallelized-mf.tex`) and `weekend2-cases.tex` input it, one `\section` per case.
- Shared: `cases-kit.tex` (styles and macros), `numbers.tex` (generated), `tools/cases_numbers.py`.

```bash
python3 tools/cases_numbers.py
../style/tools/build.sh block1-nearest-neighbors.tex
../style/tools/check.sh block1-nearest-neighbors.pdf
python3 ../style/tools/check_overlays.py block1-nearest-neighbors.pdf
python3 tools/check_numbers.py block1-nearest-neighbors.pdf tools/expected-block1-nearest-neighbors.txt
python3 tools/check_links.py block1-nearest-neighbors.pdf
python3 ../style/tools/make_handout.py block1-nearest-neighbors.pdf block1-nearest-neighbors-handout.pdf
```

## Adding a case

1. Copy `airbnb-frames.tex` to `<case>-frames.tex`, then write the frames and the source macro with its `\weblink`.
2. In `tools/cases_numbers.py`: a block with the numbers and their source sentences, `show("<case>", ...)` for
   every string the PDF must show, `"<case>"` in `deck_expect` and in its block's list in `BLOCK_DECKS`.
3. In the block deck and in `weekend2-cases.tex`: `\section{<title>}` and `\input{<case>-frames}`, in the order of
   `BLOCK_DECKS`. A case for a block without a deck: copy `block4-parallelized-mf.tex` to `block<N>-<name>.tex` and
   add it to `BLOCK_DECKS`.
4. Build and check the block deck and `weekend2-cases.tex`; update README.md and CLAUDE.md; `git pull --rebase`,
   commit, push; copy the PDFs to the course site (README.md, section "On the course site").

## Candidates for further decks

The bandit and advertising decks were chosen on 2026-11-06 from eight candidates (Spotify's home page, Amazon
Payments, LinkedIn's ads; the five set aside are in `chosen_bandit_and_ads_cases.md` of the folder below). Candidates
for a 16:00 deck or a replacement, in `git_ainit/research_notes/Business cases of the weekend 2 techniques/`:

- `recent_bandits.md`: Amazon Payments, Dream11, Amazon retail, Expedia AdaptEx, Uber CRM e-mails, DoorDash, and a
  failure (Amazon, WWW 2024), all from 2021 on and checked against primary sources.
- `recent_scale.md`: Kuaishou OneRec, LinkedIn LiRank (Feed, Jobs and Ads), Stripe, Netflix.
- `bandits.md`: older cases (Yahoo 2010 among them); check the year of each.

Also `cases.tex`, card 3: Adyen's payment bandit (KDD workshop 2025). The opener deck (`../opener-deck/`) already
shows advertising figures of Meta, Amazon and Nubank (October 2026); a case deck repeats none of its numbers.

## Maintenance contract

- This file is part of the folder's working memory with CLAUDE.md and README.md. After a major change in how case
  decks are made, UPDATE THIS FILE IN THE SAME COMMIT.
- Every subdirectory that holds work of its own carries its own CLAUDE.md, and that file must itself carry this
  same maintenance contract, including this propagation rule. When you create a subdirectory, create its
  CLAUDE.md at the same time.
- Keep it concrete: real file names, real identifiers, real commands. Record the gotchas that cost someone an
  hour. Do not restate what the code already says plainly.
