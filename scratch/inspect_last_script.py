with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script.*?</script>', text, re.DOTALL)
print(f'Total script tags: {len(scripts)}')
print('=== LAST SCRIPT TAG ===')
print(scripts[-1])
