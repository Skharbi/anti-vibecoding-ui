#!/usr/bin/env python3
import json
import re
import sys
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    print("VALIDATION FAILED\n- QA dependency missing: run python -m pip install -r requirements-dev.txt")
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "anti-vibecoding-ui"
errors = []


class UniqueSafeLoader(yaml.SafeLoader):
    """Reject duplicate keys rather than silently overwriting them."""


def unique_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in mapping:
            raise yaml.constructor.ConstructorError(None, None, "duplicate/non-string key", key_node.start_mark)
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def yaml_mapping(body, label):
    try:
        value = yaml.load(body, Loader=UniqueSafeLoader)
        if not isinstance(value, dict):
            errors.append(label + " must be a YAML mapping")
            return {}
        return value
    except yaml.YAMLError:
        # Do not print parser excerpts: malformed YAML may contain credentials.
        errors.append(label + " invalid YAML (including duplicate keys)")
        return {}


def read(path: Path) -> str:
    if path.is_relative_to(SKILL):
        try:
            if not path.resolve().is_relative_to(SKILL.resolve()):
                errors.append("installed path escapes skill bundle: " + str(path.relative_to(ROOT)))
                return ""
        except (OSError, RuntimeError):
            errors.append("unresolvable installed path: " + str(path.relative_to(ROOT)))
            return ""
    if not path.is_file():
        errors.append("missing: " + str(path.relative_to(ROOT)))
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        errors.append("unreadable UTF-8 file: " + str(path.relative_to(ROOT)))
        return ""


def json_mapping(path):
    """Validate the container before consumers access required properties."""
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate key")
            result[key] = value
        return result

    label = str(path.relative_to(ROOT))
    try:
        value = json.loads(read(path), object_pairs_hook=unique_object)
    except (ValueError, TypeError):
        errors.append(label + " invalid JSON (including duplicate keys)")
        return {}
    if not isinstance(value, dict) or not value:
        errors.append(label + " must be a non-empty JSON object")
        return {}
    return value


required = [
    ROOT / "requirements-dev.txt",
    ROOT / "scripts" / "test_validator.py",
    ROOT / "scripts" / "prepare_evals.py",
    ROOT / "scripts" / "test_preparation.py",
    ROOT / "evals" / "case-manifest.json",
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "HANDOVER.md",
    ROOT / "PASTE-TO-INSTALL.md",
    ROOT / "INSTALL.md",
    ROOT / "SECURITY.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CHANGELOG.md",
    ROOT / "RELEASE.md",
    ROOT / "AGENTS.md",
    ROOT / "SUPPORT.md",
    ROOT / "CODE_OF_CONDUCT.md",
    ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "bug_report.md",
    ROOT / ".github" / "ISSUE_TEMPLATE" / "skill_gap.md",
    ROOT / "plugin.json",
    ROOT / ".codex-plugin" / "plugin.json",
    SKILL / "SKILL.md",
    SKILL / "agents" / "openai.yaml",
    SKILL / "references" / "checklist.md",
    SKILL / "references" / "review-protocol.md",
    SKILL / "references" / "component-behavior.md",
    SKILL / "references" / "security.md",
    SKILL / "references" / "best-practices-matrix.md",
    SKILL / "references" / "sources.md",
    ROOT / "evals" / "README.md",
    ROOT / "evals" / "cases.md",
    ROOT / "evals" / "EXECUTION-GATE.md",
    ROOT / "evals" / "SECOND-AGENT-RUN.md",
    ROOT / "evals" / "runtime-fixtures" / "README.md",
    ROOT / "evals" / "runtime-fixtures" / "r3-responsive.html",
    ROOT / "evals" / "runtime-fixtures" / "r9-rtl.html",
    ROOT / "evals" / "runtime-fixtures" / "g1-dashboard.html",
    ROOT / "evals" / "runtime-fixtures" / "g2-portfolio.html",
    ROOT / "evals" / "runtime-fixtures" / "g3-mobile-form.html",
    ROOT / "evals" / "runtime-fixtures" / "p1-browser-feature.html",
]

