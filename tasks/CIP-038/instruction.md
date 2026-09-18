**From:** Maria Santos, Partner — Agriculture
**To:** Associate case team
**Subject:** Prairie Co-op — DTC beef incremental vs wholesale
**Date:** Monday, 10:05 AM

Team,

Prairie Co-op is debating a DTC beef box. Two exhibits disagree on whether the 70% retail yield applies to **live weight** or **hanging weight**. Use hanging first (62% of live), then 70% retail of hanging.

Launch DTC if incremental contribution vs wholesale ≥ **$1.5M**.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<launch|stay_wholesale>",
  "retail_lb": <float>,
  "dtc_contribution_millions": <float>,
  "wholesale_contribution_millions": <float>,
  "method": "<live × hang × retail; DTC net price vs wholesale>"
}
```

Retail lb = live × 62% × 70%. DTC net = price × (1 − 4% returns) − $1.90 fulfillment. Wholesale = retail lb × $4.10. Do not use live pounds as sellable.
End with a concrete client next step—not generic risk monitoring.

Maria
