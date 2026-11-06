#!/usr/bin/env python3
"""cases_numbers.py: writes numbers.tex, the macros for every number on the slides of the cases deck.

Run from cases-deck/:   python3 tools/cases_numbers.py

No number is typed into cases.tex. Each one is defined here next to the sentence of its source, read
on 4 November 2026. Every number is measured or stated by its source; none is invented. Since the same
day every case is a result published in 2021 or later (Carlos: "Results should be latest from 2021").
README.md lists the sources with links and grades.
"""
from pathlib import Path

macros = []          # (name, text) for numbers.tex
expect = []          # strings tools/check_numbers.py must find in the rendered PDF


def num(name, text, on_slide=None):
    """Define \\<name> as text. on_slide is the string the PDF must contain, if the number is shown."""
    macros.append((name, text))
    if on_slide:
        expect.append(on_slide)


# ===== CASE 1, Friday 08:00, nearest neighbours: Etsy, search candidates by inner product, 2024 =====
# Jha, Subramaniyam, Benjamin, Taula (Etsy), "Unified Embedding Based Personalized Retrieval in Etsy Search", 2024 IEEE
# International Conference on Future Machine Learning and Data Science (FMLDS), Sydney, pp. 258-264, DOI
# 10.1109/FMLDS63805.2024.00055 (Crossref); preprint arXiv 2306.04833, v1 7 June 2023 (already with both A/B numbers),
# v2 25 September 2024 (https://arxiv.org/abs/2306.04833), read in full:
#   "Our personalized retrieval model significantly improves the overall search experience, as measured by a 5.58%
#    increase in search purchase rate and a 2.63% increase in site-wide conversion rate, aggregated across multiple
#    A/B tests - on live traffic." (abstract)
#   "We evaluated the effectiveness of our system by deploying it online and conducting A/B tests on live Etsy
#    traffic. Our evaluation focused on two important metrics: the relative change in site-wide conversion rate (CVR)
#    and the organic search purchase rate (OSPR). [...] On aggregate, our UEPPR system improved CVR by 2.63% and OSPR
#    by 5.58%." (Sec. VI.C)
#   "to find products of interest among more than 100 million vintage, handmade and craft items" and "an initial
#    candidate retrieval stage which selects several thousand items from our catalog based on the search query and
#    user context" (Sec. I)
#   "Historically, candidate retrieval has been powered by lexical matching engines" (Sec. I) and "Within Etsy, our
#    inverted index candidate retrieval system associates products with a query-independent "quality score""
#    (Sec. IV, present tense, beside the new ANN-based retrieval). Hence the title "nearest neighbours join keyword
#    search"; the paper does not say that the new retrieval replaced the inverted index.
#   "We implement additive boosting within ANN-based semantic retrieval by enriching our model-derived product
#    vectors with additional numerical features and add corresponding feature weights to query vectors. [...] We then
#    model candidate score as S(q', p') = dot(p', q') = dot(p, q) + dot(f(p), w). For serving, we simply index
#    hydrated product vectors rather than original product embeddings, and query our index with a hydrated query
#    vector." (Sec. IV); the quality score "can account for properties such as high product rating, product freshness,
#    and shop conversion rate" (Sec. IV)
#   Table I, Recall@100 on head queries: BM25 (keyword search) 0.63, Base (a shallow, symmetric two-tower model, the
#    baseline embedding model) 0.32, UEPPR boost 0.72. "our best non-personalized models are better at tail despite
#    being worse at head queries. Adding personalization to query tower help performance on head queries significantly
#    making it competitive with other methods." (Sec. VI.B)
#   "We use MirroredStrategy to train model on 4 A100 GPUs and it takes about 72 hours for the model to converge."
#    (Sec. VI.A)
#   "Recently, we transitioned to using the 4-bit product quantizer based fastscan index in Faiss [...] Although this
#    index had lower recall on its own, we achieved improved results by incorporating a re-ranking step after fetching
#    5 times the required K. We were able to achieve a recall loss of less than 4% while keeping our P99 latency under
#    20ms in production." (Sec. V), in the bullet on the ANN index; "The P99 inference latency for UEPPR boost is
#    18ms." and "low-latency (tens of milliseconds) candidate retrieval" (Sec. V). Hence "lookups within 20 ms".
#   "static quality features like shop popularity" (Sec. IV, the features appended to the vectors). Hence "such as
#    its shop's popularity" in the Say; rating is the keyword engine's example.
ETSY = {"cvr_pct": 2.63, "ospr_pct": 5.58, "items_million": 100, "head_base": 0.32, "head_bm25": 0.63,
        "head_final": 0.72, "gpus": 4, "train_hours": 72, "recall_loss_pct": 4, "p99_ms": 20, "fetch_factor": 5}
assert ETSY["head_final"] > ETSY["head_bm25"] > ETSY["head_base"]
num("etCvr", "%.2f" % ETSY["cvr_pct"], "+%.2f%%" % ETSY["cvr_pct"])
num("etOspr", "%.2f" % ETSY["ospr_pct"], "+%.2f%%" % ETSY["ospr_pct"])
num("etItems", "%d" % ETSY["items_million"])                                # Say only
num("etHeadBase", "%d" % round(100 * ETSY["head_base"]), "%d%% of the products bought" % round(100 * ETSY["head_base"]))
num("etHeadBM", "%d" % round(100 * ETSY["head_bm25"]), "keyword search %d%%" % round(100 * ETSY["head_bm25"]))
num("etGpus", "%d" % ETSY["gpus"])                                          # Say only
num("etHours", "%d" % ETSY["train_hours"])                                  # Say only
num("etLoss", "%d" % ETSY["recall_loss_pct"], "under %d%%" % ETSY["recall_loss_pct"])
num("etMs", "%d" % ETSY["p99_ms"], "%d ms" % ETSY["p99_ms"])


