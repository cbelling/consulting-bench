#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "cm_dollars_y1_millions": 112.0,
  "cm_dollars_y2_millions": 97.0,
  "cm_pct_y1": 28.0,
  "cm_pct_y2": 22.0,
  "headline": "CM$ fell from $112M to $97M; CM% compressed from 28% to 22% despite revenue growth."
}
ORACLE_EOF
