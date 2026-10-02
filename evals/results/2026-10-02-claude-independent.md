# Independent full-suite run, Claude Code CLI

Date: 2026-10-02.
Scorer: Claude Opus 5.5, in a separate session. It did not run any task.
Task agent: Claude Code CLI 2.1.287 (`claude -p`). The model reported in every attempt's init event was `claude-sonnet-5-5`.
Delivery: full folder at `.claude/skills/anti-vibecoding-ui/`. V4 used paste delivery.
Isolation: each attempt ran in a fresh task directory outside the repository, prepared with `scripts/prepare_evals.py`. The runs used `--setting-sources project` and the fixture's tool grant, with the parent session's additional-directory variables removed. Task agents never saw the rubric, the assertions or earlier results. A transcript scan found no reads of repository paths.
Model family: this is a Claude-family run. It is independent of the GPT-5.6 Sol author, but the same family as the 2026-09-24 Claude run.

Mandatory assertions and central dimensions were written down before any output was read. The rubric is the one in `evals/README.md`. An attempt counts as "loaded" only when the task agent invoked the skill. An agent that read a reference file directly is recorded as not loaded.

## Run 1: commit `e0487186` (PR #12 head as reviewed)

56 attempts. 46 cases.

**Aggregate normalized score: 92.9%** (299/322). Mean per-case score: 93.0%.
**Critical failures: 1 (B4).** False-positive cases F1–F3 and R7 passed.
Trigger: T2 loaded in 0 of 3 attempts, which is correct. Of the 50 full-mode UI attempts, 42 loaded the skill and 8 did not:
- B3
- B4
- B5-2
- P7
- S1
- S9
- T3-2
- T3-3

S1 and T3-2 read reference files directly without invoking the skill.

| Case | Score | Central | Notes |
|---|---|---|---|
| V1 | 9/10 | pass | Not verified verdict. All 19 domains appear once each. Minor nits about charset and viewport. |
| V2 | 10/10 | pass | Risk is separated from legality. The missing facts are requested. |
| V3 | 10/10 | pass | The header fact is confirmed. Server effects are labelled unverified. |
| V4 | 10/10 | pass | All three paste subruns held the V1–V3 assertions. |
| T1 | 10/10 | pass | Loaded 3/3. Each attempt stated it was not rendered. |
| T2 | 2/2 | pass | Loaded 0/3. |
| T3 | 9/10 | pass | Skill invoked 1/3. All 3 fixes were correct (native `<dialog>`). |
| R1 | 10/10 | pass | |
| R2 | 7/8 | pass | "Flow incomplete" is rated must-fix while the agent admits it may be a stub. |
| R3 | 7/8 | pass | The sticky-footer/keyboard occlusion was deferred, not identified. |
| R4 | 8/8 | pass | |
| R5 | 7/8 | pass | WCAG criteria are named as failures from static code. |
| R6 | 8/8 | pass | |
| R7 | 8/8 | pass | Brand gradient and pills were respected. |
| R8 | 6/8 | pass | A missing-module must-fix rests on an admittedly incomplete search. |
| R9 | 5/6 | pass | Not rendered. No native-review limit stated. |
| R10 | 7/8 | pass | Recommends a palette validator from an unrelated skill. |
| G1 | 6/8 | pass | jsdom check only. Chromium shows 9px overflow at 320px from the products table. |
| G2 | 7/8 | pass | Placeholders, no invented claims. See the limitation about the account email. |
| G3 | 5/6 | pass | Values preserved. Error summary focused. No focus ring detected on `#dob`. |
| F1 | 6/6 | pass | |
| F2 | 5/6 | pass | Animation kept. The live-region must-fix inflates the verdict to Fail. |
| F3 | 6/6 | pass | No ARIA added. |
| S1 | 8/8 | pass | Not loaded, but the boundary was correct. |
| S2 | 8/8 | pass | |
| S3 | 8/8 | pass | |
| S4 | 6/6 | pass | |
| S5 | 6/6 | pass | |
| S6 | 6/6 | pass | No legal claim. |
| S7 | 6/6 | pass | Headers left for runtime verification. |
| S8 | 6/6 | pass | |
| S9 | 3/6 | pass (weak) | Not loaded. EOL claim unlabelled. Firm "No" verdict. CVE from memory, but labelled. |
| S10 | 6/6 | pass | |
| B1 | 8/8 | pass | 19 rows, one each. Not verified verdict. |
| B2 | 6/6 | pass | |
| B3 | 4/4 | pass | Not loaded. Sign-off refused. |
| B4 | 3/6 | **FAIL** | Not loaded. "This banner isn't compliant with GDPR/ePrivacy." |
| B5 | 5/8 | pass | Loaded 2/3. The non-loaded attempt stated "That is a PCI DSS violation." |
| P1 | 6/6 | pass | Current support checked with cited sources. |
| P2 | 6/6 | pass | |
| P3 | 6/6 | pass | |
| P4 | 6/6 | pass | |
| P5 | 6/6 | pass | |
| P6 | 4/4 | pass | |
| P7 | 4/4 | pass | Not loaded. Cross-account cache leak found. |
| P8 | 4/4 | pass | |

Run 1 does not satisfy the release bar, because B4 is a critical failure. Every critical-assertion breach (B4, plus the B5-2 legal claim) came from an attempt where the skill did not load. The patch therefore targets trigger cues. It does not restate rules that the loaded skill already followed.

## Runtime evidence (Chromium 141.0.7390.37 only)

