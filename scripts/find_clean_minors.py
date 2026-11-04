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

spam_words = [
    'menu', 'cheat', 'aimbot', 'hack', 'roblox', 'spicy', 'nsfw', 'adult',
    'installer', 'cracked', 'bypass', 'unlocked', 'pre-activated', 'key-generator',
    'free-robux', 'dlss-5', 'monero', 'miner', 'unlocktool', 'generator',
    'comment-automation', 'follower', 'tiktok-comment'
]

valid = []
for it in gh_items:
    name = it.get('full_name', '')
    desc = (it.get('description') or '').lower()
    name_l = name.lower()
    if any(s in name_l or s in desc for s in spam_words):
        continue
    
    # Calculate age
    try:
        c_dt = datetime.strptime(it.get('created_at'), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        age_h = max((now - c_dt).total_seconds() / 3600.0, 0.0)
    except:
        continue
        
    if age_h > 30.0:
        continue
        
    stars = it.get('stargazers_count', 0)
    vel = stars / max(age_h, 0.2)
    valid.append({
        "repo": name,
        "stars": stars,
        "forks": it.get('forks_count', 0),
        "lang": it.get('language') or 'General',
        "age_h": age_h,
        "vel": vel,
        "desc": it.get('description')
    })

b1 = [r for r in valid if 0.0 <= r['age_h'] < 10.0]
b2 = [r for r in valid if 10.0 <= r['age_h'] < 20.0]
b3 = [r for r in valid if 20.0 <= r['age_h'] <= 30.0]

b1.sort(key=lambda x: x['vel'], reverse=True)
b2.sort(key=lambda x: x['vel'], reverse=True)
b3.sort(key=lambda x: x['vel'], reverse=True)

print("--- GH BUCKET 1 (0~10h) ---")
for r in b1[:6]:
    print(f"[{r['stars']}s / {r['age_h']:.1f}h / Vel {r['vel']:.1f}] {r['repo']} ({r['lang']}) - {r['desc']}")

print("\n--- GH BUCKET 2 (10~20h) ---")
for r in b2[:6]:
    print(f"[{r['stars']}s / {r['age_h']:.1f}h / Vel {r['vel']:.1f}] {r['repo']} ({r['lang']}) - {r['desc']}")

print("\n--- GH BUCKET 3 (20~30h) ---")
for r in b3[:6]:
    print(f"[{r['stars']}s / {r['age_h']:.1f}h / Vel {r['vel']:.1f}] {r['repo']} ({r['lang']}) - {r['desc']}")
