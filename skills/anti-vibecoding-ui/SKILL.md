---
name: anti-vibecoding-ui
description: Review, redesign, or generate production-quality frontend UI/UX while preventing generic AI-generated design patterns and enforcing engineering-grade interface quality. Use for landing pages, dashboards, portfolios, product screens, design systems, component libraries, responsive/mobile work, accessibility reviews, form UX, data-heavy UI, or requests to make an interface feel intentional, professional, less generic, less "AI-made", or more usable. Trigger on UI generation, redesign, frontend critique, design-system cleanup, spacing/layout complaints, accessibility/keyboard issues, responsive problems, loading/error/empty states, forms/tables/charts/navigation, and requests to fix existing UI code. Do not use for backend-only logic or infrastructure work unless the user-facing interface is part of the task.
---

# Anti-Vibecoding UI

This is not a visual-taste checklist. It is a UI engineering and product-quality protocol.

The goal is to prevent two failure modes at once:
1. generic, trend-driven "AI-looking" interfaces;
2. interfaces that look polished but fail in accessibility, states, responsive behavior, interaction semantics, performance, or real-world usability.

Use the supporting files:
- `references/checklist.md` — full review/generation checklist.
- `references/review-protocol.md` — evidence, severity, output, and verification rules.
- `references/component-behavior.md` — expected behavior for common interactive components.
- `references/sources.md` — standards and primary references.
- `evals/README.md` and `evals/cases.md` — behavioral evaluation suite.

## Operating rule

Never approve an interface from appearance alone.

A UI passes only when it is:
**specific, usable, accessible, semantically correct, state-complete, responsive, performant, consistent, credible, and clearly connected to the real product and user workflow.**

## Before changing code

1. Identify the product, primary user, primary task, and screen/flow being changed.
2. Read the actual code and styles. Do not review from assumptions.
3. Identify the framework, component library, design tokens, routing model, existing conventions, and browser/runtime constraints.
4. Preserve working product behavior unless the user explicitly asks for a workflow change.
5. Prefer the existing design system and dependencies. Do not add libraries merely to make implementation easier.
6. If an existing brand system is present, treat it as an input constraint rather than replacing it with personal taste.

## Review modes

Use the smallest mode that covers the request.

### A. Visual-quality review
Use when the concern is polish, hierarchy, generic AI aesthetics, typography, spacing, copy, or component-library sameness.

### B. UX/interaction review
Use when the concern is workflow clarity, information architecture, navigation, forms, states, destructive actions, feedback, or task completion.

### C. Accessibility review
Use when accessibility is requested or whenever the UI includes custom interactive controls, dialogs, menus, tabs, forms, keyboard-heavy workflows, drag/drop, or data visualization.

### D. Responsive review
Use whenever layout or navigation changes. Verify at desktop, tablet, and narrow mobile widths instead of assuming CSS is sufficient.

### E. Full production review
Use by default for "audit", "review the whole UI", "make it production-ready", "fix everything", or similar broad requests. Apply every relevant section of the checklist.

## Review method

For existing code:

1. Inspect real files: components, routes, CSS/Tailwind, tokens, copy, state logic, and interaction handlers.
2. Walk `references/checklist.md` section by section.
3. For every finding, provide evidence: file + line, component/selector, or observable rendered behavior.
4. Classify findings using `references/review-protocol.md`.
5. Distinguish:
   - **must-fix** — broken behavior, accessibility failure, blocked task, misleading feedback, serious responsive issue;
   - **should-fix** — inconsistency, confusing hierarchy, poor state handling, generic pattern, maintainability/design-system drift;
   - **judgment call** — aesthetic or product tradeoff that needs user context.
6. Confirm what already passes. Do not manufacture problems to make the review look thorough.
7. If asked to fix, implement the clear fixes directly and preserve unrelated working code.
8. Re-run verification after changes.

## Generation method

When creating new UI:

1. Define the information hierarchy before decoration.
2. Design around real content, real states, and real user actions.
3. Establish:
   - page/grid structure;
   - typography scale;
   - spacing scale;
   - component hierarchy;
   - interaction states;
   - responsive behavior;
   - accessibility semantics;
   - loading/empty/error/success behavior.
4. Apply product-specific visual language. Do not default to startup gradients, glass cards, oversized rounded containers, floating blobs, generic icon trios, or marketing buzzwords.
5. Use semantic HTML before ARIA. Use ARIA only when native semantics are insufficient.
6. Build keyboard and focus behavior for custom interactive widgets.
7. Verify the result using the full final gate below.

## Mandatory coverage areas

