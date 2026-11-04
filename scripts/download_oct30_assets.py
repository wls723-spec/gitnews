import urllib.request
import subprocess
import json
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = r"c:\Program Files\1a\src\gitnews\scratch"
os.makedirs(scratch_dir, exist_ok=True)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def download_file(url, out_name):
    out = os.path.join(scratch_dir, out_name)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp, open(out, "wb") as f:
            f.write(resp.read())
        print(f"[OK] Downloaded {out_name}: {os.path.getsize(out):,} bytes")
        return True
    except Exception as e:
        print(f"[FAIL] {out_name} from {url}: {e}")
        return False

# 1. Concat Editor
download_file("https://raw.githubusercontent.com/jub0t/Concat/main/assets/editor-dark.png", "concat_editor_dark.png")
download_file("https://raw.githubusercontent.com/jub0t/Concat/main/assets/editor.png", "concat_editor.png")

# 2. Hindsight assets
download_file("https://raw.githubusercontent.com/vectorize-io/hindsight/main/hindsight-docs/static/img/hindsight-overview.webp", "hindsight_overview.webp")
download_file("https://raw.githubusercontent.com/vectorize-io/hindsight/main/hindsight-docs/static/img/hindsight-benchmarks.png", "hindsight_benchmarks.png")

# 3. Superpowers assets
download_file("https://raw.githubusercontent.com/obra/superpowers/main/assets/superpowers-small.svg", "superpowers_small.svg")