# ===== CASE 2, Friday 10:00, matrix factorization: Spotify, audiobook recommendations, 2024 =====
# De Nadai, Fabbri, Gigioli, Wang, Li, Silvestri, Kim, Lin, Radosavljevic, Ghael, Nyhan, Bouchard,
# Lalmas-Roelleke, Damianou (Spotify), "Personalized Audiobook Recommendations at Spotify Through Graph Neural
# Networks", Companion Proceedings of the ACM Web Conference 2024 (WWW '24 Companion, Industry Track), pp. 403-412,
# DOI 10.1145/3589335.3648339; arXiv 2403.05185 v1 (https://arxiv.org/abs/2403.05185), read in full:
#   "This experiment involved a sample of 11.5 million monthly active users, who were randomly divided into three
#    groups. The first one was exposed to the model currently in production, the second group received
#    recommendations generated by a 2T model, while the third one from the 2T-HGNN model." (Sec. 5.3)
#   Table 5, "Online A/B test results": 2T, stream rate "Neutral", new audiobooks start rate "+23.87%"; 2T-HGNN,
#    stream rate "+25.82%", new audiobooks start rate "+46.83%". The abstract and Sec. 1 say "+46%" and "+23%"
#    for the stream rate, which does not match Table 5's +25.82%; the slide shows only the start rate.
#   "The focus of the experiment is "Audiobook for you", a section of the Spotify home page that shows the top k
#    audiobooks personalized recommendations." (Sec. 5.3)
#   "The output of each tower is a 128-dimensional vector." (Sec. 4.3.1)
#   "2T-HGNN generates daily user and audiobook vectors, where the audiobook vectors o_u are close in dot product
#    distance to users that they will be recommended to." (Sec. 4.3)
#   "nodes represent audiobooks and podcasts and are connected by an edge whenever at least one user streams both"
#    (Sec. 1)
#   "Early empirical assessments show that over 70% of initial audiobook consumers had previously engaged with
#    podcasts." (Sec. 3)
#   "approximately 25% of users account for 75% of all streaming hours" (Sec. 3); Figure 2 caption: "The audiobook
#    consumption at launch is very sparse." Hence "three quarters of the audiobook hours" in the Say.
#   "Audiobooks were initially launched using a direct-sales strategy, requiring users to purchase an audiobook
#    before it could be streamed." (Sec. 3) and "Secondly, users encounter a paywall when attempting to access the
#    content" (Sec. 3). Hence "at launch each audiobook had to be bought".
#   "Other than GNN embeddings, the user tower uses demographic features (age and country) as well as interaction
#    features (audiobook, podcast, artist) [...] The audiobook tower uses metadata features (i.e. language and BISAC
#    genre code) and LLM embeddings of the title and description" (Sec. 4.3.1). Hence the Say: two networks compute
#    the numbers, from what people streamed and from each book's description.
#   "We compare the performance of audiobook recommendations for warmstart and coldstart users [...] the latter are
#    those who never interacted with an audiobook before." (Sec. 5.2.2) Hence "users new to audiobooks".
#   Table 3, coldstart users, Coverage: 2T "19.3%", 2T-HGNN "12.0%"; "its recommendations are limited to a
#    narrower subset of the catalog. We do not consider this thade-off as a major issue at the moment, but
#    something to be eventually re-consider in the future." (Sec. 5.2.2, spelling as printed)
#   "The model is since then in production, exposed to all eligible audiobooks Spotify users." (Sec. 1)
#   "We tested the 2T model as a competitive alternative to the 2T-HGNN." (Sec. 5.3)
SPOTIFY = {"test_users_million": 11.5, "groups": 3, "start_pct": 46.83, "start_plain_pct": 23.87, "dims": 128,
           "from_podcasts_pct": 70, "heavy_users_pct": 25, "heavy_hours_pct": 75, "cover_new_pct": 12.0,
           "cover_plain_pct": 19.3}
num("spUsers", "%.1f" % SPOTIFY["test_users_million"], "%.1fM" % SPOTIFY["test_users_million"])
num("spGroups", "%d" % SPOTIFY["groups"])                                  # Say only
num("spStart", "%.1f" % SPOTIFY["start_pct"], "+%.1f%%" % SPOTIFY["start_pct"])
num("spStartPlain", "%.1f" % SPOTIFY["start_plain_pct"])                   # Say only
num("spDims", "%d" % SPOTIFY["dims"], "%d numbers" % SPOTIFY["dims"])
num("spFromPodcasts", "%d" % SPOTIFY["from_podcasts_pct"])                 # Say only
num("spHeavyUsers", "%d" % SPOTIFY["heavy_users_pct"])                     # Say only
num("spHeavyHours", "%d" % SPOTIFY["heavy_hours_pct"])                     # Say only
num("spCoverNew", "%.1f" % SPOTIFY["cover_new_pct"], "%.1f%%" % SPOTIFY["cover_new_pct"])
num("spCoverPlain", "%.1f" % SPOTIFY["cover_plain_pct"], "%.1f%%" % SPOTIFY["cover_plain_pct"])


