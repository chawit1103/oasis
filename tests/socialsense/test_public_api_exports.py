import socialsense_core as ssc


def test_public_api_exports_stable_version_and_contract_helpers():
    assert ssc.__version__ == "0.1.0"
    assert ssc.version == "0.1.0"

    required = {
        "SocialAction",
        "SocialEvent",
        "SocialActor",
        "SocialContent",
        "SocialPlatformPreset",
        "SocialBehaviorModule",
        "SimulationContext",
        "SimulationResult",
        "RecommendationSignal",
        "DiffusionSignal",
        "OpinionSignal",
        "TrustSignal",
        "ProvenanceLabel",
        "RuntimeMode",
        "DeterministicSimulationRunner",
        "run_simulation",
        "ScenarioPack",
        "get_scenario_pack",
        "list_scenario_packs",
        "run_scenario_pack",
        "to_dashboard_contract",
        "get_default_platform_registry",
        "get_default_behavior_registry",
        "build_default_action_registry",
    }

    assert required.issubset(set(ssc.__all__))
    for name in required:
        assert hasattr(ssc, name), name


def test_external_consumers_can_use_public_api_only():
    keys = ssc.list_scenario_packs()
    assert "civic_policy_message" in keys

    contract = ssc.run_scenario_pack("civic_policy_message")

    assert contract["summary"]["dashboard_contract_version"] == "socialsense-dashboard-v1"
    assert contract["summary"]["platform_preset"] == "civic_default_thailand"
    assert contract["runtime_mode"] == "research"
    assert contract["provenance_labels"] == ["synthetic", "human_authored_scenario"]
