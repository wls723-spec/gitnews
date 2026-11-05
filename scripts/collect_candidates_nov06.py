#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
collect_candidates_nov06.py
오늘자(2026-11-06) GitNews 후보군 수집 스크립트
- URL 인코딩 및 15초 타임아웃 강제 적용 (무한 행 방지)
- 네트워크/API 오류 시 최대 3회 지수 백오프 재시도
- 일부 쿼리 실패 시에도 전체 중단 없이 안전 폴백
"""
import subprocess
import urllib.request
import urllib.parse
import json
import sys
import re
import time
from pathlib import Path
from datetime import datetime, timezone, timedelta

REPO_ROOT = Path(__file__).resolve().parent.parent
SEEN_FILE = REPO_ROOT / "history_seen_projects.md"
OUTPUT_FILE = REPO_ROOT / "candidates_nov06.json"

now = datetime.now(timezone.utc)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

print(f"[*] Starting candidate collection for 2026-11-06 (Current UTC: {now.isoformat()})")

with open(SEEN_FILE, "r", encoding="utf-8") as f:
    seen_text = f.read().lower()

# ---------------------------------------------------------------------------
# 1. Fetch GitHub Trending (Daily)
# ---------------------------------------------------------------------------
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

print("[*] 1. Fetching GitHub Trending...")
for url, label in trending_urls:
    success = False
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
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
                success = True
                break
        except Exception as e:
            print(f"  [Attempt {attempt}/3] Retry {label} due to: {e}")
            time.sleep(1.5 * attempt)
    if not success:
        print(f"  ✗ Failed {label} after 3 attempts, continuing...")

# ---------------------------------------------------------------------------
# 2. Fetch GitHub Search via gh CLI with URL Encoding & 15s Timeout
# ---------------------------------------------------------------------------
since_30h = (now - timedelta(hours=30)).strftime("%Y-%m-%dT%H:%M:%SZ")
print(f"[*] 2. Fetching GitHub Search API (created:>{since_30h})...")
spam_keywords = [
    "crack", "installer", "pre-activated", "standalone setup", "full working",
    "roblox", "cheat", "aimbot", "spoofer", "driver booster", "key generator",
    "license key", "free-robux", "canva", "adobe", "autodesk", "fl studio",
    "coreldraw", "nero-platinum", "anydesk", "avid-media", "keyshot", "ibmspss",
    "dvd-creator", "axie-infinity", "bypass", "steam-wallet", "drainer"
]

gh_new_repos = []
queries = [
    f"created:>{since_30h} stars:>10",
    f"created:>{since_30h} topic:ai",
    f"created:>{since_30h} topic:agent",
    f"created:>{since_30h} topic:rust",
    f"created:>{since_30h} topic:mcp"
]

seen_names = set()

for raw_q in queries:
    # URL encode query properly (+ for space)
    encoded_q = urllib.parse.quote_plus(raw_q)
    endpoint = f"search/repositories?q={encoded_q}&sort=stars&order=desc&per_page=50"
    
    success = False
    for attempt in range(1, 4):
        try:
            cmd = ["gh", "api", endpoint]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
            if res.returncode == 0:
                data = json.loads(res.stdout)
                items = data.get("items", [])
                for it in items:
                    name = it["full_name"]
                    if name in seen_names:
                        continue
                    desc = (it.get("description") or "").lower()
                    if any(k in desc or k in name.lower() for k in spam_keywords):
                        continue
                    seen_names.add(name)
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
                success = True
                break
            else:
                print(f"  [Attempt {attempt}/3] gh api returned error: {res.stderr.strip()[:100]}")
                time.sleep(2 * attempt)
        except subprocess.TimeoutExpired:
            print(f"  [Attempt {attempt}/3] Timeout (15s) expired for query: {raw_q}")
            time.sleep(2 * attempt)
        except Exception as e:
            print(f"  [Attempt {attempt}/3] Error for query: {e}")
            time.sleep(2 * attempt)
    
    if success:
        print(f"  ✓ Processed query: {raw_q}")
    else:
        print(f"  ✗ Skipping query after 3 failed attempts: {raw_q}")

gh_new_repos.sort(key=lambda x: x["velocity"], reverse=True)

# ---------------------------------------------------------------------------
# 3. Fetch Hacker News Stories via Algolia
# ---------------------------------------------------------------------------
print("[*] 3. Fetching Hacker News Stories via Algolia...")
hn_stories = []
try:
    hn_since_ts = int((now - timedelta(hours=30)).timestamp())
    hn_url = f"https://hn.algolia.com/api/v1/search_by_date?tags=(story,show_hn)&numericFilters=points>30,created_at_i>{hn_since_ts}&hitsPerPage=100"
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(hn_url, headers=headers)
            with urllib.request.urlopen(req, timeout=12) as resp:
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
            break
        except Exception as e:
            print(f"  [Attempt {attempt}/3] HN fetch error: {e}")
            time.sleep(2 * attempt)
except Exception as e:
    print(f"  ✗ Failed HN completely: {e}")

hn_stories.sort(key=lambda x: x["velocity"], reverse=True)

# ---------------------------------------------------------------------------
# 4. Save candidates
# ---------------------------------------------------------------------------
candidates = {
    "generated_at": now.isoformat(),
    "trending": list(trending_repos.values()),
    "gh_new": gh_new_repos[:80],
    "hn": hn_stories[:60]
}

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(candidates, f, ensure_ascii=False, indent=2)

print(f"[✓] Successfully saved {len(trending_repos)} trending, {len(gh_new_repos)} new GH, {len(hn_stories)} HN candidates to {OUTPUT_FILE}")
