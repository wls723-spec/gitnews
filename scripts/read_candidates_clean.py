# -*- coding: utf-8 -*-
import urllib.request
import json
import base64
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

headers = {"User-Agent": "Mozilla/5.0"}

def print_readme(repo):
    url = f"https://api.github.com/repos/{repo}/readme"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            content = base64.b64decode(data['content']).decode('utf-8', errors='ignore')
            print(f"==================================================")
            print(f"REPO: {repo}")
            print(f"==================================================")
            print(content[:1500])
    except Exception as e:
        print(f"Error {repo}: {e}")

print_readme("affaan-m/ECC")
print_readme("beenuar/AiSOC")
print_readme("patch-gg/pixelfx")
print_readme("anomalyco/hex")
