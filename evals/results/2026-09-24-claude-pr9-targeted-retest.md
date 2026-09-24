# PR #9 Targeted Retest — Claude

Date: 2026-09-24
Evaluator: Claude (session model `claude-opus-5-5`), Claude Code 2.1.282
PR: #9 "Apply Claude validation follow-ups", head `6531de4` (branch `chatgpt/claude-followups-v0.2.0`)
Baseline: `evals/results/2026-09-24-claude-independent.md` (commit `0ee2840`)
Evaluation type: Targeted post-fix regression retest

## Method

- **Same harness, fixtures and prompts as the baseline.** See `2026-09-24-claude-independent/harness/`.
- **Skill under test:** copied from the PR #9 head as a project skill.
- **Blind run:** the agent sees only the user prompt and the fixture. The skill is never named.
- **Tool permissions:** same as the baseline.
  - P1 had WebSearch and WebFetch.
  - S7 and S9 had no web tools, so they test labelling, not lookup.
- **Cases (21):**
  - the 10 required cases: F1, F3, R9, S6, S7, S9, B1, B4, B5, P1;
  - a critical security and false-positive subset: S1, S2, S3, S4, S8, S10, P5, P7, R7, F2, B3. These could have been weakened by the new rule that only Confirmed evidence justifies a must-fix.
- **B5:** the first B5 run did **not** trigger the skill. B5 was re-run twice (B5b, B5c); both triggered. B5 is scored on the skill-loaded runs.
- **Transcripts:** `2026-09-24-claude-pr9-targeted-retest/`.
- **Package check:** `python scripts/validate_skill.py` passes on the PR head.

## Summary

- Cases tested: 21 (10 required + 11 critical subset)
- Critical failures: **0**
- New false positives: **0**
- Targeted aggregate: **97.1%** (132 / 136)
- Required-10 subset: **95.3%** (61 / 64). The same 10 cases scored 81.3% (52 / 64) in the baseline.
- Critical subset: **98.9%** (71 / 72)

| Case | Dimensions (score) | Normalized | Baseline | Critical |
|---|---|---|---|---|
| F1 | FP 2, Prio 2, Evid 2 | 100% | 83.3% | PASS |
| F3 | FP 2, Fix 2, Ver 2 | 100% | 83.3% | PASS |
| R9 | Cov 2, Evid 2, Prio 2, Ver 1 | 87.5% | 87.5% | PASS |
| S6 | Sec 2, Scope 2, Prio 2 | 100% | 83.3% | PASS |
| S7 | Scope 2, Sec 2, Evid 2 | 100% | 83.3% | PASS |
| S9 | Sec 2, Scope 2, Evid 2 | 100% | 66.7% | PASS |
| B1 | Cov 1, Scope 2, Ver 2, Fix 2 | 87.5% | 75.0% | PASS |
| B4 | Cov 2, Scope 1, Prio 2 | 83.3% | 83.3% | PASS |
| B5 | Sec 2, Fix 2, Scope 2 | 100% | 83.3% | PASS |
| P1 | Cov 2, Ver 2, Evid 2 | 100% | 83.3% | PASS |
| S1 | Sec 2, Scope 2, Evid 2, Prio 2 | 100% | 100% | PASS |
| S2 | Sec 2, Evid 2, Prio 2, Fix 2 | 100% | 100% | PASS |
| S3 | Sec 2, Scope 2, Prio 2 | 100% | 100% | PASS |
| S4 | Sec 2, Scope 2, Evid 2 | 100% | 100% | PASS |
| S8 | Sec 2, Scope 2, Prio 2 | 100% | 100% | PASS |
| S10 | Sec 2, Prio 2, Evid 2 | 100% | 100% | PASS |
| P5 | Sec 2, Scope 2, Evid 2 | 100% | 100% | PASS |
| P7 | Sec 2, Cov 2, Prio 1 | 83.3% | 100% | PASS |
| R7 | FP 2, Cov 2, Evid 2, Prio 2 | 100% | 100% | PASS |
| F2 | FP 2, Evid 2, Prio 2 | 100% | 100% | PASS |
| B3 | Prio 2, Ver 2, Cov 2 | 100% | 100% | PASS |

## Case Results

### F1 — justified cards

Relevant dimensions:
- FP
- Prio
- Evid

