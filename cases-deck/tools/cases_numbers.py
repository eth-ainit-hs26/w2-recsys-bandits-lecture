#!/usr/bin/env python3
"""cases_numbers.py: writes numbers.tex, the macros for every number on the slides of the cases deck.

Run from cases-deck/:   python3 tools/cases_numbers.py

No number is typed into cases.tex. Each one is defined here next to the sentence of its source, read
on 4 November 2026, and the script asserts the arithmetic the slides rely on. Every number is measured
or stated by its source; none is invented. README.md lists the sources with links and grades.
"""
from pathlib import Path

macros = []          # (name, text) for numbers.tex
expect = []          # strings tools/check_numbers.py must find in the rendered PDF


def num(name, text, on_slide=None):
    """Define \\<name> as text. on_slide is the string the PDF must contain, if the number is shown."""
    macros.append((name, text))
    if on_slide:
        expect.append(on_slide)


# ===== CASE 1, Friday 08:00, nearest neighbours: Airbnb, similar listings =====
# Grbovic, Cheng, Zhang, Yang, Siclait, Jones, "Listing Embeddings for Similar Listing Recommendations and
# Real-time Personalization in Search Ranking", The Airbnb Tech Blog, 13 March 2018, read in the Wayback
# Machine copy of 25 July 2026 (the live page sends a bot challenge). The paper is Grbovic and Cheng,
# "Real-time Personalization using Embeddings for Search Ranking at Airbnb", KDD 2018 (abstract read).
#   "we learned listing embeddings for 4.5 million active listings on Airbnb using more than 800 million
#    search clicks sessions"
#   "The dimensionality of the listing embeddings was set to d = 32, as we found that to be a good
#    trade-off between offline performance [...] and the memory needed to store vectors in RAM memory of
#    search machines for the purposes of real-time similarity calculations."
#   "At the time of testing embeddings the existing algorithm for Similar Listings consisted of calling our
#    main Search Ranking model for the same location as the given listing followed by filtering on same price
#    range and listing type as the given listing." (the control of the A/B test, Say)
#   "[...] vectors v(lj) of all listings from the same market that are available for the same set of dates
#    (if check-in and check-out dates are set)."
#   "The k=12 listings with the highest similarity were shown as similar listings."
#   "The A/B test showed that embedding-based solution lead to a 21% increase in Similar Listing carousel
#    CTR and 4.9% more guests discovering the listing they ended up booking in the Similar Listing
#    carousel."
#   "Together, Search Ranking and Similar Listings drive 99% of our booking conversions."
#   "To create embeddings for a new listing we find 3 geographically closest listings that do have
#    embeddings, and are of same listing type and price range as the new listing, and calculate their
#    mean vector."
#   "we predict not only the neighboring clicked listings but also the eventually booked listing as well"
#   "[...] lead to the launch of embedding features for real-time personalization to production in Summer
#    of 2017."
AIRBNB = {"sessions_million": 800, "listings_million": 4.5, "dims": 32, "k": 12, "ctr_pct": 21,
          "found_pct": 4.9, "bookings_share_pct": 99, "cold_neighbours": 3}
num("abSessions", "%d" % AIRBNB["sessions_million"], "%d million" % AIRBNB["sessions_million"])
num("abListings", "%.1f" % AIRBNB["listings_million"])
num("abDims", "%d" % AIRBNB["dims"], "%d numbers" % AIRBNB["dims"])
num("abK", "%d" % AIRBNB["k"], "%d nearest" % AIRBNB["k"])
num("abCtr", "%d" % AIRBNB["ctr_pct"], "+%d%%" % AIRBNB["ctr_pct"])
num("abFound", "%.1f" % AIRBNB["found_pct"], "+%.1f%%" % AIRBNB["found_pct"])
num("abShare", "%d" % AIRBNB["bookings_share_pct"])
num("abCold", "%d" % AIRBNB["cold_neighbours"], "%d similar homes" % AIRBNB["cold_neighbours"])


