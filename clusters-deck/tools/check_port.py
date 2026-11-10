#!/usr/bin/env python3
"""check_port.py: every number printed on the slides of block5-computing-clusters.pdf must be one the FDD deck
already prints (w7-cost-slides.tex, the source of this port) or one of the facts this port added, listed below
with its source. Run from clusters-deck/ after a build:

    python3 tools/check_port.py

It reads the text of every page with pdftotext, drops the footer (folio and slug), and prints each number that
is in neither place. Exit status 1 if there is one. Numbers glued to letters (GH200, EX254n, MI300A) are names
and are skipped, as are the digits of a link's address.
"""
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
DECK = HERE / "block5-computing-clusters.pdf"
FDD = (pathlib.Path.home() / "Documents/git_fdd/projects/weekend-07-large-scale/carlos-lectures/slides"
       / "w7-cost-slides.tex")

# The numbers this port prints that FDD's slides do not, each with where it comes from. The small integers of the
# platform frames (alps-platform-frame.tex) would pass anyway, since FDD prints them in other places; they are
# listed so that their sources are written down.
ADDED = {
    "14": "the date of the block, Saturday 14 November 2026",
    "54": "the photograph's NASA number, E49-54 (FDD slides/img/SOURCES.md)",
    "8": "HPE QuickSpecs v22 (a00094635enw): 8 chassis a cabinet, 8 compute blade slots a chassis; "
         "8 GH200 a blade, two nodes of four",
    "7": "docs.cscs.ch/alps/hardware: Alps's GH200 chassis are underpopulated, 7 blades of 8 (1,344 blades "
         "in 24 cabinets)",
    "24": "CSCS, 24 cabinets of 112 nodes (FDD NUMBERS.md, G8)",
    "2": "HPE QuickSpecs v22: EX254n, two 4-socket GH200 nodes; EX235n, EX235a, EX255a two nodes, EX4252 four "
         "nodes of 2 CPUs",
}

NUM = re.compile(r"(?<![\w.])\d+(?:[,.]\d+)*(?![\w])")


def numbers(text):
    out = set()
    for m in NUM.finditer(text):
        out.add(m.group(0).replace(",", "").rstrip("."))
    return out


def main():
    if not DECK.exists():
        sys.exit(f"build the deck first: {DECK.name} is missing")
    fdd = FDD.read_text(encoding="utf-8")
    fdd_numbers = numbers(fdd)
    pages = int(re.search(r"Pages:\s+(\d+)",
                          subprocess.run(["pdfinfo", str(DECK)], capture_output=True, text=True).stdout).group(1))
    missing = {}
    for p in range(1, pages + 1):
        text = subprocess.run(["pdftotext", "-f", str(p), "-l", str(p), str(DECK), "-"],
                              capture_output=True, text=True).stdout
        lines = [ln for ln in text.splitlines() if "AI in Industry, weekend 2" not in ln]
        body = "\n".join(lines)
        body = re.sub(r"\S+\.(?:ch|org|com)\S*", " ", body)  # link addresses
        body = re.sub(r"arXiv \d{4}\.\d{5}", " ", body)        # arXiv identifiers
        # pdftotext sets a power of ten as one number: "x 10^12" reads "x 1012" and "= 10^6" reads "= 106"
        body = re.sub(r"([×=]\s*)10(\d{1,2})\b", r"\g<1>10 \2", body)
        for n in numbers(body):
            if n in fdd_numbers or n in ADDED:
                continue
            missing.setdefault(n, p)
    if missing:
        for n, p in sorted(missing.items(), key=lambda kv: kv[1]):
            print(f"page {p}: {n} is in neither the FDD deck nor the list of added facts")
        sys.exit(1)
    print(f"check_port: every number on the {pages} pages is FDD's or a listed added fact")


if __name__ == "__main__":
    main()
