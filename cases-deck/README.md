# Cases deck: who uses it, and what it paid

Four business cases of the weekend 2 techniques, for AINIT HS26, Friday 13 November 2026: one case at the end
of each Friday lecture, then a map of business questions to the three techniques. Asked for on 2026-11-04,
after the BMAI HS26 evaluation, whose most repeated request (six comments, and the same in HS25 and FS26) was
real business use cases. Carlos chose the slot ("one case per lecture") and the length (10 to 15 minutes in
all) the same day.

- `cases.pdf`: the deck, 5 frames over 17 pages (the clicks).
- `cases-handout.pdf`: one page per frame, its last click.
- `case1-nearest-neighbours.pdf`, `case2-matrix-factorization.pdf`, `case3-bandits.pdf`,
  `case4-gradient-descent.pdf`: the deck cut into the four slots, clicks included. The fourth holds frames 4
  and 5.

## Frames

| # | Slot | Title | Technique | On the slide |
|---|---|---|---|---|
| 1 | Friday 08:00, after the video store | Airbnb, 2018: similar homes are nearest neighbours | Nearest neighbours on learned vectors | 32 numbers per home, learned from 800 million search sessions; the 12 nearest neighbours. A/B test: click rate of the row +21%, bookings discovered in the row +4.9%. Cost: a new home borrows the average of 3 similar homes. Decided: learn from bookings as well as clicks, launch after an online test |
| 2 | Friday 10:00, after the matchmaker | Netflix, 2009: the prize went to factorization | Matrix factorization | 100 million ratings, 1 million dollars for 10% better guesses. On hidden ratings: 10.06%; 100+ models, most of them factorizations. Cost: researchers re-identified customers through IMDb. Decided: the second prize cancelled after an FTC question and a lawsuit, March 2010 |
| 3 | Friday 12:00, after the bandits | Adyen, 2025: a bandit gets more payments approved | Epsilon-greedy contextual bandit | 2 to 15 ways to send each payment. A/B test: +0.1% approval rate from smarter exploring, 9M more approvals a year (Adyen's estimate). Cost: exploring risks declines; the next model scored 0.2% lower. Decided: contracts and card network rules remove options first |
| 4 | Friday 14:00, after gradient descent | Netflix, 2012: the winning blend did not ship | Matrix factorization learned by gradient descent | 8.43% with 107 models (2007), 10.06% with hundreds (2009). Cost: built for 100 million ratings, Netflix had more than 5 billion. Decided: ship the two strongest models, not the winning blend |
| 5 | Friday 14:00 | Which technique answers which question | All three | Three business questions, the technique for each, this weekend's case and other companies that use it |

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
source, asserts the Netflix arithmetic (10.06% = 1 - 0.8567 / 0.9525), and writes `numbers.tex` and
`tools/expected.txt`. `tools/check_numbers.py` reads the 19 expected strings back from the rendered PDF.

State on 2026-11-04: 17 pages, 0 log errors, 0 em and en dashes, no build metadata, nothing moves between
clicks, all 19 numbers found in the PDF. The last click of every frame was rendered and read.

## Sources

Grades: READ (the primary text was read), REVIEW (only a bibliographic record or the abstract of another
version was read), SECONDARY (a press report). All read on 2026-11-04. Sites that refused automated reading
(Medium, ACM, IEEE) were read through web.archive.org copies or author copies, as noted.

| Frame | Claim | Source | Grade |
|---|---|---|---|
| 1 | 32 numbers per listing, 800 million search click sessions, k=12, A/B test +21% carousel click rate and 4.9% more guests discovering the listing they booked, mean of 3 listings for a new one, 99% of bookings from search and similar listings (Say), learning from the booked listing | Grbovic, Cheng, Zhang, Yang, Siclait, Jones (Airbnb), "Listing Embeddings for Similar Listing Recommendations and Real-time Personalization in Search Ranking", The Airbnb Tech Blog, 13 March 2018, https://medium.com/airbnb-engineering/listing-embeddings-for-similar-listing-recommendations-and-real-time-personalization-in-search-601172f7603e , read at http://web.archive.org/web/20260725105017/https://medium.com/airbnb-engineering/listing-embeddings-for-similar-listing-recommendations-and-real-time-personalization-in-search-601172f7603e | READ |
| 1 | Offline tests, then online tests, before production | Grbovic and Cheng, "Real-time Personalization using Embeddings for Search Ranking at Airbnb", KDD 2018, DOI 10.1145/3219819.3219885, abstract at https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb | READ (abstract) |
| 2 | 1,000,000 USD for at least 10% better than Cinematch; more than 100 million ratings from over 480 thousand customers; the winners license their method to Netflix (Say) | Netflix Prize Rules, https://web.archive.org/web/20061105165727/http://www.netflixprize.com/rules | READ |
| 2 | 10.06% improvement, RMSE 0.8567 against 0.9525, submitted 26 July 2009, awarded 21 September 2009 | "Grand Prize awarded to team BellKor's Pragmatic Chaos", Netflix Prize forum, https://web.archive.org/web/20091228043112/http://www.netflixprize.com/community/viewtopic.php?id=1537 | READ |
| 2 | 51,051 contestants from 186 countries (Say) | Netflix Prize leaderboard, https://web.archive.org/web/20090926213457/http://www.netflixprize.com/leaderboard | READ |
| 2 | Cinematch is a correlation between films, a neighbour method (Say) | Bennett and Lanning, "The Netflix Prize", KDD Cup and Workshop 2007, https://www.cs.uic.edu/~liub/KDD-cup-2007/proceedings/The-Netflix-Prize-Bennett.pdf | READ |
| 2 | "more than 100 different predictor sets, the majority of which are factorization models" | Koren, Bell, Volinsky, "Matrix Factorization Techniques for Recommender Systems", IEEE Computer 42(8), 2009, DOI 10.1109/MC.2009.263, read in the author copy https://web.archive.org/web/20110401191222/http://www2.research.att.com/~volinsky/papers/ieeecomputer.pdf | READ |
| 2 | Netflix records of known users identified through IMDb | Narayanan and Shmatikov, "How To Break Anonymity of the Netflix Prize Dataset", https://arxiv.org/abs/cs/0610105 (abstract read); published as "Robust De-anonymization of Large Sparse Datasets", IEEE Symposium on Security and Privacy 2008, pp. 111-125, DOI 10.1109/SP.2008.33 (Crossref and Semantic Scholar records read) | READ (arXiv), REVIEW (S&P 2008) |
| 2 | Second prize dropped after the FTC's question and the KamberLaw lawsuit | Neil Hunt, "Netflix Prize Update", Netflix blog, 12 March 2010, https://web.archive.org/web/20110104112307/http://blog.netflix.com/2010/03/this-is-neil-hunt-chief-product-officer.html | READ |
| 3 | Production policy epsilon-greedy with a boosting model; 2 to 15 actions per payment, median 4; 5% of live traffic per variant, four weeks; +0.1% for SquareCB over epsilon-greedy, an estimated 9 million more authorised transactions a year; 87.4% and 93.5% positive rewards, "correlates with a 0.2% performance regression"; contracts, card network rules and amount thresholds filter the actions, fraud risk prunes them; retrained every 7 days (Say) | Vangara and Egg (Adyen), "Contextual Bandits in Payment Processing: Non-uniform Exploration and Supervised Learning", OARS workshop at KDD 2025, https://arxiv.org/abs/2412.00569 (version 2) | READ |
| 3 | The options (3D Secure, card update, message format, instant retry); the bandit replaced A/B tests per account and bank | van Rooijen (Adyen), "Optimizing payment conversion rates with contextual multi-armed bandits", Adyen Knowledge Hub, 2 November 2020, https://www.adyen.com/knowledge-hub/optimizing-payment-conversion-rates-with-contextual-multi-armed-bandits | READ |
| 4 | 8.43%, more than 2000 hours, 107 algorithms, the source code; SVD and RBM into production; built for 100 million ratings against more than 5 billion; the Grand Prize ensemble's gains "did not seem to justify the engineering effort" | Amatriain and Basilico, "Netflix Recommendations: Beyond the 5 stars (Part 1)", The Netflix Tech Blog, 6 April 2012, https://web.archive.org/web/20130105140308/http://techblog.netflix.com/2012/04/netflix-recommendations-beyond-5-stars.html | READ |
| 4 | Offline scores only decide which A/B test follows (Say) | the same, Part 2, 20 June 2012, https://web.archive.org/web/20130115100808/http://techblog.netflix.com/2012/06/netflix-recommendations-beyond-5-stars.html | READ |
| 4 | "All models are learned by stochastic gradient descent" (Say) | Koren, "The BellKor Solution to the Netflix Grand Prize", August 2009, https://www2.seas.gwu.edu/~simhaweb/champalg/cf/papers/KorenBellKor2009.pdf | READ |
| 4 | Learning rate 0.001; a pass over 100 million ratings in about 7.5 seconds on a laptop (Say) | Funk, "Netflix Update: Try This at Home", 11 December 2006, https://sifter.org/~simon/journal/20061211.html | READ |
| 5 | LinkedIn: job matching by the inner product of a query vector and job vectors | Shen and others, "Learning to Retrieve for Job Matching", KDD 2024, https://arxiv.org/abs/2402.13435 | READ |
| 5 | Pinterest: related pins are the nearest neighbours of a pin's vector | Ying and others, "Graph Convolutional Neural Networks for Web-Scale Recommender Systems", KDD 2018, https://arxiv.org/abs/1806.01973 | READ |
| 5 | Spotify: implicit matrix factorization, Discover Weekly | Johnson, "Algorithmic Music Discovery at Spotify", slides, 13 January 2014, https://web.archive.org/web/20160112235452/http://www.slideshare.net/MrChrisJohnson/algorithmic-music-recommendations-at-spotify ; Johnson and Newett, "From Idea to Execution: Spotify's Discover Weekly", slides, November 2015, https://web.archive.org/web/20161221213105/http://www.slideshare.net/MrChrisJohnson/from-idea-to-execution-spotifys-discover-weekly | READ (transcripts) |
| 5 | Yahoo: contextual bandit (LinUCB) for the front page | Li, Chu, Langford, Schapire, "A Contextual-Bandit Approach to Personalized News Article Recommendation", WWW 2010, https://arxiv.org/abs/1003.0146 | READ |
| 5 | Microsoft: Decision Service, epsilon-greedy on MSN | Agarwal and others, "Making Contextual Decisions with Low Technical Debt", https://arxiv.org/abs/1606.03966 (no published venue found) | READ |
| 5 | Spotify: epsilon-greedy bandit for the home page | McInerney and others, "Explore, Exploit, and Explain: Personalizing Explainable Recommendations with Bandits", RecSys 2018, DOI 10.1145/3240323.3240354, author copy http://www.jamesmc.com/s/BartRecSys.pdf | READ |
| 5 | Amazon: Thompson sampling bandit for a page layout | Hill and others, "An Efficient Bandit Algorithm for Realtime Multivariate Optimization", KDD 2017, https://arxiv.org/abs/1810.09558 | READ |

## Choices made without asking

1. **10 to 15 minutes in all**, read as about 2.5 minutes per case and 1 minute for the map.
2. **The cases.** Airbnb has the clearest A/B result for nearest neighbours on learned vectors. The Netflix
   Prize is the best known matrix factorization case and gives the failure case the brief asked for. Adyen is
   the only finance case found with a primary source and a measured result, and runs epsilon-greedy, the rule
   taught at 12:00. Netflix 2012 is the clearest case of cost against accuracy.
3. **Netflix twice, on purpose**: the prize at 10:00, what shipped at 14:00, so the second Netflix frame needs
   no new setting.
4. **Cases read and not used**, all READ and named on the map: LinkedIn job matching (+2.37% successful job
   search sessions, KDD 2024), Pinterest PinSage (10% to 30% more repins, KDD 2018), Microsoft's Decision
   Service on MSN (more than 25% click rate over the editors' order, epsilon 33%), Spotify's home page (more
   than 20% stream rate over a static order, exploration capped at 10%), Amazon's page layout (21% over the
   median of 48 layouts), Yahoo's front page (12.5% more clicks, offline replay). Also read: Spotify Discover
   Weekly (trained by alternating least squares) and Adyen AutoRescue (about 6% more orders recovered, a thin
   method).
5. **One card for every case**, four clicks, the same labels in the same places.
6. **No title page**: each frame is shown alone at the end of a lecture.
7. **The session boxes** name the video store (08:00), the matchmaker (10:00), the bandits (12:00) and
   gradient descent (14:00). The 12:00 game was not final on 2026-11-04, so its box names the subject.
8. **"9M"** on frame 3: the number column is too narrow for "9 million".
9. **None of the opener's numbers.** Netflix's 75%, in the same 2012 blog post, is left out.

## Simplifications to know when presenting

- Frame 1, "bookings discovered in this row", stands for "4.9% more guests discovering the listing they ended
  up booking in the Similar Listing carousel".
- Frame 2, "100+ models, most of them factorizations", is BellKor's description of its own winning entries.
- Frame 2 cites the S&P 2008 paper; the claim was read in the abstract of its arXiv version.
- Frame 3's +0.1% compares a smarter exploration rule (SquareCB) with epsilon-greedy. A comparison of the
  bandit with the A/B tests it replaced (2020) is published only as charts without numbers.
- Frame 3, "the next model scored 0.2% lower": the paper says the more imbalanced data "correlates with a 0.2%
  performance regression", without claiming the cause.
- Frame 4 calls the restricted Boltzmann machine "a neural network".
- Frame 4's 8.43% and 10.06% are both improvements over Netflix's Cinematch on hidden ratings, from two teams,
  two years apart.

## Open items

1. The deck is linked from nowhere. The course site gets it only after Carlos's yes.
2. It has not been projected in HG D 7.2.
3. No bank or insurer was found with matrix factorization, or nearest neighbours on embeddings, and an online
   result. PicPay (a Brazilian payments app, KDD 2023) says it rejected collaborative filtering for financial
   services because purchases are rare.
4. Box of frame 3: rename to the 12:00 game when it is final.
5. No frame on Swiss or EU rules, to keep one case per lecture. A case ready for one, READ in the FDPIC's
   final report of 15 April 2024 on Digitec Galaxus (EDÖB-A-B3653401/5, in German,
   https://www.edoeb.admin.ch/dam/en/sd-web/UbgCr4c7n-cD/20240415_Schlussbericht_Galaxus.pdf ): to order, customers
   needed an account and had to accept the analysis of their shopping behaviour, with no way to object except
   to direct marketing; the investigation ran from 15 February 2021; the FDPIC found that the profiles allow
   an assessment of essential aspects of personality, as in "high-risk profiling" under the new law (left
   open, because the old law applied), and made six recommendations, the sixth a guest checkout as a
   proportionate way out. Digitec Galaxus accepted the sixth "without acknowledging a legal obligation" (our
   translation), said it had already anticipated recommendations 1, 5 and part of 2, and rejected 3, 4 and
   the rest of 2.
