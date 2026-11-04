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
| 1 | Friday 08:00, after the video store | Airbnb, 2018: similar homes are nearest neighbours | Nearest neighbours on learned vectors | 32 numbers per home, learned from over 800 million search sessions; the 12 nearest neighbours. A/B test against the old similar homes: click rate of the row +21%, guests who found their booking in the row +4.9%. Cost: a new home borrows the average of 3 similar homes. Decided: learn from bookings as well as clicks, launch after an online test |
| 2 | Friday 10:00, after the matchmaker | Netflix, 2009: the prize went to factorization | Matrix factorization | 100 million ratings, 1 million dollars for 10% better guesses. On hidden ratings: 10.06%; 100+ models by 2008, most of them factorizations. Cost: public IMDb ratings matched to the anonymous data, 2 of about 50 IMDb users identified. Decided: Netflix Prize 2 cancelled after FTC privacy concerns and a lawsuit, March 2010 |
| 3 | Friday 12:00, after the bandits | Adyen, 2025: a better bandit approves more payments | Epsilon-greedy contextual bandit | 2 to 15 ways to send most payments. A/B test: +0.1% approval rate from smarter exploring, 9M more approvals a year (Adyen's estimate). Cost: exploring risks declines; the next model did 0.2% worse. Decided: contracts and card network rules remove options first |
| 4 | Friday 14:00, after gradient descent | Netflix, 2012: the winning blend did not ship | Matrix factorization learned by gradient descent | 8.43% with 107 models (2007), 10.06% with hundreds (2009). Cost: built for 100 million ratings, Netflix had more than 5 billion. Decided: ship the two strongest models; for newer methods, the offline gains did not seem worth the engineering |
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
`tools/expected.txt`. `tools/check_numbers.py` reads the 20 expected strings back from the rendered PDF.

State on 2026-11-04, after the second read: 17 pages, 0 log errors, 0 em and en dashes, no build metadata,
nothing moves between clicks, all 20 numbers found in the PDF. The last click of every frame was rendered and
read.

## Sources

Grades: READ (the primary text was read), REVIEW (only a bibliographic record or the abstract of another
version was read), SECONDARY (a press report). All read on 2026-11-04. Sites that refused automated reading
(Medium, ACM, IEEE) were read through web.archive.org copies or author copies, as noted.

| Frame | Claim | Source | Grade |
|---|---|---|---|
| 1 | 32 numbers per listing, more than 800 million search click sessions, k=12 among the listings of the same market free on the same dates, A/B test against the old Similar Listings algorithm (the search ranking for the same location, filtered on price range and listing type; Say), +21% carousel click rate and 4.9% more guests discovering the listing they booked, mean of 3 listings for a new one, 99% of bookings from search and similar listings (Say), learning from the booked listing | Grbovic, Cheng, Zhang, Yang, Siclait, Jones (Airbnb), "Listing Embeddings for Similar Listing Recommendations and Real-time Personalization in Search Ranking", The Airbnb Tech Blog, 13 March 2018, https://medium.com/airbnb-engineering/listing-embeddings-for-similar-listing-recommendations-and-real-time-personalization-in-search-601172f7603e , read at http://web.archive.org/web/20260725105017/https://medium.com/airbnb-engineering/listing-embeddings-for-similar-listing-recommendations-and-real-time-personalization-in-search-601172f7603e | READ |
| 1 | Offline tests, then online tests, before production | Grbovic and Cheng, "Real-time Personalization using Embeddings for Search Ranking at Airbnb", KDD 2018, DOI 10.1145/3219819.3219885, abstract at https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb | READ (abstract) |
| 2 | 1,000,000 USD for at least 10% better than Cinematch; more than 100 million ratings from over 480 thousand customers; the winners license their method to Netflix (Say) | Netflix Prize Rules, https://web.archive.org/web/20061105165727/http://www.netflixprize.com/rules | READ |
| 2 | 10.06% improvement, RMSE 0.8567 against 0.9525, submitted 26 July 2009, awarded 21 September 2009 | "Grand Prize awarded to team BellKor's Pragmatic Chaos", Netflix Prize forum, https://web.archive.org/web/20091228043112/http://www.netflixprize.com/community/viewtopic.php?id=1537 | READ |
| 2 | 51,051 contestants from 186 countries (Say) | Netflix Prize leaderboard, https://web.archive.org/web/20090926213457/http://www.netflixprize.com/leaderboard | READ |
| 2 | Cinematch is a correlation between films, a neighbour method (Say) | Bennett and Lanning, "The Netflix Prize", KDD Cup and Workshop 2007, https://www.cs.uic.edu/~liub/KDD-cup-2007/proceedings/The-Netflix-Prize-Bennett.pdf | READ |
| 2 | "more than 100 different predictor sets, the majority of which are factorization models", said of the team's winning entries up to the 2008 Progress Prize (8.43% in 2007, 9.46% in 2008), written before the final entry | Koren, Bell, Volinsky, "Matrix Factorization Techniques for Recommender Systems", IEEE Computer 42(8), 2009, DOI 10.1109/MC.2009.263, read in the author copy https://web.archive.org/web/20110401191222/http://www2.research.att.com/~volinsky/papers/ieeecomputer.pdf | READ |
| 2 | The records of 2 users found in the Netflix data from the public IMDb ratings of "around 50 IMDb users", a "proof of concept"; for one of them, political and religious views (Say) | Narayanan and Shmatikov, "Robust De-anonymization of Large Sparse Datasets", IEEE Symposium on Security and Privacy 2008, pp. 111-125, DOI 10.1109/SP.2008.33, authors' copy https://www.cs.cornell.edu/~shmat/shmat_oak08netflix.pdf ; preprint https://arxiv.org/abs/cs/0610105 , listed as "How To Break Anonymity of the Netflix Prize Dataset" (its version 2 PDF is titled "Robust De-anonymization of Large Datasets") | READ |
| 2 | The sequel (Prize 2) dropped after the FTC's question and the KamberLaw lawsuit; the lawsuit settled (Say) | Neil Hunt, "Netflix Prize Update", Netflix blog, 12 March 2010, https://web.archive.org/web/20110104112307/http://blog.netflix.com/2010/03/this-is-neil-hunt-chief-product-officer.html | READ |
| 2 | FTC staff's concerns about Prize 2, the risk of re-identification first; any future data only to researchers who agree by contract to limits on its use (Say) | FTC, closing letter to Netflix's counsel, 12 March 2010, https://www.ftc.gov/sites/default/files/documents/closing_letters/netflix-inc./100312netflixletter.pdf , read at http://web.archive.org/web/20250713123753/https://www.ftc.gov/sites/default/files/documents/closing_letters/netflix-inc./100312netflixletter.pdf | READ |
| 3 | Production policy epsilon-greedy with a boosting model; typically 2 to 15 actions per payment after the rule and risk filters, median 4; 5% of live traffic per variant, four weeks for the main comparison (two variants ran one week, Table 3); +0.1% for the best SquareCB variant over epsilon-greedy, an estimated 9 million more authorised transactions a year; 87.4% and 93.5% positive rewards, "correlates with a 0.2% performance regression", a drop the caption of Figure 10 attributes to the imbalance; contracts, card network rules and amount thresholds filter the actions, fraud risk prunes them; retrained every 7 days (Say) | Vangara and Egg (Adyen), "Contextual Bandits in Payment Processing: Non-uniform Exploration and Supervised Learning", OARS workshop at KDD 2025, https://arxiv.org/abs/2412.00569 (version 2) | READ |
| 3 | The options (3D Secure, card update, message format, instant retry); the bandit replaced A/B tests per account and bank, whose groups got too small as payment features were added and which had to be rerun when the world changed (Say) | van Rooijen (Adyen), "Optimizing payment conversion rates with contextual multi-armed bandits", Adyen Knowledge Hub, 2 November 2020, https://www.adyen.com/knowledge-hub/optimizing-payment-conversion-rates-with-contextual-multi-armed-bandits | READ |
| 4 | 8.43%, more than 2000 hours, 107 algorithms, the source code; SVD and RBM into production; built for 100 million ratings against more than 5 billion; some of the Grand Prize's new methods evaluated offline, their gains "did not seem to justify the engineering effort"; the focus had shifted, streaming being one reason (Say) | Amatriain and Basilico, "Netflix Recommendations: Beyond the 5 stars (Part 1)", The Netflix Tech Blog, 6 April 2012, https://web.archive.org/web/20130105140308/http://techblog.netflix.com/2012/04/netflix-recommendations-beyond-5-stars.html | READ |
| 4 | Offline scores only decide which A/B test follows (Say) | the same, Part 2, 20 June 2012, https://web.archive.org/web/20130115100808/http://techblog.netflix.com/2012/06/netflix-recommendations-beyond-5-stars.html | READ |
| 4 | "All models are learned by stochastic gradient descent" (Say) | Koren, "The BellKor Solution to the Netflix Grand Prize", August 2009, https://www2.seas.gwu.edu/~simhaweb/champalg/cf/papers/KorenBellKor2009.pdf | READ |
| 4 | Learning rate 0.001; a pass over 100 million ratings in about 7.5 seconds on a laptop (Say) | Funk, "Netflix Update: Try This at Home", 11 December 2006, https://sifter.org/~simon/journal/20061211.html | READ |
| 5 | Amazon: item-to-item collaborative filtering, a similar-items table of items that customers tend to buy together (cosine of item vectors over customers); recommends the items most similar to what a customer bought | Linden, Smith, York (Amazon), "Amazon.com Recommendations: Item-to-Item Collaborative Filtering", IEEE Internet Computing 7(1), 2003, pp. 76-80, DOI 10.1109/MIC.2003.1167344, copy read at https://www.cs.umd.edu/~samir/498/Amazon-Recommendations.pdf | READ |
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
4. **Cases read and not used**, all READ. Named on the map: Amazon's item-to-item filtering (no measured
   result in the paper), Pinterest PinSage (10% to 30% more repins, KDD 2018), Microsoft's Decision
   Service on MSN (more than 25% click rate over the editors' order, epsilon 33%), Spotify's home page (more
   than 20% stream rate over a static order, exploration capped at 10%), Amazon's page layout (21% over the
   median of 48 layouts), Yahoo's front page (12.5% more clicks, offline replay). Also read: Spotify Discover
   Weekly (trained by alternating least squares), Adyen AutoRescue (about 6% more orders recovered, a thin
   method) and LinkedIn job matching (+2.37% successful job search sessions, arXiv 2024).
