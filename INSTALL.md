# Installation

You only need to choose **one** installation path.

## Which one should I use?

| Your situation | Recommended path |
|---|---|
| You are on mobile, ChatGPT, Claude, or another normal chat and just want to try it | **Option A — Paste and use** |
| Your coding client supports Agent Skills folders | **Option B — Install the full skill folder** |
| You are building with the OpenAI Skills API | **Option C — Upload the skill bundle** |
| You specifically want a Codex/OpenAI plugin package | **Option D — Use the repository root** |

If you are unsure, use **Option A**.

---

## Option A — Paste and use

This is the easiest path and works without a terminal.

1. Open **[PASTE-TO-INSTALL.md](PASTE-TO-INSTALL.md)**.
2. Copy the text inside the large code block.
3. Paste it as the first instruction in a new coding/design conversation.
4. Then ask the AI to review, build, redesign, or fix your UI.

Example:

```text
Review this dashboard using the Anti-Vibecoding UI protocol.
```

This is a **condensed portable edition**. It is useful for quick/mobile use, but it does not include every reference file and evaluation rule from the full installed skill.

---

## Option B — Install the full skill folder

Use this when your coding client supports Agent Skills.

The complete skill is this folder:

```text
skills/anti-vibecoding-ui/
```

That folder is self-contained. Keep the whole folder together because `SKILL.md` links to the files inside `references/`.

The important structure is:

```text
anti-vibecoding-ui/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── checklist.md
    ├── review-protocol.md
    ├── component-behavior.md
    ├── security.md
    ├── best-practices-matrix.md
    └── sources.md
```

Install or copy that folder into the skills location supported by your client.

Because different clients use different install locations and those UI paths can change, follow your client's current Agent Skills instructions for where to place the folder.

After installation, start a **new session** so the client can rediscover the skill.

---

## Option C — OpenAI Skills API

OpenAI Skills accept a skill directory or a ZIP containing one top-level skill folder. The canonical bundle in this repository is:

```text
skills/anti-vibecoding-ui/
```

If you are using the OpenAI Skills API, upload that folder or a ZIP made from that folder. OpenAI's current Skills documentation describes directory upload and ZIP upload workflows.

This repository does **not** require any API key of its own and does not make network calls at runtime.

Official OpenAI documentation:
https://developers.openai.com/api/docs/guides/tools-skills

---

## Option D — Codex/OpenAI plugin package

Use this only if you specifically want the project packaged as a plugin rather than as a standalone skill.

Use the **repository root** because it contains:

```text
plugin.json
.codex-plugin/plugin.json
skills/
```

The standalone skill itself still lives at:

```text
skills/anti-vibecoding-ui/
```

If all you want is the skill, use Option B instead.

---

## Quick smoke test

After installation, try these prompts:

1. `Review this dashboard. Something feels off about the spacing and hierarchy.`
2. `My modal works with a mouse but keyboard users get stuck.`
3. `Audit this frontend for security and privacy risks.`
4. `Optimize this Postgres query.`

Expected behavior:

- prompts 1–3 should activate the UI skill;
- prompt 4 should **not** activate it unless the query has a real user-interface impact.

---

## For contributors only: validate the repository

You do **not** need this step just to use the skill.

If you cloned the repository and are modifying it, run:

```bash
python scripts/validate_skill.py
```

Expected result:

```text
VALIDATION PASSED
```

---

## What installation does not prove

Installing the skill successfully does not prove accessibility conformance, security compliance, universal browser support, or production readiness.

Those claims require the evaluation and execution evidence documented under `evals/`.
