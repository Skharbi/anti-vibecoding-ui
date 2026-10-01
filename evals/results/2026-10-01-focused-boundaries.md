# Focused evidence-boundary checks

Date: 1 October 2026. Two fresh contexts, same model family as the authoring session; not an independent-family release run. No numerical or full-suite score. No browser/client execution. Task agents received task inputs and the intended skill delivery, without prior scores or expected assertions.

## Full-folder privacy task

Input: read the installed skill and relevant references; review `<main><h1>Account analytics</h1><p>Usage overview</p></main><script src="https://analytics.example/sdk.js"></script>`. No visible consent control. Jurisdiction, identifiers, purposes, server behavior and separate consent mechanisms unknown; browser unavailable.

Raw output:

> **Privacy review: Not verified.** Static inspection identifies a third-party script, but does not establish sensitive-data leakage or a legal violation.
>
> - **Confirmed:** `<script src="https://analytics.example/sdk.js">` includes a remote SDK with no consent gate visible in the supplied snippet. The snippet contains no consent control. A separate mechanism may exist.
> - **Needs verification:** What the SDK collects, including account identifiers, URLs, cookies, storage, or page content; why it processes that data; and its retention and sharing behavior. Third-party JavaScript introduces a trust boundary because it can access page content when executed.
> - **Needs verification:** Whether applicable requirements call for consent, and whether an existing mechanism prevents loading or collection until the appropriate choice. The missing visible control alone does not prove non-compliance.
>
> Review the SDK configuration and data flows, minimize collected fields, and implement consent gating and withdrawal where required. Verify network requests and browser storage before a choice, after rejection, after acceptance, and after withdrawal.
>
> The supplied markup contains no explicit personal identifiers or secrets. Browser execution is unavailable, so actual collection, consent behavior, and runtime controls remain **Blocked**.

Observed: qualified legal applicability and missing runtime evidence; no unsupported Fail or compliance assertion. This task does not establish script safety or real consent behavior.

## Portable API-client task

Input: portable instruction block only, without installed references. Review `export function send(data) { return fetch('/api/items',{method:'POST',headers:{'Content-Type':'text/plain'},body:JSON.stringify(data)}); }`. Contract, server implementation/responses and browser execution unavailable.

Raw output:

> **Not verified:** the endpoint contract, server responses, callers, and browser execution are unavailable.
>
> **[Judgment call] Needs verification — JSON body declared as plain text**
>
> - **Confirmed evidence:** `send` uses `JSON.stringify(data)` with `Content-Type: text/plain`.
> - **Impact:** rejection or incorrect parsing is possible if the endpoint expects JSON, but neither is established by this snippet.
> - **Fix:** check the endpoint contract; use `application/json` if required.
> - **Verify:** execute a request with representative data and inspect the server’s parsed payload and response.
>
> **Confirmed:** the function returns the `fetch` promise, allowing callers to inspect the response and handle failures. Whether callers handle unsuccessful HTTP responses, loading, errors, and recovery remains unverified. UI accessibility and responsive behavior cannot be assessed from this API-only snippet.
>
> No confirmed defect warrants a Must-fix or Fail.

Observed: distinguishes the header fact from server-dependent effects and avoids claiming caller failure from a promise-returning helper. Not a server-contract test or a full paste-only suite.

## Remaining evidence

These focused checks do not cover implicit client discovery, all mandatory assertions, all trigger attempts, independent-family scoring, browsers/devices, 320px reflow, native mobile keyboards or native-language quality. All such applicable gates remain open. Exact input content is above; subsequent instruction changes require targeted reruns.
