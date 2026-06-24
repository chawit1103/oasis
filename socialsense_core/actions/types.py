from dataclasses import dataclass, field
from typing import Any, Mapping


@dataclass(frozen=True)
class SocialAction:
    action_type: str
    actor_id: str
    content_id: str | None = None
    target_id: str | None = None
    platform: str | None = None
    payload: Mapping[str, Any] = field(default_factory=dict)


PUBLIC_FEED_ACTIONS = ("post", "comment", "react", "share", "follow", "refresh_feed")
COMMUNITY_GROUP_ACTIONS = ("create_group", "join_group", "leave_group", "post_topic", "reply", "moderate")
PRIVATE_MESSAGING_ACTIONS = ("send_message", "reply_message", "forward_message", "create_chat_group", "listen_group")
SHORT_VIDEO_ACTIONS = ("publish_video", "watch_video", "skip_video", "like_video", "comment_video", "share_video", "follow_creator")
LONG_FORM_VIDEO_ACTIONS = ("publish_long_video", "watch_long_video", "subscribe_channel", "comment_video", "share_video")
INFLUENCER_NETWORK_ACTIONS = ("follow_influencer", "trust_influencer", "amplify_content", "creator_endorsement")
RECOMMENDATION_ACTIONS = ("discover_content", "rank_feed", "search_topic", "trend_topic")
INFORMATION_DIFFUSION_ACTIONS = ("expose_content", "propagate_content", "decay_attention")
OPINION_FORMATION_ACTIONS = ("update_sentiment", "update_belief", "update_intent")
TRUST_CREDIBILITY_ACTIONS = ("evaluate_source_trust", "update_trust_score")
SOCIAL_COMMERCE_ACTIONS = ("view_product", "ask_for_review", "purchase_intent", "share_deal")
CRISIS_SPREAD_ACTIONS = ("crisis_alert", "rumor_spread", "official_response", "correction_spread")

ACTION_DEFINITIONS = {
    "public_feed": PUBLIC_FEED_ACTIONS,
    "community_group": COMMUNITY_GROUP_ACTIONS,
    "private_messaging": PRIVATE_MESSAGING_ACTIONS,
    "short_video": SHORT_VIDEO_ACTIONS,
    "long_form_video": LONG_FORM_VIDEO_ACTIONS,
    "influencer_network": INFLUENCER_NETWORK_ACTIONS,
    "recommendation": RECOMMENDATION_ACTIONS,
    "information_diffusion": INFORMATION_DIFFUSION_ACTIONS,
    "opinion_formation": OPINION_FORMATION_ACTIONS,
    "trust_credibility": TRUST_CREDIBILITY_ACTIONS,
    "social_commerce": SOCIAL_COMMERCE_ACTIONS,
    "crisis_spread": CRISIS_SPREAD_ACTIONS,
}
