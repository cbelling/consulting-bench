#!/usr/bin/env bash
# Full 50-task Consulting Bench run: 20 Modal sandboxes at a time,
# Harbor terminus-2 + OpenRouter DeepSeek V4.1 Flash.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
  echo "OPENROUTER_API_KEY is not set."
  exit 2
fi

if [[ -z "${MODAL_TOKEN_ID:-}" || -z "${MODAL_TOKEN_SECRET:-}" ]]; then
  if [[ ! -f "$HOME/.modal.toml" ]]; then
    echo "Modal is not authenticated."
    exit 2
  fi
fi

if ! command -v harbor >/dev/null 2>&1; then
  echo "Harbor is not on PATH. Install with: uv tool install 'harbor[modal]'"
  exit 2
fi

JOBS_DIR="${JOBS_DIR:-$ROOT/jobs}"
CONFIG="$ROOT/evals/full-bench-deepseek-v4.1-flash-concurrent.json"

harbor run \
  --config "$CONFIG" \
  -e modal \
  -o "$JOBS_DIR" \
  --job-name full-bench-deepseek-v4.1-flash-concurrent \
  -n 20 \
  -y