Scores:
- FP: 2
- Prio: 2
- Evid: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Verdict changed from Fail (baseline) to **"Pass with issues. Nothing I can confirm is a must-fix."**
- Close-without-confirm, focus loss and the UTC date-only bug are now labelled "Should-fix / needs verification" or "Should-fix / likely". Each says what would upgrade it to must-fix.
- The cards were not flagged; they were praised as utilitarian and task-specific.

Regression found: None.

### F3 — native browser behavior

Relevant dimensions:
- FP
- Fix
- Ver

Scores:
- FP: 2
- Fix: 2
- Ver: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- **Kept native `disabled`.** In the baseline it was swapped for `aria-disabled`.
- Mentioned `aria-disabled` only as a conditional option, to use if screen-reader testing shows focus problems.
- Made one minimal fix: clear the status before saving so identical results are re-announced.
- Added no roles and no key handlers. Verified in the diff.

Regression found: None.

### R9 — RTL/localization

Relevant dimensions:
- Cov
- Evid
- Prio
- Ver

Scores:
- Cov: 2
- Evid: 2
- Prio: 2
- Ver: 1

Normalized score: 87.5%

Critical result: PASS

Observed behavior:
- The date fix now specifies `calendar: "gregory"`, `numberingSystem: "latn" | "arab"` and `timeZone` explicitly, "rather than relying on browser defaults".
- It flagged the date-only UTC shift as "needs checking".
- Calendar and digit choice are raised as product judgment calls.
- Logical properties, icon mirroring, plurals, `<bdi>` and truncation are all still covered.
- Bash was available, but it did not render (disclosed). This is unchanged from the baseline.

Regression found: None. The locale handling improved as intended; the verification gap is unrelated to PR #9.

### S6 — telemetry leak

Relevant dimensions:
- Sec
- Scope
- Prio

Scores:
- Sec: 2
- Scope: 2
- Prio: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The exposure of PHI and national ID to a third-party beacon is still a confirmed **must-fix**.
- The legal framing is now explicit: "I can't say from the code whether this breaks HIPAA, GDPR or any other rule. That depends on where you operate and on any agreement with the analytics vendor."
- The baseline's "very likely a reportable breach" statement is gone.

Regression found: None.

### S7 — security headers not visible

Relevant dimensions:
- Scope
- Sec
- Evid

Scores:
- Scope: 2
- Sec: 2
- Evid: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- No claim that CSP or HSTS are missing. Headers are listed under "Needs deployment check".
- The Vite advisory is now labelled "Known vulnerabilities (unchecked) … From memory". It gives no CVE IDs as fact and is conditional on the dev server being exposed.
- It produced a domain coverage table even though this isn't a full audit.

Regression found: None.

### S9 — supply-chain overreach

Relevant dimensions:
- Sec
- Scope
- Evid

Scores:
- Sec: 2
- Scope: 2
- Evid: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The only must-fix is the **confirmed** empty lockfile, with no integrity hashes.
- The Next 14.2.15 / CVE-2025-29927 item moved to **"Needs checking urgently (from memory, not checked this session)"**.
- It tried to verify against the npm advisory API and WebFetch; both were blocked by permissions.
- The Fail verdict rests only on the confirmed item.

Regression found: None.

### B1 — full production audit

Relevant dimensions:
- Cov (domain accounting)
- Scope
- Ver
- Fix

Scores:
- Cov: 1
- Scope: 2
- Ver: 2
- Fix: 2

Normalized score: 87.5%

Critical result: PASS

Observed behavior:
- It now **loads `best-practices-matrix.md` and `checklist.md`**. The baseline loaded neither.
- It **produced a Coverage table**: reviewed, needs checking, and not applicable (SEO, AI).
- It did not claim production-ready. Backend items were handed off explicitly.

Regression found: None.

Residual (non-blocking):
- The table has 7 grouped rows. It does not account for every matrix domain; Performance, Design systems, Internationalization and Regulated workflows are absent or implicit.
- SKILL.md now says "classify **every domain**", so this is partial compliance with the new rule. The core behaviour (coverage accounting produced) is met.

### B4 — privacy/compliance overreach

Relevant dimensions:
- Cov
- Scope
- Prio

Scores:
- Cov: 2
- Scope: 1
- Prio: 2

Normalized score: 83.3%

Critical result: PASS (it did not claim compliance)

Observed behavior:
- Better caveats: "I can't give a legal opinion because I don't know which jurisdictions you serve, and my regulatory references below are from memory."
- The must-fix items are confirmed technical facts: analytics loads before consent, there is no reject option, and contrast fails.
- **However:** the headline still says "almost certainly doesn't meet the GDPR/ePrivacy consent rules". A finding heading states "is not valid consent under GDPR", citing EDPB and CJEU guidance from memory.

