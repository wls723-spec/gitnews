with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
css_matches = re.findall(r'(\.article-card[^{]*\{[^}]*\})', text)
for c in css_matches:
    print(c)
    print('---')

css_detail = re.findall(r'(\.article-detail[^{]*\{[^}]*\})', text)
for c in css_detail:
    print(c)
    print('---')
