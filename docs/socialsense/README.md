# SocialSense Architecture Docs

This directory contains the SocialSense research and architecture baseline for the OASIS-derived simulation work.

## Documents

- `OASIS_RECON_REPORT.md` — Phase 1 reconnaissance of OASIS architecture, reusable seams, action types, lifecycle, recommendation models, risks, and integration strategy.
- `SOCIALSENSE_CORE_ARCHITECTURE.md` — Phase 2 core architecture baseline defining SocialSense abstractions, behavior modules, platform presets, signal families, simulation contracts, and governance hooks.
- `CIVICSENSE_3C_INTEGRATION_BRIDGE.md` — PR #2 bridge contract for CivicSense and 3C consumption, Thai platform presets, and dashboard summary shape.

## Architecture stance

SocialSense is research-first and behavior-driven. Core modules should stay reusable across verticals by using synthetic/default provenance, explicit runtime mode, typed signal outputs, and caller-supplied governance hooks instead of hard-coded project restrictions.
