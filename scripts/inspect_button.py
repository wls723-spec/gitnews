import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

p = Path(r"c:\Program Files\1a\src\gitnews\news\2026-10-23.html")
with open(p, "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find('<header class="header-hero"')
print("Body header & button markup:")
print(text[idx:idx+400])
