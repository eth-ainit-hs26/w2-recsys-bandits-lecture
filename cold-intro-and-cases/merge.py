"""One PDF per block of weekend 2: the block's cold intro, then its business cases, and for the 16:00 block the
lecture deck after them.

Carlos, 2026-11-12: "Nearest neighbors cold intro is going to be merged now with business case, Etsy, and Airbnb. So
they become now together number two, and I want you to call it nearest neighbors", the same for the bandits block and
for large-scale computing, "And always put the cold intro with the business on top at the beginning before the rest of
the material ... make that for each block the first chip." For the 16:00 block he had asked for "large-scale computing
cold intro with business case, LinkedIn ads, then computing clusters in that order", and later the same day: "Notice
the slides on large-scale computing and computing clusters. Merge them, I meant", so its PDF ends with the clusters
deck.

The PDFs are concatenated page by page with pypdf, so every page stays the page its deck built. A bookmark marks
where each deck starts; the decks' own bookmarks and page labels are left out, so a viewer counts the pages 1 to N.

Run from this folder after a rebuild of any deck below (the decks are built in their own folders):

    python3 -I merge.py

It checks that every page of the output has the size and the text of its source page, and that every link to a page
of the file lands on the page its own deck meant.

Beamer names its link targets after the page number ("Navigation2" is page 2), so two decks share names, and in a
concatenation the first deck's targets win: the section title on a divider page of the second deck then jumped to a
page of the first. Every such link is therefore rewritten to point at its page directly.
"""
import pathlib
import sys

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, NameObject

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
    ("block4-large-scale-computing.pdf", "Large-scale computing, cold intro, business case and computing clusters", [
        ("cold-intro-deck/block5-computing-clusters.pdf", "Cold intro: Dividing a computation, 1793"),
        ("cases-deck/block4-parallelized-mf.pdf", "Business case: LinkedIn's ads"),
        ("clusters-deck/block5-computing-clusters.pdf", "Computing clusters"),
    ]),
]


def size(page):
    box = page.mediabox
    return round(float(box.width), 2), round(float(box.height), 2)


def page_of_name(reader):
    """Each named link target of one deck, and the index of its page in that deck."""
    index = {p.indirect_reference.idnum: i for i, p in enumerate(reader.pages)}
    pages = {}
    for name, dest in reader.named_destinations.items():
        idnum = getattr(dest.page, "idnum", None)
        if idnum in index:
            pages[name] = index[idnum]
    return pages


def goto_actions(page):
    """The GoTo actions of the links on a page, in their order."""
    for annot in page.get("/Annots") or []:
        action = annot.get_object().get("/A")
        if action is not None and action.get_object().get("/S") == "/GoTo":
            yield action.get_object()


def merge(out, title, parts):
    writer = PdfWriter()
    sources = []
    owners = []  # for each page of the output: the named targets of its deck, and where that deck starts
    for path, mark in parts:
        reader = PdfReader(ROOT / path)
        start = len(writer.pages)
        writer.append(reader, outline_item=mark, import_outline=False)
        sources.extend((path, i, page) for i, page in enumerate(reader.pages))
        names = page_of_name(reader)
        owners.extend((path, names, start) for _ in reader.pages)
    if "/PageLabels" in writer._root_object:
        del writer._root_object["/PageLabels"]

    errors = []
    targets = []  # (output page, link target page), both counted from 0, in the order of the links
    for k, (path, names, start) in enumerate(owners):
        for action in goto_actions(writer.pages[k]):
            dest = action.get("/D")
            if isinstance(dest, str) and dest in names:
                target = start + names[dest]
                action[NameObject("/D")] = ArrayObject([writer.pages[target].indirect_reference, NameObject("/Fit")])
                targets.append((k, target))
            else:
                errors.append(f"{out} page {k + 1}: a link of {path} has the target {dest!r}, not a name of that deck")
    writer.add_metadata({"/Title": title, "/Author": "Carlos Cotrini",
                         "/Subject": "AI in Industry, ETH Zurich, HS26, weekend 2"})
    with open(HERE / out, "wb") as fh:
        writer.write(fh)

    merged = PdfReader(HERE / out)
    index = {p.indirect_reference.idnum: i for i, p in enumerate(merged.pages)}
    landed = []
    for k, page in enumerate(merged.pages):
        for action in goto_actions(page):
            dest = action.get("/D")
            landed.append((k, index.get(dest[0].idnum) if isinstance(dest, list) else None))
    if landed != targets:
        errors.append(f"{out}: the links land on {landed}, expected {targets} (output page, target page, from 0)")
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