Always consider whether each area applies. Do not silently skip them:

- visual style and brand fit;
- typography and content hierarchy;
- copy specificity and credibility;
- layout, spacing, density, and alignment;
- navigation and wayfinding;
- buttons, links, and action hierarchy;
- forms, validation, help text, and input affordances;
- empty/loading/error/success/disabled/permission/offline states;
- accessibility: semantics, names, focus, keyboard, contrast, motion, touch targets;
- responsive/mobile behavior;
- dialogs, menus, tabs, accordions, tooltips, popovers, drawers;
- tables, filters, sorting, pagination, bulk actions;
- charts/data visualization and non-color cues;
- destructive and irreversible actions;
- auth/account/permission UX where present;
- internationalization, long text, RTL, locale-sensitive content;
- performance-sensitive UI behavior;
- component-library and design-system discipline;
- consistency across screens, not just within one component;
- product-specific workflow fit;
- technical/AI credibility and claim accuracy;
- portfolio-specific rules when reviewing a personal portfolio.

## Accessibility baseline

For production-facing UI, target WCAG 2.2 AA unless the project explicitly requires another standard.

At minimum verify:
- semantic elements and heading order;
- accessible names/descriptions;
- keyboard reachability and operability;
- visible focus;
- focus order;
- focus management in overlays;
- contrast and non-color communication;
- touch target usability;
- reduced-motion behavior;
- form labels, errors, instructions, and required states;
- correct live-region use for asynchronous status;
- custom widget behavior consistent with established ARIA patterns.

Do not "fix accessibility" by adding ARIA indiscriminately. Incorrect ARIA can make an otherwise usable control worse.

## State-completeness rule

A component is not finished if only its happy-path static state is designed.

For every interactive or data-driven surface, consider:
- initial/default;
- hover where relevant;
- focus;
- active/pressed;
- selected/current;
- disabled;
- loading/pending;
- empty/no results;
- success;
- validation error;
- server/network error;
- permission-denied;
- partial data;
- long/overflowing content;
- offline/retry where relevant.

Only require states that are plausible for that component or flow; do not invent unreachable states.

## Responsive rule

Do not treat responsive design as "desktop but narrower."

Verify:
- information priority changes appropriately;
- navigation changes intentionally;
- dense tables have a usable narrow-screen strategy;
- touch targets remain usable;
- text does not overflow or wrap absurdly;
- fixed/sticky elements do not obscure content;
- dialogs/drawers fit small viewports;
- keyboard and mobile browser UI do not break critical controls;
- horizontal scrolling is intentional only where justified.

## Performance rule

Flag UI decisions that create avoidable user-facing cost:
- oversized media without responsive sizing;
- layout shift from missing dimensions;
- unnecessary client-side rendering;
- heavy animation or effects;
- expensive scroll/mouse listeners;
- rendering huge lists without an appropriate strategy;
- loading critical content behind decorative work;
- font/image choices that materially harm perceived performance.

Do not turn this skill into a generic performance audit; focus on performance that affects the interface.

## Design-system rule

When a design system or component library exists:
- reuse it before inventing replacements;
- preserve behavior contracts;
- fix tokens/systematically where the issue is systemic;
- do not fork near-identical components without a reason;
- do not leave stock defaults untouched when they conflict with the product identity;
- do not "anti-vibe" the UI by creating a second inconsistent design language.

## Final verification gate

Before saying a UI is complete, verify:

1. **Product fit** — does the screen visibly belong to this product and workflow?
2. **Task clarity** — can the primary task and next action be understood quickly?
3. **Behavior** — do interactive elements behave correctly in all relevant states?
4. **Accessibility** — keyboard, focus, semantics, names, contrast, motion, and forms are correct.
5. **Responsive** — desktop and narrow mobile are both intentionally designed.
6. **Content** — copy is specific, credible, concise, and not fabricated.
7. **Consistency** — tokens, spacing, typography, components, and interaction patterns align.
8. **Restraint** — decoration does not compete with information or actions.
9. **Performance** — no obvious UI implementation choices materially degrade the experience.
10. **Evidence** — verification is based on inspected code/rendered behavior, not assumption.

Then apply the final anti-vibecoding question:

**If the product name, logo, and copy were swapped, could this exact interface plausibly belong to dozens of unrelated products?**

If yes, the design is still too generic.

## Output behavior

Follow `references/review-protocol.md`.

Do not dump the entire checklist unless the user asks. Lead with the highest-impact findings, include evidence, implement clear fixes when requested, then summarize verification and remaining judgment calls.
