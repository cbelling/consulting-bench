**From:** Marcus Williams, Partner — Travel & Transportation
**To:** Associate case team
**Subject:** NorthAir — status-match: true-new ancillary vs $4M hurdle
**Date:** Monday, 8:20 AM

Team,

Loyalty wants a status-match campaign. Marketing quotes 0.9M "new" members. 40% are already on the file. Year-1 new members fly fewer trips than the base.

Approve only if incremental ancillary − campaign cost ≥ **$4.0M**.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<approve|reject>",
  "true_new_members_millions": <float>,
  "net_ancillary_millions": <float>,
  "method": "<true-new × y1 trips × miles × ancillary − cost>"
}
```

True new = campaign members × (1 − already-member share). Use year-1 trip rate, not the base 1.4.
End with a concrete client next step—not generic risk monitoring.

Marcus
