# -*- coding: utf-8 -*-
"""
download_nov19_assets.py
Capture real software interfaces via Playwright for 2026-11-19 Top 5 stories.
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "assets" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

TARGETS = [
    ("minimind", "https://github.com/jingyaogong/minimind", "https://jingyaogong.github.io/minimind"),
    ("substrate", "https://ate.dev/", "https://github.com/agent-substrate/substrate"),
    ("cli_anything", "https://hkuds.github.io/CLI-Anything/", "https://github.com/HKUDS/CLI-Anything"),
    ("stitch_skills", "https://stitch.withgoogle.com/docs/mcp/setup/", "https://github.com/google-labs-code/stitch-skills"),
    ("sellbird", "https://sellbird.ai", "https://github.com/ethanplusai/sellbird"),
]

async def capture_demos():
    print("[*] Capturing real software interfaces via Playwright for 2026-11-19...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1200, "height": 800}, device_scale_factor=1.5)

        for slug, primary_url, fallback_url in TARGETS:
            page = await context.new_page()
            out_file = IMAGES_DIR / f"demo_{slug}.png"
            captured = False
            try:
                print(f"  Capturing {slug} ({primary_url})...")
                await page.goto(primary_url, wait_until="networkidle", timeout=25000)
                await asyncio.sleep(2.0)
                y_offset = 140 if "github.com/" in primary_url else 0
                await page.screenshot(path=str(out_file), clip={"x": 0, "y": y_offset, "width": 1200, "height": 720})
                if out_file.stat().st_size > 15000:
                    print(f"  ✓ Saved {out_file.name} from {primary_url} ({out_file.stat().st_size:,} bytes)")
                    captured = True
            except Exception as e:
                print(f"  ✗ Primary failed for {slug}: {e}")

            if not captured:
                try:
                    print(f"  Fallback capturing {slug} ({fallback_url})...")
                    await page.goto(fallback_url, wait_until="networkidle", timeout=25000)
                    await asyncio.sleep(1.5)
                    y_offset = 140 if "github.com/" in fallback_url else 0
                    await page.screenshot(path=str(out_file), clip={"x": 0, "y": y_offset, "width": 1200, "height": 720})
                    print(f"  ✓ Saved {out_file.name} from fallback ({out_file.stat().st_size:,} bytes)")
                except Exception as e2:
                    print(f"  ✗ Fallback failed for {slug}: {e2}")
            await page.close()

        await browser.close()
    print("[✓] Demo screenshot capture routine finished!")

if __name__ == "__main__":
    asyncio.run(capture_demos())
