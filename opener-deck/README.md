# The weekend 2 opener: why understanding customers pays

Six slides that open weekend 2 of AI in Industry, HS26 (13 and 14 November 2026), for an audience of
managers. They show why recommendation, advertising and customer profiles matter, before the weekend's
games and lectures on recommender systems and bandits. Built on 2026-11-03 at Carlos's request ("Build
it in 6 slides, please"), from the opener ideas in his research notes, in the Codex plates style.

The same day he asked for frames 4 to 6 to be redone like frames 1 to 3: "I want statistics, concrete
hard numbers measured", recent ones preferred. They now carry three measurements published in
October 2026 (Meta, Amazon, Nubank). The first frames 4 to 6 (an invented table of six customers,
Ascarza's retention study of 2018, a village shopkeeper) are in git history at commit `b165aeb`.

- `opener.pdf`: the deck, 6 frames over 20 pages (the clicks).
- `opener-handout.pdf`: one page per frame, its last click.

## The six frames

| # | Title | Clicks | What it shows |
|---|---|---|---|
| 1 | Three companies, 1.5 billion dollars of ads a day | 3 | Advertising revenue in 2025: Google 294.7, Meta 196.2, Amazon 68.6 billion dollars; together 559.5 billion, about 1.5 billion a day. Each ad is a guess about one person |
| 2 | A machine suggested much of what we watch and buy | 4 | A question to the room (what share of your YouTube hours did you go looking for?), then YouTube over 70% of watch time, Netflix 75% of viewing, Amazon 35% of purchases |
| 3 | The question to ask: compared to what? | 3 | The 35% share counts purchases that would have happened anyway. A randomized experiment: 11% more sales of a product and its recommended substitutes. Published field tests more often report 1% to 5% more revenue |
| 4 | What a better model added at Meta in 2026 | 3 | July to September 2026, more conversions after one change to a model: ads for apps +9.6%, Facebook Feed ads nearly +2%, ads for websites +1.7%, Facebook ads +1.4%. The price per ad rose 14% in a year, which Meta puts down to better ad performance and a better economy |
| 5 | 400 million customers used a shopping assistant | 3 | Alexa for Shopping: over 400 million users in 12 months, interactions +570% in a year. US users spend 50% more per order than non-users. Compared to what? The users chose the assistant themselves |
| 6 | A profile learned from 100 billion transactions | 4 | Nubank adds a profile learned from raw transactions to its models: income +7.54%, spending +6.85%, lending risk +2.23%, credit default +1.25% (in use for over 100 million customers, a typical year of gains in one step). No new data: only a better reading of the bank's own transactions |

The talk track is the `% Say:` comment above each frame in `opener.tex`. Frame 3's question comes back
on frame 5, and frame 6 hands over to the weekend: how a machine learns a profile, starting with the
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
bar lengths, the order of the bars), and writes `numbers.tex` and `tools/expected.txt`.
`tools/check_numbers.py` reads the 27 expected strings back from the rendered PDF.

State of the build of 2026-11-03, after the new frames 4 to 6: 20 pages, 0 log errors, 0 em and en
dashes, no build metadata, no element that moves between clicks, all 27 numbers found in the PDF.
Every page of frames 4 to 6, each click included, was rendered and read.

## Sources

Grades as in the research notes: READ (the primary page was read), REVIEW (quoted by a published
review), SECONDARY (a press report or an excerpt of the primary document). The three revenues of
frame 1 were read in the primary documents by the second reader on 2026-11-03. Every source of frames
4 to 6 was read on 2026-11-03 in the built-in browser.

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
| 4 | Conversions: generative retrieval on Facebook Feed "nearly 2%" in "targeted segments"; GEM on more surfaces, off-site conversion campaigns +1.7% and app ad conversions +9.6%; Andromeda +1.4% on Facebook | Meta, earnings call of 21 October 2026, Susan Li, transcript: https://stockanalysis.com/stocks/meta/transcripts/718643-q3-2026/ | READ (third-party transcript) |
| 4 | "The global average price per ad increased 14% year-over-year, driven by ad performance gains and improvements in macro conditions"; ad revenue 63.1 billion USD in the quarter, up 26% (Say only) | the same call | READ (third-party transcript) |
| 5 | "Over 400 million customers have used Alexa for Shopping, our agentic shopping assistant, in the last 12 months. With customer interactions up 570% year over year. U.S. customers using Alexa for Shopping are spending 50% more per order than those who don't." | Amazon, earnings call of 29 October 2026, Andy Jassy, transcript: https://singjupost.com/amazon-com-inc-q3-2026-earnings-call-transcript/ (the passage is behind its "Continue Reading" button) | READ (third-party transcript) |
| 6 | Over 100 billion transactions of over 100 million members; 291 tabular features in the credit model; Table 2: income F1 +7.54%, spend R2 +6.85%, lending AUC +2.23%, credit default AUC +1.81% (market 2) and +1.25% (market 1), relative to the baseline models | Braithwaite and others (Nubank), "Your Spending Needs Attention: Modeling Financial Habits with Transformers", arXiv 2507.23267, version 3 of 29 October 2026, presented at the 9th Workshop on Machine Learning in Finance at KDD 2026, https://arxiv.org/abs/2507.23267v3 | READ |
| 6 | In use for the credit decisions of over 100 million users; "a contribution equivalent in magnitude to an entire year's typical cumulative gains"; "without adding new data sources or manual feature engineering" | the same paper, section 4.3 | READ |

