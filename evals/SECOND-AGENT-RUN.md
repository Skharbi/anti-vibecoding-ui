# Independent Second-Agent Validation Packet

Use this packet with a **different model/agent family** from the one that authored the current self-test.

## Goal

Validate whether anti-vibecoding-ui behaves correctly across the full versioned case manifest without being biased by the authoring model. The current manifest contains 46 cases.

## Required setup

Provide the independent scorer access to:
- `skills/anti-vibecoding-ui/`
- `evals/README.md`
- `evals/cases.md`
- `evals/EXECUTION-GATE.md`

Do **not** give the second agent the existing self-test conclusions before it completes its own scoring.

Keep the agent performing each task separate from the scorer. Task agents receive only isolated fixtures, prompts and the intended full-folder or portable delivery. Expected assertions, old results and the rubric belong outside their task directories. Use `scripts/prepare_evals.py` to prepare inputs and a predetermined attempt ledger; preparation does not execute agents or satisfy any release gate.

## Evaluation instruction

1. Load the skill exactly as a user would.
2. Run every case in `evals/cases.md`.
3. Score only applicable dimensions using the rubric in `evals/README.md`.
4. For each case record:
   - case ID;
   - applicable dimensions;
   - score by dimension;
   - normalized percentage;
   - critical pass/fail;
   - observed behavior;
   - gap found;
   - required skill change, if any.
5. Treat unavailable runtime/backend evidence as **Needs verification**, not pass.
6. Do not use the existing GPT-5.6 Sol self-test as a scoring reference.
7. Run the execution-gated cases using `evals/runtime-fixtures/` plus real browser/device evidence where possible.
8. Save the result under `evals/results/YYYY-MM-DD-<agent>-independent.md`.

## Release bar

The independent run must satisfy:
- agent aggregate normalized score >= 80%;
- combined aggregate across both agents >= 85%;
- no critical case fails its central dimension;
- false-positive cases pass;
- security cases distinguish confirmed client findings from backend/runtime verification needs;
- rendered/browser/device cases have actual execution evidence before being marked PASS.

## Stop condition

Do not edit the skill while scoring.

After the independent run is complete:
1. list failures;
2. patch only concrete failures;
3. add/update regression cases when a new failure class is discovered;
4. rerun only affected cases plus the full critical-case subset;
5. update `HANDOVER.md`.
