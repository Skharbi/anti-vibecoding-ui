# Component Behavior Reference

Use this to review common interactive components. Prefer native HTML where possible. For custom widgets, follow established accessibility patterns.

## Button
- Use a real `button` for actions.
- Enter/Space activate.
- Disabled state must match actual behavior.
- Toggle buttons expose pressed state when the label remains constant.
- Loading actions prevent duplicate execution when appropriate.

## Link
- Use an `a` element for navigation.
- Destination/action wording should be understandable.
- Do not use a link styled as a button if it actually performs a non-navigation action without matching semantics.

## Dialog / modal
- Move focus into the dialog when it opens.
- Keep keyboard focus within a modal while open.
- Escape closes when dismissible.
- Provide an accessible name.
- Background content must not remain interactable for a true modal.
- Return focus to a logical trigger/next location after close.
- Ensure the dialog fits narrow/short viewports.

## Drawer / sheet
- Treat modal drawers like dialogs.
- If non-modal, do not trap focus.
- Preserve a clear close affordance.
- Avoid covering the only route back to primary content.

## Tooltip
- Supplemental only; do not put essential information exclusively in a tooltip.
- Must be reachable for keyboard users if hover reveals meaningful content.
- Must not require precise pointer movement to stay open.

## Popover
- Define whether it behaves as modal or non-modal.
- Trigger exposes open state where appropriate.
- Focus movement must match the interaction.
- Outside-click behavior must not make keyboard use unreliable.

## Menu button
- Trigger is a button.
- Expose popup/open state.
- Enter/Space open.
- Menu items support expected keyboard movement.
- Escape closes and restores focus.

## Tabs
- Tablist, tab, and tabpanel relationships are explicit.
- Selected state is exposed.
- Arrow-key behavior is used when implementing an ARIA tab widget.
- Decide automatic vs manual activation intentionally.
- Hidden panels are not focusable.

## Accordion
- Trigger is a button in a heading context where appropriate.
- Expanded/collapsed state is exposed.
- Collapsed content is not accidentally focusable.
- Do not use accordions to hide content that users constantly need.

## Combobox / autocomplete
- Prefer established accessible primitives/library implementations.
- Keyboard users can move through options and commit a value.
- Highlighted/selected states are distinct.
- Async search provides loading/no-results/error feedback.
- Free-text vs constrained selection behavior is clear.

## Checkbox / radio / switch
- Labels are clickable and programmatically associated.
- Use checkbox/radio for native selection semantics.
- Use switch only for immediate on/off settings, not arbitrary binary choices.
- Selected/checked state is visible without relying on color alone.

## Toast / notification
- Do not steal focus for passive status.
- Announce important async status appropriately.
- Critical errors should not disappear before they can be understood.
- Do not use toast as the only record of a consequential action.

## Form field
- Persistent label.
- Help text before failure where useful.
- Error message specific and associated with field.
- Preserve entered value after recoverable error.
- Use appropriate type/autocomplete/inputmode.

## Data table
- Use semantic table structure for tabular data.
- Header relationships are clear.
- Sort direction is visible and exposed.
- Row actions are keyboard reachable.
- Responsive strategy prioritizes columns rather than blindly squeezing.

## Pagination / infinite list
- Preserve position/context after page changes when appropriate.
- Announce major result-set changes if needed.
- Infinite loading must not make footer/navigation permanently unreachable without an alternative.
- Provide a recoverable error state.

## Drag and drop
- Never make drag the only way to complete an essential task.
- Provide keyboard-accessible alternative controls.
- Drop targets and resulting state must be clear.
- Announce successful moves when needed.

## Date/time picker
- Native controls are acceptable when they meet product needs.
- Custom pickers require strong keyboard support.
- Locale/date formatting must be clear.
- Do not require pointer-only calendar navigation.

## File upload
- Label accepted types/size limits before submission.
- Drag/drop has a standard file-picker alternative.
- Upload progress, success, failure, retry, and removal states are clear.
- File errors identify the specific file/problem.

## Search/filter
- Search intent and scope are clear.
- Empty query and no-result states are distinct.
- Active filters remain visible.
- Clear-all is easy when multiple filters are active.
- URL/state persistence is considered when users need to share or revisit results.
