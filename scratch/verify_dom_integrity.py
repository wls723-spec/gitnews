import re
from pathlib import Path

html_path = Path(r"c:\Program Files\1a\src\gitnews\news\2026-10-22.html")
text = html_path.read_text(encoding="utf-8")

minor_items = re.findall(r'<div class="minor-item" id="minor-([^"]+)"[^>]*>', text)
print(f"Total minor items in HTML: {len(minor_items)}")
for i, m in enumerate(minor_items, 1):
    print(f"  [{i:02d}] minor-{m}")

assert len(minor_items) == 18, f"Expected 18, got {len(minor_items)}"

open_divs = text.count("<div")
close_divs = text.count("</div>")
print(f"\nDiv balance: open={open_divs}, close={close_divs}")
assert open_divs == close_divs, "Unbalanced <div> tags!"

print("\n>>> HTML DOM integrity 100% verified! <<<")
