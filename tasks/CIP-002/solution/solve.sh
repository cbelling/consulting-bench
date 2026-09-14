#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "estimate_millions_usd": 189.0,
  "households_millions": 3.5,
  "methodology": "3.5M households * 90% * 40 units * $1.50 = $189M; size from HH base, not population."
}
ORACLE_EOF
