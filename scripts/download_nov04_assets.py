# -*- coding: utf-8 -*-
import urllib.request
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def download_file(url, out_path):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(out_path, "wb") as f:
                f.write(data)
            print(f"Downloaded {url} -> {out_path} ({len(data):,} bytes)")
            return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")
assets_dir = Path(r"c:\Program Files\1a\src\gitnews\assets\images")

# 1. nanochat
download_file("https://raw.githubusercontent.com/karpathy/nanochat/main/dev/nanochat.png", scratch_dir / "nanochat_logo.png")
download_file("https://raw.githubusercontent.com/karpathy/nanochat/main/dev/scaling_laws_jan26.png", scratch_dir / "nanochat_scaling.png")

# 2. heretic
download_file("https://github.com/user-attachments/assets/df5f2840-2f92-4991-aa57-252747d7182e", scratch_dir / "heretic_logo.png")

# 3. shannon
download_file("https://raw.githubusercontent.com/KeygraphHQ/shannon/main/assets/github-banner-light.png", scratch_dir / "shannon_banner.png")
download_file("https://raw.githubusercontent.com/KeygraphHQ/shannon/main/assets/Shannon3GIF.gif", scratch_dir / "shannon_gif.gif")

# 4. floci
download_file("https://raw.githubusercontent.com/floci-io/floci/main/docs/assets/floci-black.svg", scratch_dir / "floci_logo.svg")

# 5. t3code
# Let's check what assets t3code repo has
