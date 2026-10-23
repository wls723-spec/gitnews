import re
from pathlib import Path

p = Path(r"c:\Program Files\1a\src\gitnews\news\2026-10-22.html")
with open(p, "r", encoding="utf-8") as f:
    text = f.read()

idx1 = text.find("/* ==========================================================================\n   MINOR EMERGING RADAR SECTION")
idx2 = text.find("</style>", idx1)
print("Minor CSS block:")
print(text[idx1:idx2])
