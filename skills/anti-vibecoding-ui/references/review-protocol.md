# Review Protocol

This file defines how to turn the checklist into a repeatable engineering review instead of a subjective design critique.

## 1. Evidence first

Every finding must be grounded in at least one of:
- file + line;
- component/selector;
- rendered behavior;
- keyboard/focus behavior;
- reproducible viewport/state;
- concrete product-flow consequence.

Do not report a violation because a pattern "might" exist.

## 2. Severity

### Must-fix
Use when the issue causes:
- blocked or incorrect task completion;
- inaccessible core interaction;
- keyboard trap or unusable focus behavior;
- misleading or missing critical feedback;
- serious responsive breakage;
- destructive-action risk;
- user data loss;
- semantic mismatch that materially harms assistive technology;
- critical content hidden or unreadable.

### Should-fix
Use for:
- confusing hierarchy or workflow;
- inconsistent states;
- weak error/empty/loading handling;
- generic AI-looking patterns that reduce product identity;
- design-system drift;
- maintainability issues visible in the UI;
- poor density or spacing that impairs scanning;
- non-critical accessibility or interaction quality gaps.

### Judgment call
Use when:
- multiple valid visual directions exist;
- product/brand context is missing;
- a checklist item is intentionally violated for a defensible reason;
- changing it would alter product strategy rather than merely fix implementation.

Never convert taste into a must-fix.

## 3. Finding format

Use compact findings:

**[Severity] Finding title**  
Evidence: `path/file.tsx:line` or observable behavior.  
Impact: what the user experiences.  
Fix: concrete action.  
Verify: how to prove the fix worked.

## 4. Review order

Prioritize:
1. blocked task / broken interaction;
2. accessibility and focus;
3. destructive/error handling;
4. mobile/responsive failures;
5. state completeness;
6. information architecture;
7. design-system consistency;
8. visual anti-vibecoding issues;
9. polish.

Do not lead with border radius while a keyboard trap exists.

## 5. Fix behavior

If the user asks to fix:
- implement must-fix items first;
- implement should-fix items when the solution is clear;
- leave judgment calls visible rather than silently deciding;
- avoid unrelated refactors;
- reuse existing tokens/components;
- do not add libraries without a real need.

## 6. Verification matrix

After changes, verify all relevant dimensions:

| Dimension | Minimum evidence |
|---|---|
| Primary task | Can be completed end-to-end |
| Keyboard | Reachable, operable, logical focus order |
| Focus | Visible, managed through overlays/navigation |
| Semantics | Native elements/ARIA states match behavior |
| Forms | Labels, validation, errors, preservation |
| Async | Loading, success, error, retry as relevant |
| Responsive | Desktop + tablet + narrow mobile |
| Content | Long text / empty / realistic data |
| Destructive | Consequence + confirmation/undo where appropriate |
| Motion | Reduced-motion behavior |
| Performance | No obvious UI-induced jank/layout shift |
| Product fit | Interface remains specific to product/workflow |

## 7. Pass rules

A review can end in:
- **Pass** — no must-fix issues; relevant verification completed.
- **Pass with issues** — no must-fix issues, but should-fix items remain.
- **Fail** — one or more must-fix issues remain or verification could not be completed.

Never claim "production-ready" from static inspection alone when interactive behavior was not executed.

## 8. False-positive control

Before logging a finding:
1. Is the rule relevant to this product?
2. Is there evidence of user harm, inconsistency, or genericness?
3. Is the implementation intentionally constrained by brand/system requirements?
4. Is there a valid exception?
5. Would the recommended fix actually improve the task?

If not, do not log it.

## 9. Output discipline

Do not dump all 28 checklist sections by default.

Return:
- highest-impact findings first;
- what already passes;
- fixes applied or recommended;
- verification performed;
- remaining judgment calls;
- final pass state.

If the user asks for a full audit, include section-by-section coverage and mark non-applicable areas explicitly.
