#!/usr/bin/env bash
# Run hardened Partner-50 Pass@4 (n_attempts=4) for all five models.
# Sequential jobs. Default n_concurrent_trials: 20 for DeepSeek, 8 for others.
# Usage:
#   bash scripts/run_pass4.sh                           # all five
#   bash scripts/run_pass4.sh deepseek-v4.1-flash       # one model
#   N_CONCURRENT=16 bash scripts/run_pass4.sh glm-5.3   # override concurrency
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
  [deepseek-v4.1-flash]="$ROOT/evals/hardened-v1-deepseek-v4.1-flash-pass4.json"
  [gpt-5.6-luna]="$ROOT/evals/hardened-v1-gpt-5.6-luna-pass4.json"
  [claude-haiku-4.5]="$ROOT/evals/hardened-v1-claude-haiku-4.5-pass4.json"
  [gemini-3.8-flash]="$ROOT/evals/hardened-v1-gemini-3.8-flash-pass4.json"
  [glm-5.3]="$ROOT/evals/hardened-v1-glm-5.3-pass4.json"
)

declare -A JOB_NAMES=(
  [deepseek-v4.1-flash]="hardened-v1-deepseek-v4.1-flash-pass4"
  [gpt-5.6-luna]="hardened-v1-gpt-5.6-luna-pass4"
  [claude-haiku-4.5]="hardened-v1-claude-haiku-4.5-pass4"
  [gemini-3.8-flash]="hardened-v1-gemini-3.8-flash-pass4"
  [glm-5.3]="hardened-v1-glm-5.3-pass4"
)

declare -A DEFAULT_CONCURRENCY=(
  [deepseek-v4.1-flash]=20
  [gpt-5.6-luna]=8
  [claude-haiku-4.5]=8
  [gemini-3.8-flash]=8
  [glm-5.3]=8
)

MODELS=("deepseek-v4.1-flash" "gpt-5.6-luna" "claude-haiku-4.5" "gemini-3.8-flash" "glm-5.3")
if [[ $# -gt 0 ]]; then
  MODELS=("$@")
fi

for key in "${MODELS[@]}"; do
  config="${CONFIGS[$key]:-}"
  job="${JOB_NAMES[$key]:-}"
  if [[ -z "$config" || -z "$job" ]]; then
    echo "Unknown model key: $key"
    echo "Expected one of: deepseek-v4.1-flash gpt-5.6-luna claude-haiku-4.5 gemini-3.8-flash glm-5.3"
    exit 2
  fi

  N_CONCURRENT="${N_CONCURRENT:-${DEFAULT_CONCURRENCY[$key]}}"

  echo "=== $job (n_attempts=4, n_concurrent=$N_CONCURRENT) ==="
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
