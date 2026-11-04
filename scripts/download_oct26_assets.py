import urllib.request
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = r"c:\Program Files\1a\src\gitnews\scratch"
os.makedirs(scratch_dir, exist_ok=True)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

downloads = [
    ("https://raw.githubusercontent.com/experientiallabs/experiential/main/assets/experiential-workflow.png", "experiential_workflow.png"),
    ("https://raw.githubusercontent.com/browser-use/video-use/main/static/video-use-banner.png", "video_use_banner.png"),
]

for url, fname in downloads:
    out = os.path.join(scratch_dir, fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp, open(out, "wb") as f:
            f.write(resp.read())
        print(f"Downloaded {fname}: {os.path.getsize(out):,} bytes")
    except Exception as e:
        print(f"Failed {fname}: {e}")

# Check what images exist in thedotmack/claude-mem repo via GitHub API
api_url = "https://api.github.com/repos/thedotmack/claude-mem/contents/docs/public"
try:
    req = urllib.request.Request(api_url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        files = json.loads(resp.read().decode('utf-8'))
        print("claude-mem docs/public files:", [f['name'] for f in files if isinstance(files, list)])
except Exception as e:
    print(f"claude-mem docs check: {e}")

# Check garrytan/gstack repo files
api_url = "https://api.github.com/repos/garrytan/gstack/contents"
try:
    req = urllib.request.Request(api_url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        files = json.loads(resp.read().decode('utf-8'))
        print("garrytan/gstack root files:", [f['name'] for f in files if isinstance(files, list)])
except Exception as e:
    print(f"gstack check: {e}")
