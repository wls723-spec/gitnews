# -*- coding: utf-8 -*-
import urllib.request
import json
import sys
import re
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

candidates = [
    ("karpathy/nanochat", "nanochat"),
    ("p-e-w/heretic", "heretic"),
    ("floci-io/floci", "floci"),
    ("FlashML-org/FreeToken", "freetoken"),
    ("pingdotgg/t3code", "t3code"),
    ("KeygraphHQ/shannon", "shannon"),
    ("cjpais/Handy", "handy"),
    ("Crosstalk-Solutions/project-nomad", "project-nomad")
]

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")

for repo, tag in candidates:
    print(f"\n==================== {repo} ====================")
    url = f"https://api.github.com/repos/{repo}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"Stars: {data.get('stargazers_count')} | Forks: {data.get('forks_count')} | License: {data.get('license', {}).get('name') if data.get('license') else 'None'}")
            print(f"Description: {data.get('description')}")
            print(f"Homepage: {data.get('homepage')}")
    except Exception as e:
        print(f"API error: {e}")

    # Fetch full README
    readme_urls = [
        f"https://raw.githubusercontent.com/{repo}/main/README.md",
        f"https://raw.githubusercontent.com/{repo}/master/README.md"
    ]
    readme_text = ""
    for r_url in readme_urls:
        try:
            req2 = urllib.request.Request(r_url, headers=headers)
            with urllib.request.urlopen(req2, timeout=10) as resp2:
                readme_text = resp2.read().decode('utf-8', errors='ignore')
                break
        except Exception:
            continue
    
    if readme_text:
        images = re.findall(r'!\[.*?\]\((.*?)\)', readme_text)
        img_tags = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', readme_text)
        all_imgs = images + img_tags
        print(f"README len: {len(readme_text):,} chars | Found images ({len(all_imgs)}):")
        for img in all_imgs[:6]:
            print(f"  - {img}")
        
        with open(scratch_dir / f"readme_{tag}.md", "w", encoding="utf-8") as rf:
            rf.write(readme_text)
        print(f"First 5 lines:")
        for line in readme_text.splitlines()[:5]:
            print(f"  > {line}")
