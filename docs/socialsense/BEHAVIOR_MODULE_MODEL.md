# Behavior Module Model

SocialSense models reusable behavior modules first, then maps platforms onto those modules.

## Modules

| Module | Actions |
|---|---|
| Public Feed | `post`, `comment`, `react`, `share`, `follow`, `refresh_feed` |
| Community Group | `create_group`, `join_group`, `leave_group`, `post_topic`, `reply`, `moderate` |
| Private Messaging | `send_message`, `reply_message`, `forward_message`, `create_chat_group`, `listen_group` |
| Short Video | `publish_video`, `watch_video`, `skip_video`, `like_video`, `comment_video`, `share_video`, `follow_creator` |
| Long-form Video | `publish_long_video`, `watch_long_video`, `subscribe_channel`, `comment_video`, `share_video` |
| Influencer Network | `follow_influencer`, `trust_influencer`, `amplify_content`, `creator_endorsement` |
| Recommendation / Discovery | `discover_content`, `rank_feed`, `search_topic`, `trend_topic` |
| Information Diffusion | `expose_content`, `propagate_content`, `decay_attention` |
| Opinion Formation | `update_sentiment`, `update_belief`, `update_intent` |
| Trust / Credibility | `evaluate_source_trust`, `update_trust_score` |
| Social Commerce | `view_product`, `ask_for_review`, `purchase_intent`, `share_deal` |
| Crisis Spread | `crisis_alert`, `rumor_spread`, `official_response`, `correction_spread` |

Each module declares actions and optional signal types. The simulation runner validates actions through the action registry and records events.
