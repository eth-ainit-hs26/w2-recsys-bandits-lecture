# The weekend 2 opener: why understanding customers pays

Six slides that open weekend 2 of AI in Industry, HS26 (13 and 14 November 2026), for an audience of
managers. They show why recommendation, advertising and customer profiles matter, before the weekend's
games and lectures on recommender systems and bandits. Built on 2026-11-03 at Carlos's request ("Build
it in 6 slides, please"), from the opener ideas in his research notes, in the Codex plates style.

- `opener.pdf`: the deck, 6 frames over 21 pages (the clicks).
- `opener-handout.pdf`: one page per frame, its last click.

## The six frames

| # | Title | Clicks | What it shows |
|---|---|---|---|
| 1 | Three companies, 1.5 billion dollars of ads a day | 3 | Advertising revenue in 2025: Google 294.7, Meta 196.2, Amazon 68.6 billion dollars; together 559.5 billion, about 1.5 billion a day. Each ad is a guess about one person |
| 2 | A machine suggested much of what we watch and buy | 4 | A question to the room (what share of your YouTube hours did you go looking for?), then YouTube over 70% of watch time, Netflix 75% of viewing, Amazon 35% of purchases |
| 3 | The question to ask: compared to what? | 3 | The 35% share counts purchases that would have happened anyway. A randomized experiment: 11% more sales of a product and its recommended substitutes. Published field tests more often report 1% to 5% more revenue |
| 4 | Six customers, two calls: whom do you call? | 4 | Invented. Called by risk, the calls change nothing for Lea and remind Marco to cancel; called by response, Nina and Jonas stay |
| 5 | Call the customers the offer can move | 3 | Ascarza: aiming the offer at the customers it moves gave 4.1 to 8.7 percentage points less churn than aiming by risk; aiming by risk sometimes raised churn |
| 6 | What the shopkeeper knew, a machine must learn | 4 | The village shopkeeper knows every regular; with millions of loyalty cards a machine places customers as points, and a new customer is read from the neighbours. The hand-over to the weekend |

The talk track is the `% Say:` comment above each frame in `opener.tex`. Frame 6 hands over to the
video store game ("Once Upon a Video Store", in `w2-cx-private`, folder `01_nearest_neighbours/`).

## Build and checks

Run from this folder:

```bash
python3 tools/opener_numbers.py
../style/tools/build.sh opener.tex
../style/tools/check.sh opener.pdf
python3 ../style/tools/check_overlays.py opener.pdf
python3 tools/check_numbers.py opener.pdf
python3 ../style/tools/make_handout.py opener.pdf opener-handout.pdf
```

No number is typed into `opener.tex`. `tools/opener_numbers.py` holds every number next to the
sentence of its source, asserts the arithmetic (the rounded values, the total, the daily figure, the
bar lengths) and the conclusions of the invented table (calling by risk picks Lea and Marco and raises
the chance of leaving, calling by response picks Nina and Jonas and lowers it), and writes
`numbers.tex` and `tools/expected.txt`. `tools/check_numbers.py` reads the 25 expected strings back
from the rendered PDF.

State of the build of 2026-11-03: 21 pages, 0 log errors, 0 em and en dashes, no build metadata, no
element that moves between clicks, all 25 numbers found in the PDF. Every frame was rendered and read
at full size.

## Sources

Grades as in the research notes: READ (the primary page was read), REVIEW (quoted by a published
review), SECONDARY (a press report or an excerpt of the primary document). The three revenues of
frame 1 were read in the primary documents by the second reader on 2026-11-03.

| Frame | Claim | Source | Grade |
|---|---|---|---|
| 1 | Google advertising 294,691 million USD in 2025 | Alphabet Form 10-K for 2025, https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm | READ |
| 1 | Meta advertising 196,175 million USD in 2025 | Meta Form 10-K for 2025, https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm | READ |
| 1 | Amazon advertising services 68,635 million USD in 2025, the sum of 13,921, 15,694, 17,703 and 21,317 | Amazon, fourth quarter 2025 results, 5 February 2026, https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Fourth-Quarter-Results/default.aspx ; Marketing Dive says it "surpassed $68 billion", https://www.marketingdive.com/news/amazon-annual-ad-revenue-passes-68b-boosted-by-full-funnel-strategy/811569/ | READ |
| 2 | YouTube: more than 70% of watch time from recommendations | CNET, 10 January 2018, Neal Mohan at CES, https://www.cnet.com/tech/services-and-software/youtube-ces-2018-neal-mohan/ | READ |
| 2 | Netflix: "75 % of what people watch is from some sort of recommendation" | Netflix Tech Blog, Amatriain and Basilico, 2012, as quoted by Jannach and Jugovac (below) | REVIEW |
| 2, 3 | Amazon: 35% of purchases | McKinsey, "How retailers can keep up with consumers", 1 October 2013, https://www.mckinsey.com/industries/retail/our-insights/how-retailers-can-keep-up-with-consumers . McKinsey names no source; Jannach and Jugovac trace it to "a statement of Amazon's CEO in 2006" | READ |
| 3 | 11% gain in total sales of a product and its recommended substitutes, randomized experiment | Kumar and Hosanagar, Information Systems Research 30(3), 2019, abstract: https://ideas.repec.org/a/inm/orisre/v30y2019i3p819-838.html | READ |
| 3 | Revenue increases "more often reported to lie between one and five percent" | Jannach and Jugovac, ACM TMIS 10(4), 2019, https://arxiv.org/html/1908.08328v3 | READ (arXiv version) |
| 5 | Two field experiments; targeting by sensitivity to the intervention is "significantly more effective" than targeting by risk | Ascarza, Journal of Marketing Research 55(1), 80 to 98, 2018, DOI 10.1509/jmr.16.0163, the published abstract as served by Crossref | READ (abstract only) |
| 5 | 4.1 to 8.7 percentage points less churn; "in some instances" targeting by risk increased churn; the telecom firm in the Middle East | The award committee's statement, AMA press release, 3 April 2023, https://www.ama.org/press-releases/eva-ascarza-receives-2023-weitz-winer-odell-award-for-retention-futility/ | READ |
| 5 | The comparison comes from simulations on both datasets | AMA, 24 April 2019, https://www.ama.org/2019/04/24/escarzas-retention-futility-targeting-high-risk-customers-might-be-ineffective-wins-2018-award/ | READ |
| 6 | Migros Cumulus and Coop Supercard, named as examples only | no figure on the slide | |