for path in required:
    read(path)

skill = read(SKILL / "SKILL.md")
checklist = read(SKILL / "references" / "checklist.md")
cases = read(ROOT / "evals" / "cases.md")
readme = read(ROOT / "README.md")
paste = read(ROOT / "PASTE-TO-INSTALL.md")
protocol = read(SKILL / "references" / "review-protocol.md")
handover = read(ROOT / "HANDOVER.md")
changelog = read(ROOT / "CHANGELOG.md")
openai_yaml = read(SKILL / "agents" / "openai.yaml")


# SKILL.md frontmatter.
if not skill.startswith("---\n"):
    errors.append("SKILL.md missing frontmatter")

fm = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if not fm:
    errors.append("SKILL.md frontmatter is unclosed or malformed")
    frontmatter = ""
else:
    frontmatter = fm.group(1)

metadata = yaml_mapping(frontmatter, "SKILL.md frontmatter") if fm else {}
skill_name = metadata.get("name", "")
skill_desc = metadata.get("description", "")
if not isinstance(skill_name, str):
    errors.append("skill name must be a string")
    skill_name = ""
if not isinstance(skill_desc, str) or not skill_desc.strip():
    errors.append("skill description must be a non-empty string")
    skill_desc = ""
if set(metadata) - {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}:
    errors.append("unsupported skill frontmatter field")
for key in ["license", "allowed-tools", "compatibility"]:
    if key in metadata and (not isinstance(metadata[key], str) or not metadata[key].strip()):
        errors.append("skill " + key + " must be a non-empty string")
compatibility = metadata.get("compatibility")
if isinstance(compatibility, str) and len(compatibility) > 500:
    errors.append("skill compatibility exceeds 500 chars")
extra_metadata = metadata.get("metadata")
if "metadata" in metadata and (not isinstance(extra_metadata, dict) or
        not all(isinstance(k, str) and isinstance(v, str) for k, v in extra_metadata.items())):
    errors.append("skill metadata must map strings to strings")
if skill_name != SKILL.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_name):
    errors.append("skill name must match folder and naming specification")
if len(skill_name) > 64:
    errors.append("skill name exceeds 64 chars")

if skill_name != "anti-vibecoding-ui":
    errors.append("invalid skill name")
if not skill_desc:
    errors.append("skill description missing")
elif len(skill_desc) > 1024:
    errors.append(f"skill description exceeds 1024 chars: {len(skill_desc)}")
if fm and not skill[fm.end():].strip():
    errors.append("skill body is empty")


# Portable Agent Plugins manifest.
plugin = json_mapping(ROOT / "plugin.json")

if plugin:
    expected_schema = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    if plugin.get("$schema") != expected_schema:
        errors.append("plugin.json schema is missing or unexpected")

    allowed_keys = {
        "$schema", "name", "version", "description", "author",
        "homepage", "repository", "license", "keywords", "extensions"
    }
    extra_keys = sorted(set(plugin) - allowed_keys)
    if extra_keys:
        errors.append("plugin.json has unsupported properties: " + ", ".join(extra_keys))

    plugin_name = plugin.get("name")
    version = plugin.get("version")
    description = plugin.get("description")

    name_pattern = r"(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?"
    if (
        not isinstance(plugin_name, str)
        or not re.fullmatch(name_pattern, plugin_name)
        or len(plugin_name) > 64
    ):
        errors.append("plugin name violates Agent Plugins schema constraints")
    if plugin_name != "anti-vibecoding-ui":
        errors.append("plugin name must be anti-vibecoding-ui")

    semver = r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?"
    if not isinstance(version, str) or not re.fullmatch(semver, version or ""):
        errors.append("plugin version must be semantic version")
    if not isinstance(description, str) or not description.strip():
        errors.append("plugin description missing")

    if isinstance(plugin_name, str) and len(plugin_name + ":" + skill_name) > 64:
        errors.append("combined plugin:skill identity exceeds 64 chars")

    if isinstance(version, str) and version and f"## [{version}]" not in changelog:
        errors.append("CHANGELOG does not contain plugin version " + version)
    if isinstance(version, str) and version and f"Current package version:** `{version}`" not in readme:
        errors.append("README package version does not match plugin.json")


