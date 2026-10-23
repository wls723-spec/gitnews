import urllib.request
import json
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}
now = datetime.datetime.now(datetime.timezone.utc)
cutoff_24h_ts = int((now - datetime.timedelta(hours=24)).timestamp())

print("=== Hacker News 최근 24시간 점수대별 통계 ===")
for pts in [50, 30, 20, 15, 10]:
    url = f'https://hn.algolia.com/api/v1/search_by_date?tags=show_hn&numericFilters=created_at_i>{cutoff_24h_ts},points>={pts}&hitsPerPage=1'
    d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read().decode('utf-8'))
    print(f"Show HN (points >= {pts}): 총 {d.get('nbHits')}개")

print("\n--- Show HN (points >= 15) 전체 목록 ---")
url = f'https://hn.algolia.com/api/v1/search_by_date?tags=show_hn&numericFilters=created_at_i>{cutoff_24h_ts},points>=15&hitsPerPage=20'
d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read().decode('utf-8'))
for i, h in enumerate(d.get('hits', [])):
    print(f"[{i+1}] {h.get('title')} (🔺 {h.get('points')} pts) | URL: {h.get('url')}")
