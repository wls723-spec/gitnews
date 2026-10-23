with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'stopPropagation', text)]
print('stopPropagation occurrences:', len(matches))
for idx in matches:
    print(text[idx-50:idx+150])

print('\nArticle detail container:')
idx = text.find('class="article-detail"')
print(text[idx-50:idx+250])