## Choices made without asking

1. **The order**: the money, how much a machine chooses, compared to what, and then three
   measurements of autumn 2026, from advertising (Meta) to a shopping assistant (Amazon) to the
   customer profile itself (Nubank), which leads into the weekend's subject, representation learning.
2. **No title page.** The opener comes after the weekend's own title, so frame 1 starts with the money.
3. **Netflix 75% from the 2012 blog**, kept with its year. The often quoted "80% of hours streamed"
   was left out because its wording could not be read in the source.
4. **YouTube "over 70%"** is drawn as a 70% bar and labelled "over 70%".
5. **The question on frame 2** comes before the bars, so the room guesses first.
6. **Frame 4 shows conversions and the price per ad.** Conversions are what the models raised; the
   price per ad is where it shows up in money, in Meta's own words. The quarter's ad revenue (63.1
   billion dollars, up 26%) is in the Say only, because nothing ties all of it to the models.
7. **Frame 5 reuses frame 3's question.** Amazon compares users with non-users, who chose for
   themselves, so the slide draws the 50% the way frame 3 draws the 11% and asks "compared to what?".
8. **Frame 6 shows four of the paper's five results**, with its two decimals so that nothing is
   rounded. The second credit market (+1.81%) is in the Say only. The "32% increase in our
   long-term surrogate metric" is left out because the paper does not define the metric.
9. **Frame 6's gloss is the paper's online result** ("an entire year's typical cumulative gains"),
   and the closing line is its sentence on new data. The paper also calls the 1.25% "3 x a typical
   model launch"; the slide uses the year.
10. **Two leads were left out**: Stripe's card-testing detection from 59% to 97% (2025, an engineer's
    post on X that was not read) and Revolut's PRAGMA (2026, gains against baselines it never names).
11. **The deck lives in this public repository**, next to the weekend 2 lecture, and copies the style
    into `../style/`. A push publishes it on GitHub Pages; nothing links to it yet.

## Simplifications to know when presenting

- Frame 3, "more sales", means the total sales of the product and of its recommended substitutes. The
  experiment also found that a product's own sales fell 1.9% while its substitutes gained 9%.
- The 70% and the 75% are the companies' own statements (2018 and 2012). The 35% is McKinsey's (2013),
  and McKinsey names no source. None comes with a method. The Say comment of frame 2 says so.
- Frame 3's 11% is an average: the effect varied across products.
- Frame 1 compares annual totals: Google's line is "Google advertising" (search, YouTube ads and the
  network), Amazon's is "advertising services".
- Frame 4's four gains come from different launches on different groups of ads, so they do not add
  up. "Ads for websites" stands for Meta's "off-site conversion campaigns", and "targeted groups" for
  its "targeted segments". Meta credits the 14% rise of the price per ad to ad performance and the
  economy together, without a split.
- Frame 5's numbers are Amazon's, said on a call, with no method. The 400 million count users over
  12 months, and the 50% compares US users with US non-users.
- Frame 6's gains are relative changes, each on its own score (F1 for income, R2 for spending, AUC
  for the others), measured on past data. The bank says it could not run an A/B test of every variant
  because the outcome takes long to observe.

## Open items

1. The deck is linked from nowhere: neither `../index.html` nor the course site has it.
2. It has not been projected in HG D 7.2. The hatching and the hairlines fade first on a weak projector.
3. Frames 4 and 5 rest on third-party transcripts of the calls. Meta's and Amazon's investor pages
   carry the official recordings; nobody has listened to them.
4. Frames 4 to 6 have not had a second reader, unlike frames 1 to 3.

## Second read (frames 1 to 3 and the first frames 4 to 6)

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
- The other fixes concerned the first frames 4 and 5, which have since been replaced.
