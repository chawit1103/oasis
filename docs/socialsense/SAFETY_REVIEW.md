# SocialSense Core Foundation Safety Review

Verdict: APPROVED

Review scope: current branch `feature/socialsense-core-foundation` in `/Users/chawit/Projects/oasis-socialsense-research`, focused on the SocialSense Core Foundation files under `socialsense_core/`, `tests/socialsense/`, `examples/socialsense_*_demo.py`, and `docs/socialsense/`.

## Acceptance criteria reviewed

- Research Mode labeling is explicit.
- Production Mode hooks exist without implying production enforcement in the reusable core.
- Examples are synthetic/mock and do not require real users or real PII.
- SocialSense Core does not require live platform access.
- No hidden external calls are present in the inspected SocialSense Core/Foundation scope.
- Provenance labels are present in core result/event structures and examples.
- Simulation disclaimers are surfaced in results/docs/examples.

## Evidence

### Branch and working tree

- Current branch: `feature/socialsense-core-foundation`.
- SocialSense Core Foundation files are currently untracked in this working tree, so this review is based on direct inspection and execution rather than a tracked diff.

### Research Mode labeling

- `socialsense_core/governance/modes.py` defines:
  - `RuntimeMode.RESEARCH = "research"`
  - `RuntimeMode.PRODUCTION = "production"`
  - `normalize_runtime_mode(...)`
- `socialsense_core/simulation/context.py` defaults `SimulationContext.runtime_mode` to `RuntimeMode.RESEARCH`.
- `docs/socialsense/RESEARCH_MODE_AND_PRODUCTION_MODE.md` describes Research Mode as synthetic simulation and research exploration.
- Demo execution showed `runtime mode: research` for SocialSense examples.

### Production Mode hooks

- `SimulationContext` exposes `governance_hooks: Mapping[str, Any]`.
- `socialsense_core/simulation/runner.py` reports `governance_hooks_available` in result summaries.
- `tests/socialsense/test_runtime_modes.py` verifies production mode is accepted and governance hook availability is true when hooks are supplied.
- Production Mode is appropriately documented as a runtime marker and hook surface; downstream applications own enforcement.

### Synthetic examples and no real PII required

- SocialSense examples use synthetic actors/content such as `Synthetic Thai participant`, `Synthetic audience`, and synthetic messages.
- `docs/socialsense/RESEARCH_MODE_AND_PRODUCTION_MODE.md` states: "All examples and tests use synthetic/mock data. No real PII, platform credentials, live scraping, or hidden external calls are required."
- `socialsense_core/simulation/runner.py` emits the disclaimer: `Synthetic deterministic simulation; no live platform access or real PII.`
- Executed examples printed that disclaimer in result summaries.

### No live platform access / no hidden external calls in SocialSense Foundation

Targeted inspection of `socialsense_core/` found no matches for network/client/secret patterns including:

- `requests`, `httpx`, `aiohttp`, `urllib`, `socket`
- `selenium`, `playwright`, `scrap`, `crawl`
- `os.environ`, `getenv`
- `api_key`, `secret`, `token`, `password`
- `openai`, `anthropic`, `deepseek`
- `http://` / `https://`

Targeted inspection of `examples/socialsense_*_demo.py` found no matches for the same classes of live network, browser automation, scraping, credential, or external model/API usage.

Important scope note: the inherited upstream OASIS repository includes older non-SocialSense examples and docs that reference OpenAI, DeepSeek, tokens, and API/server URLs. Those were not introduced by, imported by, or required for the SocialSense Core Foundation files reviewed here. They remain a repository-level safety consideration but are out of scope for this Foundation verdict.

### Provenance labels

- `socialsense_core/governance/labels.py` defines provenance labels:
  - `synthetic`
  - `mock`
  - `anonymized`
  - `oasis_derived_mapping`
  - `human_authored_scenario`
- `SimulationContext` carries `provenance_labels`, defaulting to `synthetic`.
- `DeterministicSimulationRunner` copies provenance labels into every `SocialEvent` and into `SimulationResult`.
- Demo execution printed provenance labels such as `['synthetic', 'mock']` and `['synthetic', 'human_authored_scenario']`.

### Simulation disclaimers

- `DeterministicSimulationRunner` includes `simulation_disclaimer` in result summaries.
- `tests/socialsense/test_core_architecture.py` asserts the exact disclaimer: `Synthetic deterministic simulation; no live platform access or real PII.`
- `docs/socialsense/RESEARCH_MODE_AND_PRODUCTION_MODE.md` includes a Disclaimers section.
- Example runs printed the disclaimer in result summaries.

## Commands executed

```text
git status --short && git branch --show-current && git diff --stat
python3 -m pytest tests/socialsense -q
python3 examples/socialsense_thai_platform_mix_demo.py && python3 examples/socialsense_civicsense_adapter_demo.py
```

Observed test result:

```text
15 passed in 0.03s
```

Observed example evidence included:

```text
result summary: {... 'simulation_disclaimer': 'Synthetic deterministic simulation; no live platform access or real PII.'}
provenance labels: ['synthetic', 'mock']
runtime mode: research
```

and:

```text
result summary: {... 'governance_hooks_available': True, 'simulation_disclaimer': 'Synthetic deterministic simulation; no live platform access or real PII.'}
provenance labels: ['synthetic', 'human_authored_scenario']
runtime mode: research
```

## Risks

1. Production Mode is currently a marker and hook surface only. It does not enforce downstream policy, export restrictions, PII checks, or platform-specific safety rules inside the reusable core.
2. The foundation accepts free-form scenario/message strings from callers. Downstream applications must prevent real PII ingestion if they expose this to users or imported datasets.
3. Platform presets use names of real platforms such as LINE, Facebook, TikTok, YouTube, X/Twitter, and Reddit. The current implementation treats them as simulation presets only, but UI/docs should keep showing disclaimers so users do not mistake outputs for live platform claims.
4. The broader inherited OASIS repository contains non-SocialSense examples with external model/API references. They should remain separated from SocialSense Foundation quickstarts and CI paths unless explicitly reviewed.
5. The deterministic runner is intentionally lightweight. Its outputs should be labeled as synthetic heuristic simulations, not empirical predictions or measured social-platform behavior.

## Limitations

- Review was limited to SocialSense Foundation scope, not a full audit of the entire inherited OASIS repository.
- No external network monitoring or sandbox packet capture was performed; evidence is from static inspection and local execution of SocialSense tests/examples.
- No production deployment path, UI rendering path, PDF export path, or downstream CivicSense/3C enforcement layer was reviewed.
- Because the SocialSense Foundation files are untracked, future diffs should be reviewed again once staged or committed.

## Final verdict

APPROVED for the SocialSense Core Foundation milestone.

The reviewed SocialSense Foundation satisfies the requested safety criteria for Research Mode labeling, Production Mode hooks, synthetic examples, no real PII requirement, no live platform access requirement, no hidden external calls in the SocialSense scope, provenance labels, and simulation disclaimers. Downstream applications must still enforce production policy boundaries and PII controls before any real-world deployment.
