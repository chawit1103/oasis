from collections import Counter, defaultdict

from socialsense_core.actions.types import SocialAction
from .base import DiffusionSignal, OpinionSignal, RecommendationSignal, TrustSignal

ENGAGEMENT_WEIGHTS = {
    "post": 1.0, "post_topic": 0.9, "comment": 0.5, "reply": 0.45, "react": 0.3, "share": 0.8, "follow": 0.4,
    "watch_video": 0.5, "skip_video": -0.2, "like_video": 0.4, "share_video": 0.8, "subscribe_channel": 0.6,
    "watch_long_video": 0.6, "comment_video": 0.5,
    "propagate_content": 1.0, "rumor_spread": 0.9, "official_response": 0.7, "correction_spread": 0.7,
    "forward_message": 0.7, "decay_attention": -0.2, "purchase_intent": 0.6, "view_product": 0.2,
}

TARGET_ONLY_ACTIONS = {
    "follow", "follow_creator", "follow_influencer", "subscribe_channel",
    "trust_influencer", "evaluate_source_trust", "update_trust_score",
}


def _content_signal_id(action: SocialAction) -> str | None:
    if action.content_id:
        return action.content_id
    payload_content_id = action.payload.get("content_id")
    if payload_content_id:
        return str(payload_content_id)
    if action.target_id and action.action_type not in TARGET_ONLY_ACTIONS:
        return action.target_id
    return None


def recommendation_heuristic(actions: list[SocialAction]) -> list[RecommendationSignal]:
    scores: defaultdict[str, float] = defaultdict(float)
    for action in actions:
        content_id = _content_signal_id(action)
        if content_id is None:
            continue
        weight = ENGAGEMENT_WEIGHTS.get(action.action_type, 0.0)
        if weight == 0.0:
            continue
        scores[content_id] += weight
    return [RecommendationSignal(content_id=k, score=round(v, 4), reason="deterministic engagement-weight heuristic") for k, v in sorted(scores.items()) if v > 0]


def diffusion_heuristic(actions: list[SocialAction]) -> list[DiffusionSignal]:
    out = []
    for signal in recommendation_heuristic(actions):
        share_count = sum(1 for a in actions if _content_signal_id(a) == signal.content_id and a.action_type in {"share", "share_video", "forward_message", "propagate_content", "rumor_spread"})
        reach = max(signal.score, 0.0) * (1 + share_count)
        out.append(DiffusionSignal(signal.content_id, reach=round(reach, 4), velocity=round(0.1 + share_count * 0.2, 4), reason="reach = non-negative engagement score multiplied by propagation actions"))
    return out


def opinion_update_heuristic(actions: list[SocialAction]) -> list[OpinionSignal]:
    by_actor: Counter[str] = Counter()
    for a in actions:
        if a.action_type in {"react", "like_video", "comment", "comment_video", "reply", "update_sentiment", "update_belief", "update_intent", "purchase_intent"}:
            by_actor[a.actor_id] += 1
        if a.action_type in {"skip_video", "decay_attention"}:
            by_actor[a.actor_id] -= 1
    return [OpinionSignal(actor_id=k, sentiment_delta=round(v * 0.05, 4), belief_delta=round(v * 0.03, 4), intent_delta=round(v * 0.02, 4), reason="small deterministic delta from engagement polarity") for k, v in sorted(by_actor.items())]


def trust_heuristic(actions: list[SocialAction]) -> list[TrustSignal]:
    by_actor: Counter[str] = Counter()
    for a in actions:
        if a.action_type in {"evaluate_source_trust", "update_trust_score", "trust_influencer", "official_response", "correction_spread"}:
            by_actor[a.actor_id] += 1
        if a.action_type in {"rumor_spread"}:
            by_actor[a.actor_id] -= 1
    return [TrustSignal(actor_id=k, trust_delta=round(v * 0.04, 4), reason="trust increases for verification/official response, decreases for rumor spread") for k, v in sorted(by_actor.items())]
