# -*- coding: utf-8 -*-
import urllib.request
import json
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def check_tree(repo):
    url = f"https://api.github.com/repos/{repo}/git/trees/main?recursive=1"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            images = [t['path'] for t in data.get('tree', []) if any(t['path'].lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.svg', '.webp', '.gif'])]
            print(f"=== {repo} Images ({len(images)}) ===")
            for img in images[:15]:
                print(f"  {img}")
    except Exception as e:
        print(f"Error {repo}: {e}")

check_tree("pingdotgg/t3code")
check_tree("p-e-w/heretic")
check_tree("floci-io/floci")
