# -*- coding: utf-8 -*-
import urllib.request
import json
import sys
import re
from pathlib import Path
from datetime import datetime, timezone, timedelta

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

now = datetime.now(timezone.utc)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

print(f"Current UTC time: {now.isoformat()}")

seen_file = Path(r"c:\Program Files\1a\src\gitnews\history_seen_projects.md")
with open(seen_file, "r", encoding="utf-8") as f:
    seen_text = f.read().lower()

# 1. Fetch GitHub Trending
trending_urls = [
    ("https://github.com/trending?since=daily", "General (Daily)"),
    ("https://github.com/trending/python?since=daily", "Python (Daily)"),
    ("https://github.com/trending/typescript?since=daily", "TS (Daily)"),
    ("https://github.com/trending/rust?since=daily", "Rust (Daily)"),
    ("https://github.com/trending/go?since=daily", "Go (Daily)"),
    ("https://github.com/trending?since=weekly", "General (Weekly)"),
    ("https://github.com/trending/python?since=weekly", "Python (Weekly)"),
    ("https://github.com/trending/typescript?since=weekly", "TS (Weekly)"),
    ("https://github.com/trending/rust?since=weekly", "Rust (Weekly)"),
]

trending_repos = {}

def parse_trending_html(html, source_label):
    items = html.split('<article class="Box-row"')
    if len(items) > 1:
        items = ['<article class="Box-row"' + it.split('</article>')[0] + '</article>' for it in items[1:]]
    results = []
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

        stars_period = re.search(r'([0-9,]+)\s+stars\s+(?:today|this week)', it, re.IGNORECASE)
        s_period_str = stars_period.group(1) if stars_period else "0"
        s_period = int(s_period_str.replace(",", ""))

        tot_stars = re.search(r'stargazers"[^>]*>.*?([0-9,]+)', it, re.DOTALL)
        tot_str = tot_stars.group(1).strip() if tot_stars else "?"

        lang = re.search(r'itemprop="programmingLanguage">(.*?)</span>', it)
        lang_str = lang.group(1).strip() if lang else source_label.split()[0]

        results.append({
            "repo": rname,
            "lang": lang_str,
            "period_stars": s_period,
            "period_str": s_period_str,
            "total_stars": tot_str,
            "desc": desc_text,
            "source": source_label,
            "seen": rname.lower() in seen_text
        })
    return results

print("Fetching GitHub Trending pages...")
for url, label in trending_urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode('utf-8')
            res = parse_trending_html(content, label)
            for r in res:
                repo_id = r["repo"]
                if repo_id not in trending_repos or r["period_stars"] > trending_repos[repo_id]["period_stars"]:
                    trending_repos[repo_id] = r
    except Exception as e:
        print(f"Error fetching {url}: {e}")

print(f"Total trending repos found: {len(trending_repos)}")

# 2. Fetch GitHub Search API for created in dynamic window (~32h)
since_iso = (now - timedelta(hours=32)).strftime("%Y-%m-%dT%H:%M:%SZ")
gh_search_items = []
print(f"Fetching GitHub Search API for created:>{since_iso}...")
for page in [1, 2, 3, 4, 5]:
    url = f"https://api.github.com/search/repositories?q=created:>{since_iso}&sort=stars&order=desc&per_page=100&page={page}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            items = data.get('items', [])
            gh_search_items.extend(items)
            if len(items) < 100:
                break
    except Exception as e:
        print(f"GH Search API error on page {page}: {e}")
        break

print(f"Total GH Search API items: {len(gh_search_items)}")

# 3. Fetch Hacker News (via Algolia API)
print("Fetching Hacker News stories...")
hn_stories = []

since_ts = int((now - timedelta(hours=32)).timestamp())
algolia_url = f"https://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=created_at_i>{since_ts},points>15&hitsPerPage=100"
try:
    req = urllib.request.Request(algolia_url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        for hit in data.get('hits', []):
            st_time = datetime.fromtimestamp(hit.get('created_at_i', 0), tz=timezone.utc)
            age_h = max((now - st_time).total_seconds() / 3600.0, 0.0)
            pts = hit.get('points', 0)
            vel = pts / max(age_h, 0.2)
            hn_stories.append({
                "id": hit.get('objectID'),
                "title": hit.get('title'),
                "url": hit.get('url') or f"https://news.ycombinator.com/item?id={hit.get('objectID')}",
                "hn_url": f"https://news.ycombinator.com/item?id={hit.get('objectID')}",
                "points": pts,
                "comments": hit.get('num_comments', 0),
                "created_at": hit.get('created_at'),
                "age_h": age_h,
                "velocity": vel
            })
except Exception as e:
    print(f"HN Algolia API error: {e}")

print(f"Total HN stories retrieved: {len(hn_stories)}")

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")
scratch_dir.mkdir(parents=True, exist_ok=True)

with open(scratch_dir / "trending_repos_nov04.json", "w", encoding="utf-8") as f:
    json.dump(list(trending_repos.values()), f, ensure_ascii=False, indent=2)

with open(scratch_dir / "gh_search_items_nov04.json", "w", encoding="utf-8") as f:
    json.dump(gh_search_items, f, ensure_ascii=False, indent=2)

with open(scratch_dir / "hn_stories_nov04.json", "w", encoding="utf-8") as f:
    json.dump(hn_stories, f, ensure_ascii=False, indent=2)

print("Saved raw data to scratch directory successfully.")
