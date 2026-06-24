from socialsense_core.actions.types import SocialAction
from socialsense_core.governance.labels import ProvenanceLabel
from socialsense_core.governance.modes import RuntimeMode
from socialsense_core.personas.types import SocialActor, SocialContent
from socialsense_core.simulation.context import SimulationContext
from socialsense_core.simulation.runner import run_simulation


def _actors(audience_profile):
    if isinstance(audience_profile, dict):
        name = audience_profile.get("name", "Synthetic audience")
        traits = audience_profile
    else:
        name = str(audience_profile or "Synthetic audience")
        traits = {"profile": name}
    return [SocialActor(actor_id="audience-1", display_name=name, traits=traits)]


def _run(scenario, message, audience_profile, platform_mix, runtime_mode, actions):
    content = [SocialContent(content_id="message-1", text=message, author_id="source", topic="scenario")]
    context = SimulationContext.build(
        scenario=scenario, actors=_actors(audience_profile), content=content, platform_mix=list(platform_mix or ["line", "facebook"]), actions=actions, runtime_mode=runtime_mode, provenance_labels=(ProvenanceLabel.SYNTHETIC, ProvenanceLabel.HUMAN_AUTHORED_SCENARIO), governance_hooks={"downstream_policy_boundary": "application-owned"},
    )
    return run_simulation(context)


def simulate_public_opinion(message, audience_profile, platform_mix, scenario_context, runtime_mode="research"):
    actions = [SocialAction("post", "audience-1", "message-1", platform=(platform_mix or ["facebook"])[0]), SocialAction("react", "audience-1", "message-1"), SocialAction("share", "audience-1", "message-1"), SocialAction("update_sentiment", "audience-1", "message-1")]
    return _run(f"public opinion: {scenario_context}", message, audience_profile, platform_mix, runtime_mode, actions)


def simulate_crisis_response(crisis_message, audience_profile, platform_mix, scenario_context, runtime_mode="research"):
    actions = [SocialAction("crisis_alert", "audience-1", "message-1"), SocialAction("rumor_spread", "audience-1", "message-1"), SocialAction("official_response", "audience-1", "message-1"), SocialAction("correction_spread", "audience-1", "message-1")]
    return _run(f"crisis response: {scenario_context}", crisis_message, audience_profile, platform_mix, runtime_mode, actions)


def simulate_policy_message_diffusion(policy_message, audience_profile, platform_mix, scenario_context, runtime_mode="research"):
    actions = [SocialAction("post", "audience-1", "message-1"), SocialAction("expose_content", "audience-1", "message-1"), SocialAction("propagate_content", "audience-1", "message-1"), SocialAction("update_belief", "audience-1", "message-1")]
    return _run(f"policy diffusion: {scenario_context}", policy_message, audience_profile, platform_mix, runtime_mode, actions)