Regression found: None; same score as the baseline.

Residual (non-blocking):
- The new negative-direction rule is only partly followed here: the legal characterisation is still asserted in headings, though now caveated. The verdict itself rests on confirmed technical findings.

### B5 — observability vs sensitive data

Relevant dimensions:
- Sec
- Fix
- Scope

Scores:
- Sec: 2
- Fix: 2
- Scope: 2

Normalized score: 100% (skill-loaded runs B5b and B5c)

Critical result: PASS

Observed behavior:
- Both skill-loaded runs recommend typed, allowlisted and redacted diagnostics rather than removing logging.
- PCI is framed as a scope risk: "very likely brings them into PCI DSS scope; your compliance owner should confirm", and "check this against your actual PCI scope".
- The baseline's "reportable data exposure" wording is gone.

Regression found: None attributable to PR #9.

Trigger observation (non-blocking):
- The first B5 run did not invoke the skill; 2 of 3 runs did.
- PR #9 does not change the skill description, so this is sampling variance on a borderline "client-side error logging" prompt, not a diff regression. It is worth a trigger-reliability case in a future release.

### P1 — unsupported modern feature

Relevant dimensions:
- Cov
- Ver
- Evid

Scores:
- Cov: 2
- Ver: 2
- Evid: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- **Used WebFetch** to try MDN and caniuse; the proxy blocked it.
- It then labelled browser support **"Needs verification first … From memory"** and said which part is certain (the code crashes wherever `navigation` is missing) and which is unverified (which of the target browsers lack it).
- The Fail rests on six confirmed code defects: no initial render, `?step=undefined`, a stale step on Back, skipped validation, focus reset, and a race.

Regression found: None.

### S1 — hidden admin control

Relevant dimensions:
- Sec
- Scope
- Evid
- Prio

Scores:
- Sec: 2
- Scope: 2
- Evid: 2
- Prio: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- "Only the browser checks admin" is now "[Needs verification · high impact]". That is exactly the expected handling: the client check is not authorization, and server enforcement is marked for verification.
- The Fail is supported by a confirmed must-fix: irreversible delete with no confirmation and silent failure.
- Security strictness is kept.

Regression found: None.

### S2 — unsafe rich content

Relevant dimensions:
- Sec
- Evid
- Prio
- Fix

Scores: 2 / 2 / 2 / 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The stored XSS through `marked` into `dangerouslySetInnerHTML` is still must-fix and ranked first.

Regression found: None.

### S3 — sensitive browser storage

Relevant dimensions:
- Sec
- Scope
- Prio

Scores: 2 / 2 / 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Four confirmed must-fix items: stale PHI after logout, persistent PHI, error bodies cached as records, and failed login treated as success.
- The localStorage token moved to should-fix, "depends on the token's lifetime, which I couldn't check". That is correct separation, not weakening.

Regression found: None.

### S4 — open redirect

Relevant dimensions:
- Sec
- Scope
- Evid

Scores: 2 / 2 / 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The open redirect plus `javascript:` scheme is still must-fix.
- CSRF and cookie handling are listed under backend checks.

Regression found: None.

### S8 — AI output as action input

Relevant dimensions:
- Sec
- Scope
- Prio

Scores: 2 / 2 / 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Three confirmed trust-boundary must-fix items: HTML injection from model output, model-chosen API calls, and model-chosen navigation.
- CSRF and server authorization are "Needs verification".
- It produced a coverage table.

Regression found: None.

### S10 — fail-open exceptional condition

Relevant dimensions:
- Sec
- Prio
- Evid

Scores: 2 / 2 / 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The fail-open permission check is still must-fix #1.
- The unencoded ID is should-fix, explicitly unconfirmed.
- Spacing is ranked last.

Regression found: None.

### P5 — API response trusted as authority

Relevant dimensions:
- Sec
- Scope
- Evid

Scores: 2 / 2 / 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- "The client-side flaw is confirmed. Whether it can actually be exploited depends on the server, which needs checking."
- Backend authorization, pricing and CSRF are in a verification section.

Regression found: None.

### P7 — cross-user cache leak

Relevant dimensions:
- Sec
- Cov
- Prio

Scores:
- Sec: 2
- Cov: 2
- Prio: 1

Normalized score: 83.3%

Critical result: PASS

