#!/usr/bin/env python3
# Copied on 2026-11-03 from eth-ainit-hs26/w1-lecture-material, commit 9792819, file style/tools/render_board.py.
"""render_board.py deck.pdf [outdir]

Renders the LAST overlay page of every frame (every piece revealed, the page where collisions
live) at 150 dpi to outdir/s1.png, s2.png and so on, and assembles outdir/board.png, a contact
sheet of thumbnails in three columns. Read the pages at full size: a render you do not look at is
no verification. Frame page ranges come from beamer's deck.nav, so build the deck first. Needs
pdftoppm and ImageMagick (magick)."""
import re, subprocess, sys, pathlib

def main(pdf, outdir):
    pdf = pathlib.Path(pdf)
    nav = pdf.with_suffix(".nav")
    if not nav.exists():
        sys.exit(f"{nav} not found: build the deck first")
    pages = [int(b) for _, b in re.findall(
        r"\\beamer@framepages\s*\{(\d+)\}\{(\d+)\}",
        nav.read_text(encoding="utf-8", errors="replace"))]
    out = pathlib.Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("s*.png"):
        old.unlink()
    files = []
    for i, p in enumerate(pages, 1):
        stem = out / f"s{i}"
        subprocess.run(["pdftoppm", "-png", "-r", "150", "-f", str(p), "-l", str(p),
                        "-singlefile", str(pdf), str(stem)], check=True)
        files.append(f"{stem}.png")
    board = out / "board.png"
    subprocess.run(["magick", "montage", *files, "-tile", "3x", "-geometry", "630x+8+8",
                    "-background", "#6b7280", str(board)], check=True)
    print(f"{len(pages)} frames, last pages {pages} -> {board}")

if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else "board-out")
