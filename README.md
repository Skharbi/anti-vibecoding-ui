# anti-vibecoding-ui

A production UI engineering Agent Skill for reviewing and generating interfaces without generic AI-made patterns — while also checking accessibility, responsive behavior, interaction states, frontend security/privacy, reliability, performance-sensitive UI decisions, browser/platform behavior, and evidence quality.

**Current package version:** `0.2.0`  
**Status:** packaged and under validation; not claimed as fully validated or publicly published.

## Quick start

For the full skill, use the installable folder:

```
skills/anti-vibecoding-ui/
```

For an OpenAI/Codex portable plugin workflow, use the repository root. It now includes the current portable `plugin.json` plus a `.codex-plugin/plugin.json` compatibility manifest.

For a no-install/mobile workflow, use `PASTE-TO-INSTALL.md`.

See **[INSTALL.md](INSTALL.md)** for the full install matrix and smoke tests.

## What it does

### Review mode

Reviews real frontend code and rendered behavior using evidence-based findings:

- **must-fix** — security/privacy exposure, blocked tasks, serious accessibility/responsive failures, data-loss or unsafe high-impact behavior;
- **should-fix** — confusing hierarchy, weak states, design-system drift, generic visual patterns, non-critical usability issues;
- **judgment call** — valid product/brand/design tradeoffs.

### Generation mode

Uses the same rules as design constraints before writing UI:

- information hierarchy before decoration;
- product-specific visual language;
- semantic HTML and accessible interaction behavior;
- realistic loading/empty/error/success states;
- responsive/mobile strategy;
- security/privacy and trust-boundary awareness;
- design-system consistency;
- restrained motion and credible copy;
- final verification rather than “looks good” approval.

## Coverage

The current checklist contains **38 review areas**, covering:

- product fit and information architecture;
- visual style, typography, copy, layout and navigation;
- buttons, links, icons, imagery and semantic HTML;
- keyboard/focus, forms, validation and state completeness;
- loading, empty, error and async feedback;
- responsive/mobile behavior and accessibility;
- dialogs, drawers, popovers, menus, tabs and accordions;
- tables, filters, bulk actions and data visualization;
- destructive actions, authentication and permissions;
- internationalization, localization and RTL;
- performance and perceived performance;
- component-library/design-system discipline;
- motion restraint;
- portfolio and AI-product credibility;
- cybersecurity and trust boundaries;
- privacy and data minimization;
- reliability, recovery and exceptional conditions;
- testing/verification discipline;
- observability and diagnosability;
- browser compatibility and progressive enhancement;
- public-site discoverability/metadata;
- API consumption/frontend-backend contracts;
- rendering, hydration, caching and concurrency;
- final anti-vibecoding review.

## Package structure

```
anti-vibecoding-ui/
├── plugin.json
├── .codex-plugin/
│   └── plugin.json
├── README.md
├── INSTALL.md
├── SECURITY.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── RELEASE.md
├── AGENTS.md
├── HANDOVER.md
├── LICENSE
├── PASTE-TO-INSTALL.md
├── .github/
│   └── PULL_REQUEST_TEMPLATE.md
├── evals/
│   ├── README.md
│   ├── cases.md
│   ├── EXECUTION-GATE.md
│   └── results/
├── scripts/
│   └── validate_skill.py
└── skills/
    └── anti-vibecoding-ui/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        └── references/
            ├── checklist.md
            ├── review-protocol.md
            ├── component-behavior.md
            ├── security.md
            ├── best-practices-matrix.md
            └── sources.md
```

## Validation

Validation has three layers.

### 1. Package/repository validation

Run:

```bash
python scripts/validate_skill.py
```

The validator checks package structure, manifest/version consistency, OpenAI metadata constraints, skill-description length, self-contained references, evaluation counts, documentation consistency, relative links, and common secret patterns.

### 2. Behavioral evaluation

`evals/cases.md` contains **42 regression scenarios** covering triggering, review quality, generation, false positives, security/trust, cross-domain best practices, and platform/delivery behavior.

### 3. Execution gates

`evals/EXECUTION-GATE.md` defines the cases that require real rendered/browser/device/native-language evidence rather than static inspection.

## Standards and best-practice sources

The skill's primary references include:

- W3C WCAG 2.2 and WAI-ARIA/APG;
- OWASP Top 10:2025, ASVS 5.0.0, WSTG 4.2, Cheat Sheet Series, and API Security Top 10 2023;
- NIST SP 800-218 SSDF 1.1 and NIST Privacy Framework;
- MDN Baseline/progressive enhancement;
- Google Search Essentials;
- current OpenAI Agent Skills / Agent Plugins packaging guidance.

See `skills/anti-vibecoding-ui/references/sources.md`.

## Current validation status

**Implemented**
- portable Agent Plugins manifest;
- Codex compatibility manifest;
- self-contained Agent Skill bundle;
- 38-area production UI checklist;
- security/trust, component behavior, and best-practice references;
- 42 regression scenarios;
- deterministic validator;
- installation/security/contribution/release documentation;
- recorded same-model structural/scenario self-test.

**Still required before a “fully validated” claim**
- independent second-agent/model evaluation;
- real rendered generation checks;
- RTL/native-language rendering validation;
- representative browser/device execution for execution-gated cases.

The repository deliberately does not turn unavailable evidence into a pass.

## Repository policies

- **[INSTALL.md](INSTALL.md)** — installation and smoke tests
- **[SECURITY.md](SECURITY.md)** — vulnerability reporting and security rules
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — contribution expectations
- **[RELEASE.md](RELEASE.md)** — pre-release checklist
- **[CHANGELOG.md](CHANGELOG.md)** — version history
- **[HANDOVER.md](HANDOVER.md)** — current working state

## License

MIT — use, adapt, and redistribute freely.
