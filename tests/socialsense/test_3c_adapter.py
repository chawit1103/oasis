from socialsense_core.adapters.threec_marketing_adapter import simulate_brand_sentiment, simulate_campaign_response, simulate_social_commerce_response


def test_3c_adapter_interfaces_exist():
    result = simulate_campaign_response("campaign", "product", {"name": "aud"}, ["tiktok"])
    assert result.summary["platform_mix"] == ["tiktok"]
    assert simulate_brand_sentiment("brand", {}, ["facebook"]).event_log
    assert simulate_social_commerce_response("offer", "product", {}, ["line"]).event_log
