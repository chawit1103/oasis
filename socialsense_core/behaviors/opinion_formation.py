from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="opinion_formation",
    name="Opinion Formation",
    actions=tuple(ACTION_DEFINITIONS["opinion_formation"]),
    description="Reusable behavior module for opinion formation simulations.",
    signals=("OpinionSignal",),
)
