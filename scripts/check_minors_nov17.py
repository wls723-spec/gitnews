# -*- coding: utf-8 -*-
import json
import re
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).resolve().parent.parent
with open(REPO_ROOT / "history_seen_projects.md", "r", encoding="utf-8") as f:
    seen_text = f.read().lower()

# Extract exact seen project names / urls from table rows
seen_names = set()
seen_urls = set()
for line in seen_text.splitlines():
    if line.startswith("| **"):
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 5:
            proj = parts[3].replace("**", "").strip().lower()
            url = parts[4].strip().lower()
            seen_names.add(proj)
            if "/" in proj:
                seen_names.add(proj.split("/")[-1])
            seen_urls.add(url)

with open(REPO_ROOT / "candidates_nov17.json", "r", encoding="utf-8") as f:
    cand = json.load(f)

win = cand["window"]
b1_end = win["b1_range"][1]
b2_end = win["b2_range"][1]
b3_end = win["b3_range"][1]

def is_seen(name, url=""):
    n = name.lower().strip()
    short = n.split("/")[-1] if "/" in n else n
    u = url.lower().strip()
    if n in seen_names or short in seen_names:
        return True
    if u and u in seen_urls:
        return True
    if n in seen_text:
        return True
    return False

print("=== DAILY TRENDING (SORTED BY STARS TODAY) ===")
for it in sorted(cand["trending"], key=lambda x: x["stars_today"], reverse=True):
    sources = it.get("sources", [])
    name = it["name"]
    seen_flag = " [SEEN]" if is_seen(name) else ""
    print(f"  {name}{seen_flag} (★{it['stars_today']}) [{it['lang']}] ({', '.join(sources)}): {it['desc'][:120]}")

repo_short_counts = Counter(it["full_name"].split("/")[-1].lower() for it in cand["gh_new"])
spam_keywords = [
    "iptv_player", "github-copilot-app", "ai--manus", "capri-ai",
    "rpocket", "respocket", "resp-", "cheat", "aimbot", "spoofer",
    "keygen", "crack", "torrent", "free-robux", "setup-guide", "blooket",
    "deadlock", "driver-booster", "desktop setup with", "malware-defender-desktop",
    "topaz-video-ai-desktop", "izotope-rx-11-desktop", "dxo-photolab-10-desktop",
    "muse-protocol"
]

b1_gh, b2_gh, b3_gh = [], [], []
for it in cand["gh_new"]:
    name = it["full_name"]
    short = name.split("/")[-1].lower()
    desc = (it["desc"] or "").lower()
    if is_seen(name):
        continue
    if repo_short_counts[short] > 2:
        continue
    if any(k in name.lower() or k in desc for k in spam_keywords):
        continue
    age = it["age_h"]
    if age < b1_end:
        b1_gh.append(it)
    elif age < b2_end:
        b2_gh.append(it)
    elif age <= b3_end + 1.0:
        b3_gh.append(it)

b1_hn, b2_hn, b3_hn = [], [], []
for it in cand["hn"]:
    title = it["title"]
    url = it["url"] or ""
    if is_seen(title, url):
        continue
    age = it["age_h"]
    if age < b1_end:
        b1_hn.append(it)
    elif age < b2_end:
        b2_hn.append(it)
    elif age <= b3_end + 1.0:
        b3_hn.append(it)

print(f"\nGH Pool (Clean): B1({win['b1_label']})={len(b1_gh)}, B2({win['b2_label']})={len(b2_gh)}, B3({win['b3_label']})={len(b3_gh)}")
print(f"HN Pool: B1({win['b1_label']})={len(b1_hn)}, B2({win['b2_label']})={len(b2_hn)}, B3({win['b3_label']})={len(b3_hn)}")

for label, arr in [(f"GH B1 {win['b1_label']}", b1_gh), (f"GH B2 {win['b2_label']}", b2_gh), (f"GH B3 {win['b3_label']}", b3_gh)]:
    print(f"\n--- {label} ---")
    for x in arr[:18]:
        print(f"  {x['full_name']} (★{x['stars']}, vel={x['velocity']}/h, age={x['age_h']}h, created={x['created_at']}) [{x['lang']}]: {x['desc'][:100]}")

for label, arr in [(f"HN B1 {win['b1_label']}", b1_hn), (f"HN B2 {win['b2_label']}", b2_hn), (f"HN B3 {win['b3_label']}", b3_hn)]:
    print(f"\n--- {label} ---")
    for x in arr[:18]:
        print(f"  {x['title']} (pts={x['points']}, comments={x['comments']}, vel={x['velocity']}/h, age={x['age_h']}h, id={x['objectID']}, created={x['created_at']}): {x['url'][:90]}")
