with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'\.minor-item\.active', text)]
for idx in matches:
    print('--- match .minor-item.active ---')
    print(text[idx-50:idx+250])
