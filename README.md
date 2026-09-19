# Consulting Bench

![Docs](https://img.shields.io/badge/Harbor_docs-000000?style=for-the-badge&logo=mdbook&color=105864)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

[Consulting Bench](https://austinbellinger.com/consulting-bench.html) measures how well agents handle work in a management consulting environment. Each task is a partner email to an associate — read a synthetic matter pack, write a one-page memo, and emit a checkable JSON sidecar. The inital release is 50 tasks.

It runs on [Harbor](https://www.harborframework.com/), the same evaluation harness used by [Terminal-Bench](https://github.com/harbor-framework/terminal-bench-2-1). Any Harbor-supported agent (Terminus, Claude Code, Codex, and others) can be scored with one command.

## Results

One Harbor / terminus-2 trial per model on the hardened 50-task set.

| Model | Pass@1 |
| ----- | ------ |
| GLM 5.3 | 54.0% |
| Gemini 3.8 Flash | 54.0% |
| DeepSeek V4.1 Flash | 52.0% |
| GPT-5.6 Luna | 50.0% |
| Claude Haiku 4.5 | 28.0% |

## Getting started

This walkthrough gets you from a clone to a scored agent run: install Harbor, add a model key, run Terminus-2, and open the job.

### 1. Set up your environment

Clone the repo and install [Harbor](https://github.com/harbor-framework/harbor). Local runs need [Docker](https://docs.docker.com/get-docker/).

```shell
git clone https://github.com/cbelling/management-consulting-bench.git
cd management-consulting-bench
uv tool install harbor
```

To run on [Modal](https://modal.com/) sandboxes instead of local Docker:

```shell
uv tool install "harbor[modal]"
```

### 2. Connect a model provider

The bundled Terminus configs call models through [OpenRouter](https://openrouter.ai/). Copy `.env.example` and add a key:

```shell
cp .env.example .env
```

```
OPENROUTER_API_KEY=...
```

Export it in your shell, or let Harbor read `.env`. Anthropic, OpenAI, and other Harbor-supported providers work the same way — set the matching key and pass `-m` / `-a` on the run.

For Modal, add `MODAL_TOKEN_ID` and `MODAL_TOKEN_SECRET`, or run `modal token new`.

### 3. Run the agent

Start with the three-task smoke slice:

```shell
harbor run -c configs/dry-run.yaml
```

Or one task:

```shell
harbor run -p tasks/restinn-weekend-pricing \
  -a terminus-2 \
  -m openrouter/deepseek/deepseek-v4.1-flash
```

The full 50-task set:

```shell
harbor run -c configs/terminus-2.deepseek-v4.1-flash.yaml
```

The same job on Modal:

```shell
harbor run -c configs/terminus-2.deepseek-v4.1-flash.yaml -e modal
```

Any Harbor-supported agent (Terminus, Claude Code, Codex, and others) can replace Terminus-2. Swap the model with `-m`.

To check that the environments and graders work without a model, run the oracles:

```shell
harbor run -c configs/oracle.yaml
```

### 4. Inspect the run

Harbor writes each job under `jobs/`. Open the local viewer:

```shell
harbor view jobs
```

That serves `http://127.0.0.1:8080`. Open the job, then a trial. You will see the agent transcript, `/app/output/memo.md`, `/app/output/answer.json`, and whether the script grader passed (`reward.txt` is `1` or `0`).

Recorded scoreboard jobs live in `evals/`. Modal wrappers for those runs are in `scripts/` (`run_dry_run.sh`, `run_full_bench_concurrent.sh`, `run_hardened_bench_concurrent.sh`).

## Tasks

| Slug                                                           | Category             | Description                                                                                        |
| -------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------- |
| [aerotread-tire-tam](tasks/aerotread-tire-tam)                 | market-sizing        | Should a tire maker bid a US passenger-jet replacement contract? Size that market only.            |
| [economy-hotel-revenue](tasks/economy-hotel-revenue)           | market-sizing        | Size US economy-hotel room revenue to decide if a $400M pricing tool is worth building.            |
| [india-smartphone-sellout](tasks/india-smartphone-sellout)     | market-sizing        | Size India's annual smartphone sales and decide whether a handset maker should enter.              |
| [piano-tunings-market](tasks/piano-tunings-market)             | market-sizing        | Estimate yearly US piano-tuning demand so a foundation can size a technician scholarship.          |
| [golf-balls-lost](tasks/golf-balls-lost)                       | market-sizing        | Estimate how many golf balls Americans lose each year to size replacement demand.                  |
| [hospital-outpatient-gap](tasks/hospital-outpatient-gap)       | profitability        | Reconcile conflicting surgery-center P&Ls and decide whether to expand outpatient work.            |
| [saas-margin-compression](tasks/saas-margin-compression)       | profitability        | Figure out why a SaaS company's gross margin fell and which recurring cost to attack.              |
| [hotel-fb-mix](tasks/hotel-fb-mix)                             | profitability        | Decide whether a hotel should keep banquet catering, close its restaurants, or both.               |
| [pharma-plant-oee](tasks/pharma-plant-oee)                     | operations           | Decide if a drug plant should add a Saturday shift after measuring true line utilization.          |
| [last-mile-zone-c](tasks/last-mile-zone-c)                     | profitability        | Decide whether a last-mile carrier should exit its least-dense delivery zone.                      |
| [streaming-contribution](tasks/streaming-contribution)         | profitability        | Reconcile why a streamer looks profitable to product and unprofitable to the board.                |
| [urgent-care-adjacency](tasks/urgent-care-adjacency)           | investment-decision  | Decide if a hospital system should open six urgent-care clinics after ED cannibalization.          |
| [airline-new-route](tasks/airline-new-route)                   | investment-decision  | Decide whether an airline should launch Boston–Lisbon after airport incentives expire.             |
| [battery-materials-entry](tasks/battery-materials-entry)       | market-entry         | Decide if a chemical company should spend $900M to enter US battery-materials processing.          |
| [pet-insurance-adjacency](tasks/pet-insurance-adjacency)       | adjacency            | Decide whether an insurer should launch a pet-insurance product.                                   |
| [marketplace-take-rate](tasks/marketplace-take-rate)           | strategy             | Decide if an e-commerce company should flip a category from first-party sales to a 3P marketplace. |
| [coop-dtc-beef](tasks/coop-dtc-beef)                           | go-to-market         | Decide if a farm co-op should sell beef boxes direct to consumers instead of wholesale.            |
| [organic-cpg-acquisition](tasks/organic-cpg-acquisition)       | m-and-a              | Decide whether to bid on an organic food brand after adjusting returns for synergies.              |
| [hospital-asc-acquisition](tasks/hospital-asc-acquisition)     | m-and-a              | Decide whether a hospital should buy an ambulatory surgery center.                                 |
| [saas-acqui-hire](tasks/saas-acqui-hire)                       | make-vs-buy          | Compare buying a small engineering team versus building an observability module in-house.          |
| [distressed-store-four-wall](tasks/distressed-store-four-wall) | investment-decision  | Decide whether a grocer should buy two failing stores.                                             |
| [rare-disease-biotech-ev](tasks/rare-disease-biotech-ev)       | investment-decision  | Decide whether to pay $1.2B for a rare-disease biotech, walk, or use a contingent payout.          |
| [airline-bag-fee](tasks/airline-bag-fee)                       | pricing              | Decide whether an airline should raise checked-bag fees from $30 to $40.                           |
| [saas-seat-to-usage](tasks/saas-seat-to-usage)                 | pricing              | Decide whether a SaaS company should switch from per-seat to usage-based pricing.                  |
| [restinn-weekend-pricing](tasks/restinn-weekend-pricing)       | pricing              | Pick the weekend room-rate premium that maximizes profit for a 100-room hotel.                     |
| [pharma-copay-paths](tasks/pharma-copay-paths)                 | pricing              | Choose which patient co-pay assistance program a pharma company should launch.                     |
| [telecom-unlimited-reprice](tasks/telecom-unlimited-reprice)   | pricing              | Decide whether a mobile carrier should launch a $75 unlimited plan.                                |
| [dim-weight-pricing](tasks/dim-weight-pricing)                 | pricing              | Decide whether a parcel carrier should bill by package size instead of actual weight.              |
| [municipal-water-rates](tasks/municipal-water-rates)           | pricing              | Decide whether a city should raise water rates or delay a treatment-plant project.                 |
| [crunchora-whitespace](tasks/crunchora-whitespace)             | market-sizing        | Pick the first growth move for a snack brand: more stores, a new SKU, or a price increase.         |
| [airline-loyalty-match](tasks/airline-loyalty-match)           | growth               | Decide whether an airline should run a loyalty status-match campaign.                              |
| [saas-ndr-conflict](tasks/saas-ndr-conflict)                   | profitability        | Reconcile CS vs Finance churn numbers and say whether retention clears the board bar.              |
| [grocery-fresh-deal](tasks/grocery-fresh-deal)                 | growth               | Decide whether a grocer should take a produce deal that lifts margin but raises spoilage.          |
| [streaming-ad-lite](tasks/streaming-ad-lite)                   | growth               | Decide whether a streamer should launch a cheaper ad-supported subscription tier.                  |
| [greenpouch-go-nogo](tasks/greenpouch-go-nogo)                 | investment-decision  | Decide whether a snack brand should launch a compostable bag.                                      |
| [auto-feature-subscription](tasks/auto-feature-subscription)   | product              | Decide whether a carmaker should sell a connected feature as an $18/month subscription.            |
| [bank-bnpl-feature](tasks/bank-bnpl-feature)                   | product              | Decide whether a bank should add buy-now-pay-later at checkout.                                    |
| [pharma-diagnostic-kit](tasks/pharma-diagnostic-kit)           | investment-decision  | Decide whether a diagnostics company should launch a test kit after real-world false positives.    |
| [industrial-iot-spin](tasks/industrial-iot-spin)               | corporate-strategy   | Decide whether a parent company should spin out its IoT unit.                                      |
| [retail-media-network](tasks/retail-media-network)             | new-business         | Decide whether a retailer should build an in-store advertising network.                            |
| [community-solar-yield](tasks/community-solar-yield)           | investment-decision  | Decide whether to build an 18 MW community solar farm using realistic local yield.                 |
| [heroco-private-label](tasks/heroco-private-label)             | pricing              | Pick how a branded CPG company should respond to a store-brand attack.                             |
| [airline-fare-match](tasks/airline-fare-match)                 | competitive-response | Decide whether an airline should match a competitor's 8% fare cut on overlapping routes.           |
| [saas-freemium-match](tasks/saas-freemium-match)               | competitive-response | Decide whether a SaaS company should match a competitor's free tier.                               |
| [ecomm-price-transparency](tasks/ecomm-price-transparency)     | pricing              | Pick which price-matching strategy maximizes a retailer's profit.                                  |
| [airline-cost-turnaround](tasks/airline-cost-turnaround)       | turnaround           | Decide if an airline's run-rate profit already hits the board's $500M target.                      |
| [retail-store-closures](tasks/retail-store-closures)           | turnaround           | Decide whether a retailer should close 40 losing stores.                                           |
| [cloudsaas-path-to-profit](tasks/cloudsaas-path-to-profit)     | profitability        | Choose whether a cash-burning SaaS company should cut sales or R&D to reach breakeven.             |
| [hospital-service-line](tasks/hospital-service-line)           | profitability        | Decide which hospital service lines to keep, close, or expand after stripping allocations.         |
| [nonprofit-program-cut](tasks/nonprofit-program-cut)           | turnaround           | Decide whether a nonprofit should shut a money-losing program.                                     |

## License

MIT. See [LICENSE](LICENSE).
