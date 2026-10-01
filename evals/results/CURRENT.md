# October hardening evidence

Status: unreleased; behavioral and runtime release gates pending.

Baseline: `a10b22cad7f30bb603bd9bdadfa91b3d17ea99c0`.

The baseline validator failed on an obsolete portable-disclosure assertion. Current structural work adds real duplicate-safe YAML parsing, metadata type checks, installed-reference/anchor checks, a versioned case manifest, and text-file secret scanning independent of extensions. The deterministic suite includes 33 test methods, including nine synthetic credential-file probes. These are structural tests, not agent behavior or client discovery tests.

The follow-up validator found six additional gaps. Corrected: empty/non-object root and Codex manifests now fail with controlled diagnostics; duplicate JSON keys and malformed required-field types are rejected; optional skill field types and compatibility length are checked; deletion of portable output safeguards fails structural checks; contributor installation instructions include QA dependencies. The agent default prompt must also name the skill explicitly. Negative variants are tested in isolated copies, with valid optional metadata retained as a positive control. Guardrail checks establish text presence, not semantic obedience or behavioral quality.

Review and paste rules now distinguish confirmed Fail from incomplete verification, constrain legal/server-dependent assertions, and require individual accounting for 19 domains. Scoring now requires mandatory assertions and all trigger-attempt denominators.

Second follow-up: external, dangling and cyclic installed symlinks are rejected; internal resolved symlinks remain valid. Both the matrix and portable coverage list must contain every declared domain exactly once. Deletion of each of the 19 portable domains is tested. Malformed Markdown URLs produce controlled failures rather than tracebacks.

Four evidence-boundary cases (V1–V4) bring the manifest to 46 scenarios. They have not yet been agent-executed.

Two fresh-context boundary tasks were executed using full-folder privacy and portable API-client delivery. Both retained the intended evidence boundaries. Raw outputs and limitations are recorded in [focused checks](2026-10-01-focused-boundaries.md). These are same-family focused tasks, not completed V1–V4 suite runs or independent release scores.

Portable evaluation preparation now supports all 46 manifest cases with 56 predetermined attempts, configurable skill roots, both client layouts and both delivery modes. Five local preparation tests verify full manifest coverage, file-copy layouts, paste isolation, refusal to overwrite evidence and unknown-case rejection. Exact client paths, discovery, update and uninstall steps are documented from official client guidance. This proves preparation/layout behavior only; no coding-client execution is claimed.

Pending: actual named-client discovery/invocation/update/uninstall, complete fresh full-folder/paste behavioral runs, independent model release run, actual cross-browser/mobile-input evidence, and native-language review. Neither client CLI is installed in this workspace; paid quota is unverified. Optional hosted CI was not launched. No new aggregate scores are claimed. Historical reports and raw outputs remain unchanged and must not be used as current-revision approval.
