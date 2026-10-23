import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Users\user\.gemini\antigravity-ide\brain\8fed1fc9-481c-4212-8a51-f4b0a91a41b7\.system_generated\steps\41\content.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

papers = re.findall(r'<h3[^>]*>.*?<a[^>]*href="/papers/([0-9\.]+)"[^>]*>(.*?)</a>', text, re.DOTALL)
print(f"Total papers: {len(papers)}")
for pid, title in papers[:15]:
    t = re.sub(r'<[^>]+>', '', title).strip()
    print(f"[{pid}] {t}")
