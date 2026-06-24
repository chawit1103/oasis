from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="public_feed",
    name="Public Feed",
    actions=tuple(ACTION_DEFINITIONS["public_feed"]),
    description="Reusable behavior module for public feed simulations.",
    signals=("RecommendationSignal", "DiffusionSignal", "OpinionSignal"),
)
