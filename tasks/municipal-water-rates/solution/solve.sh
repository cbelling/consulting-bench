#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend delay. Incremental revenue is $3.91M and treatment save is $0.19M, totaling $4.10M — short of the $4.5M plant need. Finance's $4.79M ignores elasticity.

## Build
- %ΔP: (5.10 − 4.20) / 4.20 = 21.429%
- New kgal: 5.4 × (1 − 0.15 × 0.21429) = **5.2264**
- New revenue: 82k × 12 × 5.2264 × 5.10 = **$26.228M**
- Current: 82k × 12 × 5.4 × 4.20 = **$22.317M**
- Incremental revenue **$3.911M**; treatment save 82k × 12 × 0.1736 × 1.10 = **$0.188M**
- Total **$4.099M** < $4.5M

## Next step
Delay the plant vote and bring a $5.25/kgal or phased-construction option to next month's council.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "delay",
  "incremental_revenue_millions": 3.911,
  "treatment_save_millions": 0.188,
  "total_vs_plant_millions": 4.099,
  "method": "accounts \u00d7 months \u00d7 kgal \u00d7 rate with elasticity \u22120.15"
}
JSON_EOF
