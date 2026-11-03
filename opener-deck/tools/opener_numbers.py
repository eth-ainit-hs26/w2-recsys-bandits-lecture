#!/usr/bin/env python3
"""opener_numbers.py: writes numbers.tex, the macros for every number on the opener's slides.

Run from opener-deck/:   python3 tools/opener_numbers.py

No number is typed into opener.tex. Each one is defined here next to the sentence of its source,
checked on 3 November 2026, and the script asserts the arithmetic the slides rely on. Every number
is measured and reported by its source; none is invented. README.md lists the sources with links.
"""
from pathlib import Path

# FRAME 1: advertising revenue in 2025, millions of US dollars.
# Alphabet Form 10-K for 2025, revenue table: "Google advertising" 294,691 (2024: 264,590).
# Meta Form 10-K for 2025, revenue table: "Advertising" 196,175 (2024: about 160.6 bn).
# Amazon reports "advertising services" by quarter. Its Q4 2025 results (5 February 2026) give the
#   four quarters of 2025: 13,921 + 15,694 + 17,703 + 21,317 = 68,635. Marketing Dive reported that
#   the year's ad revenue "surpassed $68 billion". The second reader checked all three on 2026-11-03.
AMAZON_QUARTERS = (13_921, 15_694, 17_703, 21_317)
AD_MILLIONS = {"Google": 294_691, "Meta": 196_175, "Amazon": sum(AMAZON_QUARTERS)}
assert AD_MILLIONS["Amazon"] == 68_635
ad_bn = {k: round(v / 1000, 1) for k, v in AD_MILLIONS.items()}
total_bn = round(sum(AD_MILLIONS.values()) / 1000, 1)
per_day_bn = round(sum(AD_MILLIONS.values()) / 1000 / 365, 1)
assert ad_bn == {"Google": 294.7, "Meta": 196.2, "Amazon": 68.6}, ad_bn
assert total_bn == 559.5 and round(sum(ad_bn.values()), 1) == total_bn, total_bn
assert per_day_bn == 1.5, per_day_bn
BAR_MAX_MM = 80.0                       # the Google bar
bar_mm = {k: round(BAR_MAX_MM * v / ad_bn["Google"], 2) for k, v in ad_bn.items()}

# FRAME 2: shares chosen by a recommender.
# YouTube: "For more than 70 percent of the time you spend watching ..." (CNET, 10 January 2018,
#   Neal Mohan at CES; the correction the same day confirms "more than 70 percent").
# Netflix: "75 % of what people watch is from some sort of recommendation" (Netflix Tech Blog 2012,
#   as quoted by Jannach and Jugovac, ACM TMIS 2019).
# Amazon: "35 percent of what consumers purchase on Amazon" (McKinsey, 1 October 2013). McKinsey
#   names no source; Jannach and Jugovac trace it to "a statement of Amazon's CEO in 2006".
SHARE = {"YouTube": 70, "Netflix": 75, "Amazon": 35}
assert all(0 < v < 100 for v in SHARE.values())

# FRAME 3: compared to what.
# Kumar and Hosanagar, Information Systems Research 30(3), 2019, abstract: "recommendation links of
#   a product result in an 11% gain in total sales of the product and its recommended substitutes."
LIFT = 11
WITHOUT, WITH = 100, 100 + LIFT
# Jannach and Jugovac 2019: "direct revenue increases are more often reported to lie between one
#   and five percent".
TYP_LOW, TYP_HIGH = 1, 5

# FRAME 4: Meta, earnings call of 21 October 2026 (July to September 2026), Susan Li, finance chief.
# Read in the transcript on stockanalysis.com on 2026-11-03:
#   "In Q3, we launched this approach to generative retrieval on Facebook Feed, driving a nearly 2%
#    increase in conversions across targeted segments. In addition, we expanded our GEM model for ads
#    ranking to additional surfaces, driving a 1.7% increase in conversions for off-site conversion
#    campaigns and a 9.6% increase in app ad conversions."
#   "In Q3, improvements to Andromeda, such as scaling model complexity and throughput, increased
#    conversions by 1.4% on Facebook."
#   "The global average price per ad increased 14% year-over-year, driven by ad performance gains and
#    improvements in macro conditions relative to Q3 of last year."
#   "Q3 family of apps ad revenue was $63.1 billion, up 26%" (used in the Say only).
META = {"App": 9.6, "Feed": 2.0, "Website": 1.7, "Andromeda": 1.4}   # Feed is "nearly 2%"
META_PRICE_PER_AD = 14
META_MM_PER_PCT = 4.5                   # bar length in mm per percent of more conversions
meta_bar = {k: round(META_MM_PER_PCT * v, 2) for k, v in META.items()}
assert max(meta_bar.values()) <= 50, meta_bar
assert sorted(META.values(), reverse=True) == [META[k] for k in ("App", "Feed", "Website", "Andromeda")]

