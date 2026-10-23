import urllib.request
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0'}

for repo in ['anomalyco/opencode', 'ruvnet/ruflo', 'Panniantong/Agent-Reach', 'koala73/worldmonitor', 'farion1231/cc-switch']:
    api_url = f'https://api.github.com/repos/{repo}'
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode('utf-8'))
            print(f"=== {repo} ===")
            print(f"Default branch: {data.get('default_branch')}, Stars: {data.get('stargazers_count')}")
            print(f"Description: {data.get('description')}")
            print(f"Topics: {data.get('topics')}")
    except Exception as e:
        print(f"{repo} api error: {e}")
