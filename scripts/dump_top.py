import sys
import json
import urllib.request

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

repos = [
    "oosexgang/hackios-xnu-kernel",
    "NVIDIA/OpenShell",
    "genspark-ai/genoffice",
    "anthropics/knowledge-work-plugins",
    "twentyhq/twenty",
    "shiyu-coder/Kronos",
    "trycua/cua",
    "max-sixty/worktrunk"
]

headers = {"User-Agent": "Mozilla/5.0"}

for r in repos:
    print(f"\n##################################################")
    print(f"REPO: {r}")
    print(f"##################################################")
    # API
    try:
        req = urllib.request.Request(f"https://api.github.com/repos/{r}", headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"Stars: {data.get('stargazers_count')} | Forks: {data.get('forks_count')} | Created: {data.get('created_at')} | Updated: {data.get('updated_at')}")
            print(f"Desc: {data.get('description')}")
            print(f"Homepage: {data.get('homepage')}")
            branch = data.get('default_branch', 'main')
    except Exception as e:
        print(f"API Error: {e}")
        branch = 'main'

    for b in [branch, 'master', 'main']:
        found = False
        for name in ['README.md', 'readme.md']:
            try:
                raw_url = f"https://raw.githubusercontent.com/{r}/{b}/{name}"
                req = urllib.request.Request(raw_url, headers=headers)
                with urllib.request.urlopen(req, timeout=5) as resp:
                    txt = resp.read().decode('utf-8', errors='ignore')
                    print(f"--- README ({b}/{name}, {len(txt)} chars) ---")
                    lines = [ln.strip() for ln in txt.split('\n') if ln.strip()]
                    for ln in lines[:30]:
                        print("  ", ln[:120])
                    found = True
                    break
            except Exception:
                pass
        if found:
            break
