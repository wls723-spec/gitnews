import re

with open(r'c:\Program Files\1a\src\gitnews\news\2026-10-14.html', 'r', encoding='utf-8') as f:
    c = f.read()

footers = re.findall(r'<div class="article-footer-links">.*?</div>\s*</div>', c, re.DOTALL)
for i, f in enumerate(footers, 1):
    print(f'=== Article {i} Footers ===')
    links = re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', f, re.DOTALL)
    for href, text in links:
        clean_text = re.sub(r'<[^>]+>', '', text).strip()
        print(f'  - [{clean_text}] -> {href}')
