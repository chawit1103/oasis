# Next Integration Steps

PR #3 still does **not** modify CivicSense or 3C. It prepares stable scenario packs and dashboard contracts that those applications can consume later.

## CivicSense next steps

1. Add SocialSense Core as a dependency or vendored module in a future CivicSense PR.
2. Convert CivicSense audience/group inputs into SocialSense audience profiles.
3. Start with these scenario packs:
   - `civic_policy_message`
   - `civic_crisis_response`
4. Bind dashboard widgets to:
   - `summary`
   - `platform_breakdown`
   - `sentiment_signal`
   - `diffusion_signal`
   - `trust_signal`
   - `risk_signal`
   - `recommended_next_observations`
5. Preserve `provenance_labels`, `runtime_mode`, and simulation disclaimers in UI and exports.
6. Add CivicSense-owned production governance checks outside SocialSense Core.

## 3C Marketing Simulator next steps

1. Add SocialSense Core to the future 3C app/service.
2. Convert product, campaign, and audience definitions into scenario-pack style inputs.
3. Start with these scenario packs:
   - `threec_marketing_campaign`
   - `threec_brand_sentiment`
   - `social_commerce_response`
4. Use `platform_breakdown` and `sentiment_signal` for campaign dashboards.
5. Use `diffusion_signal`, `trust_signal`, and `risk_signal` as supporting analyst context, not as direct ROI truth.

## Constraints to keep

- No live platform API calls in SocialSense Core.
- No scraping.
- No credentials.
- No real PII.
- Synthetic/deterministic defaults remain the baseline for reproducible QA.