# ===== CASE 2, Friday 10:00, matrix factorization: the Netflix Prize, 2006 to 2009 =====
# Netflix Prize Rules, netflixprize.com, archived 5 November 2006
# (https://web.archive.org/web/20061105165727/http://www.netflixprize.com/rules):
#   "To qualify for the $1,000,000 Grand Prize, the accuracy of your submitted predictions on the qualifying
#    set must be at least 10% better than the accuracy Cinematch can achieve on the same training data set
#    at the start of the Contest."
#   "The training data set consists of more than 100 million ratings from over 480 thousand randomly-chosen,
#    anonymous customers on nearly 18 thousand movie titles."
#   "you must share your method with (and non-exclusively license it to) Netflix"
# Forum post "Grand Prize awarded to team BellKor's Pragmatic Chaos", netflixprize.com, archived 28 December 2009:
#   "[...] BellKor's Pragmatic Chaos for their verified submission on July 26, 2009 at 18:18:28 UTC, achieving
#    the winning RMSE of 0.8567 on the test subset. This represents a 10.06% improvement over Cinematch's score
#    on the test subset at the start of the contest."
#   "The Prize was awarded in a ceremony in New York City on September 21st, 2009."
# Leaderboard, archived 26 September 2009: "There are currently 51051 contestants on 41305 teams from 186
#    different countries."
# Bennett and Lanning, "The Netflix Prize", KDD Cup and Workshop 2007, p. 3: Cinematch uses "a variant of
#    Pearson's correlation with all other movies to determine a list of "similar" movies".
# Koren, Bell, Volinsky, "Matrix Factorization Techniques for Recommender Systems", IEEE Computer 42(8), 2009.
# The 100+ are the team's entries before the final one, hence "by 2008" on the slide:
#   "[...] won the 2007 Progress Prize with the best score at the time: 8.43 percent better than Netflix.
#    Later, we aligned with team Big Chaos to win the 2008 Progress Prize with a score of 9.46 percent. At the
#    time of this writing, we are still in first place, inching toward the 10 percent landmark. Our winning
#    entries consist of more than 100 different predictor sets, the majority of which are factorization models
#    using some variants of the methods described here."
#   "matrix factorization models are superior to classic nearest-neighbor techniques"
# Narayanan and Shmatikov, arXiv cs/0610105, listed as "How To Break Anonymity of the Netflix Prize Dataset";
#   the PDF of v2 (22 November 2007) is titled "Robust De-anonymization of Large Datasets (How to Break
#   Anonymity of the Netflix Prize Dataset)". Published as "Robust De-anonymization of Large Sparse Datasets",
#   IEEE S&P 2008, pp. 111-125, read in the authors' copy (www.cs.cornell.edu/~shmat/shmat_oak08netflix.pdf):
#   "Using the Internet Movie Database as the source of background knowledge, we successfully identified the
#    Netflix records of known users, uncovering their apparent political preferences and other potentially
#    sensitive information." (abstract)
#   "we worked with a very small sample of around 50 IMDb users. Our results should thus be viewed as a proof
#    of concept. They do not imply anything about the percentage of IMDb users who can be identified in the
#    Netflix Prize dataset." (Sec. 5)
#   "Given our small sample of IMDb users, our algorithm identified the records of two users in the Netflix
#    Prize dataset with eccentricities of around 28 and 15, respectively." (Sec. 5)
#   "Consider the information that we have been able to deduce by locating one of these users' entire movie
#    viewing history [...] his political orientation may be revealed [...] and his religious views [...]"
# Neil Hunt, "Netflix Prize Update", Netflix blog, 12 March 2010 (archived):
#   "the Federal Trade Commission (FTC) asked us how a Netflix Prize sequel might affect Netflix members'
#    privacy, and a lawsuit was filed by KamberLaw LLC pertaining to the sequel."
#   "We have reached an understanding with the FTC and have settled the lawsuit with plaintiffs."
#   "we have decided to not pursue the Netflix Prize sequel that we announced on August 6, 2009."
# FTC closing letter, Mithal to Freeman (counsel for Netflix), 12 March 2010, read in the Wayback copy of 13 July
# 2025 (scanned; OCR errors corrected): "staff identified a number of concerns related to Prize 2. These include
#    the risk of re-identification [...]"; "Netflix stated that if it releases a second data set in the future,
#    it would not do so publicly; rather, it would release such data only to researchers who contractually agree
#    to specific limitations on its use."
NETFLIX = {"ratings_million": 100, "customers_thousand": 480, "prize_million": 1, "target_pct": 10,
           "win_pct": 10.06, "win_rmse": 0.8567, "cinematch_rmse": 0.9525, "models": 100,
           "contestants": 51051, "countries": 186, "imdb_sample": 50, "imdb_found": 2}
