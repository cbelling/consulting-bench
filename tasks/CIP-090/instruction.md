**From:** Marcus Williams, Partner — Travel & Transportation
**To:** Associate case team
**Subject:** NorthAir — match the −8% fare on overlap ASMs only
**Date:** Monday, 4:55 PM

Team,

A competitor cut fares 8% on overlap flying. Compare **revenue change if we match** vs **if we do not**. Match only if matching saves ≥ **$100M** versus not matching.

Apply the cut only to the 8.5B overlap ASMs, not the 70B system.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<match|no_match>",
  "match_revenue_delta_millions": <float>,
  "no_match_revenue_delta_millions": <float>,
  "savings_vs_walk_millions": <float>,
  "method": "<overlap ASMs × RASM; match volume vs walk spill>"
}
```

Base overlap revenue = 8.5B × $0.12. Match: ×1.03 volume ×0.92 yield. No-match: keep yield, lose 18% passengers.
End with a concrete client next step—not generic risk monitoring.

Marcus
