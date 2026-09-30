# October hardening evidence

Status: unreleased; behavioral and runtime release gates pending.

Baseline: `a10b22cad7f30bb603bd9bdadfa91b3d17ea99c0`.

The baseline validator failed on an obsolete portable-disclosure assertion. Current structural work adds real duplicate-safe YAML parsing, metadata type checks, installed-reference/anchor checks, a versioned case manifest, and text-file secret scanning independent of extensions. The deterministic suite includes 18 test methods, including nine synthetic credential-file probes. These are structural tests, not agent behavior or client discovery tests.

Review and paste rules now distinguish confirmed Fail from incomplete verification, constrain legal/server-dependent assertions, and require individual accounting for 19 domains. Scoring now requires mandatory assertions and all trigger-attempt denominators.

Four evidence-boundary cases (V1–V4) bring the manifest to 46 scenarios. They have not yet been agent-executed.

Pending: portable evaluation harness/CI, named-client installation and discovery tests, fresh full-folder/paste behavioral runs, independent model release run, actual cross-browser/mobile-input evidence, and native-language review. No new scores are claimed. Historical reports and raw outputs remain unchanged and must not be used as current-revision approval.
