from dataclasses import dataclass, field
from typing import Mapping


@dataclass(frozen=True)
class SocialBehaviorModule:
    key: str
    name: str
    actions: tuple[str, ...]
    description: str
    signals: tuple[str, ...] = ()
    metadata: Mapping[str, str] = field(default_factory=dict)
