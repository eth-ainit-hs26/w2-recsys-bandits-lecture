#!/usr/bin/env python3
"""opener_numbers.py: writes numbers.tex, the macros for every number on the opener's slides.

Run from opener-deck/:   python3 tools/opener_numbers.py

No number is typed into opener.tex. Each one is defined here next to the sentence of its source,
checked on 3 November 2026, and the script asserts the arithmetic the slides rely on. The six
customers of frame 4 are INVENTED and say so on the slide. README.md lists the sources with links.
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

# FRAME 5: Ascarza, Journal of Marketing Research 55(1), 80 to 98, 2018.
# The number is the award committee's, in the AMA release of 3 April 2023: "Targeting by customer
#   sensitivity to the offer rather than churn risk reduced churn rates 4.1 to by 8.7 percentage
#   points." The published abstract (Crossref) gives no number. An earlier talk abstract of hers
#   says "a further reduction of up to seven percentage points". The paper body was not read, so the
#   slide credits the AMA summary.
ASC_LOW, ASC_HIGH = 4.1, 8.7
assert ASC_LOW < ASC_HIGH

# FRAME 4: six INVENTED customers, two calls.
# chance of leaving, and chance of leaving if we call, in whole percent
CUSTOMERS = [("Lea", 80, 80), ("Marco", 70, 75), ("Nina", 50, 30),
             ("Jonas", 40, 25), ("Sara", 30, 25), ("Luca", 10, 10)]
CALLS = 2
risks = [r for _, r, _ in CUSTOMERS]
assert risks == sorted(risks, reverse=True), "rows are listed by chance of leaving, highest first"
change = [c+(-r) for _, r, c in CUSTOMERS]
by_risk = sorted(range(6), key=lambda i: (-CUSTOMERS[i][1]))[:CALLS]
by_response = sorted(range(6), key=lambda i: change[i])[:CALLS]
assert by_risk == [0, 1] and by_response == [2, 3], (by_risk, by_response)
assert not set(by_risk) & set(by_response)
assert sum(change[i] for i in by_risk) > 0      # calling by risk raises the chance of leaving
assert change[0] == 0 and change[1] > 0         # no change for Lea, Marco more likely to cancel
assert sum(change[i] for i in by_response) < 0  # calling by response lowers it
assert all(0 <= r <= 100 and 0 <= c <= 100 for _, r, c in CUSTOMERS)


def fmt_signed(d):
    """+5, 0, and a minus sign typeset in maths for a negative change."""
    if d == 0:
        return "0"
    if d > 0:
        return "+%d" % d
    return "$\\mathord{-}%d$" % abs(d)


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
         "\\newcommand{\\ascLow}{%.1f}" % ASC_LOW,
         "\\newcommand{\\ascHigh}{%.1f}" % ASC_HIGH]
for key, idx in (("Name", 0), ("Risk", 1), ("Call", 2)):
    cases = "\\or ".join(str(c[idx]) for c in CUSTOMERS)
    lines.append("\\newcommand{\\cu%s}[1]{\\ifcase#1\\or %s\\fi}" % (key, cases))
lines.append("\\newcommand{\\cuChange}[1]{\\ifcase#1\\or %s\\fi}"
             % "\\or ".join(fmt_signed(d) for d in change))
Path("numbers.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

# the strings tools/check_numbers.py expects to find in the rendered PDF
expect = ["%.1f" % v for v in ad_bn.values()] + ["%.1f" % total_bn, "%.1f" % per_day_bn]
expect += ["%d%%" % v for v in SHARE.values()] + ["%d%%" % LIFT, "%d" % WITHOUT, "%d" % WITH]
expect += ["%d%% to %d%%" % (TYP_LOW, TYP_HIGH), "%.1f to %.1f" % (ASC_LOW, ASC_HIGH)]
expect += [c[0] for c in CUSTOMERS] + ["%d%%" % c[1] for c in CUSTOMERS]
Path("tools/expected.txt").write_text("\n".join(expect) + "\n", encoding="utf-8")
print("numbers.tex written: %d macros; tools/expected.txt: %d strings" % (len(lines)+(-1), len(expect)))
