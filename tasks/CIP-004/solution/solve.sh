#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "estimate_millions": 8.6,
  "methodology": "200M * 0.9 * 0.4 * 0.12 = 8.64M paying subscribers."
}
ORACLE_EOF