# ===== CASE 3, Friday 12:00, bandits: Adyen, how to send each payment, 2025 =====
# Vangara and Egg (Adyen), "Contextual Bandits in Payment Processing: Non-uniform Exploration and Supervised
# Learning", Companion Proceedings of KDD '25: Online and Adaptive Recommender Systems (OARS '25), Toronto,
# August 2025; arXiv 2412.00569 v2 (https://arxiv.org/abs/2412.00569), read in full:
#   "Currently, [pi] is [epsilon]-greedy, using a boosting model during exploitation."
#   "its linear regret due to the reliance on uniform random exploration is an expensive trade off."
#   "This process typically produced |A_t| in [2, 15] actions per transaction, with median 4 actions." (after
#    the rule-based filtering and the risk-based pruning quoted below, hence "Most payments" on the slide)
#   "Both policies are A/B tested by routing 5% of the live traffic to each variant over a four-week period."
#   "The baseline uniform random [epsilon]-greedy policies were set at three levels of exploration: 1%, 4%, and
#    6%. Each variant received 5% of the total traffic to ensure a fair comparison. We conducted experiments
#    over a four-week period."
#   Table 3: Oracle 1, 5% of traffic, 4 weeks; Oracles 2 and 3, 5%, 1 week; [epsilon]-greedy, 5%, 4 weeks.
#    Hence "in the main comparison" in the Say.
#   "Figure 2 shows that the best-performing SquareCB variant achieved a +0.1% uplift over the baseline
#    [epsilon]-greedy policy within the four-week test period. This improvement translates to an estimated
#    9 million incremental authorized transactions per year. The confidence intervals (95%) indicate that
#    the improvement is statistically significant."
#   "bandit feedback from the baseline [epsilon]-greedy policies exhibits a class imbalance of approximately
#    87.4% positive rewards. Under the SquareCB regime, this imbalance increases to 93.5%, which correlates
#    with a 0.2% performance regression (see Figure 10)."
#   Caption of Figure 10: "The performance drop in the SquareCB-based training data is attributed to an increased
#    imbalance between positive and negative labels." Hence "did 0.2% worse" on the slide.
#   "(1) Rule-based Filtering: Remove actions that conflict with predefined constraints, such as: Merchant
#    payment service provider contracts, Card network regulations (e.g., country restrictions imposed by
#    Visa/MasterCard), Transaction amount thresholds. (2) Risk-based Pruning: Exclude actions considered
#    high-risk based on: Historical fraud rates [...]"
#   "Training required approximately 4 hours per model on 32 CPU cores, with periodic retraining every 7 days"
#   "Various interventions, conditioned on context, can be applied at payment-time to boost transaction
#    authorization rates" (Sec. 1)
# Egg (Adyen), "Off-policy Evaluation for Payments at Adyen", arXiv 2501.10470 v1, 15 January 2025, read in full:
#   "These systems operate by suggesting interventions at the time of payment, such as adjusting logic or
#    modifying transaction metadata, to improve the likelihood of successful authorization." (Sec. 1)
#   "One analysis of A/B testing practices at Adyen revealed that 58% of tests were flat or inconclusive,
#    resulting in over 20 weeks per year of wasted experimentation time." (Sec. 1)
#   "we emphasize that OPE is best used as a complementary tool alongside traditional on-policy evaluation."
#    (Sec. 8)
# Since 2026-11-04 (Carlos: results from 2021 on) the frame cites only these two 2025 papers; the 2020 blog
# post of van Rooijen is no longer used.
ADYEN = {"opt_min": 2, "opt_max": 15, "opt_median": 4, "uplift_pct": 0.1, "extra_million": 9, "traffic_pct": 5,
         "weeks": 4, "pos_eg_pct": 87.4, "pos_sq_pct": 93.5, "regress_pct": 0.2, "retrain_days": 7,
         "train_hours": 4, "cores": 32, "flat_tests_pct": 58, "weeks_lost": 20}
num("adOptMin", "%d" % ADYEN["opt_min"], "%d to %d ways" % (ADYEN["opt_min"], ADYEN["opt_max"]))
num("adOptMax", "%d" % ADYEN["opt_max"])
num("adUplift", "%.1f" % ADYEN["uplift_pct"], "+%.1f%%" % ADYEN["uplift_pct"])
num("adExtra", "%d" % ADYEN["extra_million"], "%dM" % ADYEN["extra_million"])
num("adRegress", "%.1f" % ADYEN["regress_pct"], "%.1f%% worse" % ADYEN["regress_pct"])
num("adTraffic", "%d" % ADYEN["traffic_pct"])                       # Say only
num("adWeeks", "%d" % ADYEN["weeks"])                               # Say only
num("adRetrain", "%d" % ADYEN["retrain_days"])                       # Say only
num("adFlatTests", "%d" % ADYEN["flat_tests_pct"])                   # Say only
num("adWeeksLost", "%d" % ADYEN["weeks_lost"])                       # Say only


