#!/usr/bin/env python3
"""make_images.py: the pictures of the cold intro of block 1, cut and graded from one painting.

    python3 -I make_images.py ORIGINAL     # ORIGINAL is the full scroll, Songhuizong5.jpg

Get the original (9079 by 1846 pixels, 6,274,394 bytes, SHA-1 df2c9dd312a6d4d91e5681b55e0ccc4f5af82f81) with
    curl -L -A "Mozilla/5.0" -o Songhuizong5.jpg https://upload.wikimedia.org/wikipedia/commons/6/67/Songhuizong5.jpg

The painting is Emperor Huizong's Auspicious Cranes (1112), the right part of the scroll; the left part is his
calligraphy and the colophons. Every frame is one view of the painting: five fill the page (1920 by 1080 pixels)
and two are the picture half of a split screen (960 by 1080); the two closing frames share one. The scan is dark, so the levels are lifted, then the
saturation is set to 96 percent with a warm cast in the shadows. The page is darkened where the type sits, with
the gradient baked into the file, so that a projector shows what the PDF shows. The fades follow the Title
sequence of the course cold intro (w1-lecture-material, cold-intro/intro-slides/make_images.py)."""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1920, 1080

# the painting inside the scroll, in pixels of the original: x from 5990 to 8640, y from 25 to 1830.
# The scan is dark, so the levels are lifted first; then saturation 96 percent and a warm cast in the shadows.
GRADE = ["-level", "3%,84%,1.08", "-modulate", "100,96,100", "-fill", "#2a1d12", "-colorize", "4%"]


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


def foot():
    """the small print sits on the last 8 mm of the page: a veil there on every full page picture"""
    return fade("down", 0.84, 1.0, 0.62)


def darken(f):
    return ["-fill", "black", "-colorize", "%d%%" % f]


def crop(x, y, w, ratio=9 / 16):
    """a window of the original, w pixels wide (16:9 unless `ratio` says otherwise), its top left corner at (x, y)"""
    return ["-crop", "%dx%d+%d+%d" % (w, round(w * ratio), x, y)]


# (output, window, extra steps, size in pixels). Positions in the original, read off a grid: the flock flies at
# y 100 to 930; the two standing cranes stand on the ridge ends at x 6930 to 7090 and 7700 to 7790, y 940 to
# 1180; the ridge runs at y 1290 to 1330 and the eaves end at x 6420 and 8230, y 1540.
HALF = (960, 1080)
JOBS = [
    # 0. the title: the whole painting, the flock bright, the standing pair and the roof sunk in the dark under the
    #    title
    ("bg-title", crop(5990, 40, 2650),
     fade("down", 0.50, 0.72, 0.92) + fade("up", 0.0, 0.14, 0.40) + foot(), (W, H)),
    # 1. the setting: the two standing cranes facing each other on the ridge ends, the words under them on the roof
    ("bg-pair", crop(6720, 900, 1290),
     fade("down", 0.40, 0.52, 0.92) + foot(), (W, H)),
    # 2. the surprise: the left part of the flock, closer, the first line of the story under it. The window starts
    #    right of the collector's seal in the top left corner, and the dark starts higher than on the title, since
    #    the cranes are larger here
    ("bg-arrive", crop(6140, 60, 1400),
     fade("down", 0.44, 0.64, 0.95) + foot(), (W, H)),
    # 3. the king: the left half of the palace roof, the crane on its left ridge end, cranes flying above.
    #    The left half of a split screen, its right edge sinking into the ground of the page
    ("half-court", crop(6300, 480, 1200, 9 / 8),
     fade("right", 0.80, 1.0, 0.85, *HALF) + fade("down", 0.84, 1.0, 0.62, *HALF), HALF),
    # 4. the answer: the right half of the flock and the crane on the right ridge end. The right half of a split
    #    screen, its left edge sinking into the ground of the page
    ("half-flock", crop(7290, 25, 1350, 9 / 8),
     fade("left", 0.80, 1.0, 0.85, *HALF) + fade("down", 0.84, 1.0, 0.62, *HALF), HALF),
    # 5. what Kun says next: the right part of the flock, his words and their explanation under it
    ("bg-kind", crop(7100, 25, 1540),
     fade("down", 0.40, 0.50, 0.92) + foot(), (W, H)),
    # 6 and 7. representation learning and its uses: the flock, out of focus and almost gone in the dark
    ("bg-map", crop(6260, 25, 2150),
     ["-blur", "0x6"] + darken(80) + foot(), (W, H)),
]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    original = sys.argv[1]
    os.makedirs(os.path.join(HERE, "img"), exist_ok=True)
    for out, window, steps, size in JOBS:
        cmd = (["magick", original] + window + ["+repage", "-resize", "%dx%d!" % size]
               + GRADE + steps + ["-quality", "88", os.path.join(HERE, "img", out + ".jpg")])
        subprocess.run(cmd, check=True)
        print("ok", out)


if __name__ == "__main__":
    main()
