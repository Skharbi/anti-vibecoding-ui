# Release Checklist

Use this before changing the portable plugin version or publishing a release.

## Package integrity
- [ ] `plugin.json` uses valid semantic versioning.
- [ ] `.codex-plugin/plugin.json` matches root name/version.
- [ ] `skills/anti-vibecoding-ui/SKILL.md` has valid frontmatter.
- [ ] Skill description is <= 1,024 characters.
- [ ] Combined `plugin-name:skill-name` identity is <= 64 characters.
- [ ] Exactly one `SKILL.md` exists in the skill folder.
- [ ] All referenced skill files are inside the installable skill folder.
- [ ] No unnecessary MCP/app/hook declarations exist.

## Repository QA
- [ ] Run `python scripts/validate_skill.py`.
- [ ] Review the diff for stale counts/version claims.
- [ ] Confirm no secrets or private data are present.
- [ ] Confirm README, INSTALL, SECURITY, CONTRIBUTING, CHANGELOG, and HANDOVER are current.
- [ ] Add a changelog entry for the release.

## Behavioral QA
- [ ] Run all trigger cases.
- [ ] Run negative/non-trigger cases.
- [ ] Run false-positive cases.
- [ ] Run security/trust-boundary cases.
- [ ] Run production-scope cases.
- [ ] Run platform/delivery cases.
- [ ] Run the six execution gates when applicable.
- [ ] Record agent/model/version/date and environment.
- [ ] Independent second-agent/model release bar is satisfied.

## Claims
- [ ] No claim of WCAG, OWASP, ASVS, privacy, performance, or browser compliance without required evidence.
- [ ] No “fully validated” claim while execution or independent-agent gates remain open.
- [ ] Published/installed status is stated accurately.

## OpenAI packaging
- [ ] Root portable manifest follows the current Agent Plugins schema.
- [ ] Skill agent metadata is valid.
- [ ] If preparing public directory submission, re-check current OpenAI submission requirements because portal metadata, assets, screenshots, and policy requirements can change.

## Final
- [ ] PR is mergeable and up to date with `main`.
- [ ] Release version matches `CHANGELOG.md`.
- [ ] `HANDOVER.md` next task is updated.
