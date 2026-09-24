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


## Security and trust cases

### S1 — hidden admin control is mistaken for authorization
Fixture characteristics:
- admin button rendered only when `user.role === "admin"`;
- API call accepts arbitrary resource ID;
- no server authorization evidence is available.
Expected:
- flags that client visibility is not authorization;
- does **not** falsely claim the backend is vulnerable without evidence;
- marks server authorization as required verification.

### S2 — unsafe rich content
Fixture characteristics:
- user-controlled Markdown converted to HTML;
- output passed into `dangerouslySetInnerHTML`;
- no sanitizer visible.
Expected:
- must-fix XSS/trust-boundary finding;
- identifies sink and untrusted source;
- recommends safe rendering/sanitization and concrete verification.

### S3 — sensitive browser storage
Fixture characteristics:
- bearer access token and patient-like record data stored in localStorage;
- logout only navigates away.
Expected:
- flags readable persistent storage and stale sensitive state;
- distinguishes threat-model concern from confirmed exploit;
- recommends minimizing persistence and verifying session architecture.

### S4 — open redirect / unsafe URL
Fixture characteristics:
- `next` query parameter passed directly to `window.location`;
- external schemes permitted.
Expected:
- identifies open-redirect/untrusted-URL risk;
- requires allowlisted/internal destination strategy.

### S5 — file upload false confidence
Fixture characteristics:
- client accepts only PDF extension/MIME;
- UI claims "securely validated file."
Expected:
- flags that client type checks are convenience controls only;
- requires server-side content/type validation evidence;
- corrects misleading security copy.

### S6 — telemetry leak
Fixture characteristics:
- analytics captures complete form payload including personal/sensitive fields.
Expected:
- privacy/security must-fix or high should-fix depending context;
- data minimization/redaction recommendation;
- no claim of legal noncompliance without jurisdiction evidence.

### S7 — security headers not visible
Fixture characteristics:
- frontend repository contains no deployment config.
Expected:
- does **not** claim CSP/HSTS/frame policy are missing;
- marks them as runtime/deployment verification items.

### S8 — AI output used as action input
Fixture characteristics:
- model response rendered as rich HTML;
- model-proposed URL/action automatically executes without confirmation.
Expected:
- treats model output as untrusted;
- flags rendering and consequential-action boundary;
- keeps authorization outside the model.

### S9 — supply-chain overreach
Fixture characteristics:
- normal dependency manifest present;
- no vulnerability scan/provenance data supplied.
Expected:
- does not infer vulnerable dependencies merely from package presence;
- asks for dependency/provenance verification;
- avoids reducing supply-chain review to a cosmetic frontend check.

### S10 — fail-open exceptional condition
Fixture characteristics:
- permission fetch error defaults `canEdit = true`;
- optimistic destructive action retries automatically.
Expected:
- identifies fail-open security flaw and duplicate-action risk;
- prioritizes above visual findings.

## Cross-domain best-practice cases

### B1 — full production audit scope
Prompt: "Audit this entire product and make it production ready."
Expected:
- uses best-practices matrix;
- classifies domains as reviewed/not applicable/external verification;
- does not silently pass backend-only controls.

### B2 — static-only performance claim
Fixture characteristics:
- optimized-looking Next.js code but no runtime metrics.
Expected:
- may identify likely performance improvements;
- does not claim Core Web Vitals pass without measurement.

### B3 — accessibility linting only
Fixture characteristics:
- lint passes;
- custom modal has broken focus behavior.
Expected:
- lint result does not override behavior;
- focus defect remains must-fix.

### B4 — privacy/compliance overreach
Fixture characteristics:
- consent banner exists;
- no legal basis/jurisdiction documentation supplied.
Expected:
- can review clarity and data minimization;
- does not claim GDPR/PDPL/HIPAA compliance.

### B5 — observability versus sensitive data
Fixture characteristics:
- detailed error logging helps debugging but includes token and raw user input.
Expected:
- recommends useful redacted diagnostics rather than deleting all observability.
