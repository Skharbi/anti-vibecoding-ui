# Evaluation Cases

Use these cases to test the skill against realistic prompts and code/screens.

## Trigger cases

### T1 — implicit design complaint
Prompt: "Something feels off about this dashboard spacing and hierarchy. Fix it."
Expected: skill triggers without the words vibe/vibecoding.

### T2 — backend-only task
Prompt: "Optimize this Postgres query."
Expected: skill does not trigger unless UI impact is explicitly part of the task.

### T3 — accessibility-specific
Prompt: "My modal works with the mouse but keyboard users get stuck."
Expected: accessibility/full interaction review; focus management prioritized.

## Review cases

### R1 — visually vibecoded but technically functional
Fixture characteristics:
- purple-blue gradient hero;
- glass cards;
- icon trio;
- generic buzzword copy;
- every section boxed in rounded cards.
Expected: flags generic visual patterns, but still checks state/responsive/accessibility basics.

### R2 — pretty UI with broken accessibility
Fixture characteristics:
- custom div buttons;
- no focus indicators;
- modal does not trap/restore focus;
- error messages not associated with inputs.
Expected: accessibility issues outrank cosmetic findings.

### R3 — responsive failure
Fixture characteristics:
- desktop sidebar fixed width;
- 4-column table overflows at 390px;
- sticky footer covers submit button when virtual keyboard opens.
Expected: specific mobile failures and verification widths.

### R4 — missing states
Fixture characteristics:
- data screen has only loaded state;
- no empty/error/loading/retry;
- submit action can double-fire.
Expected: state-completeness findings.

### R5 — form UX
Fixture characteristics:
- placeholders as labels;
- validation on every keystroke;
- password rules shown after failure;
- form clears after server error.
Expected: actionable form findings with preservation/recovery guidance.

### R6 — dense data workflow
Fixture characteristics:
- sortable table;
- filters;
- bulk delete;
- pagination.
Expected: semantics, sort state, filter visibility, selection scope, destructive confirmation, responsive strategy.

### R7 — intentional brand exception
Fixture characteristics:
- real brand guidelines explicitly require purple gradient and rounded pills.
Expected: no blanket "gradient/pill = bad" finding; assess execution and product fit instead.

### R8 — component library
Fixture characteristics:
- shadcn components mostly untouched;
- duplicate Button variants created with local classes;
- inconsistent radius/tokens across screens.
Expected: design-system findings without demanding a rewrite.

### R9 — RTL/localization
Fixture characteristics:
- Arabic locale;
- chevrons remain LTR;
- hardcoded left/right spacing;
- date/currency not localized;
- long translations overflow.
Expected: RTL/i18n coverage.

### R10 — chart accessibility
Fixture characteristics:
- red/green-only encoding;
- hover-only data;
- unlabeled axes;
- no textual alternative.
Expected: data-viz accessibility and clarity findings.

## Generation cases

### G1 — SaaS dashboard
Prompt: "Build a professional analytics dashboard."
Expected:
- requests/infers product context before visual gimmicks;
- information hierarchy first;
- real empty/loading/error states;
- responsive strategy;
- restrained, product-specific styling.

### G2 — portfolio
Prompt: "Build my portfolio for a healthcare informatics professional with AI side projects."
Expected:
- career identity before AI projects;
- implemented vs experimental status clear;
- evidence/outcomes prioritized over startup marketing aesthetic.

### G3 — mobile form
Prompt: "Create a mobile insurance authorization form."
Expected:
- persistent labels;
- appropriate input types;
- multi-step/progress if justified;
- validation/recovery;
- keyboard-safe controls;
- narrow-screen hierarchy.

## False-positive cases

### F1 — justified cards
Fixture: cards represent discrete records with separate actions.
Expected: do not flag cards merely because many exist.

### F2 — justified animation
Fixture: motion communicates reordering/state transition and respects reduced motion.
Expected: do not remove animation simply because animation exists.

### F3 — native browser behavior
Fixture: semantic controls already provide correct keyboard behavior.
Expected: do not add unnecessary ARIA or custom key handlers.
