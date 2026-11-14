# -*- coding: utf-8 -*-
import json
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).resolve().parent.parent
with open(REPO_ROOT / "history_seen_projects.md", "r", encoding="utf-8") as f:
    seen = f.read().lower()

with open(REPO_ROOT / "candidates_nov15.json", "r", encoding="utf-8") as f:
    cand = json.load(f)

win = cand["window"]
b1_end = win["b1_range"][1]
b2_end = win["b2_range"][1]
b3_end = win["b3_range"][1]

print("=== DAILY TRENDING (UNSEEN) ===")
for it in sorted(cand["trending"], key=lambda x: x["stars_today"], reverse=True):
    sources = it.get("sources", [])
    if not any("Daily" in s for s in sources):
        continue
    name = it["name"]
    short = name.split("/")[-1].lower()
    if name.lower() in seen or short in seen:
        continue
    print(f"  {name} (★{it['stars_today']}) [{it['lang']}] ({', '.join(sources)}): {it['desc'][:100]}")

print("\n=== TOP WEEKLY TRENDING (UNSEEN, NOT IN DAILY) ===")
for it in sorted(cand["trending"], key=lambda x: x["stars_today"], reverse=True):
    sources = it.get("sources", [])
    if any("Daily" in s for s in sources):
        continue
    name = it["name"]
    short = name.split("/")[-1].lower()
    if name.lower() in seen or short in seen:
        continue
    print(f"  {name} (★{it['stars_today']}) [{it['lang']}] ({', '.join(sources)}): {it['desc'][:100]}")

# Identify botnet duplicate repo names in gh_new
repo_short_counts = Counter(it["full_name"].split("/")[-1].lower() for it in cand["gh_new"])
spam_keywords = [
    "iptv_player", "github-copilot-app", "ai--manus", "capri-ai",
    "rpocket", "respocket", "resp-", "cheat", "aimbot", "spoofer",
    "keygen", "crack", "torrent", "free-robux", "setup-guide", "blooket",
    "deadlock", "driver-booster", "desktop setup with", "malware-defender-desktop",
    "topaz-video-ai-desktop", "izotope-rx-11-desktop", "dxo-photolab-10-desktop",
    "muse-protocol"
]

def is_seen(name):
    n = name.lower()
    short = n.split("/")[-1]
    return n in seen or short in seen

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
    if is_seen(title) or is_seen(url):
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
    for x in arr[:12]:
        print(f"  {x['full_name']} (★{x['stars']}, vel={x['velocity']}/h, age={x['age_h']}h) [{x['lang']}]: {x['desc'][:90]}")

for label, arr in [(f"HN B1 {win['b1_label']}", b1_hn), (f"HN B2 {win['b2_label']}", b2_hn), (f"HN B3 {win['b3_label']}", b3_hn)]:
    print(f"\n--- {label} ---")
    for x in arr[:12]:
        print(f"  {x['title']} (pts={x['points']}, vel={x['velocity']}/h, age={x['age_h']}h): {x['url'][:80]}")
