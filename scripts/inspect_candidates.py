import urllib.request
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

candidates = [
    "pbakaus/impeccable",
    "headroomlabs-ai/headroom",
    "tashfeenahmed/freellmapi",
    "anomalyco/opencode",
    "ruvnet/ruflo",
    "Panniantong/Agent-Reach",
    "koala73/worldmonitor"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

for repo in candidates:
    print(f"\n==================== {repo} ====================")
    readme_found = False
    for branch in ["main", "master"]:
        for name in ["README.md", "readme.md", "README.MD"]:
            url = f"https://raw.githubusercontent.com/{repo}/{branch}/{name}"
            try:
                req = urllib.request.Request(url, headers=headers)
                with urllib.request.urlopen(req, timeout=5) as response:
                    content = response.read().decode('utf-8', errors='ignore')
                    print(f"[FOUND README] ({branch}/{name}, {len(content)} chars)")
                    lines = content.split('\n')
                    print('\n'.join(lines[:35]))
                    readme_found = True
                    break
            except Exception:
                pass
        if readme_found:
            break
    if not readme_found:
        print("[README NOT FOUND VIA RAW]")
