from .base import SocialPlatformPreset

PRESET = SocialPlatformPreset(
    key='reddit',
    display_name='Reddit',
    behavior_modules=('community_group', 'public_feed', 'trust_credibility', 'information_diffusion'),
    actions=('post_topic', 'reply', 'react', 'moderate', 'join_group'),
    recommendation_signals=('hot_score', 'upvote_downvote_equivalent', 'community_trust'),
    context_notes=('OASIS Reddit uses show_score/hot-score recsys and default reddit actions.', 'LIKE/DISLIKE map to react with polarity.'),
    oasis_mapping={'CREATE_POST': 'post_topic', 'CREATE_COMMENT': 'reply', 'LIKE_POST': 'react', 'DISLIKE_POST': 'react', 'JOIN_GROUP': 'join_group', 'REPORT_POST': 'moderate'},
)
