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
├── visualizations/             18 single-file interactive viz (HTML+D3+KaTeX)
│   ├── index.html              Section-organized landing page
│   ├── shared/data.js          THE data layer — books matrix v2, archetypes, helpers
│   ├── shared/style.css        ETH chrome, Okabe-Ito CVD-safe palette
│   └── (18 viz files; see below)
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

## When in doubt

- Read `NARRATIVE_PLAN.md` first. It is the contract.
- Then `BOOKS_MATRIX.md` if you are touching anything that consumes `shared/data.js`.
- Then this file.
- Then ask the user.
