#!/usr/bin/env python3
"""check_numbers.py opener.pdf

Reads the numbers back from the RENDERED PDF (pdftotext) and fails if any string that
tools/opener_numbers.py expects is missing. A macro can drop or garble a number silently,
so the check runs on the PDF, never on the source. Run from opener-deck/ after the build."""
import subprocess
import sys
from pathlib import Path

pdf = sys.argv[1] if len(sys.argv) > 1 else "opener.pdf"
text = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True,
                      check=True).stdout
text = " ".join(text.split())
expected = [s for s in Path("tools/expected.txt").read_text(encoding="utf-8").splitlines() if s]
missing = [s for s in expected if s not in text]
for s in expected:
    print("%-12s %s" % ("ok" if s not in missing else "MISSING", s))
if missing:
    sys.exit("%d of %d numbers missing from %s" % (len(missing), len(expected), pdf))
print("all %d numbers found in %s" % (len(expected), pdf))