# FRAME 5: Amazon, earnings call of 29 October 2026 (July to September 2026), Andy Jassy, chief
# executive. Read in the transcript on singjupost.com on 2026-11-03:
#   "Over 400 million customers have used Alexa for Shopping, our agentic shopping assistant, in the
#    last 12 months. With customer interactions up 570% year over year. U.S. customers using Alexa
#    for Shopping are spending 50% more per order than those who don't."
AMZ_USERS_MILLION = 400
AMZ_INTERACTIONS_PCT = 570
AMZ_PER_ORDER_PCT = 50
AMZ_WITHOUT, AMZ_WITH = 100, 100 + AMZ_PER_ORDER_PCT    # spending per order, non-users set to 100
AMZ_MM_PER_UNIT = 0.25                  # bar length in mm per index point
assert AMZ_WITH * AMZ_MM_PER_UNIT <= 38

# FRAME 6: Nubank, Braithwaite et al., "Your Spending Needs Attention: Modeling Financial Habits with
# Transformers", arXiv 2507.23267, version 3 of 29 October 2026, "Presented at 9th Workshop on
# Machine Learning in Finance at KDD 2026". Read on arXiv on 2026-11-03:
#   "over 100 billion transactions across 100M+ members"
#   "In total there are 291 tabular (numerical or categorical) features. Some are derived from
#    transaction sources (e.g., average spend over a given period) [...] all improvements are
#    reported as relative improvement (%) in AUC over a LightGBM model trained on tabular features
#    only, which is our production baseline."
#   Table 2, "nuFormer improvements across tasks and markets vs. baseline models, reported as ordinary
#    relative lift": credit default market 1 AUC +1.25%, credit default market 2 AUC +1.81%, lending
#    market 1 AUC +2.23%, income prediction F1 +7.54%, spend prediction R2 +6.85%.
#   "nuFormer is currently deployed to 100% of customers in one of our markets, serving credit
#    decisions for over 100 million users."
#   "The deployed model drove a 32% increase in our long-term surrogate metric, a contribution
#    equivalent in magnitude to an entire year's typical cumulative gains [...] these improvements
#    came purely from enhanced representation learning on existing transaction data, without adding
#    new data sources or manual feature engineering."
# The gains are shown with the paper's two decimals, so that nothing is rounded.
NU_TX_BILLION = 100
NU_CUSTOMERS_MILLION = 100
NU_FEATURES = 291                       # named in the Say of frame 6 only
NU = {"Income": 7.54, "Spend": 6.85, "Lending": 2.23, "CreditTwo": 1.81, "CreditOne": 1.25}
NU_MM_PER_PCT = 5.5
nu_bar = {k: round(NU_MM_PER_PCT * v, 2) for k, v in NU.items()}
assert max(nu_bar.values()) <= 42, nu_bar
assert sorted(NU.values(), reverse=True) == list(NU.values())

