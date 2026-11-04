# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")

with open(scratch_dir / "trending_repos_nov03.json", "r", encoding="utf-8") as f:
    trending = json.load(f)

with open(scratch_dir / "hn_stories_nov03.json", "r", encoding="utf-8") as f:
    hn = json.load(f)

with open(scratch_dir / "gh_search_items_nov03.json", "r", encoding="utf-8") as f:
    gh_search = json.load(f)

daily_unseen = [r for r in trending if not r.get("seen") and "Daily" in r.get("source", "")]
daily_unseen.sort(key=lambda x: x.get("period_stars", 0), reverse=True)

print("=== TOP 25 UNSEEN DAILY TRENDING REPOS ===")
for i, r in enumerate(daily_unseen[:25]):
    print(f"{i+1:2d}. {r['repo']} ({r.get('lang')}) | +{r.get('period_stars')} ({r.get('source')})")
    print(f"    {r.get('desc')}\n")

