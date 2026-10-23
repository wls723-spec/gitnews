with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

minor_idx = text.find('<section class="minor-radar-section"')
script_idx = text.find('function toggleMinorItem')
print(f'section index: {minor_idx}')
print(f'script index: {script_idx}')
print(f'total length: {len(text)}')

if minor_idx != -1:
    print('HTML before section:')
    print(text[minor_idx-200:minor_idx])
    print('HTML after section:')
    end_sec = text.find('</section>', minor_idx)
    print(text[end_sec:end_sec+300])
