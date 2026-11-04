# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

now = datetime.now(timezone.utc)
scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")

with open(scratch_dir / "gh_search_items.json", "r", encoding="utf-8") as f:
    gh_items = json.load(f)

with open(scratch_dir / "hn_stories.json", "r", encoding="utf-8") as f:
    hn_items = json.load(f)

with open(r"c:\Program Files\1a\src\gitnews\history_seen_projects.md", "r", encoding="utf-8") as f:
    seen_text = f.read().lower()

main_5_repos = [
    "deepseek-ai/dsh-superagent-prototype",
    "ashayas/icloud-s3",
    "beenuar/AiSOC",
    "patch-gg/pixelfx",
    "Arjun-Ingole/hop"
]
main_5_lower = [m.lower() for m in main_5_repos]

# Bucket boundaries (W = 77.6h -> step = 25.9h)
b1_max = 25.9
b2_max = 51.8
b3_max = 77.6

# 1. Filter GH Search
gh_clean = []
spam_keywords = ['roblox', 'cheat', 'aimbot', 'hack-menu', 'executor', 'free-robux', 'dlss-5-swapper', 'crack', 'bypass', 'kms', 'ads-blocker', 'genesis-miner', 'startall-back', 'monero-miner', 'anyunlock', 'discord-quest']

for it in gh_items:
    rname = it['full_name']
    rname_low = rname.lower()
    desc = (it.get('description') or '').lower()
    
    if any(m in rname_low for m in main_5_lower):
        continue
    if rname_low in seen_text:
        continue
    if any(k in rname_low or k in desc for k in spam_keywords):
        continue

    created = datetime.fromisoformat(it['created_at'].replace('Z', '+00:00'))
    age_h = max((now - created).total_seconds() / 3600.0, 0.0)
    if age_h > b3_max:
        continue

    stars = it.get('stargazers_count', 0)
    vel = stars / max(age_h, 0.2)
    it['age_h'] = age_h
    it['velocity'] = vel
    gh_clean.append(it)

b1_gh = [x for x in gh_clean if 0 <= x['age_h'] < b1_max]
b2_gh = [x for x in gh_clean if b1_max <= x['age_h'] < b2_max]
b3_gh = [x for x in gh_clean if b2_max <= x['age_h'] <= b3_max]

b1_gh.sort(key=lambda x: x['velocity'], reverse=True)
b2_gh.sort(key=lambda x: x['velocity'], reverse=True)
b3_gh.sort(key=lambda x: x['velocity'], reverse=True)

print("=== GITHUB BUCKET 1 (0 ~ 25.9h) Top Candidates ===")
for i, x in enumerate(b1_gh[:10]):
    print(f"{i+1:2d}. {x['full_name']} | {x['stargazers_count']} stars | {x['age_h']:.1f}h | Vel: {x['velocity']:.1f}/h | {x.get('description')}")

print("\n=== GITHUB BUCKET 2 (25.9 ~ 51.8h) Top Candidates ===")
for i, x in enumerate(b2_gh[:10]):
    print(f"{i+1:2d}. {x['full_name']} | {x['stargazers_count']} stars | {x['age_h']:.1f}h | Vel: {x['velocity']:.1f}/h | {x.get('description')}")

print("\n=== GITHUB BUCKET 3 (51.8 ~ 77.6h) Top Candidates ===")
for i, x in enumerate(b3_gh[:10]):
    print(f"{i+1:2d}. {x['full_name']} | {x['stargazers_count']} stars | {x['age_h']:.1f}h | Vel: {x['velocity']:.1f}/h | {x.get('description')}")

# 2. Filter Hacker News
hn_clean = []
for it in hn_items:
    title = it.get('title', '')
    url = it.get('url', '')
    
    # Check if duplicates with main 5
    if any(m in url.lower() for m in main_5_lower):
        continue
        
    age_h = it.get('age_h', 0)
    if age_h > b3_max:
        continue
    vel = it.get('points', 0) / max(age_h, 0.2)
    it['velocity'] = vel
    hn_clean.append(it)

b1_hn = [x for x in hn_clean if 0 <= x['age_h'] < b1_max]
b2_hn = [x for x in hn_clean if b1_max <= x['age_h'] < b2_max]
b3_hn = [x for x in hn_clean if b2_max <= x['age_h'] <= b3_max]

b1_hn.sort(key=lambda x: x['velocity'], reverse=True)
b2_hn.sort(key=lambda x: x['velocity'], reverse=True)
b3_hn.sort(key=lambda x: x['velocity'], reverse=True)

print("\n=== HACKER NEWS BUCKET 1 (0 ~ 25.9h) Top Candidates ===")
for i, x in enumerate(b1_hn[:10]):
    print(f"{i+1:2d}. [{x['points']} pts | {x['age_h']:.1f}h | Vel: {x['velocity']:.1f}/h] {x['title']}")
    print(f"    URL: {x['url']}")

print("\n=== HACKER NEWS BUCKET 2 (25.9 ~ 51.8h) Top Candidates ===")
for i, x in enumerate(b2_hn[:10]):
    print(f"{i+1:2d}. [{x['points']} pts | {x['age_h']:.1f}h | Vel: {x['velocity']:.1f}/h] {x['title']}")
    print(f"    URL: {x['url']}")

print("\n=== HACKER NEWS BUCKET 3 (51.8 ~ 77.6h) Top Candidates ===")
for i, x in enumerate(b3_hn[:10]):
    print(f"{i+1:2d}. [{x['points']} pts | {x['age_h']:.1f}h | Vel: {x['velocity']:.1f}/h] {x['title']}")
    print(f"    URL: {x['url']}")
