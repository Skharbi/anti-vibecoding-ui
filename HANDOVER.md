# Maintainer Handover

This file contains public maintainer context only. It intentionally excludes private session links, credentials, account details, and internal-only working notes.

## Current state

- Package version: `0.2.0`
- Default branch: `main`
- Installable skill: `skills/anti-vibecoding-ui/`
- Runtime dependencies: none
- Repository validator: `python scripts/validate_skill.py`
- Behavioral suite: `evals/cases.md`
- Browser/runtime evidence: `evals/results/`

## Maintainer rules

- Keep the installable skill self-contained.
- Do not add runtime dependencies without a demonstrated need.
- Preserve evidence-first findings and false-positive controls.
- Do not claim accessibility, security, privacy, browser, or legal compliance without the required evidence.
- When skill behavior changes, update or add evaluation coverage.
- Keep installation instructions simple and user-oriented.

## Release verification

Before a release:

1. Run `python scripts/validate_skill.py`.
2. Run affected behavioral cases.
3. Run execution-gated cases when rendering/browser behavior changed.
4. Use an independent model/agent for release validation when required by `evals/README.md`.
5. Review public files for secrets, personal data, stale internal notes, and unsupported claims.
6. Confirm README, INSTALL, CHANGELOG, SECURITY, and RELEASE are current.

## Public-repository rule

Do not commit:
- API keys, tokens, passwords, private keys, or credentials;
- private session/share URLs;
- personal or customer data;
- internal-only incident details;
- local absolute paths that identify a person or workstation.

Synthetic fixtures and evaluation transcripts must use non-sensitive test data only.