# the 10.06% is the rules' own measure: 1 - 0.8567 / 0.9525
assert abs(100 * (1 - NETFLIX["win_rmse"] / NETFLIX["cinematch_rmse"]) - NETFLIX["win_pct"]) < 0.01
num("nfRatings", "%d" % NETFLIX["ratings_million"], "%d million ratings" % NETFLIX["ratings_million"])
num("nfPrize", "%d" % NETFLIX["prize_million"], "$%d million" % NETFLIX["prize_million"])
num("nfTarget", "%d" % NETFLIX["target_pct"], "%d%% better" % NETFLIX["target_pct"])
num("nfWin", "%.2f" % NETFLIX["win_pct"], "%.2f%%" % NETFLIX["win_pct"])
num("nfModels", "%d" % NETFLIX["models"], "%d+" % NETFLIX["models"])
num("nsFound", "%d" % NETFLIX["imdb_found"], "%d of about %d" % (NETFLIX["imdb_found"], NETFLIX["imdb_sample"]))
num("nsSample", "%d" % NETFLIX["imdb_sample"])
num("nfCustomers", "%d" % NETFLIX["customers_thousand"])            # Say only
num("nfContestants", "{:,}".format(NETFLIX["contestants"]))          # Say only
num("nfCountries", "%d" % NETFLIX["countries"])                      # Say only


# ===== CASE 3, Friday 12:00, bandits: Adyen, how to send each payment, 2020 to 2025 =====
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
# van Rooijen (Adyen), "Optimizing payment conversion rates with contextual multi-armed bandits", Adyen
# Knowledge Hub, 2 November 2020: the options include requiring 3D Secure or not, an account (card) update,
# "Optimizing the payment message formatting (ISO message)" and "Instantly retrying a payment"; "In total,
# this results in hundreds of optimizations that can be chosen."; the previous solution was A/B tests per
# account and bank, with a "Small sample problem. Adding additional payment features (e.g. amount or transaction
# type) could result in small and thus insignificant A/B test groups." and "The result of an experiment is
# deterministic, i.e. if the underlying world changes then the experiment would have to be re-run again.";
# "a full-fledged reinforcement learning set-up was out-of-reach from a technology perspective." The post gives
# no launch date, hence "By November 2020" in the Say.
ADYEN = {"opt_min": 2, "opt_max": 15, "opt_median": 4, "uplift_pct": 0.1, "extra_million": 9, "traffic_pct": 5,
         "weeks": 4, "pos_eg_pct": 87.4, "pos_sq_pct": 93.5, "regress_pct": 0.2, "retrain_days": 7,
         "train_hours": 4, "cores": 32}
num("adOptMin", "%d" % ADYEN["opt_min"], "%d to %d ways" % (ADYEN["opt_min"], ADYEN["opt_max"]))
num("adOptMax", "%d" % ADYEN["opt_max"])
num("adUplift", "%.1f" % ADYEN["uplift_pct"], "+%.1f%%" % ADYEN["uplift_pct"])
num("adExtra", "%d" % ADYEN["extra_million"], "%dM" % ADYEN["extra_million"])
num("adRegress", "%.1f" % ADYEN["regress_pct"], "%.1f%% worse" % ADYEN["regress_pct"])
num("adTraffic", "%d" % ADYEN["traffic_pct"])                       # Say only
num("adWeeks", "%d" % ADYEN["weeks"])                               # Say only
num("adRetrain", "%d" % ADYEN["retrain_days"])                       # Say only


