# B5c
model: claude-opus-5-5
skill_invoked: True
prompt: Review our client-side error logging.

## tools
Bash:{"command": "git log --oneline | head -5 && git status --short | head && find . -path ./.git -prune -o -type f -print | 
Skill:{"skill": "anti-vibecoding-ui", "args": "Review client-side error logging in src/errorReporting.ts and its use in src/Pa
Read:{"file_path": "<scratchpad>/h9/B5c/src/er
Read:{"file_path": "<scratchpad>/h9/B5c/src/Pa
Read:{"file_path": "<scratchpad>/h9/B5c/.claud
Read:{"file_path": "<scratchpad>/h9/B5c/.claud

## final
I reviewed `src/errorReporting.ts` and the one place it's used, `src/PaymentForm.tsx`. This was a read-only review: the repo has no commits, no `package.json` and no `src/session.ts`, so nothing could be run. Every finding comes from reading the code.

**Result: Fail.** The error logger sends card details and login tokens to an outside logging service.

## Must fix

**1. Full card number and CVC go to the outside logging service**
- **Evidence:** `PaymentForm.tsx:7` passes `input: values`, which is `{ cardNumber, cvc, amount }`. `errorReporting.ts:12` then writes that `input` into the request body sent to `logs.example-observability.io`.
- **Impact:** Every failed payment copies card data into a third party's log store. Anyone with access to those logs can read it, and the logs may be kept and indexed for a long time. Keeping CVCs is a serious PCI DSS risk; check this against your actual PCI scope.
- **Fix:** Drop `input: values` from the payment code. More broadly, remove the free-form `input?: unknown` field from `reportError`. It invites callers to dump raw form data, so replace it with a short list of allowed fields (for example `{ action, status, amount? }`).
- **Verify:** Force `/api/pay` to return a 500 and inspect the logging request in DevTools. It should contain no card number or CVC.

**2. The session's access token is sent with every error**
- **Evidence:** `errorReporting.ts:13` sends `token: session?.accessToken`.
- **Impact:** Anyone who can read the logs, or a compromised logging vendor, can reuse that token to act as the user for as long as it stays valid. The logs gain nothing from having the credential itself.
- **Fix:** Remove it. If you need to link errors to sessions, send an opaque session or user ID created for that purpose.
- **Verify:** Trigger any error and check that no token appears in the request.

## Should fix

**3. Email address sent to a third party** (`errorReporting.ts:14`). This is personal data the logs don't need. Use an internal user ID instead.

**4. `location.href` is sent with its query string and fragment** (`errorReporting.ts:15`). If an error happens on a page like password reset, magic link, OAuth callback or checkout return, the URL may carry a token or code. Send only `location.origin + location.pathname`, or allow specific query parameters.

**5. The logger can replace the real payment error** (`errorReporting.ts:8`). `JSON.stringify` throws on circular objects and `BigInt` values. If that happens inside the `catch` at `PaymentForm.tsx:6-8`, the caller gets that `TypeError` instead of the real payment failure. Wrap everything inside `reportError` in `try/catch` so logging can never throw.

**6. A failed log request is never handled** (`errorReporting.ts:5`). The `fetch` has no `.catch`. Ad blockers often block logging domains, so every reported error can also cause an unhandled promise rejection. If a global `unhandledrejection` handler also calls `reportError`, this could loop; I found no such handler in this repo. Fix: add `.catch(() => {})`.

**7. No limit on how often errors are sent.** An error that repeats in a render loop will send a request every time. Add a simple limit or skip repeated identical errors (for example, by message and action within a short time window).

**8. Large reports may never arrive.** Browsers cap `keepalive` request bodies at about 64 KB total, so a long stack trace or large payload makes the request fail. Truncate `stack` and `message` before sending.

## Things to check outside this code
- **Card data reaching your own server.** `PaymentForm.tsx:4` posts the raw card number and CVC to `/api/pay`. If you use a payment provider, its hosted fields or tokenization would keep card data off your servers entirely. That is a product and PCI-scope decision for you, not a logging bug.
- **Double charges on retry.** The payment request has no idempotency key, so retrying after a timeout could charge twice. This depends on how the backend handles duplicates.
- **The logging vendor itself:** how long it keeps data and who can access it. After fixing items 1 and 2, find and delete any card numbers, CVCs or tokens it has already received.

## What already works
- `keepalive: true` is the right way to make sure reports sent while the page closes still arrive.
- Including the release version (`release`) and the browser (`ua`) is useful for tracking down bugs.
- `PaymentForm` rethrows the error after logging it, so the caller still sees the failure.
- The error message `pay failed ${status}` contains no sensitive data.

## Suggested shape

```ts
import { getSession } from "./session";

type ErrorContext = { action: string; status?: number };

export function reportError(err: unknown, context: ErrorContext) {
  try {
    const e = err instanceof Error ? err : new Error(String(err));
    fetch("https://logs.example-observability.io/ingest", {
      method: "POST",
      keepalive: true,
      body: JSON.stringify({
        message: e.message.slice(0, 500),
        stack: e.stack?.slice(0, 8000),
        action: context.action,
        status: context.status,
        userId: getSession()?.userId, // opaque ID, not email or token
        path: location.origin + location.pathname,
        ua: navigator.userAgent,
        release: import.meta.env.VITE_RELEASE,
      }),
    }).catch(() => {});
  } catch {
    // reporting must never throw
  }
}
```

This assumes the session object has a `userId`. I couldn't confirm that because `src/session.ts` isn't in the repo. The limit on repeated errors (item 7) isn't included in this sketch.

Should I apply these fixes to both files?