import re
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def parse_trending_file(path, label):
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return []

    items = text.split('<article class="Box-row"')
    if len(items) > 1:
        items = ['<article class="Box-row"' + it.split('</article>')[0] + '</article>' for it in items[1:]]

    results = []
    for it in items:
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
        lang_str = lang.group(1).strip() if lang else label

        results.append({
            "repo": repo_name,
            "lang": lang_str,
            "today": stars_str,
            "total": tot_str,
            "desc": desc_text
        })
    return results

# Read seen projects
seen_file = Path(r"c:\Program Files\1a\src\gitnews\history_seen_projects.md")
with open(seen_file, "r", encoding="utf-8") as f:
    seen_text = f.read()

base_brain = Path(r"C:\Users\user\.gemini\antigravity-ide\brain\bab986cd-389a-4857-8cb4-c1f185aa4e09\.system_generated\steps")
sources = [
    (base_brain / "25" / "content.md", "General"),
    (base_brain / "27" / "content.md", "Python"),
    (base_brain / "29" / "content.md", "TypeScript"),
    (base_brain / "31" / "content.md", "Rust"),
]

all_repos = {}
for path, label in sources:
    for item in parse_trending_file(path, label):
        r = item["repo"]
        if r != "unknown" and r not in all_repos:
            all_repos[r] = item

print(f"=== Total unique GitHub Trending repos discovered: {len(all_repos)} ===")
unseen = []
for r, info in all_repos.items():
    is_seen = r.lower() in seen_text.lower()
    flag = "[SEEN]" if is_seen else "[NEW!]"
    if not is_seen:
        unseen.append(info)
    print(f"{flag:7} {info['repo']:35} ({info['lang']:10}) | +{info['today']:>6} today | Tot: {info['total']:>8}")

print(f"\n=== NEW CANDIDATES ({len(unseen)}) ===")
for u in unseen:
    print(f"-> {u['repo']} ({u['lang']}) : +{u['today']} today | Tot: {u['total']}")
    print(f"   {u['desc']}")

# Parse Hacker News
print("\n" + "="*50)
print("=== HACKER NEWS (Pages 1 & 2) ===")
hn_items = []
for step in ["33", "35"]:
    p = base_brain / step / "content.md"
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        rows = re.findall(r'<tr class=[\'"]athing[\'"][^>]*>.*?<span class=[\'"]titleline[\'"]><a href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>.*?</tr>\s*<tr><td class=[\'"]subtext[\'"]>(.*?)</td>', content, re.DOTALL)
        for link, title, subtext in rows:
            score = re.search(r'(\d+)\s+points', subtext)
            pts = int(score.group(1)) if score else 0
            age = re.search(r'<span class=[\'"]age[\'"][^>]*><a[^>]*>(.*?)</a>', subtext)
            time_str = age.group(1) if age else ""
            hn_items.append({"title": title, "link": link, "pts": pts, "age": time_str})

for h in sorted(hn_items, key=lambda x: x["pts"], reverse=True)[:20]:
    print(f"[{h['pts']} pts | {h['age']:10}] {h['title']}")
    print(f"   {h['link']}")

# Parse Show HN
print("\n" + "="*50)
print("=== SHOW HN (Pages 1 & 2) ===")
show_items = []
for step in ["37", "39"]:
    p = base_brain / step / "content.md"
    if p.exists():
        with open(p, "r", encoding="utf-8") as f:
            content = f.read()
        rows = re.findall(r'<tr class=[\'"]athing[\'"][^>]*>.*?<span class=[\'"]titleline[\'"]><a href=[\'"]([^\'"]+)[\'"][^>]*>(.*?)</a>.*?</tr>\s*<tr><td class=[\'"]subtext[\'"]>(.*?)</td>', content, re.DOTALL)
        for link, title, subtext in rows:
            score = re.search(r'(\d+)\s+points', subtext)
            pts = int(score.group(1)) if score else 0
            age = re.search(r'<span class=[\'"]age[\'"][^>]*><a[^>]*>(.*?)</a>', subtext)
            time_str = age.group(1) if age else ""
            show_items.append({"title": title, "link": link, "pts": pts, "age": time_str})

for s in sorted(show_items, key=lambda x: x["pts"], reverse=True)[:20]:
    print(f"[{s['pts']} pts | {s['age']:10}] {s['title']}")
    print(f"   {s['link']}")
