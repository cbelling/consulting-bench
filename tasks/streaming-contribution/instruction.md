**From:** Rachel Kim, Partner — Media & Entertainment
**To:** Associate case team
**Subject:** ViewNest profitability definition reconciliation
**Date:** Wednesday, 11:30 AM

Team,

ViewNest's board pack shows the streaming business as losing money, but the product team insists they're profitable on contribution. CFO wants us to reconcile the definitions and recommend either a price increase or content spending cut to hit the full-loaded $0.50/sub/month margin hurdle within 12 months.

Matter pack in `/app/matter/` has three exhibits (A, B, C) with conflicting profit views. This is L3—you must reconcile all three layers and bridge to the hurdle.

Deliverables by **Friday 3 PM**:
1. `/app/output/memo.md` — one-page memo with recommendation (price or content cut, quantified) in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<price|content|both>",
  "variable_contribution_per_sub": <float>,
  "full_loaded_margin_per_sub": <float>,
  "recommendation": "<specific action>",
  "method": "<contribution bridge to hurdle>"
}
```

Use a layered contribution bridge. Show math from variable contrib → after content → after platform fixed. End with specific pricing or content cut magnitude—not vague optimization.

Rachel
