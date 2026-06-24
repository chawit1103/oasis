from socialsense_core.adapters.dashboard_contract import to_dashboard_contract
from socialsense_core.adapters.civicsense_adapter import simulate_crisis_response, simulate_policy_message_diffusion
from socialsense_core.adapters.threec_marketing_adapter import simulate_campaign_response


REQUIRED_CONTRACT_KEYS = {
    "summary",
    "platform_breakdown",
    "sentiment_signal",
    "diffusion_signal",
    "trust_signal",
    "risk_signal",
    "recommended_next_observations",
    "provenance_labels",
    "runtime_mode",
}


def test_dashboard_contract_contains_required_top_level_keys():
    result = simulate_policy_message_diffusion(
        "Synthetic policy message",
        {"name": "Synthetic Thai civic audience"},
        platform_mix="civic_default_thailand",
        scenario_context="dashboard contract test",
    )

    contract = to_dashboard_contract(result, scenario_key="civic_policy_message", consumer="CivicSense")

    assert REQUIRED_CONTRACT_KEYS.issubset(contract.keys())
    assert contract["summary"]["scenario_key"] == "civic_policy_message"
    assert contract["summary"]["consumer"] == "CivicSense"
    assert contract["summary"]["dashboard_contract_version"] == "socialsense-dashboard-v1"
    assert contract["platform_breakdown"]["line"]["events"] >= 1
    assert isinstance(contract["sentiment_signal"]["net_sentiment_delta"], float)
    assert isinstance(contract["diffusion_signal"]["total_reach"], float)
    assert isinstance(contract["trust_signal"]["net_trust_delta"], float)
    assert contract["runtime_mode"] == "research"


def test_dashboard_contract_risk_signal_tracks_crisis_actions():
    result = simulate_crisis_response(
        "Synthetic crisis update",
        {"name": "Synthetic crisis audience"},
        platform_mix="crisis_default_thailand",
        scenario_context="risk signal test",
    )

    contract = to_dashboard_contract(result, scenario_key="civic_crisis_response", consumer="CivicSense")

    assert contract["risk_signal"]["rumor_events"] == 1
    assert contract["risk_signal"]["crisis_events"] == 1
    assert contract["risk_signal"]["level"] in {"medium", "high"}
    assert any("rumor" in item.lower() or "crisis" in item.lower() for item in contract["recommended_next_observations"])


def test_dashboard_contract_is_reusable_for_3c():
    result = simulate_campaign_response("Synthetic campaign", "Mock product", {"name": "Synthetic shoppers"})
    contract = to_dashboard_contract(result, scenario_key="threec_marketing_campaign", consumer="3C Marketing Simulator")

    assert contract["summary"]["consumer"] == "3C Marketing Simulator"
    assert contract["summary"]["platform_preset"] == "marketing_default_thailand"
    assert contract["platform_breakdown"]["tiktok"]["actions"]["purchase_intent"] == 1
