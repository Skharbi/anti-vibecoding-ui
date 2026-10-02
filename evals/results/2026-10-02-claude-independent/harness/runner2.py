"""Execute prepared attempts with headless Claude Code; outputs stored outside task dirs."""
import concurrent.futures as cf, importlib.util, json, os, subprocess, sys, time
from pathlib import Path

S = Path(__file__).parent
RUN = S / os.environ.get("RUNDIR", "run")
OUT = S / os.environ.get("OUTDIR", "outputs")
OUT.mkdir(exist_ok=True)
spec = importlib.util.spec_from_file_location("f", "<repo>/evals/results/2026-09-24-claude-independent/harness/fixtures.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
TOOLS = {k: v["tools"] for k, v in m.CASES.items()}
RO = "Skill Read Glob Grep"
STRIP = ["CLAUDE_ADDITIONAL_DIRECTORIES", "CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD", "CLAUDE_CODE_SESSION_ID",
         "CLAUDE_CODE_REMOTE_SESSION_ID", "CLAUDE_CODE_MESSAGING_SOCKET", "CLAUDE_CODE_MESSAGING_TOKEN",
         "CLAUDECODE", "CLAUDE_CODE_CHILD_SESSION"]
env = {k: v for k, v in os.environ.items() if k not in STRIP}
ledger = json.loads((RUN / "run.json").read_text())
only = set(sys.argv[1:])


def run(a):
    aid = a["attempt_id"]
    if only and aid not in only:
        return aid, "skipped"
    out = OUT / (aid + ".jsonl")
    if out.exists() and out.stat().st_size > 0 and not only:
        return aid, "exists"
    tools = a.get("tools") or TOOLS.get(a["source_case"], RO).split()
    prompt = (RUN / a["prompt"]).read_text()
    cmd = ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose",
           "--setting-sources", "project", "--tools", *tools, "--allowedTools", *tools,
           "--permission-mode", "acceptEdits", "--max-turns", "60"]
    t = time.time()
    with open(out, "w") as fh:
        p = subprocess.run(cmd, cwd=RUN / a["task"], stdout=fh, stderr=subprocess.PIPE, text=True,
                           env=env, timeout=1800, stdin=subprocess.DEVNULL)
    (OUT / (aid + ".meta.json")).write_text(json.dumps({"rc": p.returncode, "stderr": p.stderr[-2000:],
                                                        "seconds": round(time.time() - t), "tools": tools}))
    return aid, p.returncode


with cf.ThreadPoolExecutor(8) as ex:
    for aid, rc in ex.map(run, ledger["attempts"]):
        print(aid, rc, flush=True)
