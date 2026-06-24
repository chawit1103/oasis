from collections.abc import Iterable

from .types import ACTION_DEFINITIONS


class ActionRegistry:
    def __init__(self) -> None:
        self._actions: dict[str, set[str]] = {}

    def register(self, behavior: str, actions: Iterable[str]) -> None:
        self._actions.setdefault(behavior, set()).update(actions)

    def has(self, action_type: str) -> bool:
        return any(action_type in actions for actions in self._actions.values())

    def actions_for(self, behavior: str) -> tuple[str, ...]:
        return tuple(sorted(self._actions.get(behavior, ())))

    def all_actions(self) -> tuple[str, ...]:
        return tuple(sorted({action for actions in self._actions.values() for action in actions}))


def build_default_action_registry() -> ActionRegistry:
    registry = ActionRegistry()
    for behavior, actions in ACTION_DEFINITIONS.items():
        registry.register(behavior, actions)
    return registry


def get_default_action_registry() -> ActionRegistry:
    return build_default_action_registry()
