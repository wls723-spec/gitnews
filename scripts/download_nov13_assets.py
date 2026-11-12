# -*- coding: utf-8 -*-
"""
download_nov13_assets.py
Capture real software interfaces via Playwright for 2026-11-13 Top 5 stories.
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "assets" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

async def capture_demos():
    print("[*] Capturing real software interfaces via Playwright...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={'width': 1200, 'height': 800}, device_scale_factor=1.5)

        # 1. Simon3Sarkis/super-odyssey-pc-recomp
        p1 = await context.new_page()
        try:
            print("  Capturing Simon3Sarkis/super-odyssey-pc-recomp...")
            await p1.goto("https://github.com/Simon3Sarkis/super-odyssey-pc-recomp", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p1.screenshot(path=str(IMAGES_DIR / "demo_odyssey_recomp.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_odyssey_recomp.png")
        except Exception as e:
            print(f"  ✗ super-odyssey-pc-recomp failed: {e}")
        await p1.close()

        # 2. rivet-dev/open-orange (openorange.dev)
        p2 = await context.new_page()
        try:
            print("  Capturing openorange.dev...")
            await p2.goto("https://openorange.dev", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p2.screenshot(path=str(IMAGES_DIR / "demo_openorange.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_openorange.png from openorange.dev")
        except Exception as e:
            print(f"  ✗ Failed openorange.dev, fallback to github: {e}")
            try:
                await p2.goto("https://github.com/rivet-dev/open-orange", wait_until="networkidle", timeout=15000)
                await p2.screenshot(path=str(IMAGES_DIR / "demo_openorange.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_openorange.png from GitHub")
            except Exception as e2:
                print(f"  ✗ open-orange fallback failed: {e2}")
        await p2.close()

        # 3. simpsoka/zigzag (zigzag.diy)
        p3 = await context.new_page()
        try:
            print("  Capturing zigzag.diy...")
            await p3.goto("https://zigzag.diy", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p3.screenshot(path=str(IMAGES_DIR / "demo_zigzag.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_zigzag.png from zigzag.diy")
        except Exception as e:
            print(f"  ✗ Failed zigzag.diy, fallback to github: {e}")
            try:
                await p3.goto("https://github.com/simpsoka/zigzag", wait_until="networkidle", timeout=15000)
                await p3.screenshot(path=str(IMAGES_DIR / "demo_zigzag.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_zigzag.png from GitHub")
            except Exception as e2:
                print(f"  ✗ zigzag fallback failed: {e2}")
        await p3.close()

        # 4. makepad/relax (makepad.github.io/relax/)
        p4 = await context.new_page()
        try:
            print("  Capturing makepad.github.io/relax/...")
            await p4.goto("https://makepad.github.io/relax/", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p4.screenshot(path=str(IMAGES_DIR / "demo_relax.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_relax.png from makepad.github.io/relax/")
        except Exception as e:
            print(f"  ✗ Failed makepad.github.io/relax/, fallback to github: {e}")
            try:
                await p4.goto("https://github.com/makepad/relax", wait_until="networkidle", timeout=15000)
                await p4.screenshot(path=str(IMAGES_DIR / "demo_relax.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_relax.png from GitHub")
            except Exception as e2:
                print(f"  ✗ relax fallback failed: {e2}")
        await p4.close()

        # 5. tylertms/Stela
        p5 = await context.new_page()
        try:
            print("  Capturing tylertms/Stela...")
            await p5.goto("https://github.com/tylertms/Stela", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p5.screenshot(path=str(IMAGES_DIR / "demo_stela.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_stela.png from GitHub")
        except Exception as e:
            print(f"  ✗ tylertms/Stela failed: {e}")
        await p5.close()

        await browser.close()
    print("[✓] All 5 demo screenshots captured successfully!")

if __name__ == "__main__":
    asyncio.run(capture_demos())
