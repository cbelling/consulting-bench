# Consulting Bench tasks

50 Harbor partner-memo tasks. Each folder is a Terminal-Bench-style task:
`task.toml`, `instruction.md`, `environment/`, `tests/`, and `solution/`.

Run the full set:

```shell
harbor run -c configs/oracle.yaml
```

Run one task:

```shell
harbor run -p tasks/CIP-054 -a oracle
```

| ID | Level | Category | Description |
|----|-------|----------|-------------|
| [CIP-003](CIP-003) | L2 | market-sizing | AeroTread narrowbody tire replacement TAM — exclude cargo/spares |
| [CIP-005](CIP-005) | L2 | market-sizing | US economy-hotel room revenue TAM — exclude midscale and stale STR |
| [CIP-006](CIP-006) | L2 | market-sizing | India smartphone sell-out TAM — exclude feature phones and gray sell-in |
| [CIP-010](CIP-010) | L3 | market-sizing | Piano tunings market sizing — unusual stock × frequency |
| [CIP-012](CIP-012) | L3 | market-sizing | Golf balls lost — unusual market sizing with conflicting exhibits |
| [CIP-015](CIP-015) | L3 | profitability | Hospital outpatient surgery profit gap — cash EBITDA hurdle |
| [CIP-016](CIP-016) | L2 | profitability | SaaS gross-margin compression — isolate recurring hosting drag |
| [CIP-018](CIP-018) | L2 | profitability | Hotel F&B mix — banquet vs outlet contribution after shared kitchen |
| [CIP-019](CIP-019) | L2 | operations | Pharma plant: run extra shift only if true OEE contribution clears hurdle |
| [CIP-021](CIP-021) | L3 | profitability | Logistics last-mile Zone C true contribution after redelivery |
| [CIP-025](CIP-025) | L3 | profitability | Media streaming profitability — contribution layers conflict |
| [CIP-028](CIP-028) | L3 | investment-decision | Hospital urgent-care adjacency — cannibalization threshold |
| [CIP-030](CIP-030) | L2 | investment-decision | Airline new route — contribution after airport incentives expire |
| [CIP-032](CIP-032) | L3 | market-entry | Chemical battery materials entry — conflicting margin exhibits |
| [CIP-033](CIP-033) | L2 | adjacency | Pet-insurance adjacency — combined ratio after adverse selection |
| [CIP-034](CIP-034) | L2 | strategy | 3P marketplace take-rate vs 1P margin after returns and ads |
| [CIP-038](CIP-038) | L3 | go-to-market | Ag co-op DTC beef — hanging yield then retail yield, not live weight |
| [CIP-040](CIP-040) | L2 | m-and-a | Organic CPG brand acquisition — syn-adjusted ROIC vs 13% hurdle |
| [CIP-041](CIP-041) | L2 | m-and-a | Hospital ASC acquisition — cash EBITDA after physician leakage |
| [CIP-043](CIP-043) | L2 | make-vs-buy | SaaS acqui-hire vs build — 24-month cash including dead-time |
| [CIP-044](CIP-044) | L3 | investment-decision | Retail distressed-store acquisition four-wall analysis |
| [CIP-050](CIP-050) | L3 | investment-decision | Pharma rare-disease biotech valuation — bull vs bear EV |
| [CIP-052](CIP-052) | L3 | pricing | Airline bag-fee increase — elasticity and spill scenarios |
| [CIP-053](CIP-053) | L2 | pricing | SaaS seat-to-usage price move — net ARR after elasticity and grandfathering |
| [CIP-054](CIP-054) | L1 | pricing | RestInn hotel weekend dynamic pricing optimization |
| [CIP-055](CIP-055) | L3 | pricing | Pharma co-pay assistance path comparison |
| [CIP-057](CIP-057) | L2 | pricing | Telecom unlimited — net after heavy-user cannibal and network opex |
| [CIP-059](CIP-059) | L2 | pricing | Logistics dim-weight — incremental billable pounds minus churn |
| [CIP-062](CIP-062) | L3 | pricing | Municipal water rate — elasticity plus treatment save vs $4.5M plant |
| [CIP-063](CIP-063) | L1 | market-sizing | Crunchora CPG distribution white-space growth options |
| [CIP-064](CIP-064) | L2 | growth | Airline loyalty status-match — true new members only |
| [CIP-066](CIP-066) | L3 | profitability | SaaS NDR — CS vs Finance churn/expansion conflict |
| [CIP-067](CIP-067) | L2 | growth | Grocery fresh vendor deal — GM bps vs extra shrink on SKU subset |
| [CIP-070](CIP-070) | L3 | growth | Streaming ad-lite tier — price mix plus ads minus ad-lite churn |
| [CIP-075](CIP-075) | L1 | investment-decision | Compostable snack bag launch/no-go decision |
| [CIP-076](CIP-076) | L2 | product | Auto connected-feature subscription after cellular COGS and trim churn |
| [CIP-077](CIP-077) | L2 | product | Bank BNPL — take-rate minus losses, opex, and revolving NII cannibal |
| [CIP-079](CIP-079) | L3 | investment-decision | Pharma diagnostic kit — field false-positive cost, not analytical |
| [CIP-084](CIP-084) | L2 | corporate-strategy | Industrial IoT spin — strip captive transfer revenue |
| [CIP-085](CIP-085) | L2 | new-business | Retail media network — joiners only, minus guarantees and serving |
| [CIP-087](CIP-087) | L3 | investment-decision | Community solar — temperate yield and 88% offtake vs 9% hurdle |
| [CIP-089](CIP-089) | L1 | pricing | Hero brand private-label attack response options |
| [CIP-090](CIP-090) | L2 | competitive-response | Airline fare-match on overlap ASMs only — vs walk-away spill |
| [CIP-091](CIP-091) | L2 | competitive-response | SaaS freemium match — downgrade leak vs competitor churn |
| [CIP-093](CIP-093) | L3 | pricing | Retail e-comm price transparency — selective match strategy |
| [CIP-096](CIP-096) | L3 | turnaround | Airline cost turnaround — strip hedge loss, add labor contract |
| [CIP-097](CIP-097) | L2 | turnaround | Retail store closures — four-wall save minus stranded leases and halo |
| [CIP-098](CIP-098) | L1 | profitability | CloudSaaS path to profitability — S&M vs R&D cut |
| [CIP-099](CIP-099) | L3 | profitability | Hospital service-line turnaround — allocation trap |
| [CIP-100](CIP-100) | L2 | turnaround | Nonprofit — cut Program B using unrestricted only |

The Harbor dataset name is `consulting-bench/consulting-bench` (see
[`dataset.toml`](../dataset.toml)). Individual task slugs remain
`management-consulting-bench/cip-XXX`.
