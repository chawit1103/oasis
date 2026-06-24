# OASIS Mapping Strategy

OASIS is used as a research base and accelerator. SocialSense maps OASIS concepts into platform-agnostic behavior modules.

## Map, do not copy

- Copying OASIS `Platform` would import runtime, SQLite schema, channel loop, and dependency assumptions.
- Mapping OASIS concepts preserves the useful design vocabulary while keeping SocialSense modular.

## Twitter/X

OASIS Twitter-like `CREATE_POST`, `LIKE_POST`, `REPOST`, `QUOTE_POST`, `FOLLOW`, `TREND`, and `REFRESH` map to Public Feed, Information Diffusion, Recommendation / Discovery, and Opinion Formation.

## Reddit

OASIS Reddit-like score display and hot-score recommendation map to Community Group, Public Feed, Trust / Credibility, and Information Diffusion.

## Future work

Optional OASIS compatibility adapters can translate OASIS traces into SocialSense event logs, but the MVP does not import OASIS code.
