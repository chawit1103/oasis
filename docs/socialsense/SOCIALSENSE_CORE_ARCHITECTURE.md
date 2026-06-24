# SocialSense Core Architecture

Date: 2026-06-24
Status: Phase 2 architecture baseline
Scope: research-first SocialSense core abstractions, behavior modules, platform presets, simulation contracts, signals, and governance seams. This document defines reusable architecture only; it does not add project-specific hard-coded policy restrictions or live-platform integrations.

## Design goals

SocialSense is a reusable simulation layer on top of OASIS concepts. It keeps OASIS's useful agent/action/platform/recommendation separation while making the domain model explicit enough to support multiple social surfaces: public feeds, community groups, private messaging, short video, long-form video, influencer networks, recommendation discovery, information diffusion, opinion formation, trust and credibility, social commerce, and crisis spread.

The core must remain:

1. Research-first: deterministic and synthetic by default, suitable for experiments, reproducible benchmarks, and scenario analysis.
2. Behavior-driven: simulations are composed from behavior modules and platform presets rather than from one hard-coded social network.
3. Governable: runtime mode, provenance labels, event metadata, and optional governance hooks are present at core boundaries.
4. Production-aware but policy-neutral: production runtime can attach review, audit, safety, privacy, or compliance hooks without embedding one project's restrictions in reusable core code.
5. Adapter-friendly: CivicSense, 3C marketing, or future verticals should map their own scenarios onto the same abstractions without changing the core.

## Architecture layers

```
Scenario / vertical adapter
        |
        v
SimulationContext -----> DeterministicSimulationRunner -----> SimulationResult
        |                         |                                  |
        |                         v                                  v
        |                 SocialEvent / EventLog             RecommendationSignal
        |                         |                          DiffusionSignal
        v                         |                          OpinionSignal
SocialActor, SocialContent,       |                          TrustSignal
SocialAction, SocialPlatformPreset|
        |                         v
        +-----------------> behavior/action registries
```

## Core abstractions

### SocialAction

Source: `socialsense_core/actions/types.py`

`SocialAction` is the normalized request shape for behavior execution. It is deliberately platform-neutral.

Fields:

- `action_type`: canonical action verb, for example `post`, `watch_video`, `forward_message`, `trend_topic`, `evaluate_source_trust`.
- `actor_id`: actor performing the action.
- `content_id`: optional content being acted on.
- `target_id`: optional target actor, group, channel, source, or entity.
- `platform`: optional platform preset key such as `x_twitter`, `reddit`, `line`, `facebook`, `tiktok`, or `youtube`.
- `payload`: arbitrary structured parameters for the behavior module or adapter.

Responsibilities:

- Provide one action envelope for manual, deterministic, and future LLM-driven simulation flows.
- Keep OASIS action mappings outside adapters when possible.
- Preserve extensibility through `payload` without requiring schema changes for every experiment.

Non-goals:

- It is not a live API call.
- It does not enforce project-specific policy decisions.

### SocialEvent

Source: `socialsense_core/events/types.py`

`SocialEvent` records an executed `SocialAction` plus simulation metadata.

Fields:

- `event_id`: deterministic or runtime-generated event identifier.
- `action`: the normalized `SocialAction` that was executed.
- `timestamp`: event time, defaulting to UTC now but deterministic runners may override it.
- `provenance`: tuple of `ProvenanceLabel` values.
- `metadata`: runtime-specific annotations such as platform, runtime mode, policy hook IDs, trace references, or audit handles.

Responsibilities:

- Build an auditable event stream from synthetic action execution.
- Preserve provenance and governance-relevant metadata at the event boundary.
- Feed event summaries, diffusion metrics, trust updates, and downstream adapters.

### SocialActor

Source: `socialsense_core/personas/types.py`

`SocialActor` is the platform-neutral synthetic persona state.

Fields:

- `actor_id`: stable actor identifier.
- `display_name`: human-readable label for logs and scenario authoring.
- `traits`: structured persona, demographic, behavioral, or cohort attributes.
- `trust_score`: baseline trust/credibility score.
- `sentiment`: current sentiment state.
- `belief`: current belief state.
- `intent`: current intent state.

