# -*- coding: utf-8 -*-
import urllib.request
import json
import sys
import re
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

repos = [
    ("vercel-labs/agent-desktop", "agent-desktop"),
    ("Donchitos/Claude-Code-Game-Studios", "game-studios"),
    ("JustVugg/colibri", "colibri"),
    ("anomalyco/hex", "hex"),
    ("calesthio/OpenMontage", "openmontage")
]

for repo, tag in repos:
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
        except:
            continue
    
    if readme_text:
        # Find images in readme
        images = re.findall(r'!\[.*?\]\((.*?)\)', readme_text)
        img_tags = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', readme_text)
        all_imgs = images + img_tags
        print(f"Found images ({len(all_imgs)}):")
        for img in all_imgs[:8]:
            print(f"  - {img}")
        
        # Save readme to scratch for deep reading
        scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")
        with open(scratch_dir / f"readme_{tag}.md", "w", encoding="utf-8") as rf:
            rf.write(readme_text)
        print(f"Saved full README to scratch/readme_{tag}.md ({len(readme_text):,} chars)")
