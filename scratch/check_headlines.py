import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

headlines = re.findall(r'<strong class="minor-headline-text">(.*?)</strong>', text)
print(f'Total headlines: {len(headlines)}')
for i, h in enumerate(headlines, 1):
    print(f'{i:02d}. {h}')
