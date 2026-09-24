# Security Policy

## Scope

This repository contains an Agent Skill and supporting documentation. It has no production service, network server, package dependency tree, or runtime secret requirement.

Security concerns can still exist in:
- skill instructions that encourage unsafe behavior;
- prompt-injection or data-exfiltration risks;
- misleading security claims;
- bundled scripts;
- future plugin/MCP additions;
- accidental credentials or sensitive data committed to the repository.

## Reporting a vulnerability

Do not place secrets, exploit details, or sensitive user data in a public issue.

Use a private GitHub security-reporting channel when available. If private reporting is not available, contact the repository owner through a private GitHub channel before publishing exploit details.

Include:
- affected file/section;
- concrete risk;
- reproduction conditions;
- whether exploitation requires a specific model/client/tool;
- suggested remediation when known.

## Security design rules

Contributions must preserve these rules:
- no secrets or credentials in repository files;
- no instruction that treats client-side authorization as server authorization;
- no claim of OWASP/ASVS/compliance status without evidence;
- no automatic privileged action based only on model output;
- no unnecessary external dependency or remote script;
- untrusted model/retrieved/uploaded content must be treated as untrusted;
- security controls outside available evidence must be marked for external verification.

## Supported version

Until formal releases are tagged, security fixes apply to the latest `main` branch and the active hardening PR/branch.

## Dependency disclosure

The installable skill has no runtime dependencies.

The repository QA validator uses only the Python standard library.
