from socialsense_core.scenario_packs import (
    get_scenario_pack,
    list_scenario_packs,
    run_scenario_pack,
)


def test_required_scenario_packs_are_available_and_synthetic():
    keys = set(list_scenario_packs())
    assert {
        "civic_policy_message",
        "civic_crisis_response",
        "threec_marketing_campaign",
        "threec_brand_sentiment",
        "social_commerce_response",
    }.issubset(keys)

    pack = get_scenario_pack("civic_policy_message")
    assert pack.platform_preset == "civic_default_thailand"
    assert pack.synthetic is True
    assert pack.consumer == "CivicSense"
    assert pack.runtime_mode == "research"


def test_scenario_pack_runs_to_dashboard_contract():
    contract = run_scenario_pack("social_commerce_response")

    assert contract["summary"]["scenario_key"] == "social_commerce_response"
    assert contract["summary"]["consumer"] == "3C Marketing Simulator"
    assert contract["platform_breakdown"]
    assert contract["sentiment_signal"]
    assert contract["diffusion_signal"]
    assert contract["trust_signal"]
    assert contract["risk_signal"]["level"] in {"low", "medium", "high"}
    assert contract["recommended_next_observations"]
    assert contract["provenance_labels"] == ["synthetic", "human_authored_scenario"]
    assert contract["runtime_mode"] == "research"
