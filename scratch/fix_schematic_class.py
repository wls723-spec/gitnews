with open(r'c:\Program Files\1a\src\gitnews\news\2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('class="schematic-container minor-schematic"', 'class="minor-schematic"')

with open(r'c:\Program Files\1a\src\gitnews\news\2026-10-22.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated minor schematic class!")
