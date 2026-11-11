# Cases deck: who uses it, and what it paid

Four business cases of the weekend 2 techniques, for AINIT HS26, Friday 13 November 2026: one case at the end
of each Friday lecture, then a map of four business questions to the techniques. Asked for on 2026-11-04,
after the BMAI HS26 evaluation, whose most repeated request (six comments, and the same in HS25 and FS26) was
real business use cases. Carlos chose the slot ("one case per lecture") and the length (10 to 15 minutes in
all) the same day. The same evening he rejected the cases of version 1 as old: "Results should be latest from
2021." Every case and every source of the map in version 2 was published from 2022 to 2026.

- `cases.pdf`: the deck, 5 frames over 17 pages (the clicks).
- `cases-handout.pdf`: one page per frame, its last click.
- `case1-nearest-neighbours.pdf`, `case2-matrix-factorization.pdf`, `case3-bandits.pdf`,
  `case4-gradient-descent.pdf`: the deck cut into the four slots, clicks included. The fourth holds frames 4
  and 5.
- `block1-nearest-neighbors.pdf`, `block2-matrix-factorization.pdf`, `block3-bandits.pdf`,
  `block4-parallelized-mf.pdf` and their handouts: since 2026-11-09 one deck per Friday block with the cases that
  follow it. Section "One deck per block" below.
- `weekend2-cases.pdf`: the deck for the weekend, all six cases in the order of the blocks, 52 pages;
  `weekend2-cases-handout.pdf`, 27 pages. Section "The weekend deck" below.
- `PRINCIPLES.md`: the lessons of the case decks and the rules for the next ones (bandits, advertising).

## One deck per block, 2026-11-09

Carlos, 2026-11-09: "Please reorganize the slides. I want that you don't make like each case a separate slide deck.
Simply for each block, put in one single deck all the slides with all the business cases." A block deck has a title
page ("Business cases", or "Business case" for one case, with the block's name below), then one `\section` per case,
which the style draws as a divider, and the case's frames file. `BLOCK_DECKS` in `tools/cases_numbers.py` lists the
cases of each deck and writes `tools/expected-<deck>.txt`.

| Deck | Friday block | Cases | Pages (handout) |
|---|---|---|---|
| `block1-nearest-neighbors.tex` | 08:15 the inner product and nearest neighbors | Etsy, Airbnb | 21 (11) |
| `block2-matrix-factorization.tex` | 10:00 and 11:00 matrix product and matrix factorization | Spotify | 8 (5) |
| `block3-bandits.tex` | 14:00 bandits | Spotify's home page, Amazon Payments | 17 (9) |
| `block4-parallelized-mf.tex` | 16:00 parallelized matrix factorization | LinkedIn's ads | 9 (5) |

The same day the six one-case decks (`etsy.tex`, `spotify.tex`, `airbnb.tex`, `spotify-home.tex`, `amazon.tex`,
`linkedin.tex`, their PDFs, handouts and expected files) were removed; commit `43e6adb` has them. The weekend deck
follows the order of the blocks since: Airbnb moved from section 3 to section 2, before Spotify. Choices made without
asking: a title page in every block deck, a divider also when a block has one case, the singular "Business case".

Build and checks, from this folder, for each block deck and for `weekend2-cases`:

```bash
python3 tools/cases_numbers.py
../style/tools/build.sh block1-nearest-neighbors.tex
../style/tools/check.sh block1-nearest-neighbors.pdf
python3 ../style/tools/check_overlays.py block1-nearest-neighbors.pdf
python3 tools/check_numbers.py block1-nearest-neighbors.pdf tools/expected-block1-nearest-neighbors.txt
python3 ../style/tools/make_handout.py block1-nearest-neighbors.pdf block1-nearest-neighbors-handout.pdf
```

State on 2026-11-09: 0 log errors, 0 em and en dashes, no build metadata, nothing moves between clicks; 14, 5, 9 and
3 strings found in the four block PDFs, 31 in the weekend deck. The title pages and dividers were rendered and read;
the frames are those of 2026-11-06, unchanged.

Later on 2026-11-09, after Carlos reviewed the facts of the matrix factorization block ("Apply the two wording fixes"):
Spotify frame 3 says "relative change" beside its two percentages, as the other cases do, and its talk track says the
full model was in production as of the paper, 2024. The paper's abstract gives +23% for the stream rate, where its
Table 5 gives +25.82% (full model) and "Neutral" (networks alone); the slide shows only Table 5's start rates.

The same evening Carlos asked what a site conversion is, then: "add in the slide this quotation that Airbnb ... calls
its plus 0.31% conversion gain a large portion of the team's annual goal ... Please relabel as you suggest". The
measures are now named by what they count: on Etsy frame 5 "visits that end in a purchase" and "searches that end in
a purchase" (the paper's site-wide conversion rate and organic search purchase rate), on Airbnb frame 3 "visits that
end in a booking" (the paper's "booking conversion"). Neither paper defines its measure; the labels give the usual
meanings. The quotation went first onto Etsy frame 5, at a new second click (commit `9107e24`). On 2026-11-10 Carlos
had it moved: "You cannot put Airbnb calls with 0.31% gain on the slides from Etsy. They need to go in the Airbnb
part." Airbnb frame 3 shows it at its second click, beside +0.31%: Airbnb calls this gain "a large portion of the
team's annual goal" (the preprint, Sec. 6.3). Etsy frame 5 shows cost and value at its first click and the recall
bars at its second, with Etsy's source line alone. A read of every Etsy and Airbnb slide and talk track against the
two papers found no other fact of one case in the other. Block 1 has 21 pages and the weekend deck 52. Words on the
handout pages: Etsy frame 5 has 61, Airbnb frame 3 has 57; Etsy frames 1 and 4 have 76 and 75, over the 70 of
PRINCIPLES.md. Checks: 0 log errors, 0 em and en dashes, no build metadata, nothing moves between clicks, 14 and 31
strings found.

## One deck per case, 2026-11-06

On 2026-11-06 Carlos asked again for business cases, now five of 10 minutes each, one after each block of the
Friday (08:00 inner product and nearest neighbours, 10:00 matrix factorization, 12:00 bandits, 14:00 matrix
factorization by gradient descent, 16:00 large-scale AI), every case at most five years old. He first wanted
ideas only ("Don't build anything show me ideas and then we shape them"), then dictated three decks slide by
slide. They are separate from `cases.tex`, whose cards are version 2 of 2026-11-04. Since 2026-11-09 they are built
in the block decks (section "One deck per block"); the one-case wrappers and PDFs of this section were removed.

| File | Frames (pages) | His plan |
|---|---|---|
| `etsy-frames.tex` | 5 (11) | Etsy and its shortlist, why keyword matching fails; the training data; a list of numbers for every search and every item; the new search, sorting by inner product step by step; cost and value |
| `spotify-frames.tex` | 3 (6) | Little data at launch; 128 numbers per listener and audiobook from two networks and a graph; the A/B test |
| `airbnb-frames.tex` | 3 (7) | The first stage of search; two networks and the nearest homes; three A/B tests and their value |

State on 2026-11-06, after the simplification: 0 log errors, 0 em and en dashes, no build metadata, nothing moves
between clicks; 11, 5 and 3 numbers found in the PDFs. Every page of the three decks was rendered and read.

Sources: Etsy and Spotify as for frames 1 and 2 of `cases.tex` (IEEE FMLDS 2024; WWW 2024 Companion). Airbnb:
Abdool and 12 others, "Applying Embedding-Based Retrieval to Airbnb Search", arXiv 2601.06873, January 2026, a
preprint (https://arxiv.org/abs/2601.06873), and their post "Embedding-Based Retrieval for Airbnb Search" on
Airbnb's engineering blog, April 2025 (https://airbnb.tech/ai-ml/embedding-based-retrieval-for-airbnb-search/).
Grade READ for both; the source sentences are in `tools/cases_numbers.py`.

### The weekend deck

Carlos, 2026-11-06: "Finally merge all this decks into a new deck for the weekend". `weekend2-cases.tex` has a
title page, then one `\section` per case, which the style draws as a divider with a Ge'ez numeral (Etsy, Spotify,
Airbnb, in the order he dictated them; since 2026-11-09 in the order of the blocks), and inputs each case's frames file. Since that evening a case is two
files: `<case>-frames.tex`, the frames with their talk track, and `<case>.tex`, a wrapper that built the case
alone until 2026-11-09. The weekend deck and the case decks share one source; after the split the three case PDFs printed the same
text as before. 28 pages, handout 15 pages, all 19 strings of `tools/expected-weekend2-cases.txt` found.

```bash
python3 tools/cases_numbers.py
../style/tools/build.sh weekend2-cases.tex
../style/tools/check.sh weekend2-cases.pdf
python3 ../style/tools/check_overlays.py weekend2-cases.pdf
python3 tools/check_numbers.py weekend2-cases.pdf tools/expected-weekend2-cases.txt
python3 ../style/tools/make_handout.py weekend2-cases.pdf weekend2-cases-handout.pdf
```

A new case: `PRINCIPLES.md`, section "Adding a case". `BLOCK_DECKS` in `tools/cases_numbers.py` lists the cases of
each block deck; the weekend deck takes them in that order (`WEEKEND_CASES`).

### Simplified, 2026-11-06

Carlos, after the first build: "This is too complicated for me. The slides need to be simplified. Make then 25%
simpler". Measured on the handouts (the last click of every frame; words counted by `pdftotext` and `wc -w`,
the source line and the page number included):

