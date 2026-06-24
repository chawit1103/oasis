from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="social_commerce",
    name="Social Commerce",
    actions=tuple(ACTION_DEFINITIONS["social_commerce"]),
    description="Reusable behavior module for social commerce simulations.",
    signals=(),
)
