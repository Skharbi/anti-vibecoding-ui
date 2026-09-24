# Anti-Vibecoding UI/UX Checklist

Use this as a **production UI review/generation checklist**, not a style scorecard. Apply only relevant items. Evidence beats opinion.

## 1. Product fit and information architecture
- [ ] The primary user and primary task are obvious.
- [ ] The page hierarchy follows the user's workflow, not a generic SaaS template.
- [ ] Important domain information is more prominent than decorative content.
- [ ] Related actions and information are grouped logically.
- [ ] Secondary content does not compete with the primary task.
- [ ] The page has a clear beginning, progression, and endpoint where appropriate.
- [ ] Navigation labels match user language, not internal terminology.
- [ ] Breadcrumbs, back behavior, and deep links are predictable where needed.
- [ ] The UI works with realistic content volume, not only ideal demo content.
- [ ] The product can still be identified from structure and workflow if branding is removed.

## 2. Visual style and brand fit
- [ ] No purple-to-blue gradient unless genuinely required by the brand.
- [ ] No gradient headline text by default.
- [ ] No glassmorphism cards by default.
- [ ] No colored-border cards or glows used purely to create visual interest.
- [ ] No grain/noise texture used as a generic "premium" effect.
- [ ] Avoid low-contrast dark-mode aesthetics.
- [ ] Avoid excessive rounded cards and pill containers.
- [ ] Do not put every piece of content inside a card.
- [ ] Use whitespace, type, alignment, and hierarchy before decoration.
- [ ] Visual language is deliberate and product-specific.
- [ ] Brand colors are used consistently and purposefully.
- [ ] Decorative treatments do not reduce readability or obscure hierarchy.

## 3. Typography
- [ ] Typography is chosen deliberately rather than defaulting to trendy AI/startup pairings.
- [ ] A defined scale exists for display, page title, section title, body, metadata, labels, and captions.
- [ ] Body text is comfortably readable.
- [ ] Line heights are consistent and appropriate.
- [ ] Line lengths are controlled for reading comfort.
- [ ] Weight is used for hierarchy rather than everywhere.
- [ ] Italics are used semantically or intentionally, not as random decoration.
- [ ] Large headings do not wrap awkwardly on common viewport widths.
- [ ] Long labels and translated strings have room to grow.
- [ ] Numeric/data typography is legible where precision matters.

## 4. Copy and content credibility
- [ ] Headings are specific and meaningful.
- [ ] No generic phrases such as "Transform your workflow" or "Unlock the power of AI" unless the product context truly justifies them.
- [ ] Buzzwords are removed where plain language is clearer.
- [ ] Buttons describe the actual action or destination.
- [ ] Empty states explain what happened and what the user can do next.
- [ ] Error messages explain the problem and recovery path.
- [ ] Metrics, outcomes, testimonials, compliance claims, and technical claims are not fabricated.
- [ ] AI-generated, deterministic, planned, tested, and production-ready capabilities are distinguished accurately.
- [ ] Regulatory or certification claims are not implied without evidence.
- [ ] Content does not repeat the same value proposition across multiple sections.

## 5. Layout, spacing, and density
- [ ] A coherent spacing scale is used.
- [ ] Section spacing is consistent.
- [ ] Alignment follows a deliberate grid.
- [ ] Related elements are visually grouped.
- [ ] Unrelated elements are clearly separated.
- [ ] Random one-off padding/margin values are minimized.
- [ ] Layout does not depend on fragile magic numbers.
- [ ] Important actions remain visible without overcrowding.
- [ ] Dense workflows stay scannable without excessive card nesting.
- [ ] Desktop columns have appropriate widths.
- [ ] Vertical rhythm remains consistent from top to bottom.
- [ ] Whitespace is useful, not wasteful.

## 6. Navigation and wayfinding
- [ ] Navigation is visually intentional and clearly distinguishable from content.
- [ ] Active/current location is clear.
- [ ] Navigation is not composed entirely of pills by default.
- [ ] Link and button semantics match behavior.
- [ ] Back/forward browser navigation behaves predictably.
- [ ] Mobile navigation is intentionally designed rather than merely collapsed.
- [ ] Nested navigation does not trap or confuse users.
- [ ] Important destinations are not hidden behind ambiguous icons.
- [ ] Navigation supports keyboard use.
- [ ] Navigation does not overflow at narrow widths.
- [ ] External links or context changes are communicated when material.

