# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('class="minor-item"')
print('=== FIRST MINOR ITEM HTML ===')
print(text[idx:idx+1500])

