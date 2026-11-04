# -*- coding: utf-8 -*-
import os
import glob
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

brain_dir = r"C:\Users\user\.gemini\antigravity-ide\brain\aac371d7-8594-478c-b6cc-0d4c1b7065bc"
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

# 1. Process 5 Thumbnails
thumb_agent = glob.glob(os.path.join(brain_dir, "thumb_agent_desktop_*.jpg"))[0]
thumb_game = glob.glob(os.path.join(brain_dir, "thumb_game_studios_*.jpg"))[0]
thumb_colibri = glob.glob(os.path.join(brain_dir, "thumb_colibri_*.jpg"))[0]
thumb_hex = glob.glob(os.path.join(brain_dir, "thumb_hex_*.jpg"))[0]
thumb_openmontage = glob.glob(os.path.join(brain_dir, "thumb_openmontage_*.jpg"))[0]

fit_and_save(thumb_agent, "thumb_agent_desktop.jpg")
fit_and_save(thumb_game, "thumb_game_studios.jpg")
fit_and_save(thumb_colibri, "thumb_colibri.jpg")
fit_and_save(thumb_hex, "thumb_hex.jpg")
fit_and_save(thumb_openmontage, "thumb_openmontage.jpg")

# 2. Process 5 In-depth Demo Images
# Story 1 Demo: agent-desktop accessibility tree terminal & UI snapshot
fit_and_save(os.path.join(dest_dir, "agent_desktop_og.png"), "demo_agent_desktop.png", "PNG")

# Story 2 Demo: game-studios hierarchy & orchestration snapshot
fit_and_save(os.path.join(dest_dir, "game_studios_og.png"), "demo_game_studios.png", "PNG")

# Story 3 Demo: colibri monitor real terminal MoE live stream
fit_and_save(os.path.join(dest_dir, "colibri_monitor.png"), "demo_colibri.png", "PNG")

# Story 4 Demo: hex native local voice dictation UI
fit_and_save(os.path.join(dest_dir, "hex_og.png"), "demo_hex.png", "PNG")

# Story 5 Demo: openmontage backlot production board
fit_and_save(os.path.join(dest_dir, "openmontage_board.png"), "demo_openmontage.png", "PNG")

print("All 10 images processed and normalized successfully.")
