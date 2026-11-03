#!/bin/bash
# Copied on 2026-11-03 from eth-ainit-hs26/w1-lecture-material, commit 9792819, file style/tools/check.sh.
# check.sh deck.pdf
# The house text checks, run on the RENDERED PDF (source greps miss text that a macro assembles).
# Exits 1 if the PDF holds an em dash, an en dash, or a line of build metadata.
#   dashes     must both be 0
#   caps       the list of ALL CAPS words, to read: only acronyms and the body's own tokens
#              (START, END, LLM, OPRO, MLOps, MDPs, SARSA, REINFORCE, AI, ETH) belong there
#   metadata   must print nothing: nothing addressed to the deck's builder may reach a slide
#   fonts      the embedded families, to confirm EB Garamond, Garamond Math and Kefa III
pdf="${1:-}"
[ -f "$pdf" ] || { echo "usage: check.sh deck.pdf"; exit 2; }
txt=$(mktemp)
pdftotext "$pdf" "$txt"
em=$(grep -c $'\xe2\x80\x94' "$txt")   # U+2014 as UTF-8 bytes: macOS grep has no -P
en=$(grep -c $'\xe2\x80\x93' "$txt")   # U+2013
meta=$(grep -niE 'SOURCES\.md|README\.md|IMAGE-SOURCES|CLAUDE\.md|not pinned|\bTBD\b|placeholder|FIXME|mockup|candidate|\.tex\b' "$txt")
echo "em dashes: $em"
echo "en dashes: $en"
echo "caps words:"
grep -oE '\b[A-Z]{3,}\b' "$txt" | sort | uniq -c | sort -rn | awk '{printf "  %s (%s)\n", $2, $1}'
echo "build metadata:"
[ -n "$meta" ] && echo "$meta" || echo "  none"
echo "fonts:"
pdffonts "$pdf" | awk 'NR>2{print $1}' | sed 's/^[A-Z]*+//; s/:.*//' | sort -u | sed 's/^/  /'
rm -f "$txt"
[ "$em" = 0 ] && [ "$en" = 0 ] && [ -z "$meta" ]
