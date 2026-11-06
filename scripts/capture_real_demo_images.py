#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "assets" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

async def capture_all():
    print("[*] Launching Chromium to capture real software interfaces...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # 1. voxl: Tembo voxl repository page / quick start section
        context = await browser.new_context(viewport={'width': 1200, 'height': 800}, device_scale_factor=1.5)
        page = await context.new_page()
        try:
            print("  Capturing tembo/voxl...")
            await page.goto("https://github.com/tembo/voxl", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            # Find the readme section
            readme = page.locator("article.markdown-body")
            if await readme.count() > 0:
                await readme.screenshot(path=str(IMAGES_DIR / "demo_voxl.png"), clip={'x': 0, 'y': 0, 'width': 1000, 'height': 650})
            else:
                await page.screenshot(path=str(IMAGES_DIR / "demo_voxl.png"), clip={'x': 0, 'y': 200, 'width': 1200, 'height': 700})
            print("  ✓ Saved demo_voxl.png")
        except Exception as e:
            print(f"  ✗ Failed voxl: {e}")
        await page.close()

        # 2. VibeVoice: https://microsoft.github.io/VibeVoice
        page = await context.new_page()
        try:
            print("  Capturing microsoft/VibeVoice...")
            await page.goto("https://microsoft.github.io/VibeVoice", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.5)
            await page.screenshot(path=str(IMAGES_DIR / "demo_vibevoice.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_vibevoice.png")
        except Exception as e:
            print(f"  ✗ Failed VibeVoice: {e}")
        await page.close()

        # 3. GPUI Kit: https://gpui-kit.com
        page = await context.new_page()
        try:
            print("  Capturing longbridge/gpui-kit...")
            await page.goto("https://gpui-kit.com", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.5)
            await page.screenshot(path=str(IMAGES_DIR / "demo_gpui_kit.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_gpui_kit.png")
        except Exception as e:
            print(f"  ✗ Failed GPUI Kit: {e}")
        await page.close()

        # 4. Poki: https://poki.bot
        page = await context.new_page()
        try:
            print("  Capturing JosssphZhou/poki...")
            await page.goto("https://poki.bot", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.5)
            await page.screenshot(path=str(IMAGES_DIR / "demo_poki.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_poki.png")
        except Exception as e:
            print(f"  ✗ Failed Poki: {e}")
        await page.close()

        # 5. sshole: https://sshhole.com
        page = await context.new_page()
        try:
            print("  Capturing sshhole.com...")
            await page.goto("https://sshhole.com", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.5)
            await page.screenshot(path=str(IMAGES_DIR / "demo_sshole.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_sshole.png")
        except Exception as e:
            print(f"  ✗ Failed sshole: {e}")
        await page.close()

        await browser.close()
    print("[✓] All real software demo captures completed.")

if __name__ == "__main__":
    asyncio.run(capture_all())
