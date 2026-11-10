#!/usr/bin/env python3
# Copied on 2026-11-10 from eth-ainit-hs26/w1-lecture-material, commit c45b754, file cold-intro/design/tools/check_overlays_any.py.
"""check_overlays_any.py deck.pdf: the no-jump check for a page of either polarity.

../../style/tools/check_overlays.py counts as ink only what is DARKER than the ground, which is right for the
vellum and blind on a dark page (v1 and v2 of design/), where the type is lighter than the ground. This variant
counts as ink every pixel that differs from the ground by more than MARGIN in either direction, and otherwise
does the same: for every frame of several clicks, every mark visible on an earlier click must be on the last
click, in place, within a 2 pixel tolerance. On the last click a pixel already counts as ink at half the margin:
a word that turns from ivory to gold on a dark wall keeps its place, but the anti-aliased edge of the gold
glyph is dimmer, and at the full margin those edge pixels (8 of them on v1, 1 on v2) read as ink that went away.
Frame page ranges come from deck.nav. Exit status 1 on stray ink.
Needs numpy, Pillow, scipy and pdftoppm."""
import pathlib
import re
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image
from scipy.ndimage import binary_dilation

DPI, MARGIN = 100, 60


def render(pdf, page, tmp):
    stem = pathlib.Path(tmp) / ("p%d" % page)
    subprocess.run(["pdftoppm", "-png", "-r", str(DPI), "-f", str(page), "-l", str(page), "-singlefile",
                    str(pdf), str(stem)], check=True)
    return np.array(Image.open(str(stem) + ".png").convert("L")).astype(int)


def main(pdf):
    pdf = pathlib.Path(pdf)
    frames = [(int(a), int(b)) for a, b in re.findall(r"\\beamer@framepages\s*\{(\d+)\}\{(\d+)\}",
                                                       pdf.with_suffix(".nav").read_text())]
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        for n, (a, b) in enumerate(frames, 1):
            if a == b:
                continue
            last = render(pdf, b, tmp)
            ground = np.median(last)
            final = binary_dilation(np.abs(last - ground) > MARGIN / 2, iterations=2)
            worst = max(int(((np.abs(render(pdf, p, tmp) - ground) > MARGIN) & ~final).sum()) for p in range(a, b))
            print("frame %2d (pages %d-%d): %d stray pixels  %s" % (n, a, b, worst, "ok" if worst == 0 else "STRAY INK"))
            bad += worst > 0
    print("no-jump check, either polarity:", "passed" if bad == 0 else "%d frame(s) move between clicks" % bad)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
