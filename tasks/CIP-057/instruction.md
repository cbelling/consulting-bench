**From:** Thomas Wright, Partner — Technology & Telecom
**To:** Associate case team
**Subject:** Relay Mobile — unlimited plan net vs $2M hurdle
**Date:** Monday, 3:30 PM

Team,

Relay wants an unlimited SKU at $75. Heavy users who switch currently spend more than $75. Build **year-1 net contribution** after cannibalization, new joiners, and network opex.

Launch only if net ≥ **$2.0M**. Marketing's $75 × switchers is not incremental.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<launch|no-go>",
  "year1_net_millions": <float>,
  "cannibal_millions": <float>,
  "method": "<new joiners − ARPU step-down − network opex>"
}
```

Cannibal = switcher count × (current heavy ARPU − $75). Add new-joiner revenue. Subtract network opex. Do not count switcher $75 as new revenue.
End with a concrete client next step—not generic risk monitoring.

Thomas
