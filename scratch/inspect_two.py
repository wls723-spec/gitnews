import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for name, p in [('pentagi', r'C:\Users\user\.gemini\antigravity-ide\brain\df4bf2a0-cfaf-4d12-a55b-1dc5faf41a55\.system_generated\steps\55\content.md'),
                ('hyperframes', r'C:\Users\user\.gemini\antigravity-ide\brain\df4bf2a0-cfaf-4d12-a55b-1dc5faf41a55\.system_generated\steps\57\content.md')]:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'<article class="markdown-body[^"]*"[^>]*>(.*?)</article>', c, re.DOTALL)
    if m:
        text = re.sub(r'<[^>]+>', ' ', m.group(1))
        text = re.sub(r'\s+', ' ', text)
        print(f'=== {name.upper()} ===')
        print(text[:1800])
    else:
        print(f"=== {name.upper()} === (markdown body not matched)")
