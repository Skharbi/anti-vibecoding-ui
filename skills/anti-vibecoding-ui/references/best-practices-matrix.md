# Best-Practice Coverage Matrix

Use this matrix to prevent blind spots and scope confusion. The skill is UI/frontend-centered, but a production review must identify adjacent risks and explicitly hand them off when evidence lives elsewhere.

| Domain | Primary baseline | What this skill should check | Boundary / escalation |
|---|---|---|---|
| Product/UX | Product workflow + established usability heuristics | task clarity, hierarchy, states, recovery, action consequences | user research/product strategy may require separate evidence |
| Accessibility | WCAG 2.2 + WAI-ARIA/APG | semantics, keyboard, focus, names, contrast, motion, forms, widgets | formal conformance and AT matrix require dedicated testing |
| Cybersecurity | OWASP Top 10:2025, ASVS 5.0.0, WSTG 4.2, Cheat Sheets | client trust boundaries, XSS sinks, auth UX, sensitive-data handling, uploads, redirects, browser policy assumptions | APIs, servers, cloud, penetration tests, crypto, authorization enforcement need backend/runtime review |
| Secure SDLC | NIST SSDF 1.1 | security requirements, dependency restraint, provenance awareness, secure defaults, verification evidence | org CI/CD, signing, release provenance need pipeline access |
| Privacy | NIST Privacy Framework (stable 1.0; track newer drafts separately) | data minimization, transparency, telemetry, consent UX, browser storage, sensitive URLs/logging | legal/regulatory compliance needs jurisdiction-specific review |
| Performance | Core Web Vitals + browser/platform guidance | perceived latency, responsive media, layout shift, main-thread-heavy UI, list rendering | actual LCP/INP/CLS require runtime measurement |
| Responsive | CSS/platform behavior + real viewport testing | narrow mobile, tablet, desktop, keyboard/viewport obstruction, dense data strategies | device/browser matrix requires executed testing |
| Internationalization | Unicode/locale/platform conventions | text expansion, locale formats, RTL, bidi safety, truncation | translation quality/cultural review needs native-language validation |
| Design systems | project tokens/components + component contracts | reuse, variants, state consistency, avoiding duplicate near-components | brand governance may require design-owner decision |
| Reliability | defensive UI state handling | partial failures, retries, optimistic rollback, stale data, offline/reconnect, idempotency assumptions | distributed-system reliability needs backend/infra review |
| Testing | project test strategy + behavioral verification | representative states, keyboard, responsive, error-path, regression fixtures | cannot claim coverage without executable test results |
| Observability | privacy-aware client diagnostics | useful error context, correlation identifiers, redaction, actionable user feedback | backend logs/alerts/SLOs require ops access |
| Content/credibility | source evidence + product truth | no fabricated metrics, capabilities, compliance, AI claims | factual claims may require domain/source verification |
| AI interfaces | secure action boundaries + human factors | untrusted model output, confirmation, provenance, uncertainty, failure/partial-action states | model evals, prompt security, tool authorization require AI/backend review |
| Regulated workflows | applicable domain rules | conservative UX, data minimization, clear responsibility/decision boundaries | legal, clinical, financial, regulatory sign-off is out of scope |
| Browser/platform compatibility | MDN Baseline + progressive enhancement | feature support, fallbacks, input modality assumptions, client-only failure modes | full browser/device matrix requires executed testing |
| Public discoverability | Google Search Essentials + page metadata/indexability | titles, canonical intent, crawlable links, accidental noindex/auth blocking, truthful structured data | search ranking/index status requires deployment/Search Console evidence |
| API client boundary | OWASP API Security Top 10 2023 + app contract | untrusted API data, object IDs/roles as untrusted client input, retry/rate-limit/error behavior | server authorization, validation, inventory and rate limiting require API/backend review |
| Rendering/cache/concurrency | framework/runtime contracts | hydration, stale user state, race conditions, duplicate actions, sensitive caching, optimistic reconciliation | CDN/edge/server cache behavior requires deployment/runtime evidence |

## How to use the matrix

For a "full production review":
1. scan every domain;
2. mark it **reviewed**, **not applicable**, or **requires external verification**;
3. never silently convert "not visible in frontend code" into "pass";
4. prioritize confirmed user/security failures over speculative architecture concerns;
5. record external-verification items in the final report.

## Evidence levels

Use these labels where helpful:
- **Confirmed** — directly evidenced in code or executed behavior.
- **Likely** — strong evidence exists but runtime/server behavior is not visible.
- **Needs verification** — important control sits outside available evidence.
- **Not applicable** — genuinely irrelevant to the product/flow.

## Anti-overreach rule

This skill should be broad in **coverage**, not careless in **claims**.

It may identify that CSP, server authorization, rate limiting, secure cookie flags, dependency provenance, logging alerts, or backend validation need verification. It must not claim those controls are absent merely because they are not visible in a frontend file.
