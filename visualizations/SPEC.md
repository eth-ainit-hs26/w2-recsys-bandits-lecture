# Visualizations — design spec

This folder hosts interactive single-file HTML visualizations for the **W2 Recsys** lecture of CAS AINIT FS26 at ETH Zürich. Each viz teaches one or two key concepts from `../w2_recsys.pdf`.

**References:**
- Existing reference: `../rating_matrix (3).html` (drag-and-drop ratings matrix; aesthetic and pattern source).
- External reference: <https://sml-fs26.github.io/pca-kmeans-rf/> (sister course's viz collection — aesthetic cues only).

## Aesthetic

Clean ETH white-card. Soft drop shadows, generous spacing.

- Page background `#FFFFFF`.
- Cards: `background: #FFFFFF; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);`.
- Header band: dark gradient `#2C3E50 → #34495E`, white text, simulated ETH logo (text "ETH zürich" with bold "ETH" and italic "zürich"; no need for the actual ETH wordmark).
- Headings light weight (300–400). No decorative fonts.
- Accent gradients live only in the page header — never inside the viz itself.

## Color palette (mandatory across all viz)

The palette is the [Okabe-Ito](https://jfly.uni-koeln.de/color/) qualitative
8-color set, tested CVD-safe for deuteranopia, protanopia, and tritanopia.
The slide colors (yellow / purple / cyan / red, green / red ratings) collapse
to two perceived hues under deuteranopia (~5–8% of men) — the palette below
fixes this.

**Latent-axis colors:**

| Token | Hex | Notes |
|---|---|---|
| Simple | `#E69F00` orange | warm; replaces slide's mustard yellow |
| Technology | `#CC79A7` reddish purple | replaces slide's purple |
| Outdoor | `#56B4E9` sky blue | replaces slide's cyan |
| Indoor | `#009E73` bluish green | **replaces slide's red — see note** |

> **Indoor = green, not red.** Slide's red and any "negative" red collide
> with each other under deuteranopia (both fall to brownish-yellow). Swapping
> Indoor to bluish green keeps all four axis colors pairwise distinguishable
> for every CVD type. Announce this mapping when introducing slide 8, or
> update the slide colors to match.

**Rating colors (CVD-safe blue/vermillion diverging):**

| Token | Foreground | Background |
|---|---|---|
| Positive ✅ | `#0072B2` blue | `#D6E6F2` |
| Negative ❌ | `#D55E00` vermillion | `#FCE4D6` |
| Neutral ➖ | `#6C757D` gray | `#F8F9FA` |
| Unknown ❓ | `#B8860B` dark gold | `#FFF6CC` |

The blue/vermillion pair is the standard anchor for CVD-safe diverging
scales — distinguishable by both hue and lightness for all CVD types.
**Never use red/green pairings.**

**Symbols carry redundancy.** Every rating cell shows ✅ / ❌ / ➖ / ❓ so
color is not the only cue. Cluster markers should pair color with shape
(different glyphs per quadrant) where possible.

Chrome:

| Token | Hex |
|---|---|
| Card / page background | `#FFFFFF` |
| Border | `#E9ECEF` |
| Body text | `#212529` |
| Muted text | `#6C757D` |
| Header gradient start | `#2C3E50` |
| Header gradient end | `#34495E` |

These tokens are also exported as CSS variables in `shared/style.css` (`--color-simple`, `--color-tech`, etc.) and as a JS object in `shared/data.js` (`RECSYS.COLORS`).

## Typography

```
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
             "Helvetica Neue", Arial, sans-serif;
```

- Body: 16px / 1.55 line-height.
- H1: weight 300, ~2rem.
- H2: weight 400, ~1.4rem.
- Math: KaTeX (CDN) via `<link>` + `<script>`; use `katex.render(...)` or auto-render. Inline `$...$` and display `$$...$$`.

## Tech stack

- D3.js v7 — `https://cdn.jsdelivr.net/npm/d3@7`
- KaTeX 0.16.x — `https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/`
- No build step. No frameworks. CDN only.
- For matrix math, prefer hand-rolled JS (the matrices are tiny). Avoid mathjs unless necessary.

## File conventions

```
visualizations/
├── SPEC.md                          (this file)
├── shared/
│   ├── data.js                      (items, people, ratings, embeddings, helpers)
│   └── style.css                    (ETH chrome shared by all viz)
├── 01_block-diagonal-puzzle.html
├── 02_latent-axes-lab.html
├── 03_inner-product-compass.html
├── 04_dot-product-bistro.html
├── 05_build-a-rating.html
├── 06_outer-product-painters.html
├── 07_embeddings-that-learn.html
├── 08_filling-the-holes.html
├── 09_movielens-taste-map.html
├── 10_embedding-interpolation.html
├── 11_cold-start-cliff.html
└── index.html                       (landing page; built last)
```

- Filename: `NN_kebab-name.html`, NN = lecture order.
- Each viz file: `<link rel="stylesheet" href="shared/style.css">` and `<script src="shared/data.js"></script>`.
- All viz-specific CSS/JS inline within the file. No per-viz extra files.

## Layout pattern

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{viz title}</title>
  <link rel="stylesheet" href="shared/style.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <style>/* viz-specific */</style>
</head>
<body>
  <header class="eth-header">
    <div class="eth-logo">ETH<em>zürich</em></div>
    <nav><a href="index.html">← All visualizations</a></nav>
  </header>
  <main class="viz-container">
    <h1>{viz title}</h1>
    <p class="lede">{one-sentence pedagogical hook}</p>
    <div class="viz-card">
      <div id="viz"><!-- the visualization --></div>
      <div class="controls"><!-- sliders / buttons --></div>
    </div>
    <aside class="explainer">
      <h2>What's happening?</h2>
      <p>{2–4 sentences tying the viz back to the slide concept}</p>
    </aside>
  </main>
  <footer class="eth-footer">CAS AINIT FS26 · W2 Recsys</footer>
  <script src="shared/data.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
  <script>/* viz code */</script>
</body>
</html>
```

## Interaction patterns

1. **Click-step** — discrete stages, "Next" / "Back" buttons + arrow keys. For algorithmic walkthroughs.
2. **Live continuous** — drag, hover, slider. For state-space exploration.
3. **Animation loop** — `requestAnimationFrame` for live training; play/pause/reset.

## Acceptance criteria for every viz

- Opens directly in Chrome / Safari / Firefox by double-clicking the file (no server). `shared/*` paths must be relative.
- No console errors on load.
- Responsive down to 1024px width (lecture projector).
- Works with mouse alone for primary interactions.
- WOW moment reachable within 30 seconds of loading.
- Math renders correctly (KaTeX).
- Uses palette and typography from this spec exclusively.

## Don'ts

- No Tailwind, no React, no Vue, no build step.
- No internet at runtime except the listed CDNs.
- Don't fork the data — pull from `shared/data.js`.
- Don't modify `../rating_matrix (3).html` or `../urn_games (1).html`.
