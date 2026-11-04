import subprocess
import json
import sys
from datetime import datetime, timezone, timedelta

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

now = datetime.now(timezone.utc)
since_30h = (now - timedelta(hours=30)).strftime("%Y-%m-%dT%H:%M:%SZ")

spam_keywords = ["crack", "installer", "pre-activated", "standalone setup", "full working", "roblox", "cheat", "aimbot", "spoofer", "driver booster", "key generator", "license key", "free-robux", "canva", "adobe", "autodesk", "fl studio", "coreldraw", "nero-platinum", "anydesk", "avid-media", "keyshot", "ibmspss", "dvd-creator", "axie-infinity"]

all_items = []
for page in [1, 2, 3, 4, 5]:
    res = subprocess.run(["gh", "api", f"search/repositories?q=created:>{since_30h}&sort=stars&order=desc&per_page=100&page={page}"], capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        break
    data = json.loads(res.stdout)
    items = data.get("items", [])
    if not items:
        break
    for it in items:
        desc = (it.get("description") or "").lower()
        name = it["full_name"].lower()
        if any(k in desc or k in name for k in spam_keywords):
            continue
        if 230 <= it["stargazers_count"] <= 245 and "desktop" in desc:
            continue
        created = datetime.fromisoformat(it['created_at'].replace('Z', '+00:00'))
        age_h = max((now - created).total_seconds() / 3600.0, 0.2)
        vel = it['stargazers_count'] / age_h
        it['age_h'] = age_h
        it['velocity'] = vel
        all_items.append(it)

print(f"Total clean repos from last 30h: {len(all_items)}")
for it in sorted(all_items, key=lambda x: x["velocity"], reverse=True)[:35]:
    print(f"[{it['stargazers_count']:4d}★ | {it['age_h']:4.1f}h | {it['velocity']:5.1f}★/h] {it['full_name']}")
    print(f"     Desc: {it['description']}")
