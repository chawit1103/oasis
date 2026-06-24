from .base import SocialPlatformPreset
from . import x_twitter, reddit, line, facebook, tiktok, youtube, thailand

DEFAULT_PRESETS = (
    x_twitter.PRESET,
    reddit.PRESET,
    line.PRESET,
    facebook.PRESET,
    tiktok.PRESET,
    youtube.PRESET,
    *thailand.THAI_PRESETS,
)


class PlatformPresetRegistry:
    def __init__(self, presets: tuple[SocialPlatformPreset, ...] = DEFAULT_PRESETS) -> None:
        self._presets = {preset.key: preset for preset in presets}

    def register(self, preset: SocialPlatformPreset) -> None:
        self._presets[preset.key] = preset

    def get(self, key: str) -> SocialPlatformPreset:
        return self._presets[key]

    def keys(self) -> tuple[str, ...]:
        return tuple(sorted(self._presets))

    def all(self) -> tuple[SocialPlatformPreset, ...]:
        return tuple(self._presets[key] for key in self.keys())


def get_default_platform_registry() -> PlatformPresetRegistry:
    return PlatformPresetRegistry()
