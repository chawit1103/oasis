from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class SocialActor:
    actor_id: str
    display_name: str
    traits: Mapping[str, Any] = field(default_factory=dict)
    trust_score: float = 0.5
    sentiment: float = 0.0
    belief: float = 0.0
    intent: float = 0.0


@dataclass(frozen=True)
class SocialContent:
    content_id: str
    text: str
    author_id: str | None = None
    topic: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)
