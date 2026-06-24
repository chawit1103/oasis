from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping

from socialsense_core.actions.types import SocialAction
from socialsense_core.governance.labels import ProvenanceLabel


@dataclass(frozen=True)
class SocialEvent:
    event_id: str
    action: SocialAction
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    provenance: tuple[ProvenanceLabel, ...] = (ProvenanceLabel.SYNTHETIC,)
    metadata: Mapping[str, Any] = field(default_factory=dict)
