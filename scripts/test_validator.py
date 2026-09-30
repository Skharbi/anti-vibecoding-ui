"""Negative probes run against isolated copies; never mutate the checkout."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="anti-validator-")
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name) / "repo"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(
            ".git", "__pycache__", ".venv", "node_modules"))

    def edit(self, path, transform):
        target = self.repo / path
        target.write_text(transform(target.read_text()), encoding="utf-8")

    def run_gate(self):
        return subprocess.run([sys.executable, str(self.repo / "scripts/validate_skill.py")],
                              capture_output=True, text=True, timeout=30)

    def rejected(self, needle):
        result = self.run_gate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(needle, result.stdout)

    def test_valid_repository(self):
        r = self.run_gate()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_manifest_containers(self):
        for path in ["plugin.json", ".codex-plugin/plugin.json"]:
            target = self.repo / path
            original = target.read_text()
            for invalid in ["{}", "[]", "[1]", "null", '"text"', "42"]:
                with self.subTest(path=path, invalid=invalid):
                    target.write_text(invalid)
                    self.rejected("non-empty JSON object")
            target.write_text(original)

    def test_plugin_required_fields(self):
        target = self.repo / "plugin.json"
        original = target.read_text()
        for key in ["$schema", "name", "version", "description"]:
            with self.subTest(key=key):
                value = json.loads(original)
                value.pop(key)
                target.write_text(json.dumps(value))
                r = self.run_gate()
                self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
                self.assertNotIn("Traceback", r.stderr)
        target.write_text(original)

    def test_plugin_field_types(self):
        target = self.repo / "plugin.json"
        original = target.read_text()
        for key in ["name", "version", "description"]:
            with self.subTest(key=key):
                value = json.loads(original)
                value[key] = {"invalid": True}
                target.write_text(json.dumps(value))
                r = self.run_gate()
                self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
                self.assertNotIn("Traceback", r.stderr)
        target.write_text(original)

    def test_duplicate_manifest_key(self):
        self.edit("plugin.json", lambda s: s.replace('"name":', '"name": "duplicate", "name":', 1))
        self.rejected("invalid JSON")

    def test_optional_skill_types(self):
        target = self.repo / "skills/anti-vibecoding-ui/SKILL.md"
        original = target.read_text()
        for field in ["compatibility: {invalid: true}", "compatibility: " + "x" * 501,
                      "license: [MIT]", "allowed-tools: [Bash]", "metadata: text",
                      "metadata: {version: 1}"]:
            with self.subTest(field=field.split(":")[0]):
                target.write_text(original.replace("name: anti-vibecoding-ui",
                    "name: anti-vibecoding-ui\n" + field, 1))
                r = self.run_gate()
                self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
                self.assertNotIn("Traceback", r.stderr)
        target.write_text(original)

    def test_valid_optional_skill_metadata(self):
        self.edit("skills/anti-vibecoding-ui/SKILL.md", lambda s: s.replace(
            "name: anti-vibecoding-ui", 'name: anti-vibecoding-ui\nlicense: MIT\ncompatibility: Coding client\nallowed-tools: Read Bash\nmetadata: {version: "1"}', 1))
        r = self.run_gate()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_default_prompt_skill_mention(self):
        self.edit("skills/anti-vibecoding-ui/agents/openai.yaml", lambda s: s.replace(
            "$anti-vibecoding-ui", "this protocol"))
        self.rejected("default_prompt must mention")

    def test_portable_safety_deletions(self):
        target = self.repo / "PASTE-TO-INSTALL.md"
        original = target.read_text()
        for prefix in ["Label evidence", "Use Pass or Pass with issues", "Never assert a legal violation",
                       "Confirm request headers", "For a full audit"]:
            with self.subTest(prefix=prefix):
                target.write_text("\n".join(l for l in original.splitlines() if not l.startswith(prefix)))
                self.rejected("portable safety contract missing")
        target.write_text(original)

    def test_install_dependency_setup(self):
        self.edit("INSTALL.md", lambda s: s.replace("python -m pip install -r requirements-dev.txt", ""))
        self.rejected("INSTALL contributor QA dependency setup missing")

    def test_invalid_skill_yaml(self):
        self.edit("skills/anti-vibecoding-ui/SKILL.md", lambda s: s.replace(
            "description: Review,", "description: invalid: Review,", 1))
        self.rejected("invalid YAML")

    def test_duplicate_skill_key(self):
        self.edit("skills/anti-vibecoding-ui/SKILL.md", lambda s: s.replace(
            "name: anti-vibecoding-ui", "name: anti-vibecoding-ui\nname: anti-vibecoding-ui", 1))
        self.rejected("invalid YAML")

    def test_description_type(self):
        self.edit("skills/anti-vibecoding-ui/SKILL.md", lambda s: s.replace(
            next(l for l in s.splitlines() if l.startswith("description:")), "description: [one, two]", 1))
        self.rejected("description must be a non-empty string")

    def test_quoted_description(self):
        self.edit("skills/anti-vibecoding-ui/SKILL.md", lambda s: s.replace(
            next(l for l in s.splitlines() if l.startswith("description:")),
            'description: "Review: frontend UI safely."', 1))
        r = self.run_gate()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_invalid_agent_yaml(self):
        self.edit("skills/anti-vibecoding-ui/agents/openai.yaml", lambda s: s + "\ninterface: [unterminated\n")
        self.rejected("invalid YAML")

    def test_agent_boolean_type(self):
        self.edit("skills/anti-vibecoding-ui/agents/openai.yaml", lambda s: s.replace(
            "allow_implicit_invocation: true", 'allow_implicit_invocation: "true"'))
        self.rejected("allow_implicit_invocation must be true")

    def test_duplicate_agent_key(self):
        self.edit("skills/anti-vibecoding-ui/agents/openai.yaml", lambda s: s + "\ninterface: {}\n")
        self.rejected("invalid YAML")

    def test_agent_products_nested_type(self):
        self.edit("skills/anti-vibecoding-ui/agents/openai.yaml", lambda s: s.replace(
            "- CHAT", "- [CHAT]"))
        self.rejected("agent products")

    def test_missing_installed_reference(self):
        self.edit("skills/anti-vibecoding-ui/references/review-protocol.md",
                  lambda s: s + "\n[Missing](nonexistent.md)\n")
        self.rejected("broken relative markdown link")

    def test_reference_escape(self):
        self.edit("skills/anti-vibecoding-ui/references/review-protocol.md",
                  lambda s: s + "\n[Outside](../../../README.md)\n")
        self.rejected("reference escapes installed skill")

    def test_invalid_anchor(self):
        self.edit("skills/anti-vibecoding-ui/references/review-protocol.md",
                  lambda s: s + "\n[Missing](#nonexistent-heading)\n")
        self.rejected("broken markdown anchor")

    def test_valid_anchor(self):
        self.edit("skills/anti-vibecoding-ui/references/review-protocol.md",
                  lambda s: s + "\n[Evidence](#1-evidence-first)\n")
        r = self.run_gate()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_disclosure_required(self):
        self.edit("PASTE-TO-INSTALL.md", lambda s: s.replace("condensed portable edition", "edition"))
        self.rejected("portable edition disclosure missing")

    def test_duplicate_case(self):
        self.edit("evals/cases.md", lambda s: s + "\n### T1 — duplicate\nExpected: fail.\n")
        self.rejected("duplicate eval case IDs")

    def test_case_manifest_mismatch(self):
        self.edit("evals/case-manifest.json", lambda s: s.replace('"T1"', '"T999"', 1))
        self.rejected("case manifest does not match")

    def test_secret_file_coverage(self):
        # Generated test value, not a credential. Do not store it in the checkout.
        synthetic = "ghp_" + "Z" * 30
        for suffix in [".html", ".js", ".ts", ".tsx", ".css", ".md", ".yaml", ".json", ".env"]:
            with self.subTest(suffix=suffix):
                p = self.repo / ("probe" + suffix)
                p.write_text(synthetic)
                r = self.run_gate()
                self.assertEqual(r.returncode, 1, r.stdout)
                self.assertIn("possible secret", r.stdout)
                self.assertNotIn(synthetic, r.stdout + r.stderr)
                p.unlink()

    def test_binary_is_skipped(self):
        (self.repo / "probe.png").write_bytes(b"\x00ghp_" + b"Z" * 30)
        r = self.run_gate()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
