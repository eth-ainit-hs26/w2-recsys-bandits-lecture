# Cold intro of weekend 2: Searching through representations

Weekend 2, Friday 13 November 2026, 08:15, before the inner product and nearest neighbors. The story of Chunyu Kun
at the court of King Xuan of Qi, *Zhanguo ce*, Qi 3, "birds with the same wings". Chosen by Carlos on 2026-11-10
from round 4 of the candidates, `research_notes/Weekend 2 cold intros/lookalikes.md`, L5 (folder
`git_ainit/research_notes`, outside this repository). The frames are the ones he dictated on 2026-11-11, his second
dictation: a title that names the topic, the setting and the challenge in plain words, the surprise, the king's
question, Kun's answer, what Kun says next with its explanation, representation learning, and four uses of it
today. His rule: citations alone confuse, and recounts alone lose the charm of the citations, so the deck mixes
them. Look: the Title sequence of the course cold intro, `w1-lecture-material/cold-intro/intro-slides/`.

## Files

| File | Content |
|---|---|
| `block1-nearest-neighbors.tex` | The deck: 8 frames, 16 pages, a "Say" comment per frame; `\tsapp` sets a row of frame 7 |
| `cold-intro-kit.tex` | The macros: full page picture, half page picture, text, credit, mapping row (unused since the rebuild of 2026-11-10) |
| `make_images.py` | Cuts and grades `img/` from the original painting; reproduces `img/` byte for byte |
| `img/` | `bg-title.jpg`, `bg-pair.jpg`, `bg-arrive.jpg`, `half-court.jpg`, `half-flock.jpg`, `bg-kind.jpg`, `bg-map.jpg` |
| `tools/check_overlays_any.py` | The no-jump check for dark pages, copied from w1-lecture-material |
| `block1-nearest-neighbors.pdf` | The deck |
| `block1-nearest-neighbors-handout.pdf` | The last click of each frame, 8 pages |

## Frames

| Frame | Pages | Picture | Text |
|---|---|---|---|
| 0 | 1 | `bg-title`: the whole painting | AI in Industry, weekend 2. Searching through representations. A story from ancient China. |
| 1 | 2, 3 | `bg-pair`: the two cranes on the ridge ends | The court of King Xuan. The state of Qi, fourth century BC. King Xuan gathers scholars at his court. Good scholars are rare. Chunyu Kun, a witty advisor, brings him new ones. On the click: How long would it take to find seven good scholars? |
| 2 | 4 | `bg-arrive`: the left part of the flock, closer | 淳于髡一日而見七人於宣王。 In one day, Chunyu Kun presented seven men to King Xuan. |
| 3 | 5 | `half-court`, left half: the palace roof, the crane on its left ridge end | King Xuan of Qi, reigned 319 to 301 BC. "Come. I have heard ... are scholars not plentiful, then?" |
| 4 | 6 | `half-flock`, right half: the flock, the crane on the right ridge end | Chunyu Kun, c. 386 to 310 BC. "Not so. Birds with the same wings ... you load them by the cartful." The birds and the beasts sentence in lavender |
| 5 | 7, 8 | `bg-kind`: the right part of the flock | "Things each have their kind ... why only seven scholars?", its first sentence in lavender. On the click: Kun is himself a scholar, so scholars surround him. To find more of a kind, look next to one you already know. |
| 6 | 9 to 11 | `bg-map`: the flock, blurred and dark | Weekend 2. Representation learning. Three statements, one per click: similar data points cluster together; each data point gets a representation, its embedding, a list of numbers with its most characteristic features; data points that belong together get similar embeddings |
| 7 | 12 to 16 | `bg-map` | Weekend 2. Representation learning today. Each side gets an embedding, and the most similar are matched. One row per click: Etsy, a shopper's search with items for sale; Airbnb, a guest's search with homes; RAG systems, a user's prompt with a company's documents; LLMs, the text so far with the most suitable next token. Last: Representation learning is one of the main drivers of AI today. |

English words per frame, on its last page, without the credits: 13, 42, 11, 55, 55, 64, 41, 60 (pdftotext splits
the letterspaced "Weekend 2" into letters; count it as two words). The three quotations are Carlos's text, which is
the gloss of `lookalikes.md`; a script compared them with the PDF, letter for letter, on 2026-11-11.

## Sources

