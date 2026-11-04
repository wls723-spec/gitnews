# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")

with open(scratch_dir / "gh_search_items_nov04.json", "r", encoding="utf-8") as f:
    gh_items = json.load(f)

with open(scratch_dir / "hn_stories_nov04.json", "r", encoding="utf-8") as f:
    hn_items = json.load(f)

with open(scratch_dir / "trending_repos_nov04.json", "r", encoding="utf-8") as f:
    trending_items = json.load(f)

seen_file = Path(r"c:\Program Files\1a\src\gitnews\history_seen_projects.md")
with open(seen_file, "r", encoding="utf-8") as f:
    seen_text = f.read().lower()

# Main 5 stories to exclude from minors
main_5_repos = [
    "karpathy/nanochat",
    "p-e-w/heretic",
    "pingdotgg/t3code",
    "floci-io/floci",
    "keygraphhq/shannon"
]

# Excluded titles/topics for spam or duplication
spam_keywords = ["crack", "installer", "pre-activated", "standalone setup", "full working", "roblox", "cheat", "aimbot", "spoofer", "driver booster", "key generator", "license key", "free-robux", "canva", "adobe", "autodesk", "fl studio", "coreldraw", "nero-platinum", "anydesk", "avid-media", "keyshot", "ibmspss", "dvd-creator", "axie-infinity"]

print("=== 1. FILTERING GITHUB ITEMS ===")
clean_gh = []
for it in gh_items:
    name = it["full_name"].lower()
    desc = (it.get("description") or "").lower()
    if any(m in name for m in main_5_repos):
        continue
    if name in seen_text:
        continue
    if any(k in desc or k in name for k in spam_keywords):
        continue
    # Require at least some stars or velocity
    if it.get("stargazers_count", 0) < 10:
        continue
    clean_gh.append(it)

# Bucket 1: 0~10.4h, Bucket 2: 10.4~20.8h, Bucket 3: 20.8~31.2h
gh_b1 = [it for it in clean_gh if it.get("age_h", 0) < 10.4]
gh_b2 = [it for it in clean_gh if 10.4 <= it.get("age_h", 0) < 20.8]
gh_b3 = [it for it in clean_gh if 20.8 <= it.get("age_h", 0) <= 32.0]

gh_b1.sort(key=lambda x: x.get("velocity", 0), reverse=True)
gh_b2.sort(key=lambda x: x.get("velocity", 0), reverse=True)
gh_b3.sort(key=lambda x: x.get("velocity", 0), reverse=True)

print(f"GH Pool: B1={len(gh_b1)}, B2={len(gh_b2)}, B3={len(gh_b3)}")

print("\n=== TOP GH CANDIDATES B1 (0~10.4h) ===")
for it in gh_b1[:8]:
    print(f"  [{it['stargazers_count']}★ | {it['age_h']:.1f}h | {it['velocity']:.1f}★/h] {it['full_name']} : {it.get('description')}")

print("\n=== TOP GH CANDIDATES B2 (10.4~20.8h) ===")
for it in gh_b2[:8]:
    print(f"  [{it['stargazers_count']}★ | {it['age_h']:.1f}h | {it['velocity']:.1f}★/h] {it['full_name']} : {it.get('description')}")

print("\n=== TOP GH CANDIDATES B3 (20.8~31.2h) ===")
for it in gh_b3[:8]:
    print(f"  [{it['stargazers_count']}★ | {it['age_h']:.1f}h | {it['velocity']:.1f}★/h] {it['full_name']} : {it.get('description')}")

print("\n" + "="*60)
print("=== 2. FILTERING HACKER NEWS ITEMS ===")
print("="*60)
clean_hn = []
for it in hn_items:
    title = it.get("title", "").lower()
    url = (it.get("url") or "").lower()
    if any(m in title or m in url for m in main_5_repos):
        continue
    # Exclude non-tech / purely political news
    if any(k in title for k in ["nfl players", "felony charges", "gambling laws", "net worth for people"]):
        continue
    clean_hn.append(it)

hn_b1 = [it for it in clean_hn if it.get("age_h", 0) < 10.4]
hn_b2 = [it for it in clean_hn if 10.4 <= it.get("age_h", 0) < 20.8]
hn_b3 = [it for it in clean_hn if 20.8 <= it.get("age_h", 0) <= 32.0]

hn_b1.sort(key=lambda x: x.get("velocity", 0), reverse=True)
hn_b2.sort(key=lambda x: x.get("velocity", 0), reverse=True)
hn_b3.sort(key=lambda x: x.get("velocity", 0), reverse=True)

print(f"HN Pool: B1={len(hn_b1)}, B2={len(hn_b2)}, B3={len(hn_b3)}")

print("\n=== TOP HN CANDIDATES B1 (0~10.4h) ===")
for it in hn_b1[:8]:
    print(f"  [{it['points']}pts | {it['age_h']:.1f}h | {it['velocity']:.1f}pts/h] {it['title']} ({it.get('url')})")

print("\n=== TOP HN CANDIDATES B2 (10.4~20.8h) ===")
for it in hn_b2[:8]:
    print(f"  [{it['points']}pts | {it['age_h']:.1f}h | {it['velocity']:.1f}pts/h] {it['title']} ({it.get('url')})")

print("\n=== TOP HN CANDIDATES B3 (20.8~31.2h) ===")
for it in hn_b3[:8]:
    print(f"  [{it['points']}pts | {it['age_h']:.1f}h | {it['velocity']:.1f}pts/h] {it['title']} ({it.get('url')})")
