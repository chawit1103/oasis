from socialsense_core.actions.types import SocialAction
from socialsense_core.recommendation.heuristics import opinion_update_heuristic


def test_opinion_update_has_actor_delta():
    signals = opinion_update_heuristic([SocialAction("react", "a1", "c1"), SocialAction("update_belief", "a1", "c1")])
    assert signals[0].actor_id == "a1"
    assert signals[0].sentiment_delta > 0
