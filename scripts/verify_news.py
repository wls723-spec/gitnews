import re
import os
import sys
from pathlib import Path

# Force UTF-8 output in Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

html_arg = sys.argv[1] if len(sys.argv) > 1 else r"c:\Program Files\1a\src\gitnews\news\2026-10-22.html"
html_path = Path(html_arg).resolve()

print(f"=== {html_path.name} Validation Report ===")
print(f"File Path: {html_path}")
print(f"File Size: {html_path.stat().st_size:,} bytes ({html_path.stat().st_size / (1024*1024):.2f} MB)")

with open(html_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Check if standalone or relative
is_standalone_css = "<style>" in text and "--bg-paper" in text
is_standalone_js = "lucide" in text and "RoughNotation" in text
has_data_images = "src=\"data:image/" in text

# Check remaining relative assets outside comments
clean_text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
clean_text = re.sub(r'<!--.*?-->', '', clean_text, flags=re.DOTALL)
remaining_assets = re.findall(r'(?:src|href|url)=["\']?(\.\./assets/[^\s"\'\)]+)', clean_text, re.IGNORECASE)
if remaining_assets:
    print(f"\n⚠️  Found {len(remaining_assets)} unresolved relative assets:")
    for a in remaining_assets[:10]:
        print(f"   - {a}")
else:
    print("\n✨ Clean check: Zero unresolved '../assets/' active references found.")

# 2. Check Images
data_imgs = re.findall(r'src="(data:image/[^;]+;base64,[^"]+)"', text)
file_imgs = re.findall(r'src="([^"]+\.(?:jpg|png|webp|svg))"', text)

print(f"\nImage Analysis:")
print(f"  - Embedded Data URI images: {len(data_imgs)}")
print(f"  - External/Relative file images: {len(file_imgs)}")

all_imgs_ok = True
if data_imgs:
    for idx, d in enumerate(data_imgs, 1):
        mime_match = re.match(r'data:(image/[^;]+);base64,', d)
        mime = mime_match.group(1) if mime_match else "unknown"
        data_len = len(d)
        is_ok = data_len > 10000
        print(f"  [Embedded #{idx}] {mime} ({data_len:,} chars) -> {'OK' if is_ok else 'TOO SMALL!'}")
        if not is_ok:
            all_imgs_ok = False

if file_imgs:
    for src in file_imgs:
        full_p = os.path.normpath(os.path.join(os.path.dirname(html_path), src))
        exists = os.path.exists(full_p)
        sz = os.path.getsize(full_p) if exists else 0
        status = "OK" if exists else "MISSING!"
        print(f"  [Local File] {src} ({sz:,} bytes) -> {status}")
        if not exists:
            all_imgs_ok = False

# 3. Check CSS
print(f"\nStyles Analysis:")
if is_standalone_css:
    style_blocks = len(re.findall(r'<style[^>]*>', text, re.I))
    print(f"  [Embedded CSS] Found {style_blocks} <style> block(s) with design system tokens (Standalone OK)")
else:
    css = re.findall(r'href="([^"]+\.css)"', text)
    for c in css:
        full_p = os.path.normpath(os.path.join(os.path.dirname(html_path), c))
        exists = os.path.exists(full_p)
        print(f"  [External CSS] {c} -> exists: {exists}")

# 4. Check Scripts
print(f"\nScripts Analysis:")
if is_standalone_js:
    script_blocks = len(re.findall(r'<script[^>]*>', text, re.I))
    print(f"  [Embedded JS] Found {script_blocks} <script> block(s) with Lucide & RoughNotation (Standalone OK)")
else:
    scripts = re.findall(r'<script src="([^"]+)"', text)
    for sc in scripts:
        full_p = os.path.normpath(os.path.join(os.path.dirname(html_path), sc))
        exists = os.path.exists(full_p)
        print(f"  [External Script] {sc} -> exists: {exists}")

# 5. Component Counts
cards = text.count('class="article-card')
schematics = text.count('class="schematic-container')
showcases = text.count('class="media-showcase-box')
quotes = text.count('class="editorial-quote')
print(f"\nComponent Counts: Cards={cards}, Schematics={schematics}, Showcases={showcases}, Quotes={quotes}")

standalone_perfect = is_standalone_css and is_standalone_js and len(data_imgs) == 10 and len(remaining_assets) == 0

if cards == 5 and schematics == 5 and showcases == 5 and quotes == 5 and all_imgs_ok:
    if standalone_perfect:
        print("\n>>> ALL VALIDATIONS PASSED: 100% PERFECT STANDALONE ALL-IN-ONE HTML! <<<")
    else:
        print("\n>>> ALL VALIDATIONS PASSED PERFECTLY! <<<")
else:
    print("\n>>> SOME VALIDATIONS FAILED! <<<")
