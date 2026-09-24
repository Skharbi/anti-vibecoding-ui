# anti-vibecoding-ui

An Agent Skill for reviewing and generating production-quality interfaces without generic AI-generated design patterns.

It started as an anti-"vibecoded" visual checklist. It now covers the broader reasons polished AI-built interfaces fail in real use: accessibility, keyboard/focus behavior, responsive design, forms, state completeness, data-heavy UI, destructive actions, RTL/localization, performance-sensitive UI decisions, design-system discipline, and evidence-based verification.

## What it does

### Review mode
Reviews real frontend code and rendered behavior using an engineering-grade checklist. Findings are evidence-based, prioritized by impact, and separated into:
- must-fix;
- should-fix;
- judgment calls.

It explicitly checks what already passes and avoids blanket bans when a pattern is justified by brand or product context.

### Generation mode
Uses the same rules as design constraints before writing UI:
- information hierarchy before decoration;
- product-specific visual language;
- semantic HTML;
- accessible interaction behavior;
- responsive/mobile strategy;
- realistic loading/empty/error/success states;
- design-system consistency;
- final anti-vibecoding self-review.

## Coverage

The current checklist contains 38 review areas, including:

- product fit and information architecture;
- visual style and brand fit;
- typography and copy credibility;
- layout, spacing, density, and navigation;
- buttons, links, icons, and imagery;
- semantic HTML;
- keyboard and focus;
- forms and validation;
- loading, empty, error, and async states;
- responsive/mobile behavior;
- WCAG-oriented accessibility;
- dialogs, drawers, popovers, menus, tabs, and accordions;
- tables, filters, bulk actions, pagination;
- charts and data visualization;
- destructive/high-impact actions;
- authentication and permission UX;
- internationalization, localization, and RTL;
- performance/perceived performance;
- component-library/design-system discipline;
- motion restraint;
- portfolio-specific credibility;
- AI/technical product credibility;
- cybersecurity and trust boundaries;
- privacy and data minimization;
- reliability/recovery and exceptional conditions;
- testing/verification discipline;
- observability and diagnosability;
- cross-domain best-practice coverage boundaries;
- browser compatibility and progressive enhancement;
- public-site discoverability/metadata;
- API consumption and frontend/backend contracts;
- rendering, hydration, caching, and concurrency;
- final "does this still look generic?" gate.

## Install

### Full skill — recommended

Install or copy the folder:

```
skills/anti-vibecoding-ui/
```

This is the canonical version. It includes the full protocol and supporting references.

**OpenAI/Codex skill path**
```
repo: Skharbi/anti-vibecoding-ui
path: skills/anti-vibecoding-ui
```

For other Agent Skills-compatible clients, copy the same folder into the client's skills directory.

### Portable single-paste edition

`PASTE-TO-INSTALL.md` remains available for users who cannot install a skill folder, including mobile-only workflows.

It is a **portable condensed edition**, not byte-for-byte identical to the full skill. The installed skill is the source of truth because it can load the complete checklist and supporting references without forcing an enormous first-message prompt.

## Structure

```
anti-vibecoding-ui/
├── README.md
├── LICENSE
├── HANDOVER.md
├── PASTE-TO-INSTALL.md
├── evals/
│   ├── README.md
│   └── cases.md
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

## Quality model

This project does not have a conventional build because it contains no runtime code.

Validation is behavioral.

The evaluation suite measures:
- trigger reliability;
- issue coverage;
- evidence quality;
- prioritization;
- false-positive control;
- fix quality;
- generation quality;
- verification discipline.

See `evals/README.md` and `evals/cases.md`.

## Standards

Accessibility and interaction guidance is grounded primarily in:
- WCAG 2.2;
- WAI-ARIA;
- ARIA Authoring Practices Guide.

The skill prefers native HTML semantics before ARIA and treats established ARIA patterns as behavior guidance that still requires real browser/assistive-technology testing for production-critical use.

## Status

**Implemented**
- Agent Skill packaging
- Full review/generation protocol
- 38-section production UI checklist
- Review severity/evidence protocol
- Common component behavior reference
- Primary standards references across accessibility, OWASP security, NIST secure development/privacy, and performance
- Behavioral evaluation suite with 42 regression scenarios
- Recorded self-test results and known verification limits
- Handover discipline

**Not yet proven**
- multi-agent evaluation results;
- quantified trigger reliability;
- quantified false-positive rate;
- generation quality across multiple model families.

Do not describe the skill as fully validated until the evaluation release bar in `evals/README.md` has been met.

## License

MIT — use, adapt, and redistribute freely.
