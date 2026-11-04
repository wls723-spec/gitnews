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
    # Colibri assets
    ("https://raw.githubusercontent.com/JustVugg/colibri/main/docs/media/ui/ui-monitor.png", "colibri_monitor.png"),
    ("https://raw.githubusercontent.com/JustVugg/colibri/main/docs/media/ui/ui-chat.png", "colibri_chat.png"),
    ("https://raw.githubusercontent.com/JustVugg/colibri/main/docs/media/sparse.png", "colibri_sparse.png"),
    
    # OpenMontage assets
    ("https://raw.githubusercontent.com/calesthio/OpenMontage/main/docs/images/backlot/board-live.png", "openmontage_board.png"),
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
