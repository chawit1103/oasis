# Changelog

## 0.1.0 — Public API boundary preparation

Prepared SocialSense Core for external project consumption without publishing a package.

### Added

- Stable public import surface in `socialsense_core.__init__`.
- Version constants:
  - `socialsense_core.__version__`
  - `socialsense_core.version`
- Public exports for core models, registries, runner helpers, scenario packs, and dashboard contracts.
- External import demo: `examples/socialsense_external_import_demo.py`.
- Public API tests: `tests/socialsense/test_public_api_exports.py`.
- Package boundary, external consumer guide, and compatibility notes.

### Compatibility

- Existing examples and tests remain compatible.
- Existing internal modules are not removed.
- External consumers are encouraged to import from `socialsense_core` only.

### Not included

- No package publication.
- No CivicSense repository changes.
- No 3C repository changes.
- No external service dependencies.
