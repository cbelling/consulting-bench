# Consulting Bench tasks

50 Harbor partner-memo tasks. Each folder is a Terminal-Bench-style task:
`task.toml`, `instruction.md`, `environment/`, `tests/`, and `solution/`.

Run the full set:

```shell
harbor run -c configs/oracle.yaml
```

Run one task:

```shell
harbor run -p tasks/restinn-weekend-pricing -a oracle
```

| Slug | Level | Category | Description |
|------|-------|----------|-------------|
| [aerotread-tire-tam](aerotread-tire-tam) | L2 | market-sizing | AeroTread narrowbody tire replacement TAM — exclude cargo/spares |
| [economy-hotel-revenue](economy-hotel-revenue) | L2 | market-sizing | US economy-hotel room revenue TAM — exclude midscale and stale STR |
| [india-smartphone-sellout](india-smartphone-sellout) | L2 | market-sizing | India smartphone sell-out TAM — exclude feature phones and gray sell-in |
| [piano-tunings-market](piano-tunings-market) | L3 | market-sizing | Piano tunings market sizing — unusual stock × frequency |
| [golf-balls-lost](golf-balls-lost) | L3 | market-sizing | Golf balls lost — unusual market sizing with conflicting exhibits |
| [hospital-outpatient-gap](hospital-outpatient-gap) | L3 | profitability | Hospital outpatient surgery profit gap — cash EBITDA hurdle |
| [saas-margin-compression](saas-margin-compression) | L2 | profitability | SaaS gross-margin compression — isolate recurring hosting drag |
| [hotel-fb-mix](hotel-fb-mix) | L2 | profitability | Hotel F&B mix — banquet vs outlet contribution after shared kitchen |
| [pharma-plant-oee](pharma-plant-oee) | L2 | operations | Pharma plant: run extra shift only if true OEE contribution clears hurdle |
| [last-mile-zone-c](last-mile-zone-c) | L3 | profitability | Logistics last-mile Zone C true contribution after redelivery |
| [streaming-contribution](streaming-contribution) | L3 | profitability | Media streaming profitability — contribution layers conflict |
| [urgent-care-adjacency](urgent-care-adjacency) | L3 | investment-decision | Hospital urgent-care adjacency — cannibalization threshold |
| [airline-new-route](airline-new-route) | L2 | investment-decision | Airline new route — contribution after airport incentives expire |
| [battery-materials-entry](battery-materials-entry) | L3 | market-entry | Chemical battery materials entry — conflicting margin exhibits |
| [pet-insurance-adjacency](pet-insurance-adjacency) | L2 | adjacency | Pet-insurance adjacency — combined ratio after adverse selection |
| [marketplace-take-rate](marketplace-take-rate) | L2 | strategy | 3P marketplace take-rate vs 1P margin after returns and ads |
| [coop-dtc-beef](coop-dtc-beef) | L3 | go-to-market | Ag co-op DTC beef — hanging yield then retail yield, not live weight |
| [organic-cpg-acquisition](organic-cpg-acquisition) | L2 | m-and-a | Organic CPG brand acquisition — syn-adjusted ROIC vs 13% hurdle |
| [hospital-asc-acquisition](hospital-asc-acquisition) | L2 | m-and-a | Hospital ASC acquisition — cash EBITDA after physician leakage |
| [saas-acqui-hire](saas-acqui-hire) | L2 | make-vs-buy | SaaS acqui-hire vs build — 24-month cash including dead-time |
| [distressed-store-four-wall](distressed-store-four-wall) | L3 | investment-decision | Retail distressed-store acquisition four-wall analysis |
| [rare-disease-biotech-ev](rare-disease-biotech-ev) | L3 | investment-decision | Pharma rare-disease biotech valuation — bull vs bear EV |
| [airline-bag-fee](airline-bag-fee) | L3 | pricing | Airline bag-fee increase — elasticity and spill scenarios |
| [saas-seat-to-usage](saas-seat-to-usage) | L2 | pricing | SaaS seat-to-usage price move — net ARR after elasticity and grandfathering |
| [restinn-weekend-pricing](restinn-weekend-pricing) | L1 | pricing | RestInn hotel weekend dynamic pricing optimization |
| [pharma-copay-paths](pharma-copay-paths) | L3 | pricing | Pharma co-pay assistance path comparison |
| [telecom-unlimited-reprice](telecom-unlimited-reprice) | L2 | pricing | Telecom unlimited — net after heavy-user cannibal and network opex |
| [dim-weight-pricing](dim-weight-pricing) | L2 | pricing | Logistics dim-weight — incremental billable pounds minus churn |
| [municipal-water-rates](municipal-water-rates) | L3 | pricing | Municipal water rate — elasticity plus treatment save vs $4.5M plant |
| [crunchora-whitespace](crunchora-whitespace) | L1 | market-sizing | Crunchora CPG distribution white-space growth options |
| [airline-loyalty-match](airline-loyalty-match) | L2 | growth | Airline loyalty status-match — true new members only |
| [saas-ndr-conflict](saas-ndr-conflict) | L3 | profitability | SaaS NDR — CS vs Finance churn/expansion conflict |
| [grocery-fresh-deal](grocery-fresh-deal) | L2 | growth | Grocery fresh vendor deal — GM bps vs extra shrink on SKU subset |
| [streaming-ad-lite](streaming-ad-lite) | L3 | growth | Streaming ad-lite tier — price mix plus ads minus ad-lite churn |
| [greenpouch-go-nogo](greenpouch-go-nogo) | L1 | investment-decision | Compostable snack bag launch/no-go decision |
| [auto-feature-subscription](auto-feature-subscription) | L2 | product | Auto connected-feature subscription after cellular COGS and trim churn |
| [bank-bnpl-feature](bank-bnpl-feature) | L2 | product | Bank BNPL — take-rate minus losses, opex, and revolving NII cannibal |
| [pharma-diagnostic-kit](pharma-diagnostic-kit) | L3 | investment-decision | Pharma diagnostic kit — field false-positive cost, not analytical |
| [industrial-iot-spin](industrial-iot-spin) | L2 | corporate-strategy | Industrial IoT spin — strip captive transfer revenue |
| [retail-media-network](retail-media-network) | L2 | new-business | Retail media network — joiners only, minus guarantees and serving |
| [community-solar-yield](community-solar-yield) | L3 | investment-decision | Community solar — temperate yield and 88% offtake vs 9% hurdle |
| [heroco-private-label](heroco-private-label) | L1 | pricing | Hero brand private-label attack response options |
| [airline-fare-match](airline-fare-match) | L2 | competitive-response | Airline fare-match on overlap ASMs only — vs walk-away spill |
| [saas-freemium-match](saas-freemium-match) | L2 | competitive-response | SaaS freemium match — downgrade leak vs competitor churn |
| [ecomm-price-transparency](ecomm-price-transparency) | L3 | pricing | Retail e-comm price transparency — selective match strategy |
| [airline-cost-turnaround](airline-cost-turnaround) | L3 | turnaround | Airline cost turnaround — strip hedge loss, add labor contract |
| [retail-store-closures](retail-store-closures) | L2 | turnaround | Retail store closures — four-wall save minus stranded leases and halo |
| [cloudsaas-path-to-profit](cloudsaas-path-to-profit) | L1 | profitability | CloudSaaS path to profitability — S&M vs R&D cut |
| [hospital-service-line](hospital-service-line) | L3 | profitability | Hospital service-line turnaround — allocation trap |
| [nonprofit-program-cut](nonprofit-program-cut) | L2 | turnaround | Nonprofit — cut Program B using unrestricted only |

The Harbor dataset name is `consulting-bench/consulting-bench` (see
[`dataset.toml`](../dataset.toml)). Individual task slugs are written kebab-case
names under `consulting-bench/`, matching Terminal-Bench. Original CIP ids stay
on `[metadata].legacy_id`.
