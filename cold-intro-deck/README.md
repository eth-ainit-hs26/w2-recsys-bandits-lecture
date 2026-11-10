# Cold intro of block 1: Birds with the same wings

Weekend 2, Friday 13 November 2026, 08:15, before the inner product and nearest neighbors. Chunyu Kun at the
court of King Xuan of Qi, *Zhanguo ce*, Qi 3. Chosen by Carlos on 2026-11-10 from round 4 of the candidates,
`research_notes/Weekend 2 cold intros/lookalikes.md`, L5 (folder `git_ainit/research_notes`, outside this
repository). Look: the Title sequence of the course cold intro, `w1-lecture-material/cold-intro/intro-slides/`.

## Files

| File | Content |
|---|---|
| `block1-nearest-neighbors.tex` | The deck: 5 frames, 10 pages, a "Say" comment per frame |
| `cold-intro-kit.tex` | The macros: full page picture, half page picture, text, credit, mapping row |
| `make_images.py` | Cuts and grades `img/` from the original painting; reproduces `img/` byte for byte |
| `img/` | `bg-title.jpg`, `half-court.jpg`, `half-flock.jpg`, `bg-pair.jpg`, `bg-map.jpg` |
| `tools/check_overlays_any.py` | The no-jump check for dark pages, copied from w1-lecture-material |
| `block1-nearest-neighbors.pdf` | The deck |
| `block1-nearest-neighbors-handout.pdf` | The last click of each frame, 5 pages |

## Frames

| Frame | Pages | Picture | Text |
|---|---|---|---|
| 0 | 1 | `bg-title`: the whole painting | The state of Qi, fourth century BC. 淳于髡一日而見七人於宣王。 In one day, Chunyu Kun presented seven men to King Xuan. |
| 1 | 2 | `half-court`, left half: the palace roof, the crane on its left ridge end | King Xuan of Qi, reigned 319 to 301 BC. The king's question, 4 lines, and its English |
| 2 | 3, 4 | `half-flock`, right half: the flock, the crane on the right ridge end | Chunyu Kun, c. 386 to 310 BC. 不然。 夫鳥同翼者而聚居，Birds with the same wings live together. Click: 獸同足者而俱行。 Beasts with the same feet walk together. |
| 3 | 5, 6 | `bg-pair`: the two cranes on the ridge ends | 夫物各有疇 to 而取火於燧也, and its English. Click: 髡將復見之，豈特七士也。 I will present more. Why only seven scholars? |
| 4 | 7 to 10 | `bg-map`: the flock, blurred and dark | Weekend 2, block 1. The inner product and nearest neighbors. The mapping, one row per click |

Most English words on a page: 47 (frame 4). The herbs of the passage (chaihu and jiegeng, never in a marsh, by the
cartful on two mountains) are in the "Say" line of frame 2 only.

## Mapping, frame 4

| Story | English | Block |
|---|---|---|
| 鳥 | birds | Customers |
| 同翼 | the same wings | Similar ratings, measured by the inner product |
| 聚居 | live together | Nearest neighbors |
| 求士於髡 | seeking scholars from Kun | A prediction: copy the nearest neighbor's rating |

## Sources

| Item | Source | Checked |
|---|---|---|
| Chinese text | 戰國策, 齊策三, zh.wikisource 戰國策/卷10, https://zh.wikisource.org/wiki/戰國策/卷10, notes in angle brackets removed | The 15 fragments on the slides are substrings of the quotation in `lookalikes.md`, which was matched against that page on 2026-11-09 |
| English | Ours, credited "English: lecturer" | Scholars for 士, the worthy for 賢者, fire-drill for 燧, as in the gloss of `lookalikes.md` |
| Painting | Emperor Huizong of Song, *Auspicious Cranes* (瑞鶴圖), 1112, Liaoning Provincial Museum. Wikimedia Commons, File:Songhuizong5.jpg | Commons API on 2026-11-10: 9079 by 1846, artist Emperor Huizong of Song, date 1112, licence "Public domain" |
| Painting, facts in "Say" | zh.wikipedia 瑞鶴圖: 20 red-crowned cranes flying and standing over the Xuande Gate of Bianliang; the 16th day of the first month of Zhenghe 2, 22 February 1112 in the Gregorian calendar | Read 2026-11-10 |
| King Xuan of Qi | en.wikipedia, King Xuan of Qi: king of Qi from 319 to 301 BC | Read 2026-11-10 |
| Chunyu Kun | zh.wikipedia 淳于髡: c. 386 to 310 BC, of Qi, of the Jixia school, known for wit and debate, often an envoy of Qi | Read 2026-11-10 |
| Not verified | The medium of the painting | Not stated on the slides |

## Build

From this folder:

```bash
python3 -I make_images.py /path/to/Songhuizong5.jpg     # only to remake img/; the docstring has the URL
../style/tools/build.sh block1-nearest-neighbors.tex
../style/tools/check.sh block1-nearest-neighbors.pdf
python3 tools/check_overlays_any.py block1-nearest-neighbors.pdf
python3 ../style/tools/make_handout.py block1-nearest-neighbors.pdf block1-nearest-neighbors-handout.pdf "Birds with the same wings"
```

`build.sh` prints `log errors: 0` and no missing character. `check.sh` lists Futura and Songti TC as the fonts.

## Open items

1. Not tried on the projector of HG D 7.2.
2. Not on the course site. Publishing there waits for Carlos.
3. The deck writes "neighbor", as the agenda does; the Video Store game writes "neighbour".
