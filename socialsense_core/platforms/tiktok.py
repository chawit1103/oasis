from .base import SocialPlatformPreset

PRESET = SocialPlatformPreset(
    key='tiktok',
    display_name='TikTok',
    behavior_modules=('short_video', 'influencer_network', 'recommendation', 'social_commerce', 'opinion_formation'),
    actions=('publish_video', 'watch_video', 'skip_video', 'like_video', 'comment_video', 'share_video', 'follow_creator', 'discover_content', 'purchase_intent'),
    recommendation_signals=('watch_time', 'completion_rate', 'engagement', 'creator_affinity', 'topic_affinity'),
    context_notes=('Short-video algorithmic discovery and creator affinity.',),
    oasis_mapping={},
)
