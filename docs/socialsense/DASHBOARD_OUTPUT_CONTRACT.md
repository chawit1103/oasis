# Dashboard Output Contract

SocialSense dashboard integrations should consume the stable contract produced by `socialsense_core.adapters.dashboard_contract.to_dashboard_contract(...)` or `socialsense_core.scenario_packs.run_scenario_pack(...)`.

The contract is deterministic, synthetic-only, and does not call live platform APIs.

## Top-level fields

| Field | Purpose |
|---|---|
| `summary` | Scenario metadata, consumer, platform preset, platform mix, event counts, action counts, and disclaimer. |
| `platform_breakdown` | Per-platform event counts and action counts. |
| `sentiment_signal` | Net sentiment, belief, and intent deltas plus raw opinion signals. |
| `diffusion_signal` | Total reach, max velocity, and raw diffusion signals. |
| `trust_signal` | Net trust delta, direction, and raw trust signals. |
| `risk_signal` | Deterministic risk score and low/medium/high level based on rumor, crisis, correction, and negative-attention actions. |
| `recommended_next_observations` | Human-readable next observations for dashboard or analyst follow-up. |
| `provenance_labels` | Provenance labels such as `synthetic` and `human_authored_scenario`. |
| `runtime_mode` | Runtime mode, normally `research` for these scenario packs. |

## Contract version

`summary.dashboard_contract_version` is currently:

```text
socialsense-dashboard-v1
```

Downstream dashboards should branch on this value before binding chart components.

## Safety boundary

- Synthetic deterministic examples only.
- No real platform APIs.
- No scraping.
- No credentials.
- No real PII.
- Production governance remains owned by downstream applications such as CivicSense or 3C.
