#!/bin/bash
set -euo pipefail
mkdir -p /app/output

cat > /app/output/memo.md << 'MEMO_EOF'
We estimate **900 million US golf balls lost/consumed annually**, supporting DimpleForge's replacement demand forecast. The estimate reconciles conflicting course loss-rate surveys (1.2 vs 0.6 balls/round) by using midpoint scenarios and adding range ball consumption.

## Replacement demand sizing

**Survey conflict on course loss rate (L3):**
- Survey A (recall method): 1.2 balls/round → 480M course loss
- Survey B (diary method): 0.6 balls/round → 240M course loss
- **Reconciled midpoint**: ~360M course loss (split the difference given methodological uncertainty)

**Complete replacement demand:**

| Component | Method | Annual balls (M) |
|-----------|--------|------------------|
| Course loss (mid) | 400M rounds × 0.9 avg | **360** |
| Range consumption | 800M purchased × 70% | **560** |
| **Total replacement** | | **920M** |

The 920M estimate falls within the 800M–1.1B band. Both survey scenarios (1.04B and 800M bookends) support a TAM in the high hundreds of millions.

## Survey reconciliation
The recall vs diary method difference (2×) is material. Diary methods typically produce lower estimates. We use 0.9 balls/round as a pragmatic midpoint for planning purposes.

## Next step
Commission a 90-day field validation study at 10 representative courses tracking actual ball inventory loss per round (pro shop records) to ground-truth the 0.6–1.2 survey range before finalizing multi-year production capacity.
MEMO_EOF

cat > /app/output/answer.json << 'JSON_EOF'
{
  "golf_balls_lost_annually_millions": 920,
  "course_loss_millions": 360,
  "range_consumption_millions": 560,
  "method": "course rounds × midpoint loss rate + range consumption with survey conflict reconciliation"
}
JSON_EOF
