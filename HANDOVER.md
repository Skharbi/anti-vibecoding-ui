# Maintainer Handover

This file contains public maintainer context only. It intentionally excludes private session links, credentials, account details, and internal-only working notes.

## Current state

- Package version: `0.2.0`
- Default branch: `main`
- Installable skill: `skills/anti-vibecoding-ui/`
- Runtime dependencies: none
- QA dependency: pinned PyYAML in `requirements-dev.txt`; install before validator/test runs.
- October hardening: unreleased; current evidence in `evals/results/CURRENT.md`. Historical model scores do not validate changed instructions.
- Repository validator: `python scripts/validate_skill.py`
- Follow-up fixes: manifest container/type and duplicate-key checks, optional skill schema checks, portable-safety deletion probes, contributor dependency setup, installed symlink boundaries, all-domain coverage checks, and controlled URL errors. Deterministic suite: 35 validator and 8 preparation test methods.
- Behavioral suite: `evals/cases.md`
- Portable preparation: `scripts/prepare_evals.py`; 46 manifest cases, 58 predetermined attempts; prepares only, no paid/model invocation.
- Preparation/layout regression checks: `python scripts/test_preparation.py`; actual CLI discovery/invocation remains unverified.
- Independent Claude Code CLI run (2026-10-02): see `evals/results/2026-10-02-claude-independent.md`. Run 2 had 0 critical failures and an aggregate of 96.3%. Evidence is Chromium only.
- Next release gate:
  - a GPT-family or other second-family full run;
  - Safari/WebKit and Firefox execution for P1;
  - physical mobile keyboard checks for R3 and G3;
  - native Arabic review for R9;
  - Codex and interactive Claude Code discovery smoke tests.
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
   Also run `python scripts/test_validator.py` after installing QA dependencies.
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
