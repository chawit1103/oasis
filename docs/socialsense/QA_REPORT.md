# SocialSense Core Foundation QA Report

Date: 2026-06-24
Branch: feature/socialsense-core-foundation
Working directory: /Users/chawit/Projects/oasis-socialsense-research
Scope: Validate SocialSense Core tests and runnable examples only. No real platform APIs, credentials, scraping, or network were used.

## Verdict

PASS for the SocialSense Core Foundation acceptance criteria covering focused tests and runnable example smoke tests.

The focused SocialSense test suite passed, and every SocialSense example demo executed successfully using synthetic/deterministic local data. The broader upstream OASIS test suite is not currently feasible in this environment without installing heavyweight/missing dependencies and possibly provisioning runtime services/API model backends; see limitations.

## Acceptance Criteria Checked

- `python3 -m pytest tests/socialsense -q` passes.
- SocialSense example demos are runnable as local smoke tests.
- Examples use synthetic/mock data and do not call real platform APIs, credentials, scraping, or network.
- Existing OASIS test feasibility is documented separately from SocialSense Core validation.
- QA changes are limited to this report file: `docs/socialsense/QA_REPORT.md`.

## Environment

Command:

```bash
python3 --version && python3 -m pytest --version
```

Result:

```text
Python 3.14.3
pytest 9.0.3
```

Git branch command:

```bash
git branch --show-current
```

Result:

```text
feature/socialsense-core-foundation
```

## Focused SocialSense Tests

Command:

```bash
python3 -m pytest tests/socialsense -q
```

Result:

```text
...............                                                          [100%]
15 passed in 0.02s
```

Status: PASS

Coverage observed from the test files under `tests/socialsense`:

- Action registry
- Behavior modules
- Platform presets
- Deterministic simulation runner
- Event log
- Runtime modes
- Diffusion heuristics
- Recommendation heuristics
- Opinion update
- CivicSense adapter
- 3C adapter
- Example module importability
- Public core architecture/export contract

## Runnable Example Smoke Tests

Command:

```bash
for f in examples/socialsense_*_demo.py; do echo "===== $f ====="; python3 "$f"; done
```

Result summary:

```text
===== examples/socialsense_3c_adapter_demo.py =====
input scenario: campaign response: mock consumer product
platform mix: ['facebook', 'tiktok', 'youtube']
actions simulated: ['post', 'discover_content', 'react', 'purchase_intent']
event log: ['evt-0001', 'evt-0002', 'evt-0003', 'evt-0004']
result summary: {'actor_count': 1, 'content_count': 1, 'platform_mix': ['facebook', 'tiktok', 'youtube'], 'action_counts': {'post': 1, 'discover_content': 1, 'react': 1, 'purchase_intent': 1}, 'governance_hooks_available': True, 'simulation_disclaimer': 'Synthetic deterministic simulation; no live platform access or real PII.'}
provenance labels: ['synthetic', 'human_authored_scenario']
runtime mode: research

===== examples/socialsense_civicsense_adapter_demo.py =====
input scenario: public opinion: demo only; no live platform data
platform mix: ['line', 'facebook', 'tiktok']
actions simulated: ['post', 'react', 'share', 'update_sentiment']
event log: ['evt-0001', 'evt-0002', 'evt-0003', 'evt-0004']
result summary: {'actor_count': 1, 'content_count': 1, 'platform_mix': ['line', 'facebook', 'tiktok'], 'action_counts': {'post': 1, 'react': 1, 'share': 1, 'update_sentiment': 1}, 'governance_hooks_available': True, 'simulation_disclaimer': 'Synthetic deterministic simulation; no live platform access or real PII.'}
provenance labels: ['synthetic', 'human_authored_scenario']
runtime mode: research

===== examples/socialsense_facebook_group_demo.py =====
input scenario: Facebook group discussion with marketplace-adjacent sharing
platform mix: ['facebook']
actions simulated: ['post_topic', 'comment', 'react', 'share', 'view_product']
event count: 5
runtime mode: research

===== examples/socialsense_line_group_demo.py =====
input scenario: LINE family/workplace group forwards a public-health update
platform mix: ['line']
actions simulated: ['create_chat_group', 'send_message', 'forward_message', 'listen_group', 'correction_spread']
event count: 5
runtime mode: research

===== examples/socialsense_thai_platform_mix_demo.py =====
input scenario: Thai platform mix: LINE, Facebook, TikTok, YouTube
platform mix: ['line', 'facebook', 'tiktok', 'youtube']
actions simulated: ['send_message', 'post', 'watch_video', 'share_video', 'watch_long_video', 'update_sentiment']
event count: 6
runtime mode: research

===== examples/socialsense_tiktok_short_video_demo.py =====
input scenario: TikTok short-video discovery and creator affinity
platform mix: ['tiktok']
actions simulated: ['publish_video', 'watch_video', 'like_video', 'share_video', 'purchase_intent']
event count: 5
runtime mode: research

===== examples/socialsense_youtube_video_demo.py =====
input scenario: YouTube long-form explanation plus trust evaluation
platform mix: ['youtube']
actions simulated: ['publish_long_video', 'watch_long_video', 'subscribe_channel', 'comment_video', 'evaluate_source_trust']
event count: 5
runtime mode: research
```

