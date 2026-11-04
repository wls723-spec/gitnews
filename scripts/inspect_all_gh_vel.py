# -*- coding: utf-8 -*-
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")

with open(scratch_dir / "gh_search_items_nov03.json", "r", encoding="utf-8") as f:
    gh_items = json.load(f)

now = datetime.now(timezone.utc)

# Let's inspect the top 100 items by stars or velocity
items_with_meta = []
for it in gh_items:
    try:
        c_dt = datetime.strptime(it.get('created_at'), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        age_h = max((now - c_dt).total_seconds() / 3600.0, 0.0)
    except:
        continue
    if age_h > 30.0:
        continue
    stars = it.get('stargazers_count', 0)
    vel = stars / max(age_h, 0.2)
    name = it.get('full_name', '')
    desc = it.get('description') or ''
    items_with_meta.append({
        "name": name,
        "stars": stars,
        "age_h": age_h,
        "vel": vel,
        "lang": it.get('language') or 'General',
        "desc": desc
    })

items_with_meta.sort(key=lambda x: x['vel'], reverse=True)

print("=== ALL ITEMS SORTED BY VELOCITY (TOP 40) ===")
for i, it in enumerate(items_with_meta[:40]):
    print(f"{i+1:2d}. [{it['stars']}s | {it['age_h']:.1f}h | Vel {it['vel']:.1f}] {it['name']} ({it['lang']})")
    print(f"    {it['desc'][:80]}")
