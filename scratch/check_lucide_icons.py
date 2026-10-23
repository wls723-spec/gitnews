with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
icons = re.findall(r'data-lucide="([^"]+)"', text)
print(f'Total icons: {len(icons)}')
unique_icons = sorted(set(icons))
print('Unique icons:', unique_icons)

# Check if these exist in lucide.min.js
with open('assets/libs/lucide.min.js', 'r', encoding='utf-8') as f:
    lucide_js = f.read()

def to_pascal(s):
    parts = s.split('-')
    return ''.join(p.capitalize() for p in parts)

missing = []
for ic in unique_icons:
    pascal = to_pascal(ic)
    # search for pascal in lucide_js
    if pascal not in lucide_js:
        missing.append((ic, pascal))

print('Missing icons in lucide:', missing)