| Item | Source | Checked |
|---|---|---|
| Chinese text, frame 2 | 戰國策, 齊策三, zh.wikisource 戰國策/卷10, https://zh.wikisource.org/wiki/戰國策/卷10, notes in angle brackets removed | A substring of the quotation in `lookalikes.md`, which was matched against that page on 2026-11-09 |
| English | Ours, credited "English: lecturer": the gloss of `lookalikes.md`, chosen by Carlos | Scholars for 士; the mountain names 睪黍 and 梁父 left in Chinese, as in the gloss |
| The book, "Say" of frame 1 | en.wikipedia, Zhan Guo Ce: anecdotes of political manipulation and warfare in the Warring States period, 5th to 3rd centuries BC (490 to 221 BC); edited by Liu Xiang from manuscripts of the imperial library. en.wikipedia, Liu Xiang (scholar): 77 to 6 BC, edited the Zhanguoce | Read 2026-11-10 |
| King Xuan's scholars, frame 1 | Shiji 46 (史記, 田敬仲完世家), zh.wikisource 史記/卷046: 宣王喜文學游說之士，自如騶衍、淳于髡 ... 七十六人，皆賜列第，為上大夫，不治而議論。是以齊稷下學士復盛，且數百千人。 | Read 2026-11-10 |
| Chunyu Kun, frames 1 and 4 | en.wikipedia, Chunyu Kun: a wit, sent several times as an envoy, "able to present scholars for promotion and introduce foreign advisers to the king". zh.wikipedia 淳于髡: c. 386 to 310 BC | Read 2026-11-10 |
| King Xuan of Qi, frame 3 | en.wikipedia, King Xuan of Qi: king of Qi from 319 to 301 BC | Read 2026-11-10 |
| "Say" lines | en.wikipedia, Li (unit): a traditional Chinese unit of distance. en.wikipedia, Bupleurum chinense (柴胡) and Platycodon (桔梗): roots used in traditional Chinese medicine | Read 2026-11-10 |
| Frames 6 and 7, the statements | Carlos's words of 2026-11-10 and 2026-11-11, condensed | |
| Frame 7, Etsy and Airbnb | The two cases of this block, `../cases-deck/` (Jha and others (Etsy), IEEE FMLDS 2024; Abdool and others (Airbnb), arXiv preprint 2026, and Airbnb's blog 2025): one network turns each search into an embedding, another each item or home, and the nearest items or homes join the shortlist. No number of the cases is on this frame | The case deck's README.md has the sources |
| Frame 7, RAG | Retrieval-augmented generation: the document chunks nearest to the prompt are inserted into the prompt (weekend 1) | |
| Frame 7, LLMs | Vaswani and others, *Attention Is All You Need*, NeurIPS 2017, section 3.4: "the usual learned linear transformation and softmax function" turn the decoder output into next-token probabilities, with one weight matrix shared with the embedding layers. So each token's score is the inner product of the decoder output with that token's embedding | arXiv 1706.03762v7, read 2026-11-11 |
| Painting | Emperor Huizong of Song, *Auspicious Cranes* (瑞鶴圖), 1112, Liaoning Provincial Museum. Wikimedia Commons, File:Songhuizong5.jpg | Commons API on 2026-11-10: 9079 by 1846, artist Emperor Huizong of Song, date 1112, licence "Public domain" |
| Painting, facts in "Say" | zh.wikipedia 瑞鶴圖: 20 red-crowned cranes flying and standing over the Xuande Gate of Bianliang; the 16th day of the first month of Zhenghe 2, 22 February 1112 in the Gregorian calendar | Read 2026-11-10 |
| Not verified | The medium of the painting | Not stated on the slides |

## Build

From this folder:

```bash
python3 -I make_images.py /path/to/Songhuizong5.jpg     # only to remake img/; the docstring has the URL
../style/tools/build.sh block1-nearest-neighbors.tex
../style/tools/check.sh block1-nearest-neighbors.pdf
python3 tools/check_overlays_any.py block1-nearest-neighbors.pdf
python3 ../style/tools/make_handout.py block1-nearest-neighbors.pdf block1-nearest-neighbors-handout.pdf "Searching through representations"
```

`build.sh` prints `log errors: 0` and no missing character. `check.sh` lists Futura and Songti TC as the fonts.

## On the course site

Since 2026-11-11 (AINIT-PAGE commit `dc80aeb`), on the Friday 08:15 row before the Video Store game, chips
`Cold intro` and `Cold intro handout`, and in the Materials list, group "Lecture slides", with the label "cold intro:
Searching through representations". Since AINIT-PAGE `9e0be17` the chips read "Nearest neighbors, cold intro" and
"Handout", numbered 02 from the agenda that day, as in the Materials list under "Slides and visualizations". The 8-frame rework is there since AINIT-PAGE commit `70f1db5` (2026-11-11, his
"Yes, replace it"); before, from `dc80aeb`, the 5-frame version of commit `9d9379a`.

| Site file | Source here |
|---|---|
| `ainit-hs26-nearest-neighbors-cold-intro.pdf` (until 2026-11-12) | `block1-nearest-neighbors.pdf` |
| `ainit-hs26-nearest-neighbors-cold-intro-and-cases.pdf` (since 2026-11-12) | `../cold-intro-and-cases/block1-nearest-neighbors.pdf`: this deck, then the cases Etsy and Airbnb |

Since AINIT-PAGE `c01c44e` (2026-11-12) the deck is on the site only as the first part of the chip "Nearest neighbors",
number 02, after the cheat sheet (Carlos, 2026-11-12: "always put the cold intro with the business on top at the beginning before the rest of the material ... make that for each block the first chip"; "they become now
together number two, and I want you to call it nearest neighbors"). After a rebuild, run `python3 -I merge.py` in
`../cold-intro-and-cases/` and copy its output (`../cold-intro-and-cases/README.md`).

The handout, `ainit-hs26-nearest-neighbors-cold-intro-handout.pdf`, is off the site since 2026-11-11 (AINIT-PAGE
`5ab848e`, Carlos: "drop the handouts for all the cold intros"), as are the handouts of the other cold intros.
A live file is https://eth-ainit-hs26.github.io/AINIT-PAGE/slides/we2/<file>
After a rebuild, merge it again (above), copy the output over its site file name, run `npm ci && npm run build` in `AINIT-PAGE`, push to
`main`, then curl the live file and `cmp` it with the merged one. Since AINIT-PAGE commit `8bf143b` the weekend 2
ZIP, `ainit-hs26-weekend-2.zip`, holds it, numbered as on the page; `npm run build` remakes it from the files in
`public/`.

## History

1. 2026-11-10, first build (commit `0beb06a`): the Chinese with our English under it on every frame, and a last
   frame that mapped the story's words to the block (birds to customers, the same wings to similar ratings).
2. 2026-11-10, rebuild to Carlos's dictated frames (commit `9d9379a`): the context frame, the two quotations in
   English only, the closing frame on representation learning; the mapping is gone.
3. 2026-11-11, published on the course site at Carlos's instruction ("Publish them please"): AINIT-PAGE commit
   `dc80aeb`, section "On the course site" above.
4. 2026-11-11, reworked to his second dictation, after he said he did not understand the story: the title
   "Searching through representations" (the first line of the story as a title had left him "a bit lost"), the
   setting and the challenge in plain words, the surprise on the old title look, what Kun says next with an
   explanation, and the four uses of representation learning today. Two new pictures, `bg-arrive` and `bg-kind`;
   the other five are unchanged byte for byte. Commit `f8389a5`.
5. 2026-11-11, the rework replaced the 5-frame version on the course site at his "Yes, replace it": AINIT-PAGE
   commit `70f1db5`, the same file names, the new title in the Materials label, and the weekend 2 ZIP.
6. 2026-11-11, the course site numbers the decks and games of weekend 2 from the agenda (AINIT-PAGE `9e0be17`):
   this deck is 02, its chips "Nearest neighbors, cold intro" and "Handout".

## Open items

1. Not tried on the projector of HG D 7.2.
2. The deck writes "neighbor", as the agenda does; the Video Store game writes "neighbour".

# Block 5: Dividing a computation, 1793

Weekend 2, Saturday 14 November 2026, 08:15, before the block on computing clusters (`../clusters-deck/`). Gaspard
de Prony's tables of logarithms, computed at the Bureau du cadastre in Paris from 1793 to 1796. Ported on 2026-11-10
from the FDD section "Dividing a computation, 1793"
(`git_fdd/projects/weekend-07-large-scale/carlos-lectures/slides/w7-cost-slides.tex`, lines 143 to 349), without
the frames "One parcel, many triangles, one each" and "One side, two angles, and a table of logarithms", which Carlos
asked to leave out. Form of block 1 after its rebuild (commit `9d9379a`): the French on the title frame only, the
quotation in English with its key sentence in lavender, no mapping frame, a closing frame on the block.

## Files of block 5

| File | Content |
|---|---|
| `block5-computing-clusters.tex` | The deck: 5 frames, 10 pages, a "Say" comment per frame |
| `make_images_block5.py` | Cuts and grades the five `img/b5-*.jpg` from four originals and reproduces them byte for byte; URLs, sizes and SHA-1 in its docstring |
| `img/` | `b5-title.jpg`, `b5-half-wire.jpg`, `b5-bg-map.jpg`, `b5-half-room.jpg`, `b5-bg-close.jpg` |
| `block5-computing-clusters.pdf` | The deck |
| `block5-computing-clusters-handout.pdf` | The last click of each frame, 5 pages |

## Frames of block 5

| Frame | Pages | Picture | Text |
|---|---|---|---|
| 0 | 1 | `b5-title`: the pin workshop, *Épinglier* plate II | Paris, 1793. "... fabriquer mes logarithmes comme on fabrique des épingles." "... to manufacture my logarithms as one manufactures pins." |
| 1 | 2 | `b5-half-wire`, right half: the wire drawer, *Épinglier* plate I | Adam Smith, 1723 to 1790. "One man draws out the wire; another straights it; a third cuts it; a fourth points it; a fifth grinds it at the top for receiving the head... Those ten persons, therefore, could make among them upwards of forty-eight thousand pins in a day." The last sentence in lavender |
| 2 | 3 | `b5-bg-map`: the principal triangles around Paris, map of 1744 | Every parcel in France. The French Revolution, 1790 to 1793. The Revolution taxes land, so the area of every parcel has to be computed. Land is measured in triangles, computed with tables of logarithms. In 1793 Gaspard de Prony, director of the Bureau du cadastre in Paris, is ordered to compute new tables. |
| 3 | 4 to 6 | `b5-half-room`, right half: the Harvard computers, about 1890 | Three tiers. Bureau du cadastre, 1793 to 1796. One per click: five or six mathematicians choose the formulas and pass them down; seven or eight analysts turn them into the first values of each page and pass the pages down; about twenty computers fill in each page, using only additions and subtractions. "computers" in lavender |
| 4 | 7 to 10 | `b5-bg-close`: the Harvard room, blurred and dark | Weekend 2. Computing clusters. One per click: on a computing cluster (lavender), one computation is divided among many computers; Alps, at CSCS in Lugano, has 10,752 GPUs (GH200); one GH200 does up to 990 x 10^12 operations per second; training the language model Apertus-70B takes about 6.3 x 10^24 operations |

Words per page without the credits (pdftotext, glyph boxes taller than 8.5 pt): 26, 49, 53, 49, 55. Block 1 by the
same count: 21, 58, 55, 58, 57.

## Changes from the FDD wording

1. Frame 0: Prony's French moved here from the FDD tiers frame and cut to its last clause; the whole sentence is in
   the "Say" comment.
2. Frame 1: the FDD bullets became Smith's own sentences. The FDD bullet "One workman making a whole pin: perhaps
   twenty in a day, perhaps not one" misreads Smith, who wrote "could not each of them have made twenty, perhaps not
   one pin in a day"; that sentence, the eighteen operations and "Same people, same tools" are in the "Say" comment.
3. Plates: the FDD caption reads "Encyclopedie, 1762". The FDD picture (Wikimedia Commons, File:Defehrt epinglier
   pl2.jpg, 1248 by 958) is plate II, the one on the title frame here. The volume of plates used here was printed in
   1765: its title page reads "Troisieme livraison, 298 Planches" and "M. DCC. LXV", and its approval is dated
   17 October 1765. Plate I, the wire drawer, now illustrates Smith.
4. Frame 2: "replaces tax privilege with one tax on land" became "taxes land". "Land is measured in triangles,
   because angles are quick and chains are slow" became "Land is measured in triangles, computed with tables of
   logarithms": with the triangle frames left out, the tables have to appear here. The reason is in the "Say" comment.
5. Frame 3: the FDD boxes ("Choose the formulas and the blocks", "Per block, one exact value and its differences",
   "Add") became sentences: pages for blocks, "additions and subtractions" for "Add", as in Babbage and Roegel.
6. Frame 4: new. Only the facts the coordinating session pinned from the lecture deck; "up to" added before
   990 x 10^12, a peak rate.

## Sources of block 5

| Item | Source | Checked |
|---|---|---|
| French, frame 0 | Prony, *Notice sur les grandes tables logarithmiques et trigonométriques, adaptées au nouveau système métrique décimal*, read at the Académie royale des sciences on 7 June 1824 (Recueil des discours, Paris: Didot, 1824, pp. 33 to 42; also printed as pp. 1 to 12). Wording of the FDD deck, which cites "Notices, 1824, p. 5" | The 1824 print was not reached: Gallica answered with a Cloudflare challenge, HathiTrust with 403, the Google Books API with a quota error, and the Internet Archive full text search found nothing. C. J. D. Roberts' English translation, https://sites.google.com/site/babbagedifferenceengine/barondepronysdescriptionoftheconstructi , reads "to manufacture my logarithms as one manufactures pins". Peaucelle, *Le détail du calendrier de calcul des tables de Prony de 1791 à 1802* (2012), p. 21, https://locomat.loria.fr/cadastre/docs/peaucelle2012prony-calendrier.pdf , quotes "fabriquer les logarithmes comme on fabrique des épingles", citing Prony 1824, p. 35 |
| English, frame 0 | Ours, credited "English: lecturer" | |
| Smith, frame 1 | *An Inquiry into the Nature and Causes of the Wealth of Nations*, 1776, Book I, chapter I, "Of the Division of Labour". Project Gutenberg ebook 3300, https://www.gutenberg.org/cache/epub/3300/pg3300.txt | Matched word for word on 2026-11-10. The Gutenberg header does not name its edition; the 1776 print was not compared |
| Smith's dates | 1723 to 1790 | Not looked up |
| Frame 2 | Denis Roegel, *The great logarithmic and trigonometric tables of the French Cadastre: a preliminary investigation*, LOCOMAT, version of 11 January 2011, https://locomat.loria.fr/cadastre/analysis.pdf . Section 1.3: all taxes abolished by the law of 1 December 1790 and replaced by a single property tax; the cadastre of 1791; Prony director of the Bureau du cadastre from 5 October 1791; his report of 10 October 1791 on revising the triangles of the Cassini map; instruments converted to the decimal division of angles. Section 1.4: Carnot, Prieur and Brunet give Prony the task of new tables in 1793; the work at the Palais Bourbon, begun 1793, probably completed mid-1796 | Read 2026-11-10 |
| Frame 3 | Babbage, *On the Economy of Machinery and Manufactures*, 1832, section 244, Project Gutenberg ebook 4238: five or six mathematicians, seven or eight persons, "nothing more than simple addition and subtraction". Roegel 2011, section 1.4.1: the three groups, the second hands calculation sheets to the third, the computers "had only to perform additions and subtractions", their number "probably never greater than 20 or 25". Prony 1824 in Roberts' translation: sheets of 100 lines, the first line from the second group, 900 to 1000 additions or subtractions a day | Read 2026-11-10. The counts differ between Prony's own texts: four or five geometricians in 1824, five or six in 1801 (in Roegel) and in Babbage; sixty or eighty computers in 1801, seventy or eighty in 1824 |
| Frame 4 | Pinned by the coordinating session from `../clusters-deck/` and FDD `NUMBERS.md`: Alps, 2,688 nodes x 4 GH200 = 10,752; one GH200, 990 x 10^12 FLOP/s peak (NVIDIA datasheet); C = 6ND with N = 70 x 10^9 parameters and D = 15 x 10^12 training numbers | The two products recomputed |
| Plates, frames 0 and 1 | *Épinglier*, plates II and I, *Encyclopédie*, Recueil de planches, troisième livraison, Paris 1765, Smithsonian Libraries copy, Internet Archive item `RecueildeplanchIVDide`. Signatures read on the scan: "Goussier Del." and "Defehrt Sculp." (plate II), "Goussier Del." and "Prevost Sculp." (plate I) | Public domain (1765). The same scan is on Wikimedia Commons as a PDF, licence "Public domain" in the Commons API |
| Map, frame 2 | Maraldi and Cassini de Thury, *Nouvelle carte qui comprend les principaux triangles qui servent de fondement à la description géométrique de la France*, 1744, Bibliothèque nationale de France, btv1b53166738w; Wikimedia Commons, 11407 by 7325 | Commons API on 2026-11-10: "Public domain" |
| Photograph, frames 3 and 4 | Wikimedia Commons, File:Astronomer Edward Charles Pickering's Harvard computers.jpg, 1920 by 1502; a chart on the wall reads "Dec 1889" | Commons API on 2026-11-10: "Public domain". A later computing room: no picture of Prony's computers was looked for |

## Build of block 5

From this folder:

```bash
python3 -I make_images_block5.py /path/to/originals     # only to remake img/b5-*; the docstring has the URLs
../style/tools/build.sh block5-computing-clusters.tex
../style/tools/check.sh block5-computing-clusters.pdf
python3 tools/check_overlays_any.py block5-computing-clusters.pdf
python3 ../style/tools/make_handout.py block5-computing-clusters.pdf block5-computing-clusters-handout.pdf "Dividing a computation, 1793"
```

`build.sh` prints 10 pages, `log errors: 0` and no missing character. `check.sh` prints 0 em dashes, 0 en dashes,
CSCS as the only capitals, no build metadata, and Futura as the only font.

## History of block 5

1. 2026-11-10, first build, ported from FDD as above.
2. 2026-11-10, committed (`8417c6d`) and published on the course site at Carlos's instruction ("Once you are done,
   please publish them on the website"): AINIT-PAGE commit `a498851`, the Saturday 08:15 row and the Lecture slides
   list, as `ainit-hs26-computing-clusters-cold-intro.pdf` and `ainit-hs26-computing-clusters-cold-intro-handout.pdf`.
   After a rebuild, copy the PDF there again (`../clusters-deck/README.md`, section "On the course site", has the
   recipe).
3. 2026-11-11, the chips read "Computing clusters, cold intro" and "Handout", number 15 of weekend 2 that day
   (AINIT-PAGE `9e0be17`, numbers from the agenda).
4. 2026-11-11, Carlos: "computing clusters is now merged with parallelized matrix factorization, and it's going to be
   called large-scale computing", and "drop the handouts for all the cold intros". AINIT-PAGE `5ab848e`: this cold intro
   opens the Friday 16:00 row "Large-scale computing", chip "Large-scale computing, cold intro", number 14, without
   its handout. The deck itself is unchanged: its closing frame "Computing clusters" leads into the lecture deck of
   that name, the next item of the row.
5. 2026-11-12, Carlos, 2026-11-12: "always put the cold intro with the business on top at the beginning before the rest of the material ... make that for each block the first chip": since AINIT-PAGE `c01c44e` the deck is on the site only as the first part of
   `ainit-hs26-large-scale-computing-cold-intro-and-cases.pdf`, the chip "Large-scale computing", number 10 since AINIT-PAGE `c5283fe` (11 before), the first
   chip of the 16:00 row, with the case LinkedIn's ads after it (`../cold-intro-and-cases/`); the separate site file
   is gone. After a rebuild, merge it again.

## Open items of block 5

1. Prony's French: "mes logarithmes" (FDD, and Roberts' "my logarithms") or "les logarithmes" (Peaucelle). Settled
   only by the 1824 print.
2. The first tier: "five or six" (Prony 1801, Babbage 1832) on the slide; Prony 1824 writes "four or five".
3. The Harvard photograph stands for Prony's room; the credit names it.
4. Not tried on the projector of HG D 7.2.

# Block 3: Estimating chances from the past

Weekend 2, Friday 13 November 2026, 14:00, before the bandits (the game "Once Upon a Mirror"). Three drafts built on
2026-11-11 from Carlos's shortlist of round 5 of the candidates (`research_notes/Weekend 2 cold intros/estimate.md`,
C1, C2 and C8, folder `git_ainit/research_notes`, outside this repository): "The Fox and the Lion's Cave. It's very
good. Graunt's Bills is also very good. And then The Stupidest Man also. Please make three parallel cold intros".
Each takes the form of block 1 (his dictation of 2026-11-11): 8 frames, 16 pages. Frames 0, 6 and 7 are the same in
the three, apart from the subtitle, the picture and the third statement of frame 6. Carlos chose GRAUNT the same
evening; it is on the course site (section "On the course site of block 3"). THE FOX and BERNOULLI stay here as
unchosen drafts, off the course site.

