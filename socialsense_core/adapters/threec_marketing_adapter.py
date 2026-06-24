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


def simulate_campaign_response(campaign_message, product_context, audience_profile, platform_mix, runtime_mode="research"):
    actions = [SocialAction("post", "audience-1", "message-1"), SocialAction("discover_content", "audience-1", "message-1"), SocialAction("react", "audience-1", "message-1"), SocialAction("purchase_intent", "audience-1", "message-1", payload={"product_context": product_context})]
    return _run(f"campaign response: {product_context}", campaign_message, audience_profile, platform_mix, runtime_mode, actions)


def simulate_brand_sentiment(brand_message, audience_profile, platform_mix, runtime_mode="research"):
    actions = [SocialAction("post", "audience-1", "message-1"), SocialAction("comment", "audience-1", "message-1"), SocialAction("update_sentiment", "audience-1", "message-1"), SocialAction("evaluate_source_trust", "audience-1", "message-1")]
    return _run("brand sentiment", brand_message, audience_profile, platform_mix, runtime_mode, actions)


def simulate_social_commerce_response(offer_message, product_context, audience_profile, platform_mix, runtime_mode="research"):
    actions = [SocialAction("view_product", "audience-1", "message-1", payload={"product_context": product_context}), SocialAction("ask_for_review", "audience-1", "message-1"), SocialAction("purchase_intent", "audience-1", "message-1"), SocialAction("share_deal", "audience-1", "message-1")]
    return _run(f"social commerce: {product_context}", offer_message, audience_profile, platform_mix, runtime_mode, actions)
