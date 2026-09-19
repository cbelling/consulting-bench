**From:** Marcus Chen, Partner — Consumer & Retail
**To:** Associate case team
**Subject:** GreenBasket — vendor 80bps vs shrink on the $80M subset
**Date:** Wednesday, 9:15 AM

Team,

A produce vendor offers +80 bps category GM on $420M fresh sales if we take a SKU reset. The reset adds **2.0pp shrink on an $80M SKU subset** (full retail, we already bought the goods).

Accept only if net ≥ **$2.5M**. Do not apply shrink to the whole $420M.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<accept|reject>",
  "gm_uplift_millions": <float>,
  "shrink_hit_millions": <float>,
  "net_millions": <float>,
  "method": "<category sales × bps − subset sales × extra shrink>"
}
```

GM uplift = $420M × 0.80%. Shrink hit = $80M × 2.0% (full retail). Net = uplift − shrink.
End with a concrete client next step—not generic risk monitoring.

Marcus
