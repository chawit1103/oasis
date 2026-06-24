from enum import Enum


class RuntimeMode(str, Enum):
    RESEARCH = "research"
    PRODUCTION = "production"


def normalize_runtime_mode(mode: str | RuntimeMode) -> RuntimeMode:
    if isinstance(mode, RuntimeMode):
        return mode
    return RuntimeMode(str(mode).lower())
