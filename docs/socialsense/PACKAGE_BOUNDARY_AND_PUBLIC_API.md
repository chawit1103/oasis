# Package Boundary and Public API

Status: SocialSense Core `0.1.0` public integration boundary.

External projects such as CivicSense and 3C Simulator should import from `socialsense_core` only. Internal modules remain available for SocialSense development, but downstream consumers should not couple to them.

## Stable import surface

```python
import socialsense_core as ssc

print(ssc.__version__)
contract = ssc.run_scenario_pack("civic_policy_message")
```

The public API is the set of names exported by `socialsense_core.__all__`, including:

- version constants: `__version__`, `version`
- core models: `SocialAction`, `SocialEvent`, `SocialActor`, `SocialContent`, `SimulationContext`, `SimulationResult`
- signal models: `RecommendationSignal`, `DiffusionSignal`, `OpinionSignal`, `TrustSignal`
- governance enums: `ProvenanceLabel`, `RuntimeMode`
- registries/builders: `ActionRegistry`, `BehaviorRegistry`, `BehaviorModuleRegistry`, `PlatformPresetRegistry`, `build_default_action_registry`, `get_default_behavior_registry`, `get_default_platform_registry`
- execution helpers: `DeterministicSimulationRunner`, `run_simulation`
- scenario/dashboard helpers: `ScenarioPack`, `list_scenario_packs`, `get_scenario_pack`, `run_scenario_pack`, `to_dashboard_contract`

## Boundary rule for downstream apps

CivicSense and 3C integration code should avoid imports such as:

```python
from socialsense_core.adapters.civicsense_adapter import ...
from socialsense_core.platforms.thailand import ...
from socialsense_core.simulation.runner import ...
```

Prefer:

```python
import socialsense_core as ssc
```

## Compatibility promise

For the `0.1.x` line, SocialSense Core will try to keep public names in `__all__` source-compatible. Internals can still move.

## Non-goals

- This PR does not publish a Python package.
- This PR does not modify CivicSense or 3C repositories.
- This PR does not add external services, credentials, scraping, or live platform APIs.
