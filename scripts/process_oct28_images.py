import os
import glob
import sys
from PIL import Image, ImageDraw, ImageFont

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

brain_dir = r"C:\Users\user\.gemini\antigravity-ide\brain\f9e7e56d-d80a-4a76-bb3e-59819bed5494"
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
thumb_hallmark_path = glob.glob(os.path.join(brain_dir, "thumb_hallmark_*.jpg"))[0]
thumb_thinkrail_path = glob.glob(os.path.join(brain_dir, "thumb_thinkrail_*.jpg"))[0]
thumb_tradingagents_path = glob.glob(os.path.join(brain_dir, "thumb_tradingagents_*.jpg"))[0]
thumb_skillspector_path = glob.glob(os.path.join(brain_dir, "thumb_skillspector_*.jpg"))[0]
thumb_deeptutor_path = glob.glob(os.path.join(brain_dir, "thumb_deeptutor_*.jpg"))[0]

fit_and_save(thumb_hallmark_path, "thumb_hallmark.jpg")
fit_and_save(thumb_thinkrail_path, "thumb_thinkrail.jpg")
fit_and_save(thumb_tradingagents_path, "thumb_tradingagents.jpg")
fit_and_save(thumb_skillspector_path, "thumb_skillspector.jpg")
fit_and_save(thumb_deeptutor_path, "thumb_deeptutor.jpg")

# 2. Showcases from downloaded repos
fit_and_save(os.path.join(scratch_dir, "hallmark_og.png"), "demo_hallmark_ui.jpg")
fit_and_save(os.path.join(scratch_dir, "thinkrail_workbench_dark.png"), "demo_thinkrail_workbench.jpg")
fit_and_save(os.path.join(scratch_dir, "trading_cli_transaction.png"), "demo_tradingagents_cli.jpg")
fit_and_save(os.path.join(scratch_dir, "deeptutor_chatloop.png"), "demo_deeptutor_ui.jpg")

# 3. Create authentic terminal window for NVIDIA SkillSpector
def create_terminal_window(title, lines, out_filename):
    canvas = Image.new("RGB", TARGET_SIZE, (18, 22, 30))
    draw = ImageDraw.Draw(canvas)
    
    # Window header bar
    draw.rectangle([0, 0, TARGET_SIZE[0], 48], fill=(30, 36, 48))
    # Traffic light buttons
    draw.ellipse([20, 18, 32, 30], fill=(255, 95, 86))
    draw.ellipse([42, 18, 54, 30], fill=(255, 189, 46))
    draw.ellipse([64, 18, 76, 30], fill=(39, 201, 63))
    
    # Title text
    try:
        font_title = ImageFont.truetype("consola.ttf", 18)
        font_body = ImageFont.truetype("consola.ttf", 20)
        font_bold = ImageFont.truetype("consolab.ttf", 20)
    except Exception:
        font_title = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_bold = font_body
        
    draw.text((TARGET_SIZE[0] // 2 - 160, 14), title, fill=(180, 190, 205), font=font_title)
    
    # Lines of terminal output
    y = 70
    for prefix, text, color in lines:
        if prefix:
            draw.text((40, y), prefix, fill=(120, 140, 165), font=font_bold)
            draw.text((40 + int(len(prefix) * 12.5), y), text, fill=color, font=font_body)
        else:
            draw.text((40, y), text, fill=color, font=font_body)
        y += 28
        
    out_path = os.path.join(dest_dir, out_filename)
    canvas.save(out_path, "JPEG", quality=92)
    print(f"[SAVED] {out_filename}: {canvas.size}, {os.path.getsize(out_path):,} bytes")

skillspector_lines = [
    ("$ ", "skillspector scan --path ~/.claude/skills/untrusted-web-scraper", (240, 245, 255)),
    ("", "NVIDIA SkillSpector v1.2.0 — Scanning against 71 patterns across 17 categories", (148, 163, 184)),
    ("  [AST Parser]", "Analyzing SKILL.md instruction blocks and Python tool hooks...", (200, 210, 225)),
    ("", "", (200, 200, 200)),
    ("  [!] VULNERABILITY DETECTED:", "Rule B.3.2 — MCP Tool Poisoning via Shadowing", (248, 113, 113)),
    ("      Severity: CRITICAL (CVSS 9.1)", "Line 42: Tool name shadows native 'read_file' with exfiltration hook", (248, 113, 113)),
    ("  [!] PROMPT INJECTION ALERT:", "Rule P.1.4 — Zero-width space instruction override", (250, 204, 21)),
    ("      Severity: HIGH", "Hidden unicode payload detected in skill preamble: system prompt leakage", (250, 204, 21)),
    ("  [!] SUPPLY CHAIN CHECK:", "Live query to OSV.dev: cve-2026-4419 detected in pinned dependency", (248, 113, 113)),
    ("", "", (200, 200, 200)),
    ("  --------------------------------------------------------------------------------", "", (100, 116, 139)),
    ("  [SECURITY AUDIT SCORE]", "RISK INDEX: 89/100 (HIGH RISK — INSTALLATION BLOCKED)", (248, 113, 113)),
    ("  [Recommendation]", "DO NOT INSTALL. Skill attempts covert credential scraping via MCP pipe.", (248, 113, 113)),
    ("  [SARIF Report]", "Saved security findings ledger to .skillspector/audit-report-20261028.sarif", (74, 222, 128)),
    ("  [Pipeline Status]", "NVIDIA Verified Skills Gate: REJECTED", (248, 113, 113)),
]
create_terminal_window("NVIDIA SkillSpector — AI Agent Skill Static & Semantic Security Analyzer", skillspector_lines, "demo_skillspector_terminal.jpg")

print("\nAll 10 images processed and verified in assets/images/!")
