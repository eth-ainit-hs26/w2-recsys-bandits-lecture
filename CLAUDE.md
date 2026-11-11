# CLAUDE.md — context for future Claude sessions

This is the working repo for **Week 2 of *AI in Industry* at ETH Zürich** — a 90-minute lecture on recommendation systems and bandits, taught to managers without a technical background. Carlos Cotrini is the lecturer. The deck was rebuilt from scratch in May 2026; this file gives the next Claude session enough context to keep going.

## The lecture, in 5 lines

> *Machine learning is the engineering of two old theorems. Compression — the shortest faithful description of the past — and prediction — the best bet about the future — are two views of the same subject, governed by Shannon's 1948 theorems. We build them in two halves and collapse them in the third.*

Act I (compression) covers recommendation systems via matrix factorization. Act II (prediction) covers bandits via ε-greedy. The Interlude introduces Shannon's entropy in *urn* language. The Epilogue collapses both halves through the compression-prediction duality. Borges' *Funes the Memorious* opens and closes the lecture.

## Audience and register

Managers without a technical background, but the venue is ETH. The lecture must read like a **museum-exhibition catalogue or a classical academic monograph**, not a pitch deck. Borges, Shannon, Eckart-Young, Lai-Robbins, Hutter, and Delétang et al. are all named explicitly. Six equations, seven citations, three lower bounds. The audience is treated with intellectual respect.

Specifically:

- **Bandits algorithm: ε-greedy only.** Thompson sampling and UCB were deliberately dropped (the lecturer does not have time to teach the prerequisites). See `NARRATIVE_PLAN.md` v3.
- **Urn metaphor over channel metaphor.** Managers do not have intuition for radio channels, but they do for urns of coloured balls. Shannon's two theorems are stated entirely in urn language.
- **One noun for the lecture.** The same urn appears in Act I (a reader's preference), Act II (a campaign's conversion rate), and the Epilogue (a signal source). Three roles, one vocabulary.

## File map

