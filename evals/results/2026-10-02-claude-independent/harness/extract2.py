"""Summarize raw stream-json outputs into per-attempt transcripts for scoring."""
import json, sys
from pathlib import Path

S = Path(__file__).parent
OUT, TR = S / "outputs2", S / "transcripts2"
TR.mkdir(exist_ok=True)
summary = {}
for f in sorted(OUT.glob("*.jsonl")):
    aid = f.stem
    loaded, refs, tools, leaks, result, model, final = False, [], [], [], None, None, {}
    task_root = str(S / "run2" / "tasks" / aid)
    for line in f.read_text().splitlines():
        try:
            d = json.loads(line)
        except ValueError:
            continue
        if d.get("type") == "system" and d.get("subtype") == "init":
            model = d.get("model")
        if d.get("type") == "assistant":
            for c in d["message"].get("content", []):
                if c.get("type") != "tool_use":
                    continue
                inp = c.get("input", {})
                s = json.dumps(inp)
                if c["name"] == "Skill" and "anti-vibecoding-ui" in s:
                    loaded = True
                p = inp.get("file_path") or inp.get("path") or ""
                if c["name"] == "Read" and "/references/" in p:
                    refs.append(p.rsplit("/", 1)[-1])
                if "anti-vibecoding-ui/evals" in s or "/home/user/anti-vibecoding-ui" in s or (p and p.startswith("/") and not p.startswith(task_root)):
                    leaks.append(c["name"] + " " + s[:200])
                tools.append(c["name"] + ("(" + p.replace(task_root + "/", "") + ")" if p else ""))
        if d.get("type") == "result":
            result = d.get("result")
            final = {k: d.get(k) for k in ["subtype", "num_turns", "total_cost_usd", "is_error"]}
    summary[aid] = {"skill_loaded": loaded, "refs": refs, "leaks": leaks, "model": model, **final}
    (TR / (aid + ".md")).write_text(
        f"# {aid}\nmodel: {model}\nskill_loaded: {loaded}\nrefs: {refs}\nleaks: {leaks}\nresult_meta: {final}\n"
        f"tools: {tools}\n\n## Final output\n\n{result}\n")
(S / "summary2.json").write_text(json.dumps(summary, indent=1))
for k, v in summary.items():
    print(k, "LOADED" if v["skill_loaded"] else "not-loaded", v["refs"], "LEAK" if v["leaks"] else "", v.get("subtype"), v.get("total_cost_usd"))
