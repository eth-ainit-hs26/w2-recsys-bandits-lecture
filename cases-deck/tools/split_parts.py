#!/usr/bin/env python3
"""split_parts.py cases.pdf

Writes one PDF per part of the talk, so that each part opens on its own at the end of its
lecture: case1-nearest-neighbours.pdf to case4-gradient-descent.pdf. The pages are copied from cases.pdf, clicks
included, so a part looks exactly like the same frames in the whole deck. The page ranges of
the frames come from cases.nav (\\beamer@framepages), so build the deck first. PARTS says
which frames (counted from 1) belong to which part; the script fails if the deck has another
number of frames. Needs pypdf. Run it from cases-deck/."""
import re
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

# part number -> (file name, frames of the deck in that part, PDF title)
PARTS = {
    1: ("case1-nearest-neighbours.pdf", [1], "Case 1: after the nearest neighbours"),
    2: ("case2-matrix-factorization.pdf", [2], "Case 2: after matrix factorization"),
    3: ("case3-bandits.pdf", [3], "Case 3: after the bandits"),
    4: ("case4-gradient-descent.pdf", [4, 5], "Case 4: after gradient descent, and the map"),
}


def main():
    deck = Path(sys.argv[1] if len(sys.argv) > 1 else "cases.pdf")
    nav = deck.with_suffix(".nav")
    if not nav.exists():
        sys.exit("%s not found: build the deck first" % nav)
    frames = [(int(a), int(b)) for a, b in re.findall(
        r"\\beamer@framepages\s*\{(\d+)\}\{(\d+)\}",
        nav.read_text(encoding="utf-8", errors="replace"))]
    wanted = sorted(f for _, fs, _ in PARTS.values() for f in fs)
    if wanted != list(range(1, len(frames) + 1)):
        sys.exit("the deck has %d frames; PARTS covers %s" % (len(frames), wanted))
    reader = PdfReader(str(deck))
    for name, fs, title in PARTS.values():
        writer = PdfWriter()
        for f in fs:
            first, last = frames[f - 1]
            for p in range(first, last + 1):
                writer.add_page(reader.pages[p - 1])
        writer.add_metadata({"/Title": title, "/Author": "Carlos Cotrini"})
        with open(deck.parent / name, "wb") as out:
            writer.write(out)
        print("%s: frames %s, %d pages" % (name, fs, len(writer.pages)))


if __name__ == "__main__":
    main()
