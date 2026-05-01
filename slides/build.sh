#!/bin/bash
# Build lecture.pdf with the ainit-academic Beamer theme.
# Run two passes for cross-references.
set -e
cd "$(dirname "$0")"

# Add the theme directory to TEXINPUTS so \usetheme{AINITAcademic} resolves.
export TEXINPUTS="../theme/ainit-academic:${TEXINPUTS:-}"

# Locate lualatex; MacTeX usually installs it at /Library/TeX/texbin/.
if command -v lualatex >/dev/null 2>&1; then
  LUA=lualatex
elif [ -x /Library/TeX/texbin/lualatex ]; then
  LUA=/Library/TeX/texbin/lualatex
else
  echo "lualatex not found on PATH or at /Library/TeX/texbin/lualatex" >&2
  exit 1
fi

"$LUA" -interaction=nonstopmode lecture.tex
"$LUA" -interaction=nonstopmode lecture.tex   # second pass for refs

echo "Built lecture.pdf"
