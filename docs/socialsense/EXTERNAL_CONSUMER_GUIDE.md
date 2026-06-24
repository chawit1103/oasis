# External Consumer Guide

This guide is for future CivicSense, 3C Simulator, and other downstream applications that want to consume SocialSense Core.

## Recommended import pattern

Use the public package surface:

```python
import socialsense_core as ssc

assert ssc.__version__ == "0.1.0"
contract = ssc.run_scenario_pack("civic_policy_message")
```

Avoid importing internal modules from `actions`, `adapters`, `platforms`, `simulation`, or `scenario_packs` directly in downstream apps. Those paths can change while the public API remains stable.

## Basic dashboard flow

```python
import socialsense_core as ssc

for key in ssc.list_scenario_packs():
    contract = ssc.run_scenario_pack(key)
    print(contract["summary"])
```

Dashboard consumers can bind to:

- `summary`
- `platform_breakdown`
- `sentiment_signal`
- `diffusion_signal`
- `trust_signal`
- `risk_signal`
- `recommended_next_observations`
- `provenance_labels`
- `runtime_mode`

## Version compatibility

`0.1.0` is a foundation integration boundary. During the `0.1.x` series:

- public names in `socialsense_core.__all__` should remain source-compatible where feasible;
- internal module paths are not compatibility guarantees;
- dashboard contract version is separately marked by `summary.dashboard_contract_version`.

## Deployment notes

- Do not publish from this PR.
- Do not require real platform credentials.
- Do not call live platform APIs.
- Treat all included scenario packs as deterministic synthetic demos.
- Downstream applications own production governance, privacy, and policy enforcement.
