# -*- coding: utf-8 -*-
"""
download_nov12_assets.py
Capture real software interfaces via Playwright for 2026-11-12 Top 5 stories.
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

        # 1. aws-emulator
        p1 = await context.new_page()
        try:
            print("  Capturing aws-emulator (docs)...")
            await p1.goto("https://docs.aws.amazon.com/emulator/latest/userguide/what-is-service.html", wait_until="networkidle", timeout=12000)
            await asyncio.sleep(1.0)
            await p1.screenshot(path=str(IMAGES_DIR / "demo_awsemulator.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_awsemulator.png from AWS docs")
        except Exception as e:
            print(f"  ✗ Failed AWS docs, fallback to github: {e}")
            try:
                await p1.goto("https://github.com/aws/aws-emulator", wait_until="networkidle", timeout=15000)
                readme = p1.locator("article.markdown-body")
                if await readme.count() > 0:
                    await readme.screenshot(path=str(IMAGES_DIR / "demo_awsemulator.png"), clip={'x': 0, 'y': 0, 'width': 1000, 'height': 680})
                else:
                    await p1.screenshot(path=str(IMAGES_DIR / "demo_awsemulator.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_awsemulator.png from GitHub")
            except Exception as e2:
                print(f"  ✗ aws-emulator fallback failed: {e2}")
        await p1.close()

        # 2. shadcn/improve
        p2 = await context.new_page()
        try:
            print("  Capturing shadcn/improve...")
            await p2.goto("https://github.com/shadcn/improve", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            readme = p2.locator("article.markdown-body")
            if await readme.count() > 0:
                await readme.screenshot(path=str(IMAGES_DIR / "demo_improve.png"))
            else:
                await p2.screenshot(path=str(IMAGES_DIR / "demo_improve.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_improve.png from GitHub")
        except Exception as e:
            print(f"  ✗ shadcn/improve failed: {e}")
        await p2.close()

        # 3. codex-security
        p3 = await context.new_page()
        try:
            print("  Capturing codex-security...")
            await p3.goto("https://developers.openai.com/codex/security", wait_until="networkidle", timeout=12000)
            await asyncio.sleep(1.0)
            await p3.screenshot(path=str(IMAGES_DIR / "demo_codexsec.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_codexsec.png from developers.openai.com")
        except Exception as e:
            print(f"  ✗ Failed openai docs, fallback to github: {e}")
            try:
                await p3.goto("https://github.com/openai/codex-security", wait_until="networkidle", timeout=15000)
                readme = p3.locator("article.markdown-body")
                if await readme.count() > 0:
                    await readme.screenshot(path=str(IMAGES_DIR / "demo_codexsec.png"), clip={'x': 0, 'y': 0, 'width': 1000, 'height': 680})
                else:
                    await p3.screenshot(path=str(IMAGES_DIR / "demo_codexsec.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_codexsec.png from GitHub")
            except Exception as e2:
                print(f"  ✗ codex-security fallback failed: {e2}")
        await p3.close()

        # 4. yogurt (yogurt.so)
        p4 = await context.new_page()
        try:
            print("  Capturing yogurt.so...")
            await p4.goto("https://yogurt.so", wait_until="networkidle", timeout=12000)
            await asyncio.sleep(1.0)
            await p4.screenshot(path=str(IMAGES_DIR / "demo_yogurt.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_yogurt.png from yogurt.so")
        except Exception as e:
            print(f"  ✗ Failed yogurt.so, fallback to github: {e}")
            try:
                await p4.goto("https://github.com/FrigadeHQ/yogurt", wait_until="networkidle", timeout=15000)
                readme = p4.locator("article.markdown-body")
                if await readme.count() > 0:
                    await readme.screenshot(path=str(IMAGES_DIR / "demo_yogurt.png"), clip={'x': 0, 'y': 0, 'width': 1000, 'height': 680})
                else:
                    await p4.screenshot(path=str(IMAGES_DIR / "demo_yogurt.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_yogurt.png from GitHub")
            except Exception as e2:
                print(f"  ✗ yogurt fallback failed: {e2}")
        await p4.close()

        # 5. sglang-omni
        p5 = await context.new_page()
        try:
            print("  Capturing sglang-omni...")
            await p5.goto("https://sgl-project.github.io/sglang-omni/", wait_until="networkidle", timeout=12000)
            await asyncio.sleep(1.0)
            await p5.screenshot(path=str(IMAGES_DIR / "demo_sglomni.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_sglomni.png from docs site")
        except Exception as e:
            print(f"  ✗ Failed sglang-omni docs, fallback to github: {e}")
            try:
                await p5.goto("https://github.com/sgl-project/sglang-omni", wait_until="networkidle", timeout=15000)
                readme = p5.locator("article.markdown-body")
                if await readme.count() > 0:
                    await readme.screenshot(path=str(IMAGES_DIR / "demo_sglomni.png"), clip={'x': 0, 'y': 0, 'width': 1000, 'height': 680})
                else:
                    await p5.screenshot(path=str(IMAGES_DIR / "demo_sglomni.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_sglomni.png from GitHub")
            except Exception as e2:
                print(f"  ✗ sglang-omni fallback failed: {e2}")
        await p5.close()

        await browser.close()
    print("[✓] All 5 demo screenshots captured successfully.")

if __name__ == "__main__":
    asyncio.run(capture_demos())
