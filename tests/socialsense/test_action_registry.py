from socialsense_core.actions.registry import get_default_action_registry


def test_action_registry_loads_core_actions():
    registry = get_default_action_registry()
    assert registry.has("post")
    assert registry.has("rumor_spread")
    assert registry.has("purchase_intent")
    assert "refresh_feed" in registry.actions_for("public_feed")
