import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Users\user\.gemini\antigravity-ide\brain\2ca0e18b-03d0-4eae-a2f9-46645d871208\.system_generated\steps\41\content.md"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

items = html.split('<article class="Box-row"')
if len(items) > 1:
    items = ['<article class="Box-row"' + it.split('</article>')[0] + '</article>' for it in items[1:]]
print(f"Total articles found: {len(items)}")

for i, it in enumerate(items):
    repo = re.search(r'<h2[^>]*>.*?<a[^>]*href="\/([a-zA-Z0-9_\.-]+\/[a-zA-Z0-9_\.-]+)"', it, re.DOTALL)
    repo_name = repo.group(1) if repo else "unknown"
    
    desc = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', it, re.DOTALL)
    if not desc:
        desc = re.search(r'<p[^>]*>(.*?)</p>', it, re.DOTALL)
    desc_text = desc.group(1).strip() if desc else ""
    desc_text = re.sub(r'<[^>]+>', '', desc_text).strip()
    
    stars_today = re.search(r'([0-9,]+)\s+stars\s+today', it, re.IGNORECASE)
    stars_str = stars_today.group(1) if stars_today else "?"
    
    total_stars = re.search(r'href="\/[^\/]+\/[^\/]+\/stargazers"[^>]*>.*?([0-9,]+)', it, re.DOTALL)
    tot_str = total_stars.group(1).strip() if total_stars else "?"
    
    lang = re.search(r'itemprop="programmingLanguage">(.*?)</span>', it)
    lang_str = lang.group(1).strip() if lang else "General"
    
    print(f"\n[#{i+1}] {repo_name} ({lang_str})")
    print(f"   Stars Today: +{stars_str} | Total: {tot_str}")
    print(f"   Desc: {desc_text}")
