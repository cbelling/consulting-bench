**From:** James Whitfield, Partner — Transportation & Logistics
**To:** Associate case team
**Subject:** SwiftRoute — Zone C looks green but is it?
**Date:** Monday, 10:30 AM

Team,

SwiftRoute's dispatch dashboard shows Zone C at **$5.20 average revenue per stop**—above the $4.50 network average. But field ops notes **35% failed-first-attempt rate** with **$4.00 redelivery cost per failed stop**, and route density is only **18 stops/hour** vs **28 stops/hour** in Zone A. Driver fully-loaded cost is **$36/hour**.

Hurdle: **≥$1.50 contribution per stop after redelivery costs**. Size true Zone C economics using `/app/matter/` and recommend whether to exit.

Deliverables by **Tuesday noon**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<exit_zone_c|retain_zone_c>",
  "true_contribution_per_stop_usd": <float>,
  "method": "<contribution per stop after redelivery>"
}
```

Show the density and redelivery math explicitly. End with a concrete next step.

James
