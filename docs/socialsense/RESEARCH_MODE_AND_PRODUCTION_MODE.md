# Research Mode and Production Mode

## Research Mode

Research Mode allows broad modeling of influence propagation, persuasion dynamics, information diffusion, social contagion, opinion formation, recommendation dynamics, marketing response, and crisis response. It is for synthetic simulation and research exploration.

## Production Mode

Production Mode exists as a runtime marker and governance-hook surface. Downstream applications may enforce their own policy boundaries. The core intentionally does **not** hard-code project-specific policy restrictions because SocialSense must remain reusable for civic, commercial, public-opinion, crisis, and consumer research applications.

## Governance hooks

`SimulationContext.governance_hooks` can carry downstream validators, policy metadata, labels, or export restrictions. The deterministic MVP only exposes whether hooks are available; downstream apps enforce them.

## Disclaimers

All examples and tests use synthetic/mock data. No real PII, platform credentials, live scraping, or hidden external calls are required.
