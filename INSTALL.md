# Installation

The repository supports four usage modes. Choose the one that matches your client.

## 1. OpenAI / Codex portable plugin package

The repository root is a portable Agent Plugins package because it contains:

```
plugin.json
skills/
  anti-vibecoding-ui/
    SKILL.md
    references/
    agents/
```

Use the repository root as the plugin package when testing or distributing through an OpenAI/Codex plugin workflow.

Current status: **packaged, not published**.

The root `plugin.json` is the canonical plugin identity. Skills are discovered from the root `skills/` directory.

## 2. OpenAI hosted/local Agent Skill bundle

If you need the skill by itself rather than the whole plugin, package only:

```
skills/anti-vibecoding-ui/
```

That folder is self-contained and includes one `SKILL.md` plus its references and OpenAI skill metadata.

For OpenAI Skills APIs or sandbox capability directories, upload/mount this folder according to the current OpenAI Skills documentation.

Current status: **bundle-compatible; this repository does not claim it has been uploaded to your account**.

## 3. Other Agent Skills-compatible clients

Copy or install:

```
skills/anti-vibecoding-ui/
```

into the client's supported skills location.

Because client installation commands and UI paths can change, use that client's current documentation for the destination directory or marketplace flow.

## 4. No-install / mobile-friendly mode

Open `PASTE-TO-INSTALL.md`, copy the instruction block, and paste it as the first instruction in a new coding/design conversation.

This is intentionally a **condensed portable edition**. It does not contain every reference or evaluation rule from the full installed skill.

## Validate the repository before packaging

From a repository checkout:

```bash
python scripts/validate_skill.py
```

Expected result:

```
VALIDATION PASSED
```

## Smoke-test after installation

Use these four prompts:

1. `Review this dashboard. Something feels off about the spacing and hierarchy.`
   - Expected: skill activates.

2. `My modal works with a mouse but keyboard users get stuck.`
   - Expected: accessibility/focus issues are prioritized.

3. `Audit this frontend for security and privacy risks.`
   - Expected: security/trust-boundary rules activate, without inventing backend failures.

4. `Optimize this Postgres query.`
   - Expected: this UI skill should **not** activate unless UI impact is part of the task.

## Compatibility status

| Surface | Status | Notes |
|---|---|---|
| Portable Agent Plugins package | Packaged | Root `plugin.json` + `skills/` |
| OpenAI skill bundle | Package-compatible | Not claimed as uploaded/published |
| Codex/OpenAI skill metadata | Included | `agents/openai.yaml` |
| Generic Agent Skills clients | Structurally compatible | Client-specific install path may differ |
| Single-paste chat usage | Available | Condensed edition only |

## What installation does not prove

Successful loading does not prove:
- trigger reliability across all models;
- rendered UI quality;
- accessibility conformance;
- security compliance;
- browser compatibility.

Those are covered by the evaluation and execution gates in `evals/`.
