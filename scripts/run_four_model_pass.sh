#!/usr/bin/env bash
# One hardened Partner-50 pass per comparison model. Sequential jobs.
# Default n=8 to stay under OpenRouter in-flight credit caps.
# Usage:
#   bash scripts/run_four_model_pass.sh                 # all four
#   bash scripts/run_four_model_pass.sh claude-haiku-4.5
#   N_CONCURRENT=8 bash scripts/run_four_model_pass.sh gemini-3.8-flash
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
  [gpt-5.6-luna]="$ROOT/evals/hardened-v1-gpt-5.6-luna-concurrent.json"
  [claude-haiku-4.5]="$ROOT/evals/hardened-v1-claude-haiku-4.5-concurrent.json"
  [gemini-3.8-flash]="$ROOT/evals/hardened-v1-gemini-3.8-flash-concurrent.json"
  [glm-5.3]="$ROOT/evals/hardened-v1-glm-5.3-concurrent.json"
)

declare -A JOB_NAMES=(
  [gpt-5.6-luna]="hardened-v1-gpt-5.6-luna-concurrent"
  [claude-haiku-4.5]="hardened-v1-claude-haiku-4.5-concurrent"
  [gemini-3.8-flash]="hardened-v1-gemini-3.8-flash-concurrent"
  [glm-5.3]="hardened-v1-glm-5.3-concurrent"
)

N_CONCURRENT="${N_CONCURRENT:-8}"

MODELS=("gpt-5.6-luna" "claude-haiku-4.5" "gemini-3.8-flash" "glm-5.3")
if [[ $# -gt 0 ]]; then
  MODELS=("$@")
fi

for key in "${MODELS[@]}"; do
  config="${CONFIGS[$key]:-}"
  job="${JOB_NAMES[$key]:-}"
  if [[ -z "$config" || -z "$job" ]]; then
    echo "Unknown model key: $key"
    echo "Expected one of: gpt-5.6-luna claude-haiku-4.5 gemini-3.8-flash glm-5.3"
    exit 2
  fi

  echo "=== $job (n=${N_CONCURRENT}) ==="
  harbor run \
    --config "$config" \
    -e modal \
    -o "$JOBS_DIR" \
    --job-name "$job" \
    -n "$N_CONCURRENT" \
    -y

  python3 "$ROOT/scripts/summarize_harbor_job.py" "$JOBS_DIR/$job"
  python3 "$ROOT/scripts/build_leaderboard.py"
done
