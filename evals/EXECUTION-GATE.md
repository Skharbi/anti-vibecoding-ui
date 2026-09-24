# Execution Validation Gate

Six cases cannot be closed by static instruction review alone.

## R3 responsive failure
Execute at 390px, tablet, desktop, and with a mobile virtual keyboard. Pass only with no accidental overflow, no covered critical action, and an intentional narrow-screen data strategy.

## R9 RTL/localization
Render Arabic/RTL with long Arabic labels, mixed Arabic/English text, localized dates/numbers, and directional icons. Pass only if direction, icon mirroring, bidi text, and text expansion remain usable.

## G1 generated analytics dashboard
Generate, then render desktop and 390px. Pass only if hierarchy is product-specific, loading/empty/error states exist, keyboard/focus works, and mobile is intentionally restructured.

## G2 generated healthcare portfolio
Generate and render desktop/mobile. Pass only if career identity leads, professional work is distinct from personal AI projects, claims are accurate, and evidence outranks startup-style decoration.

## G3 generated mobile insurance form
Render narrow mobile and operate with keyboard/touch. Pass only if labels persist, validation preserves values, actions remain visible above the keyboard, recovery is clear, and focus order is logical.

## P1 browser compatibility
Use a fixture with a deliberately limited/new platform feature. Verify current compatibility and representative supported browsers. Pass only if support is known and a fallback, feature detection, or explicit support constraint exists.

## Recording requirement
Record date, model, browser/device or emulator, viewport, fixture/commit, result, and reproducible evidence. Do not convert PARTIAL-EXEC to PASS without execution evidence.
