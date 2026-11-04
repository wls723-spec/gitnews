import re
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

base_brain = Path(r"C:\Users\user\.gemini\antigravity-ide\brain\14776ea4-88ef-4708-a435-2a8667c1b519\.system_generated\steps")
sources = [
    (base_brain / "31" / "content.md", "General"),
    (base_brain / "33" / "content.md", "Python"),
    (base_brain / "34" / "content.md", "TypeScript"),
    (base_brain / "35" / "content.md", "Rust"),
]

seen_file = Path(r"c:\Program Files\1a\src\gitnews\history_seen_projects.md")
with open(seen_file, "r", encoding="utf-8") as f:
    seen_text = f.read().lower()

all_repos = {}

for p, label in sources:
    if not p.exists():
        continue
    with open(p, "r", encoding="utf-8") as f:
        text = f.read()
    items = text.split('<article class="Box-row"')
    if len(items) > 1:
        items = ['<article class="Box-row"' + it.split('</article>')[0] + '</article>' for it in items[1:]]
    for it in items:
        h2_match = re.search(r'<h2[^>]*>(.*?)</h2>', it, re.DOTALL)
        rname = "unknown"
        if h2_match:
            repo_link = re.search(r'href="/([a-zA-Z0-9_\.-]+/[a-zA-Z0-9_\.-]+)"', h2_match.group(1))
            if repo_link:
                rname = repo_link.group(1)
        if rname == "unknown":
            repo_link = re.search(r'return_to=%2F([a-zA-Z0-9_\.-]+%2F[a-zA-Z0-9_\.-]+)', it)
            if repo_link:
                rname = repo_link.group(1).replace("%2F", "/")
        if rname in ["unknown", "trending/developers", "login", "features"] or rname.startswith("sponsors/"):
            continue

        desc = re.search(r'<p[^>]*class="[^"]*col-9[^"]*"[^>]*>(.*?)</p>', it, re.DOTALL)
        if not desc:
            desc = re.search(r'<p[^>]*>(.*?)</p>', it, re.DOTALL)
        desc_text = re.sub(r'<[^>]+>', '', desc.group(1)).strip() if desc else ""

        stars_today = re.search(r'([0-9,]+)\s+stars\s+today', it, re.IGNORECASE)
        s_today_str = stars_today.group(1) if stars_today else "0"
        s_today = int(s_today_str.replace(",", ""))

        tot_stars = re.search(r'stargazers"[^>]*>.*?([0-9,]+)', it, re.DOTALL)
        tot_str = tot_stars.group(1).strip() if tot_stars else "?"

        lang = re.search(r'itemprop="programmingLanguage">(.*?)</span>', it)
        lang_str = lang.group(1).strip() if lang else label

        if rname not in all_repos or s_today > all_repos[rname]["today_num"]:
            all_repos[rname] = {
                "repo": rname,
                "lang": lang_str,
                "today_num": s_today,
                "today_str": s_today_str,
                "total": tot_str,
                "desc": desc_text,
                "seen": rname.lower() in seen_text
            }

sorted_repos = sorted(all_repos.values(), key=lambda x: x["today_num"], reverse=True)
print(f"Total repos: {len(sorted_repos)}")
print("\n=== TOP 25 UNSEEN CANDIDATES ===")
unseen_count = 0
for r in sorted_repos:
    if r["seen"]:
        continue
    unseen_count += 1
    print(f"{unseen_count:2d}. {r['repo']} ({r['lang']}) : +{r['today_num']:,} today (Total: {r['total']})")
    print(f"    {r['desc']}")
    if unseen_count >= 25:
        break
