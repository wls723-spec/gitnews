# -*- coding: utf-8 -*-
import subprocess
import json
import sys
from pathlib import Path
from datetime import datetime, timezone, timedelta

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

now = datetime.now(timezone.utc)
since_32h = (now - timedelta(hours=32)).strftime("%Y-%m-%dT%H:%M:%SZ")
print(f"Fetching GitHub Search API via gh CLI for created:>{since_32h}...")

spam_keywords = ["crack", "installer", "pre-activated", "standalone setup", "full working", "roblox", "cheat", "aimbot", "spoofer", "driver booster", "key generator", "license key", "free-robux", "canva", "adobe", "autodesk", "fl studio", "coreldraw", "nero-platinum", "anydesk", "avid-media", "keyshot", "ibmspss", "dvd-creator", "axie-infinity"]

gh_search_items = []
for page in [1, 2, 3, 4, 5]:
    cmd = ["gh", "api", f"search/repositories?q=created:>{since_32h}&sort=stars&order=desc&per_page=100&page={page}"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        print(f"Error on page {page}: {res.stderr}")
        break
    try:
        data = json.loads(res.stdout)
        items = data.get("items", [])
        if not items:
            break
        for it in items:
            desc = (it.get("description") or "").lower()
            name = it["full_name"].lower()
            if any(k in desc or k in name for k in spam_keywords):
                continue
            created = datetime.fromisoformat(it['created_at'].replace('Z', '+00:00'))
            age_h = max((now - created).total_seconds() / 3600.0, 0.2)
            vel = it['stargazers_count'] / age_h
            it['age_h'] = age_h
            it['velocity'] = vel
            gh_search_items.append(it)
        if len(items) < 100:
            break
    except Exception as e:
        print(f"JSON parse error on page {page}: {e}")
        break

print(f"Total clean GH Search items: {len(gh_search_items)}")

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")
with open(scratch_dir / "gh_search_items_nov04.json", "w", encoding="utf-8") as f:
    json.dump(gh_search_items, f, ensure_ascii=False, indent=2)

print("Saved to scratch/gh_search_items_nov04.json")
