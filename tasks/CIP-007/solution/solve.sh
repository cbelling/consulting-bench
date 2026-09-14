#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "estimate_millions": 25.7,
  "methodology": "260M * 0.95 * 1.3 * 8% \u2248 25.7M new checking openings."
}
ORACLE_EOF
