# -*- coding: utf-8 -*-
import asyncio
import os
import urllib.request
from pathlib import Path
from playwright.async_api import async_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "assets" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

async def capture_demos():
    print("[*] Capturing real software interfaces via Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1200, 'height': 800}, device_scale_factor=1.5)

        # 1. astryx (https://astryx.atmeta.com or GitHub)
        p1 = await context.new_page()
        try:
            print("  Capturing meta/astryx...")
            await p1.goto("https://astryx.atmeta.com", wait_until="networkidle", timeout=12000)
            await asyncio.sleep(1.0)
            await p1.screenshot(path=str(IMAGES_DIR / "demo_astryx.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_astryx.png from astryx.atmeta.com")
        except Exception as e:
            print(f"  ✗ Failed astryx.atmeta.com, trying github: {e}")
            try:
                await p1.goto("https://github.com/meta/astryx", wait_until="networkidle", timeout=15000)
                await asyncio.sleep(1.0)
                readme = p1.locator("article.markdown-body")
                if await readme.count() > 0:
                    await readme.screenshot(path=str(IMAGES_DIR / "demo_astryx.png"), clip={'x': 0, 'y': 0, 'width': 1000, 'height': 650})
                else:
                    await p1.screenshot(path=str(IMAGES_DIR / "demo_astryx.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_astryx.png from GitHub")
            except Exception as e2:
                print(f"  ✗ astryx fallback failed: {e2}")
        await p1.close()

        # 2. ketchup (https://benchup3d.github.io/editor/ or GitHub)
        p2 = await context.new_page()
        try:
            print("  Capturing BenchUp3D / KetchUp...")
            await p2.goto("https://benchup3d.github.io/editor/", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(2.0)
            await p2.screenshot(path=str(IMAGES_DIR / "demo_ketchup.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_ketchup.png from BenchUp3D Web App")
        except Exception as e:
            print(f"  ✗ Failed benchup3d app, trying github: {e}")
            try:
                await p2.goto("https://github.com/BenchUp3D/editor", wait_until="networkidle", timeout=15000)
                await p2.screenshot(path=str(IMAGES_DIR / "demo_ketchup.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_ketchup.png from GitHub")
            except Exception as e2:
                print(f"  ✗ ketchup fallback failed: {e2}")
        await p2.close()

        # 3. superplane (https://app.superplane.com or https://superplane.com)
        p3 = await context.new_page()
        try:
            print("  Capturing superplane...")
            await p3.goto("https://superplane.com", wait_until="networkidle", timeout=12000)
            await asyncio.sleep(1.0)
            await p3.screenshot(path=str(IMAGES_DIR / "demo_superplane.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_superplane.png from superplane.com")
        except Exception as e:
            print(f"  ✗ Failed superplane.com, trying github: {e}")
            try:
                await p3.goto("https://github.com/superplanehq/superplane", wait_until="networkidle", timeout=15000)
                await p3.screenshot(path=str(IMAGES_DIR / "demo_superplane.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_superplane.png from GitHub")
            except Exception as e2:
                print(f"  ✗ superplane fallback failed: {e2}")
        await p3.close()

        # 4. voxcpm (https://openbmb.github.io/voxcpm2-demopage/ or GitHub)
        p4 = await context.new_page()
        try:
            print("  Capturing VoxCPM2...")
            await p4.goto("https://openbmb.github.io/voxcpm2-demopage/", wait_until="networkidle", timeout=12000)
            await asyncio.sleep(1.5)
            await p4.screenshot(path=str(IMAGES_DIR / "demo_voxcpm.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_voxcpm.png from demopage")
        except Exception as e:
            print(f"  ✗ Failed demopage, trying github: {e}")
            try:
                await p4.goto("https://github.com/OpenBMB/VoxCPM", wait_until="networkidle", timeout=15000)
                await p4.screenshot(path=str(IMAGES_DIR / "demo_voxcpm.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_voxcpm.png from GitHub")
            except Exception as e2:
                print(f"  ✗ voxcpm fallback failed: {e2}")
        await p4.close()

        # 5. gestaltx (https://github.com/huamidev/GestaltX)
        p5 = await context.new_page()
        try:
            print("  Capturing huamidev/GestaltX...")
            await p5.goto("https://github.com/huamidev/GestaltX", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            readme = p5.locator("article.markdown-body")
            if await readme.count() > 0:
                await readme.screenshot(path=str(IMAGES_DIR / "demo_gestaltx.png"), clip={'x': 0, 'y': 0, 'width': 1000, 'height': 680})
            else:
                await p5.screenshot(path=str(IMAGES_DIR / "demo_gestaltx.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_gestaltx.png from GitHub")
        except Exception as e:
            print(f"  ✗ gestaltx failed: {e}")
        await p5.close()

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_demos())
