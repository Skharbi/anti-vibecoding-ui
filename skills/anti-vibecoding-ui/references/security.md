# Cybersecurity & Trust Reference

Use this reference when a frontend/UI review touches authentication, authorization, user-supplied content, sensitive data, uploads/downloads, external links, third-party code, browser storage, admin workflows, payments, healthcare/regulated data, or any production-facing application.

This is **not a penetration-testing license** and does not replace backend, infrastructure, cloud, API, dependency, or runtime security testing. The skill must clearly separate:
- what is directly evidenced in frontend code;
- what is an architectural/security assumption;
- what requires backend/runtime verification.

## Primary baselines

Use these as the main security references:
- OWASP Top 10:2025 for current web application risk categories.
- OWASP ASVS 5.0.0 for verification requirements.
- OWASP WSTG v4.2 as the stable web-security testing guide; latest/dev content may be consulted but should not be treated as a stable release.
- OWASP Cheat Sheet Series for implementation guidance.
- NIST SP 800-218 SSDF 1.1 for secure software-development practices.

## 1. Trust boundaries and authorization

- Never assume hiding or disabling a control is authorization.
- Client-side role/permission checks are UX only unless the server independently enforces them.
- Flag object IDs, route params, query params, and action payloads that appear to control access to other users' resources without evidence of server-side authorization.
- Distinguish authentication ("who are you?") from authorization ("may you do this?").
- Privileged/admin actions need explicit server-side authorization assumptions called out.
- Do not expose sensitive fields simply because the UI hides them after fetch.

## 2. Authentication and session handling

Review for:
- secrets/tokens embedded in client code or public environment variables;
- long-lived credentials in browser-readable storage without a justified threat model;
- session-expiry handling that fails open;
- login/logout/account-switching state confusion;
- re-authentication requirements for high-risk actions;
- predictable or insecure recovery flows visible in the UI;
- sensitive information disclosed by login/reset error messages;
- missing CSRF assumptions for cookie-authenticated state-changing requests.

Do not claim session security from frontend code alone. Cookie attributes, session rotation, server invalidation, and token verification usually require backend/runtime evidence.

## 3. XSS and unsafe rendering

Flag high-risk sinks/patterns:
- React `dangerouslySetInnerHTML`;
- DOM `innerHTML`, `outerHTML`, `insertAdjacentHTML`;
- `document.write`;
- unsafe Markdown/HTML rendering;
- untrusted URLs assigned to navigation/resource attributes without validation;
- dynamic script execution such as `eval` or equivalent string-to-code behavior;
- framework-specific escaping bypasses.

Require contextual output encoding or sanitization when rendering untrusted content.

Treat Content Security Policy and Trusted Types as defense-in-depth, not substitutes for safe rendering.

## 4. Injection and untrusted input

Frontend validation improves UX but is not a security boundary.

Check for:
- direct interpolation of untrusted data into HTML, CSS, JS, URLs, templates, or commands;
- dangerous URL schemes such as `javascript:` where applicable;
- unsafe redirect targets;
- query parameters reflected into sensitive sinks;
- client-side assumptions that "validated here" means "safe on server."

Explicitly state when server-side validation, parameterization, or allowlisting must be verified elsewhere.

## 5. CSRF and state-changing requests

When cookie-based authentication is used or implied:
- identify state-changing requests;
- do not assume CORS prevents CSRF;
- verify there is an anti-CSRF strategy or document that backend verification is required;
- high-impact actions should not be accidentally triggerable via GET-like navigation;
- UI confirmation is not a CSRF control.

## 6. Sensitive data and privacy

Check whether the frontend unnecessarily:
- stores sensitive data in localStorage/sessionStorage/indexedDB;
- puts sensitive values in URLs, route params, query strings, analytics events, client logs, error reports, clipboard, or page source;
- renders more personal data than the task requires;
- caches sensitive data in ways the app cannot reliably clear;
- exposes secrets in source maps or client bundles.

For healthcare, financial, identity, or regulated data, treat unnecessary client exposure as a high-severity concern.

## 7. Browser storage and caching

- Do not treat browser storage as a secure secret vault.
- Avoid storing bearer tokens or high-value sensitive data in readable persistent storage without an explicit threat model.
- Clear user-specific client state on logout/account switch where necessary.
- Consider back/forward cache and browser history for sensitive views.
- Ensure downloaded/generated sensitive files have an appropriate lifecycle and are not silently retained in app state longer than needed.

## 8. File upload and download

Review for:
- accepted type/size guidance;
- server-side validation assumptions;
- dangerous inline preview of untrusted active content;
- executable/scriptable file types;
- filename/path handling assumptions;
- upload progress, cancellation, retry, and failure;
- user understanding of who can access the uploaded file;
- generated/downloaded file integrity and sensitivity.