## 7. Buttons, links, and action hierarchy
- [ ] Primary, secondary, tertiary, and destructive actions are visually distinct.
- [ ] Not every action is styled as a large pill.
- [ ] Icons are not added to every CTA by default.
- [ ] Arrows are not added to every link/button by default.
- [ ] Hover states provide feedback without theatrical motion.
- [ ] Focus states are clearly visible.
- [ ] Disabled controls communicate why when needed.
- [ ] Loading/pending actions prevent accidental duplicate submission.
- [ ] Destructive actions are labeled clearly.
- [ ] Touch targets are comfortably usable.
- [ ] Links look and behave like links; buttons look and behave like actions.

## 8. Icons and imagery
- [ ] Icons are used because they improve comprehension, not to fill space.
- [ ] Icon style and stroke weight are consistent.
- [ ] Official brand icons are used for recognizable services.
- [ ] Unicode symbols are not used as fake interface icons where a real accessible icon/control is required.
- [ ] Decorative icons are hidden from assistive technology.
- [ ] Meaningful icons have accessible names when text does not already provide one.
- [ ] Image alt text is meaningful when the image conveys information.
- [ ] Decorative images use empty alt text.
- [ ] Images have appropriate dimensions/aspect handling to reduce layout shift.
- [ ] Hero/media assets do not dominate content without purpose.

## 9. Semantic HTML and document structure
- [ ] Native semantic HTML is preferred over generic div/span structures.
- [ ] Heading levels reflect document hierarchy.
- [ ] One page-level main region exists where appropriate.
- [ ] Landmarks are meaningful and not overused.
- [ ] Lists are marked up as lists when they are lists.
- [ ] Tables use table semantics when data is tabular.
- [ ] Form controls use native elements where practical.
- [ ] Buttons are buttons; links are links.
- [ ] ARIA is used only where native semantics are insufficient.
- [ ] Custom controls expose role, state, value, and accessible name correctly.

## 10. Keyboard and focus
- [ ] Every interactive control is reachable by keyboard.
- [ ] Tab order follows visual/logical order.
- [ ] No positive tabindex values are used without a compelling reason.
- [ ] Focus indicators are visible and meet the intended accessibility target.
- [ ] Focus is not removed purely for aesthetic reasons.
- [ ] Focus is moved intentionally when dialogs, drawers, or major dynamic contexts open.
- [ ] Focus returns to a logical element when overlays close.
- [ ] Keyboard shortcuts do not conflict with typing or assistive technology.
- [ ] Escape behavior is predictable for dismissible overlays.
- [ ] Roving focus or arrow-key navigation is implemented where established patterns require it.

## 11. Forms and validation
- [ ] Every input has a persistent programmatic label.
- [ ] Placeholder text is not the only label.
- [ ] Required fields are communicated visually and programmatically.
- [ ] Help text appears before errors are likely where possible.
- [ ] Validation timing avoids punishing users while they type.
- [ ] Errors are specific and actionable.
- [ ] Errors are associated with the relevant field programmatically.
- [ ] A summary is provided for complex multi-error forms where useful.
- [ ] User-entered values are preserved after recoverable errors.
- [ ] Correct input types, autocomplete values, and input modes are used.
- [ ] Password requirements are visible before submission.
- [ ] Show/hide password behavior is accessible.
- [ ] Multi-step forms show progress and preserve state.
- [ ] Success states confirm what happened and next steps.

## 12. State completeness
For every interactive or data-driven component, verify all plausible states:
- [ ] default/initial;
- [ ] hover;
- [ ] focus;
- [ ] active/pressed;
- [ ] selected/current;
- [ ] disabled;
- [ ] loading/pending;
- [ ] empty/no results;
- [ ] partial data;
- [ ] success;
- [ ] validation error;
- [ ] server/network error;
- [ ] permission denied;
- [ ] offline/retry where relevant;
- [ ] long/overflowing content;
- [ ] stale/refreshing data where relevant.

Do not invent unreachable states, but do not ship only the happy path.

## 13. Loading, empty, error, and async feedback
- [ ] Loading states preserve layout where possible.
- [ ] Skeletons are used only when they meaningfully reduce perceived wait.
- [ ] Spinners are not used without context for long operations.
- [ ] Loading text explains what is happening when the action may take time.
- [ ] Empty states distinguish "nothing exists" from "no results match filters."
- [ ] Errors distinguish validation, permission, network, and server failures where useful.
- [ ] Retry controls appear when retry is meaningful.
- [ ] Background updates do not steal focus.
- [ ] Async success/error messages are announced appropriately to assistive technology.
- [ ] Optimistic UI has a rollback/reconciliation path.
- [ ] Users are not left wondering whether an action succeeded.