| Deck | Words before | Words after | Change | Pages before | Pages after |
|---|---|---|---|---|---|
| Etsy | 460 | 344 | -25% | 12 | 11 |
| Spotify | 219 | 152 | -31% | 6 | 6 |
| Airbnb | 243 | 155 | -36% | 7 | 7 |

What changed:

- All three: shorter source lines ("Jha and others (Etsy), IEEE FMLDS 2024."), and a shorter title wherever the
  title repeated a number of the slide.
- Etsy: frame 1 lost the sentence that its funnel already shows; frame 2 lost its lead sentence and one of four
  rows; frame 3 has one-line inputs and a plain sentence in place of the balloon; frame 4 has four items of three
  numbers (it had five of four; the bridge print is gone) and four pages instead of five, since the items now
  appear together with their inner products; frame 5 has shorter labels ("Plain version", his own words).
- Spotify: frame 1 lost its bars, which repeated the text, and shows "Over 70%" large at the second click; frame
  2 has a one-line lead ("The matchmaker learned the numbers. Here two networks compute them."), a graph of two
  podcasts and two audiobooks, four cells per list and no "128 numbers" labels; frame 3 is "The value: an A/B
  test", with shorter group names and no reference line.
- Airbnb: frame 1 lost the sentence on what Airbnb is and the half sentence its funnel shows; frame 2 has nine
  points and three nearest homes (it had fourteen and five) and no box around them; frame 3 is "The value: three
  A/B tests", without the labels "Version 1" to "Version 3", and keeps one quote, the paper's. The blog's
  comparison with the largest gains of two years is in the talk track only.
- Fixed on the way: the italic arrow labels of the two funnels (Etsy and Airbnb, frame 1) cut the top border of
  the box below them, also in the first build; they now have `inner sep=0.4pt`. A label of Spotify frame 2
  touched the box of the audiobook network.

### Second read, 2026-11-06

An agent read every claim of the three decks against the source files, and each finding was checked in the paper
before a change. What changed:

