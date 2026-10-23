import os
import glob
from PIL import Image, ImageDraw, ImageFont

brain_dir = r"C:\Users\user\.gemini\antigravity-ide\brain\81a8e2f1-7fe5-4702-8651-5293502e2ad2"
scratch_dir = r"c:\Program Files\1a\src\gitnews\scratch"
dest_dir = r"c:\Program Files\1a\src\gitnews\assets\images"
os.makedirs(dest_dir, exist_ok=True)

TARGET_SIZE = (1376, 768)

def fit_and_save(src_path, dest_filename):
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
    res.save(out_path, "JPEG", quality=92)
    print(f"[SAVED] {dest_filename}: {res.size}, {os.path.getsize(out_path):,} bytes")

# 1. Composite HackiOS 4-screen collage
def create_hackios_collage():
    screens = [
        os.path.join(scratch_dir, "hackios_lockscreen.jpg"),
        os.path.join(scratch_dir, "hackios_homescreen.jpg"),
        os.path.join(scratch_dir, "hackios_control-center.jpg"),
        os.path.join(scratch_dir, "hackios_settings.jpg")
    ]
    canvas = Image.new("RGB", TARGET_SIZE, (15, 18, 25))
    draw = ImageDraw.Draw(canvas)
    
    # Calculate dimensions for 4 phones side by side
    margin_top = 40
    avail_h = TARGET_SIZE[1] - 80
    avail_w = TARGET_SIZE[0] - 80
    phone_w = avail_w // 4 - 20
    phone_h = int(phone_w * (1600 / 720))
    if phone_h > avail_h:
        phone_h = avail_h
        phone_w = int(phone_h * (720 / 1600))
        
    total_w = 4 * phone_w + 3 * 24
    start_x = (TARGET_SIZE[0] - total_w) // 2
    start_y = (TARGET_SIZE[1] - phone_h) // 2
    
    titles = ["Lock Screen", "SpringBoard Home", "Control Center", "iOS 16.5 Settings"]
    for i, p in enumerate(screens):
        im = Image.open(p).convert("RGB")
        im_res = im.resize((phone_w, phone_h), Image.Resampling.LANCZOS)
        x = start_x + i * (phone_w + 24)
        y = start_y
        # Draw frame shadow and border
        draw.rectangle([x - 3, y - 3, x + phone_w + 3, y + phone_h + 3], outline=(60, 70, 90), width=2)
        canvas.paste(im_res, (x, y))
        
    out_path = os.path.join(dest_dir, "demo_hackios_ui.jpg")
    canvas.save(out_path, "JPEG", quality=92)
    print(f"[SAVED] demo_hackios_ui.jpg: {canvas.size}, {os.path.getsize(out_path):,} bytes")

# Execute
create_hackios_collage()

# 5 Thumbnails
fit_and_save(glob.glob(os.path.join(brain_dir, "thumb_hackios_*.jpg"))[0], "thumb_hackios.jpg")
fit_and_save(glob.glob(os.path.join(brain_dir, "thumb_openshell_*.jpg"))[0], "thumb_openshell.jpg")
fit_and_save(glob.glob(os.path.join(brain_dir, "thumb_genoffice_*.jpg"))[0], "thumb_genoffice.jpg")
fit_and_save(glob.glob(os.path.join(brain_dir, "thumb_anthropic_plugins_*.jpg"))[0], "thumb_anthropic_plugins.jpg")
fit_and_save(glob.glob(os.path.join(brain_dir, "thumb_cua_*.jpg"))[0], "thumb_cua.jpg")

# 4 Demo showcases
fit_and_save(glob.glob(os.path.join(brain_dir, "demo_openshell_cli_*.jpg"))[0], "demo_openshell_cli.jpg")
fit_and_save(os.path.join(scratch_dir, "genoffice_hero.webp"), "demo_genoffice_editor.jpg")
fit_and_save(glob.glob(os.path.join(brain_dir, "demo_anthropic_plugins_*.jpg"))[0], "demo_anthropic_plugins_catalog.jpg")
fit_and_save(os.path.join(scratch_dir, "cua_spaces.webp"), "demo_cua_desktop.jpg")

print("\nAll 10 images processed and saved into assets/images/ successfully!")
