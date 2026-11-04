# -*- coding: utf-8 -*-
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")

with open(scratch_dir / "gh_search_items_nov03.json", "r", encoding="utf-8") as f:
    gh_items = json.load(f)

with open(scratch_dir / "hn_stories_nov03.json", "r", encoding="utf-8") as f:
    hn_items = json.load(f)

now = datetime.now(timezone.utc)

main_story_repos = [
    "vercel-labs/agent-desktop",
    "Donchitos/Claude-Code-Game-Studios",
    "JustVugg/colibri",
    "anomalyco/hex",
    "calesthio/OpenMontage"
]

# Process GitHub Candidates
# Exclude main stories, spam, cheats, obvious malware installers
banned_keywords = ['roblox', 'cheat', 'aimbot', 'hack-menu', 'executor', 'free-robux', 'dlss-5-swapper', 
                   'crack', 'bypass', 'installer', 'pre-activated', 'monero', 'miner', 'unlocktool',
                   'generator', 'free-download', 'pirate', 'keygen']

gh_candidates = []
for it in gh_items:
    name = it.get('full_name', '')
    if any(m.lower() == name.lower() for m in main_story_repos):
        continue
    desc = (it.get('description') or '').lower()
    name_l = name.lower()
    if any(k in name_l or k in desc for k in banned_keywords):
        continue
    
    # Check creation time
    created_str = it.get('created_at')
    try:
        created_dt = datetime.strptime(created_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except:
        continue
    age_h = max((now - created_dt).total_seconds() / 3600.0, 0.0)
    if age_h > 30.0:
        continue
    
    stars = it.get('stargazers_count', 0)
    vel = stars / max(age_h, 0.2)
    gh_candidates.append({
        "full_name": name,
        "html_url": it.get('html_url'),
        "description": it.get('description'),
        "language": it.get('language') or 'General',
        "stars": stars,
        "forks": it.get('forks_count', 0),
        "created_at": created_str,
        "age_h": age_h,
        "velocity": vel
    })

# Bucketing for GH: 0~10h, 10~20h, 20~30h
b1_gh = [r for r in gh_candidates if 0.0 <= r['age_h'] < 10.0]
b2_gh = [r for r in gh_candidates if 10.0 <= r['age_h'] < 20.0]
b3_gh = [r for r in gh_candidates if 20.0 <= r['age_h'] <= 30.0]

b1_gh.sort(key=lambda x: x['velocity'], reverse=True)
b2_gh.sort(key=lambda x: x['velocity'], reverse=True)
b3_gh.sort(key=lambda x: x['velocity'], reverse=True)

print("=== GITHUB CANDIDATES BUCKET 1 ===")
print(f"Bucket 1 (0~10h): {len(b1_gh)} items")
for i, r in enumerate(b1_gh[:12]):
    print(f"  {i+1}. {r['full_name']} ({r['language']}) | {r['stars']} stars | {r['age_h']:.1f}h | Vel: {r['velocity']:.1f}/h")
    print(f"     {r['description']}")


print(f"\nBucket 2 (10~20h): {len(b2_gh)} items")
for i, r in enumerate(b2_gh[:8]):
    print(f"  {i+1}. {r['full_name']} ({r['language']}) | {r['stars']} stars | {r['age_h']:.1f}h | Vel: {r['velocity']:.1f}/h")
    print(f"     {r['description']}")

print(f"\nBucket 3 (20~30h): {len(b3_gh)} items")
for i, r in enumerate(b3_gh[:8]):
    print(f"  {i+1}. {r['full_name']} ({r['language']}) | {r['stars']} stars | {r['age_h']:.1f}h | Vel: {r['velocity']:.1f}/h")
    print(f"     {r['description']}")

# Process Hacker News Candidates
hn_candidates = []
for s in hn_items:
    url = s.get('url', '')
    title = s.get('title', '')
    pts = s.get('points', 0)
    age_h = s.get('age_h', 0.0)
    vel = s.get('velocity', 0.0)
    
    # Filter non-tech / off-topic
    if any(k in title.lower() for k in ['boy names', 'bones may release', 'freezer', 'supermarket', 'nurses sound alarm']):
        continue
    
    hn_candidates.append(s)

b1_hn = [s for s in hn_candidates if 0.0 <= s['age_h'] < 10.0]
b2_hn = [s for s in hn_candidates if 10.0 <= s['age_h'] < 20.0]
b3_hn = [s for s in hn_candidates if 20.0 <= s['age_h'] <= 30.0]

b1_hn.sort(key=lambda x: x['velocity'], reverse=True)
b2_hn.sort(key=lambda x: x['velocity'], reverse=True)
b3_hn.sort(key=lambda x: x['velocity'], reverse=True)

print("\n=== HACKER NEWS CANDIDATES ===")
print(f"Bucket 1 (0~10h): {len(b1_hn)} items")
for i, s in enumerate(b1_hn[:8]):
    print(f"  {i+1}. [{s['points']} pts | {s['age_h']:.1f}h | Vel: {s['velocity']:.1f}/h] {s['title']}")
    print(f"     URL: {s['url']}")

print(f"\nBucket 2 (10~20h): {len(b2_hn)} items")
for i, s in enumerate(b2_hn[:8]):
    print(f"  {i+1}. [{s['points']} pts | {s['age_h']:.1f}h | Vel: {s['velocity']:.1f}/h] {s['title']}")
    print(f"     URL: {s['url']}")

print(f"\nBucket 3 (20~30h): {len(b3_hn)} items")
for i, s in enumerate(b3_hn[:8]):
    print(f"  {i+1}. [{s['points']} pts | {s['age_h']:.1f}h | Vel: {s['velocity']:.1f}/h] {s['title']}")
    print(f"     URL: {s['url']}")
