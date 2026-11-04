#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import urllib.request
import json
import sys
import re
from pathlib import Path
from datetime import datetime, timezone, timedelta

REPO_ROOT = Path(__file__).resolve().parent.parent
SEEN_FILE = REPO_ROOT / "history_seen_projects.md"
OUTPUT_FILE = REPO_ROOT / "candidates_nov05.json"

now = datetime.now(timezone.utc)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

print(f"[*] Current UTC time: {now.isoformat()}")

with open(SEEN_FILE, "r", encoding="utf-8") as f:
    seen_text = f.read().lower()

# 1. Fetch GitHub Trending
trending_urls = [
    ("https://github.com/trending?since=daily", "General (Daily)"),
    ("https://github.com/trending/python?since=daily", "Python (Daily)"),
    ("https://github.com/trending/typescript?since=daily", "TS (Daily)"),
    ("https://github.com/trending/rust?since=daily", "Rust (Daily)"),
    ("https://github.com/trending/go?since=daily", "Go (Daily)"),
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
        
        desc_match = re.search(r'<p class="col-9[^>]*>(.*?)</p>', it, re.DOTALL)
        desc = desc_match.group(1).strip() if desc_match else ""
        desc = re.sub(r'<[^>]+>', '', desc).strip()
        
        stars_today_match = re.search(r'([0-9,]+)\s+stars today', it)
        stars_today = stars_today_match.group(1).replace(",", "") if stars_today_match else "0"
        
        lang_match = re.search(r'itemprop="programmingLanguage">([^<]+)<', it)
        lang = lang_match.group(1).strip() if lang_match else "Unknown"

        results.append({
            "name": rname,
            "desc": desc,
            "stars_today": int(stars_today),
            "lang": lang,
            "source": source_label
        })
    return results

print("[*] Fetching GitHub Trending...")
for url, label in trending_urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8')
            parsed = parse_trending_html(html, label)
            for item in parsed:
                rname = item["name"]
                if rname != "unknown":
                    if rname not in trending_repos:
                        trending_repos[rname] = item
                        trending_repos[rname]["sources"] = [label]
                    else:
                        trending_repos[rname]["sources"].append(label)
                        if item["stars_today"] > trending_repos[rname]["stars_today"]:
                            trending_repos[rname]["stars_today"] = item["stars_today"]
        print(f"  ✓ Fetched {label}: {len(parsed)} items")
    except Exception as e:
        print(f"  ✗ Failed {label}: {e}")

# 2. Fetch GitHub Search via gh CLI for new repos (created > 32h)
since_30h = (now - timedelta(hours=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
print(f"[*] Fetching GitHub Search API (created:>{since_30h})...")
spam_keywords = ["crack", "installer", "pre-activated", "standalone setup", "full working", "roblox", "cheat", "aimbot", "spoofer", "driver booster", "key generator", "license key", "free-robux", "canva", "adobe", "autodesk", "fl studio", "coreldraw", "nero-platinum", "anydesk", "avid-media", "keyshot", "ibmspss", "dvd-creator", "axie-infinity"]

gh_new_repos = []
for page in [1, 2, 3]:
    cmd = ["gh", "api", f"search/repositories?q=created:>{since_30h}&sort=stars&order=desc&per_page=100&page={page}"]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        print(f"  ✗ Error on page {page}: {res.stderr}")
        break
    try:
        data = json.loads(res.stdout)
        items = data.get("items", [])
        if not items:
            break
        for it in items:
            desc = (it.get("description") or "").lower()
            name = it["full_name"].lower()
            if any(k in desc or k in name for k in spam_keywords):
                continue
            created = datetime.fromisoformat(it['created_at'].replace('Z', '+00:00'))
            age_h = max((now - created).total_seconds() / 3600.0, 0.2)
            vel = it['stargazers_count'] / age_h
            gh_new_repos.append({
                "full_name": it["full_name"],
                "stars": it["stargazers_count"],
                "age_h": round(age_h, 1),
                "velocity": round(vel, 2),
                "desc": it.get("description") or "",
                "created_at": it["created_at"],
                "lang": it.get("language") or "Unknown"
            })
    except Exception as e:
        print(f"  ✗ JSON parse error: {e}")
        break

# 3. Fetch Hacker News Top Stories & Show HN
print("[*] Fetching Hacker News Stories via Algolia...")
hn_stories = []
try:
    hn_since_ts = int((now - timedelta(hours=30)).timestamp())
    hn_url = f"https://hn.algolia.com/api/v1/search_by_date?tags=(story,show_hn)&numericFilters=points>30,created_at_i>{hn_since_ts}&hitsPerPage=100"
    req = urllib.request.Request(hn_url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        hn_data = json.loads(resp.read().decode('utf-8'))
        for hit in hn_data.get("hits", []):
            url = hit.get("url") or ""
            title = hit.get("title") or ""
            points = hit.get("points") or 0
            num_comments = hit.get("num_comments") or 0
            created_at = hit.get("created_at") or ""
            c_dt = datetime.fromisoformat(created_at.replace("Z", "+00:00"))
            age_h = max((now - c_dt).total_seconds() / 3600.0, 0.2)
            vel = points / age_h
            hn_stories.append({
                "title": title,
                "url": url,
                "points": points,
                "comments": num_comments,
                "age_h": round(age_h, 1),
                "velocity": round(vel, 2),
                "objectID": hit.get("objectID")
            })
    print(f"  ✓ Fetched HN: {len(hn_stories)} stories")
except Exception as e:
    print(f"  ✗ Failed HN: {e}")

# Save all raw candidates
candidates = {
    "generated_at": now.isoformat(),
    "trending": list(trending_repos.values()),
    "gh_new": gh_new_repos[:60],
    "hn": hn_stories[:50]
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(candidates, f, ensure_ascii=False, indent=2)

print(f"[✓] Saved {len(trending_repos)} trending, {len(gh_new_repos)} new GH, {len(hn_stories)} HN to {OUTPUT_FILE}")
