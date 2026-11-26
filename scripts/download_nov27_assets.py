# -*- coding: utf-8 -*-
"""
download_nov27_assets.py
Capture real software interfaces via Playwright for 2026-11-27 Top 5 stories.
"""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

REPO_ROOT = Path(__file__).resolve().parent.parent
IMAGES_DIR = REPO_ROOT / "assets" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

TARGETS = [
    ("minipg", "https://progrium.github.io/minipg/", "https://github.com/progrium/minipg"),
    ("mailflare", "https://mailflare.co", "https://github.com/hieunc229/mailflare"),
    ("rdnaboosts", "https://github.com/stew675/llama-cpp-rdna-boosts", "https://devnull.land/amd-specific-llama-cpp"),
    ("reloc", "https://github.com/Reukix/Reloc", "https://github.com/Reukix/Reloc"),
    ("databrokers", "https://agent.garrettstimpson.ca/remove", "https://github.com/gary23w/f-ck_data_brokers"),
]

async def capture_demos():
    print("[*] Capturing real software interfaces via Playwright for 2026-11-27...")
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context(viewport={"width": 1200, "height": 800}, device_scale_factor=1.5)

        for slug, primary_url, fallback_url in TARGETS:
            page = await context.new_page()
            out_file = IMAGES_DIR / f"demo_{slug}.png"
            captured = False
            try:
                print(f"  Capturing {slug} ({primary_url})...")
                await page.goto(primary_url, wait_until="domcontentloaded", timeout=25000)
                try:
                    await page.wait_for_load_state("networkidle", timeout=8000)
                except Exception:
                    pass
                await asyncio.sleep(2.0)
                y_offset = 240 if "github.com/" in primary_url and "github.io" not in primary_url else 0
                await page.screenshot(path=str(out_file), clip={"x": 0, "y": y_offset, "width": 1200, "height": 720})
                if out_file.stat().st_size > 15000:
                    print(f"  ✓ Saved {out_file.name} from {primary_url} ({out_file.stat().st_size:,} bytes)")
                    captured = True
            except Exception as e:
                print(f"  ✗ Primary failed for {slug}: {e}")

            if not captured and fallback_url != primary_url:
                try:
                    print(f"  Fallback capturing {slug} ({fallback_url})...")
                    await page.goto(fallback_url, wait_until="domcontentloaded", timeout=25000)
                    try:
                        await page.wait_for_load_state("networkidle", timeout=8000)
                    except Exception:
                        pass
                    await asyncio.sleep(1.5)
                    y_offset = 240 if "github.com/" in fallback_url and "github.io" not in fallback_url else 0
                    await page.screenshot(path=str(out_file), clip={"x": 0, "y": y_offset, "width": 1200, "height": 720})
                    print(f"  ✓ Saved {out_file.name} from fallback ({out_file.stat().st_size:,} bytes)")
                except Exception as e2:
                    print(f"  ✗ Fallback failed for {slug}: {e2}")
            await page.close()

        await browser.close()
    print("[✓] Demo screenshot capture routine finished!")

if __name__ == "__main__":
    asyncio.run(capture_demos())
