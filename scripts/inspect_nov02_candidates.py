# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")

with open(scratch_dir / "trending_repos.json", "r", encoding="utf-8") as f:
    trending = json.load(f)

with open(scratch_dir / "gh_search_items.json", "r", encoding="utf-8") as f:
    gh_search = json.load(f)

with open(scratch_dir / "hn_stories.json", "r", encoding="utf-8") as f:
    hn = json.load(f)

print("=== 1. TOP UNSEEN GITHUB TRENDING REPOS ===")
unseen_trending = [r for r in trending if not r["seen"]]
unseen_trending.sort(key=lambda x: x["period_stars"], reverse=True)

for idx, r in enumerate(unseen_trending[:30], 1):
    print(f"{idx:2d}. {r['repo']} ({r['lang']}) | +{r['period_stars']} ({r['source']}) | Total: {r['total_stars']}")
    print(f"    {r['desc']}")

print("\n=== 2. TOP HACKER NEWS STORIES (by Points & Velocity) ===")
hn.sort(key=lambda x: x["points"], reverse=True)
for idx, s in enumerate(hn[:25], 1):
    print(f"{idx:2d}. [{s['points']} pts / {s['comments']} comments / {s['age_h']:.1f}h ago / Vel: {s['velocity']:.1f}/h] {s['title']}")
    print(f"    URL: {s['url']}")

print("\n=== 3. TOP GH SEARCH REPOS CREATED IN LAST 78h ===")
# Filter spam
gh_valid = []
for it in gh_search:
    name = it['full_name'].lower()
    desc = (it.get('description') or '').lower()
    if any(k in name or k in desc for k in ['roblox', 'cheat', 'aimbot', 'hack-menu', 'executor', 'free-robux', 'dlss-5-swapper', 'crack', 'bypass']):
        continue
    gh_valid.append(it)

gh_valid.sort(key=lambda x: x['stargazers_count'], reverse=True)
for idx, r in enumerate(gh_valid[:25], 1):
    print(f"{idx:2d}. {r['full_name']} ({r.get('language')}) | Stars: {r['stargazers_count']} | Forks: {r['forks_count']}")
    print(f"    {r.get('description')}")
    print(f"    Created: {r['created_at']}")
