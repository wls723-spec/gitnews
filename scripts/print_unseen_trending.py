# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")
with open(scratch_dir / "trending_repos.json", "r", encoding="utf-8") as f:
    trending = json.load(f)

unseen = [r for r in trending if not r["seen"]]
unseen.sort(key=lambda x: x["period_stars"], reverse=True)

print(f"=== TOP UNSEEN GITHUB TRENDING REPOS ({len(unseen)}) ===")
for i, r in enumerate(unseen[:25]):
    print(f"{i+1:2d}. {r['repo']} ({r['lang']}) | +{r['period_stars']} ({r['source']}) | Total: {r['total_stars']}")
    print(f"    {r['desc']}")
