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
| `ainit-hs26-nearest-neighbors-cold-intro.pdf` | `block1-nearest-neighbors.pdf` |
| `ainit-hs26-nearest-neighbors-cold-intro-handout.pdf` | `block1-nearest-neighbors-handout.pdf` |

A live file is https://eth-ainit-hs26.github.io/AINIT-PAGE/slides/we2/<file>
After a rebuild, copy both over the same site file names, run `npm ci && npm run build` in `AINIT-PAGE`, push to
`main`, then curl the live files and `cmp` them with the ones here. Since AINIT-PAGE commit `8bf143b` the weekend 2
ZIP, `ainit-hs26-weekend-2.zip`, holds both, numbered as on the page; `npm run build` remakes it from the files in
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
   After a rebuild, copy both there again (`../clusters-deck/README.md`, section "On the course site", has the recipe).
3. 2026-11-11, the chips read "Computing clusters, cold intro" and "Handout", number 15 of weekend 2 that day
   (AINIT-PAGE `9e0be17`, numbers from the agenda).

## Open items of block 5

1. Prony's French: "mes logarithmes" (FDD, and Roberts' "my logarithms") or "les logarithmes" (Peaucelle). Settled
   only by the 1824 print.
2. The first tier: "five or six" (Prony 1801, Babbage 1832) on the slide; Prony 1824 writes "four or five".
3. The Harvard photograph stands for Prony's room; the credit names it.
4. Not tried on the projector of HG D 7.2.