# ===== CASE 4, Friday 14:00, gradient descent at scale: LinkedIn, large ranking models, 2024 =====
# Borisyuk, Zhou, Song, Zhu, Tiwana, Parameswaran and 28 others (LinkedIn), "LiRank: Industrial Large Scale Ranking
# Models at LinkedIn", KDD '24, Barcelona, 25 to 29 August 2024, DOI 10.1145/3637528.3671561; arXiv 2402.06859 v2
# (https://arxiv.org/abs/2402.06859), read in full:
#   "These ideas have contributed to relative metrics improvements across the board at LinkedIn: +0.5% member
#    sessions in the Feed, +1.76% qualified job applications for Jobs search and recommendations, and +4.3% for Ads
#    CTR." (abstract)
#   Table 7, "Online experiment relative metrics improvements of JS and JYMBII ranking", Qualified Application: Job
#    Search "+0.89%", JYMBII (Jobs You Might Be Interested In) "+0.87%". Sec. 5.3: "leading to relative 1.76%
#    improvement in Qualified Applications across Job Search and JYMBII". The 1.76% of the abstract is the sum of two
#    relative changes measured on two products, so the Say gives "about 0.9 percent ... in job search and in job
#    suggestions" (the second read of 2026-11-04 found the sum).
#   "We have deployed these techniques to production, and through online A/B testing, we observed a 0.5% relative
#    increase in the number of member sessions visiting LinkedIn." (Sec. 5.2)
#   "We have deployed techniques to production and observed 4.3% CTR relative improvement in online A/B tests."
#    (Sec. 5.4)
#   "LinkedIn is the world's largest professionals network with more than 1 billion members" (Sec. 1)
#   "We utilized Horovod to scale out synchronous training with multiple GPUs." (Sec. 4.1)
#   "From our benchmarks, model parallelism reduced training time from 70 hours to 20 hours." (Sec. 4.1)
#   "as Feed scaled up from using 13% of sessions for training to using 100% of sessions" (Sec. 6.1)
#   "During initial training experiments with DCNv2 we observed a large number of runs diverging. To improve model
#    training stability we increased learning rate warm-up from 5% to 50% of training steps." (Sec. 6.2)
#   "Finally, we found that at our number of training steps we were under-fitting. [...] However, increasing the
#    number of training steps was not an option for production due to the decrease in experimentation velocity. As
#    a solution, we found that given the increased warm-up steps, our training was stable enough for higher learning
#    rates. Increasing the learning rate three-fold allowed us to almost completely bridge any relevance metric gaps
#    we found compared to longer training." (Sec. 6.2)
#   "Incremental training, on the other hand, not only uses the previous model for weight initialization but also
#    leverages it to create an informative regularization term." (Sec. 3.6) Tables 4 and 5: incremental training,
#    training time "-96%" for the Feed ranking and the Ads CTR models.
#   "For identifiers with high volatility and short-lived posts, known as Root Object ID, we use a specialized
#    Root-object (RO) model. This model is trained every 8 hours with the latest data" (Sec. 3.9)
#   "Our ranking model combines a global model with billions of parameters to capture broad trends" (Sec. 3.9, a
#    section on the Feed: "improving the Feed user experience"). Hence "The feed's has billions of parameters".
LIRANK = {"sessions_pct": 0.5, "jobs_search_pct": 0.89, "jobs_suggest_pct": 0.87, "jobs_abstract_pct": 1.76,
          "ads_ctr_pct": 4.3, "members_billion": 1, "hours_before": 70,
          "hours_after": 20, "sessions_from_pct": 13, "sessions_to_pct": 100, "warmup_from_pct": 5,
          "warmup_to_pct": 50, "lr_factor": 3, "incremental_cut_pct": 96, "retrain_hours": 8}
num("liSessions", "%.1f" % LIRANK["sessions_pct"], "+%.1f%%" % LIRANK["sessions_pct"])
assert abs(LIRANK["jobs_search_pct"] + LIRANK["jobs_suggest_pct"] - LIRANK["jobs_abstract_pct"]) < 1e-9
assert round(LIRANK["jobs_search_pct"], 1) == round(LIRANK["jobs_suggest_pct"], 1) == 0.9
num("liJobs", "%.1f" % LIRANK["jobs_search_pct"])                          # Say only, "about 0.9" in both products
num("liAdsCtr", "%.1f" % LIRANK["ads_ctr_pct"], "+%.1f%%" % LIRANK["ads_ctr_pct"])
num("liMembers", "%d" % LIRANK["members_billion"])                         # Say only in cases.tex; slide of linkedin.tex
num("liHoursBefore", "%d" % LIRANK["hours_before"], "%d hours" % LIRANK["hours_before"])
num("liHoursAfter", "%d" % LIRANK["hours_after"], "%d hours" % LIRANK["hours_after"])
num("liSessFrom", "%d" % LIRANK["sessions_from_pct"])                      # Say only
num("liSessTo", "%d" % LIRANK["sessions_to_pct"])                          # Say only
num("liWarmFrom", "%d" % LIRANK["warmup_from_pct"])                        # Say only
num("liWarmTo", "%d" % LIRANK["warmup_to_pct"])                            # Say only
num("liIncCut", "%d" % LIRANK["incremental_cut_pct"])                      # Say only in cases.tex; slide of linkedin.tex
num("liRetrain", "%d" % LIRANK["retrain_hours"])                           # Say only


# ===== THE CASE DECKS OF 2026-11-06: etsy.tex (5 frames), spotify.tex (3), airbnb.tex (3) =====
# Carlos asked on 2026-11-06 for one short deck per case, the text of each slide dictated by him, with diagrams.
# Their macros join numbers.tex; the strings each PDF must show go to tools/expected-<deck>.txt.
deck_expect = {"etsy": [], "spotify": [], "airbnb": [], "spotify-home": [], "amazon": [], "linkedin": []}


def show(deck, s):
    deck_expect[deck].append(s)


# ----- Etsy: the source block of CASE 1 above, plus (same paper, Sec. VI.A, read 2026-11-06):
#   "We create our training data by mining positive interactions such as cartadds and purchases from our search
#    logs using past one month of data from across all our platforms. The dataset contains upto 30 millions users
#    and more 150 million interactions." Hence frame 2: one month, more than 150 million, up to 30 million.
#   "Specifically for queries like "mothers day gift" which are common on Etsy, retrieving relevant products just
#    based on text features can be difficult." (Sec. I) Hence the search of frames 1, 3 and 4.
#   Query-user tower inputs (Sec. III.C): the query text, the user's location, "a user's recent searches, recent
#    shop clicks, terms from recently clicked items, and tags of all-time purchased items". Product tower (Sec.
#    III.A and III.B): title, tags, category, attributes, and a graph of the queries that led to the product
#    ("over a year of search logs containing positive interactions between queries and products").
#   Table I, Recall@100 on head queries, UEPPR boost (the final model): 0.72.
ETSY_DATA = {"months": 1, "interactions_million": 150, "users_million": 30}
num("etMonths", "%d" % ETSY_DATA["months"])
num("etInteractions", "%d" % ETSY_DATA["interactions_million"])
num("etUsers", "%d" % ETSY_DATA["users_million"])
num("etHeadFinal", "%d" % round(100 * ETSY["head_final"]))
for s in ["%d million items" % ETSY["items_million"],
          "more than %d million" % ETSY_DATA["interactions_million"],
          "up to %d million users" % ETSY_DATA["users_million"],
          "%d hours" % ETSY["train_hours"], "%d GPUs" % ETSY["gpus"], "%d month" % ETSY_DATA["months"],
          "+%.2f%%" % ETSY["cvr_pct"], "+%.2f%%" % ETSY["ospr_pct"],
          "%d%%" % round(100 * ETSY["head_base"]), "%d%%" % round(100 * ETSY["head_bm25"]),
          "%d%%" % round(100 * ETSY["head_final"])]:
    show("etsy", s)

