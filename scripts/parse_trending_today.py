import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Users\user\.gemini\antigravity-ide\brain\8fed1fc9-481c-4212-8a51-f4b0a91a41b7\.system_generated\steps\25\content.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

items = text.split('<article class="Box-row"')
if len(items) > 1:
    items = ['<article class="Box-row"' + it.split('</article>')[0] + '</article>' for it in items[1:]]

print(f"Total items found: {len(items)}")
for i, it in enumerate(items):
    repo = re.search(r'<h2[^>]*>.*?<a[^>]*href="/([a-zA-Z0-9_\.-]+/[a-zA-Z0-9_\.-]+)"', it, re.DOTALL)
    if not repo:
        repo = re.search(r'href="/([a-zA-Z0-9_\.-]+/[a-zA-Z0-9_\.-]+)"', it)
    repo_name = repo.group(1) if repo else "unknown"
    
    desc = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', it, re.DOTALL)
    if not desc:
        desc = re.search(r'<p[^>]*>(.*?)</p>', it, re.DOTALL)
    desc_text = re.sub(r'<[^>]+>', '', desc.group(1)).strip() if desc else ""
    
    stars_today = re.search(r'([0-9,]+)\s+stars\s+today', it, re.IGNORECASE)
    stars_str = stars_today.group(1) if stars_today else "?"
    
    tot_stars = re.search(r'stargazers"[^>]*>.*?([0-9,]+)', it, re.DOTALL)
    tot_str = tot_stars.group(1).strip() if tot_stars else "?"
    
    lang = re.search(r'itemprop="programmingLanguage">(.*?)</span>', it)
    lang_str = lang.group(1).strip() if lang else "General"
    
    print(f"[{i+1}] {repo_name} ({lang_str}) | +{stars_str} today | Total: {tot_str}")
    print(f"    Desc: {desc_text}")
