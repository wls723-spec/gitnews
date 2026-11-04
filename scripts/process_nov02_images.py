# -*- coding: utf-8 -*-
import os
import glob
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

brain_dir = r"C:\Users\user\.gemini\antigravity-ide\brain\32632ad5-390b-4df6-9d9a-9b706ef97d76"
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

# 1. Save 5 Thumbnails
thumb_deepseek = glob.glob(os.path.join(brain_dir, "thumb_deepseek_superagent_*.jpg"))[0]
thumb_icloud = glob.glob(os.path.join(brain_dir, "thumb_icloud_s3_*.jpg"))[0]
thumb_aisoc = glob.glob(os.path.join(brain_dir, "thumb_aisoc_*.jpg"))[0]
thumb_pixelfx = glob.glob(os.path.join(brain_dir, "thumb_pixelfx_*.jpg"))[0]
thumb_hop = glob.glob(os.path.join(brain_dir, "thumb_hop_linux_*.jpg"))[0]

fit_and_save(thumb_deepseek, "thumb_deepseek_superagent.jpg")
fit_and_save(thumb_icloud, "thumb_icloud_s3.jpg")
fit_and_save(thumb_aisoc, "thumb_aisoc.jpg")
fit_and_save(thumb_pixelfx, "thumb_pixelfx.jpg")
fit_and_save(thumb_hop, "thumb_hop_linux.jpg")

# Helper for drawing window/terminal apps
def create_app_window(title, draw_func, out_filename):
    canvas = Image.new("RGB", TARGET_SIZE, (15, 20, 28))
    draw = ImageDraw.Draw(canvas)
    
    # Header bar
    draw.rectangle([0, 0, TARGET_SIZE[0], 48], fill=(28, 35, 48))
    # Traffic light buttons
    draw.ellipse([20, 18, 32, 30], fill=(255, 95, 86))
    draw.ellipse([42, 18, 54, 30], fill=(255, 189, 46))
    draw.ellipse([64, 18, 76, 30], fill=(39, 201, 63))
    
    try:
        font_title = ImageFont.truetype("consola.ttf", 18)
    except Exception:
        font_title = ImageFont.load_default()
    draw.text((100, 14), title, fill=(180, 195, 215), font=font_title)
    
    draw_func(canvas, draw)
    
    out_path = os.path.join(dest_dir, out_filename)
    canvas.save(out_path, "JPEG", quality=92)
    print(f"[SAVED] {out_filename}: {canvas.size}, {os.path.getsize(out_path):,} bytes")

# 2. Demo DeepSeek SuperAgent Web Panel & Session Runtime
def draw_deepseek_panel(canvas, draw):
    try:
        font_h1 = ImageFont.truetype("consolab.ttf", 24)
        font_code = ImageFont.truetype("consola.ttf", 17)
        font_bold = ImageFont.truetype("consolab.ttf", 18)
        font_small = ImageFont.truetype("consola.ttf", 14)
    except Exception:
        font_h1 = font_code = font_bold = font_small = ImageFont.load_default()
        
    draw.rectangle([0, 48, TARGET_SIZE[0], TARGET_SIZE[1]], fill=(13, 17, 23))
    
    # Left Column: Work Items & Assessor Intake
    draw.rectangle([40, 70, 680, 720], fill=(22, 27, 34), outline=(48, 54, 61), width=2)
    draw.rectangle([40, 70, 680, 120], fill=(33, 38, 45))
    draw.text((60, 83), "dsh-superagent // Active Tickets & MasterAssessor", fill=(88, 166, 255), font=font_h1)
    
    tickets = [
        ("TKT-1082", "Feishu #dev-channel", "PROACTIVE", "Refactor payment webhook retry with exponential backoff", "DshExecutor [Running]", (56, 189, 248)),
        ("TKT-1083", "GitHub Issue #442", "QUEUED", "Fix memory leak in websocket broadcast listener", "MasterAssessor [Approved]", (74, 222, 128)),
        ("TKT-1084", "GitHub PR #450", "IN_REVIEW", "Implement Z3 formal verification check in CI pipeline", "Waiting Human Review", (250, 204, 21)),
        ("TKT-1085", "Cron Scheduled", "ADMITTED", "Nightly dependency vulnerability sweep & patch generation", "Scope: Repository Root", (168, 85, 247))
    ]
    
    y = 135
    for tid, src, badge, desc, status, col in tickets:
        draw.rectangle([55, y, 665, y + 120], fill=(18, 22, 29), outline=(48, 54, 61), width=1)
        draw.text((70, y + 12), f"[{tid}] {src}", fill=(139, 148, 158), font=font_small)
        draw.rectangle([520, y + 8, 650, y + 32], fill=(30, 41, 59), outline=col, width=1)
        draw.text((530, y + 11), badge, fill=col, font=font_small)
        draw.text((70, y + 42), desc[:52], fill=(240, 246, 252), font=font_bold)
        draw.text((70, y + 72), desc[52:], fill=(240, 246, 252), font=font_bold)
        draw.text((70, y + 95), f"Status: {status}", fill=col, font=font_code)
        y += 140

    # Right Column: Live Session Execution & Outbox
    draw.rectangle([710, 70, 1335, 720], fill=(22, 27, 34), outline=(48, 54, 61), width=2)
    draw.rectangle([710, 70, 1335, 120], fill=(33, 38, 45))
    draw.text((730, 83), "Active Execution Sandbox [TKT-1082]", fill=(63, 185, 80), font=font_h1)
    
    logs = [
        ("[08:34:12] Engine: ticket TKT-1082 admitted by MasterAssessor (confidence=0.98)", (139, 148, 158)),
        ("[08:34:13] DshExecutor: spawning workspace in /tmp/dsh-agent-session-819", (139, 148, 158)),
        ("[08:34:14] Tool: git clone --single-branch -b main repo /tmp/dsh-agent-session-819", (100, 180, 255)),
        ("[08:34:16] Tool: read_file src/webhooks/payment.ts (lines 1-140)", (100, 180, 255)),
        ("[08:34:18] Agent: detected unbounded while loop on HTTP 503 responses", (250, 204, 21)),
        ("[08:34:20] Tool: edit_file src/webhooks/payment.ts with backoff jitter logic", (74, 222, 128)),
        ("[08:34:22] Tool: run_command pnpm test (tests: 48 passed, 0 failed)", (74, 222, 128)),
        ("[08:34:25] Policy: changes strictly contained within allowed scope (payment.ts)", (56, 189, 248)),
        ("[08:34:27] Outbox: drafting GitHub Pull Request #451 with reproduction trace", (168, 85, 247)),
        ("[08:34:29] Outbox: replying to Feishu thread: 'PR #451 opened. 0 human tokens wasted.'", (63, 185, 80)),
        ("[08:34:30] Session: workspace cleaned. Zero orphan processes remaining.", (139, 148, 158)),
        ("----------------------------------------------------------------", (48, 54, 61)),
        ("Core Philosophy: Take minimal human attention, deliver maximal engineering value.", (240, 246, 252))
    ]
    
    ly = 138
    for line, lcol in logs:
        draw.text((730, ly), line, fill=lcol, font=font_code)
        ly += 42