# Codex compatibility manifest.
codex_plugin = json_mapping(ROOT / ".codex-plugin" / "plugin.json")

for key in ["name", "version", "description", "skills"]:
    if not isinstance(codex_plugin.get(key), str) or not codex_plugin[key].strip():
        errors.append("Codex compatibility manifest missing/non-string " + key)

if plugin and codex_plugin:
    if codex_plugin.get("name") != plugin.get("name"):
        errors.append("Codex compatibility plugin name does not match root plugin.json")
    if codex_plugin.get("version") != plugin.get("version"):
        errors.append("Codex compatibility plugin version does not match root plugin.json")
    if codex_plugin.get("skills") != "./skills/":
        errors.append("Codex compatibility manifest must point skills to ./skills/")


# Installable skill must stay self-contained.
for path in SKILL.rglob("*"):
    if path.is_symlink():
        try:
            resolved = path.resolve(strict=True)
            if not resolved.is_relative_to(SKILL.resolve()):
                errors.append("installed symlink escapes skill bundle: " + str(path.relative_to(ROOT)))
        except (OSError, RuntimeError):
            errors.append("unresolvable installed symlink: " + str(path.relative_to(ROOT)))

if "evals/" in skill:
    errors.append("installable SKILL.md must not reference repo-root evals")

for ref in re.findall(r"references/([A-Za-z0-9_-]+\.md)", skill):
    if not (SKILL / "references" / ref).exists():
        errors.append("missing package reference: " + ref)


# OpenAI skill metadata.
agent = yaml_mapping(openai_yaml, "agents/openai.yaml")
interface = agent.get("interface", {})
policy = agent.get("policy", {})
if not isinstance(interface, dict):
    errors.append("agent interface must be a mapping")
    interface = {}
if not isinstance(policy, dict):
    errors.append("agent policy must be a mapping")
    policy = {}
for key in ["display_name", "short_description", "default_prompt"]:
    if not isinstance(interface.get(key), str) or not interface[key].strip():
        errors.append("agent interface missing/non-string " + key)
short = interface.get("short_description", "")
if isinstance(short, str) and not 25 <= len(short) <= 64:
    errors.append("agent short_description must be 25..64 chars")
default_prompt = interface.get("default_prompt")
if isinstance(default_prompt, str) and "$anti-vibecoding-ui" not in default_prompt:
    errors.append("agent default_prompt must mention $anti-vibecoding-ui")
if policy.get("allow_implicit_invocation") is not True:
    errors.append("agent allow_implicit_invocation must be true (boolean)")
products = policy.get("products")
if products is not None and (not isinstance(products, list) or
                             not all(isinstance(item, str) for item in products) or
                             set(products) != {"CHAT", "CODEX"}):
    errors.append("agent products, when present, must be CHAT and CODEX")


# Checklist and eval contracts.
nums = [int(x) for x in re.findall(r"^##\s+(\d+)\.\s+", checklist, re.M)]
if nums != list(range(1, 39)):
    errors.append("checklist numbering is not consecutive 1..38")

ids = re.findall(r"^###\s+([A-Z]+\d+)\s+—", cases, re.M)
manifest = json_mapping(ROOT / "evals" / "case-manifest.json")
if manifest.get("case_ids") != ids or manifest.get("schema_version") != 1:
    errors.append("case manifest does not match versioned case list")
if len(ids) != len(set(ids)):
    errors.append("duplicate eval case IDs")


# Documentation consistency.
if "38 review areas" not in readme or f"{len(ids)} regression scenarios" not in readme:
    errors.append("README counts are stale")
