#!/usr/bin/env python3
# Copied on 2026-11-03 from eth-ainit-hs26/w1-lecture-material, commit 34bce22, file llm-deck/tools/make_handout.py.
"""make_handout.py deck.pdf handout.pdf [title]

A handout of a deck: one page for each frame, the page where the frame's last click shows. The page ranges of
the frames come from deck.nav (\\beamer@framepages), so build the deck first. The pages are copied, not
typeset again, so the handout looks exactly like the room's last view of each frame.

Why not beamer's own handout option: it draws every piece of a frame at once, and a frame whose clicks replace
each other (the three questions on the table, the film subtitles) piles them on top of one another.

Needs pypdf. Run it from llm-deck/:   python3 tools/make_handout.py geez-slides.pdf geez-handout.pdf"""
import re
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def main():
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    deck = Path(sys.argv[1])
    out = Path(sys.argv[2])
    nav = deck.with_suffix(".nav")
    if not nav.exists():
        sys.exit("%s not found: build the deck first" % nav)
    last = [int(b) for _, b in re.findall(r"\\beamer@framepages\s*\{(\d+)\}\{(\d+)\}",
                                          nav.read_text(encoding="utf-8", errors="replace"))]
    reader = PdfReader(str(deck))
    assert last and max(last) <= len(reader.pages), (last[-3:], len(reader.pages))
    writer = PdfWriter()
    for p in last:
        writer.add_page(reader.pages[p - 1])
    title = sys.argv[3] if len(sys.argv) == 4 else None
    meta = dict(reader.metadata or {})
    if title:
        meta["/Title"] = title
    writer.add_metadata({k: str(v) for k, v in meta.items() if k in ("/Title", "/Author")})
    with open(out, "wb") as f:
        writer.write(f)
    print("%s: %d pages, the last click of each of %d frames of %s (%d pages)"
          % (out, len(last), len(last), deck, len(reader.pages)))


if __name__ == "__main__":
    main()
