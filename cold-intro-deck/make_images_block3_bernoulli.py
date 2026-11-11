#!/usr/bin/env python3
"""make_images_block3_bernoulli.py: the pictures of BERNOULLI, one of the three drafts of the cold intro of the
Friday 14:00 bandits block (block3-bandits-bernoulli.tex), cut and graded from four public domain originals.
make_images.py (block 1) and make_images_block5.py (block 5) are not touched by this script.

    python3 -I make_images_block3_bernoulli.py ORIGDIR [OUTDIR]     # OUTDIR defaults to img/

ORIGDIR holds the four originals under these names (sizes, bytes and SHA-1 of the files downloaded on 2026-11-11;
for the three files from Commons, the Commons API gave the same size and SHA-1):

  zbz-muenster-rheinbruecke-991007613699705501.jpg   4857 x 4147, 3,777,386 bytes,
      SHA-1 09b5ce4acd35babd52763877f49551fe565b2a15
      Emanuel Buechel (drawing) and David Herrliberger (publisher), Prospect des Grossen Muensters und Rheinbruecke zu
      Basel, 1761, etching, plate 254 of Herrliberger's Topographie der Eidgnossschaft, vol. 2; Zentralbibliothek
      Zuerich, Graphische Sammlung, STF XVI, 21. Licence in the Commons API: "Public domain" (PD-Art, PD-old-100).
      https://commons.wikimedia.org/wiki/File:Zentralbibliothek_Z%C3%BCrich_-_Prospect_des_Grossen_M%C3%BCnsters_und_Rheinbr%C3%BCcke_zu_Basel_-_991007613699705501.jpg
      curl -L -A "Mozilla/5.0" -o zbz-muenster-rheinbruecke-991007613699705501.jpg "https://upload.wikimedia.org/wikipedia/commons/e/ee/Zentralbibliothek_Z%C3%BCrich_-_Prospect_des_Grossen_M%C3%BCnsters_und_Rheinbr%C3%BCcke_zu_Basel_-_991007613699705501.jpg"
  Jakob_Bernoulli.jpg   2000 x 2338, 605,476 bytes, SHA-1 5f8e6e99394b838dc383034def9bcd0712c2e0c5
      Niklaus Bernoulli (1662 to 1716), portrait of his brother Jakob Bernoulli, 1687, oil; in the Commons category
      "Portraits at the Old Aula of University of Basel". Licence in the Commons API: "Public domain"
      (PD-old-auto-1923, deathyear 1716).
      https://commons.wikimedia.org/wiki/File:Jakob_Bernoulli.jpg
      curl -L -A "Mozilla/5.0" -o Jakob_Bernoulli.jpg "https://upload.wikimedia.org/wikipedia/commons/1/19/Jakob_Bernoulli.jpg"
  Bernoulli_-_Ars_conjectandi_1713_-_058b.tif   1564 x 2048, 9,637,836 bytes,
      SHA-1 561cfbc6b020fc5283a0117862d2ea9b28401165
      The title page of Jakob Bernoulli, Ars Conjectandi, Basel: impensis Thurnisiorum, fratrum, 1713; a photograph
      of the copy of the Fondazione Mansutti, Milan. Licence in the Commons API: "Public domain" (PD-old-100-1923).
      https://commons.wikimedia.org/wiki/File:Bernoulli_-_Ars_conjectandi,_1713_-_058b.tif
      curl -L -A "Mozilla/5.0" -o Bernoulli_-_Ars_conjectandi_1713_-_058b.tif "https://upload.wikimedia.org/wikipedia/commons/d/db/Bernoulli_-_Ars_conjectandi%2C_1713_-_058b.tif"
  jacobibernoulli00bern_0280.jp2   2547 x 3477, 341,017 bytes, SHA-1 c14909f30016a2352423f50689d38f056015c52d
      Page 226 of the same book (part IV, chapter 4, the urn: "no in urna quadam te inscio reconditos esse ter mille
      calculos albos & bis mille nigros ..."), leaf 280 of the scan of the Smithsonian Libraries copy, Internet
      Archive item jacobibernoulli00bern, https://archive.org/details/jacobibernoulli00bern ; the item states
      "Public domain. The Library considers that this work is no longer under copyright protection". The same scan
      is on Wikimedia Commons as a PDF ("File:Jacobi Bernoulli profess. basil. & utriusque societ. ... Ars
      conjectandi ... (IA jacobibernoulli00bern).pdf"), licence "Public domain" in the Commons API.
      curl -L -A "Mozilla/5.0" -o jacobibernoulli00bern_0280.jp2 "https://archive.org/download/jacobibernoulli00bern/jacobibernoulli00bern_jp2.zip/jacobibernoulli00bern_jp2%2Fjacobibernoulli00bern_0280.jp2"
      In this item the jp2 number equals the leafNum of the scandata (leaf 278 is page 224, leaf 280 page 226).

Downloaded files are untrusted data: keep ORIGDIR outside the repository and run this script with python3 -I.

The grade follows the Title sequence of the course cold intro, as make_images_block5.py does: the etching becomes a
warm silver; the portrait keeps its colour at 92 percent saturation; the two pages keep their paper at 70 percent
saturation with a warm cast in the shadows. The paper is pulled down, so that no page glares on the projector, and
the page is darkened where the type sits, with the gradient baked into the file."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1920, 1080
HALF = (960, 1080)

SILVER = ["-colorspace", "Gray", "-colorspace", "sRGB", "+level-colors", "#0d0a08,#efe6d6"]
OIL = ["-modulate", "100,92,100", "-fill", "#2a1d12", "-colorize", "3%"]
PAPER = ["-modulate", "100,70,100", "-fill", "#2a1d12", "-colorize", "6%"]


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


VIEW = "zbz-muenster-rheinbruecke-991007613699705501.jpg"
PORTRAIT = "Jakob_Bernoulli.jpg"
TITLEPAGE = "Bernoulli_-_Ars_conjectandi_1713_-_058b.tif"
PAGE226 = "jacobibernoulli00bern_0280.jp2"

# (output, original, window, tone, extra steps, size). Positions in the originals, read off a grid:
# the etching: the picture inside its border is x 185 to 4700, y 80 to 2640; the two towers of the Minster at
#   x 870 to 1410, their spires from y 130; the Rhine bridge at x 3000 to 4300, y 1720 to 1760; the caption below
#   y 2700 and the colour chart below y 3250 stay outside every window.
# the portrait: the face at x 900 to 1350, y 400 to 1000; the hand on the globe at x 0 to 650, y 1580 to 2000; the
#   painted inscription JAC. BERNOULLI, MATH. P.P. from y 2180 stays outside the window.
# the title page: the page is x 0 to 1460, y 90 to 1940 of the photograph (white beyond); JACOBI BERNOULLI at
#   y 290 to 345, ARS CONJECTANDI at x 115 to 1075, y 520 to 590, RETICULARIS ends at y 1130, the printer's mark
#   at y 1230 to 1600, BASILEAE at y 1640.
# page 226: the running head at y 180 to 250, the urn from the first line to "ater exeat" at y 300 to 720, the text
#   block x 560 to 2420.
JOBS = [
    # 0. the title: the whole etching, the Minster on the left, the bridge on the right; below the bridge the page
    #    sinks into the dark under the title, and the top is veiled under the small kicker
    ("b3b-title", VIEW, crop(215, 100, 4460), SILVER,
     darken(25) + fade("down", 0.50, 0.70, 0.94) + fade("up", 0.80, 1.0, 0.84) + foot(), (W, H)),
    # 1. the setting: the two towers of the Minster against the sky, the words under them
    ("b3b-bg-towers", VIEW, crop(215, 100, 2700), SILVER,
     darken(25) + fade("down", 0.35, 0.46, 0.94) + foot(), (W, H)),
    # 2. the surprise: the Rhine bridge and the far bank, closer; the two lines of Latin under them
    ("b3b-bg-bridge", VIEW, crop(2850, 1240, 1850), SILVER,
     darken(25) + fade("down", 0.50, 0.58, 1.0) + foot(), (W, H)),
    # 3. Titius: the portrait, the left half of a split screen, its right edge sinking into the ground of the page
    ("b3b-half-portrait", PORTRAIT, crop(40, 10, 1920, 9 / 8), OIL,
     fade("right", 0.80, 1.0, 0.85, *HALF) + fade("down", 0.80, 1.0, 0.75, *HALF), HALF),
    # 4. the book: the upper part of the title page, the right half of a split screen, its left edge sinking into
    #    the ground of the page; the top of the printer's mark sits under the credit, so the foot is veiled harder
    ("b3b-half-titlepage", TITLEPAGE, crop(0, 110, 1150, 9 / 8), PAPER,
     darken(30) + fade("left", 0.80, 1.0, 0.85, *HALF) + fade("down", 0.78, 1.0, 0.90, *HALF), HALF),
    # 5. the urn: the head of page 226, where the urn begins, the English under it. In this window the fifth line
    #    of the urn ("calculorum ... & quoties") has its x-height at 0.381 to 0.408 of the height and the sixth
    #    ("ater exeat") its ascenders from 0.430: the fifth sinks into the dark, the sixth is black
    ("b3b-bg-urn", PAGE226, crop(300, 140, 2240), PAPER,
     darken(40) + fade("down", 0.375, 0.428, 1.0) + foot(), (W, H)),
    # 6 and 7. the estimate and its uses: the etching, out of focus and almost gone in the dark
    ("b3b-bg-close", VIEW, crop(215, 100, 4460), SILVER,
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