5. **One card for every case**, four clicks, the same labels in the same places.
6. **No title page**: each frame is shown alone at the end of a lecture.
7. **The session boxes** name the video store (08:00), the matchmaker (10:00), the bandits (12:00) and
   gradient descent (14:00). The 12:00 game was not final on 2026-11-04, so its box names the subject.
8. **"9M"** on frame 3: the number column is too narrow for "9 million".
9. **None of the opener's numbers.** Netflix's 75%, in the same 2012 blog post, is left out.
10. **Amazon in place of LinkedIn on the map**, after the second read. LinkedIn's job matching answers "which
    jobs suit this member", closer to the second question, and its KDD 2024 venue is not confirmed. Amazon's
    item-to-item filtering answers the first question exactly. Amazon is named twice on the map, for two
    techniques.

## Simplifications to know when presenting

- Frame 1, "guests who found their booking here", stands for "4.9% more guests discovering the listing they
  ended up booking in the Similar Listing carousel". The control was the old Similar Listings algorithm.
- Frame 2, "100+ models by 2008, most factorizations", is BellKor's description of its winning entries up to the
  2008 Progress Prize. The final blend of 2009 held hundreds (Koren 2009 blends a set of 454 predictors).
- Frame 2, "2 of about 50 IMDb users identified": the authors call it a proof of concept that says nothing
  about the share of IMDb users who could be identified.
