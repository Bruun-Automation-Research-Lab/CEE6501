#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || -z "${1:-}" ]]; then
  echo "ERROR: No notebook path provided."
  exit 1
fi

NB_PATH="$1"
NB_DIR="$(cd "$(dirname "$NB_PATH")" && pwd)"
NB_NAME="$(basename "$NB_PATH")"
NB_STEM="${NB_NAME%.*}"
HTML_PATH="${NB_DIR}/${NB_STEM}.slides.html"

echo "Notebook path: \"$NB_PATH\""
echo "HTML path    : \"$HTML_PATH\""
echo

if [[ ! -f "$HTML_PATH" ]]; then
  echo "ERROR: Slides HTML not found: \"$HTML_PATH\""
  echo "Run the slide conversion first."
  exit 1
fi

# Run your existing converter script (same one you use on Windows)
# If HTML_to_PDF.py lives in the repo root:
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="${SCRIPT_DIR}/HTML_to_PDF.py"

if [[ ! -f "$PY_SCRIPT" ]]; then
  echo "ERROR: Could not find HTML_to_PDF.py at: \"$PY_SCRIPT\""
  exit 1
fi

conda run -n CEE6501-dev python "$PY_SCRIPT" "$HTML_PATH"