Observed behavior:
- The cross-account cache leak and the ignored failed switch are both confirmed must-fix.
- Finding #3 (`text/plain` body) was raised to must-fix on the assumption that "a server expecting JSON … will read an empty body". The header fact is confirmed; the effect depends on the server, so under the new rule it should be should-fix or needs verification.
- The Fail is independently supported by the two confirmed items.

Regression found:
- Minor severity slip, non-blocking. It is not a false positive: the finding is accurate, only its severity is slightly high.

### R7 — intentional brand exception

Relevant dimensions:
- FP
- Cov
- Evid
- Prio

Scores: 2 / 2 / 2 / 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The gradient and pills were treated as fixed by the brand.
- The only must-fix is the **calculated** "See fees" contrast failure (about 2.1:1).
- Mobile contrast and overflow are now labelled "likely, not rendered" and kept as should-fix. The baseline had these as must-fix.

Regression found: None.

### F2 — justified animation

Relevant dimensions:
- FP
- Evid
- Prio

Scores: 2 / 2 / 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The animation was kept, and the reduced-motion check was credited.
- The single must-fix, the live region announcing the wrong item, is labelled "Confirmed in code".
- A Safari list-semantics claim is explicitly marked "haven't checked this against current Safari".

Regression found: None.

### B3 — accessibility lint only

Relevant dimensions:
- Prio
- Ver
- Cov

Scores: 2 / 2 / 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Focus-in and focus-return, non-modal behaviour, and Escape are still must-fix, "confirmed from the code".
- Lint is not accepted as sign-off.
- Reflow is labelled "likely, I haven't seen it rendered".

Regression found: None.

## Verification of PR #9 goals

| Goal | Result | Evidence |
|---|---|---|
| No must-fix/Fail from "Likely" or memory alone | Met; one minor slip | F1, R7, S9, P1 downgraded correctly. P7 #3 is a small slip, with the Fail supported by confirmed items. |
| Time-sensitive claims verified or labelled | Met | S7, S9, P1, F2 all label memory-based claims. P1 and S9 attempted lookups. |
| Unverified memory claims clearly labelled | Met | "from memory, not checked this session" (S9), "unchecked … From memory" (S7) |
| No legal non-compliance/breach conclusion as fact | Mostly met | S6 and B5 fixed. B4 still asserts GDPR invalidity in headings, with caveats. |
| Confirmed security issues still strict | Met | S1–S4, S8, S10, P5, P7 keep confirmed must-fix items and Fail verdicts. |
| Frontend vs backend/runtime separation | Met | Every security case has explicit needs-verification sections. |
| Full-audit coverage accounting | Met (partial granularity) | B1 produces a coverage table. It is grouped rather than per matrix domain. |
| Native `disabled` vs `aria-disabled` | Met | F3 keeps native `disabled`; `aria-disabled` is conditional only. |
| Arabic/RTL calendar, numbering system, timezone | Met | R9 sets calendar, numbering system and timezone explicitly, and flags the date-only UTC shift. |
| No new false positives / no weakening | Met | False-positive cases F1, F2, F3, R7 are all at 100%. No security case weakened. |

## Non-blocking observations

1. **B1:** the coverage table groups domains; it doesn't list every row of `best-practices-matrix.md`. A future tweak could ask for one row per matrix domain.
2. **B4:** GDPR invalidity is still stated in headings. The caveat is present, but the new negative-direction rule is not fully followed.
3. **P7:** a server-dependent effect (`text/plain` body) was rated must-fix.
4. **B5 trigger variance:** 1 of 3 runs did not load the skill. PR #9 doesn't change the description; consider a trigger case for client-side logging and observability prompts.
5. **Process:** AGENTS.md asks behaviour changes to update or add a case in `evals/cases.md`. PR #9 changes behaviour but adds no regression case (for example, legal-conclusion restraint, or memory-claim labelling).
6. **R9:** the agent still didn't render even though Bash was available. This is unchanged from the baseline and unrelated to PR #9.
7. **Limitations:** same model family as agent and scorer; one sample per case (three for B5); static review cases only. No new browser execution was needed, because PR #9 changes no rendering fixtures.

## Merge criteria check

- **No tested case has a critical failure:** met (0).
- **No new false positive:** met.
- **Targeted aggregate ≥ 80%:** met (97.1%).
- **Security findings stay strict when evidence is confirmed:** met.
- **Speculative/unverified findings downgraded to verification requests:** met, with one minor P7 slip.
- **Full-audit coverage accounting produced when required:** met (B1).

PASS — PR #9 targeted regression bar met. Safe to merge.
