from dataclasses import dataclass


@dataclass(frozen=True)
class RecommendationSignal:
    content_id: str
    score: float
    reason: str


@dataclass(frozen=True)
class DiffusionSignal:
    content_id: str
    reach: float
    velocity: float
    reason: str


@dataclass(frozen=True)
class OpinionSignal:
    actor_id: str
    sentiment_delta: float
    belief_delta: float
    intent_delta: float
    reason: str


@dataclass(frozen=True)
class TrustSignal:
    actor_id: str
    trust_delta: float
    reason: str
