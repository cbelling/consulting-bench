#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "max_price_usd": 2.79,
  "min_share_pct": 35,
  "contribution_per_bar_usd": 1.71,
  "rationale": "$2.79 is the highest price maintaining \u226535% share (36%) with max contribution $1.71/bar."
}
ORACLE_EOF
