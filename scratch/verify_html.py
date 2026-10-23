import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r'c:\Program Files\1a\src\gitnews\news\2026-10-15.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

print('Length of 2026-10-15.html:', len(html))

# Check images and scripts referenced in HTML
imgs = re.findall(r'src="([^"]+)"', html)
print('\nReferenced images/scripts:')
all_exist = True
for img in imgs:
    target = os.path.normpath(os.path.join(r'c:\Program Files\1a\src\gitnews\news', img))
    exists = os.path.exists(target)
    if not exists:
        all_exist = False
    print(f'  {img} -> exists: {exists}')

# Check CSS
css_files = re.findall(r'rel="stylesheet"\s+href="([^"]+)"', html)
for c in css_files:
    target = os.path.normpath(os.path.join(r'c:\Program Files\1a\src\gitnews\news', c))
    print(f'  CSS {c} -> exists: {os.path.exists(target)}')

# Check structural elements
print('\nHero title present:', 'id="hero-title"' in html)
print('Editorial quotes count:', len(re.findall(r'class="editorial-quote', html)))
print('Schematic containers count:', len(re.findall(r'class="schematic-container', html)))
print('Media showcase count:', len(re.findall(r'class="media-showcase-box', html)))
print('Article cards count:', len(re.findall(r'class="article-card', html)))

# Tag balance check
tags = ['article', 'div', 'p', 'h1', 'h2', 'h3', 'header', 'footer', 'script']
print('\nTag balance check:')
for t in tags:
    opens = len(re.findall(rf'<{t}\b', html))
    closes = len(re.findall(rf'</{t}>', html))
    diff = opens - closes
    print(f'  <{t}> opens: {opens}, closes: {closes}, diff: {diff}')
    if diff != 0:
        print(f'    WARNING: Unbalanced <{t}> tag!')