# INVENTED toy numbers for frames 3 and 4 (no source): the search "mothers day gift" and four items, three numbers
# each, small integers so that the room can multiply in its head. The script computes every product, sum and the
# order; nothing is typed in etsy.tex. Chosen so that the item with the word "gift" (gift wrap) ranks last and the
# necklace, which shares no word with the search, ranks first. Until the simplification of 2026-11-06 (Carlos:
# "too complicated", "25% simpler") there were five items of four numbers each, with a bridge print.
ET_QUERY = (2, 1, -1)
ET_ITEMS = [("Gift wrap", "W", (-1, 0, 2)), ("Flower necklace", "N", (2, 2, -1)),
            ("Photo mug", "M", (1, 1, 0)), ("Recipe board", "R", (1, 2, 0))]
ABCD = "abc"
for i, v in enumerate(ET_QUERY):
    num("etQ" + ABCD[i], "%d" % v)
scores = {}
for name, key, vec in ET_ITEMS:
    prods = [a * b for a, b in zip(ET_QUERY, vec)]
    scores[key] = sum(prods)
    num("etName" + key, name)
    for i, v in enumerate(vec):
        num("et" + key + ABCD[i], "%d" % v)
    for i, p in enumerate(prods):
        num("et" + key + "p" + ABCD[i], "%d" % p)
    num("et" + key + "sum", "%d" % scores[key])
ranked = sorted(ET_ITEMS, key=lambda it: -scores[it[1]])
assert len(set(scores.values())) == len(scores)                  # no ties, so the order is unambiguous
assert ranked[0][1] == "N"                                       # the necklace comes first
assert [it[1] for it in ranked].index("W") >= 2                  # gift wrap falls out of the top 2
for r, (name, key, vec) in enumerate(ranked):
    num("etRank" + "ABCD"[r] + "name", name)
    num("etRank" + "ABCD"[r] + "sum", "%d" % scores[key])
print("Etsy toy order:", [(it[0], scores[it[1]]) for it in ranked])

# ----- Spotify: the source block of CASE 2 above. Frame 3 draws the start rate of new audiobooks as bars
# against the production model: 100, then 100 plus each relative change of Table 5 (23.87 and 46.83).
num("spIdxPlain", "%.2f" % (100 + SPOTIFY["start_plain_pct"]))   # a bar length only
num("spIdxFull", "%.2f" % (100 + SPOTIFY["start_pct"]))          # a bar length only
# Frame 1 says the quarter and the three quarters in words since the simplification of 2026-11-06 (no bars).
for s in ["%d%%" % SPOTIFY["from_podcasts_pct"], "%d numbers" % SPOTIFY["dims"],
          "%.1f million" % SPOTIFY["test_users_million"],
          "+%.1f%%" % SPOTIFY["start_plain_pct"], "+%.1f%%" % SPOTIFY["start_pct"]]:
    show("spotify", s)

# ----- Airbnb: embedding-based retrieval for search, 2025 blog and 2026 paper -----
# Abdool, Banerjee, Paul, Kim, Liu, Xu, Yu, Gao, Ouyang, Gao, He, Moyerman, Katariya (Airbnb), "Applying
# Embedding-Based Retrieval to Airbnb Search", arXiv 2601.06873 v1, 11 January 2026 (a preprint, no peer review;
# https://arxiv.org/abs/2601.06873), read in full on 2026-11-06:
#   "popular search locations can have around a hundred thousand available homes" (abstract)
#   "Retrieval/Candidate Selection Model (Leaf Service): A low-latency model which can evaluate and filter tens of
#    thousands of homes. The top K results are sent to the next stage." (Sec. 2)
#   "Baseline: Our legacy system which uses a simple linear model to generate a query-independent score for all
#    listings daily." (Sec. 6.1) Hence "scored every home once a day, whatever the search".
#   "A key technical decision is that we designed the features used in the listing tower such that it could be
#    computed entirely in an daily offline batch job. In this way, we only need to compute the query tower at
#    inference time" (Sec. 4.5)
#   Listing features: "aggregations based on historical engagement such as past views, wishlists, and reviews" and
#    "amenities, location (S2Cell IDs of various resolutions), and guest capacity" (Sec. 4.5). Query features:
#    "the location [...], number of guests, and geographic size of the search location" (Sec. 4.5 and 5)
#   V1: "two-tower EBR model [...] with a pointwise loss function and inner product similarity. We do not use any
#    ANN solutions here and instead take a union of the top results from the baseline model and the new EBR model
#    scores." V2: "Same strategy as the V1 system but the EBR model now uses an IVF solution to reduce runtime and
#    compute costs." V3: "an updated EBR model which now includes more features, larger network size (20% more
#    parameters) and a pairwise loss function with Euclidean distance." (Sec. 6.1) IVF, Sec. 5.4: "an offline
#    k-means clustering stage in our offline data pipeline that ran daily after the listing embeddings are
#    re-computed" and nprobes "defines the number of closest clusters (to the query embedding) to retrieve
#    listings from". Hence "join the shortlist" (a union) and "clustered index".
#   "We conducted online A/B tests for each of the three major versions mentioned above. In total, the successive
#    launches of these three retrieval systems yielded a combined relative 0.31% increase in conversion gains and
#    the V3 system is currently in production. This conversion gain is a large portion of the team's annual goal
#    and is on par with recent major innovations" (Sec. 6.3)
#   "when adopting IVF as an ANN solution in the V2 system, we were able to yield a reduction in compute resources
#    of around 16% relative to the baseline system." (Sec. 6.3)
#   "for email promotional campaigns specifically, our A/B test yielded +2.3% bookings from email promotions"
#    (Sec. 6.3)
# Abdool and 12 others (Airbnb), "Embedding-Based Retrieval for Airbnb Search", Airbnb Engineering and Data Science
# blog, 1 April 2025 (https://airbnb.tech/ai-ml/embedding-based-retrieval-for-airbnb-search/), read 2026-11-04:
#   "the bookings lift from this new retrieval system was on par with some of the largest machine learning
#    improvements to our search ranking in the past two years."
AIRBNB = {"conv_pct": 0.31, "email_pct": 2.3, "compute_cut_pct": 16, "versions": 3, "years": 2}
num("abConv", "%.2f" % AIRBNB["conv_pct"])
num("abEmail", "%.1f" % AIRBNB["email_pct"])
num("abCompute", "%d" % AIRBNB["compute_cut_pct"])
num("abYears", "%d" % AIRBNB["years"])                      # "the past two years", in words on the slide
for s in ["+%.2f%%" % AIRBNB["conv_pct"], "+%.1f%%" % AIRBNB["email_pct"], "%d%%" % AIRBNB["compute_cut_pct"]]:
    show("airbnb", s)


