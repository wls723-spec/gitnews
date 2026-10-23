with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print('toggleMinorItem in html:', 'toggleMinorItem' in text)
print('minor-radar-section in html:', 'minor-radar-section' in text)
print('minor-item in html count:', text.count('minor-item'))

scripts = re.findall(r'<script.*?</script>', text, re.DOTALL)
print(f'Total script tags: {len(scripts)}')
for i, s in enumerate(scripts):
    print(f'=== Script {i} ===')
    print(s[:1000])

# Also check CSS related to minor
css_matches = re.findall(r'\.minor[^{]*\{[^}]*\}', text)
print(f'Found {len(css_matches)} CSS rules for .minor:')
for r in css_matches[:15]:
    print(r)