lines = ["% numbers.tex: WRITTEN BY tools/opener_numbers.py. Do not edit by hand; rerun the script.",
         "\\newcommand{\\adGoogle}{%.1f}" % ad_bn["Google"],
         "\\newcommand{\\adMeta}{%.1f}" % ad_bn["Meta"],
         "\\newcommand{\\adAmazon}{%.1f}" % ad_bn["Amazon"],
         "\\newcommand{\\adTotal}{%.1f}" % total_bn,
         "\\newcommand{\\adPerDay}{%.1f}" % per_day_bn,
         "\\newcommand{\\barGoogle}{%.2f}" % bar_mm["Google"],
         "\\newcommand{\\barMeta}{%.2f}" % bar_mm["Meta"],
         "\\newcommand{\\barAmazon}{%.2f}" % bar_mm["Amazon"],
         "\\newcommand{\\shYouTube}{%d}" % SHARE["YouTube"],
         "\\newcommand{\\shNetflix}{%d}" % SHARE["Netflix"],
         "\\newcommand{\\shAmazon}{%d}" % SHARE["Amazon"],
         "\\newcommand{\\liftPct}{%d}" % LIFT,
         "\\newcommand{\\liftWithout}{%d}" % WITHOUT,
         "\\newcommand{\\liftWith}{%d}" % WITH,
         "\\newcommand{\\typLow}{%d}" % TYP_LOW,
         "\\newcommand{\\typHigh}{%d}" % TYP_HIGH,
         "\\newcommand{\\metaApp}{%.1f}" % META["App"],
         "\\newcommand{\\metaFeed}{%d}" % META["Feed"],
         "\\newcommand{\\metaWebsite}{%.1f}" % META["Website"],
         "\\newcommand{\\metaAndromeda}{%.1f}" % META["Andromeda"],
         "\\newcommand{\\metaPrice}{%d}" % META_PRICE_PER_AD,
         "\\newcommand{\\barMetaApp}{%.2f}" % meta_bar["App"],
         "\\newcommand{\\barMetaFeed}{%.2f}" % meta_bar["Feed"],
         "\\newcommand{\\barMetaWebsite}{%.2f}" % meta_bar["Website"],
         "\\newcommand{\\barMetaAndromeda}{%.2f}" % meta_bar["Andromeda"],
         "\\newcommand{\\amzUsers}{%d}" % AMZ_USERS_MILLION,
         "\\newcommand{\\amzInteractions}{%d}" % AMZ_INTERACTIONS_PCT,
         "\\newcommand{\\amzPerOrder}{%d}" % AMZ_PER_ORDER_PCT,
         "\\newcommand{\\amzWithout}{%d}" % AMZ_WITHOUT,
         "\\newcommand{\\amzWith}{%d}" % AMZ_WITH,
         "\\newcommand{\\barAmzWithout}{%.2f}" % (AMZ_MM_PER_UNIT * AMZ_WITHOUT),
         "\\newcommand{\\barAmzWith}{%.2f}" % (AMZ_MM_PER_UNIT * AMZ_WITH),
         "\\newcommand{\\nuTx}{%d}" % NU_TX_BILLION,
         "\\newcommand{\\nuCustomers}{%d}" % NU_CUSTOMERS_MILLION]
for key, value in NU.items():
    lines.append("\\newcommand{\\nu%s}{%.2f}" % (key, value))
    lines.append("\\newcommand{\\barNu%s}{%.2f}" % (key, nu_bar[key]))
Path("numbers.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

# the strings tools/check_numbers.py expects to find in the rendered PDF
expect = ["%.1f" % v for v in ad_bn.values()] + ["%.1f" % total_bn, "%.1f" % per_day_bn]
expect += ["%d%%" % v for v in SHARE.values()] + ["%d%%" % LIFT, "%d" % WITHOUT, "%d" % WITH]
expect += ["%d%% to %d%%" % (TYP_LOW, TYP_HIGH)]
expect += ["+%.1f%%" % META["App"], "nearly +%d%%" % META["Feed"], "+%.1f%%" % META["Website"],
           "+%.1f%%" % META["Andromeda"], "+%d%%" % META_PRICE_PER_AD]
expect += ["%d million" % AMZ_USERS_MILLION, "+%d%%" % AMZ_INTERACTIONS_PCT,
           "+%d%%" % AMZ_PER_ORDER_PCT, "%d" % AMZ_WITH]
expect += ["%d billion" % NU_TX_BILLION, "%d million" % NU_CUSTOMERS_MILLION]
expect += ["+%.2f%%" % NU[k] for k in ("Income", "Spend", "Lending", "CreditOne")]   # on the slide
Path("tools/expected.txt").write_text("\n".join(expect) + "\n", encoding="utf-8")
print("numbers.tex written: %d macros; tools/expected.txt: %d strings" % (len(lines)+(-1), len(expect)))
