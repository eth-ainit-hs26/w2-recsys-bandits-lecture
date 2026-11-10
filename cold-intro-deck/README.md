# Cold intro of weekend 2: Birds with the same wings

Weekend 2, Friday 13 November 2026, 08:15, before the inner product and nearest neighbors. Chunyu Kun at the
court of King Xuan of Qi, *Zhanguo ce*, Qi 3. Chosen by Carlos on 2026-11-10 from round 4 of the candidates,
`research_notes/Weekend 2 cold intros/lookalikes.md`, L5 (folder `git_ainit/research_notes`, outside this
repository). The same day he dictated the frames: the title frame of the first build, a context frame, the king's
question and Kun's answer in his English (one paragraph each, Kun's stopping at "by the cartful", the birds and the
beasts highlighted), and a closing frame on representation learning. Look: the Title sequence of the course cold
intro, `w1-lecture-material/cold-intro/intro-slides/`.

## Files

| File | Content |
|---|---|
| `block1-nearest-neighbors.tex` | The deck: 5 frames, 8 pages, a "Say" comment per frame |
| `cold-intro-kit.tex` | The macros: full page picture, half page picture, text, credit, mapping row (unused since the rebuild) |
| `make_images.py` | Cuts and grades `img/` from the original painting; reproduces `img/` byte for byte |
| `img/` | `bg-title.jpg`, `bg-pair.jpg`, `half-court.jpg`, `half-flock.jpg`, `bg-map.jpg` |
| `tools/check_overlays_any.py` | The no-jump check for dark pages, copied from w1-lecture-material |
| `block1-nearest-neighbors.pdf` | The deck |
| `block1-nearest-neighbors-handout.pdf` | The last click of each frame, 5 pages |

## Frames

| Frame | Pages | Picture | Text |
|---|---|---|---|
| 0 | 1 | `bg-title`: the whole painting | The state of Qi, fourth century BC. 淳于髡一日而見七人於宣王。 In one day, Chunyu Kun presented seven men to King Xuan. |
| 1 | 2 | `bg-pair`: the two cranes on the ridge ends | Strategies of the Warring States. *Zhanguo ce* 戰國策, edited by Liu Xiang in the 1st century BC. Stories of the politics and wars of the Chinese states, 5th to 3rd century BC. King Xuan of Qi gathered hundreds of scholars in his capital. One of them, Chunyu Kun, known for his wit, presented new scholars to the king. |
| 2 | 3 | `half-court`, left half: the palace roof, the crane on its left ridge end | King Xuan of Qi, reigned 319 to 301 BC. "Come. I have heard ... are scholars not plentiful, then?" |
| 3 | 4 | `half-flock`, right half: the flock, the crane on the right ridge end | Chunyu Kun, c. 386 to 310 BC. "Not so. Birds with the same wings ... you load them by the cartful." The birds and the beasts sentence in lavender |
| 4 | 5 to 8 | `bg-map`: the flock, blurred and dark | Weekend 2. Representation learning. Four statements, one per click: similar data points cluster together; each data point gets a representation, its embedding, a list of numbers with its most characteristic features; data points that belong together get similar embeddings; embeddings are one of the main drivers of AI today |

English words per page without the credits: 20, 60, 55, 55, 57. The two quotations are Carlos's text of
2026-11-10, which is the gloss of `lookalikes.md`; a script compared them with the PDF, letter for letter.

## Sources

| Item | Source | Checked |
|---|---|---|
| Chinese text, frame 0 | 戰國策, 齊策三, zh.wikisource 戰國策/卷10, https://zh.wikisource.org/wiki/戰國策/卷10, notes in angle brackets removed | A substring of the quotation in `lookalikes.md`, which was matched against that page on 2026-11-09 |
| English | Ours, credited "English: lecturer": the gloss of `lookalikes.md`, chosen by Carlos | Scholars for 士; the mountain names 睪黍 and 梁父 left in Chinese, as in the gloss |
| The book, frame 1 | en.wikipedia, Zhan Guo Ce: anecdotes of political manipulation and warfare in the Warring States period, 5th to 3rd centuries BC (490 to 221 BC); edited by Liu Xiang from manuscripts of the imperial library. en.wikipedia, Liu Xiang (scholar): 77 to 6 BC, edited the Zhanguoce | Read 2026-11-10 |
| King Xuan's scholars, frame 1 | Shiji 46 (史記, 田敬仲完世家), zh.wikisource 史記/卷046: 宣王喜文學游說之士，自如騶衍、淳于髡 ... 七十六人，皆賜列第，為上大夫，不治而議論。是以齊稷下學士復盛，且數百千人。 | Read 2026-11-10 |
| Chunyu Kun, frames 1 and 3 | en.wikipedia, Chunyu Kun: a wit, sent several times as an envoy, "able to present scholars for promotion and introduce foreign advisers to the king". zh.wikipedia 淳于髡: c. 386 to 310 BC | Read 2026-11-10 |
| King Xuan of Qi, frame 2 | en.wikipedia, King Xuan of Qi: king of Qi from 319 to 301 BC | Read 2026-11-10 |
| "Say" lines | en.wikipedia, Li (unit): a traditional Chinese unit of distance. en.wikipedia, Bupleurum chinense (柴胡) and Platycodon (桔梗): roots used in traditional Chinese medicine | Read 2026-11-10 |
| Frame 4 | Carlos's words of 2026-11-10, condensed | |
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
python3 ../style/tools/make_handout.py block1-nearest-neighbors.pdf block1-nearest-neighbors-handout.pdf "Birds with the same wings"
```

`build.sh` prints `log errors: 0` and no missing character. `check.sh` lists Futura and Songti TC as the fonts.

## History

1. 2026-11-10, first build (commit `0beb06a`): the Chinese with our English under it on every frame, and a last
   frame that mapped the story's words to the block (birds to customers, the same wings to similar ratings).
2. 2026-11-10, rebuild to Carlos's dictated frames: the context frame, the two quotations in English only, the
   closing frame on representation learning; the mapping is gone.

## Open items

1. Not tried on the projector of HG D 7.2.
2. Not on the course site. Publishing there waits for Carlos.
3. The deck writes "neighbor", as the agenda does; the Video Store game writes "neighbour".
