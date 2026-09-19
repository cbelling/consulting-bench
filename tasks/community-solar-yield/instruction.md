**From:** James Park, Partner — Energy
**To:** Associate case team
**Subject:** HelioCo-op 18MW — temperate yield, not desert
**Date:** Monday, 9:25 AM

Team,

18 MW community solar. Developer deck uses 1,800 kWh/kW-year (desert) and 100% offtake. Site is temperate: **1,450 kWh/kW-year** and **88% offtake**.

Build if EBITDA / capex ≥ **9%**. Capex is $21.6M.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<build|no-go>",
  "ebitda_millions": <float>,
  "ebitda_over_capex_pct": <float>,
  "method": "<MW × kWh/kW × price × offtake − O&M − lease − interconnection>"
}
```

Revenue = 18,000 kW × 1,450 × $0.11 × 88%. Subtract O&M $0.28M, lease $0.45M, interconnection $0.22M.
End with a concrete client next step—not generic risk monitoring.

James
