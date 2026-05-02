# Two Engines · AI in Industry · Week 2

### → **[https://eth-ainit-fs26.github.io/recsys_bandits_lecture/](https://eth-ainit-fs26.github.io/recsys_bandits_lecture/)** ←

The live site is the entry point. It opens onto the slides PDF, all eighteen
interactive visualizations grouped by lecture act, the narrative plan, and the
archive. Everything browsable, everything linkable.

---

A 90-minute lecture on recommendation systems and bandits, taught to managers, framed as a single question: *what is the difference between **memory** and **prediction**?*

- **Lecturer:** Carlos Cotrini, ETH Zürich
- **Course:** AI in Industry, Week 2
- **Source:** [github.com/eth-ainit-fs26/recsys_bandits_lecture](https://github.com/eth-ainit-fs26/recsys_bandits_lecture)
- **Deploy:** every push to `main` runs `.github/workflows/pages.yml`, which deploys the whole repo to GitHub Pages (enable once at *Settings → Pages → Source: GitHub Actions*).

## Quick start

| What | Where |
|---|---|
| Open the unified entry page locally | `open index.html` |
| View the slides | `slides/lecture.pdf` |
| Build the slides from source | `cd slides && bash build.sh` (requires LuaLaTeX) |
| Run any one visualization | `open visualizations/<name>.html` |
| Read the narrative arc | `NARRATIVE_PLAN.md` |
| Read the data design | `BOOKS_MATRIX.md` |
| Get the design system | `theme/ainit-academic/` |
| Learn how the lecture was built | `CLAUDE.md` |

## Repository layout

```
recsys_bandits_lecture/
├── index.html              Unified landing page
├── slides/                 Beamer source + compiled PDF
├── theme/ainit-academic/   Custom Beamer theme (LuaLaTeX, EB Garamond)
├── visualizations/         18 single-file interactive viz (D3 + KaTeX)
├── original-decks/         Pre-rebuild lecture PDFs (Nov 2025)
└── archive/                Early prototypes
```

`CLAUDE.md` has the long version.

## License

The slides, narrative, and visualizations are released for educational use. The original-deck PDFs and the ETH branding remain the property of ETH Zürich.
