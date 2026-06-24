# Integration Plan for 3C Marketing Simulator

3C can integrate later through `socialsense_core.adapters.threec_marketing_adapter`.

## Interfaces

- `simulate_campaign_response(campaign_message, product_context, audience_profile, platform_mix, runtime_mode="research")`
- `simulate_brand_sentiment(brand_message, audience_profile, platform_mix, runtime_mode="research")`
- `simulate_social_commerce_response(offer_message, product_context, audience_profile, platform_mix, runtime_mode="research")`

## Later integration steps

1. Map product/category/offer context into content metadata.
2. Use Facebook/TikTok/YouTube/LINE presets for Thai-first campaigns.
3. Extend deterministic heuristics with segment-specific response curves.
4. Add executive charts and ROI-oriented summary metrics downstream.
