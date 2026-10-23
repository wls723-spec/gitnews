import urllib.request
import json
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}

now = datetime.datetime.now(datetime.timezone.utc)
cutoff_24h_iso = (now - datetime.timedelta(hours=24)).strftime('%Y-%m-%dT%H:%M:%SZ')
print(f"=== GitHub 최근 24시간 이내 생성 (기준: {cutoff_24h_iso} 이후) ===")

url = f"https://api.github.com/search/repositories?q=created:%3E{cutoff_24h_iso}+stars:%3E=20&sort=stars&order=desc&per_page=50"

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        total_count = data.get('total_count', 0)
        items = data.get('items', [])
        print(f"총 발견된 저장소: {total_count}개\n")
        for i, it in enumerate(items[:25]):
            created_dt = datetime.datetime.fromisoformat(it['created_at'].replace('Z', '+00:00'))
            hours_ago = (now - created_dt).total_seconds() / 3600
            print(f"[{i+1}] {it['full_name']} ({it.get('language')}) | ⭐ {it['stargazers_count']}개 | {hours_ago:.1f}시간 전 생성")
            print(f"    URL: {it['html_url']}")
            print(f"    설명: {it.get('description')}\n")
except Exception as e:
    print(f"Error: {e}")
