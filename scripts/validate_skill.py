#!/usr/bin/env python3
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "anti-vibecoding-ui"
errors = []

def read(p):
    if not p.exists():
        errors.append("missing: " + str(p.relative_to(ROOT)))
        return ""
    return p.read_text(encoding="utf-8")

required = [
    ROOT/"README.md", ROOT/"LICENSE", ROOT/"HANDOVER.md", ROOT/"PASTE-TO-INSTALL.md",
    SKILL/"SKILL.md", SKILL/"agents"/"openai.yaml",
    SKILL/"references"/"checklist.md", SKILL/"references"/"review-protocol.md",
    SKILL/"references"/"component-behavior.md", SKILL/"references"/"security.md",
    SKILL/"references"/"best-practices-matrix.md", SKILL/"references"/"sources.md",
    ROOT/"evals"/"README.md", ROOT/"evals"/"cases.md"
]
for p in required:
    read(p)

skill = read(SKILL/"SKILL.md")
checklist = read(SKILL/"references"/"checklist.md")
cases = read(ROOT/"evals"/"cases.md")
readme = read(ROOT/"README.md")
paste = read(ROOT/"PASTE-TO-INSTALL.md")

if not skill.startswith("---\n"):
    errors.append("SKILL.md missing frontmatter")
m = re.search(r"^name:\s*([^\n]+)$", skill, re.M)
if not m or m.group(1).strip() != "anti-vibecoding-ui":
    errors.append("invalid skill name")
m = re.search(r"^description:\s*(.+)$", skill, re.M)
if not m or len(m.group(1).strip()) < 120:
    errors.append("skill description too weak")

if "evals/" in skill:
    errors.append("installable SKILL.md must not reference repo-root evals")

for ref in re.findall(r"references/([A-Za-z0-9_-]+\.md)", skill):
    if not (SKILL/"references"/ref).exists():
        errors.append("missing package reference: " + ref)

nums = [int(x) for x in re.findall(r"^##\s+(\d+)\.\s+", checklist, re.M)]
if nums != list(range(1, 39)):
    errors.append("checklist numbering is not consecutive 1..38")

ids = re.findall(r"^###\s+([A-Z]+\d+)\s+—", cases, re.M)
if len(ids) != 42:
    errors.append("expected 42 eval cases, found " + str(len(ids)))
if len(ids) != len(set(ids)):
    errors.append("duplicate eval case IDs")

if "38 review areas" not in readme or "42 regression scenarios" not in readme:
    errors.append("README counts are stale")

if "condensed portable edition" not in paste.lower() or "canonical/full version" not in paste.lower():
    errors.append("portable edition disclosure missing")

security = read(SKILL/"references"/"security.md")
matrix = read(SKILL/"references"/"best-practices-matrix.md")
if "OWASP compliant" not in security or "ASVS compliant" not in security:
    errors.append("security anti-overclaim guard missing")
if "requires external verification" not in (skill + matrix):
    errors.append("external-verification boundary missing")
if "native semantic HTML before ARIA" not in skill:
    errors.append("native-semantics rule missing")

secret_patterns = [
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    r"\bsk-proj-[A-Za-z0-9_-]{20,}\b",
    r"\bghp_[A-Za-z0-9]{20,}\b"
]
for p in ROOT.rglob("*"):
    if not p.is_file() or ".git" in p.parts:
        continue
    if p.suffix.lower() not in {".md",".yaml",".yml",".py",".txt"}:
        continue
    body = p.read_text(encoding="utf-8", errors="ignore")
    for pat in secret_patterns:
        if re.search(pat, body):
            errors.append("possible secret in " + str(p.relative_to(ROOT)))

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print("- " + e)
    sys.exit(1)

print("VALIDATION PASSED")
print("required files:", len(required))
print("checklist sections:", len(nums))
print("evaluation cases:", len(ids))
