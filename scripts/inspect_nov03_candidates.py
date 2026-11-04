# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")

with open(scratch_dir / "trending_repos_nov03.json", "r", encoding="utf-8") as f:
    trending = json.load(f)

with open(scratch_dir / "gh_search_items_nov03.json", "r", encoding="utf-8") as f:
    gh_search = json.load(f)

with open(scratch_dir / "hn_stories_nov03.json", "r", encoding="utf-8") as f:
    hn = json.load(f)

print("=== 1. TOP UNSEEN GITHUB TRENDING REPOS ===")
unseen_trending = [r for r in trending if not r.get("seen")]
unseen_trending.sort(key=lambda x: x.get("period_stars", 0), reverse=True)

for idx, r in enumerate(unseen_trending[:35], 1):
    print(f"{idx:2d}. {r['repo']} ({r.get('lang')}) | +{r.get('period_stars')} ({r.get('source')}) | Total: {r.get('total_stars')}")
    print(f"    {r.get('desc')}")

print("\n=== 2. TOP HACKER NEWS STORIES (by Points & Velocity) ===")
hn.sort(key=lambda x: x.get("points", 0), reverse=True)
for idx, s in enumerate(hn[:30], 1):
    print(f"{idx:2d}. [{s.get('points')} pts / {s.get('comments')} comments / {s.get('age_h', 0):.1f}h ago / Vel: {s.get('velocity', 0):.1f}/h] {s.get('title')}")
    print(f"    URL: {s.get('url')}")
    print(f"    HN: {s.get('hn_url')}")

print("\n=== 3. TOP GH SEARCH REPOS CREATED IN LAST 30h ===")
gh_valid = []
for it in gh_search:
    name = it.get('full_name', '').lower()
    desc = (it.get('description') or '').lower()
    if any(k in name or k in desc for k in ['roblox', 'cheat', 'aimbot', 'hack-menu', 'executor', 'free-robux', 'dlss-5-swapper', 'crack', 'bypass']):
        continue
    gh_valid.append(it)

gh_valid.sort(key=lambda x: x.get('stargazers_count', 0), reverse=True)
for idx, r in enumerate(gh_valid[:30], 1):
    print(f"{idx:2d}. {r.get('full_name')} ({r.get('language')}) | Stars: {r.get('stargazers_count')} | Forks: {r.get('forks_count')}")
    print(f"    {r.get('description')}")
    print(f"    Created: {r.get('created_at')}")