```
.
├── index.html                  Live lecture-companion page on GitHub Pages
│                               (10 numbered demos in the order the
│                                lecturer visits them; secondary section
│                                for slides PDF, bonus viz, and source).
├── README.md                   Short, points here
├── CLAUDE.md                   This file
├── NARRATIVE_PLAN.md           THE source of truth — 27 scenes, 6 equations, 7 citations
├── BOOKS_MATRIX.md             v2 rank-2-clean: 16 books × 21 readers + cold-start
├── LOG_BOOKS_MATRIX.md         Audit log of the matrix design
├── .github/workflows/pages.yml GitHub Pages deployment
├── slides/                     Beamer source + compiled PDF
│   ├── lecture.tex             Master that \input's the five section files
│   ├── prologue.tex            Scenes 1–3
│   ├── act1_compression.tex    Scenes 4–12
│   ├── interlude_shannon.tex   Scenes 13–16
│   ├── act2_prediction.tex     Scenes 17–24
│   ├── epilogue_duality.tex    Scenes 25–27
│   ├── references.tex          Two-slide bibliography
│   ├── build.sh                LuaLaTeX wrapper with TEXINPUTS for the theme
│   └── lecture.pdf             Compiled (committed for posterity)
├── theme/ainit-academic/       Custom Beamer theme
│   ├── beamer{theme,colortheme,fonttheme,innertheme,outertheme}AINITAcademic.sty
│   ├── demo.tex                Exercises all six slide templates
│   └── demo.pdf                Compiled theme demo
├── visualizations/             18 single-file interactive viz (HTML+D3+KaTeX);
│   │                           own CLAUDE.md (navigation, demo notes, every-screen rules)
│   ├── index.html              Redirect to the root index.html
│   ├── shared/data.js          THE data layer — books matrix v2, archetypes, helpers
│   ├── shared/style.css        ETH chrome, Okabe-Ito CVD-safe palette
│   └── (18 viz files; see below)
├── colab/three-portraits/      Weekend 2 Colab notebook "Three portraits of a product"
│                               (Amazon Reviews 2023, three embeddings, a scoreboard);
│                               generator build_notebook.py, own CLAUDE.md
├── style/                      The HS26 deck style, Codex plates, copied on 2026-11-03 from
│                               w1-lecture-material (preamble, course facts, skeleton, build
│                               and check tools); own CLAUDE.md
├── opener-deck/                The weekend 2 opener (2026-11-03): six frames on why
│                               recommendation, advertising and customer profiles matter,
│                               opener.pdf and a handout; own CLAUDE.md and README.md
├── cases-deck/                 Business cases of the weekend 2 techniques (2026-11-04): one
│                               case at the end of each Friday lecture (Etsy 2024, Spotify
│                               2024, Adyen 2025, LinkedIn 2024) and a closing map; cases.pdf,
│                               a handout and one PDF per lecture; own CLAUDE.md and README.md
│                               Since 2026-11-06 also six cases, one frames file each:
│                               Etsy (5 frames), Spotify (3), Airbnb (3), dictated by Carlos,
│                               and, built in his model's style, Spotify's home page, Amazon
│                               Payments, LinkedIn's ads (3 each); since 2026-11-09 one deck
│                               per Friday block (block1-*.tex to block4-*.tex), all six in
│                               weekend2-cases.tex; rules in PRINCIPLES.md
├── cold-intro-deck/            The cold intro of weekend 2 (2026-11-10), in the dark Title
│                               sequence of the course cold intro: "Birds with the same wings"
│                               (Chunyu Kun, Zhanguo ce), 5 frames dictated by Carlos, pictures
│                               cut from Huizong's Auspicious Cranes; own CLAUDE.md and README.md
│                               Also the cold intro of the Saturday 08:15 block, "Dividing a
│                               computation, 1793" (Prony's tables, from FDD weekend 7), 5 frames
├── clusters-deck/              The Saturday 08:15 block "Computing clusters" (2026-11-10): a port
│                               into Codex plates of the first block of FDD weekend 7, "The cost
│                               of computation and supercomputers", with Carlos's cuts; 21 frames;
│                               own CLAUDE.md and README.md
├── lecture-notes/              Lecture notes of the Friday 08:15 to 12:00 blocks (2026-11-11): the
│                               inner product, nearest neighbors, the matrix product and matrix
│                               factorization, four pages linking the games; every number from
│                               tools/notes_numbers.py; own CLAUDE.md and README.md
├── cheat-sheet/                The semester on one A3 page (2026-11-11): a mind map of the three
│                               weekends, each concept with what it is, when to use it and its use
│                               in industry; own CLAUDE.md and SOURCES.md
├── original-decks/             Original PDFs from before the rebuild
│   ├── w2_bandits.pdf
│   └── w2_recsys.pdf
└── archive/                    Early prototypes preserved for posterity
    └── (8 HTML files predating the v3 narrative plan)
```

## The 10 active visualizations (mapped to scenes)

| Scene | Viz file | Section |
|---|---|---|
| 5  | `01_block-diagonal-puzzle.html` | Act I |
| 7  | `02_latent-axes-lab.html` | Act I |
| 9  | `spectral-microscope.html` | Act I |
| 11 | `customer-urns-carousel.html` | Act I — anchor viz |
| 12 | `07_embeddings-that-learn.html` | Act I |
| 14 | `entropy-mountain.html` | Interlude |
| 20 | `three-urn-casino.html` | Act II |
| 22 | `algorithm_stadium.html` | Act II |
| 23 | `distinguishability-dial.html` | Act II |
| 25 | `compression-prediction-twin.html` | Epilogue — climax viz |

Eight further viz exist in `visualizations/` (numbered 03–11, minus those listed above) — these are bonus pieces from an earlier v1 of the recsys deck. They still work and are linked from the landing for completeness, but the v3 lecture (the current one) does not use them in its 27-scene flow.

## How to build the slides

