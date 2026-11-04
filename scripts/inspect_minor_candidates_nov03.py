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

with open(scratch_dir / "hn_stories_nov03.json", "r", encoding="utf-8") as f:
    hn_items = json.load(f)

now = datetime.now(timezone.utc)

main_repos = [
    "vercel-labs/agent-desktop",
    "Donchitos/Claude-Code-Game-Studios",
    "JustVugg/colibri",
    "anomalyco/hex",
    "calesthio/OpenMontage"
]

seen_file = Path(r"c:\Program Files\1a\src\gitnews\history_seen_projects.md")
with open(seen_file, "r", encoding="utf-8") as f:
    seen_text = f.read().lower()

spam_keywords = [
    'menu', 'cheat', 'aimbot', 'hack', 'roblox', 'spicy', 'nsfw', 'adult',
    'installer', 'cracked', 'bypass', 'unlocked', 'pre-activated', 'key-generator',
    'free-robux', 'dlss-5', 'monero', 'miner', 'unlocktool', 'generator',
    'comment-automation', 'follower', 'tiktok-comment', 'recoverit', 'touch-copy',
    'sp-flash-tool', '4ukey', 'dr.fone', 'tenorshare', 'foneazy', 'anyunlock',
    'trading-bot', 'server-raider', 'server-cloner', 'discord-quest', 'aim-assist',
    'video-maker', 'pdf-compressor-offline', 'animated-wallpapers'
]

# 1. GH Filter
gh_clean = []
for it in gh_items:
    name = it.get('full_name', '')
    if any(m.lower() == name.lower() for m in main_repos):
        continue
    if name.lower() in seen_text:
        continue
    desc = (it.get('description') or '').lower()
    name_l = name.lower()
    if any(k in name_l or k in desc for k in spam_keywords):
        continue
    try:
        c_dt = datetime.strptime(it.get('created_at'), "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        age_h = max((now - c_dt).total_seconds() / 3600.0, 0.0)
    except:
        continue
    if age_h > 30.0:
        continue
    stars = it.get('stargazers_count', 0)
    vel = stars / max(age_h, 0.2)
    gh_clean.append({
        "name": name,
        "stars": stars,
        "forks": it.get('forks_count', 0),
        "lang": it.get('language') or 'General',
        "age_h": age_h,
        "vel": vel,
        "desc": it.get('description') or '',
        "url": it.get('html_url')
    })

b1_gh = [r for r in gh_clean if 0.0 <= r['age_h'] < 10.0]
b2_gh = [r for r in gh_clean if 10.0 <= r['age_h'] < 20.0]
b3_gh = [r for r in gh_clean if 20.0 <= r['age_h'] <= 30.0]

for b in (b1_gh, b2_gh, b3_gh):
    b.sort(key=lambda x: x['vel'], reverse=True)

print("=== GITHUB CLEAN BUCKET 1 (0~10h) ===")
for i, r in enumerate(b1_gh[:10]):
    print(f"{i+1:2d}. [{r['stars']}s | {r['age_h']:.1f}h | Vel {r['vel']:.1f}] {r['name']} ({r['lang']})")
    print(f"    {r['desc'][:90]}")

print("\n=== GITHUB CLEAN BUCKET 2 (10~20h) ===")
for i, r in enumerate(b2_gh[:10]):
    print(f"{i+1:2d}. [{r['stars']}s | {r['age_h']:.1f}h | Vel {r['vel']:.1f}] {r['name']} ({r['lang']})")
    print(f"    {r['desc'][:90]}")

print("\n=== GITHUB CLEAN BUCKET 3 (20~30h) ===")
for i, r in enumerate(b3_gh[:10]):
    print(f"{i+1:2d}. [{r['stars']}s | {r['age_h']:.1f}h | Vel {r['vel']:.1f}] {r['name']} ({r['lang']})")
    print(f"    {r['desc'][:90]}")

# 2. HN Filter
hn_clean = []
for it in hn_items:
    title = it.get('title') or ''
    title_l = title.lower()
    url = it.get('url') or ''
    # Exclude if in seen_text
    if it.get('id') and str(it.get('id')) in seen_text:
        continue
    # Exclude general political/commercial non-tech news unless highly relevant dev story
    age_h = it.get('age_h', 0)
    if age_h > 30.0:
        continue
    pts = it.get('points', 0)
    vel = it.get('velocity', 0)
    hn_clean.append({
        "id": it.get('id'),
        "title": title,
        "url": url,
        "hn_url": it.get('hn_url'),
        "points": pts,
        "comments": it.get('comments', 0),
        "age_h": age_h,
        "vel": vel
    })

b1_hn = [r for r in hn_clean if 0.0 <= r['age_h'] < 10.0]
b2_hn = [r for r in hn_clean if 10.0 <= r['age_h'] < 20.0]
b3_hn = [r for r in hn_clean if 20.0 <= r['age_h'] <= 30.0]

for b in (b1_hn, b2_hn, b3_hn):
    b.sort(key=lambda x: x['vel'], reverse=True)

print("\n=== HACKER NEWS BUCKET 1 (0~10h) ===")
for i, r in enumerate(b1_hn[:10]):
    print(f"{i+1:2d}. [{r['points']}p | {r['comments']}c | {r['age_h']:.1f}h | Vel {r['vel']:.1f}] {r['title']}")
    print(f"    {r['url'][:90]}")

print("\n=== HACKER NEWS BUCKET 2 (10~20h) ===")
for i, r in enumerate(b2_hn[:10]):
    print(f"{i+1:2d}. [{r['points']}p | {r['comments']}c | {r['age_h']:.1f}h | Vel {r['vel']:.1f}] {r['title']}")
    print(f"    {r['url'][:90]}")

print("\n=== HACKER NEWS BUCKET 3 (20~30h) ===")
for i, r in enumerate(b3_hn[:10]):
    print(f"{i+1:2d}. [{r['points']}p | {r['comments']}c | {r['age_h']:.1f}h | Vel {r['vel']:.1f}] {r['title']}")
    print(f"    {r['url'][:90]}")
