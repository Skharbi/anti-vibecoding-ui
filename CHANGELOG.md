# Changelog

All notable repository changes are documented here.

The project follows semantic versioning for the portable plugin manifest.

## [Unreleased]

- Corrected manifest validation bypasses and non-object crashes; reject duplicate JSON keys and invalid required-field types.
- Validate optional skill metadata types and compatibility length.
- Protect portable safety-rule presence and agent skill mentions against deletion.
- Document contributor QA dependencies and expand deterministic regressions to 33 test methods.
- Reject escaping/unresolvable installed symlinks, enforce every coverage domain exactly once, and handle malformed Markdown URLs without tracebacks.
- Release behavioral/client/runtime gates remain pending; no new model score or version bump.

## [0.2.0] - 2026-09-24

Historical validation below applies only to that revision, not October changes. See `evals/results/CURRENT.md`.

### Added
- portable root `plugin.json` packaging;
- Codex compatibility manifest;
- 38-area production UI review checklist;
- cybersecurity and trust-boundary guidance;
- privacy, reliability, observability, browser compatibility, API-boundary, SEO/discoverability, and rendering/cache/concurrency coverage;
- component behavior reference;
- best-practice coverage matrix;
- 42 behavioral regression cases;
- six execution-gated runtime/render cases;
- deterministic repository validator;
- installation, security, contribution, release, support, conduct, AI-agent, PR, and issue-intake documentation.

### Changed
- expanded the skill from visual anti-vibecoding review into a production UI engineering protocol;
- strengthened triggering for accessibility, security/privacy, production-readiness, browser/platform, and API/rendering requests;
- added false-positive and evidence-level controls;
- made the portable paste edition explicitly condensed.

### Validation status
- repository structural gate: passing;
- author-model scored run: **100%**;
- independent Claude full-suite run: **95.6%**, with **0 critical failures**;
- post-hardening targeted Claude regression run: **97.1%**, with **0 critical failures** and **0 new false positives**;
- Chromium runtime evidence recorded with documented limitations;
- v0.2.0 satisfies the repository's documented release-validation bar.

## [0.1.0] - 2026-09-17

### Added
- initial anti-vibecoding UI Agent Skill;
- visual/UI checklist;
- README and portable installation guidance;
- OpenAI skill metadata.
