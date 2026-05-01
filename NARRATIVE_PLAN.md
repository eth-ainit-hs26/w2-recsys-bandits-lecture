# W2 lecture — narrative plan

**Course:** CAS AINIT FS26 · Week 2
**Audience:** managers without technical background
**Format:** 90 minutes, lecture + interactive viz, ETH academic register
**Lecturer:** Carlos Cotrini

This document is the contract for every downstream artefact (Beamer slides, viz files, speaker script, books matrix data). When in doubt, this file is the source of truth.

---

## The thesis

> *Machine learning is the engineering of two old theorems. Compression — the shortest faithful description of the past — and prediction — the best bet about the future — are two views of the same subject, governed by Shannon's 1948 theorems. We will build them in two halves and collapse them in the third.*

Recommendation systems live on the compression side. Bandits live on the prediction side. Both are bounded above by the same information-theoretic ceilings. The lecture's intellectual spine is three lower bounds (Eckart–Young 1936, Shannon entropy 1948, Lai–Robbins 1985) and one equation that shows they share a single quantity (KL divergence).

---

## The four-act spine

| Block | Time | Scenes | What it does |
|---|---|---|---|
| Prologue | 5 min | 1–3 | Funes; thesis stated |
| Act I — Compression | 30 min | 4–12 | Book matrix → factorization → urns |
| Interlude — Shannon | 7 min | 13–16 | Entropy as the compression floor |
| Act II — Prediction | 30 min | 17–24 | Bandits → ε-greedy → Lai–Robbins floor |
| Epilogue — Duality | 8 min | 25–27 | The Twin viz; KL as protagonist; Funes returns |

Acts I and II are deliberately equal in length. The lecture has bilateral symmetry around the Shannon interlude.

10-minute buffer absorbs slippage.

---

## Cross-cutting threads

### Three philosophical pillars at fixed scenes

- **Funes** (Borges, 1942): opens at scene 2, returns at scene 27.
- **Shannon** (1948): anchors the interlude, scenes 13–16.
- **The duality** (Hutter prize 2005; Delétang et al. 2023): lands at scenes 25–26.

### Six equations

Each equation appears on its own slide, never crowded, read aloud once.

| # | Equation | Scene | One-line gloss |
|---|---|---|---|
| 1 | $\hat r_{ui} = u_i^\top v_j$ | 8 | preference is a dot product |
| 2 | $H(p) = -p\log p - (1-p)\log(1-p)$ | 14–15 | the entropy of an urn |
| 3 | $\hat p_n = \tfrac{x_1 + \ldots + x_n}{n}$ | 17 | the empirical estimator |
| 4 | $A_t = \begin{cases}\text{random urn}, & \text{w.p.}\ \varepsilon\\ \arg\max_i \hat p_{n_i}, & \text{w.p.}\ 1-\varepsilon\end{cases}$ | 21 | ε-greedy |
| 5 | $\liminf\frac{R_T}{\log T} \geq \sum_{i \neq i^*}\frac{\mu^* - \mu_i}{\mathrm{KL}(\mu_i \| \mu^*)}$ | 24 | Lai–Robbins lower bound |
| 6 | $\text{cross-entropy} = H(p) + \mathrm{KL}(p \| \hat p)$ | 26 | floor + inefficiency |

### Three named lower bounds

- **Eckart–Young (1936)** — closes Act I; floor for matrix compression.
- **Shannon entropy (1948)** — anchors the interlude; floor for sequence compression.
- **Lai–Robbins (1985)** — closes Act II; floor for prediction regret.

The epilogue collects the debt: all three involve KL divergence in different roles.

### Eight citations

Spread across nine decades, one citation roughly every 11 minutes.

| Year | Author | Where |
|---|---|---|
| 1936 | Eckart & Young | scene 10 |
| 1942 | Borges | scenes 2 and 27 |
| 1948 | Shannon | scenes 13, 15 |
| 1985 | Lai & Robbins | scene 24 |
| 1998 | Sutton & Barto | scene 21 (ε-greedy) |
| 2005 | Hutter | scene 25 |
| 2023 | Delétang et al. | scene 25 |