## 14. Responsive and mobile behavior
- [ ] Mobile is not simply a shrunken desktop layout.
- [ ] Information priority adapts to viewport size.
- [ ] Test around 390px and below.
- [ ] Test common tablet widths.
- [ ] No accidental horizontal overflow.
- [ ] Dense grids/tables have an intentional narrow-screen strategy.
- [ ] Sticky/fixed UI does not obscure critical content.
- [ ] Dialogs/drawers fit within small viewport heights.
- [ ] Mobile browser chrome and virtual keyboards do not hide critical actions.
- [ ] Metadata stacks cleanly.
- [ ] Touch targets remain usable.
- [ ] Typography remains readable without excessive wrapping.
- [ ] Mobile navigation is coherent and discoverable.
- [ ] Orientation changes do not break the interface where relevant.

## 15. Accessibility: perceivable
- [ ] Text and essential UI contrast meet the intended accessibility standard.
- [ ] Information is not conveyed by color alone.
- [ ] Status/error/success indicators use text or another non-color cue.
- [ ] Text can zoom/reflow without loss of information or functionality.
- [ ] Content is not clipped at larger text settings.
- [ ] Images conveying text are avoided except where essential.
- [ ] Captions/transcripts exist for relevant media.
- [ ] Motion, flashing, and animation do not create avoidable accessibility barriers.

## 16. Accessibility: operable and understandable
- [ ] All functionality is keyboard operable.
- [ ] No keyboard traps exist.
- [ ] Focus order is logical.
- [ ] Focus is visible.
- [ ] Controls have understandable names.
- [ ] Repeated navigation/controls stay consistent.
- [ ] User input errors are identified and described.
- [ ] Destructive or important transactions allow confirmation, review, or recovery where appropriate.
- [ ] Time limits are avoidable, adjustable, or clearly communicated where applicable.
- [ ] Reduced-motion preferences are respected.

## 17. Dialogs, drawers, popovers, tooltips, menus, tabs, accordions
- [ ] Trigger semantics are correct.
- [ ] Open/closed state is exposed programmatically where relevant.
- [ ] Focus behavior matches the component type.
- [ ] Modal dialogs keep interaction within the modal while open.
- [ ] Escape closes dismissible overlays where expected.
- [ ] Closing returns focus logically.
- [ ] Tooltips are not the only source of essential information.
- [ ] Hover-only content is also keyboard/touch accessible.
- [ ] Menus support expected keyboard behavior.
- [ ] Tabs expose selected state and associated panels correctly.
- [ ] Accordions expose expanded state.
- [ ] Nested overlays do not create broken focus or z-index behavior.

## 18. Tables, lists, filters, and bulk workflows
- [ ] Tabular data uses semantic tables.
- [ ] Headers are clear and associated correctly.
- [ ] Sorting direction is visible and programmatically exposed.
- [ ] Filters show active state.
- [ ] Users can clear filters easily.
- [ ] "No results" differs from "no data."
- [ ] Pagination/infinite scrolling preserves context.
- [ ] Bulk selection clearly indicates scope.
- [ ] Bulk destructive actions require appropriate confirmation.
- [ ] Row actions are keyboard reachable.
- [ ] Dense tables remain usable at narrow widths.
- [ ] Columns are prioritized rather than blindly compressed.
- [ ] Large datasets are not rendered naively when it harms responsiveness.

## 19. Charts and data visualization
- [ ] The chart answers a clear question.
- [ ] Color is not the only differentiator.
- [ ] Legends and labels are understandable.
- [ ] Axes, units, ranges, and time periods are explicit.
- [ ] Truncated axes are not misleading.
- [ ] Tooltips are keyboard/touch accessible when they contain essential data.
- [ ] A textual or tabular alternative exists where accessibility requires it.
- [ ] Decorative 3D effects and chart junk are avoided.
- [ ] Data density matches the decision being supported.
- [ ] Empty/loading/error chart states are designed.
- [ ] Confidence/uncertainty is shown where materially relevant.

## 20. Destructive, irreversible, and high-impact actions
- [ ] Destructive actions are visually distinguishable but not theatrically alarming.
- [ ] Confirmation is proportional to consequence.
- [ ] Generic "Are you sure?" copy is replaced by consequence-specific wording.
- [ ] Destructive confirmation identifies the object/action.
- [ ] Undo is preferred when feasible for low-risk reversible actions.
- [ ] Double confirmation is reserved for genuinely high-impact cases.
- [ ] Disabled destructive actions explain unmet conditions when needed.
- [ ] Success and failure states are clear.
- [ ] Accidental double execution is prevented.

## 21. Authentication, permissions, and account UX
- [ ] Signed-out, unauthorized, forbidden, and expired-session states are distinct.
- [ ] Users understand why access is blocked.
- [ ] Re-authentication preserves intended destination where practical.
- [ ] Permission-dependent UI does not expose actions users cannot perform without explanation.
- [ ] Sensitive data is not unnecessarily echoed in the interface.
- [ ] Account switching/logout is predictable.
- [ ] Security-sensitive actions communicate consequence and completion clearly.

