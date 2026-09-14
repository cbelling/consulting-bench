#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "estimate_millions": 40.0,
  "methodology": "Adults: 260M * 0.35 / 2.5 = 36.4M; Kids: 70M * 0.15 / 3 = 3.5M; Total \u2248 40M units."
}
ORACLE_EOF