# ===== THE BANDIT AND ADVERTISING CASE DECKS, 2026-11-06 (evening): spotify-home.tex, amazon.tex, linkedin.tex =====
# Carlos chose three of eight candidates ("Spotify, Amazon Payments, and LinkedIn Lirank") and asked: "Produce the
# slides, follow the style from the slides for the matrix factorization part". Read as the Spotify audiobooks deck
# (spotify.tex, the case after the 10:00 matrix factorization block): three frames, the problem, the method as a
# diagram tied to the block's game, the value as an A/B test. The quotes and locators of all three are also in
# git_ainit/research_notes/Business cases of the weekend 2 techniques/chosen_bandit_and_ads_cases.md.

# == Spotify's home page: a contextual bandit chooses the mix of music and podcasts, 2025 ==
# Feijer, Abdollahpouri, Gupta, Clare, Wen, Wasson, Dimakopoulou, Nazari, Kretschman, Lalmas (Spotify, NYU, Uber),
# "Calibrated Recommendations with Contextual Bandits", CONSEQUENCES workshop at ACM RecSys 2025 (arXiv comment:
# "Accepted at ACM RecSys '25, CONSEQUENCES workshop"); arXiv 2509.05460 v1, 5 September 2025
# (https://arxiv.org/abs/2509.05460), read in full on 2026-11-06:
#   "Spotify's Home page features a variety of content types, including music, podcasts, and audiobooks. However,
#    historical data is heavily skewed toward music" and "users' preference towards different content types may vary
#    depending on the time of day, the day of week, or even the device they use." (abstract)
#   "A widely used approach in industry for diversifying recommendations based on user preferences is calibration"
#    and "These calibration techniques aim to align the composition of recommendation sets with the historical
#    distribution of content types consumed by the user." (Sec. 1) Hence "The usual rule gives each user the mix of
#    their past listening"; the paper does not say which rule ran before the bandit.
#   "We conducted an online A/B test in which the control variant was the 90-day SC" (Sec. 3.2); SC is "Steck's
#    calibration approach", the target "computed based on [...] long-term (last 90 days) historical user preferences"
#    (Sec. 3.1). Hence the control group "The mix of the last 90 days".
#   "the content type of each shelf include music or podcast" (Sec. 3, the evaluations)
#   "Spotify's Home page construction for more than 600 Million users" (Sec. 2.2.3). Hence "Over 600 million users
#    of the home page"; the paper does not say how many of them get the bandit's mix.
#   "Select a content-type probability distribution p_k from a discrete set P" (Sec. 2.2). P is not listed, so the
#    three mixes of frame 2 and their estimates are INVENTED, and the slide says so.
#   "r_k = 1 if the user u_k engages with (e.g. streams) any shelf i in I_k, and 0 otherwise" (Sec. 2.2). Hence "the
#    chance of a stream from the page", the tap of the mirror game.
#   "a fully connected neural network (MLP) with two hidden layers (sizes 256 and 64)" and "Input features include
#    user demographics and past consumption behavior across content types aggregated over various time windows,
#    content representations, contextual signals (e.g., device type)" and "temporal signals (e.g., time of day and
#    day of week)" (Sec. 2.2.1). Hence "Listening history, device, time of day".
#   "We use an epsilon-greedy strategy: with a small probability of 1.5%, we sample p_k in P from the logging policy"
#    and, of a uniform draw and "a truncated Gaussian centered around p(c|u) as defined in Equation (3)": "The latter
#    yielded more positive training samples and improved model performance." (Sec. 2.2.2) Hence "1.5%: a random mix
#    near the usual one".
#   Table 2, "Online A/B experiment results vs SC (90 days)": Podcast i2s "+36.6%", Overall i2s "+3.93%", Consumption
#    "+1.28%", Activity "+1.54%". Sec. 3.2: "impression efficiency measured by impression-to-stream (i2s) ratios,
#    homepage activity (measured by fraction of users initiating a stream from the homepage) and overall consumption
#    (measured by overall minutes streamed on the platform)". The items of the page are shelves (Sec. 3). The size
#    and the length of the test are not stated.
#   "the system has been successfully deployed at Spotify as of March 2025." (Sec. 3.2)
#   "3 weeks of user data is collected and two weeks is used for training the model and the last week is used for
#    evaluations." (Sec. 2.2)
#   "use of upper confidence bound (UCB)-based exploration [18, 34], which has been shown to outperform epsilon-greedy
#    strategies in many settings." (Sec. 4, future work)
SPHOME = {"users_million": 600, "days": 90, "explore_pct": 1.5, "pod_i2s_pct": 36.6, "all_i2s_pct": 3.93,
          "minutes_pct": 1.28, "activity_pct": 1.54, "weeks_data": 3, "deployed": "March 2025"}
