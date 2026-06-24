from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="community_group",
    name="Community Group",
    actions=tuple(ACTION_DEFINITIONS["community_group"]),
    description="Reusable behavior module for community group simulations.",
    signals=(),
)
