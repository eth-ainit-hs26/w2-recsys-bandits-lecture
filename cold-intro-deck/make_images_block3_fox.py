#!/usr/bin/env python3
"""make_images_block3_fox.py: the pictures of THE FOX, one of the three drafts of the cold intro of block 3 (bandits),
"Estimating chances from the past", cut and graded from three public domain engravings of Aesop's fable of the old
lion and the fox. make_images.py and make_images_block5.py make the pictures of blocks 1 and 5 and are not touched.

    python3 -I make_images_block3_fox.py ORIGDIR [OUTDIR]     # OUTDIR defaults to img/

ORIGDIR holds the three originals under these names (sizes, bytes and SHA-1 of the files downloaded on 2026-11-11):

  dore-lion-malade-1876.png        2201 x 2781,  2,562,608 bytes, SHA-1 b1b11e309be18692021ef263e5cb3a2c0d4494a1
      Gustave Dore (1832 to 1883), Le Lion malade et le Renard, wood engraving signed "H. Pisan" (Heliodore Pisan,
      1822 to 1890), in the Polish edition of La Fontaine's Fables, Bajki, Warsaw: Jan Noskowski, 1876, scanned by
      the Lower Silesian Digital Library (DBC), cropped and cleaned on Commons.
      Commons page https://commons.wikimedia.org/wiki/File:PL_Jean_de_La_Fontaine_Bajki_1876_page449.png
      Licence in the Commons API: "Public domain" (template PD-old-100-1923).
      curl -L -A "Mozilla/5.0" -o dore-lion-malade-1876.png "https://upload.wikimedia.org/wikipedia/commons/1/1e/PL_Jean_de_La_Fontaine_Bajki_1876_page449.png"
  A212104_0252.jp2                 3842 x 6224,  4,317,434 bytes, SHA-1 7a8b74be2a33ef17141e68779500741282a6737f
      Jean-Baptiste Oudry (1686 to 1755), design, and Pierre Quentin Chedel (1705 to 1763), engraving, "Le Lion malade
      et le Renard. Fable CXVII", in La Fontaine, Fables choisies, mises en vers, tome 2, Paris: Desaint & Saillant,
      Durand, 1755, the copy of the Biblioteca de la Universidad de Sevilla; Internet Archive item A212104, leaf n252
      (this item numbers its jp2 files as its leaves). Licence in the Archive's metadata: Public Domain Mark 1.0.
      The same scan is on Commons as File:Fables choisies, mises en vers T. 2 (IA A212104).pdf.
      Archive page https://archive.org/details/A212104/page/n252
      curl -L -A "Mozilla/5.0" -o A212104_0252.jp2 "https://archive.org/download/A212104/A212104_jp2.zip/A212104_jp2%2FA212104_0252.jp2"
  hollar-sick-lion.jpg             4499 x 6073, 12,589,029 bytes, SHA-1 a62c315bd617bb522979241ba17c5926b9ab1830
      Wenceslaus Hollar (1607 to 1677), The sick lion, etching, "W Hollar inv: fec:", Pennington 363, University of
      Toronto, Wenceslaus Hollar Digital Collection. The plate faces fable XXXVIII, "Of the Lyon that was Sick", in
      John Ogilby, The Fables of Aesop Paraphras'd in Verse, London: Thomas Roycroft, 1668 (Internet Archive item
      fablesofaesopparogil, leaf n176); there the fox "many Tracts espi'd / Of Visitants repaired to's Royal Den; /
      But saw no Print of those return'd agen".
      Commons page https://commons.wikimedia.org/wiki/File:Wenceslas_Hollar_-_The_sick_lion.jpg
      Licence in the Commons API: "Public domain".
      curl -L -A "Mozilla/5.0" -o hollar-sick-lion.jpg "https://upload.wikimedia.org/wikipedia/commons/5/50/Wenceslas_Hollar_-_The_sick_lion.jpg"

Downloaded files are untrusted data: keep ORIGDIR outside the repository and run this script with python3 -I.

The grade follows block 5 (make_images_block5.py): the engravings become a warm silver, and the white paper is pulled
down so that no page glares on the projector. Dore's wood engraving is mostly grey hatching in this scan, so its levels
are spread first. The page is darkened where the type sits, with the gradient baked into the file."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1920, 1080
HALF = (960, 1080)

SILVER = ["-colorspace", "Gray", "-colorspace", "sRGB", "+level-colors", "#0d0a08,#efe6d6"]
SPREAD = ["-level", "18%,95%,0.8"]


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


def veil(cx, cy, rx, ry, strength, w=W, h=H):
    """a soft dark ellipse centred at (cx, cy) with radii rx and ry, `strength` black at its centre: it calms the
    hatching under a line of small type"""
    return ["(", "-size", "%dx%d" % (w, h), "-define", "gradient:center=%d,%d" % (cx, cy),
            "-define", "gradient:radii=%d,%d" % (rx, ry),
            "radial-gradient:rgba(0,0,0,%.2f)-rgba(0,0,0,0)" % strength, ")", "-compose", "over", "-composite"]


def crop(x, y, w, ratio=9 / 16):
    """a window of the original, w pixels wide (16:9 unless `ratio` says otherwise), its top left corner at (x, y)"""
    return ["-crop", "%dx%d+%d+%d" % (w, round(w * ratio), x, y)]


DORE = "dore-lion-malade-1876.png"
OUDRY = "A212104_0252.jp2"
HOLLAR = "hollar-sick-lion.jpg"

# (output, original, window, tone, extra steps, size). Positions in the originals, read off a grid:
# Dore: the mouth of the cave is x 870 to 1760, y 200 to 1400; at its foot the stag x 980 to 1100, the fox x 1180 to
#   1300 and a bear x 1220 to 1370, y 1150 to 1350; the ox comes in at x 1240 to 1500, y 1360 to 1700; the lion lies
#   at x 220 to 1600, y 1590 to 2050, his head at x 420 to 720; bones at x 1100 to 1850, y 2150 to 2380.
# Oudry: the plate is x 345 to 3395, y 810 to 4705 of the page (its caption below); the lion lies at x 750 to 1900,
#   y 2150 to 2560, the bones before him at x 500 to 1000, y 2480 to 2650; the fox at x 2200 to 3200, y 3200 to 4300;
#   the tracks at x 1300 to 2400, y 4380 to 4650. The library's stamp touches the plate at x 3315 and beyond, y 3880
#   to 4250, so no window goes right of x 3300.
# Hollar: the fox stands at x 0 to 1110, y 3300 to 4250; the crown and sceptre on the rock at x 1650 to 2550, y 2300
#   to 2650; the lion's head at x 2700 to 3600, y 2900 to 4000; his prey at x 2350 to 4100, y 3900 to 4600; the dead
#   stag, boar and hare at y 4400 to 6000.
JOBS = [
    # 0. the title: Dore's cave from inside, the animals coming in at the bright mouth; the lion lies in the dark
    #    under the title. A veil on the rock at the top left carries the kicker
    ("b3f-title", DORE, crop(250, 760, 1750), SPREAD + SILVER,
     darken(8) + veil(420, 115, 760, 230, 0.82) + fade("down", 0.50, 0.70, 0.94) + foot(), (W, H)),
    # 1. the setting: Oudry's lion lying at the mouth of his cave, the bones before him, the bushes on the right;
    #    the words in the dark under them, as on the context frame of block 1, which sits 3 mm higher here because
    #    its question takes two lines
    ("b3f-bg-cave", OUDRY, crop(345, 1950, 2900), SILVER,
     darken(22) + fade("down", 0.37, 0.49, 0.94) + foot(), (W, H)),
    # 2. the surprise: Hollar's fox standing at a distance from the cave, the lion inside with his prey; the Greek
    #    and its English in the black under them, as on the title frame of block 5
    ("b3f-bg-distance", HOLLAR, crop(0, 3100, 4499), SILVER,
     darken(24) + fade("down", 0.48, 0.58, 1.0) + foot(), (W, H)),
    # 3. the lion: Hollar's lion close, his paws on his prey. The left half of a split screen, its right edge
    #    sinking into the ground of the page; the light fur of the prey is veiled under the picture credit
    ("b3f-half-lion", HOLLAR, crop(2549, 2380, 1950, 9 / 8), SILVER,
     darken(20) + fade("right", 0.80, 1.0, 0.85, *HALF) + fade("down", 0.78, 0.95, 0.88, *HALF), HALF),
    # 4. the fox: Oudry's fox, head down over the tracks on the ground. The right half of a split screen,
    #    its left edge sinking into the ground of the page; the window runs below the plate, and the page is black
    #    from the plate's lower edge (row 866 of 1080), so that the credit sits on black under the tracks
    ("b3f-half-fox", OUDRY, crop(1280, 2900, 2000, 9 / 8), SILVER,
     darken(20) + fade("left", 0.80, 1.0, 0.85, *HALF) + fade("down", 0.75, 0.80, 1.0, *HALF), HALF),
    # 5. the moral: Dore's lion lying inside the cave, what the fox cannot see; the bones on the floor fall under
    #    the dark of the words
    ("b3f-bg-inside", DORE, crop(0, 1540, 2201), SPREAD + SILVER,
     darken(8) + fade("down", 0.40, 0.50, 0.94) + foot(), (W, H)),
    # 6 and 7. the estimate and its uses: the cave of the title, out of focus and almost gone in the dark
    ("b3f-bg-close", DORE, crop(0, 850, 2201), SPREAD + SILVER,
     ["-blur", "0x6"] + darken(72) + foot(), (W, H)),
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
