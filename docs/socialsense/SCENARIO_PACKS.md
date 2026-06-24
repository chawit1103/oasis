# Scenario Packs

Scenario packs are reusable deterministic inputs for CivicSense and 3C dashboard integration. They live in `socialsense_core/scenario_packs.py`.

## Available packs

| Key | Consumer | Platform preset | Purpose |
|---|---|---|---|
| `civic_policy_message` | CivicSense | `civic_default_thailand` | Policy message diffusion dashboard demo. |
| `civic_crisis_response` | CivicSense | `crisis_default_thailand` | Crisis response tabletop / rumor-correction demo. |
| `threec_marketing_campaign` | 3C Marketing Simulator | `marketing_default_thailand` | Campaign engagement and purchase-intent demo. |
| `threec_brand_sentiment` | 3C Marketing Simulator | `marketing_default_thailand` | Brand comment, creator, and trust response demo. |
| `social_commerce_response` | 3C Marketing Simulator | `commerce_default_thailand` | Social-commerce offer, review prompt, and purchase-intent demo. |

## API

```python
from socialsense_core.scenario_packs import list_scenario_packs, get_scenario_pack, run_scenario_pack

keys = list_scenario_packs()
pack = get_scenario_pack("civic_policy_message")
contract = run_scenario_pack("civic_policy_message")
```

`run_scenario_pack(...)` returns the dashboard output contract described in `DASHBOARD_OUTPUT_CONTRACT.md`.

## Determinism

All scenario packs use synthetic actors, synthetic content, deterministic action sequences, and the SocialSense deterministic runner. They are designed for integration smoke tests and dashboard development before CivicSense or 3C connects live app data.
