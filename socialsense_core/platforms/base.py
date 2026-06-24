from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True)
class SocialPlatformPreset:
    key: str
    display_name: str
    behavior_modules: tuple[str, ...]
    actions: tuple[str, ...]
    recommendation_signals: tuple[str, ...] = ()
    context_notes: tuple[str, ...] = ()
    oasis_mapping: Mapping[str, str] = field(default_factory=dict)