create_app_window("DeepSeek Harness // dsh-superagent Autonomous Control Plane (localhost:3000)", draw_deepseek_panel, "demo_deepseek_superagent.jpg")

# 3. Demo iCloud-S3
def draw_icloud_demo(canvas, draw):
    try:
        font_h1 = ImageFont.truetype("consolab.ttf", 22)
        font_code = ImageFont.truetype("consola.ttf", 16)
        font_bold = ImageFont.truetype("consolab.ttf", 18)
        font_small = ImageFont.truetype("consola.ttf", 14)
    except Exception:
        font_h1 = font_code = font_bold = font_small = ImageFont.load_default()
        
    draw.rectangle([0, 48, TARGET_SIZE[0], TARGET_SIZE[1]], fill=(18, 22, 28))
    
    # Left: Apple Photos.app Shared Album view
    draw.rectangle([40, 70, 700, 720], fill=(28, 32, 40), outline=(50, 58, 70), width=2)
    draw.rectangle([40, 70, 700, 115], fill=(38, 44, 56))
    draw.text((60, 82), "Photos.app — Shared Albums // 'S3-Bucket-Backups-01'", fill=(225, 235, 245), font=font_h1)
    
    # 2x2 grid of Photos with HUD headers
    photos_meta = [
        ("pg_dump_production_20261102.sql.gz", "11.8 MB", "RGB Lossless Carrier #001", "CRC32: 0x8FA43E19"),
        ("redis_dump_cluster_node3.rdb", "9.4 MB", "RGB Lossless Carrier #002", "CRC32: 0x3C9B10F2"),
        ("app_assets_bundle_v4.2.tar.zst", "12.1 MB", "RGB Lossless Carrier #003", "CRC32: 0xEE71A90B"),
        ("clickhouse_mergetree_part.bin", "10.6 MB", "RGB Lossless Carrier #004", "CRC32: 0x51BD884A")
    ]
    
    grid_coords = [
        (60, 135, 360, 405),
        (380, 135, 680, 405),
        (60, 430, 360, 700),
        (380, 430, 680, 700)
    ]
    
    for (name, sz, carrier, crc), (gx1, gy1, gx2, gy2) in zip(photos_meta, grid_coords):
        draw.rectangle([gx1, gy1, gx2, gy2], fill=(12, 14, 18), outline=(60, 72, 88), width=1)
        # Burned-in 64px HUD Banner
        draw.rectangle([gx1, gy1, gx2, gy1 + 64], fill=(15, 23, 42))
        draw.rectangle([gx1, gy1 + 62, gx2, gy1 + 64], fill=(56, 189, 248))
        draw.text((gx1 + 10, gy1 + 8), "iCloudS3 OBJECT CARRIER", fill=(56, 189, 248), font=font_small)
        draw.text((gx1 + 10, gy1 + 24), name[:28], fill=(255, 255, 255), font=font_small)
        draw.text((gx1 + 10, gy1 + 42), f"Size: {sz} | {crc}", fill=(148, 163, 184), font=font_small)
        # Steganography pixel noise texture representation
        draw.rectangle([gx1 + 10, gy1 + 75, gx2 - 10, gy2 - 10], fill=(24, 30, 42))
        draw.text((gx1 + 35, gy1 + 140), "2048x2048 24-bit RGB PNG", fill=(100, 116, 139), font=font_code)
        draw.text((gx1 + 45, gy1 + 165), "[12.18 MB Stego Payload]", fill=(52, 211, 153), font=font_code)

    # Right: Terminal running AWS CLI against icloud-s3
    draw.rectangle([730, 70, 1335, 720], fill=(15, 17, 23), outline=(48, 54, 61), width=2)
    draw.rectangle([730, 70, 1335, 115], fill=(22, 27, 34))
    draw.text((750, 82), "Terminal — AWS S3 CLI REST Interface (port 9000)", fill=(240, 246, 252), font=font_h1)
    
    term_lines = [
        ("$ icloud-s3 serve --port 9000 --quota-bypass-mode shared-album", (240, 246, 252)),
        ("INFO  icloud_s3::server > Initializing S3 REST Gateway on 127.0.0.1:9000", (56, 189, 248)),
        ("INFO  icloud_s3::apple  > Authenticated iCloud session: 200 Shared Albums available", (74, 222, 128)),
        ("INFO  icloud_s3::apple  > Max capacity: 1,000,000 objects (~12.18 TB at $0.00/mo)", (250, 204, 21)),
        ("INFO  icloud_s3::server > Apple Shared Album Quota policy: EXEMPT from iCloud Drive quota", (74, 222, 128)),
        ("", (0, 0, 0)),
        ("$ export AWS_ENDPOINT_URL=http://localhost:9000", (240, 246, 252)),
        ("$ aws s3 cp ./pg_dump_production.sql.gz s3://backups/prod-db.sql.gz", (240, 246, 252)),
        ("upload: ./pg_dump_production.sql.gz to s3://backups/prod-db.sql.gz (11.8 MB)", (56, 189, 248)),
        ("DEBUG icloud_s3::stego > lower byte stream into 2048x2048x3 PNG buffer", (139, 148, 158)),
        ("DEBUG icloud_s3::stego > burned 64px HUD header overlay (SHA-256 + metadata)", (139, 148, 158)),
        ("DEBUG icloud_s3::apple > PhotoKit sync: POST /album/upload -> HTTP 200 OK", (74, 222, 128)),
        ("", (0, 0, 0)),
        ("$ aws s3 ls s3://backups/", (240, 246, 252)),
        ("2026-11-02 08:14:02   12411420 prod-db.sql.gz", (226, 232, 240)),
        ("2026-11-02 08:15:33    9856512 redis_dump_cluster_node3.rdb", (226, 232, 240)),
        ("2026-11-02 08:18:41   12713984 app_assets_bundle_v4.2.tar.zst", (226, 232, 240)),
        ("", (0, 0, 0)),
        ("$ aws s3 cp s3://backups/prod-db.sql.gz /tmp/restored.sql.gz", (240, 246, 252)),
        ("download: s3://backups/prod-db.sql.gz to /tmp/restored.sql.gz [CRC32 VALID]", (52, 211, 153))
    ]
    
    ty = 135
    for tline, tcol in term_lines:
        draw.text((750, ty), tline, fill=tcol, font=font_code)
        ty += 28

create_app_window("iCloudS3 Architecture // Apple Shared Album Stego Gateway + AWS S3 REST", draw_icloud_demo, "demo_icloud_s3.jpg")

# 4. Demo AiSOC: combine aisoc_og.png or build custom dashboard
fit_and_save(os.path.join(scratch_dir, "aisoc_og.png"), "demo_aisoc.jpg")

# 5. Demo PixelFX: extract best frame from montage.gif
gif_path = os.path.join(scratch_dir, "pixelfx_montage.gif")
if os.path.exists(gif_path):
    gim = Image.open(gif_path)
    # seek to frame 15
    gim.seek(15)
    gim_frame = gim.convert("RGB")
    gim_frame.save(os.path.join(scratch_dir, "pixelfx_frame.png"))
    fit_and_save(os.path.join(scratch_dir, "pixelfx_frame.png"), "demo_pixelfx.jpg")

# 6. Demo Hop: fit hop_screenshot.png into app window
fit_and_save(os.path.join(scratch_dir, "hop_screenshot.png"), "demo_hop_linux.jpg")
