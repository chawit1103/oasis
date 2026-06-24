from socialsense_core.actions.types import ACTION_DEFINITIONS
from .types import SocialBehaviorModule

MODULE = SocialBehaviorModule(
    key="information_diffusion",
    name="Information Diffusion",
    actions=tuple(ACTION_DEFINITIONS["information_diffusion"]),
    description="Reusable behavior module for information diffusion simulations.",
    signals=("DiffusionSignal",),
)
