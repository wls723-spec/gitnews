import os
import glob
from PIL import Image

brain_dir = r"C:\Users\user\.gemini\antigravity-ide\brain\8fed1fc9-481c-4212-8a51-f4b0a91a41b7"
scratch_dir = r"c:\Program Files\1a\src\gitnews\scratch"
dest_dir = r"c:\Program Files\1a\src\gitnews\assets\images"
os.makedirs(dest_dir, exist_ok=True)

TARGET_SIZE = (1376, 768)

def fit_and_save(src_path, dest_filename):
    im = Image.open(src_path)
    if im.mode != "RGB":
        im = im.convert("RGB")
    
    # Calculate aspect ratio
    target_ratio = TARGET_SIZE[0] / TARGET_SIZE[1]
    src_ratio = im.width / im.height
    
    if abs(src_ratio - target_ratio) < 0.05:
        # Close enough, simple resize
        res = im.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
    elif src_ratio > target_ratio:
        # Image is wider: crop sides or fit with background
        new_width = int(im.height * target_ratio)
        left = (im.width - new_width) // 2
        im_cropped = im.crop((left, 0, left + new_width, im.height))
        res = im_cropped.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
    else:
        # Image is taller: crop top/bottom or fit
        new_height = int(im.width / target_ratio)
        top = (im.height - new_height) // 2
        im_cropped = im.crop((0, top, im.width, top + new_height))
        res = im_cropped.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        
    out_path = os.path.join(dest_dir, dest_filename)
    res.save(out_path, "JPEG", quality=92)
    print(f"[SAVED] {dest_filename}: {res.size}, {os.path.getsize(out_path):,} bytes")

image_map = {
    "thumb_impeccable.jpg": glob.glob(os.path.join(brain_dir, "thumb_impeccable_*.jpg"))[0],
    "demo_impeccable_audit.jpg": glob.glob(os.path.join(brain_dir, "demo_impeccable_audit_*.jpg"))[0],
    "thumb_headroom.jpg": glob.glob(os.path.join(brain_dir, "thumb_headroom_*.jpg"))[0],
    "demo_headroom_compression.jpg": os.path.join(scratch_dir, "headroom_hero.png"),
    "thumb_freellmapi.jpg": glob.glob(os.path.join(brain_dir, "thumb_freellmapi_*.jpg"))[0],
    "demo_freellmapi_dashboard.jpg": os.path.join(scratch_dir, "freellmapi_desktop.png"),
    "thumb_agent_reach.jpg": glob.glob(os.path.join(brain_dir, "thumb_agent_reach_*.jpg"))[0],
    "demo_agent_reach_cli.jpg": glob.glob(os.path.join(brain_dir, "demo_agent_reach_cli_*.jpg"))[0],
    "thumb_worldmonitor.jpg": glob.glob(os.path.join(brain_dir, "thumb_worldmonitor_*.jpg"))[0],
    "demo_worldmonitor_map.jpg": os.path.join(scratch_dir, "worldmonitor_map.jpg"),
}

for dest_name, src in image_map.items():
    fit_and_save(src, dest_name)

print("\nAll 10 images processed successfully into assets/images/!")
