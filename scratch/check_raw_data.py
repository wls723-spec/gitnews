import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# In generate_deep_minor_section:
from generate_deep_minor_section import deep_minor_items

for i, it in enumerate(deep_minor_items, 1):
    for field in ['community_reaction', 'mechanism', 'use_case', 'future_outlook']:
        val = it[field]
        # check for raw <
        raw_tags = re.findall(r'<[^>]*>', val)
        if raw_tags:
            print(f"Item {i} ({it['title']}) field '{field}' has raw tags: {raw_tags}")
