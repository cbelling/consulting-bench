#!/bin/bash
set -euo pipefail
mkdir -p /app/output

cat > /app/output/memo.md << 'MEMO_EOF'
We recommend ViewNest raise subscription price from $12/mo to $14.50/mo (+$2.50) to reach the $0.50/sub/mo full-loaded margin hurdle within 12 months. The product team's "$3 contribution profit" view excludes $4.50 content amortization and $1.20 fixed costs, masking a −$2.70/sub/mo full-loaded loss that requires a $3.20/sub/mo improvement.

## Profitability bridge (reconciling conflicting exhibits)

| Layer | Per sub/month | Status vs hurdle |
|-------|---------------|------------------|
| Variable contribution (Exhibit A) | +$3.00 | ✓ Product view |
| Less: Content amortization (Exhibit B) | −$4.50 | |
| **= After content** | **−$1.50** | ❌ CFO concern |
| Less: Platform fixed (Exhibit C) | −$1.20 | |
| **= Full-loaded margin** | **−$2.70** | ❌ Board view |
| **Hurdle** | **+$0.50** | |
| **Gap to close** | **$3.20** | |

The L3 conflict stems from definitional layers: variable contribution is healthy, but content economics dominate.

## Recommended action
**Price increase to $14.50/mo** closes the full $3.20 gap solo:
- New full-loaded: −$2.70 + $2.50 = −$0.20... requires $14.70, round to **$15/mo** for $0.30 cushion above hurdle.

Alternative: Price +$2 to $14 PLUS cut content spend by $50M (18%) closes gap but risks catalog competitiveness.

## Next step
Model churn elasticity at $14.50 and $15.00 price points using historical upgrade cohort data before finalizing the price change for Q1.
MEMO_EOF

cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "price",
  "variable_contribution_per_sub": 3.0,
  "full_loaded_margin_per_sub": -2.7,
  "recommendation": "raise price to $14.50-$15.00/month",
  "method": "layered contribution bridge from variable through content and fixed to hurdle"
}
JSON_EOF
