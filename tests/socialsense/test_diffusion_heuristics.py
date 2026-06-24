from socialsense_core.actions.types import SocialAction
from socialsense_core.recommendation.heuristics import diffusion_heuristic


def test_diffusion_heuristic_reflects_shares():
    signals = diffusion_heuristic([SocialAction("post", "a1", "c1"), SocialAction("share", "a1", "c1")])
    assert signals[0].reach > 1.0
    assert signals[0].velocity > 0.1