### Eleven interactive moments

| Scene | Viz | Status |
|---|---|---|
| 5 | Block-diagonal puzzle | retrofit existing |
| 7 | Latent-axes lab | retrofit existing |
| 9 | Spectral microscope | NEW |
| 11 | Customer-Urns Carousel | NEW (anchor) |
| 12 | Embeddings that learn | retrofit existing |
| 14 | Entropy Mountain | NEW |
| 20 | Three-Urn Casino | NEW |
| 22 | Algorithm stadium | retrofit existing |
| 23 | Distinguishability Dial | NEW |
| 25 | Compression-Prediction Twin | NEW (climax) |

Average pacing: one interactive moment every ~8 minutes. No frontal block exceeds ~5 minutes between scenes 6 and 26.

### One noun: *urn*

The urn metaphor carries the whole 90 minutes. Three roles, one vocabulary:

- **Act I:** an urn is a *reader* whose hidden bias is their preference for a particular book.
- **Act II:** an urn is a *campaign* whose hidden bias is its conversion rate.
- **Epilogue:** an urn is a *signal source* whose hidden bias determines how compressible its draws are.

---

## Scene-by-scene plan

Each scene gives: time bracket, what's on screen, what the audience does, the lecturer's intent (talking points), and the citation/equation/viz tags.

---

### Prologue (5 min)

#### Scene 1 — Title (00:00 → 00:01)
- **On screen:** ETH title slide; *"Two engines of machine learning: prediction and compression."*
- **Audience:** settling.
- **Intent:** welcome; state the promise — *"by the end of 90 minutes you will have seen two ideas, both older than computers, that quietly run most of modern AI."*
- **Tags:** slide.

#### Scene 2 — Funes (00:01 → 00:03)
- **On screen:** stylized library; the Funes quote — *"To think is to forget differences, generalize, abstract."*
- **Audience:** listen, read.
- **Intent:** open the philosophical thread. Funes remembers every leaf and therefore cannot read. Compression *is* understanding. This sentence will close the lecture too.
- **Tags:** slide; cite Borges, *Ficciones* (1942).

#### Scene 3 — Thesis (00:03 → 00:05)
- **On screen:** the thesis paragraph in clean type.
- **Audience:** listen.
- **Intent:** state the entire lecture in one paragraph; the audience now knows what they're in for.
- **Tags:** slide.

---

### Act I — Compression (30 min)

#### Scene 4 — The book matrix (00:05 → 00:07)
- **On screen:** 21 readers × 16 books, ratings as ✅ / ❌ / ?. Names anonymous.
- **Audience:** look. Whisper to neighbour for 30 sec: *"do you see structure?"*
- **Intent:** present the matrix as a problem. *"Three hundred and fifty-seven cells. Can your brain remember them? No. But maybe it can compress them."*
- **Tags:** slide.

#### Scene 5 — Block-diagonal puzzle ★ INTERACTIVE (00:07 → 00:14)
- **On screen:** viz `01_block-diagonal-puzzle` (retrofitted to books).
- **Audience:** drag rows and columns; find the clusters.
- **Intent:** let them compress by hand. Frame the score as a compression ratio. Debrief: *"you just compressed 357 ratings into 4 reader-types × 4 book-types. Twenty-two-fold compression, by eye, in seven minutes."*
- **Tags:** viz #1.

#### Scene 6 — The four-corner reveal (00:14 → 00:17)
- **On screen:** the 16 books placed in 2D, axes Fiction/Nonfiction × Light/Demanding.
- **Audience:** listen.
- **Intent:** the axes are not invented. Fiction/Nonfiction is the oldest taxonomic axis in libraries; Light/Demanding maps to readability indices (Flesch, Lexile). *"The geometry was always there. We just named it."*
- **Tags:** slide.

#### Scene 7 — Latent axes lab ★ INTERACTIVE (00:17 → 00:20)
- **On screen:** viz `02_latent-axes-lab` (retrofitted).
- **Audience:** swap axis labels, watch books rearrange.
- **Intent:** the names on the axes are arbitrary; the geometry is not. *"You can rotate this picture; you cannot collapse it."*
- **Tags:** viz #2.

