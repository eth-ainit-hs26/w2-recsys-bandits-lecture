#!/usr/bin/env python3
# Copied on 2026-11-03 from eth-ainit-hs26/w1-lecture-material, commit 9792819, file style/tools/check_overlays.py.
"""check_overlays.py deck.pdf [--allow N,N,...]

The no-jump check. For every frame that expands into several overlay pages, render each page and
test that every mark visible on an earlier click is also on the last click, in the same place
(allowing a 2 pixel tolerance for anti-aliasing). A diagram that reflows when a piece appears
leaves stray ink on the early clicks, and the check reports it. Frame page ranges come from beamer's
own deck.nav, so build the deck first. Exit status 1 if any frame has stray ink.

--allow N,N lists frames (counted as the check prints them) whose clicks replace each other on purpose,
such as the subtitles of a spoken welcome, where each line takes the place of the one before. Their
stray ink is printed and not counted. Name every such frame in the deck's CLAUDE.md, because a number
does not follow a frame that is moved.

Needs numpy, Pillow and scipy, and pdftoppm on the path."""
import re, subprocess, sys, tempfile, pathlib
import numpy as np
from PIL import Image
from scipy.ndimage import binary_dilation

DPI = 100
MARGIN = 60          # a pixel counts as ink when it is this much darker than the ground

def frame_pages(nav):
    text = pathlib.Path(nav).read_text(encoding="utf-8", errors="replace")
    return [(int(a), int(b)) for a, b in
            re.findall(r"\\beamer@framepages\s*\{(\d+)\}\{(\d+)\}", text)]

def render(pdf, page, tmp):
    stem = pathlib.Path(tmp) / f"p{page}"
    subprocess.run(["pdftoppm", "-png", "-r", str(DPI), "-f", str(page), "-l", str(page),
                    "-singlefile", str(pdf), str(stem)], check=True)
    return np.array(Image.open(f"{stem}.png").convert("L")).astype(int)

def main(pdf, allow=()):
    pdf = pathlib.Path(pdf)
    nav = pdf.with_suffix(".nav")
    if not nav.exists():
        sys.exit(f"{nav} not found: build the deck first")
    bad = 0
    with tempfile.TemporaryDirectory() as tmp:
        for n, (a, b) in enumerate(frame_pages(nav), 1):
            if b == a:
                continue
            last = render(pdf, b, tmp)
            ground = np.median(last)
            final_ink = binary_dilation(last < ground - MARGIN, iterations=2)
            worst = max(int(((render(pdf, p, tmp) < ground - MARGIN) & ~final_ink).sum())
                        for p in range(a, b))
            allowed = worst > 0 and n in allow
            status = "ok" if worst == 0 else ("REPLACES ON PURPOSE (allowed)" if allowed else "STRAY INK")
            print(f"frame {n:2d} (pages {a}-{b}): {worst} stray pixels  {status}")
            bad += worst > 0 and not allowed
    print("no-jump check:", "passed" if bad == 0 else f"{bad} frame(s) move between clicks")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    args = sys.argv[1:]
    allow = ()
    if len(args) == 3 and args[1] == "--allow":
        allow = tuple(int(x) for x in args[2].split(",") if x)
        args = args[:1]
    if len(args) != 1:
        sys.exit(__doc__)
    main(args[0], allow)