num("shUsers", "%d" % SPHOME["users_million"])
num("shDays", "%d" % SPHOME["days"])
num("shExplore", "%.1f" % SPHOME["explore_pct"])
num("shGreedy", "%.1f" % (100 - SPHOME["explore_pct"]))
num("shPod", "%.1f" % SPHOME["pod_i2s_pct"])
num("shAllItoS", "%.2f" % SPHOME["all_i2s_pct"])                 # Say only
num("shMinutes", "%.2f" % SPHOME["minutes_pct"])
num("shActivity", "%.2f" % SPHOME["activity_pct"])               # Say only
num("shWeeksData", "%d" % SPHOME["weeks_data"])                  # Say only
num("shDeployed", SPHOME["deployed"])
num("shIdxPod", "%.2f" % (100 + SPHOME["pod_i2s_pct"]))          # a bar length only: 100 for the control
# INVENTED for frame 2 (no source gives the mixes or their estimates): three mixes and the network's estimate of a
# stream from the page for one listener at one moment, as bar lengths in mm. The story: the half and half mix has the
# highest estimate, so the greedy step shows it; the slide marks the estimates as invented.
SH_EST = {"music": 30, "half": 40, "podcasts": 22}
assert max(SH_EST, key=SH_EST.get) == "half" and len(set(SH_EST.values())) == 3
num("shEstMusic", "%d" % SH_EST["music"])
num("shEstHalf", "%d" % SH_EST["half"])
num("shEstPod", "%d" % SH_EST["podcasts"])
for s in ["Over %d million" % SPHOME["users_million"], "last %d days" % SPHOME["days"],
          "%.1f%%" % (100 - SPHOME["explore_pct"]), "%.1f%%" % SPHOME["explore_pct"],
          "+%.1f%%" % SPHOME["pod_i2s_pct"], "+%.2f%%" % SPHOME["minutes_pct"], SPHOME["deployed"]]:
    show("spotify-home", s)

# == Amazon Payments: one UCB score for each step of an application, added up, 2026 ==
# Chidi Prince John and Burak Gozluklu (Amazon), "Uplifting conversion across the acquisition funnel with
# personalization using contextual bandits on AWS", AWS Machine Learning Blog, 1 October 2026
# (https://aws.amazon.com/blogs/machine-learning/uplifting-conversion-across-the-acquisition-funnel-with-personalization-using-contextual-bandits-on-aws/),
# read in full on 2026-11-06. The product is not named.
#   "we share how Amazon Payments applied AI-based personalization to a product acquisition funnel, using a
#    multi-objective contextual multi-armed bandit (MAB)"
#   "In a seven-week online A/B test we currently see a high single-digit percentage relative lift in final-funnel
#    conversion for one customer population, while another saw no improvement over the existing experience."
#   "we chose UCB, a strategy that selects the arm with the highest estimated reward plus an uncertainty bonus" and
#    "Its deterministic selection rule gives an auditable, reproducible decision for every impression"
#   "Our production system represents each customer as a context vector of behavioral signals (payment behavior,
#    transaction mix, and similar features)"
#   "The bonus is context-dependent. It's large for a kind of visitor the arm has rarely seen, and small for one it
#    has seen often."
#   "The customer journey in our use case comprises three steps: application start, submission, and approval."
#   "Content optimized for starts tends to attract a broad audience, yet approval depends on whether the offer
#    genuinely suits the applicant. Optimizing one stage in isolation can degrade another. We refer to this as the
#    seesaw problem." and "approvals are rare and delayed"
#   "running one LinUCB model per stage (start, submit, approve) and combining their UCB scores through a linear
#    combination" and "We used approximately equal weights." Hence the sum of frame 2.
#   "Our content was assembled from two kinds of parts: industry-themed images and benefit-focused taglines" and
#    "each arm is one (image, tagline) pairing"
#   "approval decisions lag by days"
#   "Policies optimized for a single funnel stage consistently produced at least one negative directional lift
#    elsewhere." (Lessons learned, before deployment)
#   "In our A/B test, one customer population saw directionally positive lifts across all three funnel metrics,
#    currently a high single-digit percentage relative lift on the final stage. For the second population, the model
#    explored most of its arm pool yet found no combination that beat the static page. The lifts were negative, and
#    the approval regression was statistically significant. This was not a model failure. Thorough exploration can
#    confirm that a content pool contains no winner."
#   "only a conventional A/B test (bandit-personalized compared to static baseline) determines whether
#    personalization outperforms your existing experience."
#   "We run a weekly SageMaker AI batch job"; "There is no real-time model inference."; "If no recommendation exists
#    for a visitor, the page falls back to the default static experience"; "Training one model per group";
#    "Consider making the baseline an arm."
#   Not stated: absolute rates, traffic, confidence intervals, the exact lift.
AMAZON = {"weeks": 7, "steps": 3}
num("amWeeks", "%d" % AMAZON["weeks"])
num("amSteps", "%d" % AMAZON["steps"])                          # Say only
# INVENTED for frame 2 (the post gives no scores): three (image, tagline) pairs and their UCB score at each step for
# one visitor, small integers. The story, the seesaw: pair A has the best score for the first step and the worst for
# the approval; pair B has the highest sum, so the sum of the three scores shows B. Equal weights, as in the post.
AM_PAIRS = [("A", (6, 3, 1)), ("B", (4, 4, 4)), ("C", (3, 2, 3))]
am_sum = {p: sum(v) for p, v in AM_PAIRS}
assert max(AM_PAIRS, key=lambda pv: pv[1][0])[0] == "A"                    # the first step alone picks A
assert min(AM_PAIRS, key=lambda pv: pv[1][2])[0] == "A"                    # A has the worst approval score
assert max(am_sum, key=am_sum.get) == "B" and len(set(am_sum.values())) == 3   # the sum picks B, no ties
assert len(set(v[0] for _, v in AM_PAIRS)) == 3                            # no tie in the first step either
for p, v in AM_PAIRS:
    for step, x in zip(["start", "sub", "app"], v):
        num("am%s%s" % (p, step), "%d" % x)
    num("am%ssum" % p, "%d" % am_sum[p])
