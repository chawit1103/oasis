from socialsense_core.adapters.civicsense_adapter import simulate_crisis_response, simulate_policy_message_diffusion, simulate_public_opinion


def test_civicsense_adapter_interfaces_exist():
    result = simulate_public_opinion("message", {"name": "aud"}, ["line"], "context")
    assert result.summary["platform_mix"] == ["line"]
    assert simulate_crisis_response("crisis", {}, ["facebook"], "ctx").event_log
    assert simulate_policy_message_diffusion("policy", {}, ["youtube"], "ctx").event_log
