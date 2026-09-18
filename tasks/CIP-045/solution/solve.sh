#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "irr_pct": 7.5,
  "max_price_millions": 75.0,
  "offer_price_millions": 120,
  "decision": "no-go",
  "rationale": "7.5% IRR at $120M is below 12% hurdle; max price $75M\u2014no-go at ask."
}
ORACLE_EOF
