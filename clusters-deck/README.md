# Computing clusters, in the Friday 16:00 block "Large-scale computing" of weekend 2

The Saturday 08:15 block of weekend 2 until 2026-11-11, when Carlos merged it with parallelized matrix factorization:
"computing clusters is now merged with parallelized matrix factorization, and it's going to be called large-scale
computing". The title page reads Friday 13 November 2026 since then.

A port into Codex plates of the first block of FDD weekend 7, "The cost of computation and supercomputers"
(`git_fdd/projects/weekend-07-large-scale/carlos-lectures/slides/w7-cost-slides.tex`, commit `b296f78`), with the
cuts and changes Carlos dictated on 2026-11-10. Saturday 14 November 2026, 08:15. 124 pages: a title page, five
section dividers and 21 frames. The cold intro of the block, FDD's section "Dividing a computation, 1793", is in
`../cold-intro-deck/`.

## Files

| File | What it is |
|---|---|
| `block5-computing-clusters.tex` | The deck. Above each frame a comment names its FDD slide and what changed |
| `alps-platform-frame.tex` | The two platform frames, input by the deck. Its header lists the facts and their sources |
| `clusters-kit.tex` | The drawings: the styles `box`, `box strong`, `box quiet`, `part`, `link`, `leader`, `zoom`, the sheet, and the macros `\cxsheet`, `\cxsrc`, `\cxsrctwo`, `\arxiv`. Its header maps FDD's style names to these |
| `img/human-computers-1949.jpg` | The photograph of "One computer, then and now". `img/SOURCES.md` has its source |
| `tools/check_port.py` | Checks that every number on the slides is FDD's or one of the added facts it lists |
| `block5-computing-clusters.pdf` | The deck, 124 pages |
| `block5-computing-clusters-handout.pdf` | The handout, one page per frame, 27 pages |

## Build and check

From this folder:

```bash
../style/tools/build.sh block5-computing-clusters.tex
../style/tools/check.sh block5-computing-clusters.pdf
python3 ../style/tools/check_overlays.py block5-computing-clusters.pdf
python3 tools/check_port.py
python3 ../style/tools/make_handout.py block5-computing-clusters.pdf block5-computing-clusters-handout.pdf
```

State on 2026-11-10: no build errors, no dash, nothing moves between clicks, every number accounted for.

## Frames

"Slide" is the number printed on the slide. FDD's numbers count its title page and section dividers.

| Slide | Title | FDD slide | Change |
|---|---|---|---|
| | Section 1, "One operation, and who does it" | | |
| 1 | A FLOP is one operation on two numbers | 11 | Ported |
| 2 | One computer, then and now | 12 | One sheet under both pictures, one click per row. The captions under the pictures are dropped; the photograph's credit is the source line |
| 3 | A GH200 is a CPU and a GPU on one module | 13 | FDD's three bullets are glosses on the drawing |
| 4 | Alps is an HPE Cray EX254n | 14 | Drawn, at Carlos's request: one cabinet (8 chassis), one chassis (8 blade slots, 7 used at Alps), one EX254n blade (2 nodes of 4 GH200) |
| 5 | One platform, several blade types | 14 | New, same request: five blades of the HPE Cray EX platform, a box per node |
| 6 | The atelier against Alps | 15 | Ported |
| 7 | CSCS and Alps, the machine behind Apertus | 17 | "At dense BF16 the whole partition is about" and the TOP500 sentence dropped. 10.6 EFLOP/s is written as 10.6 × 10^18 FLOP/s. A last line introduces Apertus, which FDD's title called "the anchor" |
| 8 | Nodes and sockets | 30 | Moved here from FDD's section 4, at Carlos's request |
| 9 | One second of a GH200, in three registers | 18 | Ported |
| | Section 2, "What the headline rate hides" | | |
| 10 | Capacity and bandwidth are different numbers | 25 | Ported |
| 11 | Two hundred and forty six operations per byte | 26 | Ported |
| | Section 3, "The machine, and what it draws" | | |
| 12 | A watt is a rate, a kilowatt hour is an amount | 28 | Its first half: the tap and the glass of water |
| 13 | Watch the slash | 28 | Its second half: km/h and kWh, then rate × time = amount, FLOP/s × seconds = FLOP, watts × hours = watt hours |
| 14 | A wattage becomes a bill in two multiplications | 29 | Ported |
| 15 | Four links, and each step down costs you | 31 | Drawn: Alps, one node, one GH200, inside the GPU, each a zoom into the part outlined in the panel before. Each link carries its speed: 4,023 GB/s the GPU to its HBM3, 900 GB/s Grace to Hopper, 150 GB/s socket to socket, 25 GB/s per GPU between nodes |
| | Section 4, "From a model to GPU hours" | | |
| 16 | Two numbers price a training run | 33 | "Training tokens" is "training numbers", here and on every later frame |
| 17 | A million by a million is two minutes | 34 | Ported |
| 18 | The same formula on Apertus-70B | 36 | Carries the model source of the dropped slide 35 |
| 19 | From one GPU hour to the whole run | 37 | Its first line gives the 6 million GPU hours on up to 4,096 GPUs, with the run paper that slide 35 cited |
| | Section 5, "Dollars and energy" | | |
| 20 | Six million hours, priced at cloud rates | 45 | Ported |
| 21 | The same hours, in gigawatt hours | 46 | Ported |

## FDD slides not ported

