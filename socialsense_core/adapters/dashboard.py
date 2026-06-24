from dataclasses import asdict, replace
from typing import Any, Mapping, Sequence

from socialsense_core.platforms.registry import get_default_platform_registry
from socialsense_core.simulation.result import SimulationResult


def resolve_platform_mix(platform_mix: str | Sequence[str] | None, default_preset: str) -> tuple[str, list[str]]:
    """Resolve a platform preset key or explicit platform list into dashboard metadata."""
    registry = get_default_platform_registry()
    preset_key = default_preset
    raw_mix = platform_mix or default_preset

    if isinstance(raw_mix, str):
        preset = registry.get(raw_mix)
        preset_key = preset.key
        mapped = preset.oasis_mapping.get("platform_mix", raw_mix)
        return preset_key, [item for item in mapped.split(",") if item]

    return "custom_platform_mix", list(raw_mix)


def platform_for(platform_mix: Sequence[str], preferred: str) -> str | None:
    """Return a platform from the caller-requested mix, preferring the rich preset mapping."""
    if preferred in platform_mix:
        return preferred
    if platform_mix:
        return platform_mix[0]
    return None


def with_dashboard_summary(
    result: SimulationResult,
    *,
    consumer: str,
    scenario_family: str,
    platform_preset: str,
    input_metadata: Mapping[str, Any],
) -> SimulationResult:
    actions_by_step = [
        {
            "step": index,
            "event_id": event.event_id,
            "action": event.action.action_type,
            "platform": event.metadata.get("platform") or event.action.platform,
            "content_id": event.action.content_id,
        }
        for index, event in enumerate(result.event_log, start=1)
    ]
    action_counts = dict(result.summary.get("action_counts", {}))
    headline_metrics = {
        "events": len(actions_by_step),
        "actors": result.summary.get("actor_count", 0),
        "content_items": result.summary.get("content_count", 0),
        "platforms": len(result.summary.get("platform_mix", ())),
        "engagement_events": sum(action_counts.get(action, 0) for action in ("react", "share", "comment", "like_video", "share_video")),
        "sentiment_events": action_counts.get("update_sentiment", 0) + action_counts.get("update_belief", 0) + action_counts.get("update_intent", 0),
        "purchase_intent_events": action_counts.get("purchase_intent", 0),
        "crisis_response_events": action_counts.get("official_response", 0) + action_counts.get("correction_spread", 0),
    }
    dashboard_summary = dict(result.summary)
    dashboard_summary.update(
        {
            "dashboard_version": "socialsense-core-v1",
            "scenario_family": scenario_family,
            "platform_preset": platform_preset,
            "headline_metrics": headline_metrics,
            "series": {"actions_by_step": actions_by_step, "action_counts": action_counts},
            "signals": {
                "recommendation": [asdict(signal) for signal in result.recommendation_signals],
                "diffusion": [asdict(signal) for signal in result.diffusion_signals],
                "opinion": [asdict(signal) for signal in result.opinion_signals],
                "trust": [asdict(signal) for signal in result.trust_signals],
            },
            "integration_contract": {
                "consumer": consumer,
                "format": "dashboard_summary",
                "schema_version": "1.0",
                "external_services": "none",
                "pii_policy": "synthetic-only",
            },
            "input_metadata": dict(input_metadata),
        }
    )
    return replace(result, summary=dashboard_summary)
