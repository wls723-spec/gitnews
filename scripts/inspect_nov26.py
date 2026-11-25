# -*- coding: utf-8 -*-
import json
import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
with open(REPO_ROOT / "candidates_nov26.json", "r", encoding="utf-8") as f:
    cand = json.load(f)

with open(REPO_ROOT / "history_seen_projects.md", "r", encoding="utf-8") as f:
    hist_lines = f.read().splitlines()

seen_14d = {}
seen_older = {}
for line in hist_lines:
    if line.startswith("| **"):
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 5:
            d = parts[1].replace("**", "").strip()
            proj = parts[3].replace("**", "").strip().lower()
            if d >= "2026-11-12":
                seen_14d[proj] = d
            else:
                seen_older[proj] = d

print("=== TOP UNSEEN TRENDING CANDIDATES (CHECK 14D & OLDER HISTORY + GH API) ===")
trending_checked = []
for it in sorted(cand["trending"], key=lambda x: x["stars_today"], reverse=True):
    name = it["name"]
    nl = name.lower()
    if nl in seen_14d:
        continue
    old_tag = f" [OLD:{seen_older[nl]}]" if nl in seen_older else ""
    trending_checked.append((it, old_tag))
    if len(trending_checked) >= 25:
        break

for it, old_tag in trending_checked:
    repo = it["name"]
    res = subprocess.run(["gh", "api", f"repos/{repo}"], capture_output=True, text=True)
    if res.returncode == 0:
        d = json.loads(res.stdout)
        lic = (d.get("license") or {}).get("spdx_id") or "None"
        hp = d.get("homepage") or ""
        print(f"{repo}{old_tag} | +★{it['stars_today']}/d | total★={d.get('stargazers_count')} | lic={lic} | lang={d.get('language')} | hp={hp} | pushed={d.get('pushed_at')}")
        print(f"   desc: {d.get('description')}")
    else:
        print(f"{repo}{old_tag} | +★{it['stars_today']}/d | GH API ERR")

win = cand["window"]
b1_end, b2_end, b3_end = win["b1_range"][1], win["b2_range"][1], win["b3_range"][1]

bad_re = re.compile(
    r'(coregold|latest2026|studio-latest|latestversion|coop-[a-z]+ora|coop-[a-z]+lia|coop-[a-z]+ven|'
    r'velmora|calvion|norvella|vellorin|velvaora|callona|averona|calora|varrona|cerroora|avvona|orvella|'
    r'verona|serona|corvian|vireon|calralia|belvora|avrilia|rob-run|gta-?6|gtavi|gta-vi|'
    r'delta-force|bodycam-assistant|2b2t|red4ext|wabbajack|lossless-scaling|dlss-5-swapper|'
    r'capcut-pro-video-editor|premiere-pro-for-windows|minectaft-on-rust|'
    r'powertoys-focused-workspace|openclaw-personal-workspace|rustdesk-remote-workspace|'
    r'open-webui-private-ai-desk|codex-cli-repo-workbench|claude-code-agent-workspace|'
    r'opencode-project-workbench|cyber-engine-tweaks-runtime-workspace|marvel-rivals|'
    r'special-k-presentation-workbench|adlabs-toolz|windows-clipboard-manager-sync|'
    r'-elvona|-varriora|-mervaora|-norlora|-avrara|-orlorin|-talloora|-orveven|-elvaora|-callorin|-varvana|-cerrilia|-velrolia|-velrina)',
    re.IGNORECASE
)

b1, b2, b3 = [], [], []
for it in cand["gh_new"]:
    name = it["full_name"]
    nl = name.lower()
    desc = it["desc"] or ""
    if nl in seen_14d or not desc.strip():
        continue
    if bad_re.search(nl) or bad_re.search(desc):
        continue
    age = it["age_h"]
    if age < b1_end:
        b1.append(it)
    elif age < b2_end:
        b2.append(it)
    elif age <= b3_end + 1.0:
        b3.append(it)

for label, arr in [(f"GH B1 ({win['b1_label']})", b1), (f"GH B2 ({win['b2_label']})", b2), (f"GH B3 ({win['b3_label']})", b3)]:
    print(f"\n=== {label} (filtered count={len(arr)}) ===")
    for it in arr[:20]:
        repo = it["full_name"]
        res = subprocess.run(["gh", "api", f"repos/{repo}"], capture_output=True, text=True)
        if res.returncode == 0:
            d = json.loads(res.stdout)
            sz = d.get("size", 0)
            lic = (d.get("license") or {}).get("spdx_id") or "None"
            hp = d.get("homepage") or ""
            print(f"  {repo} | ★{d.get('stargazers_count')} | vel={it['velocity']}/h | age={it['age_h']}h | size={sz}KB | lic={lic} | lang={d.get('language')} | hp={hp}")
            print(f"     desc: {it['desc'][:120]}")
