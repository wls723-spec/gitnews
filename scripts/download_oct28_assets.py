import urllib.request
import os
import sys
import json

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = r"c:\Program Files\1a\src\gitnews\scratch"
os.makedirs(scratch_dir, exist_ok=True)
headers = {"User-Agent": "Mozilla/5.0"}

def download_file(url, out_name):
    out = os.path.join(scratch_dir, out_name)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp, open(out, "wb") as f:
            f.write(resp.read())
        print(f"[OK] Downloaded {out_name}: {os.path.getsize(out):,} bytes")
        return True
    except Exception as e:
        print(f"[FAIL] {out_name} from {url}: {e}")
        return False

# 1. Hallmark images
download_file("https://raw.githubusercontent.com/Nutlope/hallmark/main/site/OG-hallmark.png", "hallmark_og.png")
download_file("https://raw.githubusercontent.com/Nutlope/hallmark/main/docs/screenshots/dusk.jpg", "hallmark_dusk.jpg")
download_file("https://raw.githubusercontent.com/Nutlope/hallmark/main/docs/screenshots/cobalt.jpg", "hallmark_cobalt.jpg")

# 2. ThinkRail images
download_file("https://raw.githubusercontent.com/JetBrains/thinkrail/main/.github/readme-assets/workbench-dark.png", "thinkrail_workbench_dark.png")
download_file("https://raw.githubusercontent.com/JetBrains/thinkrail/main/.github/readme-assets/workbench-light.png", "thinkrail_workbench_light.png")

# 3. Check contents of TradingAgents, SkillSpector, DeepTutor
for repo, sub in [
    ("TauricResearch/TradingAgents", ""),
    ("TauricResearch/TradingAgents", "tradingagents/assets"),
    ("NVIDIA/SkillSpector", "docs"),
    ("NVIDIA/SkillSpector", "assets"),
    ("HKUDS/DeepTutor", "assets/figs"),
]:
    api_url = f"https://api.github.com/repos/{repo}/contents/{sub}".rstrip('/')
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            files = json.loads(resp.read().decode('utf-8'))
            if isinstance(files, list):
                print(f"Contents of {repo}/{sub}:", [f['name'] for f in files])
    except Exception as e:
        print(f"Error checking {repo}/{sub}: {e}")
