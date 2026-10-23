import urllib.request
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = r"c:\Program Files\1a\src\gitnews\scratch"
os.makedirs(scratch_dir, exist_ok=True)
headers = {"User-Agent": "Mozilla/5.0"}

# Test downloading hackios images
hackios_imgs = ["lockscreen.jpg", "homescreen.jpg", "control-center.jpg", "settings.jpg"]
for img in hackios_imgs:
    url = f"https://raw.githubusercontent.com/oosexgang/hackios-xnu-kernel/main/docs/{img}"
    out = os.path.join(scratch_dir, f"hackios_{img}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp, open(out, "wb") as f:
            f.write(resp.read())
        print(f"Downloaded {img}: {os.path.getsize(out):,} bytes")
    except Exception as e:
        print(f"Failed {img}: {e}")

# Check genoffice hero image
genoffice_url = "https://raw.githubusercontent.com/genspark-ai/genoffice/main/docs/assets/readme/hero.webp"
try:
    req = urllib.request.Request(genoffice_url, headers=headers)
    out = os.path.join(scratch_dir, "genoffice_hero.webp")
    with urllib.request.urlopen(req, timeout=10) as resp, open(out, "wb") as f:
        f.write(resp.read())
    print(f"Downloaded genoffice_hero: {os.path.getsize(out):,} bytes")
except Exception as e:
    print(f"Failed genoffice_hero: {e}")

# Check openshell banner
openshell_url = "https://raw.githubusercontent.com/NVIDIA/OpenShell/main/docs/brand/assets/openshell-banner-dark.png"
try:
    req = urllib.request.Request(openshell_url, headers=headers)
    out = os.path.join(scratch_dir, "openshell_banner.png")
    with urllib.request.urlopen(req, timeout=10) as resp, open(out, "wb") as f:
        f.write(resp.read())
    print(f"Downloaded openshell_banner: {os.path.getsize(out):,} bytes")
except Exception as e:
    print(f"Failed openshell_banner: {e}")

# Check trycua images
trycua_url = "https://raw.githubusercontent.com/trycua/cua/main/img/card-cua-spaces-wide.webp"
try:
    req = urllib.request.Request(trycua_url, headers=headers)
    out = os.path.join(scratch_dir, "cua_spaces.webp")
    with urllib.request.urlopen(req, timeout=10) as resp, open(out, "wb") as f:
        f.write(resp.read())
    print(f"Downloaded cua_spaces: {os.path.getsize(out):,} bytes")
except Exception as e:
    print(f"Failed cua_spaces: {e}")
