**From:** Marcus Williams, Partner — Consumer & Recreation
**To:** Associate case team
**Subject:** DimpleForge golf ball replacement demand forecast
**Date:** Tuesday, 2:15 PM

Team,

DimpleForge is forecasting annual US golf ball replacement demand driven by balls lost (not recovered for replay). The commercial team wants to size the total addressable market for new ball sales, excluding balls that remain in play.

The matter pack is in `/app/matter/`. I'm seeing conflicting survey data on course loss rates (1.2 vs 0.6 balls per round), and we need to reconcile that with the range ball consumption numbers. This is L3 complexity—handle the conflict explicitly.

Deliverables by **Thursday 4 PM**:
1. `/app/output/memo.md` — one-page memo with your recommendation in paragraph one on annual US golf balls lost.
2. `/app/output/answer.json`:

```json
{
  "golf_balls_lost_annually_millions": <float>,
  "course_loss_millions": <float>,
  "range_consumption_millions": <float>,
  "method": "<course rounds × loss rate + range consumption>"
}
```

Report both loss-rate scenarios or a reconciled midpoint with reasoning. Target band 800M–1.1B balls. End with a concrete validation step—not generic risk monitoring.

Marcus