Responsibilities:

- Support opinion, trust, recommendation, and diffusion behavior modules.
- Avoid storing raw PII in core experiments unless a governed adapter explicitly provides sanitized fields.

### SocialContent

Source: `socialsense_core/personas/types.py`

`SocialContent` is the platform-neutral content object acted on by agents and recommendation systems.

Fields:

- `content_id`: stable content identifier.
- `text`: text or summary representation for deterministic simulations.
- `author_id`: optional author actor.
- `topic`: optional scenario topic/category.
- `metadata`: structured content properties such as media type, source, language, channel, product, or moderation labels.

Responsibilities:

- Let behavior modules reason over content without depending on one platform database schema.
- Carry enough metadata for future multimodal or vertical-specific adapters.

### SocialPlatformPreset

Source: `socialsense_core/platforms/base.py`

`SocialPlatformPreset` describes a social surface as a composition of behavior modules and available actions.

Fields:

- `key`: stable preset key.
- `display_name`: readable platform label.
- `behavior_modules`: behavior module keys used by this platform.
- `actions`: normalized actions available on the platform.
- `recommendation_signals`: feature names or signal families used by platform-specific discovery.
- `context_notes`: explanatory notes for scenario builders and adapters.
- `oasis_mapping`: optional map from OASIS `ActionType` names to SocialSense action verbs.

Default presets:

- `x_twitter`: public feed, recommendation, information diffusion, opinion formation.
- `reddit`: community group, public feed, trust/credibility, information diffusion.
- `line`: private messaging, community group, trust/credibility, information diffusion, crisis spread.
- `facebook`: public feed, community group, influencer network, social commerce, crisis spread.
- `tiktok`: short video, influencer network, recommendation, social commerce, opinion formation.
- `youtube`: long-form video, short video, influencer network, recommendation, trust/credibility.

Responsibilities:

- Keep platform differences data-driven.
- Make OASIS-to-SocialSense migration explicit through `oasis_mapping`.
- Allow new platform surfaces without changing simulation runners.

### SocialBehaviorModule

Source: `socialsense_core/behaviors/types.py`

`SocialBehaviorModule` groups actions and expected signal families for a reusable social behavior.

Fields:

- `key`: stable module key.
- `name`: human-readable name.
- `actions`: normalized action verbs owned by the module.
- `description`: concise behavioral purpose.
- `signals`: signal class names emitted or consumed by the module.
- `metadata`: extra descriptors for scenario authors.

Default modules:

- `public_feed`
- `community_group`
- `private_messaging`
- `short_video`
- `long_form_video`
- `influencer_network`
- `recommendation_discovery`
- `information_diffusion`
- `opinion_formation`
- `trust_credibility`
- `social_commerce`
- `crisis_spread`

Responsibilities:

- Make experiments behavior-driven rather than platform-driven.
- Provide a registry boundary for adding/removing capabilities.
- Keep action sets auditable for tests and governance review.

### SimulationContext

Source: `socialsense_core/simulation/context.py`

`SimulationContext` is the immutable input contract for a simulation run.

Fields:

- `scenario`: scenario name or narrative identifier.
- `actors`: tuple of `SocialActor` inputs.
- `content`: tuple of `SocialContent` inputs.
- `platform_mix`: tuple of platform preset keys participating in the scenario.
- `actions`: tuple of `SocialAction` steps to execute.
- `runtime_mode`: `RuntimeMode.RESEARCH` by default, optionally `RuntimeMode.PRODUCTION`.
- `provenance_labels`: tuple of `ProvenanceLabel` values, synthetic by default.
- `governance_hooks`: optional hook configuration for runtime policy, audit, privacy, review, or compliance systems.

Responsibilities:

- Carry all data required for deterministic simulation.
- Keep runtime mode and provenance explicit.
- Provide a single adapter boundary for vertical products.

### SimulationResult

Source: `socialsense_core/simulation/result.py`

`SimulationResult` is the immutable output contract from a simulation run.

Fields:

