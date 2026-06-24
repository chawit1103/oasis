from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="short_video",
    name="Short Video",
    actions=tuple(ACTION_DEFINITIONS["short_video"]),
    description="Reusable behavior module for short video simulations.",
    signals=(),
)
