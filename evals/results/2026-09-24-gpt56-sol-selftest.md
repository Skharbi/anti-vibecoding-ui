# Evaluation Run — GPT-5.6 Sol Self-Test

Date: 2026-09-24
Branch: `chatgpt/skill-hardening-v2`
Evaluator: GPT-5.6 Sol
Run type: **single-agent structural + scenario walkthrough**
Release qualification: **does not satisfy the required two-agent release bar**

## Scope

All current cases in `evals/cases.md` were walked against the actual skill instructions and references.

Total cases after gap discovery: **42**

Groups:
- Trigger: 3
- Review: 10
- Generation: 3
- False-positive: 3
- Security/trust: 10
- Cross-domain best-practice: 5
- Platform/delivery: 8

## Important limitation

This run can verify:
- trigger wording and exclusions;
- whether the skill contains the rules required to handle a scenario;
- prioritization logic;
- false-positive controls;
- security/scope boundaries;
- whether verification claims are appropriately constrained.

This run cannot independently prove:
- real trigger behavior in another model;
- rendered visual quality;
- browser/device behavior;
- assistive-technology behavior;
- Core Web Vitals;
- backend/runtime security controls;
- actual multi-agent consistency.

Those remain release-gate items.

## Gaps found during the run

### GAP-01 — Evaluation denominator was invalid
**Found:** every case used the same 18-point maximum even when dimensions were irrelevant.

**Risk:** backend-only trigger cases or visual exception cases could be penalized for irrelevant security/fix dimensions.

**Fix:** scoring now supports N/A, normalizes only applicable dimensions, and defines critical dimensions that can independently fail a case.

**Retest:** PASS.

### GAP-02 — Installed skill referenced files outside its package
**Found:** `SKILL.md` referenced repo-root `evals/*`.

**Risk:** users installing only `skills/anti-vibecoding-ui/` would receive broken reference paths.

**Fix:** removed runtime references to repo-root evaluation files. Evals remain repository-development QA only.

**Retest:** PASS.

### GAP-03 — Security severity was under-specified
**Found:** review severity and prioritization did not explicitly elevate confirmed security/privacy exposure.

**Risk:** a serious client-side security flaw could be reported alongside or below cosmetic findings.

**Fix:** must-fix now includes confirmed high-impact client security issues, sensitive-data exposure, fail-open authorization/permissions, and unsafe untrusted-content execution. Review ordering now puts security/privacy/data-loss first.

**Retest:** PASS.

### GAP-04 — Trigger metadata under-signaled security/privacy audits
**Found:** description strongly covered UI/accessibility but did not explicitly mention frontend security/privacy/production-readiness.

**Risk:** direct requests such as "audit frontend security" could fail to activate reliably.

**Fix:** expanded trigger description for frontend security/privacy, sensitive data, production audits, API consumption, rendering/cache/concurrency, browser compatibility, and public discoverability.

**Retest:** PASS.

### GAP-05 — Browser/platform compatibility missing
**Found:** responsive coverage did not explicitly cover unsupported web APIs, feature detection, progressive enhancement, cross-input behavior, or browser-support assumptions.

**Fix:** added dedicated browser compatibility/progressive enhancement section grounded in MDN Baseline/progressive enhancement guidance.

**Retest:** PASS for policy coverage; executed browser matrix still required.

### GAP-06 — Public discoverability/SEO missing
**Found:** public landing/marketing/content pages could pass without document-title, canonical/indexability, crawlable-link, or truthful structured-data review.

**Fix:** added public-site discoverability/metadata section and Search Essentials references.

**Retest:** PASS for policy coverage; deployed indexability still requires runtime/search verification.

### GAP-07 — API client trust boundary incomplete
**Found:** general security covered object IDs and server authorization, but API-consumption behavior was not a dedicated frontend contract.

**Fix:** added API consumption/frontend-backend contract section using OWASP API Security Top 10 2023 as the adjacent baseline.

**Retest:** PASS.

### GAP-08 — Rendering/cache/concurrency blind spot
**Found:** hydration mismatch, cross-user client caching, stale permissions, race conditions, request cancellation, and cache revalidation were not explicit.

**Fix:** added rendering, hydration, caching, and concurrency coverage plus regression cases.

**Retest:** PASS.

## Case walkthrough

### Trigger
| Case | Result | Notes |
|---|---|---|
| T1 implicit spacing/hierarchy | PASS | explicit trigger coverage |
| T2 backend-only Postgres | PASS | explicit backend-only exclusion remains |
| T3 keyboard-stuck modal | PASS | accessibility + component behavior coverage |

