# anti-vibecoding-ui

An Agent Skill for Claude Code, OpenAI Codex, and compatible Agent Skills clients. It applies a 15-section anti-vibecoding UI/UX checklist to any interface work — building new UI or reviewing existing code.

## Why

Most AI-generated interfaces converge on the same look: purple-blue gradients, glassmorphism cards, pill-shaped everything, icon-box rows, buzzword headlines, scroll-triggered fade-ins. That look now signals "AI built this" more than it signals quality. This skill packages a concrete checklist to actively catch and avoid those patterns, instead of relying on taste alone.

## What it does

- **Review mode**: point it at a UI codebase and it flags checklist violations with file/line references, section by section, and confirms what already passes.
- **Generation mode**: when building new UI, it applies the checklist as constraints up front — deliberate typography and palette, specific copy, restrained icon/card/nav use, real spacing and mobile hierarchy — then self-checks the output before presenting it.

Covers: visual style, typography, headings/copy, icons, cards/containers, navigation, buttons/CTAs, animation, spacing/alignment, responsive design, component-library discipline (shadcn/ui, MUI, etc.), product-specific design, portfolio-specific pitfalls, AI/technical credibility claims, and a final "does this look vibecoded?" gut-check with an acceptance rule.

## Install

**Easiest, works on any device (recommended)**: open [`PASTE-TO-INSTALL.md`](./PASTE-TO-INSTALL.md), copy the code block, and paste it as your first message in a new Claude (or ChatGPT/Codex) chat. No file download, no repo cloning — works identically on phone, tablet, or desktop. For something that persists across conversations, paste the same content into Claude's **Settings → Skills → Add → Create a skill**.

**Claude Code / other Agent Skills clients**: copy `skills/anti-vibecoding-ui/` into your skills directory.

**OpenAI Codex** (via the stock GitHub skill installer):
```
repo: Skharbi/anti-vibecoding-ui
path: skills/anti-vibecoding-ui
```

## Structure

```
anti-vibecoding-ui/
├── README.md
├── LICENSE
├── PASTE-TO-INSTALL.md             # copy-paste install, no download needed
└── skills/
    └── anti-vibecoding-ui/
        ├── SKILL.md               # triggering + how to apply the checklist
        ├── agents/
        │   └── openai.yaml        # optional Codex UI metadata
        └── references/
            └── checklist.md       # the full 15-section checklist
```

## Status

Packaging and format compatibility (Claude Agent Skills spec, Codex skill loader) are validated. Trigger reliability, generation-mode output quality, and false-positive behavior have not yet been verified against a live agent session — an evaluation pass is in progress.

## License

MIT — use, adapt, redistribute freely.
