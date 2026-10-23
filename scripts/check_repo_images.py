import urllib.request
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0'}

repos = [
    "pbakaus/impeccable",
    "headroomlabs-ai/headroom",
    "tashfeenahmed/freellmapi",
    "Panniantong/Agent-Reach",
    "koala73/worldmonitor"
]

for repo in repos:
    url = f"https://api.github.com/repos/{repo}/contents"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as r:
            import json
            items = json.loads(r.read().decode('utf-8'))
            names = [it['name'] for it in items]
            print(f"[{repo}] root files: {names}")
    except Exception as e:
        print(f"[{repo}] error: {e}")