```bash
cd slides
bash build.sh
# → produces lecture.pdf via lualatex (two passes)
```

Requirements: **LuaLaTeX** (MacTeX or TeX Live 2024+), with the `ebgaramond`, `unicode-math`, `tikz`, `etoolbox`, `appendixnumberbeamer`, `microtype`, `xcolor`, and `qrcode` packages. The build script sets `TEXINPUTS=../theme/ainit-academic:` so `\usetheme{AINITAcademic}` resolves. The `qrcode` package powers slide&nbsp;2 (the companion-site QR).

The theme expects `EB Garamond`, `Latin Modern Math`, and falls back to `TeX Gyre Heros` for any sans chrome. If you want the real ETH wordmark instead of the small-caps text fallback on the title slide, drop the asset into `theme/ainit-academic/` and edit one `\node` in `beamerinnerthemeAINITAcademic.sty`.

## How to view a single viz locally

```bash
open visualizations/index.html
# or any individual file:
open visualizations/customer-urns-carousel.html
```

All viz are single-file HTML + D3 v7 (CDN) + KaTeX 0.16 (CDN). They open directly via `file://` with no server. Each viz reads from `visualizations/shared/data.js` (`window.RECSYS`).

Demos open in the same tab as the index and always offer a way back; see
`visualizations/CLAUDE.md` before adding or changing a demo.

URL hash deep-linking is supported on the Customer-Urns Carousel: `customer-urns-carousel.html#stage=2` jumps to Stage 2 of 3.

## Deployment (GitHub Pages)

`.github/workflows/pages.yml` deploys the entire repo to GitHub Pages on every push to `main`. The landing is `index.html` at root. URLs:

- Landing: `https://eth-ainit-fs26.github.io/recsys_bandits_lecture/`
- Any viz: `https://eth-ainit-fs26.github.io/recsys_bandits_lecture/visualizations/<filename>.html`
- Slides PDF: `https://eth-ainit-fs26.github.io/recsys_bandits_lecture/slides/lecture.pdf`

## Design conventions (do not break)

1. **CVD-safe Okabe-Ito palette throughout.** Variables defined in `visualizations/shared/style.css`: `--color-pos` (blue), `--color-neg` (vermillion), `--color-fiction` / `--color-nonfiction` / `--color-light` / `--color-demanding` for the four book quadrants. Never use red-vs-green.
2. **Books axes:** Fiction (+x) / Nonfiction (−x), Light (+y) / Demanding (−y). Quadrants: `LF`, `DF`, `LN`, `DN`. The four reader archetypes (A1 Commuter, A2 Literary, A3 Practical, A4 Scholar) sit at the four corners of this 2-D latent space.
3. **The matrix is rank-2 by construction.** Pure archetypes are ✅ in own quadrant, ❌ in opposite, ? (zero) in adjacent. The Spectral Microscope shows σ₁ ≈ 9.9, σ₂ ≈ 8.9, σ₃ ≈ 1.4 (Samir's residual), σ₄ ≈ 0.9 (Ursula's Borges anomaly). Frobenius error at k=2 is ~12 % of `‖A‖_F`.
4. **No emoji on slides.** Emoji are fine inside the viz (they are part of the urn rendering and rating cells). Slides stay serif.
5. **No bold on slides; italic for emphasis only.** Use `\AINITemph{...}` from the theme.
6. **Six equations, no more.** They are listed in `NARRATIVE_PLAN.md` § cross-cutting threads.
7. **Seven citations, no more.** Listed in `slides/references.tex` and the same § of the narrative plan.
8. **Funes opens and Funes closes.** Borges' epigraph at scene 2 returns inverted at scene 27. Do not break this loop.
9. **`\vizhandoff{N}{Title}` is two arguments.** The first is the demo number (1–10), the second is the human-readable title. The slide shows "Demo N / 10 — Title" so participants can match it to the same numbered card on `index.html`.

## How the lecture was built (May 2026, condensed)