- Etsy: the training rows are positive actions "such as" cart adds and purchases (the paper's words), so frame
  2 no longer says "one row per search that ended in a cart add or a purchase", and frame 3 names cart adds and
  purchases where it said "random items". Keyword matching still runs beside the new retrieval (talk track of
  frame 4), so frame 1 keeps "used to come from keyword matching only".
- Spotify: the graph links items of all three kinds (a podcast and an audiobook, two podcasts, two audiobooks),
  and frame 2 draws both kinds of link. The listener's numbers are computed at each visit and the networks are
  retrained every day (talk track).
- Airbnb: "a hundred thousand homes" holds for popular places (frame 1). The new model's top results are added
  to those of the old first stage (a union), hence "used to be only a simple linear model". The blog's
  comparison of April 2025 concerns the bookings lift of the new system; the combined +0.31% comes from the
  paper (talk track of frame 3).

Choices made without asking:

- Etsy: he named slides one, two, four and five. Slide two is read as the data, slide three as the lists of
  numbers he described with it.
- Etsy frame 1: the search "mothers day gift" is the paper's example; the necklace listing is invented, and the
  source line says so.
- Etsy frame 2: the three rows are invented; the counts are the paper's ("more than 150 million interactions"
  from "up to 30 million users", one month of cart adds and purchases).
- Etsy frames 3 and 4: invented small integers, three per list, four items. `tools/cases_numbers.py` computes
  every product, sum and the order, and asserts that the necklace comes first and the gift wrap, the only item
  with the word "gift", falls out of the top two. The cells are tinted by sign as in the video store (blue above
  0, orange below, grey for 0, stronger from 2 and from -2 on), a solid tint where Codex plates otherwise hatch.
- Etsy frame 4 is built over four pages: the search's numbers; one inner product worked out (the necklace); every
  item with its numbers and its inner product; the sorted list with the top two as the shortlist. A click only
  adds, so the "animation" also plays in a PDF viewer.
- Etsy frame 5: the comparison is recall@100 on popular (head) searches, Table I of the paper.
- Spotify frame 1: the quarter and the three quarters are in the text, and "Over 70%" is large at the second
  click; he asked for diagrams on frames 2 and 3 only.
- Spotify frame 3: bars against the production model, drawn at 100, 123.87 and 146.83.
- Airbnb frame 1: "whatever the search" for the paper's "query-independent score".
- Airbnb frame 2: the inputs of both networks from Sec. 4.5; the picture of homes as points is a drawing.
- Airbnb frame 3: the three versions as boxes (two networks; a clustered index; a larger network); the paper's
  phrase is quoted, the blog's sentence is in the talk track.

Open items of these decks:

1. Which case goes after which block. Etsy and Airbnb are both nearest neighbours on two-tower vectors; Spotify
   fits the matchmaker. Since the evening of 2026-11-06 the 12:00 block has two decks and advertising one (next
   section); the 16:00 block has none.
2. Whether these decks replace `cases.tex`.
3. Linked from nowhere; the course site gets them only after Carlos's yes.

## The bandit and advertising decks, 2026-11-06 (evening)

Carlos asked for "the business-case decks for the bandit block and for advertising ... the same way as the Etsy,
Spotify and Airbnb decks", candidates first. Eight candidates went to him in chat, two paragraphs each; he chose
"Spotify, Amazon Payments, and LinkedIn Lirank", then wrote "Produce the slides, follow the style from the slides
for the matrix factorization part". He dictated none of these three: they follow the Spotify deck (`spotify-frames.tex`), the case after the
10:00 matrix factorization block, in three frames: the problem, with a big number or a funnel at the second click;
the method as a diagram whose top line ties it to the block's game; the value of an A/B test.

| File | Frames (pages) | Content |
|---|---|---|
| `spotify-home-frames.tex` | 3 (7) | Music or podcasts on the home page, a common rule of past listening, over 600 million users; epsilon-greedy with a network for the estimates (three invented mixes as bars), 98.5% and 1.5%; the A/B test against the mix of the last 90 days: +36.6% streams per podcast shelf shown, +1.28% minutes listened, in production as of March 2025 |
| `amazon-frames.tex` | 3 (7) | One image and one tagline per page, the steps started, submitted, approved, a page that wins the first step can lose the last; one UCB score per step, added up (an invented table: the first step alone picks pair A, the sum pair B); the A/B test of 7 weeks: approvals up by a high single-digit percentage in one group (so far, not reported as significant), no pair the bandit tried beat the fixed page in the other, Amazon's sentence on exploration |
| `linkedin-frames.tex` | 3 (7) | The chance of a click enters the auction and the price, which clicks advertisers pay for, over 1 billion members; a list of numbers for every advertiser, campaign and ad, learned from clicks by gradient descent; +4.3% click rate on ads in A/B tests, 96% less training time in an offline test of incremental training |

The game of each: Spotify's home page and Amazon tie to "Once Upon a Mirror" (`w2-cx-private/03_bandits`: the
mirror counts taps, epsilon-greedy spins a roulette, UCB adds a bonus to the estimate, "the fewer dots, the bigger
the bonus"); LinkedIn ties to "Once Upon a Matchmaker" (`02_matrix_factorization`: a list of numbers for every
customer and film, improved by gradient descent).

Words on the slides, counted as in "Simplified" (handouts, `pdftotext` and `wc -w`, without the footer line):
Spotify's home page 175 (59, 65, 51 a slide), Amazon 196 (57, 70, 69), LinkedIn 156 (54, 44, 58), after the second
read below. Amazon's 70 include the 12 numbers of its table. The audiobooks deck has 152.

State on 2026-11-06: 0 log errors, 0 em and en dashes, no build metadata, nothing moves between clicks; 7, 2 and 3
strings found in the PDFs of the one-case decks of that day (removed on 2026-11-09). The weekend deck has
52 pages, a handout of 27 pages, and all 31 strings found. Every page of the three decks was rendered and read.

Sources, grade READ; the sentences are in `tools/cases_numbers.py` and in
`git_ainit/research_notes/Business cases of the weekend 2 techniques/chosen_bandit_and_ads_cases.md`:

