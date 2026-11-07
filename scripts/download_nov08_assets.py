# -*- coding: utf-8 -*-
import asyncio
import base64
import json
import os
import re
import subprocess
import urllib.request
from pathlib import Path
from playwright.async_api import async_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "assets" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

repos = [
    ("milind-soni/OpenMausBot", "openmausbot", "https://www.openmausbot.com/"),
    ("mitchellh/ghostty", "ghostty", "https://ghostty.org"),
    ("Th0rgal/satmux", "satmux", "https://github.com/Th0rgal/satmux"),
    ("voyager-so/vork", "vork", "https://voyager.so/vork"),
    ("cjpais/Handy", "handy", "https://handy.computer"),
]

def download_og_banners():
    print("[*] Downloading OpenGraph banners for 5 main stories...")
    for rname, slug, _ in repos:
        og_url = f"https://opengraph.githubassets.com/1/{rname}"
        dest = IMAGES_DIR / f"thumb_{slug}.jpg"
        try:
            req = urllib.request.Request(og_url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp, open(dest, "wb") as f:
                f.write(resp.read())
            print(f"  ✓ Saved OG banner: {dest.name} ({os.path.getsize(dest):,} bytes)")
        except Exception as e:
            print(f"  ✗ Failed OG for {rname}: {e}")

async def capture_demos():
    print("[*] Capturing real software interfaces via Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1200, 'height': 800}, device_scale_factor=1.5)

        # 1. OpenMausBot (https://www.openmausbot.com/)
        p1 = await context.new_page()
        try:
            print("  Capturing openmausbot.com...")
            await p1.goto("https://www.openmausbot.com/", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p1.screenshot(path=str(IMAGES_DIR / "demo_openmausbot.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_openmausbot.png")
        except Exception as e:
            print(f"  ✗ Failed OpenMausBot: {e}")
            # fallback to repo readme
            try:
                await p1.goto("https://github.com/milind-soni/OpenMausBot", wait_until="networkidle", timeout=15000)
                await p1.screenshot(path=str(IMAGES_DIR / "demo_openmausbot.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_openmausbot.png from GitHub")
            except Exception as e2:
                print(f"  ✗ Fallback failed: {e2}")
        await p1.close()

        # 2. Ghostty / Libghostty (https://ghostty.org or https://mitchellh.com/writing/libghostty-1-0)
        p2 = await context.new_page()
        try:
            print("  Capturing ghostty.org...")
            await p2.goto("https://ghostty.org", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p2.screenshot(path=str(IMAGES_DIR / "demo_ghostty.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_ghostty.png")
        except Exception as e:
            print(f"  ✗ Failed ghostty: {e}")
        await p2.close()

        # 3. satmux (https://github.com/Th0rgal/satmux)
        p3 = await context.new_page()
        try:
            print("  Capturing Th0rgal/satmux README...")
            await p3.goto("https://github.com/Th0rgal/satmux", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            readme = p3.locator("article.markdown-body")
            if await readme.count() > 0:
                await readme.screenshot(path=str(IMAGES_DIR / "demo_satmux.png"), clip={'x': 0, 'y': 0, 'width': 1000, 'height': 650})
            else:
                await p3.screenshot(path=str(IMAGES_DIR / "demo_satmux.png"), clip={'x': 0, 'y': 200, 'width': 1200, 'height': 700})
            print("  ✓ Saved demo_satmux.png")
        except Exception as e:
            print(f"  ✗ Failed satmux: {e}")
        await p3.close()

        # 4. vork (https://voyager.so/vork or https://github.com/voyager-so/vork)
        p4 = await context.new_page()
        try:
            print("  Capturing voyager.so/vork...")
            await p4.goto("https://voyager.so/vork", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p4.screenshot(path=str(IMAGES_DIR / "demo_vork.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_vork.png")
        except Exception as e:
            print(f"  ✗ Failed vork web: {e}")
            try:
                await p4.goto("https://github.com/voyager-so/vork", wait_until="networkidle", timeout=15000)
                await p4.screenshot(path=str(IMAGES_DIR / "demo_vork.png"), clip={'x': 0, 'y': 200, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_vork.png from GitHub")
            except Exception as e2:
                print(f"  ✗ vork fallback failed: {e2}")
        await p4.close()

        # 5. Handy (https://handy.computer or https://github.com/cjpais/Handy)
        p5 = await context.new_page()
        try:
            print("  Capturing handy.computer...")
            await p5.goto("https://handy.computer", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p5.screenshot(path=str(IMAGES_DIR / "demo_handy.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_handy.png")
        except Exception as e:
            print(f"  ✗ Failed Handy web: {e}")
            try:
                await p5.goto("https://github.com/cjpais/Handy", wait_until="networkidle", timeout=15000)
                await p5.screenshot(path=str(IMAGES_DIR / "demo_handy.png"), clip={'x': 0, 'y': 200, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_handy.png from GitHub")
            except Exception as e2:
                print(f"  ✗ Handy fallback failed: {e2}")
        await p5.close()

        await browser.close()
    print("[✓] Real demo capture complete.")

if __name__ == "__main__":
    download_og_banners()
    asyncio.run(capture_demos())
