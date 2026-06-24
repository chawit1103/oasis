from dataclasses import dataclass, field

from .types import SocialEvent


@dataclass
class EventLog:
    events: list[SocialEvent] = field(default_factory=list)

    def append(self, event: SocialEvent) -> None:
        self.events.append(event)

    def __iter__(self):
        return iter(self.events)

    def __len__(self) -> int:
        return len(self.events)

    def by_action(self, action_type: str) -> tuple[SocialEvent, ...]:
        return tuple(event for event in self.events if event.action.action_type == action_type)

    def to_summary(self) -> dict[str, int]:
        summary: dict[str, int] = {}
        for event in self.events:
            summary[event.action.action_type] = summary.get(event.action.action_type, 0) + 1
        return summary
