# -*- coding: utf-8 -*-
"""
download_nov15_assets.py
Capture real software interfaces via Playwright for 2026-11-15 Top 5 stories.
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "assets" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

TARGETS = [
    ("opencodereview", "https://open-codereview.ai", "https://github.com/alibaba/open-code-review"),
    ("egm", "https://egm.dev", "https://github.com/google/elephant-goldfish-model"),
    ("plannotator", "https://plannotator.ai", "https://github.com/backnotprop/plannotator"),
    ("tailcat", "https://tailscale.github.io/tailcat/", "https://github.com/tailscale/tailcat"),
    ("openseo", "https://openseo.so", "https://github.com/every-app/open-seo"),
]

async def capture_demos():
    print("[*] Capturing real software interfaces via Playwright for 2026-11-15...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1200, "height": 800}, device_scale_factor=1.5)

        for slug, primary_url, fallback_url in TARGETS:
            page = await context.new_page()
            out_file = IMAGES_DIR / f"demo_{slug}.png"
            captured = False
            try:
                print(f"  Capturing {slug} ({primary_url})...")
                await page.goto(primary_url, wait_until="networkidle", timeout=18000)
                await asyncio.sleep(1.2)
                await page.screenshot(path=str(out_file), clip={"x": 0, "y": 0, "width": 1200, "height": 720})
                print(f"  ✓ Saved {out_file.name} from {primary_url}")
                captured = True
            except Exception as e:
                print(f"  ✗ Primary failed for {slug}: {e}")

            if not captured:
                try:
                    print(f"  Fallback capturing {slug} ({fallback_url})...")
                    await page.goto(fallback_url, wait_until="networkidle", timeout=18000)
                    await asyncio.sleep(1.2)
                    await page.screenshot(path=str(out_file), clip={"x": 0, "y": 150, "width": 1200, "height": 720})
                    print(f"  ✓ Saved {out_file.name} from GitHub fallback")
                except Exception as e2:
                    print(f"  ✗ Fallback failed for {slug}: {e2}")
            await page.close()

        await browser.close()
    print("[✓] Demo screenshot capture routine finished!")

if __name__ == "__main__":
    asyncio.run(capture_demos())
