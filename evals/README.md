# Behavioral Evaluation Suite

This repository has no runtime code, so its quality must be tested behaviorally.

## What to measure

1. **Trigger reliability** — does the skill activate for obvious and implicit UI requests?
2. **Coverage** — does it catch the relevant visual, UX, accessibility, responsive, state, security, privacy, and reliability issues?
3. **Evidence quality** — are findings tied to real code/behavior?
4. **False positives** — does it avoid banning valid brand/product decisions or inventing unsupported security failures?
5. **Prioritization** — does it rank blocked-task, security, accessibility, and data-loss issues above cosmetic ones?
6. **Fix quality** — when a fix is requested, does it preserve behavior and existing design-system conventions?
7. **Generation quality** — for generation cases, does output avoid generic AI patterns while remaining usable?
8. **Verification discipline** — does the agent verify changes instead of declaring success from inspection alone?
9. **Security/trust-boundary reasoning** — when relevant, does it catch client-side risks without inventing backend vulnerabilities?
10. **Scope discipline** — does it mark external verification instead of silently passing unavailable controls?

## Scoring

Score only dimensions that are relevant to the case:
- 0 = missed / incorrect
- 1 = partial
- 2 = strong
- N/A = dimension is not meaningfully exercised by this case

Do **not** give an irrelevant dimension a zero.

Calculate:
`normalized score = points earned / maximum applicable points`

Example: if 6 dimensions apply, the maximum is 12 rather than 20.

## Critical dimensions

Predeclare mandatory assertions for each case before running it. A missed mandatory assertion fails the case even if its aggregate score is high; do not hide omissions inside partial credit.

For trigger cases, predeclare at least three paraphrases per case and record every attempt, including failures to load the skill. Report loaded/attempted and end-to-end successful/attempted counts separately from quality conditional on loading. Never discard non-loaded attempts from the denominator. Record full-folder versus paste-only delivery explicitly.

A case fails regardless of normalized score if it scores 0 on a dimension that is central to that case, such as:
- trigger reliability for trigger cases;
- blocked-task/accessibility prioritization for accessibility cases;
- security/trust-boundary reasoning for security cases;
- false-positive control for intentional-exception cases;
- verification discipline for claims that require runtime evidence;
- scope discipline for backend/runtime controls unavailable to the reviewer.

## Minimum release bar

Before claiming the skill is validated:
- run every case in `cases.md` on at least two compatible agents/models;
- each agent's aggregate normalized score must be >= 80%;
- combined aggregate normalized score must be >= 85%;
- no critical case may fail its central dimension;
- false-positive cases must pass;
- generation cases must be inspected at desktop and narrow mobile widths when the agent can render/execute UI;
- security cases must distinguish confirmed findings from controls requiring external verification.

Record agent/model/version, date, environment, whether rendering/execution was available, and any unavailable verification surface.

## Evaluation result template

For each case record:
- Case ID
- Applicable dimensions
- Score by dimension
- Normalized %
- Critical pass/fail
- Observed behavior
- Gap found
- Skill change required
- Retest result
- Mandatory assertion outcomes and all trigger attempts
- Delivery mode, exact source commit, prompt, raw output, scorer rationale, and limitations

## Portable preparation

After checking available model quota, prepare a run in a new directory outside the source repository:

```bash
python scripts/prepare_evals.py --client claude --mode full --output /tmp/anti-ui-eval-full
python scripts/prepare_evals.py --client codex --mode paste --output /tmp/anti-ui-eval-paste
```

Use `--skill-root` to supply another installed bundle and `--cases B1 B4 B5 P7 V1 V2 V3 V4` for a focused run. Existing output directories are refused. Historical raw results remain untouched; only their input fixture definitions are reused. Each run prepares all manifest cases, three trigger paraphrases per trigger case, three B5 logging prompts, and three separate V4 subruns. `run.json` records every predetermined attempt as Not run and hashes the actual skill files.

Launch the intended client inside each `tasks/<attempt>` directory with the corresponding `prompts/<attempt>.txt`. Keep the ledger, expected assertions and scorer outside the task's context. Record exact model/client version, raw output and whether the skill actually loaded. Failed or blocked invocations stay in the denominator. No CLI/model is invoked by the preparation script; paid execution requires a quota check and the intended client environment. Score only after recording actual outputs.

The original historical harness remains preserved as historical evidence; use this portable script for new preparation.

## Evaluation rule

Do not tune the skill only to the fixtures. Add new cases whenever a real review reveals a missed class of issue.
