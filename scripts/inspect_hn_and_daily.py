# -*- coding: utf-8 -*-
import json
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/hn_stories_nov04.json', 'r', encoding='utf-8') as f:
    hn = json.load(f)

print("=== TOP 30 HACKER NEWS STORIES ===")
hn_sorted = sorted(hn, key=lambda x: x.get('points', 0), reverse=True)
for i, s in enumerate(hn_sorted[:30]):
    print(f"[{i+1:2d}] {s.get('points')} pts | {s.get('comments')} cmts | {s.get('velocity', 0):.1f} pts/h")
    print(f"     Title: {s.get('title')}")
    print(f"     URL: {s.get('url')}")
    print(f"     HN: {s.get('hn_url')}")

with open('scratch/trending_repos_nov04.json', 'r', encoding='utf-8') as f:
    trending = json.load(f)

with open(r'c:\Program Files\1a\src\gitnews\history_seen_projects.md', 'r', encoding='utf-8') as f:
    seen = f.read().lower()

print("\n=== TOP 30 DAILY & WEEKLY TRENDING (DETAILED) ===")
unseen = [r for r in trending if r['repo'].lower() not in seen]
unseen.sort(key=lambda x: x.get('period_stars', 0), reverse=True)
for i, r in enumerate(unseen[:30]):
    print(f"[{i+1:2d}] {r['repo']} | +{r.get('period_stars')} ({r.get('source')}) | Lang: {r.get('lang')}")
    print(f"     Desc: {r.get('desc')}")