The body of Ascarza's paper was not read: the journal's site refused automated reading, and no open
copy turned up. Its abstract gives no number. The 4.1 to 8.7 points therefore come from the AMA's
award summary, whose sentence is garbled as printed ("reduced churn rates 4.1 to by 8.7 percentage
points"), and the slide's source line says so. An earlier talk abstract of hers, on a seminar page of
the Universidad de Chile (https://www.dii.uchile.cl/eventos/ciclo-seminarios-cea-mipp-13/), says "a
further reduction of up to seven percentage points in churn rate" instead.

## Choices made without asking

1. **The order**, from the recommendation in the notes: the money, how much a machine chooses,
   compared to what, a toy, the field studies behind the toy, the hand-over.
2. **No title page.** The opener comes after the weekend's own title, so frame 1 starts with the money.
3. **Netflix 75% from the 2012 blog**, kept with its year. The often quoted "80% of hours streamed"
   was left out because its wording could not be read in the source.
4. **YouTube "over 70%"** is drawn as a 70% bar and labelled "over 70%".
5. **The question on frame 2** comes before the bars, so the room guesses first.
6. **Frame 4 is invented and says so** ("Invented customers"). Its numbers were chosen to show the
   point in two calls: a call changes nothing for Lea (80% either way), raises Marco's chance of
   leaving (70% to 75%), and lowers Nina's (50% to 30%) and Jonas's (40% to 25%).
7. **Frame 5 keeps the number 4.1 to 8.7 and credits it to the AMA's summary**, with the hedge that
   the comparison was simulated on the field data. "Two field experiments" is the abstract's wording.
8. **Frame 6 names Migros Cumulus and Coop Supercard** as examples of loyalty cards without their
   member counts, which only a press report gives (Blick, 2025). Its points are invented and say so.
9. **The deck lives in this public repository**, next to the weekend 2 lecture, and copies the style
   into `../style/`. A push publishes it on GitHub Pages; nothing links to it yet.

## Simplifications to know when presenting

- Frame 3, "more sales", means the total sales of the product and of its recommended substitutes. The
  experiment also found that a product's own sales fell 1.9% while its substitutes gained 9%.
- The 70% and the 75% are the companies' own statements (2018 and 2012). The 35% is McKinsey's (2013),
  and McKinsey names no source. None comes with a method. The Say comment of frame 2 says so.
- Frame 3's 11% is an average: the effect varied across products.
- Frame 1 compares annual totals: Google's line is "Google advertising" (search, YouTube ads and the
  network), Amazon's is "advertising services".
- The "Change" column of frame 4 is in percentage points.

## Open items

1. The deck is linked from nowhere: neither `../index.html` nor the course site has it.
2. It has not been projected in HG D 7.2. The hatching and the hairlines fade first on a weak projector.
3. Read Ascarza's paper (Journal of Marketing Research 55(1), 80 to 98, DOI 10.1509/jmr.16.0163)
   through the ETH library, to confirm the 4.1 and the 8.7 in its own tables, and then credit the paper
   alone on frame 5.

## Second read

A second reader (a separate agent that saw only the deck, the generator, the notes and the sources)
checked every claim on the slides and in the Say comments on 2026-11-03 and found no wrong number.
It read the two 10-K filings, Amazon's results for the fourth quarter, the RePEc abstract of Kumar
and Hosanagar, the arXiv version of Jannach and Jugovac, and the two AMA releases; CNET, the Netflix
blog and McKinsey refused it, so those three were checked against the quotes in the research notes.
Fixed after its report, on the same day:

- Amazon's revenue now comes from its own quarterly results (68,635 million, unchanged on the slide),
  in place of the press report.
- Frame 1's Say: "Many of those guesses draw on a profile", in place of "every one".
- Frame 2's Say: the 35% is McKinsey's, which names no source.
- Frame 3: "on average" added to the experiment's measure; its Say no longer applies the 1% to 5%
  to the advertising revenue of frame 1.
- Frame 4: the call makes Marco "more likely to cancel" (70% to 75%), on the slide and in the Say.
- Frame 5: "two field experiments" (the abstract), the 4.1 to 8.7 credited to the AMA's summary on
  the slide, and a note for the lecturer under the Say in `opener.tex`; the Say follows the AMA's
  description of the two studies.
