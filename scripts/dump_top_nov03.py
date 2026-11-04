# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")

with open(scratch_dir / "trending_repos_nov03.json", "r", encoding="utf-8") as f:
    trending = json.load(f)

unseen = [r for r in trending if not r.get("seen")]
unseen.sort(key=lambda x: x.get("period_stars", 0), reverse=True)

print("=== TOP 30 UNSEEN TRENDING REPOS ===")
for i, r in enumerate(unseen[:30]):
    print(f"{i+1:2d}. {r['repo']} ({r.get('lang')}) | +{r.get('period_stars')} ({r.get('source')}) | Total: {r.get('total_stars')}")
    print(f"    {r.get('desc')}\n")
