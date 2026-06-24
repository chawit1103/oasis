from socialsense_core import RuntimeMode, SocialAction, SocialActor, SocialContent
from socialsense_core.actions.registry import get_default_action_registry
from socialsense_core.behaviors.registry import get_default_behavior_registry
from socialsense_core.recommendation.heuristics import diffusion_heuristic, recommendation_heuristic, trust_heuristic
from socialsense_core.simulation.context import SimulationContext
from socialsense_core.simulation.runner import run_simulation


def test_recommendation_actions_resolve_by_behavior_key():
    registry = get_default_action_registry()

    assert registry.actions_for("recommendation") == (
        "discover_content",
        "rank_feed",
        "search_topic",
        "trend_topic",
    )


def test_production_mode_does_not_imply_governance_hooks_available():
    context = SimulationContext.build(
        scenario="production without hooks",
        actors=[SocialActor("a1", "Actor")],
        content=[SocialContent("c1", "Content")],
        platform_mix=["line"],
        actions=[SocialAction("post", "a1", "c1")],
        runtime_mode=RuntimeMode.PRODUCTION,
    )

    result = run_simulation(context)

    assert result.runtime_mode is RuntimeMode.PRODUCTION
    assert result.summary["runtime_mode"] == "production"
    assert result.summary["governance_hooks_available"] is False


def test_target_only_actions_do_not_create_content_recommendation_signals():
    signals = recommendation_heuristic(
        [
            SocialAction("follow", "a1", target_id="actor-2"),
            SocialAction("evaluate_source_trust", "a1", target_id="source-1"),
        ]
    )

    assert signals == []


def test_single_platform_context_is_preserved_in_event_metadata():
    context = SimulationContext.build(
        scenario="single platform adapter action",
        actors=[SocialActor("a1", "Actor")],
        content=[SocialContent("c1", "Content")],
        platform_mix=["line"],
        actions=[SocialAction("send_message", "a1", "c1")],
    )

    result = run_simulation(context)

    assert result.event_log.events[0].metadata["platform"] == "line"


def test_negative_engagement_does_not_increase_recommendation_or_diffusion():
    actions = [
        SocialAction("watch_video", "a1", "video-1"),
        SocialAction("skip_video", "a1", "video-1"),
        SocialAction("decay_attention", "a1", "video-1"),
    ]

    recommendation = recommendation_heuristic(actions)
    diffusion = diffusion_heuristic(actions)

    assert recommendation[0].content_id == "video-1"
    assert recommendation[0].score == 0.1
    assert diffusion[0].reach == 0.1


def test_negative_only_engagement_is_suppressed_from_diffusion():
    actions = [
        SocialAction("skip_video", "a1", "video-1"),
        SocialAction("decay_attention", "a1", "video-1"),
    ]

    assert recommendation_heuristic(actions) == []
    assert diffusion_heuristic(actions) == []


def test_public_feed_advertises_emitted_signal_families():
    public_feed = get_default_behavior_registry().get("public_feed")

    assert public_feed.signals == (
        "RecommendationSignal",
        "DiffusionSignal",
        "OpinionSignal",
    )


def test_unweighted_neutral_actions_do_not_create_recommendation_signals():
    actions = [
        SocialAction("create_chat_group", "a1", "content-1"),
        SocialAction("send_message", "a1", "content-1"),
        SocialAction("refresh_feed", "a1", "content-1"),
    ]

    assert recommendation_heuristic(actions) == []
    assert diffusion_heuristic(actions) == []


def test_forward_message_creates_diffusion_signal():
    actions = [SocialAction("forward_message", "a1", "content-1")]

    diffusion = diffusion_heuristic(actions)

    assert diffusion[0].content_id == "content-1"
    assert diffusion[0].reach > 0


def test_long_form_video_actions_create_recommendation_signals():
    signals = recommendation_heuristic(
        [
            SocialAction("watch_long_video", "a1", "video-1"),
            SocialAction("comment_video", "a1", "video-1"),
        ]
    )

    assert signals[0].content_id == "video-1"
    assert signals[0].score > 0


def test_update_trust_score_emits_trust_signal():
    signals = trust_heuristic([SocialAction("update_trust_score", "a1", target_id="source-1")])

    assert signals[0].actor_id == "a1"
    assert signals[0].trust_delta > 0


def test_runner_rejects_unknown_actor_and_content_references():
    import pytest

    valid_actor = SocialActor("a1", "Actor")
    valid_content = SocialContent("c1", "Content")
    missing_actor_context = SimulationContext.build(
        scenario="missing actor",
        actors=[valid_actor],
        content=[valid_content],
        platform_mix=["line"],
        actions=[SocialAction("post", "missing-actor", "c1")],
    )
    missing_content_context = SimulationContext.build(
        scenario="missing content",
        actors=[valid_actor],
        content=[valid_content],
        platform_mix=["line"],
        actions=[SocialAction("post", "a1", "missing-content")],
    )

    with pytest.raises(ValueError, match="unknown actor"):
        run_simulation(missing_actor_context)
    with pytest.raises(ValueError, match="unknown content"):
        run_simulation(missing_content_context)
