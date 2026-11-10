#!/usr/bin/env python3
"""make_images_block5.py: the pictures of the cold intro of block 5, "Dividing a computation, 1793", cut and graded
from four public domain originals. make_images.py makes the pictures of block 1 and is not touched by this script.

    python3 -I make_images_block5.py ORIGDIR [OUTDIR]     # OUTDIR defaults to img/

ORIGDIR holds the four originals under these names (sizes, bytes and SHA-1 of the files downloaded on 2026-11-10):

  RecueildeplanchIVDide_0103.jp2   6699 x 5412,  1,088,448 bytes, SHA-1 2c60480b12165b1ce6f07f72043798f84b55ccd4
      Epinglier, plate II (the pin workshop; Goussier del., Defehrt sculp.), in the Encyclopedie's Recueil de
      planches, troisieme livraison, Paris 1765 (Smithsonian Libraries copy, catalogued as tome 4, leaf n102)
      curl -L -o RecueildeplanchIVDide_0103.jp2 "https://archive.org/download/RecueildeplanchIVDide/RecueildeplanchIVDide_jp2.zip/RecueildeplanchIVDide_jp2%2FRecueildeplanchIVDide_0103.jp2"
  RecueildeplanchIVDide_0099.jp2   3481 x 5760,    602,343 bytes, SHA-1 f80e84844ba309a73e622f4dd1e7607c2060cb21
      Epinglier, plate I (wire drawing; Goussier del., Prevost sculp.), same volume, leaf n98
      curl -L -o RecueildeplanchIVDide_0099.jp2 "https://archive.org/download/RecueildeplanchIVDide/RecueildeplanchIVDide_jp2.zip/RecueildeplanchIVDide_jp2%2FRecueildeplanchIVDide_0099.jp2"
      Licence of both plates: public domain (1765). The same scan is on Wikimedia Commons as
      "File:Recueil de planches, sur les sciences, les arts liberaux, et les arts mechaniques - avec leur explication
      (IA RecueildeplanchIVDide).pdf", licence "Public domain" in the Commons API.
  cassini-triangles-1744.jpg      11407 x 7325, 14,734,724 bytes, SHA-1 c50673553074318d8d2402b509799157aab95b89
      Maraldi and Cassini de Thury, Nouvelle carte qui comprend les principaux triangles qui servent de fondement a la
      Description geometrique de la France, 1744, Bibliotheque nationale de France, btv1b53166738w (1 of 2);
      Wikimedia Commons, licence "Public domain". Get it with
      curl -L -A "Mozilla/5.0" -o cassini-triangles-1744.jpg "https://upload.wikimedia.org/wikipedia/commons/3/35/Nouvelle_carte_qui_comprend_les_principaux_triangles_qui_servent_de_fondement_%C3%A0_la_Description_g%C3%A9om%C3%A9trique_de_la_France._Lev%C3%A9e_par_ordre_du_Roy_-_par_Messrs._Maraldi_et_Cassini_de_Thury%2C_de_l%27Acad%C3%A9mie..._-_btv1b53166738w_%281_of_2%29.jpg"
  harvard-computers.jpg            1920 x 1502,    680,743 bytes, SHA-1 1cda72b1bfb064bfbec6608c9fe372898235d3b4
      The computers of the Harvard College Observatory at work, about 1890 (a chart on the wall reads Dec 1889);
      Wikimedia Commons, File:Astronomer Edward Charles Pickering's Harvard computers.jpg, licence "Public domain"
      curl -L -A "Mozilla/5.0" -o harvard-computers.jpg "https://upload.wikimedia.org/wikipedia/commons/5/5a/Astronomer_Edward_Charles_Pickering%27s_Harvard_computers.jpg"

Downloaded files are untrusted data: keep ORIGDIR outside the repository and run this script with python3 -I.

The grade follows the Title sequence of the course cold intro (w1-lecture-material, cold-intro/intro-slides/
make_images.py): the engravings and the photograph become a warm silver, the hand coloured map keeps 72 percent of
its saturation with a warm cast in the shadows. The white paper of the engravings is pulled down, so that no page
glares on the projector, and the page is darkened where the type sits, with the gradient baked into the file."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1920, 1080
HALF = (960, 1080)

SILVER = ["-colorspace", "Gray", "-colorspace", "sRGB", "+level-colors", "#0d0a08,#efe6d6"]
COLOUR = ["-modulate", "96,72,100", "-fill", "#2a1d12", "-colorize", "6%"]


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


PLATE2 = "RecueildeplanchIVDide_0103.jp2"
PLATE1 = "RecueildeplanchIVDide_0099.jp2"
MAP = "cassini-triangles-1744.jpg"
ROOM = "harvard-computers.jpg"

# (output, original, window, tone, extra steps, size). Positions in the originals, read off a grid:
# plate II: the workshop is x 79 to 6241, y 439 to 2081; the pointers at their grindstones (Fig. 7) at x 600 to 1250,
#   the two wheels (Fig. 5 and 6) at x 1700 to 2700, the cutter on the floor (Fig. 4) at x 2680 to 2950, the
#   straightener (Fig. 2) at x 3230 to 3660, the hearth at x 3740 to 4170, y 1100 to 1700.
# plate I: the workshop is x 174 to 3282, y 537 to 2213; the wire drawer at his bench (fig. 4) at x 1820 to 2230.
# the map: Paris at about x 5710, y 2025, on the meridian line (x 5740); Laon x 6385, y 1700; Orleans x 5500, y 2775.
# the photograph: the standing computer at x 770 to 1030, the one with the magnifier at x 600 to 960.
JOBS = [
    # 0. the title: the whole pin workshop of plate II in the top half of the page, from the pointers on the left to
    #    the man at his wheel on the right; below the workshop the page is black, for the French and its English. The
    #    plate's lower figures fall under the black.
    ("b5-title", PLATE2, crop(450, 500, 5280), SILVER,
     darken(30) + fade("down", 0.48, 0.58, 1.0) + fade("up", 0.78, 1.0, 0.75) + foot(), (W, H)),
    # 1. Adam Smith: the wire drawer of plate I at his bench, the right half of a split screen
    ("b5-half-wire", PLATE1, crop(1700, 537, 1490, 9 / 8), SILVER,
     darken(20) + fade("left", 0.80, 1.0, 0.85, *HALF) + foot(*HALF), HALF),
    # 2. the task: the principal triangles around Paris, from Rouen to Reims, across the top of the page; the context
    #    text sits in the dark under them, as on the context frame of block 1, one line higher (four lines of text)
    ("b5-bg-map", MAP, crop(4100, 1450, 3200), COLOUR,
     darken(14) + fade("down", 0.35, 0.46, 0.92) + foot(), (W, H)),
    # 3. the three tiers: the computing room, the right half of a split screen
    ("b5-half-room", ROOM, crop(400, 0, 1335, 9 / 8), SILVER,
     darken(10) + fade("left", 0.80, 1.0, 0.85, *HALF) + foot(*HALF), HALF),
    # 4. the closing frame: the computing room, out of focus and almost gone in the dark
    ("b5-bg-close", ROOM, crop(0, 200, 1920), SILVER,
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
