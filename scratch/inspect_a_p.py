with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# check <a> tags
a_opens = list(re.finditer(r'<a\b[^>]*>', text))
a_closes = list(re.finditer(r'</a>', text))
print(f'Open <a> count: {len(a_opens)}, Close </a> count: {len(a_closes)}')

# Check which <a> tags do not have matching </a>
# Let's inspect where <a> tags are
for i, m in enumerate(a_opens):
    next_close = None
    # find first close after this open
    for c in a_closes:
        if c.start() > m.start():
            next_close = c
            break
    # check if another open happens before next_close
    # or just print <a> tags
    print(f'[{i+1}] at {m.start()}: {m.group(0)[:60]}')

# check <p> tags
p_opens = list(re.finditer(r'<p\b[^>]*>', text))
p_closes = list(re.finditer(r'</p>', text))
print(f'\nOpen <p> count: {len(p_opens)}, Close </p> count: {len(p_closes)}')
