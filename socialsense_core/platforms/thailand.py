from .base import SocialPlatformPreset


THAI_PLATFORM_MIX = ("line", "facebook", "tiktok", "youtube")


CIVIC_DEFAULT_THAILAND = SocialPlatformPreset(
    key="civic_default_thailand",
    display_name="Civic default Thailand",
    behavior_modules=(
        "public_feed",
        "private_messaging",
        "community_group",
        "information_diffusion",
        "opinion_formation",
        "trust_credibility",
    ),
    actions=(
        "post",
        "comment",
        "react",
        "share",
        "send_message",
        "forward_message",
        "join_group",
        "expose_content",
        "propagate_content",
        "update_sentiment",
        "update_belief",
        "evaluate_source_trust",
    ),
    recommendation_signals=("topic_affinity", "group_trust", "forward_rate", "engagement"),
    context_notes=(
        "Synthetic Thai civic discussion mix spanning LINE groups, Facebook communities, TikTok short video, and YouTube explainers.",
        "Designed for dashboard demos only; no live platform API, scraping, credential, or external-service use.",
    ),
    oasis_mapping={"platform_mix": ",".join(THAI_PLATFORM_MIX), "vertical": "civicsense"},
)


MARKETING_DEFAULT_THAILAND = SocialPlatformPreset(
    key="marketing_default_thailand",
    display_name="Marketing default Thailand",
    behavior_modules=(
        "public_feed",
        "short_video",
        "long_form_video",
        "influencer_network",
        "recommendation",
        "social_commerce",
        "opinion_formation",
    ),
    actions=(
        "post",
        "discover_content",
        "watch_video",
        "like_video",
        "share_video",
        "follow_creator",
        "watch_long_video",
        "view_product",
        "ask_for_review",
        "purchase_intent",
        "share_deal",
        "update_intent",
    ),
    recommendation_signals=("watch_time", "creator_affinity", "topic_affinity", "marketplace_intent"),
    context_notes=(
        "Synthetic Thai campaign mix for Facebook, TikTok, YouTube, and LINE sharing paths.",
        "Suitable for 3C marketing demos and ROI dashboards without using real platform data.",
    ),
    oasis_mapping={"platform_mix": ",".join(THAI_PLATFORM_MIX), "vertical": "3c_marketing"},
)


CRISIS_DEFAULT_THAILAND = SocialPlatformPreset(
    key="crisis_default_thailand",
    display_name="Crisis default Thailand",
    behavior_modules=(
        "private_messaging",
        "community_group",
        "public_feed",
        "information_diffusion",
        "trust_credibility",
        "crisis_spread",
    ),
    actions=(
        "send_message",
        "forward_message",
        "post",
        "share",
        "expose_content",
        "propagate_content",
        "evaluate_source_trust",
        "crisis_alert",
        "rumor_spread",
        "official_response",
        "correction_spread",
    ),
    recommendation_signals=("forward_rate", "group_trust", "engagement", "source_reliability"),
    context_notes=(
        "Synthetic Thai crisis-response mix emphasizing LINE forwarding, Facebook groups, official pages, and video explainers.",
        "For tabletop and governance simulations only; no real incidents or live monitoring.",
    ),
    oasis_mapping={"platform_mix": ",".join(THAI_PLATFORM_MIX), "vertical": "crisis_response"},
)


THAI_PRESETS = (CIVIC_DEFAULT_THAILAND, MARKETING_DEFAULT_THAILAND, CRISIS_DEFAULT_THAILAND)
