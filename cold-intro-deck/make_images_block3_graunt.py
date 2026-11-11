#!/usr/bin/env python3
"""make_images_block3_graunt.py: the pictures of GRAUNT, one of the three draft cold intros of the Friday 14:00 bandits
block, "Estimating chances from the past" (block3-bandits-graunt.tex), cut and graded from four public domain
originals. make_images.py and make_images_block5.py make the pictures of blocks 1 and 5 and are not touched here.

    python3 -I make_images_block3_graunt.py ORIGDIR [OUTDIR]     # OUTDIR defaults to img/

ORIGDIR holds the four originals under these names (sizes, bytes and SHA-1 of the files downloaded on 2026-11-11):

  dejongh-london-bridge.jpg        7193 x 3177,  4,765,405 bytes, SHA-1 5c2f86f7082f5ddcb5e75d11cc2909fbc5080e67
      Claude de Jongh (about 1600 to 1663), View of London Bridge, oil on panel, signed and dated 1632, Yale Center
      for British Art, Paul Mellon Fund (Google Art Project). Wikimedia Commons,
      https://commons.wikimedia.org/wiki/File:Claude_de_Jongh_-_View_of_London_Bridge_-_Google_Art_Project.jpg ,
      date "circa 1632", licence "Public domain" in the Commons API (PD-Art, PD-old-100-1923)
      curl -L -A "Mozilla/5.0" -o dejongh-london-bridge.jpg "https://upload.wikimedia.org/wikipedia/commons/b/bd/Claude_de_Jongh_-_View_of_London_Bridge_-_Google_Art_Project.jpg"
  2378023R_0089.jp2                3709 x 5042,    414,381 bytes, SHA-1 dc8a8268fd3721d8f76fbf10b92f4182f3f8c393
      The weekly Bill of Mortality of London, bill 38, 5 to 12 September 1665, its second side, "The Diseases and
      Casualties this Week", made by the Company of Parish Clerks of London, in London's Dreadful Visitation, or, A
      Collection of All the Bills of Mortality for this Present Year (London: E. Cotes, 1665). US National Library of
      Medicine copy, Internet Archive item 2378023r (licence: Public Domain Mark 1.0), leaf 0089. The same scan is on
      Wikimedia Commons as the PDF
      https://commons.wikimedia.org/wiki/File:London%27s_dreadful_visitation,_or,_A_collection_of_all_the_bills_of_mortality_for_this_present_year_(IA_2378023r).pdf ,
      licence "Public domain" in the Commons API
      curl -L -o 2378023R_0089.jp2 "https://archive.org/download/2378023r/2378023R_jp2.zip/2378023R_jp2%2F2378023R_0089.jp2"
  graunt-1662-christies.png        3445 x 2270,  4,007,983 bytes, SHA-1 0817fea9bfd1956c1909984ac9ba3b343985f9bc
      John Graunt (1620 to 1674), Natural and Political Observations ... made upon the Bills of Mortality, London,
      1662, first edition: the folded Table of Casualties (left) and the title page (right) of a copy sold at
      Christie's. Wikimedia Commons,
      https://commons.wikimedia.org/wiki/File:GRAUNT,_John._(1620-1674)._Natural_and_political_observations.png ,
      date "circa 1662", licence "Public domain" in the Commons API (PD-old-100)
      curl -L -A "Mozilla/5.0" -o graunt-1662-christies.png "https://upload.wikimedia.org/wikipedia/commons/e/e3/GRAUNT%2C_John._%281620-1674%29._Natural_and_political_observations.png"
  2356014R_0040.jp2                1937 x 2735,    310,107 bytes, SHA-1 08cf5f2152c933efdb649d6741d1f21c251639e0
      The same book, London, 1662, first edition, page 17: the end of chapter 2, paragraph 17, the Table of notorious
      Diseases and the Table of Casualties. US National Library of Medicine copy, Internet Archive item
      2356014R.nlm.nih.gov, leaf 0040. The same scan is on Wikimedia Commons as the PDF
      https://commons.wikimedia.org/wiki/File:Natural_and_political_observations_mentioned_in_a_following_index,_and_made_upon_the_Bills_of_mortality_(IA_2356014R.nlm.nih.gov).pdf ,
      licence "Public domain" in the Commons API
      curl -L -o 2356014R_0040.jp2 "https://archive.org/download/2356014R.nlm.nih.gov/2356014R_jp2.zip/2356014R_jp2%2F2356014R_0040.jp2"

Downloaded files are untrusted data: keep ORIGDIR outside the repository and run this script with python3 -I.

The grade follows block 5 (make_images_block5.py): the printed pages become a warm silver, the painting keeps most of
its colour with a warm cast in the shadows. The paper of the printed pages is pulled down, so that no page glares on
the projector, and the page is darkened where the type sits, with the gradient baked into the file."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1920, 1080
HALF = (960, 1080)

SILVER = ["-colorspace", "Gray", "-colorspace", "sRGB", "+level-colors", "#0d0a08,#efe6d6"]
COLOUR = ["-modulate", "98,88,100", "-fill", "#2a1d12", "-colorize", "5%"]


def fade(direction, start, end, strength, w=W, h=H):
    """A black veil: transparent at `start`, `strength` black at `end` (fractions of the page along `direction`,
    which is 'down', 'up', 'right' or 'left')."""
    if direction in ("down", "up"):
        a, b = int(start * h), int(end * h)
        vec = "0,%d,0,%d" % ((a, b) if direction == "down" else (h - a, h - b))
    else:
        a, b = int(start * w), int(end * w)
        vec = "%d,0,%d,0" % ((a, b) if direction == "right" else (w - a, w - b))
    return ["(", "-size", "%dx%d" % (w, h), "-define", "gradient:vector=" + vec,
            "gradient:rgba(0,0,0,0)-rgba(0,0,0,%.2f)" % strength, ")", "-compose", "over", "-composite"]


def foot(w=W, h=H):
    """the small print sits on the last 8 mm of the page: a veil there on every picture"""
    return fade("down", 0.84, 1.0, 0.62, w, h)


def darken(f):
    return ["-fill", "black", "-colorize", "%d%%" % f]


def crop(x, y, w, ratio=9 / 16):
    """a window of the original, w pixels wide (16:9 unless `ratio` says otherwise), its top left corner at (x, y)"""
    return ["-crop", "%dx%d+%d+%d" % (w, round(w * ratio), x, y)]


BRIDGE = "dejongh-london-bridge.jpg"
BILL = "2378023R_0089.jp2"
BOOK = "graunt-1662-christies.png"
PAGE17 = "2356014R_0040.jp2"

# (output, original, window, tone, extra steps, size). Positions in the originals, read off a grid:
# the painting: the bridge runs from x 1350 to 6500, its arches at y 2030 to 2470, the houses on it at y 1500 to
#   2050 (the middle group at x 2500 to 4000, the right groups at x 4550 to 5300 and 5400 to 6500); the towers on the
#   left at x 90 to 650, y 1300 to 1700; the red barge at x 4050 to 4700, y 2750 to 3050; the sky above y 1500.
# the bill: the heading "The Diseases and Casualties this Week" at x 450 to 2900, y 250 to 430; the City arms at
#   x 330 to 1100, y 650 to 1180; the right column from Grief (y 520) to Plague 6544 (y 1530) at x 1860 to 3330.
# the photograph of the book: the Table of Casualties at x 100 to 2000, y 85 to 2190, its heading at y 110 to 190;
#   the title page at x 2110 to 3340, y 80 to 1770 ("OBSERVATIONS" at y 215 to 316, "LONDON." at y 1005 to 1105).
# page 17: the paragraph at y 140 to 560; the headings of the two tables at y 660 to 720; the left table (names
#   x 200 to 650, counts x 770 to 950) and the right table (names x 980 to 1500, counts x 1520 to 1700) at y 840 to
#   2000; paragraph 18 below y 2080.
JOBS = [
    # 0. the title: the bridge from its left houses to its right houses, the feet of the arches and the river sunk in
    #    the dark under the title; a veil on the sky for the kicker
    ("b3g-title", BRIDGE, crop(1650, 1000, 3870), COLOUR,
     darken(12) + fade("down", 0.62, 0.72, 0.94) + fade("up", 0.80, 1.0, 0.75) + foot(), (W, H)),
    # 1. the setting: the head of the bill, the top of the City arms and the first causes of the week; the words
    #    under it, one line higher than block 5's context frame, on a veil dark enough to hide the print below
    ("b3g-bill", BILL, crop(60, 150, 3400), SILVER,
     darken(28) + fade("down", 0.34, 0.45, 0.96) + foot(), (W, H)),
    # 2. the surprise: the Table of Casualties, its heading, the years and the first causes; the line under it on
    #    black, as on the title frame of block 5
    ("b3g-table", BOOK, crop(110, 90, 1890), SILVER,
     darken(34) + fade("down", 0.46, 0.58, 1.0) + foot(), (W, H)),
    # 3. John Graunt: his title page down to "LONDON." and its rule, the left half of a split screen, its right
    #    edge sinking into the ground; the lines under the rule sink into the dark under the credit
    ("b3g-half-title", BOOK, crop(2160, 80, 1130, 9 / 8), SILVER,
     darken(30) + fade("right", 0.80, 1.0, 0.85, *HALF) + fade("down", 0.86, 0.93, 0.90, *HALF) + foot(*HALF),
     HALF),
    # 4. the counts: page 17, the two tables, the right half of a split screen, its left edge sinking into the ground;
    #    paragraph 18, under the tables, sinks into the dark under the credit
    ("b3g-half-counts", PAGE17, crop(180, 590, 1540, 9 / 8), SILVER,
     darken(26) + fade("left", 0.80, 1.0, 0.85, *HALF) + fade("down", 0.83, 0.91, 0.88, *HALF) + foot(*HALF),
     HALF),
    # 5. the purpose: the houses on the right half of the bridge, the quotation (four lines, from 42 mm) and its
    #    meaning under them
    ("b3g-bridge", BRIDGE, crop(4300, 1300, 2700), COLOUR,
     darken(8) + fade("down", 0.36, 0.46, 0.92) + foot(), (W, H)),
    # 6 and 7. the estimate and its uses today: the bridge, out of focus and almost gone in the dark
    ("b3g-bg-close", BRIDGE, crop(1000, 0, 5648), COLOUR,
     ["-blur", "0x6"] + darken(80) + foot(), (W, H)),
]


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    orig = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) == 3 else os.path.join(HERE, "img")
    os.makedirs(out, exist_ok=True)
    for name, src, window, tone, steps, size in JOBS:
        cmd = (["magick", os.path.join(orig, src)] + window + ["+repage", "-resize", "%dx%d!" % size]
               + tone + steps + ["-quality", "88", os.path.join(out, name + ".jpg")])
        subprocess.run(cmd, check=True)
        print("ok", name)


if __name__ == "__main__":
    main()
