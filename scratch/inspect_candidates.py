import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

steps = {
    "pentagi": r"C:\Users\user\.gemini\antigravity-ide\brain\df4bf2a0-cfaf-4d12-a55b-1dc5faf41a55\.system_generated\steps\55\content.md",
    "hyperframes": r"C:\Users\user\.gemini\antigravity-ide\brain\df4bf2a0-cfaf-4d12-a55b-1dc5faf41a55\.system_generated\steps\57\content.md",
    "ruview": r"C:\Users\user\.gemini\antigravity-ide\brain\df4bf2a0-cfaf-4d12-a55b-1dc5faf41a55\.system_generated\steps\59\content.md",
    "ifixai": r"C:\Users\user\.gemini\antigravity-ide\brain\df4bf2a0-cfaf-4d12-a55b-1dc5faf41a55\.system_generated\steps\61\content.md",
    "soup": r"C:\Users\user\.gemini\antigravity-ide\brain\df4bf2a0-cfaf-4d12-a55b-1dc5faf41a55\.system_generated\steps\63\content.md",
}

for name, path in steps.items():
    print(f"\n==================== {name.upper()} ====================")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    m = re.search(r'<article class="markdown-body[^"]*"[^>]*>(.*?)</article>', c, re.DOTALL)
    if m:
        body = m.group(1)
        # strip tags but keep line breaks
        text = re.sub(r'<h[1-6][^>]*>(.*?)</h[1-6]>', r'\n### \1\n', body)
        text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n', text)
        text = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', text)
        text = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', text)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        print(text[:2500])
    else:
        print("markdown-body not found")