### Review
| Case | Result | Notes |
|---|---|---|
| R1 generic AI visual patterns | PASS | anti-vibe rules + broader QA retained |
| R2 pretty but inaccessible | PASS | accessibility outranks cosmetics |
| R3 mobile overflow/keyboard obstruction | PARTIAL-EXEC | rules present; real mobile/virtual-keyboard execution still needed |
| R4 missing states | PASS | state completeness explicit |
| R5 form UX | PASS | labels/errors/value preservation covered |
| R6 dense data workflow | PASS | tables/filters/bulk/destructive/responsive covered |
| R7 intentional brand exception | PASS | false-positive control explicit |
| R8 component-library drift | PASS | systematic design-system guidance present |
| R9 RTL/localization | PARTIAL-EXEC | RTL rules present; native-language/device validation remains |
| R10 chart accessibility | PASS | non-color cues, labels, alternatives, tooltip access covered |

### Generation
| Case | Result | Notes |
|---|---|---|
| G1 analytics dashboard | PARTIAL-EXEC | generation contract strong; rendered output still must be inspected |
| G2 healthcare informatics portfolio | PARTIAL-EXEC | portfolio rules strong; rendered output still must be inspected |
| G3 mobile insurance form | PARTIAL-EXEC | form/mobile/accessibility rules strong; rendered mobile test still needed |

### False positives
| Case | Result | Notes |
|---|---|---|
| F1 justified cards | PASS | exceptions/judgment rules prevent blanket ban |
| F2 justified animation | PASS | functional motion + reduced motion accepted |
| F3 native controls | PASS | native semantics preferred; avoids ARIA overengineering |

### Security/trust
| Case | Result | Notes |
|---|---|---|
| S1 hidden admin control | PASS | frontend visibility explicitly not authorization |
| S2 unsafe rich content | PASS | untrusted source + dangerous sink covered |
| S3 sensitive localStorage | PASS | persistent browser-readable sensitive storage covered |
| S4 open redirect | PASS | untrusted destinations/schemes covered |
| S5 file-upload false confidence | PASS | client validation explicitly non-security boundary |
| S6 telemetry leak | PASS | data minimization/redaction + no legal overclaim |
| S7 headers unavailable | PASS | runtime verification required; absence not invented |
| S8 AI output drives action | PASS | model output untrusted; confirmation/authorization boundary explicit |
| S9 supply-chain overreach | PASS | dependency vulnerability not inferred without evidence |
| S10 fail-open permission | PASS | now explicitly must-fix/highest priority |

### Cross-domain
| Case | Result | Notes |
|---|---|---|
| B1 full production audit | PASS | matrix forces reviewed/N/A/external verification |
| B2 static performance claim | PASS | runtime measurement required for CWV claims |
| B3 lint-only accessibility | PASS | executed behavior outranks lint result |
| B4 privacy/compliance overreach | PASS | review UX/privacy without inventing legal compliance |
| B5 useful logging with sensitive payload | PASS | redaction, not "remove all logging" |

### Platform/delivery
| Case | Result | Notes |
|---|---|---|
| P1 unsupported modern feature | PARTIAL-EXEC | Baseline/fallback policy present; actual target-browser test required |
| P2 hover-only action | PASS | keyboard/touch/input modality covered |
| P3 public page unindexable | PASS | discoverability section catches intent mismatch |
| P4 misleading structured data | PASS | visible-content/credibility rule explicit |
| P5 API data trusted as authority | PASS | server trust boundary explicit |
| P6 race condition | PASS | stale-response/cancel/request-order coverage added |
| P7 cross-user cache leak | PASS | sensitive/user-specific cache isolation now explicit |
| P8 hydration mismatch | PASS | server/client divergence coverage added |

## Self-test outcome

Policy/scenario coverage after fixes:
- PASS: 36
- PARTIAL-EXEC: 6
- FAIL: 0

The six PARTIAL-EXEC cases are not instruction gaps. They require actual rendering/browser/device or language validation and must not be promoted to PASS by static review.

## Release status

**NOT YET VALIDATED FOR RELEASE CLAIMS.**

Remaining mandatory evidence:
1. run the full suite with a second compatible agent/model;
2. execute/render generation cases;
3. run representative browser/mobile verification for responsive/platform cases;
4. record actual results, not expected behavior;
5. feed any new failures back into the skill and rerun.

## Conclusion

The self-test found and fixed eight concrete gaps. No known policy-level gap remains in the 42-case suite after retest, but independent-agent and runtime verification are still outstanding.


## Post-run repository hardening

Additional changes after the scenario walkthrough:
- added deterministic repository/package validator at `scripts/validate_skill.py`;
- validated current branch invariants directly against GitHub: 17 required files present, 38 consecutive checklist sections, 42 unique eval cases, package-local references valid, anti-overclaim guards present;
- added `evals/EXECUTION-GATE.md` for the six cases that require real render/browser/device evidence;
- attempted GitHub-hosted CI, but the private-repo workflow failed before any step started; the unusable automatic workflow was removed to avoid a false red quality signal.

Current structural validation result: **PASS**.
