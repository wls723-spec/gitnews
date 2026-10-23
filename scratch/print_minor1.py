import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx1 = text.find('id="minor-gh-1"')
idx2 = text.find('id="minor-gh-2"')
print('=== FULL MINOR ITEM 1 HTML ===')
print(text[idx1:idx2])
