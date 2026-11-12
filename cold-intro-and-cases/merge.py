"""One PDF per block of weekend 2: the block's cold intro, then its business cases.

Carlos, 2026-11-12: "Nearest neighbors cold intro is going to be merged now with business case, Etsy, and Airbnb. So
they become now together number two, and I want you to call it nearest neighbors", the same for the bandits block and
for large-scale computing, "And always put the cold intro with the business on top at the beginning before the rest of
the material ... make that for each block the first chip."

The PDFs are concatenated page by page with pypdf, so every page stays the page its deck built. A bookmark marks
where each deck starts; the decks' own bookmarks and page labels are left out, so a viewer counts the pages 1 to N.

Run from this folder after a rebuild of any deck below (the decks are built in their own folders):

    python3 -I merge.py

It checks that every page of the output has the size and the text of its source page.
"""
import pathlib
import sys

from pypdf import PdfReader, PdfWriter

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

# output file, its title, then (source deck, bookmark) in the order of the pages
BLOCKS = [
    ("block1-nearest-neighbors.pdf", "Nearest neighbors, cold intro and business cases", [
        ("cold-intro-deck/block1-nearest-neighbors.pdf", "Cold intro: Searching through representations"),
        ("cases-deck/block1-nearest-neighbors.pdf", "Business cases: Etsy and Airbnb"),
    ]),
    ("block3-bandits.pdf", "Bandits, cold intro and business cases", [
        ("cold-intro-deck/block3-bandits-graunt.pdf", "Cold intro: Estimating chances from the past"),
        ("cases-deck/block3-bandits.pdf", "Business cases: Spotify's home page and Amazon Payments"),
    ]),
    ("block4-large-scale-computing.pdf", "Large-scale computing, cold intro and business case", [
        ("cold-intro-deck/block5-computing-clusters.pdf", "Cold intro: Dividing a computation, 1793"),
        ("cases-deck/block4-parallelized-mf.pdf", "Business case: LinkedIn's ads"),
    ]),
]


def size(page):
    box = page.mediabox
    return round(float(box.width), 2), round(float(box.height), 2)


def merge(out, title, parts):
    writer = PdfWriter()
    sources = []
    for path, mark in parts:
        reader = PdfReader(ROOT / path)
        writer.append(reader, outline_item=mark, import_outline=False)
        sources.extend((path, i, page) for i, page in enumerate(reader.pages))
    if "/PageLabels" in writer._root_object:
        del writer._root_object["/PageLabels"]
    writer.add_metadata({"/Title": title, "/Author": "Carlos Cotrini",
                         "/Subject": "AI in Industry, ETH Zurich, HS26, weekend 2"})
    with open(HERE / out, "wb") as fh:
        writer.write(fh)

    merged = PdfReader(HERE / out)
    errors = []
    if len(merged.pages) != len(sources):
        errors.append(f"{out}: {len(merged.pages)} pages, expected {len(sources)}")
    for k, (page, (path, i, src)) in enumerate(zip(merged.pages, sources)):
        if size(page) != size(src):
            errors.append(f"{out} page {k + 1}: size {size(page)}, {path} page {i + 1} has {size(src)}")
        if page.extract_text() != src.extract_text():
            errors.append(f"{out} page {k + 1}: text differs from {path} page {i + 1}")
    print(f"{out}: {len(merged.pages)} pages ({' + '.join(str(len(PdfReader(ROOT / p).pages)) for p, _ in parts)})")
    return errors


if __name__ == "__main__":
    problems = []
    for block in BLOCKS:
        problems += merge(*block)
    for p in problems:
        print("ERROR", p)
    sys.exit(1 if problems else 0)
