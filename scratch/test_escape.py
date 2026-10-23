# -*- coding: utf-8 -*-
import sys
import html
import re
from pathlib import Path
from generate_deep_minor_section import deep_minor_items

sys.stdout.reconfigure(encoding='utf-8')

def escape_text(text):
    # Escape < and > and &
    # We want &lt; and &gt;
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# Test on all items
for i, it in enumerate(deep_minor_items, 1):
    for f in ['community_reaction', 'mechanism', 'use_case', 'future_outlook']:
        raw = it[f]
        esc = escape_text(raw)
        if "<" in esc:
            print(f"ERROR: still has < in item {i} {f}")

print("All text fields cleanly escaped!")
