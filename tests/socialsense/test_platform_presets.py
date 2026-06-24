from socialsense_core.platforms.registry import get_default_platform_registry


def test_platform_presets_map_expected_behavior_modules():
    registry = get_default_platform_registry()
    assert "line" in registry.keys()
    assert "private_messaging" in registry.get("line").behavior_modules
    assert "short_video" in registry.get("tiktok").behavior_modules
    assert "community_group" in registry.get("reddit").behavior_modules
    assert "post" in registry.get("x_twitter").actions
