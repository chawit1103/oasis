from .base import SocialPlatformPreset

PRESET = SocialPlatformPreset(
    key='facebook',
    display_name='Facebook',
    behavior_modules=('public_feed', 'community_group', 'influencer_network', 'social_commerce', 'crisis_spread'),
    actions=('post', 'comment', 'react', 'share', 'join_group', 'follow', 'post_topic', 'view_product', 'share_deal'),
    recommendation_signals=('group_activity', 'page_follow', 'marketplace_intent'),
    context_notes=('Groups, pages, marketplace behavior, and live commerce can be modeled by adapters without hard-coding a locale.',),
    oasis_mapping={},
)