if "\\n" in readme:
    errors.append("README contains escaped newline text")
if "28 checklist sections" in protocol or "34 checklist sections" in protocol:
    errors.append("review protocol contains stale checklist count")
if "Adding a JS/Python test harness" in handover:
    errors.append("handover contradicts current validator architecture")
if "condensed portable edition" not in paste.lower() or "skills/anti-vibecoding-ui/" not in paste:
    errors.append("portable edition disclosure missing")
# prepare_evals.py extracts the paste prompt with this exact block shape.
if not re.search(r"```\n(You are applying.*?\n)```", paste, re.S):
    errors.append("portable instruction block not extractable")

# Protect the portable output contract from accidental deletion. These are
# structural presence checks, not proof that an agent obeys the instructions.
output_block = paste.split("REVIEW OUTPUT", 1)[-1].split("For each real finding:", 1)[0]
portable_guards = {
    "evidence labels": r"Confirmed.*Likely.*Needs verification.*Not applicable",
    "confirmed-only severity": r"Only confirmed defects justify.*Must-fix.*Fail",
    "incomplete verification verdict": r"Use Pass.*required checks.*Not verified.*Blocked",
    "legal applicability": r"Never assert a legal violation.*jurisdiction.*external verification",
    "server effects": r"request headers.*server effects.*contract or executed response",
    "current sources": r"current security/standards claims.*authoritative sources",
    "domain accounting": r"one coverage row per domain:.*Secure SDLC.*Observability.*Regulated workflows.*external verification",
}
for label, pattern in portable_guards.items():
    if not re.search(pattern, output_block, re.I | re.S):
        errors.append("portable safety contract missing: " + label)
install = read(ROOT / "INSTALL.md")
contributor_block = install.split("## For contributors only", 1)[-1].split("---", 1)[0]
if "python -m pip install -r requirements-dev.txt" not in contributor_block:
    errors.append("INSTALL contributor QA dependency setup missing")

priority_block = (
    paste.split("PRIORITY ORDER", 1)[1].split("MANDATORY AREAS TO CONSIDER", 1)[0]
    if "PRIORITY ORDER" in paste and "MANDATORY AREAS TO CONSIDER" in paste
    else ""
)
priority_nums = [int(x) for x in re.findall(r"^(\d+)\.\s+", priority_block, re.M)]
if priority_nums != list(range(1, 11)):
    errors.append("portable priority list numbering is invalid")


# Guardrails that must not regress.
security = read(SKILL / "references" / "security.md")
matrix = read(SKILL / "references" / "best-practices-matrix.md")
expected_domains = [
    "Product/UX", "Accessibility", "Cybersecurity", "Secure SDLC", "Privacy",
    "Performance", "Responsive", "Internationalization", "Design systems",
    "Reliability", "Testing", "Observability", "Content/credibility", "AI interfaces",
    "Regulated workflows", "Browser/platform compatibility", "Public discoverability",
    "API client boundary", "Rendering/cache/concurrency",
]
domain_match = re.search(r"one coverage row per domain:\s*([^\n]+?)\.\s*Mark each", output_block, re.I)
portable_domains = [s.strip().casefold() for s in domain_match.group(1).split(";")] if domain_match else []
matrix_domains = [s.strip().casefold() for s in re.findall(r"^\| ([^|]+) \|", matrix, re.M)
                  if s.strip() != "Domain"]
expected = sorted(s.casefold() for s in expected_domains)
if sorted(portable_domains) != expected:
    errors.append("portable coverage must contain each of the 19 domains exactly once")
if sorted(matrix_domains) != expected:
    errors.append("coverage matrix must contain each of the 19 domains exactly once")
if "OWASP compliant" not in security or "ASVS compliant" not in security:
    errors.append("security anti-overclaim guard missing")
if "requires external verification" not in (skill + matrix):
    errors.append("external-verification boundary missing")
