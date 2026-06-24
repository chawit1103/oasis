from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="crisis_spread",
    name="Crisis Spread",
    actions=tuple(ACTION_DEFINITIONS["crisis_spread"]),
    description="Reusable behavior module for crisis spread simulations.",
    signals=(),
)
