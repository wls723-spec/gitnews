# -*- coding: utf-8 -*-
import urllib.request
import json
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

repos = [
    "vercel-labs/agent-desktop",
    "Donchitos/Claude-Code-Game-Studios",
    "anomalyco/hex",
    "calesthio/OpenMontage",
    "JustVugg/colibri"
]

for r in repos:
    readme_url = f"https://raw.githubusercontent.com/{r}/main/README.md"
    print(f"\n==================== {r} ====================")
    try:
        req2 = urllib.request.Request(readme_url, headers=headers)
        with urllib.request.urlopen(req2, timeout=10) as resp2:
            readme = resp2.read().decode('utf-8', errors='ignore')
            lines = [line for line in readme.split('\n') if line.strip()][:30]
            print('\n'.join(lines))
    except Exception as e:
        try:
            req3 = urllib.request.Request(f"https://raw.githubusercontent.com/{r}/master/README.md", headers=headers)
            with urllib.request.urlopen(req3, timeout=10) as resp3:
                readme = resp3.read().decode('utf-8', errors='ignore')
                lines = [line for line in readme.split('\n') if line.strip()][:30]
                print('\n'.join(lines))
        except Exception as e2:
            print(f"Error fetching readme: {e2}")
