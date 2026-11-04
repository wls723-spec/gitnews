# -*- coding: utf-8 -*-
import urllib.request
import json
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = r"c:\Program Files\1a\src\gitnews\scratch"
headers = {"User-Agent": "Mozilla/5.0"}

def download_asset(url, filename):
    out = os.path.join(scratch_dir, filename)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp, open(out, "wb") as f:
            f.write(resp.read())
        print(f"[OK] {filename} ({os.path.getsize(out):,} bytes) from {url}")
        return True
    except Exception as e:
        print(f"[FAIL] {filename} from {url}: {e}")
        return False

# 1. Hop screenshot: docs/screenshot.png
download_asset("https://raw.githubusercontent.com/Arjun-Ingole/hop/main/docs/screenshot.png", "hop_screenshot.png")
download_asset("https://raw.githubusercontent.com/Arjun-Ingole/hop/main/assets/brand/hop-lockup-dark.svg", "hop_lockup.svg")

# 2. PixelFX montage: docs/readme/montage.gif or gallery assets
download_asset("https://raw.githubusercontent.com/patch-gg/pixelfx/main/docs/readme/montage.gif", "pixelfx_montage.gif")
download_asset("https://raw.githubusercontent.com/patch-gg/pixelfx/main/docs/readme/hero.png", "pixelfx_hero.png")

# 3. AiSOC logo or screenshots
download_asset("https://raw.githubusercontent.com/beenuar/AiSOC/main/apps/web/public/logo-mark.svg", "aisoc_logo.svg")
# Check if AiSOC has screenshots or docs
download_asset("https://raw.githubusercontent.com/beenuar/AiSOC/main/apps/web/public/og-image.png", "aisoc_og.png")
download_asset("https://raw.githubusercontent.com/beenuar/AiSOC/main/apps/web/public/images/dashboard-preview.png", "aisoc_preview.png")

# 4. iCloud-S3 demo gif
download_asset("https://raw.githubusercontent.com/ashayas/icloud-s3/main/demo/icloud-s3-demo.gif", "icloud_s3_demo.gif")

# 5. DeepSeek SuperAgent
download_asset("https://raw.githubusercontent.com/deepseek-ai/dsh-superagent-prototype/main/docs/images/architecture.png", "dsh_arch.png")
download_asset("https://raw.githubusercontent.com/deepseek-ai/dsh-superagent-prototype/main/docs/images/web-panel.png", "dsh_panel.png")
download_asset("https://raw.githubusercontent.com/deepseek-ai/dsh-superagent-prototype/main/docs/overview.png", "dsh_overview.png")
