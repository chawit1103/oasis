from dataclasses import dataclass, field
from typing import Any, Mapping

from socialsense_core.events.event_log import EventLog
from socialsense_core.governance.labels import ProvenanceLabel
from socialsense_core.governance.modes import RuntimeMode
from socialsense_core.recommendation.base import DiffusionSignal, OpinionSignal, RecommendationSignal, TrustSignal


@dataclass(frozen=True)
class SimulationResult:
    scenario: str
    runtime_mode: RuntimeMode
    event_log: EventLog
    recommendation_signals: tuple[RecommendationSignal, ...]
    diffusion_signals: tuple[DiffusionSignal, ...]
    opinion_signals: tuple[OpinionSignal, ...]
    trust_signals: tuple[TrustSignal, ...]
    provenance_labels: tuple[ProvenanceLabel, ...]
    summary: Mapping[str, Any] = field(default_factory=dict)
