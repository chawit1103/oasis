from socialsense_core.behaviors.registry import get_default_behavior_registry


def test_behavior_modules_expose_expected_actions():
    registry = get_default_behavior_registry()
    assert "public_feed" in registry.keys()
    assert "post" in registry.get("public_feed").actions
    assert "rumor_spread" in registry.get("crisis_spread").actions
