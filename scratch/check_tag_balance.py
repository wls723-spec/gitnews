with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
open_styles = [m.start() for m in re.finditer(r'<style\b', text, re.I)]
close_styles = [m.start() for m in re.finditer(r'</style>', text, re.I)]
print(f'open <style>: {len(open_styles)}, close </style>: {len(close_styles)}')
for i, (o, c) in enumerate(zip(open_styles, close_styles)):
    print(f'Style {i+1}: open at {o}, close at {c}')

# Also check for unclosed <p> tags or unclosed <pre> or unclosed <div>
# Let's check tag balance for all common tags
for tag in ['style', 'script', 'div', 'p', 'section', 'article', 'button', 'a']:
    o = len(re.findall(f'<{tag}\\b', text, re.I))
    c = len(re.findall(f'</{tag}>', text, re.I))
    print(f'Tag <{tag}>: open={o}, close={c}, diff={o-c}')
