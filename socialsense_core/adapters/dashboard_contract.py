from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any, Mapping

from socialsense_core.simulation.result import SimulationResult


def _platform_breakdown(result: SimulationResult) -> dict[str, dict[str, Any]]:
    breakdown: dict[str, dict[str, Any]] = defaultdict(lambda: {"events": 0, "actions": Counter()})
    for event in result.event_log:
        platform = event.metadata.get("platform") or event.action.platform or "mixed"
        bucket = breakdown[str(platform)]
        bucket["events"] += 1
        bucket["actions"][event.action.action_type] += 1
    return {
        platform: {"events": data["events"], "actions": dict(sorted(data["actions"].items()))}
        for platform, data in sorted(breakdown.items())
    }


def _sentiment_signal(result: SimulationResult) -> dict[str, Any]:
    net_sentiment = float(round(sum(signal.sentiment_delta for signal in result.opinion_signals), 4))
    net_belief = float(round(sum(signal.belief_delta for signal in result.opinion_signals), 4))
    net_intent = float(round(sum(signal.intent_delta for signal in result.opinion_signals), 4))
    direction = "positive" if net_sentiment > 0 else "negative" if net_sentiment < 0 else "neutral"
    return {
        "net_sentiment_delta": net_sentiment,
        "net_belief_delta": net_belief,
        "net_intent_delta": net_intent,
        "direction": direction,
        "signals": [signal.__dict__.copy() for signal in result.opinion_signals],
    }


def _diffusion_signal(result: SimulationResult) -> dict[str, Any]:
    total_reach = float(round(sum(signal.reach for signal in result.diffusion_signals), 4))
    max_velocity = float(round(max((signal.velocity for signal in result.diffusion_signals), default=0.0), 4))
    return {
        "total_reach": total_reach,
        "max_velocity": max_velocity,
        "signals": [signal.__dict__.copy() for signal in result.diffusion_signals],
    }


def _trust_signal(result: SimulationResult) -> dict[str, Any]:
    net_trust = float(round(sum(signal.trust_delta for signal in result.trust_signals), 4))
    direction = "improving" if net_trust > 0 else "declining" if net_trust < 0 else "neutral"
    return {
        "net_trust_delta": net_trust,
        "direction": direction,
        "signals": [signal.__dict__.copy() for signal in result.trust_signals],
    }


def _risk_signal(result: SimulationResult, action_counts: Mapping[str, int]) -> dict[str, Any]:
    rumor_events = int(action_counts.get("rumor_spread", 0))
    crisis_events = int(action_counts.get("crisis_alert", 0))
    correction_events = int(action_counts.get("correction_spread", 0) + action_counts.get("official_response", 0))
    negative_attention = int(action_counts.get("decay_attention", 0) + action_counts.get("skip_video", 0))
    risk_score = max(0, rumor_events * 3 + crisis_events * 2 + negative_attention - correction_events)
    level = "high" if risk_score >= 4 else "medium" if risk_score >= 2 else "low"
    return {
        "level": level,
        "score": risk_score,
        "rumor_events": rumor_events,
        "crisis_events": crisis_events,
        "correction_events": correction_events,
        "negative_attention_events": negative_attention,
    }


def _recommended_next_observations(contract: Mapping[str, Any]) -> list[str]:
    observations = [
        "Track platform-level action counts against the synthetic scenario assumptions.",
        "Compare sentiment, diffusion, and trust deltas before using results in executive dashboards.",
    ]
    risk = contract["risk_signal"]
    if risk["rumor_events"] or risk["crisis_events"]:
        observations.append("Monitor rumor/crisis propagation and compare correction response timing in the next simulation pass.")
    if contract["summary"].get("consumer") == "3C Marketing Simulator":
        observations.append("Segment purchase-intent and engagement signals by platform before ROI interpretation.")
    return observations


def to_dashboard_contract(result: SimulationResult, *, scenario_key: str, consumer: str) -> dict[str, Any]:
    """Convert a SimulationResult into a stable dashboard-facing contract."""
    action_counts = dict(result.summary.get("action_counts", {}))
    summary = {
        "dashboard_contract_version": "socialsense-dashboard-v1",
        "scenario_key": scenario_key,
        "consumer": consumer,
        "scenario": result.scenario,
        "platform_preset": result.summary.get("platform_preset", "unknown"),
        "platform_mix": list(result.summary.get("platform_mix", ())),
        "event_count": len(result.event_log),
        "action_counts": action_counts,
        "simulation_disclaimer": result.summary.get("simulation_disclaimer", "Synthetic deterministic simulation; no live platform access or real PII."),
    }
    contract: dict[str, Any] = {
        "summary": summary,
        "platform_breakdown": _platform_breakdown(result),
        "sentiment_signal": _sentiment_signal(result),
        "diffusion_signal": _diffusion_signal(result),
        "trust_signal": _trust_signal(result),
        "risk_signal": _risk_signal(result, action_counts),
        "recommended_next_observations": [],
        "provenance_labels": [label.value for label in result.provenance_labels],
        "runtime_mode": result.runtime_mode.value,
    }
    contract["recommended_next_observations"] = _recommended_next_observations(contract)
    return contract
