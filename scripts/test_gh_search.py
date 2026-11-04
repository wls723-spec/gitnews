import urllib.request
import json
import sys
from datetime import datetime, timezone, timedelta

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Current time
now = datetime.now(timezone.utc)
since_30h = (now - timedelta(hours=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
print(f"Searching GitHub repos created since: {since_30h}")

url = f"https://api.github.com/search/repositories?q=created:>{since_30h}&sort=stars&order=desc&per_page=30"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print(f"Total found: {data.get('total_count', 0)}")
        for it in data.get('items', [])[:20]:
            created = datetime.fromisoformat(it['created_at'].replace('Z', '+00:00'))
            age_h = max((now - created).total_seconds() / 3600.0, 0.2)
            velocity = it['stargazers_count'] / age_h
            desc = (it['description'] or '')[:70]
            print(f"{it['full_name']:35} | {it['stargazers_count']:4d} stars | {age_h:4.1f}h ago | Vel: {velocity:5.1f} */h | {desc}")
except Exception as e:
    print(f"Error: {e}")
