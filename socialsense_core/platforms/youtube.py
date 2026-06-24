from .base import SocialPlatformPreset

PRESET = SocialPlatformPreset(
    key='youtube',
    display_name='YouTube',
    behavior_modules=('long_form_video', 'short_video', 'influencer_network', 'recommendation', 'trust_credibility'),
    actions=('publish_long_video', 'watch_long_video', 'publish_video', 'watch_video', 'subscribe_channel', 'comment_video', 'share_video', 'evaluate_source_trust'),
    recommendation_signals=('watch_time', 'subscription_affinity', 'source_credibility'),
    context_notes=('Long-form plus Shorts with channel trust and subscriptions.',),
    oasis_mapping={},
)
