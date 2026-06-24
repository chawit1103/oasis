from socialsense_core.adapters.dashboard import resolve_platform_mix
from socialsense_core.platforms.registry import get_default_platform_registry


def test_thai_platform_mix_defaults_include_commerce_default():
    registry = get_default_platform_registry()

    for key in (
        "civic_default_thailand",
        "crisis_default_thailand",
        "marketing_default_thailand",
        "commerce_default_thailand",
    ):
        preset = registry.get(key)
        assert preset.key == key
        assert preset.oasis_mapping["platform_mix"] == "line,facebook,tiktok,youtube"


def test_commerce_default_thailand_advertises_commerce_actions():
    commerce = get_default_platform_registry().get("commerce_default_thailand")

    assert "social_commerce" in commerce.behavior_modules
    assert "recommendation" in commerce.behavior_modules
    assert "view_product" in commerce.actions
    assert "ask_for_review" in commerce.actions
    assert "purchase_intent" in commerce.actions
    assert "share_deal" in commerce.actions


def test_resolve_platform_mix_uses_commerce_default():
    preset_key, platform_mix = resolve_platform_mix("commerce_default_thailand", "marketing_default_thailand")

    assert preset_key == "commerce_default_thailand"
    assert platform_mix == ["line", "facebook", "tiktok", "youtube"]
