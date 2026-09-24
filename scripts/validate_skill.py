#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "anti-vibecoding-ui"
errors = []

def read(path: Path) -> str:
    if not path.exists():
        errors.append("missing: " + str(path.relative_to(ROOT)))
        return ""
    return path.read_text(encoding="utf-8")

required = [
    ROOT/"README.md", ROOT/"LICENSE", ROOT/"HANDOVER.md", ROOT/"PASTE-TO-INSTALL.md",
    ROOT/"INSTALL.md", ROOT/"SECURITY.md", ROOT/"CONTRIBUTING.md", ROOT/"CHANGELOG.md",
    ROOT/"RELEASE.md", ROOT/"AGENTS.md", ROOT/".github"/"PULL_REQUEST_TEMPLATE.md",
    ROOT/"plugin.json", ROOT/".codex-plugin"/"plugin.json",
    SKILL/"SKILL.md", SKILL/"agents"/"openai.yaml",
    SKILL/"references"/"checklist.md", SKILL/"references"/"review-protocol.md",
    SKILL/"references"/"component-behavior.md", SKILL/"references"/"security.md",
    SKILL/"references"/"best-practices-matrix.md", SKILL/"references"/"sources.md",
    ROOT/"evals"/"README.md", ROOT/"evals"/"cases.md", ROOT/"evals"/"EXECUTION-GATE.md"
]
for path in required:
    read(path)

skill = read(SKILL/"SKILL.md")
checklist = read(SKILL/"references"/"checklist.md")
cases = read(ROOT/"evals"/"cases.md")
readme = read(ROOT/"README.md")
paste = read(ROOT/"PASTE-TO-INSTALL.md")
protocol = read(SKILL/"references"/"review-protocol.md")
handover = read(ROOT/"HANDOVER.md")
changelog = read(ROOT/"CHANGELOG.md")
openai_yaml = read(SKILL/"agents"/"openai.yaml")

# SKILL.md frontmatter / OpenAI skill constraints.
if not skill.startswith("---\n"):
    errors.append("SKILL.md missing frontmatter")
fm = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if not fm:
    errors.append("SKILL.md frontmatter is unclosed or malformed")
    frontmatter = ""
else:
    frontmatter = fm.group(1)

name_match = re.search(r"^name:\s*([^\n]+)$", frontmatter, re.M)
desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
skill_name = name_match.group(1).strip() if name_match else ""
skill_desc = desc_match.group(1).strip() if desc_match else ""

if skill_name != "anti-vibecoding-ui":
    errors.append("invalid skill name")
if not skill_desc:
    errors.append("skill description missing")
elif len(skill_desc) > 1024:
    errors.append(f"skill description exceeds 1024 chars: {len(skill_desc)}")
if fm and not skill[fm.end():].strip():
    errors.append("skill body is empty")

# Root portable plugin manifest.
try:
    plugin = json.loads(read(ROOT/"plugin.json"))
except Exception as exc:
    plugin = {}
    errors.append("plugin.json invalid JSON: " + str(exc))

if plugin:
    if plugin.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("plugin.json schema is missing or unexpected")
    plugin_name = plugin.get("name")
    version = plugin.get("version")
    description = plugin.get("description")
    if plugin_name != "anti-vibecoding-ui":
        errors.append("plugin name must be anti-vibecoding-ui")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?", version or ""):
        errors.append("plugin version must be semantic version")
    if not isinstance(description, str) or not description.strip():
        errors.append("plugin description missing")
    if len((plugin_name or "") + ":" + skill_name) > 64:
        errors.append("combined plugin:skill identity exceeds 64 chars")
    if version and f"## [{version}]" not in changelog:
        errors.append("CHANGELOG does not contain plugin version " + version)
    if version and f"Current package version:** `{version}`" not in readme:
        errors.append("README package version does not match plugin.json")

# Codex compatibility manifest must match the portable root manifest.
try:
    codex_plugin = json.loads(read(ROOT/".codex-plugin"/"plugin.json"))
except Exception as exc:
    codex_plugin = {}
    errors.append(".codex-plugin/plugin.json invalid JSON: " + str(exc))

if plugin and codex_plugin:
    if codex_plugin.get("name") != plugin.get("name"):
        errors.append("Codex compatibility plugin name does not match root plugin.json")
    if codex_plugin.get("version") != plugin.get("version"):
        errors.append("Codex compatibility plugin version does not match root plugin.json")
    if codex_plugin.get("skills") != "./skills/":
        errors.append("Codex compatibility manifest must point skills to ./skills/")

# Installable skill must be self-contained.
if "evals/" in skill:
    errors.append("installable SKILL.md must not reference repo-root evals")
