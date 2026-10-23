import re
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

p = Path(r"c:\Program Files\1a\src\gitnews\news\2026-10-22.html")
with open(p, "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'(<div class="minor-item".*?</div>\s*</div>\s*</div>)', text, re.DOTALL)
if m:
    print(m.group(1)[:1200])