- Frame 2, "Netflix Prize 2": Hunt's post calls it the sequel; the FTC letter calls it Prize 2.
- Frame 3's +0.1% compares a smarter exploration rule (SquareCB) with the epsilon-greedy bandit already
  running. The paper does not say whether Adyen switched. A comparison of the bandit with the A/B tests it
  replaced (by November 2020) is published only as charts without numbers.
- Frame 3, "the next model did 0.2% worse": the text says the more imbalanced data "correlates with a 0.2%
  performance regression"; the caption of Figure 10 attributes the drop to the imbalance.
- Frame 3, "Most payments ... 2 to 15 ways": the paper's "typically", counted after the rule and risk filters.
- Frame 3, "2025" is the year of the workshop. The test ran before 30 November 2024: version 1 of the paper
  already reports it; the 9 million estimate first appears in version 2.
- Frame 4 calls the restricted Boltzmann machine "a neural network"; the Say names it once.
- Frame 4, "Newer methods: the offline gains did not seem worth the engineering": Netflix evaluated some of the
  new methods of the Grand Prize offline, and gives a second reason, its focus had moved on.
- Frame 4's 8.43% and 10.06% are both improvements over Netflix's Cinematch on hidden ratings, from two teams,
  two years apart.

## Second read

After the first commit (`b840920`) a second agent checked every claim of `cases.tex` against its source. No
number was wrong. Fixed in the next commit:

