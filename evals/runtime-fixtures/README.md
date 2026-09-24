# Runtime Fixtures

These fixtures support the six execution-gated cases in `../EXECUTION-GATE.md`.

They are **not** proof by themselves. They exist so browser/device testing is reproducible.

## Files

- `r3-responsive.html` — responsive table/form/footer behavior.
- `r9-rtl.html` — Arabic/RTL, bidi, logical properties, text expansion.
- `g1-dashboard.html` — product-specific dashboard with loaded/empty/error states.
- `g2-portfolio.html` — healthcare informatics portfolio hierarchy.
- `g3-mobile-form.html` — mobile authorization form labels/focus/action visibility.
- `p1-browser-feature.html` — feature detection + fallback for a modern browser API.

## Suggested local run

From this directory:

```bash
python -m http.server 8765
```

Then open the fixture URLs in representative browsers/devices.

## Evidence to record

For each fixture:
- browser/version;
- OS/device/emulator;
- viewport;
- screenshot or reproducible observation;
- pass/fail against `../EXECUTION-GATE.md`;
- any defect found.

## Current environment note

On 2026-09-24, the authoring environment could not complete a local Chromium headless session even for a one-line HTML file. An external headless Chromium renderer was also attempted but was blocked by zero available rendering credits.

Therefore these fixtures are committed as reproducible inputs, but runtime PASS claims remain open until executed successfully in a working browser environment.