## Files of block 3

| File | Content |
|---|---|
| `block3-bandits-fox.tex` | THE FOX (C1): Aesop, *The old lion and the fox*, Chambry 196 |
| `block3-bandits-graunt.tex` | GRAUNT (C2): John Graunt, *Natural and Political Observations ... upon the Bills of Mortality*, London, 1662 |
| `block3-bandits-bernoulli.tex` | BERNOULLI (C8): Jakob Bernoulli, *Ars Conjectandi*, Basel, 1713, part IV, chapter 4 |
| `make_images_block3_fox.py`, `make_images_block3_graunt.py`, `make_images_block3_bernoulli.py` | Cut and grade `img/b3f-*.jpg`, `img/b3g-*.jpg` and `img/b3b-*.jpg` (7 each) from the originals in their docstrings (URL, size, SHA-1, licence), byte for byte |
| `block3-bandits-<name>.pdf`, `block3-bandits-<name>-handout.pdf` | The decks, 16 pages each, and their handouts, 8 pages |

## Frames of block 3

Shared:

| Frame | Pages | Text |
|---|---|---|
| 0 | 1 | AI in Industry, weekend 2. Estimating chances from the past. A fable from ancient Greece; A book from London, 1662; A book from Basel, 1713 |
| 6 | 9 to 11 | Weekend 2. The estimate. One statement per click: We estimate the chance of an event from how often it happened before. For a product shown to a customer, the estimate (lavender) of a tap is the number of taps divided by the number of showings. The more showings, the closer the estimate tends to get to the true chance (BERNOULLI: This afternoon, every customer and product is an urn like Bernoulli's: an orange ball is a tap, a white ball no tap) |
| 7 | 12 to 16 | Weekend 2. Estimating chances today. Each option gets an estimate of its chance from the past, and the most promising is shown. One row per click: Spotify, mixes of music and podcasts for the home page; Amazon Payments, images and taglines for a page; Online shops, products for a customer; News sites, headlines for a story. Last: Such estimates decide much of what we are shown online. |

THE FOX (pictures: Gustave Dore, *Le Lion malade et le Renard*, Warsaw edition of 1876; Oudry and Chedel, the same
fable, 1755; Wenceslaus Hollar, *The sick lion*, in Ogilby's Aesop, 1668):

| Frame | Pages | Picture | Text |
|---|---|---|---|
| 0 | 1 | `b3f-title`: Dore, the animals at the cave | as above |
| 1 | 2, 3 | `b3f-bg-cave`: Oudry, the lion among the bones | The lion's cave. Ancient Greece, a fable of Aesop. An old lion can no longer hunt. He lies down in his cave and lets it be known that he is ill. The animals come to visit him, one after another. On the click: The fox cannot see inside the cave. How can she tell what happens to the visitors? |
| 2 | 4 | `b3f-bg-distance`: Hollar, the fox outside the cave | καὶ στᾶσα ἄποθεν τοῦ σπηλαίου ἐπυνθάνετο αὐτοῦ πῶς ἔχοι. She stood at a distance from the cave and asked him how he was. The Greek in Palatino |
| 3 | 5 | `b3f-half-lion`, left half: Hollar, the lion | The lion, too old to hunt. "Badly," he said, and he asked her why she did not come in. |
| 4 | 6 | `b3f-half-fox`, right half: Oudry, the fox and the tracks | The fox, at a distance from the cave. "But I would have come in, if I did not see the tracks of many going in, and of none coming out." From "if" in lavender |
| 5 | 7, 8 | `b3f-bg-inside`: Dore, the lion in the cave | "So sensible people foresee dangers from the evidence and escape them." The middle in lavender. On the click: The fox cannot see inside the cave. She counts what happened before: many went in, none came out. From the past, she estimates her own chance of coming out. |
| 6, 7 | 9 to 16 | `b3f-bg-close`: Dore, blurred and dark | as above |

GRAUNT (pictures: Claude de Jongh, *View of London Bridge*, 1632; the weekly bill of 5 to 12 September 1665; the first
edition of 1662, its folded Table of Casualties, its title page and its page 17):

| Frame | Pages | Picture | Text |
|---|---|---|---|
| 0 | 1 | `b3g-title`: de Jongh, the bridge | as above |
| 1 | 2, 3 | `b3g-bill`: "The Diseases and Casualties this Week", 1665 | The Bills of Mortality. London, seventeenth century. Every week, the parish clerks of London print the burials of the week and what each person died of. Londoners read these bills in fear of the plague and of many other diseases. On the click: How afraid should a Londoner be of each disease? |
| 2 | 4 | `b3g-table`: the Table of Casualties, 1662 | I shall onely set down how many died of each. John Graunt, a haberdasher of London, 1662 |
| 3 | 5 | `b3g-half-title`, left half: the title page, 1662 | John Graunt, 1620 to 1674, haberdasher. "Now having (I know not by what accident) engaged my thoughts upon the Bills of Mortality, and so far succeeded therein, as to have reduced several great confused Volumes into a few perspicuous Tables..." The tables in lavender |
| 4 | 6 | `b3g-half-counts`, right half: page 17, the two tables | Of 229250 deaths, twenty years of bills: Drowned 829, Sodainly 454, Grief 279, Lunatique 158, Murthered 86, Head-Ach 51, Frighted 22, Excessive drinking 2. "That not one in two thousand are Murthered in London." in lavender |
| 5 | 7, 8 | `b3g-bridge`: de Jongh, the houses on the bridge | "Whereas many persons live in great fear, and apprehension of some of the more formidable, and notorious diseases... I shall onely set down how many died of each: that the respective numbers, being compared with the Total 229250, those persons may the better understand the hazard they are in." The last clause in lavender. On the click: Graunt divides each count by all the deaths. From the past, every Londoner can estimate the hazard of each disease. |
| 6, 7 | 9 to 16 | `b3g-bg-close`: de Jongh, blurred and dark | as above |

BERNOULLI (pictures: Emanuel Buechel, *Prospect des Grossen Muensters und Rheinbruecke zu Basel*, etching, 1761; the
portrait of Jakob Bernoulli by his brother Niklaus, 1687; the title page and page 226 of the book, 1713):

| Frame | Pages | Picture | Text |
|---|---|---|---|
| 0 | 1 | `b3b-title`: Buechel, the Minster above the Rhine | as above |
| 1 | 2, 3 | `b3b-bg-towers`: Buechel, the Minster's towers | A professor in Basel. Switzerland, around 1690. Jakob Bernoulli teaches mathematics in Basel. The chances of a die can be counted before the throw: one face in six. But nobody can count in advance the chance that a man dies within ten years, or that it rains tomorrow. On the click: How could anyone know such a chance? |
| 2 | 4 | `b3b-bg-bridge`: Buechel, the Rhine bridge | Quod a priori elicere non datur, saltem a posteriori ... eruere licebit. What we cannot find out beforehand, we may at least find out afterwards. |
| 3 | 5 | `b3b-half-portrait`, left half: the portrait | Jakob Bernoulli, 1655 to 1705. "Suppose that of three hundred men of the age and constitution of Titius, two hundred died within ten years. Then you can conclude, safely enough, that there are twice as many cases in which Titius pays his debt to nature within ten years as cases in which he lives longer." From "there are" in lavender |
| 4 | 6 | `b3b-half-titlepage`, right half: the title page | Ars Conjectandi, The Art of Conjecturing, 1713. "One or two experiments are not enough; a great number is needed. Even the most stupid person, by some instinct of nature, on his own and without any instruction (which is truly astonishing), knows that the more observations are taken, the smaller the danger of missing the mark." The last clause in lavender |
| 5 | 7, 8 | `b3b-bg-urn`: page 226, which prints the urn | "Suppose that, without your knowledge, three thousand white pebbles and two thousand black ones are hidden in an urn. You draw one pebble after another, putting each back, and observe how often a white one and how often a black one comes out." From "observe" in lavender. On the click: After many draws, black comes out about two times in five. Everyone knows it by instinct; Bernoulli spent twenty years on the proof. |
| 6, 7 | 9 to 16 | `b3b-bg-close`: Buechel, blurred and dark | as above |

Words per frame without the credits (pdftotext, glyph boxes taller than 8.5 pt): THE FOX 13, 56, 23, 19, 30, 40, 54,
62; GRAUNT 13, 49, 17, 40, 34, 69, 54, 62; BERNOULLI 13, 55, 25, 55, 55, 66, 62, 62. A script of each building agent
compared every quotation and statement with the brief, letter for letter.

## Sources of block 3

| Item | Source | Checked |
|---|---|---|
| THE FOX, Greek | Aesop, Λέων γηράσας καὶ ἀλώπηξ, Chambry 196 (Perry 142), el.wikisource, from Chambry's edition | Matched on 2026-11-11 (`estimate.md`, C1). The English is ours, credited "English: lecturer" |
| THE FOX, "Say" of frame 5 | Horace, *Epistles* I.1, 73 to 75 (The Latin Library); La Fontaine, *Fables* VI.14 (fr.wikisource, edition of 1874) | Matched on 2026-11-11 (`estimate.md`, C1) |
| GRAUNT, every quotation and count | Ed Stephan's transcription: http://www.edstephan.org/Graunt/0.html (the dedication), 00.html (the index), 2.html (chapter 2), 3.html (chapter 3) | Matched by script on 2026-11-11. The line of frame 4 is entry 13 of the book's index: "That not one in two thousand are Murthered in London, with the Reasons thereof, p. 21" |
| GRAUNT, the tables of the book | The folded Table of Casualties prints 827 drowned and 21 frighted; chapter 2 and page 17 print 829 and 22. The slides follow chapter 2 and page 17; the crop of frame 2 leaves out those rows | Seen on the scans on 2026-11-11 |
| BERNOULLI, Latin | *Ars Conjectandi*, 1713, part IV, chapter 4, Internet Archive `jacobibernoulli00bern`, its OCR cleaned by hand | Matched on 2026-11-11 (`estimate.md`, C8). The English is ours; Sung's English (1966) is protected and stays out |
| BERNOULLI, German | Haussner's translation (Ostwalds Klassiker 107 and 108, 1899): the urn and the twenty years | Read on 2026-11-11 |
| Frame 6 | The game, `w2-cx-private/03_bandits/03_mirror_game.html`: the estimate is taps / showings; "The more dots, the closer it tends to get to p"; "Cinderella's urn for the mattress: 2 orange balls and 3 white balls", the 2 to 3 of Bernoulli's urn | Read on 2026-11-11 |
| Frame 7 | The two cases of this block, `../cases-deck/block3-bandits.tex`: Spotify's home page (Feijer and others, CONSEQUENCES workshop at RecSys 2025) and Amazon Payments (John and Gozluklu, AWS Machine Learning Blog, 2026). Online shops and news sites name no company. No numbers on the frame | |
| Pictures | The docstrings of the three `make_images_block3_*.py` | Commons API or Internet Archive metadata, 2026-11-11: public domain, every artist dead before 1956 |

## Build of block 3

From this folder, for each of `fox`, `graunt` and `bernoulli`:

```bash
python3 -I make_images_block3_fox.py /path/to/originals     # only to remake img/b3f-*; the docstring has the URLs
../style/tools/build.sh block3-bandits-fox.tex
python3 tools/check_overlays_any.py block3-bandits-fox.pdf
python3 ../style/tools/make_handout.py block3-bandits-fox.pdf block3-bandits-fox-handout.pdf "Estimating chances from the past"
```

`build.sh` prints `log errors: 0` and no missing character for the three. The fox sets its Greek in Palatino.

## On the course site of block 3

GRAUNT since 2026-11-11 (AINIT-PAGE commit `9e509ca`), on the Friday 14:00 row before the Mirror, chips "Bandits,
cold intro" and "Handout", number 11 of weekend 2 that day; the Mirror and every item after it moved up by one
(the Saturday cold intro to 16, computing clusters to 17).

| Site file | Source here |
|---|---|
| `ainit-hs26-bandits-cold-intro.pdf` (until 2026-11-12) | `block3-bandits-graunt.pdf` |
| `ainit-hs26-bandits-cold-intro-and-cases.pdf` (since 2026-11-12) | `../cold-intro-and-cases/block3-bandits.pdf`: GRAUNT, then the cases Spotify's home page and Amazon Payments |

Since AINIT-PAGE `c01c44e` (2026-11-12) GRAUNT is on the site only as the first part of the chip "Bandits", number 08 since AINIT-PAGE `c5283fe` (09 before),
the first chip of the 14:00 row; after a rebuild, merge it again (`../cold-intro-and-cases/`).

The handout, `ainit-hs26-bandits-cold-intro-handout.pdf`, is off the site since AINIT-PAGE `5ab848e` (2026-11-11).
The recipe after a rebuild is the one of block 1 (section "On the course site"): copy the PDF over the same site file
name, `npm ci && npm run build` in `AINIT-PAGE`, push to `main`, curl the live file and `cmp` it with this one.

## History of block 3

1. 2026-11-11, round 5 of the candidates, `estimate.md`, 9 stories in which a chance is estimated from past counts.
2. The same evening Carlos shortlisted C1, C2 and C8 and asked for three parallel cold intros. Three agents built
   them at the same time from one brief with the texts; after the review, line breaks moved to the ends of
   sentences (commit `5bb67bd`).
3. 2026-11-11, asked which draft goes on the course site, Carlos answered "Graunt": published at AINIT-PAGE commit
   `9e509ca`, section "On the course site of block 3" above. The deck keeps its file name.

## Open items of block 3

1. Not tried on the projector of HG D 7.2.
2. THE FOX and BERNOULLI are unchosen drafts; a push keeps their PDFs public on the Pages of this repository.
