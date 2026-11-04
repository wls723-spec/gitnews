# -*- coding: utf-8 -*-
import urllib.request
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

now = datetime.now(timezone.utc)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

since_ts = int((now - timedelta(hours=78)).timestamp())
all_hn = []

# Fetch 3 pages of Algolia search
for page in [0, 1, 2, 3]:
    url = f"https://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=created_at_i>{since_ts},points>30&hitsPerPage=100&page={page}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            hits = data.get('hits', [])
            all_hn.extend(hits)
            if len(hits) < 100:
                break
    except Exception as e:
        print(f"Error page {page}: {e}")

print(f"Total HN stories in 78h: {len(all_hn)}")

processed = []
for h in all_hn:
    st_time = datetime.fromtimestamp(h.get('created_at_i', 0), tz=timezone.utc)
    age_h = max((now - st_time).total_seconds() / 3600.0, 0.0)
    pts = h.get('points', 0)
    vel = pts / max(age_h, 0.2)
    processed.append({
        "id": h.get('objectID'),
        "title": h.get('title'),
        "url": h.get('url') or f"https://news.ycombinator.com/item?id={h.get('objectID')}",
        "hn_url": f"https://news.ycombinator.com/item?id={h.get('objectID')}",
        "points": pts,
        "comments": h.get('num_comments', 0),
        "created_at": h.get('created_at'),
        "age_h": age_h,
        "velocity": vel
    })

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")
with open(scratch_dir / "hn_stories_full.json", "w", encoding="utf-8") as f:
    json.dump(processed, f, ensure_ascii=False, indent=2)

b1 = [x for x in processed if 0 <= x['age_h'] < 25.9]
b2 = [x for x in processed if 25.9 <= x['age_h'] < 51.8]
b3 = [x for x in processed if 51.8 <= x['age_h'] <= 78.0]

for name, bucket in [("Bucket 1 (0~25.9h)", b1), ("Bucket 2 (25.9~51.8h)", b2), ("Bucket 3 (51.8~78h)", b3)]:
    bucket.sort(key=lambda x: x['velocity'], reverse=True)
    print(f"\n=== HN {name} (Total: {len(bucket)}) ===")
    for i, x in enumerate(bucket[:8]):
        print(f"{i+1:2d}. [{x['points']} pts | {x['age_h']:.1f}h | Vel: {x['velocity']:.1f}/h] {x['title']}")
        print(f"    URL: {x['url']}")
