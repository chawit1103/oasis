from socialsense_core.adapters.civicsense_adapter import demo_public_opinion_scenarios, simulate_crisis_response, simulate_policy_message_diffusion, simulate_public_opinion


def test_civicsense_adapter_interfaces_exist():
    result = simulate_public_opinion("message", {"name": "aud"}, ["line"], "context")
    assert result.summary["platform_mix"] == ["line"]
    assert simulate_crisis_response("crisis", {}, ["facebook"], "ctx").event_log
    assert simulate_policy_message_diffusion("policy", {}, ["youtube"], "ctx").event_log


def test_civicsense_adapter_outputs_dashboard_ready_summary_with_rich_scenario():
    scenarios = demo_public_opinion_scenarios()
    assert len(scenarios) >= 3
    assert {"key", "title", "message", "audience_profile", "platform_preset", "scenario_context"}.issubset(scenarios[0])
    assert scenarios[0]["platform_preset"] == "civic_default_thailand"

    result = simulate_public_opinion(
        scenarios[0]["message"],
        scenarios[0]["audience_profile"],
        scenarios[0]["platform_preset"],
        scenarios[0]["scenario_context"],
    )

    summary = result.summary
    assert summary["dashboard_version"] == "socialsense-core-v1"
    assert summary["scenario_family"] == "civicsense_public_opinion"
    assert summary["platform_preset"] == "civic_default_thailand"
    assert summary["headline_metrics"]["events"] == len(result.event_log)
    assert summary["series"]["actions_by_step"]
    assert summary["integration_contract"]["consumer"] == "CivicSense"
    assert summary["simulation_disclaimer"].startswith("Synthetic deterministic simulation")


def test_civicsense_adapter_honors_explicit_and_omitted_platform_mix():
    explicit = simulate_public_opinion("message", {"name": "aud"}, ["line"], "context")
    assert explicit.summary["platform_mix"] == ["line"]
    assert {step["platform"] for step in explicit.summary["series"]["actions_by_step"]} == {"line"}

    omitted = simulate_public_opinion("message", {"name": "aud"}, scenario_context="context")
    assert omitted.summary["platform_preset"] == "civic_default_thailand"
    assert omitted.summary["platform_mix"] == ["line", "facebook", "tiktok", "youtube"]