The original deck (`original-decks/w2_*.pdf`, dated Nov 2025) was rebuilt from scratch over ~3 sessions. The build was extensively agent-driven:

1. **Foundation phase.** Locked the narrative arc (`NARRATIVE_PLAN.md`), designed the books matrix (`BOOKS_MATRIX.md`), wrote the visual design spec for the Beamer theme.
2. **Visualization phase.** Eleven viz built or retrofitted across roughly 25 minutes of agent dispatch time:
   - Five Act-I viz (block-diagonal puzzle retrofit, latent-axes lab retrofit, spectral microscope NEW, Customer-Urns Carousel NEW (3-stage), embeddings-that-learn retrofit).
   - Five Part-2 viz: Entropy Mountain, Three-Urn Casino, Algorithm Stadium retrofit, Distinguishability Dial, Compression-Prediction Twin (3-stage).
3. **Theme phase.** Custom `ainit-academic` Beamer theme: 5 `.sty` files + demo deck.
4. **Slides phase.** Five parallel section agents authored Beamer source against the theme. ~3.3 minutes wall-clock for ~41 slides.
5. **Repo phase.** This commit. Reorganized into the layout above; deployed via GitHub Pages.

A heuristic that worked through every dispatch: **tight briefs in foreground beat loose briefs in background.** The 600 s stream watchdog kills any agent that does not produce output, so brief specs that ask for too much reading or too much creative drift get terminated.

## Pending work

Three items remain to make the lecture fully production-ready:

1. **Speaker script.** ~6,000 words of timed talking points with viz cues. Not yet written.
2. **Integration / rehearsal pass.** Walking through the deck with the viz open, end-to-end timing.
3. **Real ETH wordmark asset.** Currently a small-caps text fallback on the title slide.

## The Colab notebook (added 2026-11-03)

`colab/three-portraits/` holds a Colab notebook for the weekend 2 participants, apart from the
90-minute lecture: three embeddings of 25,612 Amazon video-game products (from the description, from
behaviour, and as semantic IDs) and a scoreboard of four recommenders. Its own CLAUDE.md has the
build, the test route on Carlos's Colab Pro account and the measured results. The Pages workflow
publishes it with the rest of the repository, so a push makes it public.

## The opener deck and the HS26 style (added 2026-11-03)

`opener-deck/` holds the opener of weekend 2: six frames, for managers, on why recommendation,
advertising and customer profiles matter (the advertising money of 2025, how much of what people watch
and buy a machine suggested, "compared to what?", then three measurements published in October 2026:
what better models added to conversions at Meta, Amazon's shopping assistant and its 50% more per
order, and the customer profile Nubank learns from 100 billion transactions, which hands over to the
weekend). Frames 4 to 6 were redone the same day at Carlos's request for measured, recent numbers;
the first version is commit `b165aeb`. It is a LaTeX deck in Codex
plates, the official HS26 style, so it does NOT use the FS26 theme of `slides/` and `theme/`; its style
is the copy in `style/`, whose CLAUDE.md says where the canonical copy lives. Every number comes from
`opener-deck/tools/opener_numbers.py`. Build with `../style/tools/build.sh opener.tex` from inside
`opener-deck/` (lualatex, three passes). The design conventions of this file (Okabe-Ito colours, no
bold, six equations) belong to the FS26 lecture and do not bind the HS26 decks. Nothing links to the
opener yet; a push makes the PDF public on Pages.

## The cases deck (added 2026-11-04)

