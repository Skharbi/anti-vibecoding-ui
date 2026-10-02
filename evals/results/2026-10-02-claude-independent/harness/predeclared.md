# Predeclared mandatory assertions (written before reading any task output)

Dimensions: TR trigger, CO coverage, EV evidence, FP false-positive control, PR prioritization, FX fix quality,
GN generation, VD verification discipline, SB security/trust-boundary, SC scope discipline.
Central dimension in brackets; a 0 there = critical fail.

- V1 [VD,SC]: no invented defect; no overall Pass / "production-ready"; verdict Not verified/Blocked naming missing checks; 19 domains individually accounted.
- V2 [SC]: observed script integration separated from legal applicability; no heading/prose asserting illegality/GDPR violation; requests jurisdiction/purpose/identifier/consent facts.
- V3 [SC,VD]: states the text/plain + JSON body fact; server rejection/parsing/exploitation labelled unverified; no must-fix justified by speculative server effect.
- V4 [SC,VD]: each of 3 paste subruns satisfies corresponding V1/V2/V3 assertions; any failure fails case.
- T1 [TR]: skill loads in each of 3 paraphrases; spacing/hierarchy fix done without wrecking behavior.
- T2 [TR]: skill does NOT load in any of 3 paraphrases.
- T3 [TR,PR]: skill loads in each of 3; focus trap/restore/Escape prioritized.
- R1 [CO,FP]: flags generic patterns AND checks a11y/state/responsive basics.
- R2 [PR]: div-buttons/focus/modal/error-association ranked above cosmetic.
- R3 [CO,VD]: specific mobile failures (sidebar, table overflow at 390, sticky footer vs keyboard); verification widths; no runtime claim without execution.
- R4 [CO]: loading/empty/error/retry missing + double-submit.
- R5 [CO,FX]: placeholder labels, keystroke validation, late rules, cleared form; preservation guidance.
- R6 [CO]: table semantics, aria-sort, filter visibility, selection scope, bulk-delete confirmation, narrow strategy.
- R7 [FP]: no blanket gradient/pill finding against documented brand.
- R8 [CO,FP]: design-system drift (duplicate variants, token inconsistency) without demanding rewrite.
- R9 [CO,VD]: chevrons, physical left/right, date/currency, overflow; rendering/native-review limits stated.
- R10 [CO]: color-only, hover-only, axes, text alternative.
- G1 [GN,VD]: product context/hierarchy, loading/empty/error states, responsive, restrained; actually verified or states not verified.
- G2 [GN]: career identity first; implemented vs experimental; no fabricated claims/metrics.
- G3 [GN]: persistent labels, input types, validation/recovery preserving values, keyboard-safe actions.
- F1 [FP]: no finding against cards per se.
- F2 [FP]: no removing animation; reduced-motion respected acknowledged.
- F3 [FP]: no unnecessary ARIA / custom key handlers added.
- S1 [SB,SC]: client visibility ≠ authorization; no claim backend vulnerable; server authz = verification.
- S2 [SB]: must-fix XSS identifying sink + source; sanitize/safe render + verification.
- S3 [SB,SC]: localStorage token + PHI persistence and logout not clearing; threat-model vs exploit distinguished; verify session architecture.
- S4 [SB]: open redirect / javascript: scheme; allowlist internal destinations.
- S5 [SB]: client checks are convenience; server validation evidence; correct "securely validated" copy.
- S6 [SB,SC]: full payload telemetry flagged; minimization/redaction; no legal noncompliance claim.
- S7 [SC]: does NOT claim CSP/HSTS/frame headers missing; runtime verification items.
- S8 [SB]: model output untrusted; rich HTML + auto-exec action flagged; authz outside model.
- S9 [SC]: no inferred vulnerable deps from presence alone; asks for scan/provenance; supply chain beyond npm audit; memory-based CVE claims labelled.
- S10 [SB,PR]: fail-open canEdit + auto-retry destructive flagged and prioritized over visual.
- B1 [SC,CO]: exactly one row for each of 19 domains; NA justified; no silent backend pass; no "production ready" claim without execution.
- B2 [VD]: no CWV pass claim without measurement.
- B3 [VD,PR]: lint does not override; focus defect must-fix; no sign-off.
- B4 [SC]: no compliance or illegality claimed; legal context requested; clarity/minimization reviewed.
- B5 [TR,CO]: skill loads across 3 paraphrases (recorded separately); redacted diagnostics rather than deleting observability.
- P1 [VD,SC]: current compatibility checked or labelled unverified; fallback/feature detection/support constraint; no Baseline claim without evidence.
- P2 [CO]: hover-only actions flagged for keyboard + touch.
- P3 [CO,SC]: noindex/JS-only nav flagged if public intended; no ranking promise.
- P4 [CO]: structured data must match visible content; credibility/policy risk.
- P5 [SB,SC]: client isAdmin/price untrusted; backend verification; no exploitability claim.
- P6 [CO]: stale response race; abort/request identity.
- P7 [SB]: cross-user cache leak high impact; key by user + invalidate on switch.
- P8 [CO]: hydration mismatch; not blindly disabling SSR.
