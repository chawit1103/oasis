# OASIS Reconnaissance Report

## Scope

Repository: `https://github.com/camel-ai/oasis` cloned into `/Users/chawit/Projects/oasis-socialsense-research` on branch `feature/socialsense-core-foundation`.

SocialSense uses OASIS as a research accelerator, not a direct product dependency. This report maps concepts that can inform a reusable, platform-agnostic simulation core.

## Important files

| Area | Files |
|---|---|
| Platform runtime | `oasis/social_platform/platform.py`, `oasis/social_platform/platform_utils.py`, `oasis/social_platform/channel.py` |
| Platform typing | `oasis/social_platform/typing.py` |
| Recommendation systems | `oasis/social_platform/recsys.py`, `oasis/social_platform/process_recsys_posts.py`, `oasis/social_platform/schema/rec.sql` |
| Data model | `oasis/social_platform/schema/*.sql`, `oasis/social_platform/database.py` |
| Agents | `oasis/agents/*`, tests under `test/agent/*` |
| Graph/network examples | `visualization/dynamic_follow_network/*`, `visualization/twitter_simulation/*` |
| Reddit analysis | `visualization/reddit_simulation_*/*`, `test/infra/recsys/test_update_rec_table_reddit.py` |
| Tests/examples | `test/agent/*`, `test/infra/database/*`, `test/infra/recsys/*`, `examples/*` if present |
| License | `LICENSE`, file headers using Apache License 2.0 |

## Existing platform abstractions

OASIS has a concrete `Platform` class that owns the runtime loop, SQLite database, channel messaging, clock, recommendation refreshes, and platform actions. `DefaultPlatformType` currently identifies `twitter` and `reddit`. SocialSense should not copy this as-is because it combines platform runtime, persistence, network channel, recommendation, and behavior into one concrete service.

Reusable idea: represent platform operations as action messages and record traces/events.

OASIS-specific part: SQLite schema, Camel agent integration, embedding models, runtime channel loop, Neo4j visualizations, and platform-specific implementation details.

## Existing action types

`oasis/social_platform/typing.py` defines `ActionType` values including `refresh`, `search_user`, `search_posts`, `create_post`, `like_post`, `dislike_post`, `follow`, `trend`, `repost`, `quote_post`, `create_comment`, `purchase_product`, `join_group`, `leave_group`, `send_to_group`, `create_group`, and `listen_from_group`.

SocialSense maps these into behavior-level actions rather than copying platform names directly.

## Existing simulation lifecycle

1. Agents send `(agent_id, message, action)` through a `Channel`.
2. `Platform.running()` receives the message.
3. The string action is coerced into `ActionType`.
4. The corresponding async method is called on `Platform` via `getattr`.
5. The method updates SQLite tables and records trace rows.
6. Recommendation refreshes update rec tables.
7. Results are sent back through the channel.

SocialSense MVP keeps only the deterministic event lifecycle: action in, event log out, signals computed.

## Existing recommendation model

OASIS includes `RecsysType` values `twitter`, `twhin-bert`, `reddit`, and `random`. Twitter-style recommendation can use embeddings/TwHIN; Reddit-style ranking uses a hot-score approach; random is a baseline. These are valuable research references but carry heavyweight dependencies (`torch`, `sentence-transformers`, model downloads) that are not appropriate for the SocialSense Core MVP.

SocialSense MVP implements deterministic lightweight heuristics for recommendation, diffusion, opinion, and trust. Advanced OASIS-like recommenders can be added later as optional plugins.

## Twitter/X mapping

| OASIS concept | SocialSense behavior | SocialSense action |
|---|---|---|
| `CREATE_POST` | Public Feed | `post` |
| `CREATE_COMMENT` | Public Feed | `comment` |
| `LIKE_POST` | Public Feed / Opinion Formation | `react` |
| `REPOST`, `QUOTE_POST` | Information Diffusion | `share` |
| `FOLLOW` | Public Feed / Influencer Network | `follow` |
| `SEARCH_POSTS` | Recommendation / Discovery | `search_topic` |
| `TREND` | Recommendation / Discovery | `trend_topic` |
| `REFRESH` | Public Feed / Recommendation | `refresh_feed` |

## Reddit mapping

| OASIS concept | SocialSense behavior | SocialSense action |
|---|---|---|
| `CREATE_POST` | Community Group | `post_topic` |
| `CREATE_COMMENT` | Community Group | `reply` |
| `LIKE_POST`/`DISLIKE_POST` | Trust / Credibility + Community Group | `react` with polarity metadata |
| `SEARCH_POSTS` | Recommendation / Discovery | `search_topic` |
| `TREND` | Information Diffusion | `trend_topic` |
| `JOIN_GROUP`/community membership | Community Group | `join_group` |
| Moderation/report flows | Community Group | `moderate` |

## Extension points

- Action registry: add actions independent of platforms.
- Behavior module registry: add reusable behavior families.
- Platform preset registry: map platforms to behavior modules and actions.
- Simulation runner: swap deterministic runner for richer agent-based runner.
- Recommendation heuristics: replace with learned/graph/embedding recommenders.
- Governance hooks: downstream applications can enforce production policies.
- Adapters: applications such as CivicSense and 3C can translate domain scenarios into SocialSense contexts.

## Reuse strategy

Reuse concepts, not runtime dependencies:

1. Preserve Apache-2.0 notices where OASIS code is referenced or derived.
2. Keep SocialSense Core platform-agnostic and behavior-driven.
3. Treat Twitter/X and Reddit as presets over generic behavior modules.
4. Avoid importing OASIS runtime code in the core MVP.
5. Keep synthetic tests/examples and deterministic outputs.

## Risks

| Risk | Mitigation |
|---|---|
| OASIS dependencies target Python `<3.12`; local host has Python 3.14 | SocialSense Core uses stdlib-only dataclasses for MVP tests. |
| Heavy recommendation dependencies and model downloads | Keep as future optional plugins, not core. |
| Platform-specific assumptions leaking into core | Registries and behavior modules are platform-agnostic. |
| CivicSense policy restrictions hard-coded too early | Core exposes governance hooks only; downstream apps own policy boundaries. |
| Misuse of research simulations as real platform claims | Provenance labels and simulation disclaimers in results/docs/examples. |
| Live platform/API temptation | No API credentials, scraping, or real platform calls in MVP. |

## Recommended implementation plan

1. Add SocialSense Core package with typed entities and registries.
2. Implement deterministic simulation runner and event log.
3. Add behavior modules for public feed, groups, messaging, video, influencer, recommendation, diffusion, opinion, trust, commerce, and crisis spread.
4. Add platform presets for X/Twitter, Reddit, LINE, Facebook, TikTok, and YouTube.
5. Add adapter interfaces for CivicSense and 3C Marketing Simulator.
6. Add synthetic examples and tests.
7. Document research/production mode boundary and future roadmap.
