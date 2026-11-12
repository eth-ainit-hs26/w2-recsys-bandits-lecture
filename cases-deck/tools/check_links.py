#!/usr/bin/env python3
"""Checks that every source line of a case links to its document.

Usage, from cases-deck/:
    python3 tools/check_links.py block1-nearest-neighbors.pdf [more PDFs]

Reads the pairs \\weblink{url}{citation} from the source macros of the *-frames.tex files of cases-deck/, then, for
every page of each PDF whose text shows a citation, asserts that the page carries a link (a URI annotation) to that
citation's url. Works on the block decks, the weekend deck and the merged PDFs of ../cold-intro-and-cases/, whose
merge.py rewrites internal links only. Asked for by Carlos on 2026-11-12: "put hyperlinks in the citations of the
business cases so that if a participant is curious, they can click and find the paper".
"""
import pathlib
import re
import sys

from pypdf import PdfReader

FRAMES = pathlib.Path(__file__).resolve().parent.parent
PAIR = re.compile(r"\\weblink\{([^}]*)\}\{([^}]*)\}")


def citations():
    """(frames file, url, citation) for every \\weblink outside a comment."""
    out = []
    for f in sorted(FRAMES.glob("*-frames.tex")):
        for line in f.read_text().splitlines():
            if not line.lstrip().startswith("%"):
                out += [(f.name, url, text) for url, text in PAIR.findall(line)]
    return out


def norm(s):
    return " ".join(s.replace("\u2019", "'").split())


def uris(page):
    found = []
    for annot in page.get("/Annots") or []:
        action = annot.get_object().get("/A")
        if action is not None and action.get_object().get("/S") == "/URI":
            found.append(str(action.get_object().get("/URI")))
    return found


def check(pdf, pairs):
    reader = PdfReader(pdf)
    shown, failures, seen = 0, [], set()
    for number, page in enumerate(reader.pages, start=1):
        text, links = norm(page.extract_text() or ""), uris(page)
        for name, url, citation in pairs:
            if norm(citation) in text:
                shown += 1
                seen.add(citation)
                if url not in links:
                    failures.append("page %d: '%s' without its link %s" % (number, citation, url))
    print("%s: %d pages, %d source citations shown, %d without their link; citations: %s"
          % (pdf, len(reader.pages), shown, len(failures), "; ".join(sorted(seen)) or "none"))
    for f in failures:
        print("   " + f)
    return not failures and shown > 0


def main():
    pairs = citations()
    assert pairs, "no \\weblink in the source macros of %s" % FRAMES
    ok = [check(pdf, pairs) for pdf in sys.argv[1:]]
    sys.exit(0 if ok and all(ok) else 1)


if __name__ == "__main__":
    main()
