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

repos = [
    ("synchopate/llama-modchip", "llama_modchip", "https://github.com/synchopate/llama-modchip"),
    ("herdrdev/herdr", "herdr", "https://herdr.dev"),
    ("Vincentwei1021/video-shotcraft", "video_shotcraft", "https://vincentwei1021.github.io/video-shotcraft/"),
    ("Crosstalk-Solutions/project-nomad", "project_nomad", "https://www.projectnomad.us"),
    ("can1357/oh-my-pi", "oh_my_pi", "https://omp.sh"),
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

        # 1. llama-modchip (GitHub repo README table / architecture)
        p1 = await context.new_page()
        try:
            print("  Capturing synchopate/llama-modchip...")
            await p1.goto("https://github.com/synchopate/llama-modchip", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            readme = p1.locator("article.markdown-body")
            if await readme.count() > 0:
                await readme.screenshot(path=str(IMAGES_DIR / "demo_llama_modchip.png"), clip={'x': 0, 'y': 0, 'width': 1000, 'height': 650})
            else:
                await p1.screenshot(path=str(IMAGES_DIR / "demo_llama_modchip.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 700})
            print("  ✓ Saved demo_llama_modchip.png")
        except Exception as e:
            print(f"  ✗ Failed llama-modchip: {e}")
        await p1.close()

        # 2. herdr (https://herdr.dev)
        p2 = await context.new_page()
        try:
            print("  Capturing herdr.dev...")
            await p2.goto("https://herdr.dev", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p2.screenshot(path=str(IMAGES_DIR / "demo_herdr.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_herdr.png")
        except Exception as e:
            print(f"  ✗ Failed herdr.dev, trying github: {e}")
            try:
                await p2.goto("https://github.com/herdrdev/herdr", wait_until="networkidle", timeout=15000)
                await p2.screenshot(path=str(IMAGES_DIR / "demo_herdr.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_herdr.png from GitHub")
            except Exception as e2:
                print(f"  ✗ Fallback failed: {e2}")
        await p2.close()

        # 3. video-shotcraft (https://vincentwei1021.github.io/video-shotcraft/)
        p3 = await context.new_page()
        try:
            print("  Capturing video-shotcraft gallery...")
            await p3.goto("https://vincentwei1021.github.io/video-shotcraft/", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p3.screenshot(path=str(IMAGES_DIR / "demo_video_shotcraft.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_video_shotcraft.png")
        except Exception as e:
            print(f"  ✗ Failed video-shotcraft, trying github: {e}")
            try:
                await p3.goto("https://github.com/Vincentwei1021/video-shotcraft", wait_until="networkidle", timeout=15000)
                await p3.screenshot(path=str(IMAGES_DIR / "demo_video_shotcraft.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_video_shotcraft.png from GitHub")
            except Exception as e2:
                print(f"  ✗ Fallback failed: {e2}")
        await p3.close()

        # 4. project-nomad (https://www.projectnomad.us)
        p4 = await context.new_page()
        try:
            print("  Capturing projectnomad.us...")
            await p4.goto("https://www.projectnomad.us", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p4.screenshot(path=str(IMAGES_DIR / "demo_project_nomad.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_project_nomad.png")
        except Exception as e:
            print(f"  ✗ Failed projectnomad.us, trying github: {e}")
            try:
                await p4.goto("https://github.com/Crosstalk-Solutions/project-nomad", wait_until="networkidle", timeout=15000)
                await p4.screenshot(path=str(IMAGES_DIR / "demo_project_nomad.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_project_nomad.png from GitHub")
            except Exception as e2:
                print(f"  ✗ Fallback failed: {e2}")
        await p4.close()

        # 5. oh-my-pi (https://omp.sh)
        p5 = await context.new_page()
        try:
            print("  Capturing omp.sh...")
            await p5.goto("https://omp.sh", wait_until="networkidle", timeout=15000)
            await asyncio.sleep(1.0)
            await p5.screenshot(path=str(IMAGES_DIR / "demo_oh_my_pi.png"), clip={'x': 0, 'y': 0, 'width': 1200, 'height': 720})
            print("  ✓ Saved demo_oh_my_pi.png")
        except Exception as e:
            print(f"  ✗ Failed omp.sh, trying github: {e}")
            try:
                await p5.goto("https://github.com/can1357/oh-my-pi", wait_until="networkidle", timeout=15000)
                await p5.screenshot(path=str(IMAGES_DIR / "demo_oh_my_pi.png"), clip={'x': 0, 'y': 150, 'width': 1200, 'height': 720})
                print("  ✓ Saved demo_oh_my_pi.png from GitHub")
            except Exception as e2:
                print(f"  ✗ Fallback failed: {e2}")
        await p5.close()

        await browser.close()

if __name__ == '__main__':
    download_og_banners()
    asyncio.run(capture_demos())
