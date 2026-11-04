import urllib.request
import json
import sys
import re
from datetime import datetime, timezone, timedelta
from concurrent.futures import ThreadPoolExecutor

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

now = datetime.now(timezone.utc)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

print(f"Current UTC time: {now.isoformat()}", flush=True)

# 1. Fetch GitHub candidates created in last 30h
since_30h = (now - timedelta(hours=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
gh_items = []

for page in [1, 2, 3]:
    url = f"https://api.github.com/search/repositories?q=created:>{since_30h}&sort=stars&order=desc&per_page=100&page={page}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            gh_items.extend(data.get('items', []))
    except Exception as e:
        print(f"GH API Error on page {page}: {e}", flush=True)
        break

print(f"Total GH items retrieved: {len(gh_items)}", flush=True)

# 2. Fetch Hacker News IDs
hn_ids = []
for endpoint in ["showstories.json", "topstories.json", "newstories.json"]:
    try:
        url = f"https://hacker-news.firebaseio.com/v0/{endpoint}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            ids = json.loads(resp.read().decode('utf-8'))
            hn_ids.extend(ids[:100])
    except Exception as e:
        print(f"HN API Error {endpoint}: {e}", flush=True)

hn_ids = list(dict.fromkeys(hn_ids))[:180]
print(f"Total unique HN story IDs to check in parallel: {len(hn_ids)}", flush=True)

def fetch_hn_item(sid):
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            item = json.loads(resp.read().decode('utf-8'))
            if item and item.get('type') == 'story' and not item.get('deleted') and not item.get('dead'):
                st_time = datetime.fromtimestamp(item.get('time', 0), tz=timezone.utc)
                age_h = (now - st_time).total_seconds() / 3600.0
                if 0 <= age_h <= 30:
                    pts = item.get('score', 0)
                    vel = pts / max(age_h, 0.2)
                    item['age_h'] = age_h
                    item['velocity'] = vel
                    return item
    except Exception:
        pass
    return None

hn_stories = []
with ThreadPoolExecutor(max_workers=20) as executor:
    results = executor.map(fetch_hn_item, hn_ids)
    for r in results:
        if r:
            hn_stories.append(r)

print(f"Total valid HN stories in last 30h: {len(hn_stories)}", flush=True)

# Process GitHub buckets
gh_clean = []
for it in gh_items:
    name = it['full_name'].lower()
    desc = (it.get('description') or '').lower()
    if any(k in name or k in desc for k in ['roblox', 'cheat', 'aimbot', 'hack-menu', 'executor', 'free-robux', 'dlss-5-swapper']):
        continue
    created = datetime.fromisoformat(it['created_at'].replace('Z', '+00:00'))
    age_h = (now - created).total_seconds() / 3600.0
    if 0 <= age_h <= 30:
        stars = it['stargazers_count']
        vel = stars / max(age_h, 0.2)
        it['age_h'] = age_h
        it['velocity'] = vel
        gh_clean.append(it)

b1_gh = [x for x in gh_clean if 0 <= x['age_h'] < 10]
b2_gh = [x for x in gh_clean if 10 <= x['age_h'] < 20]
b3_gh = [x for x in gh_clean if 20 <= x['age_h'] <= 30]

b1_gh.sort(key=lambda x: x['velocity'], reverse=True)
b2_gh.sort(key=lambda x: x['velocity'], reverse=True)
b3_gh.sort(key=lambda x: x['velocity'], reverse=True)

print("\n--- GITHUB BUCKET 1 (0-10h) ---")
for x in b1_gh[:8]:
    print(f"[{x['stargazers_count']}★ | {x['age_h']:.1f}h | {x['velocity']:.1f}★/h] {x['full_name']}: {x['description']}")

print("\n--- GITHUB BUCKET 2 (10-20h) ---")
for x in b2_gh[:8]:
    print(f"[{x['stargazers_count']}★ | {x['age_h']:.1f}h | {x['velocity']:.1f}★/h] {x['full_name']}: {x['description']}")

print("\n--- GITHUB BUCKET 3 (20-30h) ---")
for x in b3_gh[:8]:
    print(f"[{x['stargazers_count']}★ | {x['age_h']:.1f}h | {x['velocity']:.1f}★/h] {x['full_name']}: {x['description']}")

# Process HN buckets
hn_clean = []
for s in hn_stories:
    hn_clean.append(s)

b1_hn = [x for x in hn_clean if 0 <= x['age_h'] < 10]
b2_hn = [x for x in hn_clean if 10 <= x['age_h'] < 20]
b3_hn = [x for x in hn_clean if 20 <= x['age_h'] <= 30]

b1_hn.sort(key=lambda x: x['velocity'], reverse=True)
b2_hn.sort(key=lambda x: x['velocity'], reverse=True)
b3_hn.sort(key=lambda x: x['velocity'], reverse=True)

print("\n--- HN BUCKET 1 (0-10h) ---")
for x in b1_hn[:8]:
    print(f"[{x.get('score')}pts | {x['age_h']:.1f}h | {x['velocity']:.1f}pts/h] {x.get('title')}")
    print(f"   URL: {x.get('url')} | HN: https://news.ycombinator.com/item?id={x.get('id')}")

print("\n--- HN BUCKET 2 (10-20h) ---")
for x in b2_hn[:8]:
    print(f"[{x.get('score')}pts | {x['age_h']:.1f}h | {x['velocity']:.1f}pts/h] {x.get('title')}")
    print(f"   URL: {x.get('url')} | HN: https://news.ycombinator.com/item?id={x.get('id')}")

print("\n--- HN BUCKET 3 (20-30h) ---")
for x in b3_hn[:8]:
    print(f"[{x.get('score')}pts | {x['age_h']:.1f}h | {x['velocity']:.1f}pts/h] {x.get('title')}")
    print(f"   URL: {x.get('url')} | HN: https://news.ycombinator.com/item?id={x.get('id')}")
