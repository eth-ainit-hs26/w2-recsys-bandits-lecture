#!/usr/bin/env python3
"""check_numbers.py cases.pdf [expected file]

Reads the numbers back from the RENDERED PDF (pdftotext) and fails if any string that
tools/cases_numbers.py expects is missing. A macro can drop or garble a number silently,
so the check runs on the PDF, never on the source. Run from cases-deck/ after the build.
Copied on 2026-11-04 from ../opener-deck/tools/check_numbers.py. Changed: the default file, and the text is
read twice, in layout mode and in reading order, because a phrase that wraps inside one column of a case card
is split by the other column in layout mode. A string passes when either reading holds it. Since 2026-11-06 an
optional second argument names the expected file, for the block decks: tools/expected-block1-nearest-neighbors.txt and the like."""
import subprocess
import sys
from pathlib import Path

pdf = sys.argv[1] if len(sys.argv) > 1 else "cases.pdf"
readings = []
for mode in (["-layout"], []):
    out = subprocess.run(["pdftotext"] + mode + [pdf, "-"], capture_output=True, text=True, check=True).stdout
    readings.append(" ".join(out.split()))
text = "\n".join(readings)
expfile = sys.argv[2] if len(sys.argv) > 2 else "tools/expected.txt"
expected = [s for s in Path(expfile).read_text(encoding="utf-8").splitlines() if s]
missing = [s for s in expected if s not in text]
for s in expected:
    print("%-12s %s" % ("ok" if s not in missing else "MISSING", s))
if missing:
    sys.exit("%d of %d numbers missing from %s" % (len(missing), len(expected), pdf))
print("all %d numbers found in %s" % (len(expected), pdf))