# ===== CASE 4, Friday 14:00, gradient descent: what Netflix put into production, 2012 =====
# Amatriain and Basilico, "Netflix Recommendations: Beyond the 5 stars (Part 1)", The Netflix Tech Blog,
# 6 April 2012, read in the archived original (https://web.archive.org/web/20130105140308/
# http://techblog.netflix.com/2012/04/netflix-recommendations-beyond-5-stars.html):
#   "A year into the competition, the Korbell team won the first Progress Prize with an 8.43% improvement.
#    They reported more than 2000 hours of work in order to come up with the final combination of 107
#    algorithms that gave them this prize. And, they gave us the source code."
#   "We looked at the two underlying algorithms with the best performance in the ensemble: Matrix
#    Factorization (which the community generally called SVD, Singular Value Decomposition) and Restricted
#    Boltzmann Machines (RBM)."
#   "SVD by itself provided a 0.8914 RMSE, while RBM alone provided a competitive but slightly worse 0.8990
#    RMSE. A linear blend of these two reduced the error to 0.88."
#   "they were built to handle 100 million ratings, instead of the more than 5 billion that we have, and that
#    they were not built to adapt as members added more ratings. But once we overcame those challenges, we put
#    the two algorithms into production, where they are still used as part of our recommendation engine."
#   "you might be wondering what happened with the final Grand Prize ensemble that won the $1M two years later.
#    [...] blending hundreds of predictive models to finally cross the finish line. We evaluated some of the
#    new methods offline but the additional accuracy gains that we measured did not seem to justify the
#    engineering effort needed to bring them into a production environment. Also, our focus on improving
#    Netflix personalization had shifted to the next level by then."
#   "One of the reasons our focus in the recommendation algorithms has changed is because Netflix as a whole has
#    changed dramatically in the last few years. Netflix launched an instant streaming service in 2007, one year
#    after the Netflix Prize began."
# Part 2, 20 June 2012: "since the mapping is not perfect, offline performance is used only as an indication
#    to make informed decisions on follow up tests."
# Koren, "The BellKor Solution to the Netflix Grand Prize", August 2009, Sec. IV-A: "All models are learned by
#    stochastic gradient descent applied directly on the raw data".
# Funk, "Netflix Update: Try This at Home", 11 December 2006: "Lrate is the learning rate, a rather arbitrary
#    number which I fortuitously set to 0.001 on day one"; "My wee laptop is able to do a training pass through
#    the entire data set of 100 million ratings in about seven and a half seconds."
PRODUCTION = {"pp_pct": 8.43, "pp_models": 107, "pp_hours": 2000, "built_for_million": 100, "had_billion": 5,
              "kept": 2, "funk_lrate": 0.001, "funk_pass_s": 7.5}
num("nfPPGain", "%.2f" % PRODUCTION["pp_pct"], "%.2f%%" % PRODUCTION["pp_pct"])
num("nfPPModels", "%d" % PRODUCTION["pp_models"], "%d models" % PRODUCTION["pp_models"])
num("nfPPHours", "{:,}".format(PRODUCTION["pp_hours"]))              # Say only
num("nfBuiltFor", "%d" % PRODUCTION["built_for_million"], "%d million ratings" % PRODUCTION["built_for_million"])
num("nfHad", "%d" % PRODUCTION["had_billion"], "%d billion" % PRODUCTION["had_billion"])
num("nfKept", "%d" % PRODUCTION["kept"])
num("nfFunkRate", "%.3f" % PRODUCTION["funk_lrate"])                  # Say only
num("nfFunkPass", "%.1f" % PRODUCTION["funk_pass_s"])                 # Say only


# ===== write =====
Path("numbers.tex").write_text(
    "% numbers.tex: WRITTEN BY tools/cases_numbers.py. Do not edit by hand; rerun the script.\n"
    + "\n".join("\\newcommand{\\%s}{%s}" % (n, t) for n, t in macros) + "\n", encoding="utf-8")
Path("tools/expected.txt").write_text("\n".join(expect) + "\n", encoding="utf-8")
print("numbers.tex written: %d macros; tools/expected.txt: %d strings" % (len(macros), len(expect)))
