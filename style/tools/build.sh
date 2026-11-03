#!/bin/bash
# Copied on 2026-11-03 from eth-ainit-hs26/w1-lecture-material, commit 9792819, file style/tools/build.sh.
# build.sh deck.tex
# Compiles a deck with lualatex three times FROM the deck's own directory, so that \input of
# ../style/ainit-preamble resolves and the leaf, the pricking dots and the balloons (placed with
# remember picture) settle. Prints the page count, the number of log errors, and any missing
# glyph or overfull box wider than 2 pt.
set -u
deck="${1:-}"
[ -n "$deck" ] || { echo "usage: build.sh deck.tex"; exit 2; }
dir=$(cd "$(dirname "$deck")" && pwd)
base=$(basename "$deck" .tex)
cd "$dir" || exit 2
for pass in 1 2 3; do
  if ! lualatex -interaction=nonstopmode -halt-on-error "$base.tex" >/dev/null 2>&1; then
    echo "pass $pass FAILED. First errors in $base.log:"
    grep -n '^!' "$base.log" | head -5
    exit 1
  fi
done
echo "$base: $(pdfinfo "$base.pdf" | awk '/^Pages:/{print $2}') pages"
echo "log errors: $(grep -c '^!' "$base.log")"
grep -E 'Missing character|Overfull \\hbox \(([2-9]|[0-9]{2,})\.' "$base.log" | head -5
exit 0
