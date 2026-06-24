from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="influencer_network",
    name="Influencer Network",
    actions=tuple(ACTION_DEFINITIONS["influencer_network"]),
    description="Reusable behavior module for influencer network simulations.",
    signals=(),
)