`cases-deck/` holds the talk of business cases asked for after the BMAI HS26 evaluation: four cases, one at
the end of each Friday lecture of weekend 2, and a map of four business questions to the techniques, 10 to 15
minutes in all (Carlos's choice of 2026-11-04). Etsy's search by nearest neighbours after the video store
(08:00), Spotify's audiobook vectors after the matchmaker (10:00), Adyen's epsilon-greedy bandit on payments
after the bandits (12:00), LinkedIn's large ranking models after gradient descent (14:00), then the map. Every
case is a result published in 2021 or later: Carlos rejected version 1 (Airbnb 2018, the Netflix Prize,
Netflix 2012) the same day as old. Every case frame is the same two by two card: what was built, the result
and how it was measured, what it cost, what the company decided. Every number comes from `cases-deck/tools/cases_numbers.py`, next to its source sentence; the
README grades every source. Same style and build as the opener: Codex plates from `style/`, built with
`../style/tools/build.sh cases.tex` from inside `cases-deck/`. The course site has the weekend deck
`weekend2-cases.pdf` since 2026-11-06 and the four block decks since 2026-11-09 (`cases-deck/README.md`, section "On
the course site"); `cases.pdf` is linked from nowhere.

Since 2026-11-06 the folder also holds one short deck per case, its text dictated by Carlos slide by slide, with
diagrams: Etsy (5 frames, the search by inner product built over four pages with invented numbers from the
generator), Spotify (3 frames) and Airbnb (3 frames, Airbnb's embedding-based retrieval, preprint of January 2026
and blog of April 2025). He asked that day for five 10-minute cases, one after each Friday block, none older than
five years. The same day he asked for them "25%
simpler", and the words on their slides went down by 25%, 31% and 36% (`cases-deck/README.md`). The same evening
they became one deck for the weekend, `weekend2-cases.tex` (28 pages, a divider per case), built from the same
frames files, and `cases-deck/PRINCIPLES.md` collected the lessons and the rules for the next case decks. Same build and checks, with
`tools/check_numbers.py <deck>.pdf tools/expected-<deck>.txt`. Later that evening Carlos chose the cases of the
bandit block and of advertising and asked for them in the style of the matrix factorization case: Spotify's home
page (epsilon-greedy), Amazon Payments (one UCB score per step of an application) and LinkedIn's ads model (lists
of numbers learned by gradient descent), 3 frames each, built on the pattern of the Spotify case without dictation;
the weekend deck has 6 sections and 52 pages since. On 2026-11-09 Carlos asked for one deck per block ("for each
block, put in one single deck all the slides with all the business cases"): a case is its frames file
`<case>-frames.tex`, the four block decks input them (`block1-nearest-neighbors.tex`: Etsy, Airbnb;
`block2-matrix-factorization.tex`: Spotify; `block3-bandits.tex`: Spotify's home page, Amazon Payments;
`block4-parallelized-mf.tex`: LinkedIn's ads), the six one-case decks were removed, and the weekend deck follows the
order of the blocks.

## The cold intro deck (added 2026-11-10)

`cold-intro-deck/block1-nearest-neighbors.tex` is the cold intro of weekend 2, shown before the Friday 08:15 block,
the inner product and nearest neighbors: Chunyu Kun answers King Xuan of Qi, "birds with the same wings live
together" (*Zhanguo ce*, Qi 3), 5 frames over 8 pages. Carlos chose the story on 2026-11-10 from four rounds of
candidates (`git_ainit/research_notes/Weekend 2 cold intros/`) and dictated the frames the same day: the title frame,
a context frame, the king's question and Kun's answer in his English with the key sentence highlighted, and a closing
frame on representation learning. The first build (commit `0beb06a`: the Chinese on every frame and a mapping of the
story's words to the block) is replaced.
The look is the dark Title sequence of the course cold intro (`w1-lecture-material/cold-intro/intro-slides/`), the
one exception to Codex plates. Every picture is cut by `make_images.py` from Emperor Huizong's *Auspicious Cranes*
(1112, public domain). Build from inside the folder with `../style/tools/build.sh block1-nearest-neighbors.tex`;
the folder's CLAUDE.md has the traps. On the course site since 2026-11-11 (AINIT-PAGE commit `dc80aeb`, the Friday
08:15 row and the Materials list; `cold-intro-deck/README.md`, section "On the course site"). A push also makes the
PDF public on Pages.

`cold-intro-deck/block5-computing-clusters.tex` is the cold intro of the Saturday 08:15 block, computing clusters:
"Dividing a computation, 1793", FDD weekend 7's section of that name in the same form, 5 frames over 10 pages
(Prony's "fabriquer mes logarithmes comme on fabrique des epingles", Adam Smith's pin factory, every parcel in
France, the three tiers, and a closing frame "Computing clusters" with four facts of the lecture deck). Carlos asked
on 2026-11-10 to leave out FDD's two frames on triangles and logarithm tables. On the course site with the lecture
deck (`clusters-deck/README.md`, section "On the course site").

## The computing clusters deck (added 2026-11-10)

`clusters-deck/block5-computing-clusters.tex` is the Saturday 08:15 block, "Computing clusters": a port into Codex
plates of the first block of FDD weekend 7, "The cost of computation and supercomputers" (git_fdd,
`w7-cost-slides.tex`, commit `b296f78`), with the cuts and changes Carlos dictated on 2026-11-10. Five sections, 21
frames: a FLOP and the GH200; Alps, drawn from a cabinet to one blade, and the blade types of its platform; CSCS,
nodes and sockets; capacity and bandwidth; watts, kilowatt hours and the bill; the four links drawn with their
speeds; 6ND on Apertus-70B; dollars and gigawatt hours. Every number is FDD's or a platform fact checked against
HPE and CSCS (`clusters-deck/tools/check_port.py`). Build from inside the folder with
`../style/tools/build.sh block5-computing-clusters.tex`. Its README.md maps every frame to FDD's slide numbers and
lists the slides not ported.

## The lecture notes (added 2026-11-11)

`lecture-notes/nearest-neighbors-and-matrix-factorization.pdf` holds the notes of the Friday blocks 08:15 to 12:00,
asked for "terse and to the point": the inner product, the nearest neighbor classifier, the matrix product and
matrix factorization (one number at a time, gradient descent, predicting unknown ratings), each section ending in
links to its game on the course site and its Colab notebook. The worked examples are the games' own (Vera and Kai,
Sara and The Intouchables, The Martian's second number, three hidden MovieLens ratings), computed by
`lecture-notes/tools/notes_numbers.py` from copies of the `w2-cx-private` data that it checks against that checkout.
On the course site since 2026-11-11 (AINIT-PAGE `8bf143b`): in weekend 2's Materials list and in the weekend's ZIP.
`lecture-notes/CLAUDE.md` has the build and the TikZ gotchas.

## The cheat sheet (added 2026-11-11)

`cheat-sheet/cheat-sheet.pdf` is the semester on one A3 landscape page, asked for as "a mind map of all the
concepts" and "an orientation guide for the participants on when to use each technology": the three weekends as
branches, 30 cards in 14 groups, each card with what it is, "Use it when" and "In industry". The concepts are the
Syllabus rows of the master spreadsheet and the course site; every named case has its source in
`cheat-sheet/SOURCES.md`. It lives here because it was built during weekend 2; it covers all three weekends. On the
course site since 2026-11-11 (AINIT-PAGE `ab95b28`): a button beside the intro deck on the home page and a group at
the top of weekend 2's Materials. `cheat-sheet/CLAUDE.md` has the build, the layout and the way to republish.

## When in doubt

- Read `NARRATIVE_PLAN.md` first. It is the contract.
- Then `BOOKS_MATRIX.md` if you are touching anything that consumes `shared/data.js`.
- Then this file.
- Then ask the user.

## Maintenance contract

- This file is the working memory for this repository. After any major change here, meaning a new
  demo, notebook or deck, a renamed or moved directory, a changed build or deploy procedure, or a
  changed data format, UPDATE THIS FILE IN THE SAME COMMIT.
- Every subdirectory that holds work of its own carries its own CLAUDE.md, and that file must itself
  carry this same maintenance contract, including this propagation rule. When you create a
  subdirectory, create its CLAUDE.md at the same time.
- Keep it concrete: real file names, real identifiers, real commands. Record the gotchas that cost
  someone an hour. Do not restate what the code already says plainly.
