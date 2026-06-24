from socialsense_core.adapters.threec_marketing_adapter import demo_marketing_campaign_scenarios, simulate_brand_sentiment, simulate_campaign_response, simulate_social_commerce_response


def test_3c_adapter_interfaces_exist():
    result = simulate_campaign_response("campaign", "product", {"name": "aud"}, ["tiktok"])
    assert result.summary["platform_mix"] == ["tiktok"]
    assert simulate_brand_sentiment("brand", {}, ["facebook"]).event_log
    assert simulate_social_commerce_response("offer", "product", {}, ["line"]).event_log


def test_3c_adapter_outputs_dashboard_ready_summary_with_rich_scenario():
    scenarios = demo_marketing_campaign_scenarios()
    assert len(scenarios) >= 3
    assert {"key", "title", "campaign_message", "product_context", "audience_profile", "platform_preset"}.issubset(scenarios[0])
    assert scenarios[0]["platform_preset"] == "marketing_default_thailand"

    result = simulate_campaign_response(
        scenarios[0]["campaign_message"],
        scenarios[0]["product_context"],
        scenarios[0]["audience_profile"],
        scenarios[0]["platform_preset"],
    )

    summary = result.summary
    assert summary["dashboard_version"] == "socialsense-core-v1"
    assert summary["scenario_family"] == "threec_marketing_campaign"
    assert summary["platform_preset"] == "marketing_default_thailand"
    assert summary["headline_metrics"]["purchase_intent_events"] >= 1
    assert summary["series"]["actions_by_step"]
    assert summary["integration_contract"]["consumer"] == "3C Marketing Simulator"
