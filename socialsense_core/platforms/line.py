from .base import SocialPlatformPreset

PRESET = SocialPlatformPreset(
    key='line',
    display_name='LINE',
    behavior_modules=('private_messaging', 'community_group', 'trust_credibility', 'information_diffusion', 'crisis_spread'),
    actions=('create_chat_group', 'join_group', 'leave_group', 'send_message', 'reply_message', 'forward_message', 'listen_group', 'rumor_spread', 'correction_spread'),
    recommendation_signals=('forward_rate', 'group_trust', 'official_account_future'),
    context_notes=('Private and group messaging, high-trust groups, and forwarded messages can be modeled by adapters without hard-coding a locale.',),
    oasis_mapping={},
)