for ref in re.findall(r"references/([A-Za-z0-9_-]+\.md)", skill):
    if not (SKILL/"references"/ref).exists():
        errors.append("missing package reference: " + ref)

# OpenAI agent metadata contract.
if "interface:" not in openai_yaml:
    errors.append("agents/openai.yaml missing interface")
for key in ["display_name:", "short_description:"]:
    if key not in openai_yaml:
        errors.append("agents/openai.yaml missing " + key.rstrip(":"))
if "products:" not in openai_yaml or "CHAT" not in openai_yaml or "CODEX" not in openai_yaml:
    errors.append("agents/openai.yaml must declare CHAT and CODEX products")
if "allow_implicit_invocation: true" not in openai_yaml:
    errors.append("agents/openai.yaml should allow implicit invocation")

# Checklist / eval contracts.
nums = [int(x) for x in re.findall(r"^##\s+(\d+)\.\s+", checklist, re.M)]
if nums != list(range(1, 39)):
    errors.append("checklist numbering is not consecutive 1..38")

ids = re.findall(r"^###\s+([A-Z]+\d+)\s+—", cases, re.M)
if len(ids) != 42:
    errors.append("expected 42 eval cases, found " + str(len(ids)))
if len(ids) != len(set(ids)):
    errors.append("duplicate eval case IDs")

# Documentation consistency.
if "38 review areas" not in readme or "42 regression scenarios" not in readme:
    errors.append("README counts are stale")
if "\\n" in readme:
    errors.append("README contains escaped newline text")
if "28 checklist sections" in protocol or "34 checklist sections" in protocol:
    errors.append("review protocol contains stale checklist count")
if "Adding a JS/Python test harness" in handover:
    errors.append("handover contradicts current validator architecture")
if "condensed portable edition" not in paste.lower() or "canonical/full version" not in paste.lower():
    errors.append("portable edition disclosure missing")

priority_block = paste.split("PRIORITY ORDER", 1)[1].split("MANDATORY AREAS TO CONSIDER", 1)[0] if "PRIORITY ORDER" in paste and "MANDATORY AREAS TO CONSIDER" in paste else ""
priority_nums = [int(x) for x in re.findall(r"^(\d+)\.\s+", priority_block, re.M)]
if priority_nums != list(range(1, 11)):
    errors.append("portable priority list numbering is invalid")

# Guardrails that must not regress.
security = read(SKILL/"references"/"security.md")
matrix = read(SKILL/"references"/"best-practices-matrix.md")
if "OWASP compliant" not in security or "ASVS compliant" not in security:
    errors.append("security anti-overclaim guard missing")
if "requires external verification" not in (skill + matrix):
    errors.append("external-verification boundary missing")
if "semantic HTML before ARIA" not in skill and "native HTML semantics before ARIA" not in skill:
    errors.append("native-semantics rule missing")

# Basic repository hygiene.
secret_patterns = [
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    r"\bsk-proj-[A-Za-z0-9_-]{20,}\b",
    r"\bghp_[A-Za-z0-9]{20,}\b"
]
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    if path.suffix.lower() not in {".md", ".yaml", ".yml", ".py", ".txt", ".json"}:
        continue
    body = path.read_text(encoding="utf-8", errors="ignore")
    for pattern in secret_patterns:
        if re.search(pattern, body):
            errors.append("possible secret in " + str(path.relative_to(ROOT)))

# Relative markdown links in repository docs must resolve.
for md in [
    ROOT/"README.md", ROOT/"INSTALL.md", ROOT/"SECURITY.md",
    ROOT/"CONTRIBUTING.md", ROOT/"CHANGELOG.md", ROOT/"RELEASE.md",
    ROOT/"AGENTS.md", ROOT/"HANDOVER.md",
    ROOT/"PASTE-TO-INSTALL.md", ROOT/"evals"/"README.md"
]:
    body = read(md)
    for target in re.findall(r"\[[^\]]+\]\((?!https?://|#)([^)]+)\)", body):
        clean = target.split("#", 1)[0]
        if clean and not (md.parent/clean).resolve().exists():
            errors.append(f"broken relative markdown link in {md.relative_to(ROOT)}: {target}")

if errors:
    print("VALIDATION FAILED")
    for error in errors:
        print("- " + error)
    sys.exit(1)

print("VALIDATION PASSED")
print("required files:", len(required))
print("plugin version:", plugin.get("version"))
print("skill description chars:", len(skill_desc))
print("checklist sections:", len(nums))
print("evaluation cases:", len(ids))
print("package-local references: OK")
print("agent metadata: OK")
print("documentation consistency: OK")
print("secret-pattern scan: OK")
