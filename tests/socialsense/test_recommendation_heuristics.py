from socialsense_core.actions.types import SocialAction
from socialsense_core.recommendation.heuristics import recommendation_heuristic


def test_recommendation_heuristic_scores_content():
    signals = recommendation_heuristic([SocialAction("post", "a1", "c1"), SocialAction("share", "a1", "c1")])
    assert signals[0].content_id == "c1"
    assert signals[0].score > 1.0