- `scenario`: scenario identifier copied from context.
- `runtime_mode`: runtime mode used.
- `event_log`: ordered `EventLog` of `SocialEvent` records.
- `recommendation_signals`: tuple of `RecommendationSignal` outputs.
- `diffusion_signals`: tuple of `DiffusionSignal` outputs.
- `opinion_signals`: tuple of `OpinionSignal` outputs.
- `trust_signals`: tuple of `TrustSignal` outputs.
- `provenance_labels`: provenance labels applied to the run.
- `summary`: structured aggregate metrics and governance notes.

Responsibilities:

- Separate raw event evidence from summarized metrics.
- Expose model outputs in typed signal families.
- Preserve provenance for downstream reports.

### RecommendationSignal

Source: `socialsense_core/recommendation/base.py`

`RecommendationSignal` describes content-ranking or discovery output.

Fields:

- `content_id`: content being recommended or ranked.
- `score`: numeric relevance/priority score.
- `reason`: explanation suitable for research reports and audit trails.

### DiffusionSignal

Source: `socialsense_core/recommendation/base.py`

`DiffusionSignal` describes spread dynamics for content.

Fields:

- `content_id`: content being propagated.
- `reach`: estimated audience exposure.
- `velocity`: estimated spread speed.
- `reason`: explanation of the heuristic or model behavior.

### OpinionSignal

Source: `socialsense_core/recommendation/base.py`

`OpinionSignal` describes actor-level opinion state changes.

Fields:

- `actor_id`: actor affected by an event or content exposure.
- `sentiment_delta`: change in affective sentiment.
- `belief_delta`: change in belief alignment.
- `intent_delta`: change in behavioral intent.
- `reason`: explanation of the update.

### TrustSignal

Source: `socialsense_core/recommendation/base.py`

`TrustSignal` describes actor-level trust or credibility changes.

Fields:

- `actor_id`: actor whose trust state changes.
- `trust_delta`: positive or negative trust adjustment.
- `reason`: explanation of source, content, or interaction effect.

### ProvenanceLabel

Source: `socialsense_core/governance/labels.py`

`ProvenanceLabel` marks where simulation data or mappings came from.

Current values:

- `SYNTHETIC`: generated test/scenario data.
- `MOCK`: mock data for demos or tests.
- `ANONYMIZED`: sanitized historical or empirical data, if future governance allows it.
- `OASIS_DERIVED_MAPPING`: derived from OASIS action/platform concepts.
- `HUMAN_AUTHORED_SCENARIO`: authored scenario input.

Responsibilities:

- Keep data lineage visible in context, events, and results.
- Support future compliance gates without forcing a specific policy into core logic.

### RuntimeMode

Source: `socialsense_core/governance/modes.py`

`RuntimeMode` describes the intended operational posture.

Current values:

- `RESEARCH`: default synthetic/offline research mode.
- `PRODUCTION`: production-aware mode where governance hooks should be attached by the caller.

Responsibilities:

- Let runners and adapters branch on operational posture.
- Signal that production runs need attached hooks, review, audit, privacy controls, and monitoring from the host application.
- Avoid embedding project-specific restrictions in reusable core modules.

## Behavior catalog

| Module | Purpose | Example actions | Signals |
| --- | --- | --- | --- |
| `public_feed` | Public timeline and engagement behavior | `post`, `comment`, `react`, `share`, `follow`, `refresh_feed` | Recommendation, Diffusion, Opinion |
| `community_group` | Group/community posting, replies, moderation | `create_group`, `join_group`, `post_topic`, `reply`, `moderate` | Diffusion, Trust |
| `private_messaging` | Direct and group messaging | `send_message`, `reply_message`, `forward_message`, `listen_group` | Diffusion, Trust |
| `short_video` | Short-form video discovery and creator interactions | `publish_video`, `watch_video`, `skip_video`, `like_video`, `follow_creator` | Recommendation, Opinion |
| `long_form_video` | Channel/subscription and long-form consumption | `publish_long_video`, `watch_long_video`, `subscribe_channel` | Recommendation, Trust |
| `influencer_network` | Creator/influencer trust and amplification | `follow_influencer`, `trust_influencer`, `amplify_content` | Trust, Diffusion |
| `recommendation_discovery` | Feed ranking, search, trends, discovery | `discover_content`, `rank_feed`, `search_topic`, `trend_topic` | RecommendationSignal |
| `information_diffusion` | Exposure, propagation, attention decay | `expose_content`, `propagate_content`, `decay_attention` | DiffusionSignal |
| `opinion_formation` | Sentiment, belief, intent transitions | `update_sentiment`, `update_belief`, `update_intent` | OpinionSignal |
| `trust_credibility` | Source trust and credibility evaluation | `evaluate_source_trust`, `update_trust_score` | TrustSignal |
| `social_commerce` | Product interest and social proof | `view_product`, `ask_for_review`, `purchase_intent`, `share_deal` | Recommendation, Opinion |
| `crisis_spread` | Alerts, rumors, official response, corrections | `crisis_alert`, `rumor_spread`, `official_response`, `correction_spread` | Diffusion, Trust |