- Spotify: Feijer, Abdollahpouri, Gupta and 7 others (Spotify, NYU, Uber), "Calibrated Recommendations with
  Contextual Bandits", CONSEQUENCES workshop at ACM RecSys 2025, arXiv 2509.05460, September 2025
  (https://arxiv.org/abs/2509.05460).
- Amazon: Chidi Prince John and Burak Gozluklu (Amazon), "Uplifting conversion across the acquisition funnel with
  personalization using contextual bandits on AWS", AWS Machine Learning Blog, 1 October 2026
  (https://aws.amazon.com/blogs/machine-learning/uplifting-conversion-across-the-acquisition-funnel-with-personalization-using-contextual-bandits-on-aws/).
- LinkedIn: Borisyuk and 33 others, "LiRank: Industrial Large Scale Ranking Models at LinkedIn", KDD 2024, the paper
  of card 4 of `cases.tex`. This deck uses only what it says of the ads model: the paper covers the feed, jobs and
  ads, and its 70 to 20 hours of training, its learning rate, its "billions of parameters" and its retraining
  every 8 hours do not concern the ads model.

Choices made without asking:

- "The slides for the matrix factorization part" read as the Spotify deck (`spotify-frames.tex`), the case after the
  10:00 block.
- Spotify frame 1: "A common rule gives users the mix of their past listening". The paper calls this rule,
  calibration, "a widely used approach in industry" and does not say which rule ran before the bandit; the control
  of its A/B test was the mix of the last 90 days.
- Spotify frame 2: the three mixes and their bars are invented (the paper does not list its set of mixes), marked
  "Invented mixes and estimates" in the source line, and generated with an assert that half and half is the highest. The
  reward is "the chance of a stream from the page" (a stream from any shelf counts). "98.5% of the pages" for the
  epsilon-greedy split of 1.5%.
- Spotify frame 3: the paper's impression-to-stream ratio as "streams per podcast shelf shown"; bars at 100 and
  136.6; "split at random" for an online A/B test, whose assignment the paper does not describe.
- Amazon frame 1: "an Amazon Payments product", since the post does not name it; the funnel narrows as a drawing.
- Amazon frame 2: an invented table of three pairs (6, 3, 1; 4, 4, 4; 3, 2, 3), with asserts in
  `tools/cases_numbers.py`: pair A has the best score for the first step and the worst for the approval, pair B the
  highest sum; the scores are added with equal weights, as the post's "approximately equal weights".
- Amazon frame 3: the lift in the post's words, "a high single-digit percentage", without bars, since the post gives
  no number; arrows in the style's colours for a win (blue) and a loss (vermillion).
- LinkedIn frame 2: "gradient descent" for the paper's optimizers, Adam and AdaGrad (Sec. 6.2, said of its models
  in general).
- LinkedIn frame 3: the +4.3% belongs to the lists together with other changes of the network (the paper names
  quantization, low-rank DCNv2, TransAct and isotonic calibration beside the lists); the 96% is marked "in an offline test".
- The weekend deck: the three come after Airbnb, as sections 4 to 6 ("Spotify's home page", "Amazon Payments",
  "LinkedIn's ads"), and the first three keep their order. The style draws Ge'ez numerals up to five, so section 6
  shows the digit 6.
- `cases-kit.tex` has two new macros, `\scell` and `\scellwin`: the boxes of a small table of numbers, the chosen
  one with a violet border.

Open items of these decks:

1. Which block each one follows: Spotify's home page and Amazon after 12:00 (bandits); LinkedIn's ads after 14:00
   (gradient descent) or 16:00 (large-scale AI).
2. Whether Carlos wants to change them by dictation, as he did with the first three.
3. Linked from nowhere; the course site gets them only after his yes.

### Second read, 2026-11-06 (evening)

An agent read every claim of the three decks against the source files: 20 findings, no wrong number. Each finding
was read again in the source before a change. What changed on the slides:

- Spotify frame 1: "A common rule" (the paper: "a widely used approach in industry"; it names a second kind of
  target); "tastes can change with the hour, the day of the week, even the device", for the paper's "may vary"
  (its Figure 1 shows hours and days, no device).
- Spotify frame 2: "Invented mixes and estimates" in the source line; the paper never lists its mixes.
- Spotify frame 3: "In production as of March 2025", the paper's words; a preprint of September 2025 cannot say it
  still runs.
- Amazon frame 3: "No pair it tried beat the fixed page" (the post: the model "explored most of its arm pool yet
  found no combination that beat the static page"). Under the first group, "relative change so far, not reported as
  significant": the post says it "currently" sees the lift and calls the lifts directional, while it calls the fall
  in the second group significant.
- LinkedIn frame 1: "Advertisers choose which clicks they pay for: some count likes or comments, others only visits
  to their website", for the paper's examples ("such as") of chargeable clicks.
- LinkedIn frame 3: "in an offline test, when each new model builds on the earlier ones": the 96% comes from an
  offline test, and incremental training also keeps the new model close to the earlier ones (Sec. 3.6), which a
  plain restart from the last model does not.

What changed in the talk tracks: Spotify's reward is engagement, a stream for example; the random mixes gave fewer
successes and a weaker model, and "too far from what people like" is the authors' explanation; UCB is one of the
authors' plans. Amazon: no "separate model for each group" (the post advises it and does not say it ran it); the
parts are "reviewed", the post's word; the check before the launch was offline estimates; the scores are computed
for every prospect, and a visitor without one sees the fixed page; new images and taglines are the post's advice,
with no plan stated. LinkedIn: the changes came one after another, checked in online A/B tests; incremental training
"can" make updates cheaper (the paper does not say the ads model is updated this way); training compares predictions
with the clicks in the logs; the gain was "the score on the test data (AUC)", +0.18%, where it said "accuracy"; the
network gives three chances, one for each family of paid clicks, where the picture shows one; "LinkedIn has more than
a billion members", the paper's count of all members.

Kept as they are, with the reason:

- Spotify frame 2, "Chance of a stream from the page": the paper's reward is engagement "e.g. streams"; the slide
  keeps the concrete example, and the talk track says engagement.
- LinkedIn frame 2: the loop of gradient descent reaches the lists only, the new part on the slide; the talk track
  says the network learns too.
- LinkedIn frame 3, "LinkedIn put the new model into production", for "We have deployed techniques to production".

The sections below describe `cases.tex`, version 2 of 2026-11-04.

## On the course site, 2026-11-06

Carlos, 2026-11-06: "the slides with the business cases are not up. Publish them." The course site (`AINIT-PAGE`)
serves copies from `public/slides/we2/`. Until 2026-11-09 (commit `70fcdd4`) it had one PDF per case; since that day
(commit `2b27782`, "for each block, put in one single deck all the slides with all the business cases") one deck per
block on its Friday row, and the weekend deck with its handout in the Materials list, group "Business cases".

| Site file | Source here | Where |
|---|---|---|
| `ainit-hs26-business-cases-nearest-neighbors.pdf` | `block1-nearest-neighbors.pdf` | Friday 08:15, "Cases: Etsy, Airbnb" |
| `ainit-hs26-business-cases-matrix-factorization.pdf` | `block2-matrix-factorization.pdf` | Friday 11:00, "Case: Spotify" |
| `ainit-hs26-business-cases-bandits.pdf` | `block3-bandits.pdf` | Friday 14:00, "Cases: Spotify's home page, Amazon Payments" |
| `ainit-hs26-business-cases-parallelized-mf.pdf` | `block4-parallelized-mf.pdf` | Friday 16:00, "Case: LinkedIn's ads" |
| `ainit-hs26-business-cases.pdf`, `ainit-hs26-business-cases-handout.pdf` | `weekend2-cases.pdf`, `weekend2-cases-handout.pdf` | Materials list |
| `ainit-hs26-business-cases-<block>-handout.pdf`, the four blocks | `block<N>-<name>-handout.pdf` | only in the weekend's ZIP, folder Handouts (since 2026-11-11, AINIT-PAGE `8bf143b`) |

The four block decks are also in the Materials list, under the names of their blocks. The six one-case site files
(`ainit-hs26-case-etsy.pdf` and the others) were removed on 2026-11-09. LinkedIn's ads (gradient descent at scale)
is on the 16:00 row, "Parallelized matrix factorization", a choice Carlos can swap to 11:00. A live file is
https://eth-ainit-hs26.github.io/AINIT-PAGE/slides/we2/<file>
After a rebuild, copy the PDF over the same site file name, run `npm ci && npm run build` in `AINIT-PAGE`, push to
`main`, then curl the live file and `cmp` it with the one here. The block handouts are not published.

## Frames

| # | Slot | Title | Technique | On the slide |
|---|---|---|---|---|
| 1 | Friday 08:00, after the video store | Etsy, 2024: nearest neighbours join keyword search | Nearest neighbours by inner product, on vectors from a two-tower model | Each search and each product a list of numbers; the products nearest by inner product join the shortlist. A/B tests, relative: site-wide conversion rate +2.63%, purchase rate of searches +5.58%. Cost: on popular searches a plain version found 32% of the products bought, keyword search 63%. Decided: a compressed index: under 4% of the nearest products missed, lookups within 20 ms |
| 2 | Friday 10:00, after the matchmaker | Spotify, 2024: podcasts reveal audiobook tastes | A vector per listener and per audiobook, scored by inner product (a two-tower model on a graph of podcasts and audiobooks) | 128 numbers each, learned from what people streamed, podcasts included. A/B test with 11.5M monthly active users: +46.8% listeners starting a new audiobook. Cost: for users new to audiobooks its picks cover 12.0% of the catalogue, against 19.3% for a simpler model. Decided: in production for every eligible user; the narrower catalogue to be revisited |
| 3 | Friday 12:00, after the bandits | Adyen, 2025: a better bandit approves more payments | Epsilon-greedy contextual bandit | 2 to 15 ways to send most payments. A/B test: +0.1% approval rate from smarter exploring, 9M more approvals a year (Adyen's estimate). Cost: exploring risks declines; the next model did 0.2% worse. Decided: contracts and card network rules remove options first |
| 4 | Friday 14:00, after gradient descent | LinkedIn, 2024: bigger steps instead of longer training | Gradient descent at scale: ranking models with billions of parameters, trained on several GPUs | Models rank the feed, jobs and ads. A/B tests, relative: +0.5% member sessions in the feed, +4.3% click rate on ads. Cost: a training run took 70 hours, 20 after splitting the model across GPUs; many early runs diverged. Decided: triple the learning rate in place of longer training |
| 5 | Friday 14:00 | Which technique answers which question | All four | Four business questions, the technique for each, this weekend's case and other companies that use it (Airbnb, Snap; Pinterest, Uber; Amazon, Dream11; Kuaishou), with the venue and year of each source |

Every case frame is the same two by two card, one quarter per click: what was built, with this weekend's
session (top left); the result and how it was measured (top right); what it cost (bottom left); what the
company decided (bottom right). The talk track is the `% Say:` comment above each frame in `cases.tex`, about
2.5 minutes per case and 1 minute for the map.

## Build and checks

Run from this folder:

```bash
python3 tools/cases_numbers.py
../style/tools/build.sh cases.tex
../style/tools/check.sh cases.pdf
python3 ../style/tools/check_overlays.py cases.pdf
python3 tools/check_numbers.py cases.pdf
python3 ../style/tools/make_handout.py cases.pdf cases-handout.pdf
python3 tools/split_parts.py cases.pdf
```

No number is typed into `cases.tex`. `tools/cases_numbers.py` holds every number next to the sentence of its
source, asserts the order of Etsy's three models on popular searches (final model 72%, keyword search 63%,
plain version 32%), and writes `numbers.tex` and `tools/expected.txt`. `tools/check_numbers.py` reads the 19
expected strings back from the rendered PDF.

State on 2026-11-04, version 2 after its second read: 17 pages, 0 log errors, 0 em and en dashes, no build
metadata, nothing moves between clicks, all 19 numbers found in the PDF. The last click of every frame was
rendered and read.

## Sources

Grades: READ (the primary text was read), REVIEW (the source contradicts itself, or its venue or date is
uncertain). All read on 2026-11-04. A preprint or a company blog has no peer review; the Source column says
which each one is.

| Frame | Claim | Source | Grade |
|---|---|---|---|
| 1 | More than 100 million items, several thousand candidates per search (Say); candidate retrieval "historically" powered by lexical matching (Say), and the inverted index retrieval system still described in the present tense beside the new one (Sec. IV), hence "join keyword search"; the query tower takes the user's location, recent searches and other history (Say); trained with cosine similarity; quality numbers such as shop popularity appended to each product vector and weights to the query vector, scored by one inner product (Say); A/B tests on live traffic, aggregated: site-wide conversion rate +2.63%, organic search purchase rate +5.58%; Recall@100 on head queries (Table I): Base 0.32, BM25 0.63, the final model 0.72; 4 A100 GPUs, about 72 hours (Say); a 4-bit product quantizer fastscan index in Faiss, re-ranking after fetching 5 times K, recall loss under 4% against exact nearest neighbours, P99 latency under 20 ms (in the bullet on the index; "tens of milliseconds" is the requirement, Say) | Jha, Subramaniyam, Benjamin, Taula (Etsy), "Unified Embedding Based Personalized Retrieval in Etsy Search", 2024 IEEE International Conference on Future Machine Learning and Data Science (FMLDS), Sydney, pp. 258-264, DOI 10.1109/FMLDS63805.2024.00055 (Crossref); preprint https://arxiv.org/abs/2306.04833 , v1 7 June 2023 (both A/B numbers already in it), v2 25 September 2024, read in full | READ |
| 2 | 11.5 million monthly active users in 3 random groups: the production model, the 2T model, 2T-HGNN; the shelf "Audiobook for you" (Say); new audiobooks start rate +46.83% for 2T-HGNN and +23.87% for 2T (Table 5), "a 46% surge in the rate of people starting new audiobooks" (Sec. 1); 128-dimensional vectors, close "in dot product distance", computed by two towers from listening history, demographics and each book's title and description (Sec. 4.3.1, Say); podcasts and audiobooks linked when one user streams both; over 70% of the first audiobook listeners had listened to podcasts, at launch 25% of users made 75% of the audiobook streaming hours (Figure 2A), each audiobook had to be bought at launch (Say); coverage, offline, for users who "never interacted with an audiobook" 12.0% for 2T-HGNN against 19.3% for 2T (Table 3), a trade-off "to be eventually re-consider[ed]"; in production for all eligible users | De Nadai, Fabbri, Gigioli, Wang, Li, Silvestri, Kim, Lin, Radosavljevic, Ghael, Nyhan, Bouchard, Lalmas-Roelleke, Damianou (Spotify), "Personalized Audiobook Recommendations at Spotify Through Graph Neural Networks", Companion Proceedings of the ACM Web Conference 2024 (WWW '24 Companion, Industry Track), pp. 403-412, DOI 10.1145/3589335.3648339; https://arxiv.org/abs/2403.05185 , read in full | READ. The stream rate is REVIEW (abstract +23%, Table 5 +25.82%) and stays off the slide |
| 3 | Production policy epsilon-greedy with a boosting model; typically 2 to 15 actions per payment after the rule and risk filters, median 4; 5% of live traffic per variant, four weeks for the main comparison (two variants ran one week, Table 3); +0.1% for the best SquareCB variant over epsilon-greedy, an estimated 9 million more authorised transactions a year; 87.4% and 93.5% positive rewards, "correlates with a 0.2% performance regression", a drop the caption of Figure 10 attributes to the imbalance; contracts, card network rules and amount thresholds filter the actions, fraud risk prunes them; retrained every 7 days (Say) | Vangara and Egg (Adyen), "Contextual Bandits in Payment Processing: Non-uniform Exploration and Supervised Learning", OARS workshop at KDD 2025, https://arxiv.org/abs/2412.00569 (version 2) | READ |
| 3 | Interventions such as "adjusting logic or modifying transaction metadata" (Say); "58% of tests were flat or inconclusive, resulting in over 20 weeks per year of wasted experimentation time" (Say); off-policy evaluation "alongside traditional on-policy evaluation" (Say) | Egg (Adyen), "Off-policy Evaluation for Payments at Adyen", https://arxiv.org/abs/2501.10470 , v1 15 January 2025 (preprint) | READ |
| 4 | More than 1 billion members (Say); online A/B tests, relative: +0.5% member sessions in the Feed, +0.89% and +0.87% qualified applications in job search and job suggestions (Table 7, Say; the abstract's +1.76% is their sum), +4.3% Ads CTR; a global Feed model with billions of parameters (Sec. 3.9); synchronous training on multiple GPUs with Horovod; model parallelism of the embedding tables, training time from 70 to 20 hours in benchmarks; the Feed trained on 100% of sessions, up from 13% (Say); many diverging runs, warm-up from 5% to 50% of the training steps (Say); more training steps ruled out for "experimentation velocity", a three-fold learning rate closed almost all of the gap; incremental training starts from the previous model and stays close to it, one day of new data against a 21-day fresh start, training time -96% (Sec. 3.6, Tables 3 to 5, Say); the model for short-lived posts retrained every 8 hours (Say) | Borisyuk, Zhou, Song, Zhu, Tiwana, Parameswaran and 28 others (LinkedIn), "LiRank: Industrial Large Scale Ranking Models at LinkedIn", KDD '24, Barcelona, DOI 10.1145/3637528.3671561; https://arxiv.org/abs/2402.06859 (version 2), read in full | READ |
| 5 | Airbnb: each search and each listing a vector from a two-tower model, the listings nearest to the search kept as candidates; launched in search and promotional emails | Abdool and others (Airbnb), "Applying Embedding-Based Retrieval to Airbnb Search", https://arxiv.org/abs/2601.06873 (preprint, January 2026); "Embedding-Based Retrieval for Airbnb Search", Airbnb blog, 2025, https://airbnb.tech/ai-ml/embedding-based-retrieval-for-airbnb-search/ | READ |
| 5 | Snap: friend suggestions from the nearest neighbours of a user's vector, next to friends of friends | Shi and others (Snap), "Embedding Based Retrieval in Friend Recommendation", SIGIR '23, pp. 3330-3334, DOI 10.1145/3539618.3591848; Kung and others (Snap), "Improving Embedding-Based Retrieval in Friend Recommendation with ANN Query Expansion", SIGIR '24, pp. 2930-2934, DOI 10.1145/3626772.3661367 | READ |
| 5 | Pinterest: one vector per user (PinnerFormer) for the home feed, "deployed in production as of Fall 2021" | Pancha, Zhai, Leskovec, Rosenberg (Pinterest), "PinnerFormer: Sequence Modeling for User Representation at Pinterest", KDD '22, pp. 3702-3712, DOI 10.1145/3534678.3539156, https://arxiv.org/abs/2205.04507 | READ |
| 5 | Uber Eats: one two-tower model "replaces thousands of city DeepMF models" (Say) | Ling, Barr, Kurra, Zhu, Marcott (Uber), "Innovative Recommendation Applications Using Two Tower Embeddings at Uber", Uber Engineering Blog, 26 July 2023, read in the copy http://web.archive.org/web/20251012030030/https://www.uber.com/blog/innovative-recommendation-applications-using-two-tower-embeddings/ (the live page refused automated reading) | READ (no business result) |
| 5 | Amazon Payments: a contextual bandit (LinUCB) picks the image and tagline each visitor sees on the page of a payments product, where an application starts; tested for seven weeks against the static page (Say) | John and Gozluklu (Amazon), "Uplifting conversion across the acquisition funnel with personalization using contextual bandits on AWS", AWS Machine Learning Blog, 1 October 2026, https://aws.amazon.com/blogs/machine-learning/uplifting-conversion-across-the-acquisition-funnel-with-personalization-using-contextual-bandits-on-aws/ | READ |
| 5 | Dream11: bandits choose the payment gateway of each transaction (Say) | Chaudhary, Rai, Gupta, "Maximizing Success Rate of Payment Routing using Non-stationary Bandits", https://arxiv.org/abs/2308.01028 (version 2, October 2023) | READ; the venue year is REVIEW (printed as 2023 and as 2024) |
| 5 | Microsoft retired Azure Personalizer in 2026 (Say) | Azure update of 29 September 2023: "On 1 October 2026 AI Services Personalizer will be retired.", http://web.archive.org/web/20231206025711id_/https://azure.microsoft.com/en-us/updates/ai-services-personalizer-will-be-retired-on-1-october-2026/ ; Microsoft Lifecycle, https://learn.microsoft.com/en-us/lifecycle/end-of-support/end-of-support-2026 ; the Learn page says 25 August 2026, https://learn.microsoft.com/en-us/previous-versions/azure/ai-services/personalizer/what-is-personalizer | READ; the day is REVIEW (two dates, both in 2026) |
| 5 | Kuaishou: OneRec, a recommender trained on "90 servers for training, each equipped with 8 flagship GPUs" (Say) | OneRec Team (Kuaishou), "OneRec Technical Report", https://arxiv.org/abs/2506.13695 (version 1 June 2025, read version 4; a technical report) | READ |

## Choices made without asking

1. **10 to 15 minutes in all**, read as about 2.5 minutes per case and 1 minute for the map.
2. **Results from 2021 on**, Carlos's rule for version 2. The oldest source on the slides is Pinterest's (KDD
   2022, deployed autumn 2021).
3. **The cases.** Etsy: an A/B result of nearest neighbours by inner product, with a failure (the plain version
   against keyword search) and a speed trade-off. Spotify: a vector per listener and per audiobook, a randomised
   test of 11.5 million users, a trade-off stated by the authors. Adyen: the only finance case with a primary
   source and a measured result; it runs epsilon-greedy, the rule taught at 12:00. LinkedIn: the learning rate
   and the training time decided by the speed of experiments.
4. **Spotify in place of Twitter's TwHIN** (KDD 2022) at 10:00. TwHIN's free vectors per user are closer to the
   matchmaker, but its online result (cost per conversion -10.3%) comes from ads models that take the vectors as
   inputs, and the traffic shares, the duration and the computation are withheld. Uber's blog (2023) is the
   only source found that names matrix factorization in production after 2021, and it gives no business result.
5. **Cases read and not used**, all READ: LinkedIn job matching (arXiv 2024, +2.37% successful job search
   sessions), LinkedIn LiNR (CIKM 2024, +3% professional daily active users), Deezer (KDD 2021, a chart without
   numbers, tested in 2020), Expedia AdaptEx (RecSys 2023, no lift number), Amazon's causal bandit on Amazon.com
   pages (ORSUM 2022, +0.16% in the best of six cells), Netflix's foundation model (2025, no result). Read and
   set aside: Morgan Stanley's assistant (a vendor story, 2024), Stripe's payments foundation model (2025, no
   method or measurement described), LinkedIn 360Brew (withdrawn from arXiv). Amazon's WWW 2024 paper, in which
   Thompson sampling "catastrophically fails" on production data, is a risk case that no frame uses.
6. **One card for every case**, four clicks, the same labels in the same places.
7. **No title page**: each frame is shown alone at the end of a lecture.
8. **The session boxes** name the video store (08:00), the matchmaker (10:00), the bandits (12:00) and
   gradient descent (14:00). The 12:00 game was not final on 2026-11-04, so its box names the subject.
9. **"9M" and "11.5M"** on frames 3 and 2: the number column is too narrow for "9 million".
10. **None of the opener's numbers.** Three numbers of the talk track share a value with the opener's and
    count other things: Spotify's 70% and 75%, Etsy's 100 million items.
11. **The map has four rows**, one per lecture, so gradient descent has a row of its own (version 1 had three).
    Expedia was dropped from the bandits row for space. Microsoft's retired Personalizer is the vendor risk, in
    the Say only.
12. **The year in each title is the year of the venue.** Etsy's preprint is from June 2023, its conference
    from 2024; Adyen's test ran before 30 November 2024, its workshop was in 2025.

## Simplifications to know when presenting

- Frame 1, "nearest by inner product": Etsy trains with cosine similarity and serves an inner product of
  vectors with quality numbers appended.
- Frame 1, "found 32% of the products bought" stands for Recall@100 on head queries: the share of purchased
  products among the top 100 results of popular searches. The final model reaches 72%.
- Frame 1, "join keyword search": the paper describes Etsy's inverted index retrieval in the present tense
  beside the new one, and does not say whether the new retrieval replaced it for any traffic.
- Frame 1, "under 4% of the nearest products missed" is the recall loss of the compressed index with
  re-ranking, against exact nearest neighbours; "lookups within 20 ms" is the P99 latency stated for the index,
  99% of the lookups. The P99 of the whole model with its quality numbers, 18 ms, is reported separately.
- Frames 1 and 4 mark their results as relative changes. Frame 2's +46.8% is relative too; its header has no
  "relative" because its second number is the size of the test.
- Frame 2: in the matchmaker the numbers of each customer and film are free parameters. Spotify computes them
  with two networks (the towers) from listening history, demographics, each book's title and description and the
  graph of podcasts and audiobooks, and scores them by inner product, as in the matchmaker.
- Frame 2, "+46.8%" is Table 5's 46.83%, the rate of people starting new audiobooks. Its baseline is taken as
  the production model from the design of the test (three groups); Table 5 does not name it. The simpler model
  is 2T, the same towers without the graph network: +23.87%, and no significant change in stream rate.
- Frame 2, "users new to audiobooks" are Table 3's cold-start users, who never interacted with an audiobook.
  "Cover" is catalogue coverage: the share of the catalogue that appears in the recommendations, measured
  offline.
- Frame 3's +0.1% compares a smarter exploration rule (SquareCB) with the epsilon-greedy bandit already
  running. The paper does not say whether Adyen switched.
- Frame 3, "the next model did 0.2% worse": the text says the more imbalanced data "correlates with a 0.2%
  performance regression"; the caption of Figure 10 attributes the drop to the imbalance.
- Frame 3, "Most payments ... 2 to 15 ways": the paper's "typically", counted after the rule and risk filters.
- Frame 4, "splitting the model across GPUs" stands for 4D model parallelism: the embedding tables are split
  across the worker processes. The 70 and 20 hours are from LinkedIn's benchmarks.
- Frame 4, "triple the learning rate" came after the warm-up was lengthened from 5% to 50% of the training
  steps; the paper says the longer warm-up made the higher rates stable.
- Frame 4's results come from online tests of several of the paper's techniques, deployed one by one.
- Frame 4, "about 0.9 percent more qualified job applications" (Say): Table 7 gives +0.89% for job search and
  +0.87% for job suggestions (JYMBII), two products; the abstract adds them into +1.76%.
- Frame 5, "Matrix factorization and its successors" (Say): Pinterest and Uber learn their vectors with towers,
  and Uber's towers replaced per-city factorizations. Pinterest's online tests use its user vector as an input of
  the home feed's ranking model.

## Version 1

Commits `b840920`, `fa1c3de` and `405acd3`, 2026-11-04: Airbnb 2018 (similar homes), the Netflix Prize 2009,
Adyen 2025 and Netflix 2012, and a map of sources from 2003 to 2018. Rejected the same day for its age. Adyen
stayed; its frame cites only the two 2025 papers since then.

## Second read

After version 2 was built, a second agent checked every claim of `cases.tex` against its source. No number on
a slide was wrong. Changed:

- Frame 1: the title "nearest neighbours join keyword search" (was "search results are nearest neighbours";
  ranking stages follow the shortlist, and the inverted index retrieval still runs); "join the shortlist"; "under
  4% of the nearest products missed, lookups within 20 ms"; the result header says "relative"; the Say has shop
  popularity in place of rating and "tens of milliseconds".
- Frame 2: "users new to audiobooks" (was "new users"); the Say: each audiobook had to be bought at launch, the
  25% and 75% are audiobook hours at launch, two networks compute the numbers, the coverage is offline.
- Frame 4: the result header says "relative"; the Say has about 0.9% more qualified job applications in job
  search and in job suggestions (was 1.76%, the sum of the two), and a new model that stays close to the
  previous one and learns only from the newest data.
- Frame 5, the Say: "To close today's lectures" (Saturday follows); Kuaishou trains "a recommender, OneRec";
  Amazon's bandit picks the picture and tagline on the page where an application starts.
- `tools/cases_numbers.py`: the 8-hour quote is in Sec. 3.9.

Not checked: the control of Etsy's A/B tests; whether Etsy's 20 ms includes the query's own computation;
whether Personalizer is offline (Microsoft's pages give the retirement date only).

## Open items

1. `cases.pdf` (version 2) is linked from nowhere. The weekend deck (since 2026-11-06) and the four block decks (since
   2026-11-09) are on the course site (section "On the course site").
2. It has not been projected in HG D 7.2.
3. No bank or insurer was found with nearest neighbours or matrix factorization and an online result published
   from 2021 on. Finance is Adyen's frame and two names on the map (Amazon Payments, Dream11).
4. Box of frame 3: rename to the 12:00 game when it is final.
5. Spotify's paper gives two stream rates (abstract +23%, Table 5 +25.82%); the slide shows neither.
6. No frame on Swiss or EU rules, to keep one case per lecture. Material for one, READ, is in the research
   notes (`git_ainit/research_notes/Business cases of the weekend 2 techniques/risks_rules.md`, local and
   private):
   - The FDPIC's final report of 15 April 2024 on Digitec Galaxus (EDÖB-A-B3653401/5, in German,
     https://www.edoeb.admin.ch/dam/en/sd-web/UbgCr4c7n-cD/20240415_Schlussbericht_Galaxus.pdf ): to order,
     customers needed an account and had to accept the analysis of their shopping behaviour, with no way to
     object except to direct marketing; tying this to a mandatory account was found disproportionate; six
     recommendations, of which Digitec Galaxus accepted the sixth "without acknowledging a legal obligation" (our
     translation) and rejected 3, 4 and part of 2. The FDPIC closed the case on 12 February 2026: customers can
     now switch website personalisation off with a single click (https://www.edoeb.admin.ch/en/digitec-galaxus-en ).
   - EU Digital Services Act (2022), Article 38: very large platforms must offer, for each recommender system, at
     least one option not based on profiling.
