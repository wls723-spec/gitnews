import urllib.request
import os
import sys
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}

downloads = [
    ("impeccable_og.png", "https://impeccable.style/og-image-v6.png"),
    ("headroom_hero.png", "https://raw.githubusercontent.com/headroomlabs-ai/headroom/main/headroom-savings.png"),
    ("headroom_dash.png", "https://raw.githubusercontent.com/headroomlabs-ai/headroom/main/dashboard-cache-ttl-main.png"),
    ("freellmapi_hero.png", "https://raw.githubusercontent.com/tashfeenahmed/freellmapi/main/repo-assets/github-hero.png"),
    ("freellmapi_desktop.png", "https://raw.githubusercontent.com/tashfeenahmed/freellmapi/main/repo-assets/desktop.png"),
    ("worldmonitor_map.jpg", "https://raw.githubusercontent.com/koala73/worldmonitor/main/docs/images/worldmonitor-7-mar-2026.jpg"),
    ("worldmonitor_tui.webp", "https://raw.githubusercontent.com/koala73/worldmonitor/main/docs/images/tui/overview.webp"),
]

scratch_dir = r"c:\Program Files\1a\src\gitnews\scratch"
os.makedirs(scratch_dir, exist_ok=True)

for name, url in downloads:
    target = os.path.join(scratch_dir, name)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r, open(target, 'wb') as f:
            f.write(r.read())
        im = Image.open(target)
        print(f"[SUCCESS] {name}: {im.size}, {im.format}, {os.path.getsize(target):,} bytes")
    except Exception as e:
        print(f"[FAIL] {name} ({url}): {e}")
