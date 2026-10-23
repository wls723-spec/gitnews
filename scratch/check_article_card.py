with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

card_idx = text.find('class="article-card"')
print('=== ARTICLE CARD HTML ===')
print(text[card_idx:card_idx+1200])

print('=== TOGGLE ARTICLE FUNCTION ===')
import re
match = re.search(r'function toggleArticle.*?\n    \}', text, re.DOTALL)
if match:
    print(match.group(0))
