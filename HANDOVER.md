# HANDOVER.md
Last updated: 2026-09-24 | By: ChatGPT | Session goal: Harden anti-vibecoding-ui into an engineering-grade UI/UX skill

## 1. What this is
- Purpose: Reusable agent skill for generating/reviewing UI while avoiding generic AI design patterns and enforcing production UI quality.
- Users: Developers, designers, product builders, and AI coding agents.

## 2. Current state
- Works (verified): skill packaging exists; SKILL.md and references load from `skills/anti-vibecoding-ui/`; README install path matches repository structure.
- Enhanced on branch `chatgpt/skill-hardening-v2`: broader UI engineering protocol, 38-section checklist, review protocol, component behavior reference, primary-source references, cybersecurity/trust reference, cross-domain best-practices matrix, behavioral eval suite.
- Broken / flaky: independent second-agent and rendered/browser/device evaluation are not yet recorded. A GPT-5.6 Sol structural/scenario self-test is recorded under `evals/results/`. GitHub-hosted Actions on this private repo failed before any job step started, so the unusable auto workflow was removed rather than leaving a permanently red check.
- Half-done: policy-level gap hardening and a 42-case self-test are complete; six cases remain execution-dependent, and the required independent second-agent run is outstanding.

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
- Task: Run the 42-case suite with a second compatible agent/model and execute the six render/browser/device-dependent cases. Before any merge, run `python scripts/validate_skill.py` in a repository checkout.
- Done when: eval results are recorded with agent/model/date; release bar in `evals/README.md` is met or failures are documented and fed back into the skill.
- Files allowed to touch: `evals/*`, `skills/anti-vibecoding-ui/*` only when an evaluation exposes a concrete defect, and `HANDOVER.md`.

## 8. How to verify
- Run: `python scripts/validate_skill.py`, then install/load the skill using a supported client workflow.
- Test: execute all cases in `evals/cases.md`.
- Expected output: prioritized evidence-based findings, correct exceptions, accessibility/blocked-task issues outrank cosmetic issues, and generation output is verified on desktop + narrow mobile.