Status: PASS

Notes:

- All seven SocialSense demos completed with exit code 0.
- Outputs consistently include synthetic/mock provenance or deterministic simulation disclaimers.
- The smoke tests covered adapter demos for 3C and CivicSense plus LINE, Facebook, TikTok, YouTube, and Thai mixed-platform examples.

## No Real API / Network / Scraping Check

Inspected SocialSense example files for direct network/API/scraping indicators using a focused content search over `examples/socialsense_*_demo.py`.

Command:

```bash
# Implemented with repository search over examples/socialsense_*_demo.py for:
# requests|http|api|credential|token|scrap|network|urllib|aiohttp|OpenAI|platform
```

Result:

- Matches were local scenario/platform strings and synthetic demo content only.
- No imports or calls to `requests`, `urllib`, `aiohttp`, OpenAI clients, platform APIs, credentials, tokens, scraping, or network access were found in the SocialSense demo files.

Status: PASS

## Existing OASIS Tests Feasibility

A broad repository test command was attempted only to assess feasibility of the existing upstream OASIS suite; it is not part of the SocialSense Core acceptance gate.

Command:

```bash
python3 -m pytest -q
```

Result:

```text
ERROR test/agent/test_action_docstring.py - ModuleNotFoundError: No module named 'camel'
ERROR test/agent/test_agent_custom_prompt.py - ModuleNotFoundError: No module named 'camel'
ERROR test/agent/test_agent_generator.py - ModuleNotFoundError: No module named 'camel'
ERROR test/agent/test_agent_graph.py - ModuleNotFoundError: No module named 'torch'
ERROR test/agent/test_agent_tools.py - ModuleNotFoundError: No module named 'camel'
ERROR test/agent/test_interview_action.py - ModuleNotFoundError: No module named 'camel'
ERROR test/agent/test_multi_agent_signup_create.py - ModuleNotFoundError: No module named 'camel'
ERROR test/agent/test_twitter_user_agent_all_actions.py - ModuleNotFoundError: No module named 'camel'
ERROR multiple test/infra/database/* modules - ModuleNotFoundError: No module named 'camel'
ERROR multiple test/infra/recsys/* modules - ModuleNotFoundError: No module named 'camel'
Interrupted: 28 errors during collection
28 errors in 0.54s
```

Status: NOT FEASIBLE in the current local QA environment.

Reason:

- The upstream OASIS tests require dependencies that are not installed in this environment, especially `camel` and `torch`.
- Several upstream OASIS examples/docs also reference external LLM/API/server setup patterns. Running those would violate this QA scope unless separately provisioned with approved local/offline substitutes.
- I did not install dependencies, use credentials, call live APIs, scrape platforms, or make network calls.

Impact on SocialSense verdict:

- This does not block SocialSense Core Foundation acceptance because the requested focused suite `tests/socialsense` passes and the SocialSense demos run locally without external services.

## Limitations

- QA did not validate performance, packaging, or installation from a clean virtual environment.
- QA did not run real OASIS simulations, live social-platform integrations, LLM-backed simulations, or networked services.
- QA did not use real user/platform data or credentials.
- The repository currently shows many SocialSense files as untracked on this branch; this report validates the working tree as provided.

## Final Recommendation

Accept the SocialSense Core Foundation test/example criteria for this branch, with the explicit caveat that upstream OASIS full-suite validation should be handled as a separate environment task with declared dependencies, offline-safe configuration, and no live platform/API calls unless explicitly approved.
