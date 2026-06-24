from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="trust_credibility",
    name="Trust / Credibility",
    actions=tuple(ACTION_DEFINITIONS["trust_credibility"]),
    description="Reusable behavior module for trust / credibility simulations.",
    signals=("TrustSignal",),
)
