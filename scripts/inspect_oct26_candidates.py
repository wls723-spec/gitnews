import urllib.request
import json
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

candidates = [
    "experientiallabs/experiential",
    "anthropics/sandbox-runtime",
    "garrytan/gstack",
    "thedotmack/claude-mem",
    "ZSeven-W/openpencil",
    "google-gemini/gemini-cli",
    "SnailSploit/Claude-Red",
    "browser-use/video-use"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

for repo in candidates:
    print(f"\n{'='*20} {repo} {'='*20}")
    # Check GitHub API
    api_url = f"https://api.github.com/repos/{repo}"
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"Stars: {data.get('stargazers_count')} | Forks: {data.get('forks_count')} | License: {data.get('license', {}).get('spdx_id') if data.get('license') else 'None'}")
            print(f"Desc: {data.get('description')}")
            print(f"Homepage: {data.get('homepage')}")
    except Exception as e:
        print(f"API Error: {e}")

    # Check README
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
                    print('\n'.join(lines[:40]))
                    readme_found = True
                    break
            except Exception:
                pass
        if readme_found:
            break
