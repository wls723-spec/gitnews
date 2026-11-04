# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")

with open(scratch_dir / "trending_repos_nov04.json", "r", encoding="utf-8") as f:
    trending = json.load(f)

with open(scratch_dir / "gh_search_items_nov04.json", "r", encoding="utf-8") as f:
    gh_search = json.load(f)

with open(scratch_dir / "hn_stories_nov04.json", "r", encoding="utf-8") as f:
    hn = json.load(f)

seen_file = Path(r"c:\Program Files\1a\src\gitnews\history_seen_projects.md")
with open(seen_file, "r", encoding="utf-8") as f:
    seen_text = f.read().lower()

print("="*60)
print("=== 1. TOP DAILY TRENDING (UNSEEN) ===")
print("="*60)
daily_unseen = [r for r in trending if not r.get("seen") and "Daily" in r.get("source", "")]
daily_unseen.sort(key=lambda x: x.get("period_stars", 0), reverse=True)
for i, r in enumerate(daily_unseen[:20]):
    print(f"[{i+1:2d}] {r['repo']} ({r.get('lang')}) | +{r.get('period_stars')} stars today | Tot: {r.get('total_stars')}")
    print(f"     Desc: {r.get('desc')}")

print("\n" + "="*60)
print("=== 2. TOP WEEKLY TRENDING (UNSEEN) ===")
print("="*60)
weekly_unseen = [r for r in trending if not r.get("seen") and "Weekly" in r.get("source", "")]
weekly_unseen.sort(key=lambda x: x.get("period_stars", 0), reverse=True)
for i, r in enumerate(weekly_unseen[:15]):
    print(f"[{i+1:2d}] {r['repo']} ({r.get('lang')}) | +{r.get('period_stars')} stars this week | Tot: {r.get('total_stars')}")
    print(f"     Desc: {r.get('desc')}")

print("\n" + "="*60)
print("=== 3. TOP HACKER NEWS STORIES (BY POINTS & VELOCITY) ===")
print("="*60)
hn_sorted = sorted(hn, key=lambda x: x.get("points", 0), reverse=True)
for i, s in enumerate(hn_sorted[:20]):
    print(f"[{i+1:2d}] ({s.get('points')} pts | {s.get('comments')} cmts | {s.get('age_h', 0):.1f}h | {s.get('velocity', 0):.1f} pts/h)")
    print(f"     Title: {s.get('title')}")
    print(f"     URL: {s.get('url')}")

print("\n" + "="*60)
print("=== 4. TOP GH SEARCH NEW REPOS (BY VELOCITY) ===")
print("="*60)
gh_search_clean = [it for it in gh_search if it['full_name'].lower() not in seen_text]
gh_search_sorted = sorted(gh_search_clean, key=lambda x: x.get("velocity", 0), reverse=True)
for i, it in enumerate(gh_search_sorted[:25]):
    print(f"[{i+1:2d}] {it['full_name']} ({it.get('language')}) | {it['stargazers_count']}★ | {it.get('age_h', 0):.1f}h | {it.get('velocity', 0):.1f}★/h")
    print(f"     Desc: {it.get('description')}")
