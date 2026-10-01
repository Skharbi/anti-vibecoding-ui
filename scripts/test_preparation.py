"""Test preparation and bundle layouts without invoking a coding client."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PreparationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="anti-ui-preparation-")
        self.addCleanup(self.tmp.cleanup)
        self.output = Path(self.tmp.name) / "run"

    def run_prepare(self, client="claude", mode="full", *extra):
        return subprocess.run([sys.executable, str(ROOT / "scripts/prepare_evals.py"),
                               "--client", client, "--mode", mode, "--output", str(self.output),
                               *extra], capture_output=True, text=True, timeout=30)

    def test_full_manifest_and_attempt_ledger(self):
        r = self.run_prepare()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        ledger = json.loads((self.output / "run.json").read_text())
        manifest = json.loads((ROOT / "evals/case-manifest.json").read_text())
        self.assertEqual(set(a["case_id"] for a in ledger["attempts"]), set(manifest["case_ids"]))
        self.assertEqual(len(ledger["attempts"]), 56)
        self.assertTrue(all(a["status"] == "Not run" and a["raw_output"] is None for a in ledger["attempts"]))
        for a in ledger["attempts"]:
            task = self.output / a["task"]
            self.assertFalse((task / "run.json").exists())
            self.assertFalse((task / "AGENTS.md").exists())
            self.assertFalse((task / "evals").exists())
            if a["delivery"] == "full":
                bundle = task / ".claude/skills/anti-vibecoding-ui"
                self.assertEqual((bundle / "SKILL.md").read_bytes(), (ROOT / "skills/anti-vibecoding-ui/SKILL.md").read_bytes())
                self.assertTrue((bundle / "references/review-protocol.md").is_file())
            else:
                self.assertIn("You are applying", (self.output / a["prompt"]).read_text())

    def test_codex_layout_and_explicit_skill_root(self):
        r = self.run_prepare("codex", "full", "--skill-root", str(ROOT / "skills/anti-vibecoding-ui"), "--cases", "B1")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue((self.output / "tasks/B1-B1-1/.agents/skills/anti-vibecoding-ui/SKILL.md").is_file())

    def test_paste_mode_has_no_installed_skill(self):
        r = self.run_prepare("codex", "paste", "--cases", "V1", "V2", "V3", "V4")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        ledger = json.loads((self.output / "run.json").read_text())
        self.assertEqual(len(ledger["attempts"]), 6)
        for a in ledger["attempts"]:
            self.assertFalse((self.output / a["task"] / ".agents").exists())
            self.assertFalse((self.output / a["task"] / ".claude").exists())
            self.assertIn("Not verified", (self.output / a["prompt"]).read_text())

    def test_existing_output_refused(self):
        self.output.mkdir()
        marker = self.output / "preserve.txt"
        marker.write_text("existing evidence")
        r = self.run_prepare()
        self.assertEqual(r.returncode, 1)
        self.assertEqual(marker.read_text(), "existing evidence")

    def test_unknown_case_refused_before_writes(self):
        r = self.run_prepare("claude", "full", "--cases", "UNKNOWN")
        self.assertEqual(r.returncode, 1)
        self.assertFalse(self.output.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
