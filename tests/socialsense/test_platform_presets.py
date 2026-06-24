from socialsense_core.platforms.registry import get_default_platform_registry


def test_platform_presets_map_expected_behavior_modules():
    registry = get_default_platform_registry()
    assert "line" in registry.keys()
    assert "private_messaging" in registry.get("line").behavior_modules
    assert "short_video" in registry.get("tiktok").behavior_modules
    assert "community_group" in registry.get("reddit").behavior_modules
    assert "post" in registry.get("x_twitter").actions


def test_thai_platform_mix_presets_are_registered_and_named_for_verticals():
    registry = get_default_platform_registry()
    keys = registry.keys()

    assert "civic_default_thailand" in keys
    assert "marketing_default_thailand" in keys
    assert "crisis_default_thailand" in keys

    civic = registry.get("civic_default_thailand")
    assert civic.display_name == "Civic default Thailand"
    assert civic.context_notes
    assert {"line", "facebook", "tiktok", "youtube"}.issubset(civic.oasis_mapping["platform_mix"].split(","))
    assert "opinion_formation" in civic.behavior_modules

    marketing = registry.get("marketing_default_thailand")
    assert "social_commerce" in marketing.behavior_modules
    assert "purchase_intent" in marketing.actions

    crisis = registry.get("crisis_default_thailand")
    assert "crisis_spread" in crisis.behavior_modules
    assert "official_response" in crisis.actions
