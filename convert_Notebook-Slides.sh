#!/usr/bin/env bash
set -euo pipefail

# Check argument
if [[ $# -lt 1 || -z "${1:-}" ]]; then
  echo "ERROR: No notebook path provided."
  exit 1
fi

NB_PATH="$1"
NB_DIR="$(cd "$(dirname "$NB_PATH")" && pwd)"
NB_NAME="$(basename "$NB_PATH")"
NB_STEM="${NB_NAME%.*}"

echo "Notebook path: \"$NB_PATH\""
echo "Notebook dir : \"$NB_DIR\""
echo "Notebook name: \"$NB_STEM\""
echo

cd "$NB_DIR"

# Convert to Reveal.js slides, with tag-based removal:
# - hide-input: removes inputs on tagged cells
# - remove-cell: removes entire tagged cells
conda run -n CEE6501-dev python -m jupyter nbconvert "${NB_STEM}.ipynb" \
  --to slides \
  --TagRemovePreprocessor.enabled=True \
  --TagRemovePreprocessor.remove_input_tags="hide-input" \
  --TagRemovePreprocessor.remove_cell_tags="remove-cell"
