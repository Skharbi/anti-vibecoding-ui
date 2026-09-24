# Support

## Usage questions

For installation or usage problems:
1. read `INSTALL.md`;
2. run the smoke tests there;
3. run `python scripts/validate_skill.py` if you have a repository checkout.

When opening a support issue, include:
- client/product (ChatGPT, Codex, other Agent Skills client);
- model/version if known;
- installation mode (plugin, skill folder, paste edition);
- exact prompt that failed;
- expected behavior;
- actual behavior;
- screenshots or code only when they do not contain secrets/private data.

## Skill quality gaps

If the skill missed a UI/UX/security/accessibility issue or produced a false positive, include a minimal reproduction and propose or reference an eval case.

Behavior gaps belong in `evals/cases.md` so the fix becomes regression-tested.

## Security issues

Follow `SECURITY.md`. Do not post exploit details, credentials, or sensitive data in a public issue.

## Scope

This repository provides instructions and evaluation assets. It does not operate a hosted service and does not provide backend security, legal, accessibility-certification, or regulatory-compliance guarantees.