for s in ["%d weeks" % AMAZON["weeks"], "high single-digit"]:
    show("amazon", s)

# == LinkedIn's ads: the click model, gradient descent at scale, 2024 ==
# The paper of CASE 4 above (LiRank, KDD 2024), read again on 2026-11-06 for its ads model:
#   "At LinkedIn, ads selection relies on click-through-rate (CTR) prediction, estimating the likelihood of member
#    clicks on recommended ads. This CTR probability informs ad auctions for displaying ads to members." (Sec. 3.2)
#   "Advertisers customize chargeable clicks for campaigns, such as some advertisers consider social interaction such
#    as 'like', 'comment' as chargeable clicks while others only consider visiting ads websites as clicks." (Sec. 3.2)
#   "Ads charging prices are linked to click-through rate (CTR) probabilities, making accurate calibration
#    essential." (Sec. 3.4)
#   "besides traditional features from members and advertisers, we incorporate ID features to represent advertisers,
#    campaigns, and advertisements." (Sec. 3.2) Table 8, test AUC of Ads CTR variants: "ID embeddings (IDs)" "+1.27%".
#   "Our baseline model is a multilayer perceptron model [...] Features fall into five categories: contextual,
#    advertisement, member, advertiser, ad-member interaction. Baseline model doesn't have Id features. In the Table 5
#    we show relative improvements of each of the techniques including ID embeddings, Quantization, Lowrank DCNv2,
#    TransAct and Isotonic calibration layer. [...] We have deployed techniques to production and observed 4.3% CTR
#    relative improvement in online A/B tests." (Sec. 5.3) Hence "the lists and other changes" on the slide and in
#    the Say: the 4.3% is not the lists' alone, and the changes came one after another.
#   "While Adam was generally effective, models with numerous sparse features required AdaGrad" (Sec. 6.2): both are
#    forms of gradient descent. Hence "gradient descent learns the numbers".
#   Table 3, "Incremental Experiments Settings", Ads CTR: cold start data range "14 days", incremental data range
#    "0.5 day", incremental iterations "4". Table 5, "Ads CTR model results summary", cold start against incremental
#    training: test AUC "+0.18%", and a training time 96% shorter, printed with a minus sign (macro liIncCut above).
#    Sec. 5.1: "We tested incremental training on both Feed ranking models and Ads CTR models." Hence "in a test" on
#    the slide; the paper does not say that it runs in production for ads. "half a day" is in words on the slide.
#   "Incremental training, on the other hand, not only uses the previous model for weight initialization but also
#    leverages it to create an informative regularization term." (Sec. 3.6)
#   "more than 1 billion members" (Sec. 1, macro liMembers above)
#   Scope traps, kept off these slides: the 70 to 20 hours of Sec. 4.1 and the warm-up and learning rate of Sec. 6.2
#   name no model; "billions of parameters" and "every 8 hours" are the Feed's (Sec. 3.9); the "30-dim ID embeddings"
#   row is in the Feed's table (Sec. 5.2); Thompson sampling ran on the Feed (Sec. 3.8).
LIADS = {"cold_days": 14, "inc_days": 0.5, "inc_iters": 4, "inc_auc_pct": 0.18}
num("laColdDays", "%d" % LIADS["cold_days"])                     # Say only
num("laIncAuc", "%.2f" % LIADS["inc_auc_pct"])                   # Say only
for s in ["Over %d billion" % LIRANK["members_billion"], "+%.1f%%" % LIRANK["ads_ctr_pct"],
          "%d%%" % LIRANK["incremental_cut_pct"]]:
    show("linkedin", s)


# ----- The weekend deck, weekend2-cases.tex (Carlos, 2026-11-06: "merge all this decks into a new deck for the
# weekend"): one section per case deck, in this order, so its PDF must show every string of every case deck.
WEEKEND_CASES = ["etsy", "spotify", "airbnb", "spotify-home", "amazon", "linkedin"]
deck_expect["weekend2-cases"] = [s for d in WEEKEND_CASES for s in deck_expect[d]]


# ===== write =====
Path("numbers.tex").write_text(
    "% numbers.tex: WRITTEN BY tools/cases_numbers.py. Do not edit by hand; rerun the script.\n"
    + "\n".join("\\newcommand{\\%s}{%s}" % (n, t) for n, t in macros) + "\n", encoding="utf-8")
Path("tools/expected.txt").write_text("\n".join(expect) + "\n", encoding="utf-8")
for deck, strings in deck_expect.items():
    Path("tools/expected-%s.txt" % deck).write_text("\n".join(strings) + "\n", encoding="utf-8")
print("numbers.tex written: %d macros; tools/expected.txt: %d strings; %s" % (len(macros), len(expect),
      ", ".join("expected-%s.txt: %d" % (d, len(s)) for d, s in deck_expect.items())))
