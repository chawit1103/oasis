from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="long_form_video",
    name="Long-form Video",
    actions=tuple(ACTION_DEFINITIONS["long_form_video"]),
    description="Reusable behavior module for long-form video simulations.",
    signals=(),
)
