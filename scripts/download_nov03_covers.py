# -*- coding: utf-8 -*-
import urllib.request
import os
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

assets_dir = Path(r"c:\Program Files\1a\src\gitnews\assets\images")
assets_dir.mkdir(parents=True, exist_ok=True)

urls_to_download = [
    ("https://agent-browser.dev/desktop/og", "agent_desktop_og.png"),
    ("https://anoma.ly/hex/og.png?v=5", "hex_og.png"),
    ("https://opengraph.githubassets.com/e8712333d7aa0ff1ae69cf9b7b39e068742ffc572f6416e315ed38d7265ecb68/Donchitos/Claude-Code-Game-Studios", "game_studios_og.png"),
    ("https://opengraph.githubassets.com/39a60c04bf6cefd449f13c6bc4842b0df3c2854da0a9f5cbb66847c2e379435f/vercel-labs/agent-desktop", "agent_desktop_gh.png"),
    ("https://opengraph.githubassets.com/a42b9319d670d9a6ca260840ff702008cf2ea37a070eb37470656858e390d402/anomalyco/hex", "hex_gh.png"),
    ("https://opengraph.githubassets.com/e5ad081f26a1ca459fb7cf4a712f2c9748b64b18ad8557e4e84b80b06fe3f4f1/calesthio/OpenMontage", "openmontage_gh.png")
]

for url, filename in urls_to_download:
    dest = assets_dir / filename
    print(f"Downloading {url} -> {filename}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            with open(dest, "wb") as f:
                f.write(content)
            print(f"  Saved {filename} ({len(content):,} bytes)")
    except Exception as e:
        print(f"  Failed: {e}")
