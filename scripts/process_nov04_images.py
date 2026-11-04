# -*- coding: utf-8 -*-
import os
import glob
import sys
from pathlib import Path
from PIL import Image

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

brain_dir = r"C:\Users\user\.gemini\antigravity\brain\bfdf59d6-4e1b-483e-ab3c-322149a96cd4"
scratch_dir = r"c:\Program Files\1a\src\gitnews\scratch"
dest_dir = r"c:\Program Files\1a\src\gitnews\assets\images"
os.makedirs(dest_dir, exist_ok=True)

TARGET_SIZE = (1376, 768)

def fit_and_save(src_path, dest_filename, target_format="JPEG", quality=92):
    im = Image.open(src_path)
    if im.mode != "RGB":
        im = im.convert("RGB")
    
    target_ratio = TARGET_SIZE[0] / TARGET_SIZE[1]
    src_ratio = im.width / im.height
    
    if abs(src_ratio - target_ratio) < 0.05:
        res = im.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
    elif src_ratio > target_ratio:
        new_width = int(im.height * target_ratio)
        left = (im.width - new_width) // 2
        im_cropped = im.crop((left, 0, left + new_width, im.height))
        res = im_cropped.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
    else:
        new_height = int(im.width / target_ratio)
        top = (im.height - new_height) // 2
        im_cropped = im.crop((0, top, im.width, top + new_height))
        res = im_cropped.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        
    out_path = os.path.join(dest_dir, dest_filename)
    res.save(out_path, target_format, quality=quality)
    print(f"[SAVED] {dest_filename}: {res.size}, {os.path.getsize(out_path):,} bytes")

# 1. Process 5 Thumbnails from brain directory
thumb_nanochat = glob.glob(os.path.join(brain_dir, "thumb_nanochat_*.jpg"))[0]
thumb_heretic = glob.glob(os.path.join(brain_dir, "thumb_heretic_*.jpg"))[0]
thumb_t3code = glob.glob(os.path.join(brain_dir, "thumb_t3code_*.jpg"))[0]
thumb_floci = glob.glob(os.path.join(brain_dir, "thumb_floci_*.jpg"))[0]
thumb_shannon = glob.glob(os.path.join(brain_dir, "thumb_shannon_*.jpg"))[0]

fit_and_save(thumb_nanochat, "thumb_nanochat.jpg")
fit_and_save(thumb_heretic, "thumb_heretic.jpg")
fit_and_save(thumb_t3code, "thumb_t3code.jpg")
fit_and_save(thumb_floci, "thumb_floci.jpg")
fit_and_save(thumb_shannon, "thumb_shannon.jpg")

# 2. Process 5 In-depth Demo Images
# Story 1 Demo: nanochat scaling laws benchmark
fit_and_save(os.path.join(scratch_dir, "scaling_laws_jan26.png"), "demo_nanochat.png", "PNG")

# Story 2 Demo: heretic OpenGraph banner & vector steering architecture
fit_and_save(os.path.join(scratch_dir, "og_heretic.png"), "demo_heretic.png", "PNG")

# Story 3 Demo: t3code OpenGraph / control surface snapshot
fit_and_save(os.path.join(scratch_dir, "og_t3code.png"), "demo_t3code.png", "PNG")

# Story 4 Demo: floci local emulator runtime
fit_and_save(os.path.join(scratch_dir, "og_floci.png"), "demo_floci.png", "PNG")

# Story 5 Demo: shannon AI pentester light banner
fit_and_save(os.path.join(scratch_dir, "shannon_banner.png"), "demo_shannon.png", "PNG")

print("All 10 images successfully processed and saved to assets/images!")
