**From:** Emily Chen, Partner — Industrial
**To:** Associate case team
**Subject:** AeroTread — passenger narrowbody tire TAM before Thursday bid/no-bid
**Date:** Monday, 10:15 AM

Team,

AeroTread wants a go/no-go on bidding the US passenger **narrowbody** mainline tire contract. Size **annual replacement unit demand** and TAM at the contract ASP.

Facts are split across fleet, utilization, and a cargo/spares note in `/app/matter/`. The bid committee will only count passenger narrowbody replacements — not cargo, not spare-pool stocking.

Hurdle: bid if TAM ≥ **$20M**.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<go|no-go>",
  "annual_replacements": <float>,
  "tam_millions": <float>,
  "method": "<fleet × tires × cycles / life>"
}
```

Show the stock × frequency build (fleet × tires per ship × cycles / landing life). State which exhibits you excluded and why.
End with a concrete client next step—not generic risk monitoring.

Emily
