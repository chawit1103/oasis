from datetime import datetime, timezone

from socialsense_core.actions.registry import build_default_action_registry
from socialsense_core.events.event_log import EventLog
from socialsense_core.events.types import SocialEvent
from socialsense_core.governance.modes import RuntimeMode
from socialsense_core.recommendation.heuristics import diffusion_heuristic, opinion_update_heuristic, recommendation_heuristic, trust_heuristic
from .context import SimulationContext
from .result import SimulationResult


class DeterministicSimulationRunner:
    def __init__(self) -> None:
        self.action_registry = build_default_action_registry()

    def run(self, context: SimulationContext) -> SimulationResult:
        unknown = [a.action_type for a in context.actions if not self.action_registry.has(a.action_type)]
        if unknown:
            raise ValueError(f"Unsupported action types: {unknown}")
        event_log = EventLog()
        for idx, action in enumerate(context.actions):
            event_log.append(SocialEvent(
                event_id=f"evt-{idx + 1:04d}",
                action=action,
                timestamp=datetime.fromtimestamp(idx, timezone.utc),
                provenance=context.provenance_labels,
                metadata={"runtime_mode": context.runtime_mode.value, "platform": action.platform or "mixed"},
            ))
        recommendations = tuple(recommendation_heuristic(list(context.actions)))
        diffusion = tuple(diffusion_heuristic(list(context.actions)))
        opinion = tuple(opinion_update_heuristic(list(context.actions)))
        trust = tuple(trust_heuristic(list(context.actions)))
        summary = {
            "actor_count": len(context.actors),
            "content_count": len(context.content),
            "platform_mix": list(context.platform_mix),
            "action_counts": event_log.to_summary(),
            "governance_hooks_available": bool(context.governance_hooks) or context.runtime_mode == RuntimeMode.PRODUCTION,
            "simulation_disclaimer": "Synthetic deterministic simulation; no live platform access or real PII.",
        }
        return SimulationResult(context.scenario, context.runtime_mode, event_log, recommendations, diffusion, opinion, trust, context.provenance_labels, summary)


def run_simulation(context: SimulationContext) -> SimulationResult:
    return DeterministicSimulationRunner().run(context)
