import re
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

p = Path(r"c:\Program Files\1a\src\gitnews\news\2026-10-22.html")
with open(p, "r", encoding="utf-8") as f:
    text = f.read()

# remove base64
text_clean = re.sub(r'data:image/[^;]+;base64,[^\"]+', '[DATA_URI]', text)
lines = text_clean.split('\n')
header_lines = []
capturing = False
count = 0
for l in lines:
    if '<header' in l:
        capturing = True
    if capturing:
        header_lines.append(l)
        count += 1
        if count > 120 or '</article>' in l:
            break

print('\n'.join(header_lines[:100]))
