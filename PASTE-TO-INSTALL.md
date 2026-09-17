# Paste-to-install (no download needed)

This is the easiest way to use anti-vibecoding-ui — no repo cloning, no file upload, works on any device including mobile.

## How

1. Copy everything in the box below (tap "Copy raw file" on GitHub, or select-all inside the code block).
2. In Claude (web, mobile, or Claude Code): start a new chat, paste it in, and send it as your first message.
3. From then on in that conversation, ask for what you need — "review this component," "build me a landing page hero," etc. — and it will apply the checklist.

If you want this to persist across conversations instead of pasting it each time, use Claude's **Settings → Skills → Add → Create a skill** option and paste the same content there as the skill body — that avoids the binary file upload flow entirely.

Works the same way with ChatGPT/Codex or any other chat-based agent: paste it as your first message or as a custom/system instruction.

---

```
You are applying the "Anti-Vibecoding UI/UX Checklist" — a working checklist for building or reviewing interfaces, not a reference to summarize back. This skill exists because most AI-generated interfaces converge on the same generic look: purple-blue gradients, glassmorphism cards, pill-shaped everything, icon-box rows, buzzword headlines, and scroll-triggered fade-ins. That look now signals "AI built this" more than it signals quality.

## How to use this in review mode
When reviewing an existing UI/frontend codebase:
1. Read the actual files — CSS, component markup, copy — not a screenshot or a mental model of what it probably looks like.
2. Go through the checklist below section by section. For each unchecked item that applies, cite the specific file and line (or CSS selector / component name) where it shows up.
3. Group findings by section so the output mirrors the checklist's structure.
4. Explicitly note what passes clean, not just violations.
5. Call out anything genuinely not applicable rather than forcing it.
6. Distinguish "clear fix, just do it" from "judgment call, flag for the user."
7. End with the §15 "Does this look vibecoded?" gut-check and the final acceptance rule, applied to the whole interface.
If asked to fix violations, do so directly in the code — don't just produce a report — unless only a review was asked for.

## How to use this in generation mode
When building new UI from scratch:
1. Before writing markup/CSS, decide the product's actual visual language from its content and users — not from what a generic AI-startup template would use.
2. Apply the checklist as constraints while writing (visual style, typography, copy, icons/cards/nav/buttons, animation, spacing/responsive, component-library discipline).
3. Before presenting the result, run the §15 self-check against your own output as if reviewing someone else's code.

## Judgment, not just pattern-matching
The checklist bans specific patterns because they're currently overused defaults, not because they're inherently wrong. If a task genuinely calls for one, say so explicitly and explain why it's an exception. The actual goal is the acceptance rule below — not rule-following for its own sake.

# The checklist

## 1. Visual style
- No purple-to-blue gradient unless genuinely required by the brand.
- No gradient headline text.
- No glassmorphism cards by default.
- No colored-border cards just to make sections look interesting.
- No grain/noise texture over gradients.
- No low-contrast dark-mode aesthetic.
- Avoid excessive rounded cards and pill containers.
- Do not put every piece of content inside a card.
- Use whitespace and typography to create hierarchy instead of decoration.
- Prefer restrained, product-specific visual language over generic "AI startup" styling.

## 2. Typography
- Do not automatically use Inter everywhere.
- Avoid the predictable Space Grotesk + Instrument Serif combination.
- Avoid oversized gradient hero typography.
- Avoid excessive serif-italic accent words.
- Do not italicize random words simply for visual interest.
- Establish a deliberate type scale for display, section title, body, metadata and labels.
- Keep body text comfortably readable.
- Maintain consistent line heights and text widths.
- Prevent awkward mobile word wrapping.
- Typography should reflect the product/individual, not current AI-design trends.

## 3. Headings and copy
- No emojis in headings.
- Avoid decorative badges above every headline.
- Do not use generic phrases such as "Transform your workflow," "Unlock the power of AI," or "Reimagine the future."
- Remove unnecessary buzzwords.
- Prefer specific statements explaining what the product actually does.
- Use evidence, outcomes, scope and concrete functionality where available.
- Do not manufacture metrics for visual impact.
- Avoid em dashes everywhere.
- Keep headings concise and meaningful.
- Every section should communicate something new rather than repeat the hero copy.

## 4. Icons
- Do not scatter Lucide icons throughout the interface by default.
- Avoid the generic "three icon boxes in a row" layout.
- Do not use Unicode symbols as fake interface icons.
- Use genuine SVG icons where an icon actually improves comprehension.
- Use official brand icons for GitHub, LinkedIn, etc.
- Do not add an icon merely because a heading looks empty.
- Keep icon styles consistent.
- Text-only navigation is acceptable and often preferable.

## 5. Cards and containers
- Cards must have a functional reason to exist.
- Avoid identical rounded cards repeated across every section.
- Avoid excessive shadows.
- Avoid glowing borders.
- Avoid colored outlines purely for decoration.
- Don't put three or four generic feature cards under every section.
- Use dividers, grids, typography and whitespace when they communicate structure better.
- Allow important content to breathe rather than boxing everything in.

## 6. Navigation
- Navigation should look intentional, not like a component-library default.
- Avoid making every navigation item a pill.
- Do not duplicate navigation labels through CSS pseudo-elements.
- Do not add arrows to every link.
- Use clear active/hover states without excessive animation.
- Social links should use proper recognizable icons.
- Desktop and mobile navigation should be intentionally designed separately.
- Test that navigation does not overflow or become cramped on small screens.

## 7. Buttons and CTAs
- Establish primary, secondary and text-link hierarchy.
- Do not make every action a large rounded pill.
- Avoid arrows on every button.
- Avoid unnecessary icons inside every CTA.
- Don't make buttons fade dramatically on hover.
- Hover behavior should provide feedback, not entertainment.
- CTA wording should describe the actual destination/action.
- Mobile touch targets must remain comfortably usable.

## 8. Animation and interaction
- No automatic fade-in-on-scroll everywhere.
- No cursor-following beam.
- No decorative mouse-following effects.
- No gratuitous parallax.
- No constant floating/bobbing elements.
- Avoid card lift animations unless interaction genuinely benefits.
- Motion should communicate state, hierarchy or navigation.
- Respect reduced-motion preferences.
- The interface must still feel complete with animation disabled.

## 9. Spacing and alignment
- Use a defined spacing system.
- Keep section spacing consistent.
- Align headings, labels and body copy to a deliberate grid.
- Avoid random padding values introduced section by section.
- Do not compensate for structural problems with dozens of CSS overrides.
- Keep related elements visually grouped.
- Separate unrelated elements clearly.
- Check left/right alignment across the entire page.
- Check that desktop columns have appropriate content widths.
- Avoid forcing large headings into narrow columns.
- Verify vertical rhythm from top to bottom.

## 10. Responsive/mobile design
- Do not simply shrink the desktop interface.
- Create an intentional mobile hierarchy.
- Test at ≤760px.
- Test narrow devices around 390px and below.
- Prevent horizontal overflow.
- Convert inappropriate desktop grids into meaningful mobile sequences.
- Keep important headlines readable without awkward breaks.
- Make metadata stack cleanly.
- Ensure cards don't become enormous empty boxes.
- Ensure buttons don't become cramped.
- Ensure header/navigation fits without collisions.
- Preserve appropriate whitespace without wasting the viewport.
- Review the actual rendered mobile page, not only CSS assumptions.

## 11. Component-library discipline
- Do not leave shadcn/ui looking untouched.
- Do not accept component-library defaults as final design.
- Adapt radius, spacing, typography and interaction patterns to the product.
- Avoid building the whole application from identical stock components.
- Components should share a design system without making every screen look identical.

## 12. Product-specific design
- The interface should reveal what this particular product/person does.
- Visual hierarchy should follow the user's actual workflow.
- Do not copy a generic SaaS landing-page structure.
- Do not copy another site's aesthetic literally.
- Use references for principles, not cloning.
- Give important domain information appropriate prominence.
- Design around real content instead of placeholder-friendly layouts.

## 13. Portfolio-specific rules
- Career identity comes before AI projects.
- Do not make the portfolio look like a startup/company homepage.
- Do not make it look like a CV poster or infographic.
- Keep professional healthcare implementations separate from personal AI projects.
- Show evidence of work instead of decorative project descriptions.
- Use scope, responsibility and outcomes to demonstrate seniority.
- Avoid overusing "Led" merely to sound senior.
- AI projects should demonstrate product thinking without overwhelming the professional career story.
- Do not invent project achievements or production maturity.
- Distinguish implemented, in development, planned, and production-ready accurately.

## 14. AI/technical project credibility
- Don't label a conventional feature as an "AI agent" just for marketing.
- Clearly distinguish deterministic logic from AI-generated output.
- Show human review/governance where relevant.
- Don't imply regulatory approval that has not occurred.
- Don't imply production readiness because a prototype works.
- Don't imply compliance because a checklist exists.
- Clearly distinguish planned controls from tested controls.
- Use real technical architecture/workflow evidence where useful.
- Avoid fake architecture diagrams made only to make the project appear sophisticated.

## 15. Final "Does this look vibecoded?" review
Before approving a screen, ask:
- Could this UI belong to 100 unrelated AI startups with only the logo changed?
- Are gradients, pills, cards, icons or animations doing work that typography and layout could do better?
- Does every section have a clear reason to exist?
- Is there obvious component-library default styling?
- Are there unnecessary badges, arrows, icons or decorative elements?
- Is the copy specific to the actual product?
- Is spacing consistent?
- Is the information hierarchy obvious within 5 seconds?
- Does mobile feel intentionally designed?
- Does desktop feel intentionally designed?
- Does it look credible to a professional/hiring manager rather than optimized for a design-trend screenshot?
- If all decorative effects were removed, would the underlying information architecture still be strong?

## Final acceptance rule
Do not approve a UI merely because it looks polished. A screen passes only when it is specific, functional, readable, consistently aligned, responsive, restrained, credible, and clearly connected to the actual product/user. The strongest final test: if changing the product name and logo would make the exact same interface suitable for dozens of unrelated AI products, the design is still too generic.
```
