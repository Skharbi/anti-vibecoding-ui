# Independent Validation — Claude

Date: 2026-09-24
Evaluator: Claude (session model `claude-opus-5-5`, last served model `claude-opus-5-5`), running in Claude Code 2.1.282
Repository commit: `0ee28402ac6394313e2669267d584e8220b5ab4e`
Evaluation type: Independent second-model validation

## Summary

- Total cases: 42
- Cases passed (all applicable dimensions at 2): 31
- Cases with partial issues: 11 (R9, G2, F1, F3, S6, S7, S9, B1, B4, B5, P1)
- Critical failures: 0
- Aggregate normalized score: **95.6%** (281 / 294 applicable points)
- Release bar met: **YES**

## Method

### How cases were run (blind)

- Each of the 42 cases got a fresh sandbox directory containing:
  - a realistic fixture written from the case's fixture characteristics;
  - an unmodified copy of `skills/anti-vibecoding-ui/`, installed as a **project skill** (`.claude/skills/anti-vibecoding-ui/`), exactly as a user would install it.
- Each case was run with headless Claude Code: `claude -p "<prompt>" --model claude-opus-5-5`.
- **The agent under test only saw the user prompt and the fixture.** It never saw the "Expected" text in `evals/cases.md`, and fixtures contain no comments that hint at the expected finding.
- The skill was **not named** in any prompt. Every trigger in this report is implicit auto-triggering.
- Tool access per case:
  - review cases: Read/Glob/Grep;
  - fix cases: also Edit/Write;
  - execution-gated cases (R3, R9, G1–G3): also Bash;
  - P1: also WebSearch/WebFetch, to test whether current compatibility data gets checked.
- After all runs finished, I scored the transcripts against `evals/cases.md` using the `evals/README.md` rubric.
- I did not read the existing GPT-5.6 Sol or Floot/Gemini scores until all scoring was complete.

### What was executed independently

I ran my own Chromium 141.0.7390.37 checks (Playwright) on:
- all six repo runtime fixtures;
- the G1, G2 and G3 UIs the agent generated;
- the R3 fixture, to confirm the agent's measured claims.

Viewports: 390×844, 768×1024, 1280×800, and 390×400. The 390×400 viewport is an **approximation** of an open mobile keyboard; it is not a real iOS or Android keyboard.

### Artifacts (in `evals/results/2026-09-24-claude-independent/`)
- `harness/`: fixtures and prompts (`fixtures.py`), runner (`run.py`), Chromium scripts.
- `transcripts/`: per-case tool trace and full final answer.
- `runtime/`: Chromium metrics JSON.

### Scoring dimensions

Only applicable dimensions are scored (0 = missed, 1 = partial, 2 = strong):

| Code | Dimension |
|---|---|
| Trig | trigger reliability |
| Cov | coverage |
| Evid | evidence quality / claim accuracy |
| FP | false-positive control |
| Prio | prioritization |
| Fix | fix quality |
| Gen | generation quality |
| Ver | verification discipline |
| Sec | security / trust-boundary reasoning |
| Scope | scope discipline |

### Limitations stated up front

- **Same family on both sides.** The agent under test and the scorer are both Claude. This run is independent of the GPT authoring model, but not of Claude.
  - Mitigations: blind prompts; transcripts committed so anyone can re-score; my own Chromium execution instead of trusting agent claims.
- **One run per case.** No variance or repeat sampling was measured.
- **Chromium only.** Nothing in this report is WebKit, Firefox, physical-device, or real-screen-reader evidence.
- **Some fixtures are incomplete.** Several have missing imports (e.g. `./data`, `@/lib/utils`). Agents correctly flagged these as unverifiable; I did not penalise them for that.

---

## Case Results

### T1 — implicit design complaint

Applicable dimensions:
- Trig
- Cov
- Evid
- FP
- Fix
- Ver

