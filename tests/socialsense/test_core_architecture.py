from dataclasses import is_dataclass
from enum import Enum

import socialsense_core as core
from socialsense_core.actions.registry import build_default_action_registry
from socialsense_core.behaviors.registry import get_default_behavior_registry
from socialsense_core.platforms.registry import get_default_platform_registry


def test_required_core_abstractions_are_public() -> None:
    required_dataclasses = (
        core.SocialAction,
        core.SocialEvent,
        core.SocialActor,
        core.SocialContent,
        core.SocialPlatformPreset,
        core.SocialBehaviorModule,
        core.SimulationContext,
        core.SimulationResult,
        core.RecommendationSignal,
        core.DiffusionSignal,
        core.OpinionSignal,
        core.TrustSignal,
    )

    for abstraction in required_dataclasses:
        assert is_dataclass(abstraction), abstraction

    assert issubclass(core.ProvenanceLabel, Enum)
    assert issubclass(core.RuntimeMode, Enum)


def test_behavior_modules_and_platform_presets_are_data_driven() -> None:
    behavior_registry = get_default_behavior_registry()
    platform_registry = get_default_platform_registry()
    action_registry = build_default_action_registry()

    assert set(behavior_registry.keys()) == {
        "community_group",
        "crisis_spread",
        "information_diffusion",
        "influencer_network",
        "long_form_video",
        "opinion_formation",
        "private_messaging",
        "public_feed",
        "recommendation",
        "social_commerce",
        "short_video",
        "trust_credibility",
    }
    assert {
        "facebook",
        "line",
        "reddit",
        "tiktok",
        "x_twitter",
        "youtube",
    }.issubset(set(platform_registry.keys()))

    available_actions = set(action_registry.all_actions())
    for module in behavior_registry.all():
        assert module.actions
        assert set(module.actions).issubset(available_actions)

    available_modules = set(behavior_registry.keys())
    for preset in platform_registry.all():
        assert preset.actions
        assert isinstance(preset.context_notes, tuple)
        assert set(preset.behavior_modules).issubset(available_modules)


def test_simulation_context_result_signals_and_governance_hooks() -> None:
    actor = core.SocialActor(actor_id="actor-1", display_name="Research actor")
    content = core.SocialContent(content_id="content-1", text="Synthetic content", author_id="actor-1")
    post_action = core.SocialAction(
        action_type="post",
        actor_id="actor-1",
        content_id="content-1",
        platform="x_twitter",
        payload={"synthetic": True},
    )
    react_action = core.SocialAction(
        action_type="react",
        actor_id="actor-1",
        content_id="content-1",
        platform="x_twitter",
    )
    trust_action = core.SocialAction(
        action_type="evaluate_source_trust",
        actor_id="actor-1",
        target_id="source-1",
        platform="youtube",
    )
    context = core.SimulationContext.build(
        scenario="architecture contract smoke test",
        actors=[actor],
        content=[content],
        platform_mix=["x_twitter"],
        actions=[post_action, react_action, trust_action],
        runtime_mode="production",
        provenance_labels=(core.ProvenanceLabel.SYNTHETIC, core.ProvenanceLabel.HUMAN_AUTHORED_SCENARIO),
        governance_hooks={"audit": "enabled-by-host"},
    )

    result = core.run_simulation(context)

    assert context.runtime_mode is core.RuntimeMode.PRODUCTION
    assert result.runtime_mode is core.RuntimeMode.PRODUCTION
    assert result.provenance_labels == context.provenance_labels
    assert result.event_log.to_summary() == {"evaluate_source_trust": 1, "post": 1, "react": 1}
    assert result.summary["governance_hooks_available"] is True
    assert result.summary["simulation_disclaimer"] == "Synthetic deterministic simulation; no live platform access or real PII."
    assert result.recommendation_signals[0].content_id == "content-1"
    assert result.diffusion_signals[0].content_id == "content-1"
    assert result.opinion_signals[0].actor_id == "actor-1"
    assert result.trust_signals[0].actor_id == "actor-1"