#### Scene 8 — The dot product (00:20 → 00:22)
- **On screen:** equation slide — $\hat r_{ui} = u_i^\top v_j$, with one diagram showing the vectors.
- **Audience:** listen.
- **Intent:** introduce the only algebraic claim in Act I. The user's vector and the book's vector live in the same space; their inner product is the predicted preference.
- **Tags:** slide; equation 1.

#### Scene 9 — Spectral microscope ★ INTERACTIVE (00:22 → 00:26)
- **On screen:** NEW viz **Spectral Microscope** — slider for rank $k$, reconstruction error curve below.
- **Audience:** drag $k$ from 1 to 16, watch the matrix sharpen and the error curve fall.
- **Intent:** compression has diminishing returns. At $k{=}4$, most of the matrix is already there. *"That curve has a name."*
- **Tags:** viz #3.

#### Scene 10 — Eckart–Young (00:26 → 00:28)
- **On screen:** the theorem in plain English, citation visible.
- **Audience:** listen.
- **Intent:** name the floor. *"Among all rank-k approximations of any matrix, the top-k singular values give the best one. Nothing — no algorithm, no clever trick — beats this. It is a 90-year-old theorem."* The lecture's first lower bound.
- **Tags:** slide; cite Eckart & Young (1936).

#### Scene 11 — Customer-Urns Carousel ★ INTERACTIVE (00:28 → 00:34)
- **On screen:** NEW viz **Customer-Urns Carousel**, anchor item is *Russell's History of Western Philosophy*.
- **Audience:** click urns to draw balls (Stage 1, 90 sec); hit "compress" (Stage 2 reveal); meet the new reader (Stage 3 cold-start).
- **Intent:** this is the bridge to Act II. The urn becomes the lecture's permanent noun. *"Twenty-one urns reduce to four archetype urns plus small offsets. That is matrix factorization, in physical objects. The same urns will return after the interlude — in a different role."*
- **Tags:** viz #4; the bridge.

#### Scene 12 — Embeddings that learn ★ INTERACTIVE (00:34 → 00:37)
- **On screen:** viz `07_embeddings-that-learn` (retrofitted).
- **Audience:** watch random initialization → four-corner geometry; re-seed; watch again.
- **Intent:** the structure isn't programmed in; it emerges from gradient descent. Same trick learns image features (mention only). Close Act I cleanly.
- **Tags:** viz #5.

---

### Interlude — Shannon (7 min)

#### Scene 13 — Shannon (00:37 → 00:39)
- **On screen:** Shannon's 1948 paper title page; a small portrait.
- **Audience:** listen.
- **Intent:** name the man and the year. *"His paper has two halves. Both can be stated about urns, in language we'll now translate."*
- **Tags:** slide; cite Shannon (1948).

#### Scene 14 — Entropy Mountain ★ INTERACTIVE (00:39 → 00:42)
- **On screen:** NEW viz **Entropy Mountain** — slider for urn bias $p$, the bell curve $H(p)$ plotted live.
- **Audience:** drag $p$.
- **Intent:** feel entropy. $p{=}0.5$: 1 bit, total uncertainty. $p{=}0.99$: 0.08 bits, almost no surprise. The source-coding theorem is now physical: *no compression scheme can describe an urn's draws in fewer than $H(p)$ bits per ball*.
- **Tags:** viz #6.

#### Scene 15 — The floor stated (00:42 → 00:43)
- **On screen:** one slide — $H(p) = -p\log p - (1-p)\log(1-p)$, with the curve.
- **Audience:** read.
- **Intent:** the second lower bound of the lecture. *"Eckart–Young was the floor for compressing a matrix. Entropy is the floor for compressing a sequence. Both are walls Shannon built."*
- **Tags:** slide; equation 2.

#### Scene 16 — Bridge (00:43 → 00:44)
- **On screen:** one-line slide — *"Recsys was compression. Bandits will be prediction. Same urns, different question."*
- **Audience:** listen.
- **Intent:** signal the turn.
- **Tags:** slide.

