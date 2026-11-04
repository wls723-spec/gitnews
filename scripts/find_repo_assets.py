import subprocess
import json
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

repos = [
    "valentderah/totk-pc-recomp",
    "vectorize-io/hindsight",
    "nightly-labs/openbot",
    "obra/superpowers",
    "jub0t/Concat"
]

for r in repos:
    print(f"\n=== Assets for {r} ===")
    res = subprocess.run(["gh", "api", f"repos/{r}/contents"], capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        items = json.loads(res.stdout)
        print([it['name'] for it in items])
        # Check subdirectories like docs, assets, img
        for sub in ["assets", "docs", "img", "images", "media"]:
            if any(it['name'] == sub for it in items):
                sub_res = subprocess.run(["gh", "api", f"repos/{r}/contents/{sub}"], capture_output=True, text=True, encoding="utf-8")
                if sub_res.returncode == 0:
                    sub_items = json.loads(sub_res.stdout)
                    print(f"  /{sub}:", [s['name'] for s in sub_items])
