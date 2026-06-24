from dataclasses import dataclass, field
from typing import Any, Mapping

from socialsense_core.actions.types import SocialAction
from socialsense_core.governance.labels import ProvenanceLabel
from socialsense_core.governance.modes import RuntimeMode, normalize_runtime_mode
from socialsense_core.personas.types import SocialActor, SocialContent


@dataclass(frozen=True)
class SimulationContext:
    scenario: str
    actors: tuple[SocialActor, ...]
    content: tuple[SocialContent, ...]
    platform_mix: tuple[str, ...]
    actions: tuple[SocialAction, ...]
    runtime_mode: RuntimeMode = RuntimeMode.RESEARCH
    provenance_labels: tuple[ProvenanceLabel, ...] = (ProvenanceLabel.SYNTHETIC,)
    governance_hooks: Mapping[str, Any] = field(default_factory=dict)

    @classmethod
    def build(cls, scenario: str, actors: list[SocialActor], content: list[SocialContent], platform_mix: list[str], actions: list[SocialAction], runtime_mode: str | RuntimeMode = RuntimeMode.RESEARCH, provenance_labels: tuple[ProvenanceLabel, ...] = (ProvenanceLabel.SYNTHETIC,), governance_hooks: Mapping[str, Any] | None = None) -> "SimulationContext":
        return cls(scenario=scenario, actors=tuple(actors), content=tuple(content), platform_mix=tuple(platform_mix), actions=tuple(actions), runtime_mode=normalize_runtime_mode(runtime_mode), provenance_labels=provenance_labels, governance_hooks=governance_hooks or {})
