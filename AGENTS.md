# AGENTS.md

Instructions for AI coding agents working in this repository.

## Read first

Before editing:
1. read `HANDOVER.md`;
2. read the target file and relevant references;
3. restate the single task internally;
4. avoid unrelated cleanup.

## Repository rules

- The installable skill is `skills/anti-vibecoding-ui/`.
- Keep that folder self-contained.
- Root `plugin.json` is the portable plugin manifest.
- `.codex-plugin/plugin.json` is a compatibility manifest and must match root name/version.
- Repository QA may use standard-library scripts, but the installed skill must remain runtime dependency-free.
- Detailed rules belong in `references/`; keep `SKILL.md` focused enough for reliable instruction following.
- Do not add an MCP server unless a workflow genuinely needs live data or controlled actions.
- Do not add dependencies merely for validation or formatting convenience.

## Behavior changes

When changing what the skill should detect, generate, prioritize, or ignore:
- update or add a case in `evals/cases.md`;
- preserve false-positive controls;
- distinguish confirmed findings from external verification;
- do not claim compliance from static inspection.

## Validation

Before finishing:

```bash
python scripts/validate_skill.py
```

Then run relevant behavioral cases. For rendering/RTL/browser-dependent changes, use `evals/EXECUTION-GATE.md`.

## Stop condition

Stop when the requested task is implemented and verified. Do not broaden scope into unrelated refactors.

Update `HANDOVER.md` when the current state or next release gate materially changes.