---

### Act II — Prediction (30 min)

#### Scene 17 — Three urns and the empirical estimator (00:44 → 00:47)
- **On screen:** three urns with hidden biases, framed as three campaigns. Below them, $\hat p_n = \tfrac{x_1 + \ldots + x_n}{n}$.
- **Audience:** listen, look. Quick show of hands: *"who has run an A/B test?"*
- **Intent:** state the bandit problem in plain words. Goal: maximize total successes across rounds. The empirical mean is the audience's natural instinct: *"draw some balls, average them, pick the best urn."* Mention in passing that more draws → tighter estimate (no confidence-interval machinery).
- **Tags:** slide; equation 3.

#### Scene 18 — Explore vs exploit (00:47 → 00:50)
- **On screen:** a diagram with two arrows — *exploit* (commit to the best so far) and *explore* (keep sampling the others).
- **Audience:** listen.
- **Intent:** the central tension of Act II. Exploit too early → you may have committed to the wrong urn. Explore too long → you waste draws on losers. *"That tension has a name. We will spend the next twenty minutes on it."*
- **Tags:** slide.

#### Scene 19 — Naive estimate-then-exploit (00:50 → 00:53)
- **On screen:** the three-step strawman algorithm, with two drawback bullets.
- **Audience:** listen.
- **Intent:** state the strawman. *"Estimate first for n rounds, then exploit forever. If n is too small we pick wrong; if n is too big we waste draws on losers. The choice of n is the problem we have not solved."*
- **Tags:** slide.

#### Scene 20 — Three-Urn Casino ★ INTERACTIVE (00:53 → 01:00)
- **On screen:** NEW viz **Three-Urn Casino** — three urns with hidden biases; lecturer drives the clicks based on a per-round audience vote.
- **Audience:** vote each round by *show of hands*; lecturer clicks the urn with the most hands. Cumulative reward of the audience's choices is recorded; afterwards naive and ε-greedy are replayed on the same hidden urns for comparison.
- **Intent:** the audience's intuition vs. round-robin vs. adaptive. *"You just felt the explore-exploit tradeoff with your own hands. Now we'll see whether a tiny algorithm beats your instincts."* No phone-poll infrastructure required.
- **Tags:** viz #7.

#### Scene 21 — ε-greedy (01:00 → 01:04)
- **On screen:** equation slide — the ε-greedy rule:
  $$A_t = \begin{cases} \text{random urn}, & \text{with probability } \varepsilon \\ \arg\max_i \hat p_{n_i}, & \text{with probability } 1-\varepsilon \end{cases}$$
- **Audience:** listen.
- **Intent:** introduce the lecture's only bandit algorithm. *"Most of the time, exploit the best urn so far. A small fraction of the time, explore one at random. ε is the dial between the two pressures."* Cite Sutton & Barto. Discuss what happens at the extremes: $\varepsilon = 0$ collapses to greedy (the strawman); $\varepsilon = 1$ collapses to pure random. The right ε sits in between, and good algorithms decay it over time.
- **Tags:** slide; equation 4; cite Sutton & Barto (1998/2018).

#### Scene 22 — Algorithm stadium ★ INTERACTIVE (01:04 → 01:07)
- **On screen:** viz `algorithm_stadium` (retrofitted to race naive / ε-greedy at three values of ε / pure random).
- **Audience:** watch the cumulative-reward and cumulative-regret curves.
- **Intent:** show that growth *rates* differ. Random and pure-greedy grow regret linearly; ε-greedy grows it sublinearly. The slope is the whole story. ε too small → naive failure mode; ε too large → too much exploration; the middle ε wins.
- **Tags:** viz #8.

#### Scene 23 — Distinguishability Dial ★ INTERACTIVE (01:07 → 01:11)
- **On screen:** NEW viz **Distinguishability Dial** — two urns, slider for $|p_1 - p_2|$, sample-size counter that updates live.
- **Audience:** close the gap; watch the required sample size explode quadratically.
- **Intent:** the closer two urns are, the more samples needed. *"That curve is what your statistician means when she says 'we need a million users to A/B-test this'. It is not pedantry. It is Shannon."*
- **Tags:** viz #9.

