with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('article-action')
print(text[idx-50:idx+250])
