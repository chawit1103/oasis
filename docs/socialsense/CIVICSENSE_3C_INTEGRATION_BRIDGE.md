# CivicSense and 3C Integration Bridge

This document describes how downstream products should consume SocialSense Core after PR #2. It is intentionally a bridge contract only: **do not modify CivicSense or 3C repositories in this phase**.

## What PR #2 adds

- Richer synthetic CivicSense public-opinion demo scenarios.
- Richer synthetic 3C marketing campaign demo scenarios.
- Thai platform mix presets:
  - `civic_default_thailand`
  - `marketing_default_thailand`
  - `crisis_default_thailand`
- A dashboard-oriented result summary attached to `SimulationResult.summary`.
- Tests for Thai presets and adapter output contracts.

## Thai platform mix presets

All Thai presets are registered in `get_default_platform_registry()` and are available through `PlatformPresetRegistry.get(...)`.

| Preset | Intended consumer | Platform mix | Primary behavior modules |
|---|---|---|---|
| `civic_default_thailand` | CivicSense public opinion and policy diffusion | LINE, Facebook, TikTok, YouTube | public feed, private messaging, community group, information diffusion, opinion formation, trust/credibility |
| `marketing_default_thailand` | 3C marketing campaign and social commerce | LINE, Facebook, TikTok, YouTube | public feed, short video, long-form video, influencer network, recommendation, social commerce, opinion formation |
| `crisis_default_thailand` | CivicSense crisis response / tabletop simulations | LINE, Facebook, TikTok, YouTube | private messaging, community group, public feed, information diffusion, trust/credibility, crisis spread |

## Dashboard summary format

Adapters return normal `SimulationResult` objects. Dashboard integration fields are added under `result.summary`:

| Field | Purpose |
|---|---|
| `dashboard_version` | Stable dashboard format marker, currently `socialsense-core-v1`. |
| `scenario_family` | Adapter scenario family such as `civicsense_public_opinion` or `threec_marketing_campaign`. |
| `platform_preset` | Preset key used to resolve the platform mix. |
| `headline_metrics` | Compact counters suitable for dashboard cards. |
| `series.actions_by_step` | Ordered event/action timeline. |
| `series.action_counts` | Count by action type. |
| `signals.recommendation` | Recommendation signal objects converted to dictionaries. |
| `signals.diffusion` | Diffusion signal objects converted to dictionaries. |
| `signals.opinion` | Opinion signal objects converted to dictionaries. |
| `signals.trust` | Trust signal objects converted to dictionaries. |
| `integration_contract` | Consumer name, schema version, no-external-services marker, synthetic-only PII policy. |
| `input_metadata` | Echo of synthetic scenario inputs useful for dashboard provenance. |

## CivicSense consumption plan

CivicSense should later call SocialSense Core through the adapter layer, not by importing platform preset internals directly.

Recommended later flow:

1. Convert CivicSense audience groups into `audience_profile` dictionaries.
2. Pass message/scenario context into one of:
   - `simulate_public_opinion(...)`
   - `simulate_crisis_response(...)`
   - `simulate_policy_message_diffusion(...)`
3. Use one of the Thai presets, or omit `platform_mix` to use the adapter default:
   - public opinion / policy diffusion → `civic_default_thailand`
   - crisis response → `crisis_default_thailand`
4. Read `result.summary["headline_metrics"]` for top dashboard cards.
5. Read `result.summary["series"]["actions_by_step"]` for timeline tables.
6. Read `result.summary["signals"]` for chart inputs.
7. Preserve `result.provenance_labels` and `simulation_disclaimer` in the UI/report/export layer.

Example:

```python
from socialsense_core.adapters.civicsense_adapter import simulate_public_opinion

result = simulate_public_opinion(
    message="Synthetic policy explainer",
    audience_profile={"name": "Synthetic Bangkok commuters", "country": "TH"},
    platform_mix="civic_default_thailand",
    scenario_context="public consultation demo",
)

cards = result.summary["headline_metrics"]
timeline = result.summary["series"]["actions_by_step"]
signals = result.summary["signals"]
```

## 3C Marketing Simulator consumption plan

3C should call the marketing adapter layer and use `marketing_default_thailand` for Thai-first campaign simulation.

Recommended later flow:

1. Convert product/category/offer context into `product_context`.
2. Convert segment/persona into `audience_profile`.
3. Call one of:
   - `simulate_campaign_response(...)`
   - `simulate_brand_sentiment(...)`
   - `simulate_social_commerce_response(...)`
4. Read `headline_metrics.purchase_intent_events`, `engagement_events`, and the signal arrays for dashboard and ROI-oriented summaries.
5. Keep all examples synthetic until a downstream production governance layer is designed.

Example:

```python
from socialsense_core.adapters.threec_marketing_adapter import simulate_campaign_response

result = simulate_campaign_response(
    campaign_message="Synthetic creator-led product launch",
    product_context="mock healthy snack bundle",
    audience_profile={"name": "Synthetic Thai shoppers", "country": "TH"},
    platform_mix="marketing_default_thailand",
)

summary = result.summary
```

## Boundaries

- No CivicSense repo changes in PR #2.
- No 3C repo changes in PR #2.
- No live platform API calls.
- No scraping.
- No platform credentials.
- No real PII required.
- All demos remain synthetic and deterministic.