| FDD slide | Title | Reason |
|---|---|---|
| 2 | The same three questions, asked for the AI | Carlos: skip |
| 3 | What the next hour computes | Carlos: skip |
| 5 to 7 | Adam Smith, 1776; The task: the area of every parcel in France; Three tiers, and what each hands down | The cold intro, `../cold-intro-deck/` |
| 8, 9 | One parcel, many triangles, one each; One side, two angles, and a table of logarithms | Carlos: skip |
| 16 | What the TOP500 actually measures | Carlos: skip |
| 19 | One training step of linear regression | Carlos: skip |
| 21 to 24 | One floating point number, taken apart; What the seven bits cost; Not every FLOP costs the same; Why we say dense BF16, and not just BF16 | Carlos: skip section 3 but for slides 25 and 26 |
| 35 | The anchor: Apertus, trained on Alps | Carlos: drop |
| 39 to 43 | Section 6, "Peak, and what a real run gets" | Carlos: drop entirely |
| 47 | What you can price | Dropped without asking: it is the closing twin of slide 3, its middle box is "Peak × MFU" (section 6), and it hands over to an FDD lecture and an FDD exercise |

## Changes made without asking

- "The atelier against Alps" (FDD 15) is kept. Carlos's list does not name it.
- "Dense BF16" is gone from every frame. FDD's "990 TFLOP/s dense BF16" is "990 × 10^12 FLOP/s", with "16 bits per
  number" in the row Format of slide 2. Every rate with a prefix is written as a power of ten, after Carlos's
  question about the E of EFLOP/s.
- "The trailing n marks the NVIDIA accelerated blades" is "Every name here that ends in n carries NVIDIA GPUs":
  HPE's documents show the pattern and state no rule.
- "Top to bottom, 161 times" is "End to end, 161 times", since the drawing runs from left to right.
- "A campaign is not one uninterrupted run at full width" is "a campaign rarely runs at full width without a
  break", for the house write hook.
- FDD's two energy figures stay as FDD has them: 3.96 GWh on slide 19 (6 million GPU hours at 660 W) and 4.95 GWh
  on slide 21 (8.85 million GPU hours at 560 W).
- The deck no longer derives the 6 million GPU hours (FDD's section 6). Slide 19 states them with their source.

## Numbers

Every number is FDD's (its `NUMBERS.md`, sections A and G) except the facts of the two platform frames, checked
on 2026-11-10 against HPE's QuickSpecs of the Cray EX (version 22, 21 September 2026, a00094635enw) and CSCS's
hardware page (docs.cscs.ch/alps/hardware): 8 chassis a cabinet, 8 blade slots a chassis, 7 used in Alps's GH200
chassis, 2 nodes of 4 GH200 an EX254n blade, 24 cabinets, and the node layout of the five blades.
`tools/check_port.py` lists each with its source.

## On the course site

Since 2026-11-10, on the Saturday 08:15 row and in the Materials list, group "Lecture slides": this deck since
AINIT-PAGE commit `0f4cd90`, the cold intro before it since `a498851`. Since 2026-11-11 (AINIT-PAGE `9e0be17`) the
chips read "Computing clusters, cold intro", "Handout", "Computing clusters", "Handout", numbered 15 and 16 that day
from the agenda, and the Materials list shows them under "Slides and visualizations".
Since AINIT-PAGE `5ab848e` (2026-11-11) both are on the Friday 16:00 row, "Large-scale computing", followed by Matchmaker
on a Grid and the case LinkedIn's ads: chips "Large-scale computing, cold intro" (14), "Computing clusters" and
"Handout" (15), "Matchmaker on a Grid" (16), "Business case, LinkedIn's ads" (17), its handout removed in AINIT-PAGE
`9d5e19e` (Carlos: "Remove also the handouts for the business cases"). The cold intro's handout is off the site since
`5ab848e` (Carlos: "drop the handouts for all the cold intros"). This deck's handout is the only handout left on
weekend 2.

| Site file | Source here |
|---|---|
| `ainit-hs26-computing-clusters.pdf` | `block5-computing-clusters.pdf` |
| `ainit-hs26-computing-clusters-handout.pdf` | `block5-computing-clusters-handout.pdf` |
| `ainit-hs26-computing-clusters-cold-intro.pdf` (until 2026-11-12) | `../cold-intro-deck/block5-computing-clusters.pdf` |
| `ainit-hs26-large-scale-computing-cold-intro-and-cases.pdf` (since 2026-11-12) | `../cold-intro-and-cases/block4-large-scale-computing.pdf`: the cold intro, then the case LinkedIn's ads |

Since AINIT-PAGE `c01c44e` (2026-11-12) the 16:00 row reads, in Carlos's order ("merge large-scale computing cold
intro with business case, LinkedIn ads, then computing clusters in that order"): "Large-scale computing" (11, the cold
intro and the case in one PDF), "Computing clusters" and "Handout" (12), "Matchmaker on a Grid" (13).

A live file is https://eth-ainit-hs26.github.io/AINIT-PAGE/slides/we2/<file>
After a rebuild, copy the PDF and its handout over the same site file names, run `npm ci && npm run build` in `AINIT-PAGE`, push to
`main`, then curl the live file and `cmp` it with the one here.

## Open items

1. Eight frames are over the 70 words of the house rule (title and text, source line excluded): slide 2 (72
   words), 3 (73), 4 (72), 10 (77), 11 (90), 14 (79), 15 (81), 19 (76). FDD's wording is kept.
2. Not projected in HG D 7.2.

## Maintenance

Update `CLAUDE.md` and this file in the same commit as any change to a frame, a number, a source or the build.