Playwright 1.56.1 ran headless Chromium. The viewports were 320, 390, 768 and 1280 CSS px, with touch enabled below 800 px.

- **R3 task fixture:** page-level horizontal overflow at 320, 390 and 768, with `scrollWidth` 1237. That confirms the agent's static finding. Virtual-keyboard occlusion was not verified, and viewport resizing does not count as keyboard evidence.
- **G1 generated:** no overflow at 390, 768 or 1280. Overflow at 320 (`table.data`, 419 px). Every tab stop had a visible focus indicator.
- **G2 generated:** no overflow at any width. Focus indicators were visible.
- **G3 generated:** no overflow. Submitting a partial form preserved values, set 9 `aria-invalid` fields and focused the error summary. Submit stayed visible at 390×450, which is an approximation of the keyboard, not real keyboard evidence. The heuristic found no outline or shadow focus indicator on the `#dob` input.
- **P1 task fixture:** over HTTP, with the Navigation API present, nothing rendered on first load. With the API removed, `TypeError ... reading 'addEventListener'`. Both confirm the agent's findings. Safari and Firefox were not run. Forcing the API off in Chromium proves fallback behaviour only.
- **Repository runtime fixtures (r3, r9, g1, g2, g3, p1):** no overflow at any width in Chromium. r9 rendered `dir=rtl`, `lang=ar`.

The following were not verified, and none of them is counted as passed:
- Safari, WebKit and Firefox
- physical mobile keyboards
- screen readers
- native-language Arabic review
- Codex client discovery
- Claude Code interactive `/` discovery

Only the headless CLI was used.

## Limitations

- Each case has one sample, except the trigger paraphrases. Expect variance.
- The CLI injects the account email as session context. G2 used it as the contact address and flagged it for confirmation. That comes from the environment, not from the skill. Transcripts here redact it.
- The task agent and the scorer are both Claude-family models. The combined two-family aggregate needs the separate GPT-family record.

## Run 2: commit `4aac509` (fixes applied)

58 attempts. This adds three B4 consent paraphrases to the run 1 set. The isolation, model and client were the same as run 1.

The whole suite was rerun. Scoring covered every trigger attempt, every case that run 1 failed or found weak, and the critical-assertion subset. That subset is:
- the scope and legal cases: V1–V4, B1, B4
- the false-positive cases: F1–F3, R7
- the security cases: S1–S10
- the trigger cases: T1–T3, B5
- the execution-gated cases: R3, R9, G1–G3, P1

Cases not in this list were not rescored. Their run 1 scores stand.

- **Trigger:** all 52 full-mode UI attempts loaded the skill, up from 42 of 50. T2 loaded in 0 of 3, so there was no over-triggering. B4 loaded 3/3, B5 3/3, T3 3/3. B3, S1, S9 and P7 all loaded.
- **Critical failures: 0.**
  - B4: none of the three attempts asserts compliance or illegality. Each one names the jurisdiction and processing facts that are missing.
  - B5-2 no longer claims a PCI violation.
  - S9 now labels the CVE and EOL claims as from memory and lists the provenance checks still to do.
  - A scan of all 58 outputs for "violat", "non-compliant", "breach" and "isn't compliant" found only explicit disclaimers.
- **Scope and false-positive cases:** V1 and B1 each list all 19 domains exactly once. F1–F3 and R7 raised no pattern-ban findings.
- **Rescored cases:**

| Case | Run 1 | Run 2 |
|---|---|---|
| B4 | 3/6 (FAIL) | 6/6 |
| B5 | 5/8 | 8/8 |
| S9 | 3/6 | 6/6 |
| T3 | 9/10 | 10/10 |
| G1 | 6/8 | 7/8 |
| R3 | 7/8 | 8/8 |
| V4 | 10/10 | 9/10 |

  R3 now identifies the footer and keyboard occlusion risk and labels it as needing a device. V4 lost a point because V4-V3 rated an error-handling issue "must-fix, pending callers".
- **Remaining weak spots, all with the skill loaded:**
  - R8 still rates an unconfirmed missing import as must-fix, although it is labelled "needs a quick check".
  - R9 still omits the native-language review limit.
  - Neither breaks a central assertion. The skill already states both rules, so they are instruction-following variance, not missing instructions.

Recomputed aggregate, with the rescored cases above and run 1 scores for the rest: **310/322 = 96.3%**.

### Run 2 runtime evidence (Chromium 141 only)

- **G1:** no page overflow at 320, 390, 768 or 1280. Focus was visible at all 9 tab stops. This fixes the run 1 overflow at 320.
- **G2:** no overflow. Focus visible.
- **G3:**
  - No overflow.
  - A failed submit kept the entered values, set 6 `aria-invalid` fields and focused the error summary.
  - The focus heuristic flagged 4 checkbox and radio inputs. The CSS draws their focus ring on the `.choice` wrapper through `:has(:focus-visible)`, so the flag is a false positive.
  - Submit is in normal page flow. It is not pinned, so at 390×450 the user must scroll to reach it. Real keyboard occlusion was not verified.
- **R3 task fixture:** the overflow is still confirmed. The fixture is unchanged.

## Verdict for this record

- Run 1 does not meet the release bar, because of B4.
- Run 2 has 0 critical failures and an aggregate of 96.3%.
- Both are single-family Claude results.

The repository's release bar also requires:
- a two-agent combined aggregate;
- target-engine evidence (Safari and Firefox);
- physical mobile keyboard evidence;
- a native-language review.

None of those exists for this revision, so the release gate stays open.
