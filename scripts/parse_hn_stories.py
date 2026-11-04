import re
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

base_brain = Path(r"C:\Users\user\.gemini\antigravity-ide\brain\14776ea4-88ef-4708-a435-2a8667c1b519\.system_generated\steps")

for step in ["36", "38"]:
    p = base_brain / step / "content.md"
    if not p.exists():
        continue
    with open(p, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    
    print(f"=== HN Step {step} ===")
    i = 0
    while i < len(lines):
        m = re.match(r'\[(.*?)\]\((https?://[^\)]+)\)', lines[i])
        if m:
            title, link = m.group(1), m.group(2)
            if not any(k in link for k in ["ycombinator.com/news", "ycombinator.com/newest", "ycombinator.com/front", "ycombinator.com/newcomments", "ycombinator.com/ask", "ycombinator.com/show", "ycombinator.com/jobs", "ycombinator.com/submit", "ycombinator.com/login"]):
                sub = lines[i+1:i+6]
                sub_str = " | ".join(sub)
                print(f"- {title}")
                print(f"    Link: {link}")
                print(f"    Meta: {sub_str}")
        i += 1
