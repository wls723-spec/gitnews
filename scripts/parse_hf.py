import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Users\user\.gemini\antigravity-ide\brain\2ca0e18b-03d0-4eae-a2f9-46645d871208\.system_generated\steps\51\content.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

print("=== Hugging Face Daily Papers Today ===")
# extract paper links and titles
matches = re.findall(r'<h3[^>]*>.*?<a[^>]*href="\/papers\/([0-9\.]+)"[^>]*>(.*?)<\/a>', text, re.DOTALL)
if not matches:
    matches = re.findall(r'href="\/papers\/([0-9\.]+)"', text)
    print("Paper IDs:", list(dict.fromkeys(matches))[:8])
else:
    seen = set()
    for pid, title in matches:
        clean = re.sub(r'<[^>]+>', '', title).strip()
        if pid not in seen and len(clean) > 3:
            seen.add(pid)
            print(f"[{pid}] {clean}")
