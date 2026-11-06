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

## One deck per case, 2026-11-06

On 2026-11-06 Carlos asked again for business cases, now five of 10 minutes each, one after each block of the
Friday (08:00 inner product and nearest neighbours, 10:00 matrix factorization, 12:00 bandits, 14:00 matrix
factorization by gradient descent, 16:00 large-scale AI), every case at most five years old. He first wanted
ideas only ("Don't build anything show me ideas and then we shape them"), then dictated three decks slide by
slide. They are separate from `cases.tex`, whose cards are version 2 of 2026-11-04.

| File | Frames (pages) | His plan |
|---|---|---|
| `etsy.tex`, `etsy.pdf`, `etsy-handout.pdf` | 5 (12) | Etsy and its shortlist, why keyword matching fails; the training data; a list of numbers for every search and every item; the new search, sorting by inner product step by step; cost and value |
| `spotify.tex`, `spotify.pdf`, `spotify-handout.pdf` | 3 (6) | Little data at launch; 128 numbers per listener and audiobook from two networks and a graph; the A/B test |
| `airbnb.tex`, `airbnb.pdf`, `airbnb-handout.pdf` | 3 (7) | The first stage of search; two networks and the nearest homes; three A/B tests and their value |

Build and checks, from this folder, for each of `etsy`, `spotify`, `airbnb`:

```bash
python3 tools/cases_numbers.py
../style/tools/build.sh etsy.tex
../style/tools/check.sh etsy.pdf
python3 ../style/tools/check_overlays.py etsy.pdf
python3 tools/check_numbers.py etsy.pdf tools/expected-etsy.txt
python3 ../style/tools/make_handout.py etsy.pdf etsy-handout.pdf
```

State on 2026-11-06: 0 log errors, 0 em and en dashes, no build metadata, nothing moves between clicks; 11, 7
and 3 numbers found in the PDFs. Every page of the three decks was rendered and read.

Sources: Etsy and Spotify as for frames 1 and 2 of `cases.tex` (IEEE FMLDS 2024; WWW 2024 Companion). Airbnb:
Abdool and 12 others, "Applying Embedding-Based Retrieval to Airbnb Search", arXiv 2601.06873, January 2026, a
preprint (https://arxiv.org/abs/2601.06873), and their post "Embedding-Based Retrieval for Airbnb Search" on
Airbnb's engineering blog, April 2025 (https://airbnb.tech/ai-ml/embedding-based-retrieval-for-airbnb-search/).
Grade READ for both; the source sentences are in `tools/cases_numbers.py`.

Choices made without asking:

- Etsy: he named slides one, two, four and five. Slide two is read as the data, slide three as the lists of
  numbers he described with it.
- Etsy frame 1: the search "mothers day gift" is the paper's example; the necklace listing is invented, and the
  source line says so.
- Etsy frame 2: the four rows are invented; the counts are the paper's ("more than 150 million interactions"
  from "up to 30 million users", one month of cart adds and purchases).
- Etsy frames 3 and 4: invented small integers, four per list. `tools/cases_numbers.py` computes every product,
  sum and the order, and asserts that the necklace comes first and the gift wrap, the only item with the word
  "gift", falls out of the top three. The cells are tinted by sign as in the video store (blue above 0, orange
  below, grey for 0, stronger from 2 and from -2 on), a solid tint where Codex plates otherwise hatch.
- Etsy frame 4 is built over five clicks in his order: the search's numbers, the items' numbers, one inner
  product worked out, all inner products, the sorted list with the top three as the shortlist. A click only
  adds, so the "animation" also plays in a PDF viewer.
- Etsy frame 5: the comparison is recall@100 on popular (head) searches, Table I of the paper.
- Spotify frame 1: small share bars for the 25% and 75% and the "over 70%"; he asked for diagrams on frames 2
  and 3 only.
- Spotify frame 3: bars against the production model, drawn at 100, 123.87 and 146.83.
- Airbnb frame 1: an opening sentence on what Airbnb is, and "whatever the search" for the paper's
  "query-independent score".
- Airbnb frame 2: the inputs of both networks from Sec. 4.5; the picture of homes as points is a drawing.
- Airbnb frame 3: the three versions as boxes (two networks; a clustered index; a larger network); the paper's
  phrase is quoted, the blog's sentence paraphrased.

Open items of these decks:

1. Which case goes after which block. Etsy and Airbnb are both nearest neighbours on two-tower vectors; Spotify
   fits the matchmaker. The 12:00, 14:00 and 16:00 blocks have no deck yet; candidates are in
   `git_ainit/research_notes/Business cases of the weekend 2 techniques/recent_*.md`.
2. Whether these decks replace `cases.tex`.
3. Linked from nowhere; the course site gets them only after Carlos's yes.

The sections below describe `cases.tex`, version 2 of 2026-11-04.

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

1. The deck is linked from nowhere. The course site gets it only after Carlos's yes.
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
