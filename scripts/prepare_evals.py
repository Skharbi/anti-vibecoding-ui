"""Prepare isolated blind tasks and a ledger; never invoke a paid model."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "anti-vibecoding-ui"


def definitions():
    # Historical input fixtures are reusable inputs, never prior outputs/scores.
    path = ROOT / "evals/results/2026-09-24-claude-independent/harness/fixtures.py"
    spec = importlib.util.spec_from_file_location("blind_fixture_inputs", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    cases = dict(module.CASES)
    cases.update({
        "V1": {"prompt": "Audit this interface for production readiness. Browser, server, product requirements and jurisdiction evidence are unavailable.", "files": {"index.html": '<!doctype html><html lang="en"><meta name="viewport" content="width=device-width"><title>Items</title><main><h1>Items</h1><p>No items.</p></main></html>'}},
        "V2": {"prompt": "Review privacy risks of this analytics UI. Jurisdiction, processing purpose, identifiers and any separate consent mechanism are unknown.", "files": {"index.html": '<main><h1>Overview</h1><p>Dashboard</p></main><script src="https://analytics.example/sdk.js"></script>'}},
        "V3": {"prompt": "Review this API client. Server contract and responses are unavailable.", "files": {"client.js": "export function send(data) { return fetch('/api/items', {method:'POST',headers:{'Content-Type':'text/plain'},body:JSON.stringify(data)}); }"}},
    })
    # V4 is three fresh paste-only tasks, not a fixture containing answers.
    cases["V4"] = {"subcases": ["V1", "V2", "V3"]}
    return cases


PARAPHRASES = {
    "T1": ["Something feels off about this dashboard spacing and hierarchy. Fix it.", "Improve this dashboard's layout and visual hierarchy.", "This dashboard feels crowded. Fix its spacing."],
    "T2": ["Optimize this Postgres query.", "Speed up this database query without changing its results.", "Analyze this SQL query's execution performance."],
    "T3": ["My modal works with the mouse but keyboard users get stuck.", "Review why keyboard navigation gets trapped in this dialog.", "Fix this modal's focus behavior for keyboard users."],
    "B5": ["Review these frontend error logs for useful diagnostics and privacy risks.", "Check whether client-side logging exposes tokens or user-entered data.", "Improve our frontend observability while protecting sensitive data."],
}


def prepare(output, skill_root, client, mode, selected):
    cases = definitions()
    manifest = json.loads((ROOT / "evals/case-manifest.json").read_text())
    if set(cases) != set(manifest["case_ids"]):
        raise ValueError("Fixture definitions and case manifest differ")
    unknown = set(selected) - set(cases)
    if unknown:
        raise ValueError("Unknown case IDs: " + ", ".join(sorted(unknown)))
    if not (skill_root / "SKILL.md").is_file():
        raise ValueError("Skill root must contain SKILL.md")
    if output.is_relative_to(ROOT):
        raise ValueError("Output must be outside the source repository to avoid inherited context")
    # A directory is never overwritten or deleted by this harness.
    output.mkdir(parents=True, exist_ok=False)
    source_commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip() or "unavailable"
    dirty = bool(subprocess.run(["git", "-C", str(ROOT), "status", "--porcelain"], capture_output=True, text=True).stdout.strip())
    hashes = {str(p.relative_to(skill_root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in skill_root.rglob("*") if p.is_file()}
    portable = re.search(r"```\n(You are applying.*?\n)```", (ROOT / "PASTE-TO-INSTALL.md").read_text(), re.S).group(1)
    attempts = []
    for cid in selected:
        runs = cases[cid].get("subcases", [cid])
        for source_id in runs:
            fixture = cases[source_id]
            prompts = PARAPHRASES.get(cid, [fixture["prompt"]])
            for number, prompt in enumerate(prompts, 1):
                aid = f"{cid}-{source_id}-{number}"
                task = output / "tasks" / aid
                task.mkdir(parents=True)
                for relative, content in fixture["files"].items():
                    target = task / relative
                    if not target.resolve().is_relative_to(task.resolve()):
                        raise ValueError("Fixture path escapes task")
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(content, encoding="utf-8")
                delivery = "paste" if cid == "V4" else mode
                if delivery == "full":
                    location = ".claude" if client == "claude" else ".agents"
                    shutil.copytree(skill_root, task / location / "skills" / SKILL_NAME)
                prompt_file = output / "prompts" / (aid + ".txt")
                prompt_file.parent.mkdir(exist_ok=True)
                prompt_file.write_text((portable + "\n\n" if delivery == "paste" else "") + prompt, encoding="utf-8")
                attempts.append({"attempt_id": aid, "case_id": cid, "source_case": source_id,
                                 "delivery": delivery, "task": str(task.relative_to(output)),
                                 "prompt": str(prompt_file.relative_to(output)), "status": "Not run",
                                 "skill_loaded": None, "mandatory_assertions_pass": None,
                                 "model": None, "raw_output": None, "limitations": []})
    record = {"schema_version": 1, "source_commit": source_commit, "dirty_source": dirty,
              "skill_sha256": hashes, "client": client, "attempts": attempts,
              "portable_sha256": hashlib.sha256(portable.encode()).hexdigest(),
              "fixture_sha256": hashlib.sha256((ROOT / "evals/results/2026-09-24-claude-independent/harness/fixtures.py").read_bytes()).hexdigest(),
              "case_manifest_sha256": hashlib.sha256((ROOT / "evals/case-manifest.json").read_bytes()).hexdigest(),
              "note": "Prepared only. No model invoked, no behavior scored. Retain every attempt."}
    (output / "run.json").write_text(json.dumps(record, indent=2) + "\n")
    return len(attempts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="New directory; existing paths are refused")
    parser.add_argument("--skill-root", type=Path, default=ROOT / "skills" / SKILL_NAME)
    parser.add_argument("--client", choices=["claude", "codex"], required=True)
    parser.add_argument("--mode", choices=["full", "paste"], default="full")
    parser.add_argument("--cases", nargs="+")
    args = parser.parse_args()
    selected = args.cases or json.loads((ROOT / "evals/case-manifest.json").read_text())["case_ids"]
    try:
        count = prepare(args.output.resolve(), args.skill_root.resolve(), args.client, args.mode, selected)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Preparation failed: {exc}\n")
    print(f"Prepared {count} predetermined attempts. No agent execution or scores claimed.")


if __name__ == "__main__":
    main()