Client-side MIME/extension checks are convenience controls only; server-side validation is required.

## 9. External links, redirects, and embedded content

- Validate or constrain untrusted redirect destinations.
- Avoid open-redirect patterns.
- Treat externally supplied URLs as untrusted.
- For new-tab links, use platform/framework-safe behavior and avoid giving the opened page unnecessary control of the opener.
- Review iframe/embed trust, sandboxing, permissions, and whether embedding is needed.
- Flag insecure mixed-content assumptions.
- Avoid embedding third-party content that silently expands privacy/security exposure.

## 10. Security headers and browser policy

Frontend code may reveal missing assumptions but usually cannot prove deployment headers.

When relevant, require runtime verification of:
- Content-Security-Policy;
- frame-embedding protections;
- MIME sniffing protections;
- referrer policy;
- permissions policy;
- HSTS on HTTPS deployments where appropriate.

Do not claim these are configured from source inspection unless deployment configuration is actually available.

## 11. Third-party scripts and supply chain

- Every dependency/script should have a real product reason.
- Avoid loading remote scripts for trivial UI effects.
- Flag unpinned/untrusted remote resources where integrity/provenance matters.
- Review analytics/chat/widgets for data leakage and privilege.
- Do not recommend a new dependency when the platform/browser already provides the capability.
- Treat dependency vulnerability status and CI/CD provenance as separate verification work when not visible in the UI repo.

OWASP Top 10:2025 explicitly includes software supply-chain failures; the skill must not reduce supply-chain review to `npm audit` alone.

## 12. Secrets and configuration

Flag:
- API keys/tokens/private credentials in client source;
- secrets in public environment-variable namespaces;
- credentials committed to fixtures/examples;
- admin/debug features protected only by UI hiding;
- environment confusion that points production users to test systems or vice versa.

Public identifiers and publishable client keys must not be mislabeled as secrets; understand the provider's model before reporting.

## 13. Error handling and exceptional conditions

The 2025 OWASP Top 10 includes mishandling of exceptional conditions.

Review:
- fail-open permission states;
- UI proceeding after partial/failed authorization;
- stale optimistic state after server rejection;
- sensitive stack traces or internal identifiers exposed to users;
- retry loops that duplicate high-impact operations;
- inconsistent state after timeout/cancellation;
- recovery after interrupted uploads/submissions;
- null/undefined/partial-data paths.

Security and UX overlap here: confusing failure handling can become a real security flaw.

## 14. Logging, analytics, and telemetry

Flag client-side telemetry that may include:
- passwords/tokens;
- full request/response bodies with sensitive data;
- personal identifiers beyond what is needed;
- healthcare/financial data;
- security answers;
- raw form fields;
- unredacted error context.

Do not assume "analytics" is harmless. Privacy, retention, access, and third-party transfer matter.

## 15. Clickjacking and UI redress

For sensitive flows:
- consider whether the app may be embedded unexpectedly;
- require runtime verification of frame protections when risk is material;
- do not invent client-side visual tricks as a substitute for proper frame policy.

## 16. High-risk workflows

Apply extra scrutiny to:
- password/email/phone changes;
- MFA enrollment/removal;
- payment/account changes;
- role/permission administration;
- exports/downloads of sensitive datasets;
- deletion;
- consent changes;
- healthcare/financial decisions;
- API-key management.

Require clear identity, consequence, re-authentication where appropriate, confirmation proportional to risk, and reliable server-side authorization.

## 17. AI-specific security and trust

When the UI handles model output or agent/tool actions:
- treat model output as untrusted content;
- sanitize/encode rendered rich content;
- distinguish model suggestions from verified facts/actions;
- show tool/action boundaries and confirmation for consequential operations;
- do not allow prompt/model output to silently trigger privileged actions;
- prevent secret/system-prompt leakage through client code;
- keep authorization checks outside the model;
- surface failures/partial execution clearly;
- treat uploaded/retrieved external content as untrusted input.

## 18. Security review output

Security findings must include:
- evidence;
- affected trust boundary;
- plausible impact;
- whether the issue is confirmed or requires backend/runtime verification;
- remediation direction;
- verification method.

Never say "secure", "OWASP compliant", or "ASVS compliant" based on a frontend-only review.

## Security acceptance rule

A frontend security review passes only when:
- no confirmed high-impact client-side flaw remains;
- trust boundaries are explicit;
- client-side controls are not mistaken for server security;
- sensitive data exposure is minimized;
- untrusted content is handled safely;
- high-risk actions fail safely;
- unresolved backend/runtime assumptions are documented rather than silently accepted.
