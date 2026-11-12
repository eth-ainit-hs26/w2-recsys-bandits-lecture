# Cold intro and business cases, one PDF per block

Since 2026-11-12 each block of weekend 2 that has a cold intro opens with one PDF: the cold intro, then the block's
business cases. Carlos, that day: "Nearest neighbors cold intro is going to be merged now with business case, Etsy,
and Airbnb. So they become now together number two, and I want you to call it nearest neighbors", the same for the
14:00 and 16:00 blocks, and "always put the cold intro with the business on top at the beginning before the rest of
the material ... make that for each block the first chip." Later that day, for the 16:00 block: "Notice the slides on
large-scale computing and computing clusters. Merge them, I meant": its PDF ends with the clusters deck since
AINIT-PAGE `5c1a936`.

| File | Pages | Cold intro | Business cases | Site file (`AINIT-PAGE/public/slides/we2/`) | Chip |
|---|---|---|---|---|---|
| `block1-nearest-neighbors.pdf` | 37 = 16 + 21 | `../cold-intro-deck/block1-nearest-neighbors.pdf` | `../cases-deck/block1-nearest-neighbors.pdf` (Etsy, Airbnb) | `ainit-hs26-nearest-neighbors-cold-intro-and-cases.pdf` | Friday 08:15, "Nearest neighbors", first (after the cheat sheet until AINIT-PAGE `6c59082`) |
| `block3-bandits.pdf` | 33 = 16 + 17 | `../cold-intro-deck/block3-bandits-graunt.pdf` | `../cases-deck/block3-bandits.pdf` (Spotify's home page, Amazon Payments) | `ainit-hs26-bandits-cold-intro-and-cases.pdf` | Friday 14:00, "Bandits", first |
| `block4-large-scale-computing.pdf` | 143 = 10 + 9 + 124 | `../cold-intro-deck/block5-computing-clusters.pdf` | `../cases-deck/block4-parallelized-mf.pdf` (LinkedIn's ads), then the clusters deck `../clusters-deck/block5-computing-clusters.pdf` | `ainit-hs26-large-scale-computing.pdf` (until `5c1a936`: `ainit-hs26-large-scale-computing-cold-intro-and-cases.pdf`, without the clusters deck) | Friday 16:00, "Large-scale computing", first; then "Handout", `ainit-hs26-large-scale-computing-handout.pdf`, a copy of `../clusters-deck/block5-computing-clusters-handout.pdf` |

Build, from this folder, after a rebuild of any of the six decks:

```bash
python3 -I merge.py
python3 ../cases-deck/tools/check_links.py block1-nearest-neighbors.pdf block3-bandits.pdf block4-large-scale-computing.pdf
```

The second command checks that the source line of every case page still links to its paper or post (since
2026-11-12, `../cases-deck/README.md`, section "Links to the sources").

Then copy each PDF over its site file, push AINIT-PAGE, curl the live file and `cmp` it with the one here. A live
file is https://eth-ainit-hs26.github.io/AINIT-PAGE/slides/we2/<site file>
