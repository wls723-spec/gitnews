with open('news/2026-10-22.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find all occurrences of <article>, <button>, <a>, etc in the paragraphs
paras = re.findall(r'<p[^>]*>(.*?)</p>', text, re.DOTALL)
print(f'Total paragraphs: {len(paras)}')

for p in paras:
    # check if there are raw tags like <style>, <script>, <article>, <button>, <a> inside paragraph text that might not be closed
    inner_tags = re.findall(r'<([a-zA-Z0-9]+)[^>]*>', p)
    for t in inner_tags:
        if t.lower() not in ['br', 'strong', 'em', 'span', 'i', 'code']:
            print(f'Found suspicious inner tag <{t}> inside paragraph:')
            print(p[:300])
            print('---')
