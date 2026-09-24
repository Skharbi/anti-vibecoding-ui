# HANDOVER.md
Last updated: 2026-09-24 | By: ChatGPT | Session goal: Harden anti-vibecoding-ui into an engineering-grade UI/UX skill

## 1. What this is
- Purpose: Reusable agent skill for generating/reviewing UI while avoiding generic AI design patterns and enforcing production UI quality.
- Users: Developers, designers, product builders, and AI coding agents.

## 2. Current state
- Works (verified): root portable `plugin.json` and Codex compatibility manifest are present; installable skill is self-contained under `skills/anti-vibecoding-ui/`; skill description is within OpenAI's 1,024-character limit; package/version/docs consistency checks pass in direct branch audit.
- Enhanced on branch `chatgpt/skill-hardening-v2`: portable Agent Plugins package v0.2.0, Codex compatibility manifest, broader UI engineering protocol, 38-section checklist, review/component/security/best-practice references, 42-case eval suite, deterministic validator, and full install/security/contribution/release/support documentation.
- Broken / flaky: no known release-blocking repository defect. Chromium runtime evidence is recorded and the independent Floot/Gemini validation is complete.
- Independent Claude run (2026-09-24, `evals/results/2026-09-24-claude-independent.md`): 95.6% aggregate, 0 critical failures, PASS. It lists non-blocking follow-ups: legal-conclusion overreach, memory-sourced advisory/compatibility claims, the full-audit coverage table not being enforced, likely-vs-must-fix severity, and corrections to the G1/G3 runtime fixture record.
- Half-done: none for v0.2.0 release validation. Publication visibility/tagging are distribution actions, not validation gaps.

## 3. Architecture
- Stack: Markdown-only installable Agent Skill with no runtime dependencies; repository QA includes one standard-library Python validator.
- Entry point: `skills/anti-vibecoding-ui/SKILL.md`
- Data flow: user UI request → skill trigger → checklist/protocol references → review/generation → verification output.
- External deps / APIs / keys: none.

## 4. Decisions & why
| Decision | Reason | Rejected alternative |
|---|---|---|
| Keep installed skill runtime dependency-free | Portability and low install friction | Adding runtime dependencies to the skill package |
| Use WCAG 2.2 AA as default accessibility target | Current broadly applicable baseline | Visual-only review |
| Separate checklist from protocol | Avoid bloated execution instructions | One monolithic SKILL.md |
| Add behavioral eval fixtures | Skills must be validated by behavior, not build success | Claiming validation from syntax/package checks |
| Preserve justified exceptions | Prevent dogmatic anti-pattern matching | Blanket bans on gradients/cards/animation |

## 5. Hard rules
- No new runtime libraries without a demonstrated need.
- No unrelated repository rewrites.
- Do not turn aesthetic preferences into accessibility/engineering claims.
- Prefer primary standards for accessibility, cybersecurity, privacy, secure development, and performance guidance.
- No fabricated validation claims.
- Update evaluation fixtures when a real failure mode is discovered.

## 6. Known traps
- The skill can over-trigger on backend-only tasks if the description becomes too broad.
- A very long checklist can produce noisy output; the review protocol requires prioritization.
- ARIA should not be added when native semantics already solve the problem.
- "Anti-vibecoding" must not become "ban modern design patterns."
- Do not claim backend/runtime security controls fail merely because frontend evidence is unavailable.
- Do not claim OWASP/ASVS/security/privacy/accessibility/performance compliance from static inspection.

## 7. Next task
- Task: Publish/distribute v0.2.0 when desired. Keep future behavior changes behind the same validator, 42-case regression suite, independent-model gate, and execution gate.
- Done when: repository visibility/release distribution matches the owner's publication choice. v0.2.0 validation itself is complete.
- Files allowed to touch: `evals/*`, `skills/anti-vibecoding-ui/*` only when an evaluation exposes a concrete defect, and `HANDOVER.md`.

## 8. How to verify
- Run: `python scripts/validate_skill.py`, then install/load the skill using a supported client workflow.
- Test: execute all cases in `evals/cases.md`.
- Expected output: prioritized evidence-based findings, correct exceptions, accessibility/blocked-task issues outrank cosmetic issues, and generation output is verified on desktop + narrow mobile.
