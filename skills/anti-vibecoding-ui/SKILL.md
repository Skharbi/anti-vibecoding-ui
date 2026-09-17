---
name: anti-vibecoding-ui
description: Apply an anti-vibecoding UI/UX checklist whenever front-end UI is built, generated, redesigned, or reviewed — landing pages, dashboards, portfolios, product screens, marketing sites, or component-library code (shadcn/ui, MUI, Tailwind). Trigger proactively on requests to build/create a page, site, component, or dashboard; "make it look better/more professional/less AI-generated"; polishing a hero, nav, card grid, or layout; a design/UI review; even vague complaints like "something feels off about the spacing" — even without the words "vibecoding" or "checklist." Covers new UI and fixing existing files. Not for backend logic, build/deploy errors, or non-visual debugging unless design is also in question. Covers gradients/glassmorphism, generic AI-startup typography, buzzword copy, icon overuse, cookie-cutter cards, pill navs, decorative animation, spacing/responsive discipline, component-library defaults, portfolio pitfalls, and overclaiming AI credibility.
---

# Anti-Vibecoding UI/UX Checklist

This skill exists because most AI-generated interfaces converge on the same generic look: purple-blue gradients, glassmorphism cards, pill-shaped everything, Lucide icons in threes, buzzword headlines, and scroll-triggered fade-ins. That look is now a tell — it signals "AI built this" more than it signals quality. This skill is a working checklist to actively apply, not a reference to summarize back to the user.

The full checklist lives in `references/checklist.md` — 15 sections, each with concrete checkbox items. **Read that file and use it directly** rather than relying on the short recap below; the recap exists only to help you decide which sections matter most for the task at hand.

## How to use this in review mode

When reviewing an existing UI/frontend codebase:

1. Read the actual files — CSS, component markup, copy — not a screenshot or a mental model of what it probably looks like.
2. Go through `references/checklist.md` section by section. For each unchecked item that applies, cite the specific file and line (or CSS selector / component name) where it shows up.
3. Group findings by section so the output mirrors the checklist's structure.
4. Explicitly note what *passes* clean, not just violations — a checklist that only lists problems reads as noise; confirming what's already good is part of the review.
5. Call out anything genuinely not applicable (e.g. §13 Portfolio-specific rules on a B2B SaaS dashboard) rather than forcing it.
6. Distinguish "clear fix, just do it" from "judgment call, flag for the user" — some items (like using a checkmark glyph as plain status text vs. a fake icon) are legitimately ambiguous.
7. End with the §15 "Does this look vibecoded?" gut-check and the final acceptance rule, applied to the whole interface, not just the sum of individual violations.

If asked to fix violations, do so directly in the code — don't just produce a report — unless the user only asked for a review.

## How to use this in generation mode

When building new UI from scratch:

1. Before writing markup/CSS, decide the product's actual visual language from its content and users — not from what a generic AI-startup template would use. What does this specific product do, and what should that make visible?
2. Apply the checklist as constraints while writing, especially:
   - §1 Visual style and §2 Typography — pick a deliberate palette and type scale tied to the product, not defaults.
   - §3 Headings and copy — write specific, concrete copy; no manufactured metrics or "Transform your..." phrasing.
   - §4–7 Icons, cards, navigation, buttons — use these elements only when they do real work, not to fill visual space.
   - §8 Animation — motion only where it communicates state or hierarchy.
   - §9–10 Spacing and responsive — a real spacing system and real mobile hierarchy, not shrink-to-fit.
   - §11 Component-library discipline — if using shadcn/ui or similar, deliberately override radius/spacing/type so it doesn't read as default.
3. Before presenting the result, run the §15 self-check against your own output as if reviewing someone else's code.

## Judgment, not just pattern-matching

The checklist bans specific patterns (gradients, pill navs, Lucide icon rows) because they're currently overused defaults — not because they're inherently wrong. If a task genuinely calls for one (a brand's real identity uses a purple gradient; a nav pattern requires pills for a specific reason), say so explicitly and explain why it's an exception rather than silently applying it. The goal named in the acceptance rule is the actual target: specific, functional, readable, consistently aligned, responsive, restrained, credible, and clearly tied to the real product — not rule-following for its own sake.
