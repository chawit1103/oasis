from socialsense_core.actions.types import SocialAction
from socialsense_core.governance.labels import ProvenanceLabel
from socialsense_core.personas.types import SocialActor, SocialContent
from socialsense_core.simulation.context import SimulationContext
from socialsense_core.simulation.runner import run_simulation

from .dashboard import platform_for, resolve_platform_mix, with_dashboard_summary


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
        consumer="3C Marketing Simulator",
        scenario_family=scenario_family,
        platform_preset=preset_key,
        input_metadata=input_metadata,
    )


def demo_marketing_campaign_scenarios():
    return [
        {
            "key": "healthy-snack-launch-value-seekers",
            "title": "Healthy snack launch for value-seeking shoppers",
            "campaign_message": "Synthetic launch message with trial pack, creator review, and LINE coupon reminder.",
            "product_context": "mock healthy snack bundle; no real brand, SKU, or ad account",
            "audience_profile": {"name": "Synthetic Thai value-seeking shoppers", "country": "TH", "segment": "family grocery buyers"},
            "platform_preset": "marketing_default_thailand",
        },
        {
            "key": "ev-test-drive-regional-awareness",
            "title": "EV test-drive regional awareness",
            "campaign_message": "Synthetic awareness campaign comparing total cost of ownership and service coverage.",
            "product_context": "mock EV test-drive campaign; synthetic offer only",
            "audience_profile": {"name": "Synthetic regional car intenders", "country": "TH", "segment": "mid-income commuters"},
            "platform_preset": "marketing_default_thailand",
        },
        {
            "key": "tourism-weekend-social-commerce",
            "title": "Weekend tourism social-commerce offer",
            "campaign_message": "Synthetic creator-led weekend package message with review prompts and shareable deal.",
            "product_context": "mock travel package; demo inventory only",
            "audience_profile": {"name": "Synthetic domestic travelers", "country": "TH", "segment": "short-break planners"},
            "platform_preset": "marketing_default_thailand",
        },
    ]


def simulate_campaign_response(campaign_message, product_context, audience_profile, platform_mix=None, runtime_mode="research"):
    preset_key, resolved_mix = resolve_platform_mix(platform_mix, "marketing_default_thailand")
    actions = [
        SocialAction("post", "audience-1", "message-1", platform=platform_for(resolved_mix, "facebook")),
        SocialAction("discover_content", "audience-1", "message-1", platform=platform_for(resolved_mix, "tiktok")),
        SocialAction("watch_video", "audience-1", "message-1", platform=platform_for(resolved_mix, "tiktok")),
        SocialAction("react", "audience-1", "message-1", platform=platform_for(resolved_mix, "facebook")),
        SocialAction("view_product", "audience-1", "message-1", platform=platform_for(resolved_mix, "facebook"), payload={"product_context": product_context}),
        SocialAction("purchase_intent", "audience-1", "message-1", platform=platform_for(resolved_mix, "tiktok"), payload={"product_context": product_context}),
        SocialAction("share_deal", "audience-1", "message-1", platform=platform_for(resolved_mix, "facebook")),
    ]
    return _run(
        f"campaign response: {product_context}",
        campaign_message,
        audience_profile,
        resolved_mix,
        runtime_mode,
        actions,
        "threec_marketing_campaign",
        preset_key,
        {"product_context": product_context, "campaign_message": campaign_message},
    )


def simulate_brand_sentiment(brand_message, audience_profile, platform_mix=None, runtime_mode="research"):
    preset_key, resolved_mix = resolve_platform_mix(platform_mix, "marketing_default_thailand")
    actions = [
        SocialAction("post", "audience-1", "message-1", platform=platform_for(resolved_mix, "facebook")),
        SocialAction("comment", "audience-1", "message-1", platform=platform_for(resolved_mix, "facebook")),
        SocialAction("comment_video", "audience-1", "message-1", platform=platform_for(resolved_mix, "tiktok")),
        SocialAction("update_sentiment", "audience-1", "message-1", platform=platform_for(resolved_mix, "facebook")),
        SocialAction("evaluate_source_trust", "audience-1", "message-1", platform=platform_for(resolved_mix, "youtube")),
    ]
    return _run(
        "brand sentiment",
        brand_message,
        audience_profile,
        resolved_mix,
        runtime_mode,
        actions,
        "threec_brand_sentiment",
        preset_key,
        {"brand_message": brand_message},
    )


def simulate_social_commerce_response(offer_message, product_context, audience_profile, platform_mix=None, runtime_mode="research"):
    preset_key, resolved_mix = resolve_platform_mix(platform_mix, "commerce_default_thailand")
    actions = [
        SocialAction("view_product", "audience-1", "message-1", platform=platform_for(resolved_mix, "facebook"), payload={"product_context": product_context}),
        SocialAction("ask_for_review", "audience-1", "message-1", platform=platform_for(resolved_mix, "line")),
        SocialAction("purchase_intent", "audience-1", "message-1", platform=platform_for(resolved_mix, "tiktok")),
        SocialAction("share_deal", "audience-1", "message-1", platform=platform_for(resolved_mix, "facebook")),
        SocialAction("update_intent", "audience-1", "message-1", platform=platform_for(resolved_mix, "tiktok")),
    ]
    return _run(
        f"social commerce: {product_context}",
        offer_message,
        audience_profile,
        resolved_mix,
        runtime_mode,
        actions,
        "threec_social_commerce",
        preset_key,
        {"product_context": product_context, "offer_message": offer_message},
    )
