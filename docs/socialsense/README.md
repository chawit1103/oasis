# SocialSense Architecture Docs

This directory contains the SocialSense research and architecture baseline for the OASIS-derived simulation work.

## Documents

- `OASIS_RECON_REPORT.md` — Phase 1 reconnaissance of OASIS architecture, reusable seams, action types, lifecycle, recommendation models, risks, and integration strategy.
- `SOCIALSENSE_CORE_ARCHITECTURE.md` — Phase 2 core architecture baseline defining SocialSense abstractions, behavior modules, platform presets, signal families, simulation contracts, and governance hooks.
- `CIVICSENSE_3C_INTEGRATION_BRIDGE.md` — PR #2 bridge contract for CivicSense and 3C consumption, Thai platform presets, and dashboard summary shape.
- `DASHBOARD_OUTPUT_CONTRACT.md` — PR #3 reusable dashboard output contract for CivicSense and 3C.
- `SCENARIO_PACKS.md` — PR #3 deterministic scenario packs for civic, crisis, marketing, brand sentiment, and social commerce use cases.
- `NEXT_INTEGRATION_STEPS.md` — PR #3 future integration plan for downstream CivicSense and 3C repos.

## Architecture stance

SocialSense is research-first and behavior-driven. Core modules should stay reusable across verticals by using synthetic/default provenance, explicit runtime mode, typed signal outputs, and caller-supplied governance hooks instead of hard-coded project restrictions.
