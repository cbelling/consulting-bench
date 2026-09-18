window.LEADERBOARD = {
  "bench": "Partner-50",
  "set": "hardened-v1",
  "n_tasks": 50,
  "mix": {
    "L1": 5,
    "L2": 25,
    "L3": 20
  },
  "environment": "modal",
  "agent": "terminus-2",
  "n_concurrent_trials": 20,
  "updated_at": "2026-09-18T23:02:09.002273+00:00",
  "cost_estimate": {
    "method": "Scale DeepSeek V4.1 Flash hardened-v1 token volume to OpenRouter list prices, plus ~$1 Modal per 50-task pass.",
    "baseline_job": "hardened-v1-deepseek-v4.1-flash-concurrent",
    "baseline_tokens": {
      "input": 1077282,
      "output": 562730
    },
    "modal_usd_per_pass": 1.0,
    "four_flagships_expected_usd": 33.0,
    "four_flagships_upper_usd": 55.0,
    "notes": "Expected band is about $35\u201345 if token volume stays near the DeepSeek baseline. Upper band is about $70 if thinking models emit ~2\u00d7 output tokens."
  },
  "models": [
    {
      "id": "deepseek-v4.1-flash",
      "display": "DeepSeek V4.1 Flash",
      "lab": "DeepSeek",
      "openrouter": "openrouter/deepseek/deepseek-v4.1-flash",
      "role": "cheap-model baseline",
      "job_name": "hardened-v1-deepseek-v4.1-flash-concurrent",
      "list_price_usd_per_m": {
        "input": 0.15,
        "output": 0.6
      },
      "estimated_llm_usd": 0.5,
      "estimated_llm_usd_2x_output": 0.84,
      "status": "complete",
      "n_trials": 50,
      "n_pass": 26,
      "n_fail": 24,
      "n_errors": 0,
      "mean_reward": 0.52,
      "cost_usd": 0.7265428428239997,
      "n_input_tokens": 1077282,
      "n_output_tokens": 562730,
      "total_runtime_sec": 580,
      "finished_at": "2026-09-18T21:32:40.160575",
      "failed_tasks": [
        "CIP-010",
        "CIP-018",
        "CIP-019",
        "CIP-028",
        "CIP-032",
        "CIP-034",
        "CIP-038",
        "CIP-040",
        "CIP-043",
        "CIP-044",
        "CIP-050",
        "CIP-052",
        "CIP-054",
        "CIP-057",
        "CIP-059",
        "CIP-062",
        "CIP-064",
        "CIP-066",
        "CIP-075",
        "CIP-085",
        "CIP-090",
        "CIP-096",
        "CIP-097",
        "CIP-100"
      ],
      "passed_tasks": [
        "CIP-003",
        "CIP-005",
        "CIP-006",
        "CIP-012",
        "CIP-015",
        "CIP-016",
        "CIP-021",
        "CIP-025",
        "CIP-030",
        "CIP-033",
        "CIP-041",
        "CIP-053",
        "CIP-055",
        "CIP-063",
        "CIP-067",
        "CIP-070",
        "CIP-076",
        "CIP-077",
        "CIP-079",
        "CIP-084",
        "CIP-087",
        "CIP-089",
        "CIP-091",
        "CIP-093",
        "CIP-098",
        "CIP-099"
      ],
      "by_level": {
        "L1": {
          "n": 5,
          "n_pass": 3,
          "mean": 0.6
        },
        "L2": {
          "n": 25,
          "n_pass": 13,
          "mean": 0.52
        },
        "L3": {
          "n": 20,
          "n_pass": 10,
          "mean": 0.5
        }
      },
      "trials": [
        {
          "task": "CIP-003",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-005",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-006",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-010",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-012",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-015",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-016",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-018",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-019",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-021",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-025",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-028",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-030",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-032",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-033",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-034",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-038",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-040",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-041",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-043",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-044",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-050",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-052",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-053",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-054",
          "level": "L1",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-055",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-057",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-059",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-062",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-063",
          "level": "L1",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-064",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-066",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-067",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-070",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-075",
          "level": "L1",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-076",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-077",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-079",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-084",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-085",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-087",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-089",
          "level": "L1",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-090",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-091",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-093",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-096",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-097",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-098",
          "level": "L1",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-099",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-100",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        }
      ]
    },
    {
      "id": "gpt-5.4",
      "display": "GPT-5.4",
      "lab": "OpenAI",
      "openrouter": "openrouter/openai/gpt-5.4",
      "role": "flagship",
      "job_name": "hardened-v1-gpt-5.4-concurrent",
      "list_price_usd_per_m": {
        "input": 2.5,
        "output": 15.0
      },
      "estimated_llm_usd": 11.13,
      "estimated_llm_usd_2x_output": 19.58,
      "status": "complete",
      "n_trials": 50,
      "n_pass": 27,
      "n_fail": 23,
      "n_errors": 0,
      "mean_reward": 0.54,
      "cost_usd": 2.1379685,
      "n_input_tokens": 395399,
      "n_output_tokens": 83121,
      "total_runtime_sec": 69,
      "finished_at": "2026-09-18T22:54:44.397611",
      "failed_tasks": [
        "CIP-015",
        "CIP-016",
        "CIP-018",
        "CIP-019",
        "CIP-028",
        "CIP-032",
        "CIP-033",
        "CIP-034",
        "CIP-040",
        "CIP-043",
        "CIP-044",
        "CIP-050",
        "CIP-052",
        "CIP-057",
        "CIP-062",
        "CIP-064",
        "CIP-075",
        "CIP-076",
        "CIP-084",
        "CIP-091",
        "CIP-096",
        "CIP-097",
        "CIP-100"
      ],
      "passed_tasks": [
        "CIP-003",
        "CIP-005",
        "CIP-006",
        "CIP-010",
        "CIP-012",
        "CIP-021",
        "CIP-025",
        "CIP-030",
        "CIP-038",
        "CIP-041",
        "CIP-053",
        "CIP-054",
        "CIP-055",
        "CIP-059",
        "CIP-063",
        "CIP-066",
        "CIP-067",
        "CIP-070",
        "CIP-077",
        "CIP-079",
        "CIP-085",
        "CIP-087",
        "CIP-089",
        "CIP-090",
        "CIP-093",
        "CIP-098",
        "CIP-099"
      ],
      "by_level": {
        "L1": {
          "n": 5,
          "n_pass": 4,
          "mean": 0.8
        },
        "L2": {
          "n": 25,
          "n_pass": 11,
          "mean": 0.44
        },
        "L3": {
          "n": 20,
          "n_pass": 12,
          "mean": 0.6
        }
      },
      "trials": [
        {
          "task": "CIP-003",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-005",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-006",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-010",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-012",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-015",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-016",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-018",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-019",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-021",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-025",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-028",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-030",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-032",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-033",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-034",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-038",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-040",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-041",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-043",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-044",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-050",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-052",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-053",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-054",
          "level": "L1",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-055",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-057",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-059",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-062",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-063",
          "level": "L1",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-064",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-066",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-067",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-070",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-075",
          "level": "L1",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-076",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-077",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-079",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-084",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-085",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-087",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-089",
          "level": "L1",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-090",
          "level": "L2",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-091",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-093",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-096",
          "level": "L3",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-097",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        },
        {
          "task": "CIP-098",
          "level": "L1",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-099",
          "level": "L3",
          "reward": 1.0,
          "exception": null
        },
        {
          "task": "CIP-100",
          "level": "L2",
          "reward": 0.0,
          "exception": null
        }
      ]
    },
    {
      "id": "claude-haiku-4.5",
      "display": "Claude Haiku 4.5",
      "lab": "Anthropic",
      "openrouter": "openrouter/anthropic/claude-haiku-4.5",
      "role": "flagship",
      "job_name": "hardened-v1-claude-haiku-4.5-concurrent",
      "list_price_usd_per_m": {
        "input": 1.0,
        "output": 5.0
      },
      "estimated_llm_usd": 3.89,
      "estimated_llm_usd_2x_output": 6.7,
      "status": "pending"
    },
    {
      "id": "gemini-3.1-pro",
      "display": "Gemini 3.1 Pro",
      "lab": "Google",
      "openrouter": "openrouter/google/gemini-3.1-pro-preview",
      "role": "flagship",
      "job_name": "hardened-v1-gemini-3.1-pro-concurrent",
      "list_price_usd_per_m": {
        "input": 2.0,
        "output": 12.0
      },
      "estimated_llm_usd": 8.91,
      "estimated_llm_usd_2x_output": 15.66,
      "status": "pending"
    },
    {
      "id": "grok-4.6",
      "display": "Grok 4.6",
      "lab": "xAI",
      "openrouter": "openrouter/x-ai/grok-4.6",
      "role": "flagship",
      "job_name": "hardened-v1-grok-4.6-concurrent",
      "list_price_usd_per_m": {
        "input": 2.0,
        "output": 6.0
      },
      "estimated_llm_usd": 5.53,
      "estimated_llm_usd_2x_output": 8.91,
      "status": "pending"
    }
  ],
  "tasks": [
    {
      "id": "CIP-003",
      "level": "L2",
      "topic": "AeroTread NB tire TAM (exclude cargo/spares)",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-005",
      "level": "L2",
      "topic": "US economy-hotel room revenue (exclude midscale)",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-006",
      "level": "L2",
      "topic": "India smartphone sell-out (exclude gray sell-in)",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-010",
      "level": "L3",
      "topic": "Piano tunings \u2014 unusual stock \u00d7 frequency",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-012",
      "level": "L3",
      "topic": "Golf balls lost \u2014 conflicting exhibits",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-015",
      "level": "L3",
      "topic": "Hospital outpatient surgery profit gap",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-016",
      "level": "L2",
      "topic": "SaaS gross margin compression",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-018",
      "level": "L2",
      "topic": "Hotel F&B profit mix",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-019",
      "level": "L2",
      "topic": "Pharma plant utilization",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-021",
      "level": "L3",
      "topic": "Logistics last-mile Zone C contribution",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-025",
      "level": "L3",
      "topic": "Media streaming contribution layers",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-028",
      "level": "L3",
      "topic": "Hospital urgent-care adjacency",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-030",
      "level": "L2",
      "topic": "Airline new route",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-032",
      "level": "L3",
      "topic": "Battery materials entry \u2014 conflicting margins",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-033",
      "level": "L2",
      "topic": "Insurance pet adjacency",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-034",
      "level": "L2",
      "topic": "E-commerce 3P marketplace",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-038",
      "level": "L3",
      "topic": "Ag co-op DTC beef",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-040",
      "level": "L2",
      "topic": "CPG M&A organic brand",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-041",
      "level": "L2",
      "topic": "Hospital ASC acquisition",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-043",
      "level": "L2",
      "topic": "SaaS acqui-hire vs build",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-044",
      "level": "L3",
      "topic": "Retail distressed-store four-wall",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-050",
      "level": "L3",
      "topic": "Pharma rare-disease biotech EV",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-052",
      "level": "L3",
      "topic": "Airline bag-fee increase",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-053",
      "level": "L2",
      "topic": "SaaS pricing model",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-054",
      "level": "L1",
      "topic": "RestInn weekend dynamic pricing",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-055",
      "level": "L3",
      "topic": "Pharma co-pay assistance paths",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-057",
      "level": "L2",
      "topic": "Telecom unlimited repricing",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-059",
      "level": "L2",
      "topic": "Logistics dim-weight",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-062",
      "level": "L3",
      "topic": "Municipal water rates",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-063",
      "level": "L1",
      "topic": "Crunchora CPG distribution white space",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-064",
      "level": "L2",
      "topic": "Airline loyalty growth",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-066",
      "level": "L3",
      "topic": "SaaS NDR \u2014 CS vs Finance conflict",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-067",
      "level": "L2",
      "topic": "Grocery fresh growth",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-070",
      "level": "L3",
      "topic": "Media ad-tier growth",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-075",
      "level": "L1",
      "topic": "GreenPouch compostable bag go/no-go",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-076",
      "level": "L2",
      "topic": "Auto subscription feature",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-077",
      "level": "L2",
      "topic": "Bank BNPL feature",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-079",
      "level": "L3",
      "topic": "Pharma diagnostic kit",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-084",
      "level": "L2",
      "topic": "Industrial IoT spin",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-085",
      "level": "L2",
      "topic": "Retail media network",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-087",
      "level": "L3",
      "topic": "Energy community solar",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-089",
      "level": "L1",
      "topic": "HeroCo private-label response",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-090",
      "level": "L2",
      "topic": "Airline competitive response",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-091",
      "level": "L2",
      "topic": "SaaS freemium response",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-093",
      "level": "L3",
      "topic": "Retail e-comm price transparency",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-096",
      "level": "L3",
      "topic": "Airline cost turnaround",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-097",
      "level": "L2",
      "topic": "Retail store closures",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-098",
      "level": "L1",
      "topic": "CloudSaaS path to profitability",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-099",
      "level": "L3",
      "topic": "Hospital service-line turnaround",
      "results": {
        "deepseek-v4.1-flash": 1,
        "gpt-5.4": 1,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    },
    {
      "id": "CIP-100",
      "level": "L2",
      "topic": "Nonprofit turnaround",
      "results": {
        "deepseek-v4.1-flash": 0,
        "gpt-5.4": 0,
        "claude-haiku-4.5": null,
        "gemini-3.1-pro": null,
        "grok-4.6": null
      }
    }
  ]
};
