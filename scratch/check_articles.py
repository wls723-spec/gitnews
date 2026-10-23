with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
articles = re.findall(r'<article class="article-card[^"]*".*?</article>', text, re.DOTALL)
print(f'Total article-card elements: {len(articles)}')
for i, a in enumerate(articles):
    print(f'Article {i+1}: length={len(a)}, has toggleArticle={"toggleArticle" in a}, has onclick={"onclick" in a}')
