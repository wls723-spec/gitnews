import urllib.request
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0'}

paths = [
    ("pbakaus/impeccable", "demos"),
    ("pbakaus/impeccable", "docs"),
    ("tashfeenahmed/freellmapi", "repo-assets"),
    ("koala73/worldmonitor", "public"),
    ("Panniantong/Agent-Reach", "docs"),
]

for repo, p in paths:
    url = f"https://api.github.com/repos/{repo}/contents/{p}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as r:
            items = json.loads(r.read().decode('utf-8'))
            names = [it['name'] for it in items]
            print(f"[{repo}/{p}] files: {names}")
    except Exception as e:
        print(f"[{repo}/{p}] error: {e}")
