import re
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

base_brain = Path(r"C:\Users\user\.gemini\antigravity-ide\brain\81a8e2f1-7fe5-4702-8651-5293502e2ad2\.system_generated\steps")

def parse_trending(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    items = text.split('<article class="Box-row"')
    if len(items) > 1:
        items = ['<article class="Box-row"' + it.split('</article>')[0] + '</article>' for it in items[1:]]
    results = []
    for it in items:
        repo = re.search(r'href="/([a-zA-Z0-9_\.-]+/[a-zA-Z0-9_\.-]+)"', it)
        repo_name = repo.group(1) if repo else "unknown"
        desc = re.search(r'<p[^>]*>(.*?)</p>', it, re.DOTALL)
        desc_text = re.sub(r'<[^>]+>', '', desc.group(1)).strip() if desc else ""
        stars_today = re.search(r'([0-9,]+)\s+stars\s+today', it, re.IGNORECASE)
        stars_str = stars_today.group(1) if stars_today else "?"
        tot_stars = re.search(r'stargazers"[^>]*>.*?([0-9,]+)', it, re.DOTALL)
        tot_str = tot_stars.group(1).strip() if tot_stars else "?"
        lang = re.search(r'itemprop="programmingLanguage">(.*?)</span>', it)
        lang_str = lang.group(1).strip() if lang else "General"
        results.append({
            "repo": repo_name,
            "lang": lang_str,
            "today": stars_str,
            "total": tot_str,
            "desc": desc_text
        })
    return results

print("=== [GitHub Trending General (Step 45)] ===")
for i, it in enumerate(parse_trending(base_brain / "45" / "content.md"), 1):
    print(f"[{i:2d}] {it['repo']} ({it['lang']}) +{it['today']} today | Tot: {it['total']}")
    print(f"     {it['desc']}")

print("\n=== [Hacker News Top (Step 53)] ===")
with open(base_brain / "53" / "content.md", "r", encoding="utf-8") as f:
    hn_text = f.read()
# Parse HN stories
hn_rows = re.findall(r'<tr class=[\'"]athing[\'"][^>]*>.*?<span class=[\'"]titleline[\'"]><a href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>.*?</tr>\s*<tr><td class=[\'"]subtext[\'"]>(.*?)</td>', hn_text, re.DOTALL)
print(f"Total HN stories: {len(hn_rows)}")
for i, (link, title, subtext) in enumerate(hn_rows[:15], 1):
    score = re.search(r'(\d+)\s+points', subtext)
    pts = score.group(1) if score else "0"
    age = re.search(r'<span class=[\'"]age[\'"][^>]*><a[^>]*>(.*?)</a>', subtext)
    time_str = age.group(1) if age else ""
    by = re.search(r'by\s+<a[^>]*>(.*?)</a>', subtext)
    by_str = by.group(1) if by else ""
    comments = re.search(r'(\d+)\s+comments', subtext)
    comms = comments.group(1) if comments else "0"
    print(f"[{i:2d}] {title} ({pts} pts, {time_str}, {comms} comments)")
    print(f"     Link: {link}")

print("\n=== [Show HN (Step 55)] ===")
with open(base_brain / "55" / "content.md", "r", encoding="utf-8") as f:
    show_text = f.read()
show_rows = re.findall(r'<tr class=[\'"]athing[\'"][^>]*>.*?<span class=[\'"]titleline[\'"]><a href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>.*?</tr>\s*<tr><td class=[\'"]subtext[\'"]>(.*?)</td>', show_text, re.DOTALL)
print(f"Total Show HN: {len(show_rows)}")
for i, (link, title, subtext) in enumerate(show_rows[:15], 1):
    score = re.search(r'(\d+)\s+points', subtext)
    pts = score.group(1) if score else "0"
    age = re.search(r'<span class=[\'"]age[\'"][^>]*><a[^>]*>(.*?)</a>', subtext)
    time_str = age.group(1) if age else ""
    print(f"[{i:2d}] {title} ({pts} pts, {time_str})")
    print(f"     Link: {link}")
