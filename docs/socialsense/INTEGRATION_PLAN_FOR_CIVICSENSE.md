# Integration Plan for CivicSense

CivicSense can integrate later through `socialsense_core.adapters.civicsense_adapter`.

## Interfaces

- `simulate_public_opinion(message, audience_profile, platform_mix, scenario_context, runtime_mode="research")`
- `simulate_crisis_response(crisis_message, audience_profile, platform_mix, scenario_context, runtime_mode="research")`
- `simulate_policy_message_diffusion(policy_message, audience_profile, platform_mix, scenario_context, runtime_mode="research")`

## Later integration steps

1. Translate CivicSense audience groups into `SocialActor` inputs.
2. Translate messages/scenario context into `SocialContent`.
3. Select platform presets using Thai-first defaults.
4. Enforce CivicSense production policy in the adapter/downstream layer.
5. Surface provenance labels and simulation disclaimers in UI/PDF exports.
