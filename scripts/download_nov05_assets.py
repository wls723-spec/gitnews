import urllib.request
import json
import re
import os
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "assets" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

repos = [
    ("NVIDIA/auto-ontology", "auto_ontology"),
    ("D4Vinci/Scrapling", "scrapling"),
    ("max-sixty/worktrunk", "worktrunk"),
    ("FareedKhan-dev/kimi-k3-in-c", "kimi_k3"),
    ("crmne/zapfast", "zapfast"),
]

print("[*] Inspecting repos and downloading assets...")

for rname, slug in repos:
    cmd = ["gh", "api", f"repos/{rname}"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        repo_data = json.loads(res.stdout)
        owner = repo_data["owner"]["login"]
        repo = repo_data["name"]
        
        # Download GitHub OpenGraph image
        og_url = f"https://opengraph.githubassets.com/1/{rname}"
        og_dest = IMAGES_DIR / f"thumb_{slug}.jpg"
        try:
            req = urllib.request.Request(og_url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp, open(og_dest, "wb") as f:
                f.write(resp.read())
            print(f"  ✓ Saved OG banner: {og_dest.name} ({os.path.getsize(og_dest):,} bytes)")
        except Exception as e:
            print(f"  ✗ Failed OG for {rname}: {e}")

    # Also inspect readme for demo images
    res_readme = subprocess.run(["gh", "api", f"repos/{rname}/readme"], capture_output=True, text=True)
    if res_readme.returncode == 0:
        import base64
        readme_json = json.loads(res_readme.stdout)
        content_b64 = readme_json.get("content", "")
        if content_b64:
            readme_text = base64.b64decode(content_b64).decode("utf-8", errors="ignore")
            # Find URLs
            urls = re.findall(r'https?://[^\s\)\"\'>]+\.(?:png|jpg|jpeg|webp|gif)', readme_text)
            demo_saved = False
            for u in urls:
                if any(k in u.lower() for k in ["demo", "architecture", "overview", "screenshot", "assets", "img", "image"]):
                    demo_dest = IMAGES_DIR / f"demo_{slug}.png"
                    try:
                        req = urllib.request.Request(u, headers=headers)
                        with urllib.request.urlopen(req, timeout=10) as resp, open(demo_dest, "wb") as f:
                            f.write(resp.read())
                        print(f"  ✓ Saved demo image from {u}: {demo_dest.name} ({os.path.getsize(demo_dest):,} bytes)")
                        demo_saved = True
                        break
                    except Exception as e:
                        print(f"  ✗ Failed to download {u}: {e}")
            if not demo_saved:
                print(f"  ℹ No direct demo image found in readme for {rname}, using thumb copy")
                demo_dest = IMAGES_DIR / f"demo_{slug}.jpg"
                if og_dest.exists() and not demo_dest.exists():
                    import shutil
                    shutil.copy(og_dest, demo_dest)

print("[✓] Asset preparation complete.")
