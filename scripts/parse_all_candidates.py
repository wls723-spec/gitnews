import re
import sys
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

# Seen projects
with open(r"c:\Program Files\1a\src\gitnews\history_seen_projects.md", "r", encoding="utf-8") as f:
    seen_text = f.read()

sources = [
    (r"C:\Users\user\.gemini\antigravity-ide\brain\8fed1fc9-481c-4212-8a51-f4b0a91a41b7\.system_generated\steps\25\content.md", "General"),
    (r"C:\Users\user\.gemini\antigravity-ide\brain\8fed1fc9-481c-4212-8a51-f4b0a91a41b7\.system_generated\steps\35\content.md", "Python"),
    (r"C:\Users\user\.gemini\antigravity-ide\brain\8fed1fc9-481c-4212-8a51-f4b0a91a41b7\.system_generated\steps\37\content.md", "TypeScript"),
    (r"C:\Users\user\.gemini\antigravity-ide\brain\8fed1fc9-481c-4212-8a51-f4b0a91a41b7\.system_generated\steps\39\content.md", "Rust"),
]

all_repos = {}
for path, label in sources:
    for item in parse_trending_file(path, label):
        r = item["repo"]
        if r != "unknown" and r not in all_repos:
            all_repos[r] = item

print(f"=== Total unique repos discovered: {len(all_repos)} ===")
unseen = []
for r, info in all_repos.items():
    is_seen = r.lower() in seen_text.lower()
    flag = "[SEEN]" if is_seen else "[NEW!]"
    if not is_seen:
        unseen.append(info)
    print(f"{flag:7} {info['repo']} ({info['lang']}) | +{info['today']} today | Tot: {info['total']}")
    print(f"        {info['desc'][:100]}")

print(f"\n=== NEW CANDIDATES ({len(unseen)}) ===")
for u in unseen:
    print(f"-> {u['repo']} ({u['lang']}) : +{u['today']} today | Tot: {u['total']}")
    print(f"   {u['desc']}")
