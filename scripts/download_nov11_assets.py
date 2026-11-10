# -*- coding: utf-8 -*-
"""
download_nov11_assets.py
Capture real software interfaces via Playwright for 2026-11-11 Top 5 stories.
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

        # 1. holyarrs
        p1 = await context.new_page()
        try:
            print("  Capturing HolyArrs (holyarrs.com)...")
            await p1.goto("https://holyarrs.com", wait_until="networkidle", timeout=12000)
            await asyncio.sleep(1.0)
            await p1.screenshot(path=str(IMAGES_DIR / "demo_holyarrs.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_holyarrs.png from holyarrs.com")
        except Exception as e:
            print(f"  ✗ Failed holyarrs.com, fallback to github: {e}")
            try:
                await p1.goto("https://github.com/HolyArrs/HolyArrs", wait_until="networkidle", timeout=15000)
                readme = p1.locator("article.markdown-body")
                if await readme.count() > 0:
                    await readme.screenshot(path=str(IMAGES_DIR / "demo_holyarrs.png"), clip={'x': 0, 'y': 0, 'width': 1000, 'height': 680})
                else:
                    await p1.screenshot(path=str(IMAGES_DIR / "demo_holyarrs.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_holyarrs.png from GitHub")
            except Exception as e2:
                print(f"  ✗ holyarrs fallback failed: {e2}")
        await p1.close()

        # 2. ha-mcp
        p2 = await context.new_page()
        try:
            print("  Capturing ha-mcp...")
            await p2.goto("https://homeassistant-ai.github.io/ha-mcp/", wait_until="networkidle", timeout=12000)
            await asyncio.sleep(1.0)
            await p2.screenshot(path=str(IMAGES_DIR / "demo_hamcp.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_hamcp.png from docs site")
        except Exception as e:
            print(f"  ✗ Failed ha-mcp docs site, fallback to github: {e}")
            try:
                await p2.goto("https://github.com/homeassistant-ai/ha-mcp", wait_until="networkidle", timeout=15000)
                readme = p2.locator("article.markdown-body")
                if await readme.count() > 0:
                    await readme.screenshot(path=str(IMAGES_DIR / "demo_hamcp.png"), clip={'x': 0, 'y': 0, 'width': 1000, 'height': 680})
                else:
                    await p2.screenshot(path=str(IMAGES_DIR / "demo_hamcp.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_hamcp.png from GitHub")
            except Exception as e2:
                print(f"  ✗ ha-mcp fallback failed: {e2}")
        await p2.close()

        # 3. watermarks-remover
        p3 = await context.new_page()
        try:
            print("  Capturing watermarks-remover...")
            await p3.goto("https://github.com/guillaumemeyer/watermarks-remover", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            readme = p3.locator("article.markdown-body")
            if await readme.count() > 0:
                await readme.screenshot(path=str(IMAGES_DIR / "demo_watermark.png"))
            else:
                await p3.screenshot(path=str(IMAGES_DIR / "demo_watermark.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_watermark.png from GitHub")
        except Exception as e:
            print(f"  ✗ watermarks-remover failed: {e}")
        await p3.close()

        # 4. modern-web-guidance
        p4 = await context.new_page()
        try:
            print("  Capturing modern-web-guidance...")
            await p4.goto("https://developer.chrome.com/docs/modern-web-guidance", wait_until="networkidle", timeout=12000)
            await asyncio.sleep(1.0)
            await p4.screenshot(path=str(IMAGES_DIR / "demo_modernweb.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_modernweb.png from chrome docs")
        except Exception as e:
            print(f"  ✗ Failed chrome docs, fallback to github: {e}")
            try:
                await p4.goto("https://github.com/GoogleChrome/modern-web-guidance", wait_until="networkidle", timeout=15000)
                readme = p4.locator("article.markdown-body")
                if await readme.count() > 0:
                    await readme.screenshot(path=str(IMAGES_DIR / "demo_modernweb.png"))
                else:
                    await p4.screenshot(path=str(IMAGES_DIR / "demo_modernweb.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_modernweb.png from GitHub")
            except Exception as e2:
                print(f"  ✗ modernweb fallback failed: {e2}")
        await p4.close()

        # 5. ghostwalk
        p5 = await context.new_page()
        try:
            print("  Capturing GhostWalk...")
            await p5.goto("https://github.com/DhanushNehru/GhostWalk", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            readme = p5.locator("article.markdown-body")
            if await readme.count() > 0:
                await readme.screenshot(path=str(IMAGES_DIR / "demo_ghostwalk.png"))
            else:
                await p5.screenshot(path=str(IMAGES_DIR / "demo_ghostwalk.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_ghostwalk.png from GitHub")
        except Exception as e:
            print(f"  ✗ GhostWalk failed: {e}")
        await p5.close()

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture_demos())
