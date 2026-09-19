**From:** Emily Chen, Partner — Education & Nonprofit
**To:** Associate case team
**Subject:** Harbor House — cut Program B only if surplus ≥ $0.5M
**Date:** Tuesday, 2:20 PM

Team,

Harbor House is $2.4M in deficit. Program B loses money. If we cut B we save its expenses but lose only the **unrestricted** B revenue. Restricted B gifts leave with the program.

Cut B if the resulting surplus ≥ **$0.5M**. Do not treat restricted gifts as remaining fuel for overhead.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<cut_b|keep_b>",
  "surplus_if_cut_millions": <float>,
  "unrestricted_revenue_lost_millions": <float>,
  "method": "<current deficit + expense save − unrestricted revenue lost>"
}
```

Improvement = B expenses − unrestricted B revenue. New surplus = −2.4 + improvement. Restricted $2.4M of B revenue goes away with B and was not funding the deficit.
End with a concrete client next step—not generic risk monitoring.

Emily
