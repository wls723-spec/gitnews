with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
minor_items = re.findall(r'<div class="minor-item"[^>]*>.*?</div>\s*</div>', text, re.DOTALL)
print(f'Total minor items found: {len(minor_items)}')
for i, m in enumerate(minor_items[:3]):
    print(f'Minor {i+1}: length={len(m)}, has toggleMinorItem={"toggleMinorItem" in m}')