## OASIS reuse strategy

Phase 1 reconnaissance found that OASIS is most reusable as an offline synthetic interaction engine and reference schema, not as a live platform connector. SocialSense should reuse these OASIS ideas:

- Agent/action/platform separation.
- Channel-mediated action dispatch.
- SQLite-backed event traces for reproducibility.
- Recommendation table refresh concepts.
- Twitter/X and Reddit action mappings as migration examples.
- Synthetic simulation lifecycle: build agents, reset, step, close.

SocialSense should not copy OASIS platform assumptions directly into new modules. Instead, `SocialPlatformPreset.oasis_mapping` records the mapping where useful, and behavior modules remain platform-neutral.

## Governance hooks

The core exposes governance seams but does not enforce one product's policy:

- `SimulationContext.runtime_mode` states research or production posture.
- `SimulationContext.provenance_labels` and `SocialEvent.provenance` preserve lineage.
- `SimulationContext.governance_hooks` accepts caller-owned hook configuration.
- `SocialEvent.metadata` and `SimulationResult.summary` carry audit references or hook results.
- `RuntimeMode.PRODUCTION` is a signal to attach host-application controls before execution.

Examples of hook families a production host may attach:

- data minimization and PII validation;
- scenario review/approval gates;
- model card or experiment registry references;
- human-in-the-loop review checkpoints;
- safety, privacy, compliance, and audit logging callbacks;
- rate limits and operational monitoring for non-synthetic integrations.

These hook families are intentionally configuration points, not hard-coded core restrictions.

## Deterministic runner baseline

`DeterministicSimulationRunner` validates every action against the default `ActionRegistry`, emits one `SocialEvent` per action, and computes simple heuristic signals. Its baseline summary includes actor/content counts, platform mix, action counts, governance availability, and a synthetic-simulation disclaimer.

This runner is intentionally simple so tests and architecture reviews can validate the core contracts before integrating stochastic LLM agents, external recommenders, or richer OASIS runtime adapters.

## Extension rules

When adding a new behavior, platform, vertical adapter, or signal:

1. Add or reuse a `SocialBehaviorModule`; avoid hiding behavior inside a platform preset.
2. Register normalized action verbs in `ACTION_DEFINITIONS`.
3. Add a `SocialPlatformPreset` only for platform-surface composition.
4. Keep vertical/domain assumptions in adapters, examples, or scenario files.
5. Keep provenance labels and runtime mode explicit in contexts and results.
6. Add tests that import the public `socialsense_core` API and verify registry coverage.
7. Prefer typed dataclasses for new stable contracts; use `payload` or `metadata` for experiment-specific fields.

## Acceptance coverage

This Phase 2 baseline defines the required core abstractions:

- `SocialAction`
- `SocialEvent`
- `SocialActor`
- `SocialContent`
- `SocialPlatformPreset`
- `SocialBehaviorModule`
- `SimulationContext`
- `SimulationResult`
- `RecommendationSignal`
- `DiffusionSignal`
- `OpinionSignal`
- `TrustSignal`
- `ProvenanceLabel`
- `RuntimeMode`

It also documents research-first behavior, behavior-driven platform composition, production governance hooks, and the explicit rule that reusable core modules should not contain project-specific hard-coded restrictions.