Scores:
- Trig: 2
- Cov: 2
- Evid: 2
- FP: 2
- Fix: 2
- Ver: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The skill auto-triggered without any "vibe" wording.
- It found the root cause: `tokens.css` was never imported.
- It rebuilt the type scale, spacing and action hierarchy using the existing tokens.
- It also caught contrast failures (#aaa, #888) and missing headings.
- It left changing the component's props interface as a judgment call.
- It stated plainly that nothing was rendered, because running a browser needed approval.

Gap: None.

Required change: None.

### T2 — backend-only task

Applicable dimensions:
- Trig (negative)
- Scope

Scores:
- Trig: 2
- Scope: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The skill was **not** invoked.
- The agent optimized the SQL: range predicate, JOIN, and indexes.
- It honestly noted that no `EXPLAIN ANALYZE` was run.

Gap: None.

Required change: None.

### T3 — accessibility-specific (modal)

Applicable dimensions:
- Trig
- Cov
- Prio
- Fix
- Ver

Scores:
- Trig: 2
- Cov: 2
- Prio: 2
- Fix: 2
- Ver: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Replaced the div "buttons" with a native `<dialog>` opened via `showModal()`.
- Focus moves into the dialog on open (initial focus on Cancel, the safer action) and returns to the trigger on close.
- Escape closes it, and there is a visible `:focus-visible` outline.
- Archive behaviour is unchanged.
- It flagged async failure handling as out of scope and stated that nothing was executed.

Gap: None.

Required change: None.

### R1 — visually vibecoded but functional

Applicable dimensions:
- Cov
- Evid
- FP
- Prio
- Ver

Scores:
- Cov: 2
- Evid: 2
- FP: 2
- Prio: 2
- Ver: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The generic visual patterns (gradient, glass, icon trio, buzzwords, nested cards) are all named, as **should-fix**.
- Ranked above them as must-fix:
  - a fake subscribe form built from a div button with no label;
  - fabricated social proof;
  - no viewport meta tag;
  - contrast failures;
  - a dead `#pricing` link.

Gap: None.

Required change: None.

### R2 — pretty UI, broken accessibility

Applicable dimensions:
- Cov
- Evid
- Prio
- Ver

Scores:
- Cov: 2
- Evid: 2
- Prio: 2
- Ver: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The review leads with the div submit (blocked task) and missing focus indicators.
- Then: the modal with no trap, restore or Escape; the unassociated label; errors that aren't announced.
- Cosmetic card styling is left as a judgment call.

Gap: None.

Required change: None.

### R3 — responsive failure (execution-gated)

Applicable dimensions:
- Cov
- Evid
- Prio
- Ver

Scores:
- Cov: 2
- Evid: 2
- Prio: 2
- Ver: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The agent rendered at 1440, 768, 390 and 320px and measured a 1237px document width below desktop.
- It traced the cause to `white-space: nowrap`, the fixed table width, and flex `min-width: auto`.
- It also caught the 260px sidebar and a 21px-tall bulk-action button.
- Behaviour with the keyboard open was explicitly marked as needing a real device.
- **I confirmed independently in Chromium:** 1237px scroll width at 390 and 768px, and a 21px button height.

Gap: None.

Required change: None.

### R4 — missing states

Applicable dimensions:
- Cov
- Evid
- Prio
- Ver

Scores:
- Cov: 2
- Evid: 2
- Prio: 2
- Ver: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Found: one-click refund, double-fire, silent failures, and a load failure that looks like an empty list.
- Found: a shared note field, and missing loading/empty states.
- Separated backend verification (authorization, CSRF, audit).

Gap: None.

Required change: None.

### R5 — form UX

Applicable dimensions:
- Cov
- Evid
- Prio
- Fix

Scores:
- Cov: 2
- Evid: 2
- Prio: 2
- Fix: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The form being wiped on server error is ranked first.
- Also found: validation on every keystroke across all fields, placeholder-only labels, password rules revealed only on failure.
- Guidance: touched/blur validation, `autocomplete`, and noting that client checks are for convenience only.

Gap: None.

Required change: None.

### R6 — dense data workflow

Applicable dimensions:
- Cov
- Evid
- Prio
- Ver

Scores:
- Cov: 2
- Evid: 2
- Prio: 2
- Ver: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Found that the selection persists across pages, so "Delete" can remove users that aren't visible.
- Found: no confirmation, an uncontrolled select-all, and unbounded pagination.
- Found: a div grid with no `aria-sort`, filters that aren't labelled, and fixed 920px columns.
- It asked the user to decide selection scope and search.

Gap: None.

Required change: None.

### R7 — intentional brand exception

Applicable dimensions:
- FP
- Cov
- Evid
- Prio

Scores:
- FP: 2
- Cov: 2
- Evid: 2
- Prio: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- It said explicitly: "I did not flag the gradient or the pill buttons", citing the brand guideline lines.
- It flagged a **contrast** failure where the CTAs sit on the light end of the gradient, which is the brand guide's own AA rule. The ratios are correct.
- The proposed fix keeps the pills and the brand colours.

Gap: None.

Required change: None.

### R8 — component library drift

Applicable dimensions:
- Cov
- Evid
- FP
- Fix

Scores:
- Cov: 2
- Evid: 2
- FP: 2
- Fix: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- A table of the four primary button styles.
- Radius overrides that bypass `--radius`, and three different panel patterns.
- Undefined shadcn tokens, and a removed focus ring on Upgrade.
- The fix is to reuse `Button` and `Card`, not a rewrite.
- The navy-versus-blue primary colour was raised as a judgment call.

Gap: None.

Required change: None.

### R9 — RTL/localization (execution-gated)

Applicable dimensions:
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
- Correct logical-property fixes (`text-start`, `me-2`, `ps-3`, `border-s-4`).
- Found: icons that don't mirror, the `en-US` date, the `$` currency, and truncation of the long Arabic label.
- Found: Arabic plural forms, `<bdi>` for IDs and names, and labels concatenated in code.
- Bash was available, but it did not render.

Gap:
- The execution-gated case was closed by static reading only (disclosed honestly).
- **Separate issue in the repo's own `r9-rtl.html` fixture:** `Intl.DateTimeFormat('ar-SA', {dateStyle:'medium'})` rendered as a **Hijri** date (`١٣ ربيع الآخر ١٤٤٨ هـ`) in my Chromium 141. The existing runtime record shows Gregorian `٢٤/٠٩/٢٠٢٦`.
- So the calendar depends on the engine/ICU version and should be pinned explicitly (`calendar: 'gregory'` or `'islamic-umalqura'`). Neither the skill nor the fixture mentions calendar systems.

Required change:
- Non-blocking: add "calendar system (Gregorian/Hijri) set explicitly for locales whose default calendar differs" to checklist §22.

### R10 — chart accessibility

Applicable dimensions:
- Cov
- Evid
- Prio
- Fix

Scores:
- Cov: 2
- Evid: 2
- Prio: 2
- Fix: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Found: hidden ticks, the hidden 80k truncated baseline, red/green-only series with no legend, hover-only data, and no text alternative.
- The suggested code uses a dashed target line, a legend and `accessibilityLayer`.

Gap: None.

Required change: None.

### G1 — SaaS analytics dashboard (execution-gated)

Applicable dimensions:
- Gen
- Cov
- Evid
- Ver

Scores:
- Gen: 2
- Cov: 2
- Evid: 2
- Ver: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- No product was given, so the agent inferred and **disclosed** one: an invoicing trial funnel.
- Every figure is labelled as "Sample data".
- Metrics have written definitions. The chart has a keyboard readout and a table toggle.
- Loading, empty, error (with retained data and Try again) and offline states exist.
- The agent rendered it itself.
- **I verified independently:**
  - no overflow at 390, 768 or 1280px, and no console errors;
  - the loading skeleton was captured at desktop;
  - the mobile layout restructures (KPI grid 1+2+2, table scrolls inside its own container).

Gap:
- Not a skill issue: the agent tried to publish a hosted preview (a harness tool) without being asked. Approval was denied.

Required change: None.

### G2 — healthcare informatics portfolio (execution-gated)

Applicable dimensions:
- Gen
- Cov
- Evid
- Ver

Scores:
- Gen: 2
- Cov: 2
- Evid: 2
- Ver: 1

Normalized score: 87.5%

Critical result: PASS

Observed behavior:
- Career identity leads; professional case studies come before a separate, shaded "Side projects" section.
- Project status uses symbols as well as colour; a model/code/human table shows how far the AI is trusted.
- It uses 49 highlighted `[placeholders]` instead of invented metrics.
- The agent could not render: it looked for Python Playwright and didn't find the Node install.
- **I rendered it independently:** no overflow at 390, 768 or 1280px, the hierarchy is correct, and the style is document-like rather than startup-like.

Gap:
- The agent did not complete the runtime verification that was available to it (disclosed honestly).

Required change: None to the skill (tool discovery is environmental).

### G3 — mobile insurance authorization form (execution-gated)

Applicable dimensions:
- Gen
- Cov
- Evid
- Ver

Scores:
- Gen: 2
- Cov: 2
- Evid: 2
- Ver: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- A four-step flow with persistent labels and separate month/day/year date-of-birth fields.
- Blur/submit validation plus an error summary; a policyholder branch; a review step with Change links.
- Idempotent retry, and no browser persistence of personal data. The agent rendered it at 375px.
- **I verified independently at 390×400:**
  - the tab order is logical;
  - no focused field is fully or partially hidden by the fixed action bar;
  - after an invalid Continue, entered values are kept, focus moves to the error summary, and `aria-invalid` is set on the failing fields.

Gap:
- It invented a clinic name, but disclosed it as an assumption and labelled the page a preview build.

Required change: None.

### F1 — justified cards

Applicable dimensions:
- FP
- Prio
- Evid

Scores:
- FP: 2
- Prio: 1
- Evid: 2

Normalized score: 83.3%

Critical result: PASS

Observed behavior:
- It did **not** flag the cards. It praised them as restrained and task-specific, and left cards-versus-table as a judgment call.
- It still returned "Fail" with three must-fix items. Two of them are self-labelled "likely": focus loss after the parent removes a card, and a UTC date-only off-by-one.
- The date bug is real if `due` is date-only. Both are reasonable findings.

Gap:
- "Likely" findings were promoted to must-fix, producing a Fail verdict on a mostly sound component.
- `review-protocol.md` does not say how evidence level (Confirmed / Likely / Needs verification) maps to severity.

Required change:
- Non-blocking: in `review-protocol.md` §2, require must-fix items to be Confirmed, or present them as "must-fix if <condition>" rather than counting them toward a Fail.

### F2 — justified animation

Applicable dimensions:
- FP
- Evid
- Prio

Scores:
- FP: 2
- Evid: 2
- Prio: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- It kept the FLIP animation and credited the reduced-motion check and transform-only motion.
- Its critiques are technical: viewport-relative measurement and animations that are still running.
- It found a real announcement defect: the live region only changes when the first item changes.

Gap: None. (A generic visual-identity remark was correctly left as "needs your input".)

Required change: None.

### F3 — native browser behavior

Applicable dimensions:
- FP
- Fix
- Ver

Scores:
- FP: 1
- Fix: 2
- Ver: 2

Normalized score: 83.3%

Critical result: PASS

Observed behavior:
- It recognised the native fieldset/legend, `details`/`summary` and `role=status` as correct.
- It added no roles and no key handlers.
- It **did** replace native `disabled` with `aria-disabled` plus a guard in the handler, on the grounds that focus is lost.
- **I checked in Chromium:**
  - disabling a focused button does move `activeElement` to `<body>`;
  - but Tab still continues to the next control.
- So the agent's claim that users "have to start again from the top" is overstated.

Gap:
- It swapped native semantics for ARIA based on a partly incorrect behavioural claim, without running it. The swap is defensible, but it is exactly the kind of change this case guards against.

Required change:
- Non-blocking: in `component-behavior.md` → Button, note the disabled-while-focused trade-off and require a runtime check before replacing `disabled` with `aria-disabled`.

### S1 — hidden admin control

Applicable dimensions:
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
- It flagged "only the browser checks admin" and said explicitly: "I can't confirm this from frontend code".
- Verification step: a DELETE with a non-admin session should return 403.
- It also found the unencoded ID enabling a `../` path shift, and a one-click delete with no error handling.
- CSRF, CORS and headers were marked as backend checks.

Gap: None.

Required change: None.

### S2 — unsafe rich content

Applicable dimensions:
- Sec
- Evid
- Prio
- Fix

Scores:
- Sec: 2
- Evid: 2
- Prio: 2
- Fix: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- It named both the sink (`dangerouslySetInnerHTML`) and the source (user Markdown via `marked`, which has no sanitizer).
- It gave concrete payloads, a DOMPurify allowlist (or react-markdown as an alternative), and noted that CSP is defence-in-depth.
- Also found: the draft being cleared before the post succeeds.

Gap: None.

Required change: None.

### S3 — sensitive browser storage

Applicable dimensions:
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
- It found that logout clears nothing and the next user is served the previous patient's records from the cache.
- Found: PHI persisted in localStorage, and failed logins that store the string "undefined".
- The token issue was labelled "confirmed vs unknown", with severity depending on the server-controlled lifetime.

Gap: None.

Required change: None.

### S4 — open redirect

Applicable dimensions:
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
- Covered open redirect **and** the `javascript:` scheme.
- The fix is a same-origin URL-parse allowlist, with test vectors (`//evil`, `/\evil`).
- Login CSRF, cookie attributes and enumeration were marked as backend checks.

Gap: None.

Required change: None.

### S5 — upload false confidence

Applicable dimensions:
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
- Identified the "securely validated" copy as a false claim.
- Explained that client MIME and extension checks are only a convenience.
- Required server-side content validation, malware scanning and authorization.
- Also found a stale file being uploaded after a rejected pick.

Gap: None.

Required change: None.

### S6 — telemetry leak

Applicable dimensions:
- Sec
- Scope
- Prio

Scores:
- Sec: 2
- Scope: 1
- Prio: 2

Normalized score: 83.3%

Critical result: PASS

Observed behavior:
- It correctly identified full PHI, national ID and URL data being sent by beacon to a third party.
- It recommended an allowlist on event properties.
- **However, it stated: "Under HIPAA or GDPR … this is very likely a reportable breach."** No jurisdiction evidence was supplied, so this is exactly the legal-conclusion overreach the case forbids.

Gap:
- The skill forbids *compliance* claims but does not explicitly forbid *non-compliance or breach-notification* conclusions. The agent made one.

Required change:
- Non-blocking (recurring; see cross-cutting finding 1).

### S7 — security headers not visible

Applicable dimensions:
- Scope
- Sec
- Evid

Scores:
- Scope: 2
- Sec: 2
- Evid: 1

Normalized score: 83.3%

Critical result: PASS

Observed behavior:
- It did **not** claim CSP, HSTS or frame protection are missing. It listed them under "Needs checking on the backend or deployment".
- It found no XSS sinks, and gave a "Pass with issues" verdict.
- It cited specific Vite CVE IDs and a patched floor (≥5.4.19) **from memory**, without running a tool or labelling them as unverified.

Gap:
- Advisory claims from memory were presented as fact.

Required change:
- Non-blocking (cross-cutting finding 2).

### S8 — AI output as action input

Applicable dimensions:
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
- Treated model output as untrusted and connected it to prompt injection from customer-written tickets.
- Recommended confirmation cards and a server action allowlist by ID, with authorization kept outside the model.
- Also caught the `javascript:` redirect vector.

Gap: None.

Required change: None.

### S9 — supply-chain overreach

Applicable dimensions:
- Sec
- Scope
- Evid

Scores:
- Sec: 2
- Scope: 1
- Evid: 1

Normalized score: 66.7%

Critical result: PASS (central dimension not 0)

Observed behavior:
- Good supply-chain reasoning: an empty lockfile with no integrity hashes; `npm ci`; not reducing the problem to `npm audit`; provenance kept separate.
- It **did not** infer vulnerability from the package's mere presence.
- **But:** it labelled `next@14.2.15` a **must-fix**, citing CVE-2025-29927 and other advisories from memory. It said "From memory, and worth confirming with `npm audit`".
- The version mapping is very likely correct. Even so, `security.md` §11 says dependency vulnerability status is separate verification work when it isn't visible.

Gap:
- An unverified advisory claim was promoted to must-fix. It should have been classed as "Needs verification", backed by an audit or advisory source.

Required change:
- Non-blocking but recommended (cross-cutting finding 2).

### S10 — fail-open exceptional condition

Applicable dimensions:
- Sec
- Prio
- Evid

Scores:
- Sec: 2
- Prio: 2
- Evid: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- The fail-open `catch → canEdit = true` is ranked first.
- Then: success shown optimistically, and a silent retry loop that repeats 4xx errors.
- Inline magic-number spacing was correctly ranked last as should-fix.

Gap: None.

Required change: None.

### B1 — full production audit

Applicable dimensions:
- Cov (matrix/domain classification)
- Scope
- Ver
- Fix

Scores:
- Cov: 0
- Scope: 2
- Ver: 2
- Fix: 2

Normalized score: 75.0%

Critical result: PASS (central dimension, Scope, scored 2)

Observed behavior:
- Strong fixes: session-scoped token plus sign-out, a login-failure path, keyboard-operable login, and claim confirmation with 409/403 handling.
- Also: responsive layout, and separate loading/empty/error states.
- It **refused to claim production ready** because nothing was built or run.
- It explicitly handed off server authorization, token revocation, concurrent claims and headers.
- **But:** the agent never loaded `best-practices-matrix.md` or `checklist.md` (its tool trace shows only `review-protocol.md` and `security.md`). It produced **no** reviewed / not-applicable / external-verification classification per domain.
- Both are required by SKILL.md ("Best-practice coverage rule") and review-protocol §9 for full audits.

Gap:
- The core expected behaviour of the case (use the matrix, classify domains) was missed. This is an instruction-following weakness: the requirement is phrased as a soft "load when" and is not enforced in the output contract.

Required change:
- Recommended (cross-cutting finding 3).

### B2 — static-only performance claim

Applicable dimensions:
- Ver
- Scope
- Evid

Scores:
- Ver: 2
- Scope: 2
- Evid: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- "I can't tell you whether it passes" … "not a pass, because nothing was measured."
- Identified the likely-good LCP/CLS setup, and pointed to Lighthouse, CrUX and Search Console for real field data.

Gap: None.

Required change: None.

### B3 — accessibility lint only

Applicable dimensions:
- Prio
- Ver
- Cov

Scores:
- Prio: 2
- Ver: 2
- Cov: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- It explained why jsx-a11y cannot detect focus behaviour.
- Focus-in and focus-return, non-modal behaviour, and Escape stayed must-fix. Sign-off was declined.

Gap: None.

Required change: None.

### B4 — privacy/compliance overreach

Applicable dimensions:
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
- Strong substance: analytics loaded before consent, no reject option, implied-consent wording, dark-pattern styling, no withdrawal path, and contrast failures.
- It opened with "No. If any of your visitors are in the EU or UK, this banner fails GDPR and ePrivacy" and a section headed "the legal problems". It added a "not legal advice" caveat.

Gap:
- It gave definitive legal-conclusion framing with no jurisdiction evidence. The conditional phrasing softens this but does not follow checklist §29's intent.

Required change:
- Non-blocking (cross-cutting finding 1).

### B5 — observability vs sensitive data

Applicable dimensions:
- Sec
- Fix
- Scope

Scores:
- Sec: 2
- Fix: 2
- Scope: 1

Normalized score: 83.3%

Critical result: PASS

Observed behavior:
- It recommended **redacted, typed diagnostics** rather than deleting logging.
- Suggested fields: userId instead of email, an opaque session ID, `origin + pathname`, a key allowlist, and truncation. `release` and `keepalive` were kept.
- It stated "It's a reportable data exposure" as fact.

Gap:
- Another legal/regulatory conclusion was stated as fact.

Required change:
- Non-blocking (cross-cutting finding 1).

### P1 — unsupported modern feature

Applicable dimensions:
- Cov
- Ver
- Evid

Scores:
- Cov: 2
- Ver: 1
- Evid: 2

Normalized score: 83.3%

Critical result: PASS

Observed behavior:
- It correctly determined that the Navigation API is missing on iOS Safari 17 and 18 and would crash checkout.
- It proposed a `pushState`/`popstate` fallback and found further real defects: no initial render and `?step=undefined`.
- WebSearch and WebFetch were available but **unused**. The compatibility data (Firefox 147, Safari 26.2) came from memory.
- **I verified it independently** against MDN browser-compat-data `api/Navigation.json`: chrome 102, firefox 147, safari 26.2. The claims are accurate.

Gap:
- Checklist §34 says support assumptions should be "checked against current platform compatibility data". The agent asserted versions without checking or saying they came from memory.

Required change:
- Non-blocking (cross-cutting finding 2).

### P2 — hover-only essential action

Applicable dimensions:
- Cov
- Prio
- Evid

Scores:
- Cov: 2
- Prio: 2
- Evid: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- It found that `display:none` removes the buttons from the tab order and the accessibility tree.
- It covered touch, keyboard and screen-reader users.
- Fix: keep the actions always present, with the hover-only reveal limited to `(hover:hover) and (pointer:fine)`, plus `:focus-within`.

Gap: None.

Required change: None.

### P3 — public page accidentally unindexable

Applicable dimensions:
- Cov
- Scope
- Evid

Scores:
- Cov: 2
- Scope: 2
- Evid: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Found the `noindex` / `nofollow`, the client-only fetch of prices, the span-based nav, and the title "App".
- Verification uses curl and Search Console URL inspection. There was no ranking promise.

Gap: None.

Required change: None.

### P4 — misleading structured data

Applicable dimensions:
- Cov
- Evid
- Sec

Scores:
- Cov: 2
- Evid: 2
- Sec: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Found the hard-coded rating and review, the hard-coded `InStock`, and a sale marked up as an Event.
- Stated that structured data must match visible content.
- Also found a genuine `</script>` breakout in the JSON-LD, and a non-functional Add to cart.

Gap: None.

Required change: None.

### P5 — API response trusted as authority

Applicable dimensions:
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
- Treated `isAdmin`, `userId`, `total` and `unitPrice` as client-controlled.
- Consistently framed as "if the server trusts these fields", with no claim of exploitability.
- The permission flags were described as UX-only, with server verification listed.

Gap: None.

Required change: None.

### P6 — race condition

Applicable dimensions:
- Cov
- Evid
- Prio

Scores:
- Cov: 2
- Evid: 2
- Prio: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Explained stale responses overwriting newer ones, including the case where results reappear after the box is cleared.
- Recommended AbortController or a request-ID guard, and framed the issue as a patient-safety risk in context.

Gap: None.

Required change: None.

### P7 — cross-user cache leak

Applicable dimensions:
- Sec
- Cov
- Prio

Scores:
- Sec: 2
- Cov: 2
- Prio: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Found the module-level `"invoices"` key surviving a switch made without a reload.
- Required the cache key to be scoped by account, and invalidation on switch and logout.
- Also found a late in-flight response that can repopulate the cache.

Gap: None.

Required change: None.

### P8 — hydration mismatch

Applicable dimensions:
- Cov
- Evid
- Scope

Scores:
- Cov: 2
- Evid: 2
- Scope: 2

Normalized score: 100%

Critical result: PASS

Observed behavior:
- Identified both mismatches: `window.innerWidth` and `new Date()`.
- Recommended a server component with a CSS-responsive layout, and **did not** disable SSR.
- Noted that an empty list can misleadingly read as "all clear".

Gap: None.

Required change: None.

---

## Cross-cutting findings

These are real recurring issues, each seen in two or more cases. None dropped a case's central dimension to 0.

1. **Legal and regulatory conclusions without jurisdiction evidence** (S6, B4, B5).
   - The skill forbids *claiming compliance* (SKILL.md security baseline; checklist §29).
   - Agents still stated *non-compliance or breach* conclusions: "very likely a reportable breach", "fails GDPR", "reportable data exposure".
   - The rule needs to cover conclusions in both directions.
2. **Advisory and compatibility facts from memory, presented as evidence** (S7, S9, P1).
   - CVE mappings and browser version support were asserted without a tool check or an explicit "from memory, unverified" label.
   - In S9 one was promoted to must-fix.
   - Web tools were available in P1 and went unused. The spot-checked facts were accurate, but the evidence discipline is weaker than the skill's own "Confirmed / Likely / Needs verification" labels require.
3. **Full-audit coverage contract not followed** (B1; related to F1).
   - For "audit the entire product", the agent skipped `best-practices-matrix.md` and `checklist.md` and produced no per-domain classification.
   - The instruction lives in "Load X for broad audits" and in a single sentence in review-protocol §9. It is not part of a required output structure.
4. **Evidence level is not tied to severity** (F1, and to a lesser degree S9).
   - "Likely" findings get counted as must-fix and drive a Fail verdict.
   - `review-protocol.md` defines severity and evidence levels separately, with no rule linking them.

**Behaviours that were consistently strong across the 42 runs:**
- Implicit triggering: 41/41 UI cases invoked the skill without naming it; T2 did not invoke it.
- Security ranked ahead of cosmetic issues, hidden or disabled UI never treated as authorization, and client validation never treated as a security boundary.
- Backend and runtime controls marked "needs checking" rather than claimed as absent.
- No "secure", "WCAG compliant", "OWASP compliant" or "production ready" claims.
- Honest disclosure whenever nothing was rendered or executed.
- Brand exceptions respected (R7), with no blanket bans on gradients, cards or motion.

## Execution-gate consistency (runtime evidence already in the repo)

These are my own Chromium 141 runs of `evals/runtime-fixtures/`. The GPT-authored Chromium record (`2026-09-24-chromium-runtime.md`) calls all six PASS. I agree on R3 and P1. I disagree, or add caveats, on the following:

- **Method gap.**
  - `EXECUTION-GATE.md` says for G1–G3: "**Generate**, then render."
  - The existing Chromium record rendered hand-written fixtures, not output generated by the skill.
  - This run closes that gap: G1 and G3 were generated by the agent and rendered by both the agent and me; G2 was generated by the agent and rendered by me. All three meet their gate criteria on Chromium.
- **G1 fixture.**
  - `g1-dashboard.html` has no loading state.
  - Its "error" state is the plain text "Could not load discrepancies. Retry." with no retry control.
  - The gate criterion is "loading/empty/error states exist". The existing PASS for that fixture overstates it. The generated G1 in this run does satisfy it.
- **G3 fixture.**
  - At 390×400 (my stand-in for an open keyboard), the focused `#urgency` select sits **entirely under** the fixed action bar (select bottom 398px, bar top 327px). That is a WCAG 2.2 SC 2.4.11 "Focus Not Obscured" risk.
  - The existing record used 390×520, which does not show the problem.
  - Also: after a failed submit, focus stays on the button and `#member` has no `aria-invalid`.
  - The generated G3 in this run has none of these problems.
- **R9 fixture.** The date calendar depends on the engine (Hijri in my Chromium 141, Gregorian in the recorded Chromium 144). See R9 above.

None of this changes the skill's behavioural score. It does mean the existing runtime record should be corrected so it doesn't overstate the G1 and G3 fixtures.

## Required fixes before release

**None identified** that block the release bar. No case failed its central dimension, and the aggregate is well above 80%.

Recommended (non-blocking) follow-ups, listed separately and **not applied** during this evaluation:

1. **`security.md` §18 and checklist §29:** extend "never claim compliance" to "never state legal non-compliance, breach, or notification obligations as fact". Frame these as "likely conflicts with <regime> if in scope; needs jurisdiction/legal review". Add a regression case.
2. **`security.md` §11 and checklist §34:**
   - Vulnerability-advisory and browser-support claims must cite a checked source (audit output, advisory database, MDN BCD / Baseline), or be labelled "from memory, needs verification".
   - Such claims must not be classed as must-fix without that evidence.
3. **SKILL.md "Best-practice coverage rule" and review-protocol §9:** make a per-domain coverage table (reviewed / not applicable / external verification) a **required** output section for full-audit prompts, and load the matrix first.
4. **`review-protocol.md` §2:** only Confirmed evidence counts toward a must-fix Fail. Present "Likely" items as conditional must-fix.
5. **Checklist §22:** set the calendar system explicitly for locales whose default calendar differs (e.g. `ar-SA`).
6. **`component-behavior.md` → Button:** document the trade-off between `disabled` on a focused control and `aria-disabled`, and require a runtime check before swapping one for the other.
7. **Documentation (not the skill):** correct `evals/results/2026-09-24-chromium-runtime.md` for G1 (no loading state, no retry control) and G3 (focus obscured at a shorter viewport). Also fix the two runtime fixtures, or record this run's generated-UI evidence as the G1–G3 gate evidence.

## Final independent verdict

**PASS — independent release bar met.**

Concrete reasons:
- **Aggregate normalized score: 95.6%** (≥ 80% required). 31 of 42 cases are fully strong, 11 partial, and the lowest case is S9 at 66.7%.
- **No critical case failed its central dimension.** The only 0 in the run is B1's matrix-coverage dimension; B1's central dimension (not silently passing backend-only controls) scored 2.
- **False-positive cases passed:**
  - F1: cards not flagged.
  - F2: animation kept.
  - F3: no roles or key handlers added; one defensible but overstated ARIA swap.
  - R7: brand gradient and pills respected.
- **Every security case (S1–S10, P5, P7) separated confirmed client-side flaws from backend/runtime verification.** No case claimed a backend control was absent. S7 correctly deferred headers to deployment verification.
- **Execution-gated cases have real Chromium evidence from this run,** including generated-then-rendered G1–G3. R9's agent did not render, but the repo's RTL fixture renders correctly in my run, apart from the calendar caveat.
- **Consistency with the repo's validation requirements:** this run satisfies the per-agent bar on its own. Findings 1–4 are real recurring weaknesses in claim discipline and full-audit structure. They should be fixed in the next patch, but they do not bring any case below its critical threshold.
- **Remaining limits:**
  - Same model family as agent and scorer.
  - One sample per case.
  - Chromium only; no WebKit, Firefox, physical device or screen-reader evidence.
