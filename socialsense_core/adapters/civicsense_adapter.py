from socialsense_core.actions.types import SocialAction
from socialsense_core.governance.labels import ProvenanceLabel
from socialsense_core.personas.types import SocialActor, SocialContent
from socialsense_core.simulation.context import SimulationContext
from socialsense_core.simulation.runner import run_simulation

from .dashboard import resolve_platform_mix, with_dashboard_summary


def _actors(audience_profile):
    if isinstance(audience_profile, dict):
        name = audience_profile.get("name", "Synthetic audience")
        traits = audience_profile
    else:
        name = str(audience_profile or "Synthetic audience")
        traits = {"profile": name}
    return [SocialActor(actor_id="audience-1", display_name=name, traits=traits)]


def _run(scenario, message, audience_profile, platform_mix, runtime_mode, actions, scenario_family, preset_key, input_metadata):
    content = [SocialContent(content_id="message-1", text=message, author_id="source", topic="scenario")]
    context = SimulationContext.build(
        scenario=scenario,
        actors=_actors(audience_profile),
        content=content,
        platform_mix=platform_mix,
        actions=actions,
        runtime_mode=runtime_mode,
        provenance_labels=(ProvenanceLabel.SYNTHETIC, ProvenanceLabel.HUMAN_AUTHORED_SCENARIO),
        governance_hooks={"downstream_policy_boundary": "application-owned"},
    )
    result = run_simulation(context)
    return with_dashboard_summary(
        result,
        consumer="CivicSense",
        scenario_family=scenario_family,
        platform_preset=preset_key,
        input_metadata=input_metadata,
    )


def demo_public_opinion_scenarios():
    return [
        {
            "key": "transit-fare-consultation-bangkok",
            "title": "Bangkok transit fare consultation",
            "message": "Synthetic explainer about staged fare changes, household impact, and feedback windows.",
            "audience_profile": {"name": "Synthetic Bangkok commuters", "country": "TH", "segment": "urban commuters"},
            "platform_preset": "civic_default_thailand",
            "scenario_context": "public consultation on transit affordability and service reliability",
        },
        {
            "key": "flood-preparedness-local-services",
            "title": "Flood preparedness and municipal services",
            "message": "Synthetic civic update on drainage work, shelters, hotlines, and local reporting steps.",
            "audience_profile": {"name": "Synthetic flood-prone community", "country": "TH", "segment": "local households"},
            "platform_preset": "crisis_default_thailand",
            "scenario_context": "local readiness communication before seasonal flooding",
        },
        {
            "key": "digital-id-service-redesign",
            "title": "Digital ID service redesign",
            "message": "Synthetic policy message explaining privacy safeguards and service access trade-offs.",
            "audience_profile": {"name": "Synthetic digital public service users", "country": "TH", "segment": "mixed age groups"},
            "platform_preset": "civic_default_thailand",
            "scenario_context": "public opinion around digital government service changes",
        },
    ]


def simulate_public_opinion(message, audience_profile, platform_mix, scenario_context, runtime_mode="research"):
    preset_key, resolved_mix = resolve_platform_mix(platform_mix, "civic_default_thailand")
    actions = [
        SocialAction("post", "audience-1", "message-1", platform="facebook"),
        SocialAction("send_message", "audience-1", "message-1", platform="line"),
        SocialAction("react", "audience-1", "message-1", platform="facebook"),
        SocialAction("share", "audience-1", "message-1", platform="facebook"),
        SocialAction("watch_video", "audience-1", "message-1", platform="tiktok"),
        SocialAction("update_sentiment", "audience-1", "message-1", platform="facebook"),
        SocialAction("evaluate_source_trust", "audience-1", "message-1", platform="line"),
    ]
    return _run(
        f"public opinion: {scenario_context}",
        message,
        audience_profile,
        resolved_mix,
        runtime_mode,
        actions,
        "civicsense_public_opinion",
        preset_key,
        {"scenario_context": scenario_context, "message": message},
    )


def simulate_crisis_response(crisis_message, audience_profile, platform_mix, scenario_context, runtime_mode="research"):
    preset_key, resolved_mix = resolve_platform_mix(platform_mix, "crisis_default_thailand")
    actions = [
        SocialAction("crisis_alert", "audience-1", "message-1", platform="line"),
        SocialAction("rumor_spread", "audience-1", "message-1", platform="line"),
        SocialAction("official_response", "audience-1", "message-1", platform="facebook"),
        SocialAction("correction_spread", "audience-1", "message-1", platform="line"),
        SocialAction("evaluate_source_trust", "audience-1", "message-1", platform="facebook"),
    ]
    return _run(
        f"crisis response: {scenario_context}",
        crisis_message,
        audience_profile,
        resolved_mix,
        runtime_mode,
        actions,
        "civicsense_crisis_response",
        preset_key,
        {"scenario_context": scenario_context, "message": crisis_message},
    )


def simulate_policy_message_diffusion(policy_message, audience_profile, platform_mix, scenario_context, runtime_mode="research"):
    preset_key, resolved_mix = resolve_platform_mix(platform_mix, "civic_default_thailand")
    actions = [
        SocialAction("post", "audience-1", "message-1", platform="facebook"),
        SocialAction("expose_content", "audience-1", "message-1", platform="youtube"),
        SocialAction("propagate_content", "audience-1", "message-1", platform="line"),
        SocialAction("share_video", "audience-1", "message-1", platform="tiktok"),
        SocialAction("update_belief", "audience-1", "message-1", platform="facebook"),
    ]
    return _run(
        f"policy diffusion: {scenario_context}",
        policy_message,
        audience_profile,
        resolved_mix,
        runtime_mode,
        actions,
        "civicsense_policy_diffusion",
        preset_key,
        {"scenario_context": scenario_context, "message": policy_message},
    )
