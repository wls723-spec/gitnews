import urllib.request
import json
import sys
from datetime import datetime, timezone, timedelta

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

now = datetime.now(timezone.utc)
headers = {"User-Agent": "Mozilla/5.0"}

# Filter list for spam, cracks, cheats
SPAM_KEYWORDS = [
    'kms', 'pico', 'camtasia', 'cinema-4d', 'borisfx', 'roblox', 'cheat', 'aimbot', 
    'hack-menu', 'executor', 'free-robux', 'dlss-5-swapper', 'cracked', 'keygen',
    'activation', 'patcher'
]

# 1. Fetch GitHub candidates created in last 30h
since_30h = (now - timedelta(hours=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
gh_items = []

for page in [1, 2, 3, 4]:
    url = f"https://api.github.com/search/repositories?q=created:>{since_30h}&sort=stars&order=desc&per_page=100&page={page}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            gh_items.extend(data.get('items', []))
    except Exception as e:
        print(f"GH API Error page {page}: {e}")
        break

main_repos = [
    "nutlope/hallmark",
    "jetbrains/thinkrail",
    "tauricresearch/tradingagents",
    "nvidia/skillspector",
    "hkuds/deeptutor"
]

gh_clean = []
for it in gh_items:
    name = it['full_name'].lower()
    desc = (it.get('description') or '').lower()
    if any(m in name for m in main_repos):
        continue
    if any(k in name or k in desc for k in SPAM_KEYWORDS):
        continue
    created = datetime.fromisoformat(it['created_at'].replace('Z', '+00:00'))
    age_h = (now - created).total_seconds() / 3600.0
    if 0 <= age_h <= 30:
        stars = it['stargazers_count']
        vel = stars / max(age_h, 0.2)
        it['age_h'] = age_h
        it['velocity'] = vel
        gh_clean.append(it)

b1 = [x for x in gh_clean if 0 <= x['age_h'] < 10]
b2 = [x for x in gh_clean if 10 <= x['age_h'] < 20]
b3 = [x for x in gh_clean if 20 <= x['age_h'] <= 30]

b1.sort(key=lambda x: x['velocity'], reverse=True)
b2.sort(key=lambda x: x['velocity'], reverse=True)
b3.sort(key=lambda x: x['velocity'], reverse=True)

print("=== GITHUB BUCKET 1 (0-10h) ===")
for x in b1[:10]:
    print(f"[{x['stargazers_count']}★ | {x['age_h']:.1f}h | {x['velocity']:.1f}★/h] {x['full_name']}")
    print(f"   {x['description']}")

print("\n=== GITHUB BUCKET 2 (10-20h) ===")
for x in b2[:10]:
    print(f"[{x['stargazers_count']}★ | {x['age_h']:.1f}h | {x['velocity']:.1f}★/h] {x['full_name']}")
    print(f"   {x['description']}")

print("\n=== GITHUB BUCKET 3 (20-30h) ===")
for x in b3[:10]:
    print(f"[{x['stargazers_count']}★ | {x['age_h']:.1f}h | {x['velocity']:.1f}★/h] {x['full_name']}")
    print(f"   {x['description']}")
