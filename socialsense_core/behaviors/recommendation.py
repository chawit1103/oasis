from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="recommendation",
    name="Recommendation / Discovery",
    actions=tuple(ACTION_DEFINITIONS["recommendation_discovery"]),
    description="Reusable behavior module for recommendation / discovery simulations.",
    signals=("RecommendationSignal",),
)
