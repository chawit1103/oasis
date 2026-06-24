from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping


class ProvenanceLabel(str, Enum):
    SYNTHETIC = "synthetic"
    MOCK = "mock"
    ANONYMIZED = "anonymized"
    OASIS_DERIVED_MAPPING = "oasis_derived_mapping"
    HUMAN_AUTHORED_SCENARIO = "human_authored_scenario"


@dataclass(frozen=True)
class ProvenanceRecord:
    label: ProvenanceLabel
    note: str = ""
    metadata: Mapping[str, str] = field(default_factory=dict)
