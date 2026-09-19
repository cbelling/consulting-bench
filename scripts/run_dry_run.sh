#!/usr/bin/env bash
# Dry-run the Partner-50 bench on Modal sandboxes with the cheapest planned
# model: DeepSeek V4.1 Flash via OpenRouter ($0.15 / $0.60 per 1M tokens).
#
# Slice: restinn-weekend-pricing (L1), cloudsaas-path-to-profit (L1),
# hospital-outpatient-gap (L3).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
  echo "OPENROUTER_API_KEY is not set."
  echo "Export an OpenRouter key, then re-run:"
  echo "  export OPENROUTER_API_KEY=..."
  echo "  bash scripts/run_dry_run.sh"
  exit 2
fi

if [[ -z "${MODAL_TOKEN_ID:-}" || -z "${MODAL_TOKEN_SECRET:-}" ]]; then
  if [[ ! -f "$HOME/.modal.toml" ]]; then
    echo "Modal is not authenticated."
    echo "Set MODAL_TOKEN_ID and MODAL_TOKEN_SECRET, or run: modal token new"
    exit 2
  fi
fi

if ! command -v harbor >/dev/null 2>&1; then
  echo "Harbor is not on PATH. Install with: uv tool install 'harbor[modal]'"
  exit 2
fi

JOBS_DIR="${JOBS_DIR:-$ROOT/jobs}"
CONFIG="$ROOT/evals/dry-run-deepseek-v4.1-flash.json"

harbor run \
  --config "$CONFIG" \
  -e modal \
  -o "$JOBS_DIR" \
  --job-name dry-run-deepseek-v4.1-flash \
  -n 3 \
  -y