## 22. Internationalization, localization, and RTL
- [ ] Layout tolerates text expansion.
- [ ] Strings are not embedded inside graphics.
- [ ] Dates, times, numbers, currency, and pluralization are locale-aware where required.
- [ ] RTL layouts mirror directional structure appropriately.
- [ ] Directional icons/arrows behave correctly in RTL.
- [ ] Mixed LTR/RTL content remains legible.
- [ ] Truncation does not hide essential meaning.
- [ ] User-facing text is not assembled from brittle string fragments.

## 23. Performance and perceived performance
- [ ] Critical content is not delayed by decorative work.
- [ ] Images are appropriately sized and responsive.
- [ ] Dimensions/aspect ratios prevent avoidable layout shift.
- [ ] Fonts are loaded intentionally.
- [ ] Expensive scroll/mouse effects are avoided.
- [ ] Animation does not monopolize main-thread work.
- [ ] Huge lists are handled appropriately.
- [ ] Client-side rendering is not used unnecessarily for static content.
- [ ] Loading feedback matches real latency.
- [ ] Repeated requests/actions are debounced or guarded where appropriate.
- [ ] The interface remains responsive during background work.

## 24. Component-library and design-system discipline
- [ ] Existing components/tokens are reused before creating near-duplicates.
- [ ] Component-library defaults are not treated as final product design.
- [ ] Radius, spacing, typography, and interaction states align with the product system.
- [ ] Variants are explicit rather than created through scattered one-off classes.
- [ ] Shared behaviors live in shared components where appropriate.
- [ ] Design tokens are used consistently.
- [ ] One fix does not create a second competing design language.
- [ ] New components have clear API/behavior contracts.
- [ ] Visual and behavioral variants are documented or inferable.

## 25. Animation and interaction restraint
- [ ] No automatic fade-in-on-scroll everywhere.
- [ ] No cursor-following beam or decorative mouse trail.
- [ ] No gratuitous parallax.
- [ ] No constant floating/bobbing elements.
- [ ] Card lift animations are used only where they clarify interaction.
- [ ] Motion communicates state, hierarchy, spatial relationship, or causality.
- [ ] Reduced-motion mode remains fully usable.
- [ ] The interface still feels complete with animation disabled.
- [ ] Transitions are fast enough not to block task completion.

## 26. Portfolio-specific rules
- [ ] Career identity comes before AI projects.
- [ ] The portfolio does not look like a generic startup homepage.
- [ ] Professional healthcare work and personal AI projects are clearly distinguished.
- [ ] Evidence of work is stronger than decorative descriptions.
- [ ] Scope, responsibility, and outcomes demonstrate seniority.
- [ ] "Led" and similar verbs are not overused to imply authority.
- [ ] AI projects do not overwhelm the professional story.
- [ ] Implemented, in development, planned, and production-ready states are labeled accurately.
- [ ] Metrics/achievements are not invented.

## 27. AI/technical product credibility
- [ ] Conventional automation is not marketed as an "AI agent" without agentic behavior.
- [ ] Deterministic logic and model-generated output are clearly distinguished.
- [ ] Human review/governance is shown where materially relevant.
- [ ] Model uncertainty or limitations are surfaced when needed for user decisions.
- [ ] AI output has a clear correction/retry path.
- [ ] AI-generated content does not masquerade as verified fact.
- [ ] Model latency and failure states are designed.
- [ ] Sensitive/regulated use cases do not imply approval or compliance without evidence.
- [ ] Technical diagrams reflect real architecture rather than decorative complexity.

## 28. Final anti-vibecoding review
Before approval, ask:
- [ ] Could this UI belong to 100 unrelated products with only the logo and copy changed?
- [ ] Are gradients, pills, cards, icons, animation, and badges doing work that structure and typography could do better?
- [ ] Does every section have a clear reason to exist?
- [ ] Is there obvious untouched component-library styling?
- [ ] Is the information hierarchy obvious within a few seconds?
- [ ] Is the primary task obvious?
- [ ] Does the interface work with realistic error, empty, long-content, and loading states?
- [ ] Does mobile feel intentionally designed?
- [ ] Does desktop feel intentionally designed?
- [ ] Does keyboard-only use work?
- [ ] Do custom interactive components follow established accessibility behavior?
- [ ] Does the interface remain coherent with motion disabled?
- [ ] Does it look credible to a professional user rather than optimized for a trend screenshot?
- [ ] If decorative effects were removed, would the information architecture still be strong?

## Final acceptance rule

Do not approve a UI because it is polished.

A screen passes only when it is:

**Specific + usable + accessible + semantically correct + state-complete + responsive + performant + consistent + restrained + credible + clearly connected to the actual product/user.**
