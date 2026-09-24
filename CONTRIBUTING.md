# Contributing

Contributions are welcome when they make the skill more accurate, useful, testable, or less prone to false positives.

## Before changing the skill

1. Read `SKILL.md`, the relevant reference file, and `evals/README.md`.
2. State the failure mode you are fixing.
3. Prefer a focused change over a broad rewrite.
4. Add or update an evaluation case for any new behavior rule.
5. Do not turn personal visual taste into a must-fix rule.

## Quality requirements

A contribution should:
- preserve the installable skill's self-contained folder structure;
- keep `SKILL.md` focused and move detailed material to `references/`;
- distinguish confirmed evidence from assumptions;
- preserve explicit backend/runtime verification boundaries;
- avoid unsupported compliance claims;
- preserve native HTML-before-ARIA guidance;
- avoid adding dependencies unless deterministic code is genuinely necessary;
- include realistic positive, negative, or false-positive eval coverage when behavior changes.

## Validate

Run:

```bash
python scripts/validate_skill.py
```

Then run the relevant cases from `evals/cases.md`.

For changes affecting responsive rendering, RTL, generation quality, or browser compatibility, follow `evals/EXECUTION-GATE.md`.

## Pull request notes

Describe:
- problem found;
- files changed;
- evidence/best-practice source;
- tests/evals run;
- remaining limitations.

Do not describe the skill as "fully validated", "secure", "WCAG compliant", "OWASP compliant", or similar unless the necessary independent/runtime evidence actually exists.