- Frame 1: "over 800 million"; "guests who found their booking here"; the Say names the A/B control, the same
  market, a 21 percent higher click rate, and the 32 numbers as a trade-off between offline results and memory.
- Frame 2: "100+ models by 2008"; "2 of about 50 IMDb users identified"; "Netflix Prize 2" after "FTC privacy
  concerns"; the FTC letter added to the sources; the Say adds the settlement, the contract-only data, the
  non-exclusive licence, "registered" contestants and Cinematch at the start as the baseline.
- Frame 3: the title "a better bandit approves more payments"; "Most payments"; "did 0.2% worse"; the Say says
  what the +0.1% compares, the main comparison's four weeks, that the paper does not say whether Adyen
  switched, and "By November 2020".
- Frame 4: "Newer methods: the offline gains"; the Say drops a quotation that was not verbatim, adds the second
  reason (the focus had moved on), names the restricted Boltzmann machine, and says "about 7.5 seconds".
- Frame 5: Amazon in place of LinkedIn (choice 10).
- `tools/cases_numbers.py`: the Adyen sentence on the 1%, 4% and 6% levels is verbatim again ("uniform
  random"); the title of the arXiv preprint is given as listed and as printed.

Not checked: the full text of Airbnb's KDD 2018 paper (ACM sent a bot challenge; every number on the slide is
from the blog); whether LinkedIn's paper appeared at KDD 2024 (Crossref has no record); whether Adyen shipped
SquareCB.

## Open items

1. The deck is linked from nowhere. The course site gets it only after Carlos's yes.
2. It has not been projected in HG D 7.2.
3. No bank or insurer was found with matrix factorization, or nearest neighbours on embeddings, and an online
   result. PicPay (a Brazilian payments app, KDD 2023) says it rejected collaborative filtering for financial
   services because purchases are rare.
4. Box of frame 3: rename to the 12:00 game when it is final.
5. No frame on Swiss or EU rules, to keep one case per lecture. Material for one, all READ, is in the
   research notes (`git_ainit/research_notes/Business cases of the weekend 2 techniques/risks_rules.md`, local
   and private):
   - The FDPIC's final report of 15 April 2024 on Digitec Galaxus (EDÖB-A-B3653401/5, in German,
     https://www.edoeb.admin.ch/dam/en/sd-web/UbgCr4c7n-cD/20240415_Schlussbericht_Galaxus.pdf ): to order,
     customers needed an account and had to accept the analysis of their shopping behaviour, with no way to
     object except to direct marketing; tying this to a mandatory account was found disproportionate; six
     recommendations, of which Digitec Galaxus accepted the sixth "without acknowledging a legal obligation" (our
     translation) and rejected 3, 4 and part of 2. The FDPIC closed the case on 12 February 2026: customers can
     now switch website personalisation off with a single click (https://www.edoeb.admin.ch/en/digitec-galaxus-en ).
   - ING (Netherlands), 2014: a trial of offers from other companies matched to customers' payments, postponed
     after criticism from the AFM, the central bank and the data protection authority. In 2019 the Dutch
     authority wrote that reusing payment data for direct marketing without consent is "probably incompatible"
     with the purpose of collection (our translation).
   - EU Digital Services Act, Article 38: very large platforms must offer, for each recommender system, at least
     one option not based on profiling.
