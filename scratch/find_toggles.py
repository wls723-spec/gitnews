with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '펼치기' in line or 'toggle' in line.lower() or 'active' in line.lower():
        if len(line.strip()) < 300:
            print(f'L{i+1}: {line.strip()}')
