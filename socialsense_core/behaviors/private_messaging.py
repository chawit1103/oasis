from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="private_messaging",
    name="Private Messaging",
    actions=tuple(ACTION_DEFINITIONS["private_messaging"]),
    description="Reusable behavior module for private messaging simulations.",
    signals=(),
)