if "semantic HTML before ARIA" not in skill and "native HTML semantics before ARIA" not in skill:
    errors.append("native-semantics rule missing")


# Relative Markdown links in repository docs.
docs_to_check = [
    ROOT / "README.md",
    ROOT / "INSTALL.md",
    ROOT / "SECURITY.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "CHANGELOG.md",
    ROOT / "RELEASE.md",
    ROOT / "AGENTS.md",
    ROOT / "SUPPORT.md",
    ROOT / "CODE_OF_CONDUCT.md",
    ROOT / "HANDOVER.md",
    ROOT / "PASTE-TO-INSTALL.md",
    ROOT / "evals" / "README.md",
    ROOT / "evals" / "SECOND-AGENT-RUN.md",
    ROOT / "evals" / "runtime-fixtures" / "README.md",
]

docs_to_check += list(SKILL.rglob("*.md"))


def heading_ids(body):
    slugs = set()
    counts = {}
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    for heading in re.findall(r"^#{1,6}\s+(.+)$", body, re.M):
        slug = re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        slugs.add(slug + (f"-{count}" if count else ""))
    slugs.update(re.findall(r'(?:id|name)=[\"\']([^\"\']+)', body))
    return slugs


for md in docs_to_check:
    body = read(md)
    # Code samples are not live Markdown dependencies.
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", body):
        target = target.strip().split(' "', 1)[0].strip("<>")
        try:
            parts = urlsplit(target)
        except ValueError:
            errors.append("malformed markdown URL in " + str(md.relative_to(ROOT)))
            continue
        if parts.scheme or parts.netloc:
            continue
        clean = unquote(parts.path)
        try:
            resolved = (md.parent / clean).resolve() if clean else md.resolve()
        except (OSError, RuntimeError, ValueError):
            errors.append("unresolvable markdown link in " + str(md.relative_to(ROOT)))
            continue
        if md.is_relative_to(SKILL) and not resolved.is_relative_to(SKILL.resolve()):
            errors.append("reference escapes installed skill: " + str(md.relative_to(ROOT)))
            continue
        if not resolved.is_file():
            errors.append(f"broken relative markdown link in {md.relative_to(ROOT)}: {target}")
        elif parts.fragment and resolved.suffix == ".md" and unquote(parts.fragment) not in heading_ids(read(resolved)):
            errors.append(f"broken markdown anchor in {md.relative_to(ROOT)}: {target}")


# Common accidental-secret patterns.
secret_patterns = [
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    r"\bsk-proj-[A-Za-z0-9_-]{20,}\b",
    r"\bghp_[A-Za-z0-9]{20,}\b",
    r"\bgithub_pat_[A-Za-z0-9_]{30,}\b",
    r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b",
]

# Scan versioned + candidate source, not extension-limited files. In test copies
# without .git, scan the copy itself. This does not scan historical commits.
tracked = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--show-toplevel"], capture_output=True, text=True)
if tracked.returncode == 0 and Path(tracked.stdout.strip()).resolve() == ROOT.resolve():
    listed = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-co", "--exclude-standard", "-z"], capture_output=True, check=True)
    candidates = [ROOT / p.decode("utf-8") for p in listed.stdout.split(b"\0") if p]
else:
    candidates = list(ROOT.rglob("*"))
for path in set(candidates):
    if not path.is_file() or path.is_symlink() or any(p in {".git", ".venv", "__pycache__", "node_modules"} for p in path.parts):
        continue
    raw = path.read_bytes()
    if b"\0" in raw:
        continue
    try:
        body = raw.decode("utf-8")
    except UnicodeDecodeError:
        continue
    for pattern in secret_patterns:
        if re.search(pattern, body):
            errors.append("possible secret in " + str(path.relative_to(ROOT)))


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
print("portable + Codex manifests: OK")
print("package-local references: OK")
print("agent metadata: OK")
print("documentation consistency: OK")
print("relative links: OK")
print("secret-pattern scan: OK")
