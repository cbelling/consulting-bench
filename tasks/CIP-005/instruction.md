**From:** Sarah Martinez, Partner — Hospitality
**To:** Associate case team
**Subject:** LodgeCo — economy-segment room revenue before product-TAM review
**Date:** Monday, 9:40 AM

Team,

LodgeCo is sizing whether a $400M RevPAR tool is worth building. We need **US economy-segment annual room revenue** only.

Use current census + occupancy/ADR in `/app/matter/`. A stale STR extract and a midscale rollup are in the pack as distractors.

Proceed if economy room revenue ≥ **$10B**.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<proceed|hold>",
  "economy_room_nights_millions": <float>,
  "economy_room_revenue_billions": <float>,
  "method": "<properties × rooms × occ × ADR>"
}
```

Build properties × rooms × 365 × occupancy × ADR. Do not mix midscale or the outdated STR snapshot.
End with a concrete client next step—not generic risk monitoring.

Sarah
