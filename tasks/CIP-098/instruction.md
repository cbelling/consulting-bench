**From:** Rachel Kim, Partner — Technology & Analytics
**To:** Associate case team
**Subject:** CloudSaaS — breakeven path for board prep
**Date:** Monday, 8:00 AM

Team,

CloudSaaS is burning cash. Board deck shows **$80M ARR**, **70% gross margin**, **$50M S&M**, **$30M R&D**, **$15M G&A**. FP&A flagged a duplicate corp allocation in G&A—see `/app/matter/cloudsaas_pl.txt` for the corrected run-rate and two cost-cut scenarios.

Hurdle: **operating breakeven within four quarters**. Compare (A) cut S&M 30% with growth slowing to 5% ARR over 4Q vs. (B) cut R&D 20% while holding growth at 10% ARR over 4Q.

Deliverables by **Tuesday 3 PM**:
1. `/app/output/memo.md` — recommend one path in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<sm_cut|rd_cut>",
  "q4_operating_profit_millions": <float>,
  "method": "<four-quarter breakeven P&L>"
}
```

Show a four-quarter breakeven P&L. Note the single FP&A correction in the memo body. End with a concrete board/next-step ask.

Rachel
