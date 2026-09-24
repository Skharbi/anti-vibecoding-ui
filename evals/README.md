# Behavioral Evaluation Suite

This repository has no runtime code, so its quality must be tested behaviorally.

## What to measure

1. **Trigger reliability** — does the skill activate for obvious and implicit UI requests?
2. **Coverage** — does it catch visual, UX, accessibility, responsive, and state issues rather than only styling?
3. **Evidence quality** — are findings tied to real code/behavior?
4. **False positives** — does it avoid banning valid brand/product decisions?
5. **Prioritization** — does it rank blocked-task/accessibility issues above cosmetic ones?
6. **Fix quality** — do fixes preserve behavior and existing design-system conventions?
7. **Generation quality** — does new UI avoid generic AI patterns while remaining usable?
8. **Verification discipline** — does the agent verify changes instead of declaring success from code inspection alone?

## Scoring

Score each case 0–2:
- 0 = missed / incorrect
- 1 = partial
- 2 = strong

Recommended dimensions:
- trigger
- coverage
- evidence
- prioritization
- false-positive control
- fix quality
- verification

Total per case: 14.

## Minimum release bar

Before claiming the skill is validated:
- run every case in `cases.md` on at least two compatible agents;
- average score >= 11/14;
- no case may score 0 on accessibility/blocked-task prioritization;
- false-positive control must pass the intentional-brand exceptions;
- generation cases must be inspected at desktop and narrow mobile widths.

Record agent/model/version and date because behavior changes over time.

## Evaluation rule

Do not tune the skill only to the fixtures. Add new cases whenever a real review reveals a missed class of issue.
