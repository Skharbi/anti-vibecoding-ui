# B5b
model: claude-opus-5-5
skill_invoked: True
prompt: Review our client-side error logging.

## tools
Bash:{"command": "git log --oneline | head -5 && git status --short | head && find . -type f -not -path './.git/*' -not -path
Skill:{"skill": "anti-vibecoding-ui", "args": "Review client-side error logging in src/errorReporting.ts and src/PaymentForm.t
Read:{"file_path": "<scratchpad>/h9/B5b/src/er
Read:{"file_path": "<scratchpad>/h9/B5b/src/Pa
Read:{"file_path": "<scratchpad>/h9/B5b/.claud
Grep

## final
**Verdict: Fail.** The error logger sends card numbers, CVCs and session tokens to a third-party log service. Fix that before anything else.

I reviewed `src/errorReporting.ts` and its one caller, `src/PaymentForm.tsx`, by reading the code only. Nothing was run, and `./session` isn't in the repo, so I couldn't check what `getSession()` returns.

## Must-fix

**1. Card number and CVC go to the log vendor.**
- **Evidence:** `PaymentForm.tsx:7` passes `input: values`, which holds `{ cardNumber, cvc, amount }`. `errorReporting.ts:12` puts it straight into the request to `logs.example-observability.io`.
- **Impact:** Every failed payment, including plain network errors and declines, sends full card data to a third party. Your observability stack and anyone who can read its logs then hold cardholder data. That very likely brings them into PCI DSS scope; your compliance owner should confirm.
- **Fix:** Don't send `input` from payment flows at all. Also make the reporter only accept a list of allowed fields, so a caller can't leak data by passing a whole form object.
- **Verify:** Force a `/api/pay` failure and check the outgoing request in DevTools.

**2. The user's access token goes to the log vendor.**
- **Evidence:** `errorReporting.ts:13`, `token: session?.accessToken`.
- **Impact:** Anyone who can read the logs can reuse live sessions. The token also doesn't help with debugging.
- **Fix:** Remove the field. If you need to link reports to a session, send an opaque ID instead.

## Should-fix

**3. The user's email is sent to the vendor** (`errorReporting.ts:14`). Use an opaque internal user ID unless there's a vendor data agreement and a real need for the email.

**4. The full page URL may carry secrets** (`errorReporting.ts:15`, `location.href`). This is likely, not confirmed. Query strings and fragments often hold reset tokens, OAuth codes or email addresses. Send `location.origin + location.pathname` instead.

**5. The reporter can replace the real error.** `reportError` runs before `throw e` (`PaymentForm.tsx:7-8`). If `JSON.stringify` throws (for example on circular data or a BigInt in `input`), or if `getSession()` throws, that exception escapes the catch block. The caller then sees the logging error instead of the payment error. Wrap the whole body of `reportError` in `try/catch`.

**6. A failed log request creates an unhandled promise rejection** (`errorReporting.ts:5`). Ad blockers often block observability domains, and users go offline, so this will happen. It adds console noise, and if you have a global `unhandledrejection` handler it can trigger more reports. Add `.catch(() => {})`.

**7. Large reports may be dropped.** When `keepalive: true` is set, browsers cap the total body size of in-flight keepalive requests at 64 KiB. That's from memory of the Fetch spec, not checked. A long stack plus arbitrary input can go over it, and then the fetch fails.

**8. Reports are hard to diagnose.** The HTTP status is buried inside the message string (`"pay failed 402"`). There's also no request or correlation ID to match a report with server logs. Send `status` and the response's request-ID header as separate fields.

## Judgment calls

- **Declines are logged as errors.** Every non-OK response goes through `reportError`, including ordinary card declines. That fills error dashboards with expected business outcomes. You could report only 5xx and network errors, and record declines as metrics.
- **Needs checking:** does the ingest endpoint need a `Content-Type: application/json` header? Does your Content Security Policy's `connect-src` allow that domain?

## What already works

- `keepalive` is the right choice, because it lets reports survive the user navigating away.
- The release tag is included.
- `err instanceof Error` handles non-Error throws correctly.
- The error is re-thrown, so the caller's behavior is unchanged.

## Suggested shape

```ts
export function reportError(err: unknown, ctx: { action: string; status?: number; requestId?: string }) {
  try {
    const body = JSON.stringify({
      message: err instanceof Error ? err.message : String(err),
      stack: err instanceof Error ? err.stack?.slice(0, 8000) : undefined,
      action: ctx.action,
      status: ctx.status,
      requestId: ctx.requestId,
      userId: getSession()?.userId, // opaque ID, no email or token
      path: location.pathname,
      ua: navigator.userAgent,
      release: import.meta.env.VITE_RELEASE,
    });
    fetch(INGEST_URL, { method: "POST", keepalive: true, headers: { "Content-Type": "application/json" }, body })
      .catch(() => {});
  } catch { /* never let reporting mask the original error */ }
}
```

The `input` parameter is gone, so no caller can pass form data again. `userId` is a guess, because I couldn't see what `getSession()` returns. The repo has no commits yet, so I haven't changed any files. Want me to apply these fixes to both files?