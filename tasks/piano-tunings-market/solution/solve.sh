#!/bin/bash
set -euo pipefail
mkdir -p /app/output

cat > /app/output/memo.md << 'MEMO_EOF'
We estimate **9.3 million annual piano tunings** in the US, supporting a MusicBridge scholarship cohort of approximately 90–100 technicians per year at 1% market penetration. The estimate segments home (4.8M), institutional (4.0M), and concert/rental add-on (0.5M) tunings using stock × frequency methodology.

## Market sizing approach

| Segment | Piano stock | Tuning rate | Annual tunings |
|---------|-------------|-------------|----------------|
| Home pianos | 10.0M | 40% tune at 1.2×/yr | **4.8M** |
| Institutional | 2.0M | 2.0×/yr | **4.0M** |
| Concert/rental add-on | — | — | **0.5M** |
| **Total** | | | **9.3M** |

The segmented approach avoids the trap of applying a blended rate, which would undercount institutional frequency. The 9.3M estimate falls within the 7–12M band and reflects current tuning behavior (60% of home pianos never tuned).

## Scholarship sizing implication
At 100 average tunings per technician per year, 9.3M tunings implies ~93k active technicians nationally. A 1% cohort (90–100 scholarships annually) would be material to guild membership growth.

## Next step
Commission a validation survey with Piano Technicians Guild chapters in 5 regions to verify the 1.2 home tuning frequency and institutional 2.0× average against actual member service records.
MEMO_EOF

cat > /app/output/answer.json << 'JSON_EOF'
{
  "annual_us_piano_tunings_millions": 9.3,
  "home_tunings_millions": 4.8,
  "institutional_tunings_millions": 4.5,
  "method": "stock × frequency segmented by home vs institutional"
}
JSON_EOF
