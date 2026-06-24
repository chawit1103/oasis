from .base import SocialPlatformPreset

PRESET = SocialPlatformPreset(
    key='x_twitter',
    display_name='X / Twitter',
    behavior_modules=('public_feed', 'recommendation', 'information_diffusion', 'opinion_formation'),
    actions=('post', 'comment', 'react', 'share', 'follow', 'search_topic', 'trend_topic', 'refresh_feed'),
    recommendation_signals=('engagement', 'recency', 'topic_affinity'),
    context_notes=('OASIS ActionType.CREATE_POST -> post', 'LIKE_POST -> react', 'REPOST/QUOTE_POST -> share', 'FOLLOW -> follow', 'SEARCH_POSTS/TREND/REFRESH -> search_topic/trend_topic/refresh_feed'),
    oasis_mapping={'CREATE_POST': 'post', 'CREATE_COMMENT': 'comment', 'LIKE_POST': 'react', 'REPOST': 'share', 'QUOTE_POST': 'share', 'FOLLOW': 'follow', 'SEARCH_POSTS': 'search_topic', 'TREND': 'trend_topic', 'REFRESH': 'refresh_feed'},
)
