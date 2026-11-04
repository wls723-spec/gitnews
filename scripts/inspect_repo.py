import urllib.request
import json
import base64
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

repo = sys.argv[1] if len(sys.argv) > 1 else "TauricResearch/TradingAgents"
headers = {"User-Agent": "Mozilla/5.0"}

# 1. Repo info
try:
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers=headers)
    with urllib.request.urlopen(req) as resp:
        info = json.loads(resp.read().decode('utf-8'))
        print(f"=== {info.get('full_name')} ===")
        print(f"Description: {info.get('description')}")
        print(f"Stars: {info.get('stargazers_count')} | Forks: {info.get('forks_count')}")
        print(f"Homepage: {info.get('homepage')}")
        print(f"Topics: {info.get('topics')}")
except Exception as e:
    print(f"Error fetching repo info: {e}")

# 2. Readme
try:
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}/readme", headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        content = base64.b64decode(data['content']).decode('utf-8')
        print("\n=== README (first 3500 chars) ===")
        print(content[:3500])
except Exception as e:
    print(f"Error fetching readme: {e}")
