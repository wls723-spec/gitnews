import urllib.request
import json
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}
now = datetime.datetime.now(datetime.timezone.utc)
cutoff = (now - datetime.timedelta(hours=48)).strftime('%Y-%m-%dT%H:%M:%SZ')
url = f'https://api.github.com/search/repositories?q=created:%3E{cutoff}+stars:%3E=50&sort=stars&order=desc&per_page=30'

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
    print(f"Total count: {data.get('total_count')}")
    for i, it in enumerate(data.get('items', [])):
        print(f"[{i+1}] {it['full_name']} ({it.get('language')}) ⭐ {it.get('stargazers_count')}")
        print(f"    생성일: {it.get('created_at')} | {it.get('html_url')}")
        print(f"    설명: {it.get('description')}")