#### Scene 24 — Lai–Robbins (01:11 → 01:15)
- **On screen:** the bound, KL highlighted in colour:
  $$\liminf_{T \to \infty}\frac{R_T}{\log T} \;\geq\; \sum_{i \neq i^*} \frac{\mu^* - \mu_i}{\mathrm{KL}(\mu_i \,\|\, \mu^*)}$$
- **Audience:** listen.
- **Intent:** the third lower bound. Read aloud: *"no algorithm can beat this rate. The hardest thing in bandits is telling apart distributions that look alike. The cost is in KL divergence — the same KL Shannon used in 1948 to define information. Eckart–Young bounded compression. Lai–Robbins bounds prediction. The two halves of the lecture share one ceiling."*
- **Tags:** slide; equation 5; cite Lai & Robbins (1985).

---

### Epilogue — Duality (8 min)

#### Scene 25 — Compression-Prediction Twin ★ INTERACTIVE (01:15 → 01:21)
- **On screen:** NEW viz **Compression-Prediction Twin**, three modes: binary urn → English text (paragraph from Russell) → tiny language model.
- **Audience:** cycle through modes; watch the Forecaster's loss and the Encoder's bits/ball stay locked together, both approaching $H(p)$.
- **Intent:** the duality made visible. *"A perfect predictor is a perfect compressor. Your forecasting loss equals your compressor's bit rate. Both reach the floor; the gap above the floor is KL."* Close on the LLM mode: cite Delétang et al. (2023) — *"a 7-billion-parameter language model compresses ImageNet pixels better than PNG. It learned text; it compresses images. Hutter is paying €500'000 to whoever does it better still."*
- **Tags:** viz #10; cite Delétang et al. (2023); reference Hutter (2005).

