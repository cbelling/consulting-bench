#!/usr/bin/env bash
# One hardened Partner-50 pass per flagship model. Sequential jobs, 20 Modal sandboxes each.
# Usage:
#   bash scripts/run_four_model_pass.sh              # all four
#   bash scripts/run_four_model_pass.sh gpt-5.4      # one model
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

declare -A CONFIGS=(
  [gpt-5.4]="$ROOT/evals/hardened-v1-gpt-5.4-concurrent.json"
  [claude-sonnet-5]="$ROOT/evals/hardened-v1-claude-sonnet-5-concurrent.json"
  [gemini-3.1-pro]="$ROOT/evals/hardened-v1-gemini-3.1-pro-concurrent.json"
  [grok-4.6]="$ROOT/evals/hardened-v1-grok-4.6-concurrent.json"
)

declare -A JOB_NAMES=(
  [gpt-5.4]="hardened-v1-gpt-5.4-concurrent"
  [claude-sonnet-5]="hardened-v1-claude-sonnet-5-concurrent"
  [gemini-3.1-pro]="hardened-v1-gemini-3.1-pro-concurrent"
  [grok-4.6]="hardened-v1-grok-4.6-concurrent"
)

MODELS=("gpt-5.4" "claude-sonnet-5" "gemini-3.1-pro" "grok-4.6")
if [[ $# -gt 0 ]]; then
  MODELS=("$@")
fi

for key in "${MODELS[@]}"; do
  config="${CONFIGS[$key]:-}"
  job="${JOB_NAMES[$key]:-}"
  if [[ -z "$config" || -z "$job" ]]; then
    echo "Unknown model key: $key"
    echo "Expected one of: gpt-5.4 claude-sonnet-5 gemini-3.1-pro grok-4.6"
    exit 2
  fi

  echo "=== $job ==="
  harbor run \
    --config "$config" \
    -e modal \
    -o "$JOBS_DIR" \
    --job-name "$job" \
    -n 20 \
    -y

  python3 "$ROOT/scripts/summarize_harbor_job.py" "$JOBS_DIR/$job"
  python3 "$ROOT/scripts/build_leaderboard.py"
done
