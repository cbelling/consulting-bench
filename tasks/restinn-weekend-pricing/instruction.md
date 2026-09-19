**From:** Elena Vasquez, Partner — Hospitality & Leisure
**To:** Associate case team
**Subject:** RestInn — weekend dynamic pricing before Monday walk-in
**Date:** Thursday, 4:00 PM

Team,

RestInn (100 rooms) wants a weekend-night pricing recommendation before Monday's owner walk-in. Revenue management sent occupancy/ADR scenarios in `/app/matter/restinn_weekend.csv`.

Please read the facts, size contribution margin per occupied room (ADR minus variable cost of $25/occupied night), and compare base vs. +10% vs. +20% weekend ADR premiums with the occupancy curves provided.

Deliverables due by **Friday 5 PM**:
1. A **one-page memo** at `/app/output/memo.md` suitable for a walk-in readout (recommendation in the opening paragraph).
2. Sidecar JSON at `/app/output/answer.json`:

```json
{
  "decision": "<base|premium_10|premium_20>",
  "optimal_premium_pct": <int>,
  "weekend_contribution_profit_dollars": <float>,
  "method": "<contribution margin tree>"
}
```

Use a clear contribution-margin decision tree in the memo. End with a concrete next step for the client—not generic risk monitoring.

Thanks,
Elena
