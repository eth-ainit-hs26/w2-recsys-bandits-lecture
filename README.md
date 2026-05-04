# Recommendation Systems and Bandits · AI in Industry · Week 2

### → **[https://eth-ainit-fs26.github.io/recsys_bandits_lecture/](https://eth-ainit-fs26.github.io/recsys_bandits_lecture/)** ←

The live site is the **lecture's companion page.** Participants visit
it on their laptop or phone at the start of the lecture; the ten
interactive demos used during the talk are listed there in the order
the lecturer will visit them. When a slide says *"Demo N"*, the
participant clicks the matching numbered card.

Slide 2 carries a QR code so the room can join in seconds.

---

A 90-minute lecture on recommendation systems and bandits, taught to
managers, framed as a single question: *what is the difference between
**memory** and **prediction**?*

- **Lecturer:** Carlos Cotrini, ETH Zürich
- **Course:** AI in Industry, Week 2, Spring 2026
- **Source:** [github.com/eth-ainit-fs26/recsys_bandits_lecture](https://github.com/eth-ainit-fs26/recsys_bandits_lecture)
- **Deploy:** every push to `main` runs `.github/workflows/pages.yml`,
  which deploys the whole repo to GitHub Pages
  (enable once at *Settings → Pages → Source: GitHub Actions*).

## Quick start

| What | Where |
|---|---|
| Open the companion page locally | `open index.html` |
| View the slides | `slides/lecture.pdf` |
| Build the slides from source | `cd slides && bash build.sh` (LuaLaTeX) |
| Run any one visualization | `open visualizations/<name>.html` |
| Read the narrative arc | `NARRATIVE_PLAN.md` |
| Read the data design | `BOOKS_MATRIX.md` |
| Get the design system | `theme/ainit-academic/` |
| Long-form context for future Claude sessions | `CLAUDE.md` |

## Repository layout

```
recsys_bandits_lecture/
├── index.html              Live companion page (demos in lecture order)
├── slides/                 Beamer source + compiled PDF
├── theme/ainit-academic/   Custom Beamer theme (LuaLaTeX, EB Garamond)
├── visualizations/         18 single-file interactive viz (D3 + KaTeX)
├── original-decks/         Pre-rebuild lecture PDFs (Nov 2025)
└── archive/                Early prototypes
```

`CLAUDE.md` has the long version.

## License

The slides, narrative, and visualizations are released for educational
use. The original-deck PDFs and the ETH branding remain the property
of ETH Zürich.