#### Scene 26 — Cross-entropy = floor + inefficiency (01:21 → 01:23)
- **On screen:** the closing equation:
  $$\underbrace{-\mathbb{E}_p[\log \hat p]}_{\text{cross-entropy}} \;=\; \underbrace{H(p)}_{\text{Shannon's floor}} \;+\; \underbrace{\mathrm{KL}(p \| \hat p)}_{\text{your inefficiency}}$$
- **Audience:** read.
- **Intent:** pull all three threads through. *"Recsys: KL is the gap between your factorization and the truth. Bandits: KL is the cost of mistaking one urn for another. Compression: KL is the bits you waste because your predictor is imperfect. One quantity, three roles. Shannon's 1948 ceiling."*
- **Tags:** slide; equation 6.

#### Scene 27 — Funes returns (01:23 → 01:24)
- **On screen:** black slide, white text:
  > *"Funes remembered everything and could think nothing.*
  > *Machine learning forgets almost everything — and that is why it understands."*
- **Audience:** silence.
- **Intent:** close the loop. The lecture began with Borges; it ends inside him. Hold the silence. Then: *"Questions."*
- **Tags:** slide; cite Borges (1942) again.

---

## What this narrative locks in

Reading down the scene list, several invariants are now committed:

- **Ten interactive moments** in 90 minutes — average one every ~9 minutes. No frontal block exceeds ~5 minutes between scenes 6 and 26.
- **Six equations**, evenly distributed, each on its own slide and read aloud once.
- **Seven citations**, spanning 1936 to 2023.
- **Three lower bounds** — Eckart–Young (Act I), Entropy (Interlude), Lai–Robbins (Act II) — and one equation showing they share KL divergence (Epilogue). The intellectual spine is auditable.
- **One noun** — *urn* — carries the whole 90 minutes.
- **One narrative bookend** — Funes opens at scene 2, returns at scene 27.

---

## What this narrative deliberately does not yet contain

Three things belong in downstream specs, not in this storyboard:

1. **Exact ratings in the books matrix** — the 21×16 binary table. Belongs in `BOOKS_MATRIX.md` and `shared/data.js`.
2. **Exact UI of each new viz** — the Carousel and Twin specs already drafted in conversation; the four others (Spectral Microscope, Entropy Mountain, Three-Urn Casino, Distinguishability Dial) need their own one-page specs.
3. **Exact prose of each slide** — derivable from the talking points but not yet written. Belongs in the Beamer slide tracks of Stage 1C.

These are the next three deliverables. None of them block each other once *this* narrative is approved.

---

## Decisions resolved

| # | Decision | Resolution | Implication |
|---|---|---|---|
| 1 | Books matrix design | **Owned by a separate dedicated agent.** Matrix is the star of the show and gets focused design attention. | Blocks Stage 1A until that agent delivers `BOOKS_MATRIX.md` and `shared/data.js`. |
| 2 | Audience polling | **Show of hands only.** No Slido / Mentimeter / phone infrastructure. | Three-Urn Casino simplified to a lecturer-driven viz where the lecturer clicks based on the audience's hands per round. |
| 3 | Twin viz LLM mode | **Yes — include the in-browser language model.** | Adds ~1.5 days to viz #10 build. Tools: TensorFlow.js or ONNX Runtime Web with a small character-level model (≤ ~10 MB, lazy-loaded). The mode reveals the Hutter-prize / Delétang-2023 punchline. |
| 4 | Real urns on stage | **Optional / nice-to-have, not required.** | Speaker script will note it as a stage-prop suggestion (a paper bag with white and yellow chips) but the lecture must work without it. |
| 5 | Beamer theme | **Custom build — stylish, academic, professional, not mainstream.** | See *Visual design direction* below; one downstream agent owns the theme as `theme/ainit-academic`. |

---

## Visual design direction (Beamer theme)

Theme working name: **`ainit-academic`**.

**Design intent.** Stylish, academic, professional, not mainstream. Reference points: Edward Tufte's typography, classical academic-monograph design, restrained Swiss minimalism, the dignified plainness of journals like *Cabinet* or AMS publications. Avoid: Metropolis (overused in academia in 2026), Madrid / Berlin / Frankfurt (bureaucratic), corporate templates, drop-shadows, gradients, rounded corners, emoji, clip-art, stock photography.

The audience is managers, but the venue is ETH. The slides should read like a museum-exhibition catalogue or a classical academic monograph, not like a pitch deck.

### Typography

- **Body & headings:** EB Garamond (free, well-supported in LuaLaTeX). Cormorant Garamond is an acceptable alternative if rendering issues appear.
- **Math:** Latin Modern Math (default `unicode-math` package), italic variables, upright operators. The serif math harmonises with the body text and reinforces the academic register.
- **Sans-serif:** Inter or Source Sans 3, used *only* for tiny chrome (axis labels in figures, slide-number footers). Never for body, headings, or equations.
- **Body size:** 11pt (readable at the back of an ETH lecture hall).
- **Line height:** 1.45.
- **No drop-caps, no decorative initials. No bold. Italic for emphasis only.**

### Color palette

Three colors visible at any time, never more.

| Token | Hex | Use |
|---|---|---|
| `bg-cream` | `#FAF7F0` | page background (warmer than pure white; reduces projector glare) |
| `ink` | `#1A1A1A` | body text and equations |
| `accent-oxblood` | `#722F37` | section bars, KL highlight in equations 5–6, occasional emphasis |
| `accent-prussian` | `#1B365D` | hyperlinks and inline citations only |
| `muted-warm-gray` | `#6E665C` | page numbers, lecture title in chrome |

The two accent colors do not appear on the same slide. Oxblood is for content emphasis; Prussian is for navigation. Every other slide is pure ink-on-cream.

### Layout

- 16:9 aspect ratio.
- Generous outer margins: ≥ 12% of slide width on left and right.
- Single column. Content **left-aligned**, never centered (centered titles read as PowerPoint).
- Slide titles: serif, 24pt, semibold, single line, with a 1pt oxblood underline.
- Body: 16pt, line-height 1.45.
- Equations centered, with generous vertical space; one-line italic caption permitted below.
- Tufte-style sidenote zone in the left margin available for citations and asides on content slides — used sparingly (≤ 1 sidenote per slide).

### Page furniture

- Page number: lower-right corner, warm-gray, no "of N" suffix.
- Lecture short-title (*"Two engines"*): lower-left corner, warm-gray, italic.
- Section indicator (*"Act II — Prediction"* etc.): upper-right corner, oxblood, italic, small caps.
- The ETH zürich wordmark appears on the title slide and the closing slide only. No per-slide logo (reduces chrome).

### Slide templates

| Template | Use | Distinguishing feature |
|---|---|---|
| `title` | scene 1 | full-bleed cream; large serif title; subtitle; lecturer in small caps; ETH wordmark in lower corner |
| `section-divider` | between acts | full-page italic epigraph (Borges, Shannon, etc.) with attribution, then act title in small caps |
| `content` | most slides | title + body + optional left sidenote |
| `equation` | scenes 8, 14, 17, 21, 24, 26 | equation centered, generous whitespace, one-line italic caption |
| `viz-handoff` | between viz scenes | inverse colour: cream-on-ink; centered text *"Now switching to: [viz name]"* — the visual cue that the lecturer is leaving slides for the browser |
| `closing` | scene 27 | black background, white serif text — the Funes-inverse close |

### Equations

Numbered only when cross-referenced. Sections use roman numerals (I–IV) only for the four acts; everything else is unnumbered.

The KL term in equations 5 and 6 is rendered in oxblood, matching the closing slide's emphasis.

### Citations

Inline as superscript footnote markers in serif numerals. Full citations gathered in a `References` slide at the very end (after the closing). No bibliography on every slide.

### Animations

Minimal. Build animations only for:
- equations (one term at a time on scene 24, scene 26)
- the matrix reveal at scene 4
- the four-corner reveal at scene 6

No fade-ins between slides. Hard cuts.

### Build target

- Engine: **LuaLaTeX** (for `fontspec` + EB Garamond).
- Required packages: `fontspec`, `unicode-math`, `xcolor`, `tikz`, `etoolbox`, `appendixnumberbeamer`, `microtype`.
- Class: `beamer` with custom theme files in `theme/ainit-academic/`:
  - `beamerthemeAINITAcademic.sty` (master)
  - `beamercolorthemeAINITAcademic.sty`
  - `beamerfontthemeAINITAcademic.sty`
  - `beamerinnerthemeAINITAcademic.sty`
  - `beamerouterthemeAINITAcademic.sty`

### Acceptance criteria for the theme

A theme is shipped when:
1. A 5-slide demo deck (title, section, content, equation, closing) compiles cleanly with `lualatex`.
2. Renders at 16:9 with all five templates exhibited.
3. Passes a side-by-side aesthetic check: does *not* look like Metropolis, Madrid, or any default corporate/academic template.
4. Embeds an example equation with the KL term highlighted in oxblood.
5. Includes a viz-handoff slide that is unmistakably "the lecturer is now switching to a browser viz".

---

## Changelog

- **v3 (current):** Pending decisions resolved. Books matrix design delegated to a dedicated agent. Audience interactions simplified to show-of-hands (no polling infrastructure). Compression-Prediction Twin will include in-browser LLM mode. Real urns are an optional stage prop. Beamer theme `ainit-academic` is a custom build with full design spec written; engine LuaLaTeX, font EB Garamond + Latin Modern Math, palette ink-on-cream with oxblood and Prussian accents. Scene 20 updated to reflect show-of-hands voting.
- **v2:** Thompson sampling and all Bayesian prerequisites dropped (Beta-bloom viz, posterior framing, UCB confidence-bonus). ε-greedy becomes the lecture's single bandit algorithm at scene 21. Citation registry: Thompson (1933) removed; Sutton & Barto (1998/2018) added. Algorithm stadium reframed to race naive vs ε-greedy at three values of ε. Total scene count unchanged at 27.
- **v1:** initial 27-scene plan with Beta-bloom (scene 18) and UCB+Thompson (scene 21).
