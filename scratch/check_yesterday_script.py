with open('news/2026-10-21.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script.*?</script>', text, re.DOTALL)
print('2026-10-21.html script count:', len(scripts))
print('Last script:')
print(scripts[-1])
