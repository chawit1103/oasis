"""Stable public API for SocialSense Core external consumers.

CivicSense, 3C Simulator, and future downstream projects should import from this
module instead of reaching into internal package paths. Anything listed in
``__all__`` is part of the v0.1 public integration surface.
"""

from socialsense_core.actions.registry import ActionRegistry, build_default_action_registry
from socialsense_core.actions.types import SocialAction
from socialsense_core.adapters.dashboard_contract import to_dashboard_contract
from socialsense_core.behaviors.registry import BehaviorModuleRegistry, get_default_behavior_registry
from socialsense_core.behaviors.types import SocialBehaviorModule
from socialsense_core.events.event_log import EventLog
from socialsense_core.events.types import SocialEvent
from socialsense_core.governance.labels import ProvenanceLabel
from socialsense_core.governance.modes import RuntimeMode
from socialsense_core.personas.types import SocialActor, SocialContent
from socialsense_core.platforms.base import SocialPlatformPreset
from socialsense_core.platforms.registry import PlatformPresetRegistry, get_default_platform_registry
from socialsense_core.recommendation.base import DiffusionSignal, OpinionSignal, RecommendationSignal, TrustSignal
from socialsense_core.scenario_packs import ScenarioPack, get_scenario_pack, list_scenario_packs, run_scenario_pack
from socialsense_core.simulation.context import SimulationContext
from socialsense_core.simulation.result import SimulationResult
from socialsense_core.simulation.runner import DeterministicSimulationRunner, run_simulation

__version__ = "0.1.0"
version = __version__
BehaviorRegistry = BehaviorModuleRegistry

__all__ = [
    "__version__",
    "version",
    "ActionRegistry",
    "BehaviorRegistry",
    "BehaviorModuleRegistry",
    "PlatformPresetRegistry",
    "SocialAction",
    "SocialEvent",
    "EventLog",
    "SocialActor",
    "SocialContent",
    "SocialPlatformPreset",
    "SocialBehaviorModule",
    "SimulationContext",
    "SimulationResult",
    "RecommendationSignal",
    "DiffusionSignal",
    "OpinionSignal",
    "TrustSignal",
    "ProvenanceLabel",
    "RuntimeMode",
    "DeterministicSimulationRunner",
    "run_simulation",
    "ScenarioPack",
    "get_scenario_pack",
    "list_scenario_packs",
    "run_scenario_pack",
    "to_dashboard_contract",
    "get_default_platform_registry",
    "get_default_behavior_registry",
    "build_default_action_registry",
]
