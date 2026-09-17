# anti-vibecoding-ui

A Claude Code / Claude skill that applies a 15-section anti-vibecoding UI/UX checklist to any interface work — building new UI or reviewing existing code.

## Why

Most AI-generated interfaces converge on the same look: purple-blue gradients, glassmorphism cards, pill-shaped everything, Lucide icons in threes, buzzword headlines, scroll-triggered fade-ins. That look now signals "AI built this" more than it signals quality. This skill packages a concrete checklist to actively catch and avoid those patterns, instead of relying on taste alone.

## What it does

- **Review mode**: point it at a UI codebase and it flags checklist violations with file/line references, section by section, and confirms what already passes.
- **Generation mode**: when building new UI, it applies the checklist as constraints up front — deliberate typography and palette, specific copy, restrained icon/card/nav use, real spacing and mobile hierarchy — then self-checks the output before presenting it.

Covers: visual style, typography, headings/copy, icons, cards/containers, navigation, buttons/CTAs, animation, spacing/alignment, responsive design, component-library discipline (shadcn/ui, MUI, etc.), product-specific design, portfolio-specific pitfalls, AI/technical credibility claims, and a final "does this look vibecoded?" gut-check with an acceptance rule.

## Install

Download `anti-vibecoding-ui.skill` and use the "Save skill" option in Claude, or drop the `anti-vibecoding-ui/` folder into your skills directory (`SKILL.md` + `references/checklist.md`).

## Structure

```
anti-vibecoding-ui/
├── SKILL.md                  # triggering + how to apply the checklist
└── references/
    └── checklist.md          # the full 15-section checklist
```

## License

MIT — use, adapt, redistribute freely.
