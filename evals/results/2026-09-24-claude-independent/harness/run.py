import json, os, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, os.path.dirname(__file__))
from fixtures import CASES

ROOT = os.path.dirname(os.path.abspath(__file__))
H = os.path.join(ROOT, "h")
SKILL = "/home/user/anti-vibecoding-ui/skills/anti-vibecoding-ui"
MODEL = os.environ.get("EVAL_MODEL", "claude-opus-5-5")

def build(cid):
    d = os.path.join(H, cid)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    for p, c in CASES[cid]["files"].items():
        fp = os.path.join(d, p)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, "w").write(c)
    shutil.copytree(SKILL, os.path.join(d, ".claude/skills/anti-vibecoding-ui"))
    subprocess.run(["git", "init", "-q"], cwd=d)
    return d

def run(cid):
    d = build(cid)
    c = CASES[cid]
    cmd = ["claude", "-p", c["prompt"], "--model", MODEL, "--output-format", "stream-json", "--verbose",
           "--allowedTools", *c["tools"].split(), "--max-turns", "60"]
    with open(os.path.join(ROOT, f"out/{cid}.jsonl"), "w") as f:
        subprocess.run(cmd, cwd=d, stdout=f, stderr=subprocess.STDOUT, timeout=1800)
    return summarize(cid)

def summarize(cid):
    skill_used, tools, final, model = False, [], "", None
    for line in open(os.path.join(ROOT, f"out/{cid}.jsonl")):
        try: ev = json.loads(line)
        except Exception: continue
        if ev.get("type") == "system" and ev.get("subtype") == "init": model = ev.get("model")
        if ev.get("type") == "assistant":
            for b in ev["message"].get("content", []):
                if b.get("type") == "tool_use":
                    tools.append(b["name"] + (":" + json.dumps(b["input"])[:120] if b["name"] in ("Skill", "Read", "Bash") else ""))
                    if b["name"] == "Skill" and "anti-vibecoding" in json.dumps(b["input"]): skill_used = True
        if ev.get("type") == "result": final = ev.get("result", "")
    open(os.path.join(ROOT, f"out/{cid}.md"), "w").write(
        f"# {cid}\nmodel: {model}\nskill_invoked: {skill_used}\nprompt: {CASES[cid]['prompt']}\n\n## tools\n" +
        "\n".join(tools) + "\n\n## final\n" + final)
    return cid, skill_used, len(final)

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "out"), exist_ok=True)
    ids = sys.argv[1:] or list(CASES)
    with ThreadPoolExecutor(int(os.environ.get("PAR", "6"))) as ex:
        for r in ex.map(run, ids):
            print(r, flush=True)
