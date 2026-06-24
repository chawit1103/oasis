from .types import SocialBehaviorModule
from . import public_feed, community_group, private_messaging, short_video, long_form_video, influencer_network, recommendation, information_diffusion, opinion_formation, trust_credibility, social_commerce, crisis_spread

DEFAULT_MODULES = (
    public_feed.MODULE, community_group.MODULE, private_messaging.MODULE, short_video.MODULE, long_form_video.MODULE,
    influencer_network.MODULE, recommendation.MODULE, information_diffusion.MODULE, opinion_formation.MODULE,
    trust_credibility.MODULE, social_commerce.MODULE, crisis_spread.MODULE,
)


class BehaviorModuleRegistry:
    def __init__(self, modules: tuple[SocialBehaviorModule, ...] = DEFAULT_MODULES) -> None:
        self._modules = {module.key: module for module in modules}

    def register(self, module: SocialBehaviorModule) -> None:
        self._modules[module.key] = module

    def get(self, key: str) -> SocialBehaviorModule:
        return self._modules[key]

    def keys(self) -> tuple[str, ...]:
        return tuple(sorted(self._modules))

    def all(self) -> tuple[SocialBehaviorModule, ...]:
        return tuple(self._modules[key] for key in self.keys())


def get_default_behavior_registry() -> BehaviorModuleRegistry:
    return BehaviorModuleRegistry()
