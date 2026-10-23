import urllib.request
import json
import datetime
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

now = datetime.datetime.now(datetime.timezone.utc)
cutoff_48h_iso = (now - datetime.timedelta(hours=48)).strftime('%Y-%m-%dT%H:%M:%SZ')
cutoff_24h_ts = int((now - datetime.timedelta(hours=24)).timestamp())

print(f"=== 실행 기준 시각 (UTC): {now.strftime('%Y-%m-%d %H:%M:%S')} ===")
print(f"1. GitHub 48시간 기준: {cutoff_48h_iso} 이후 생성")
print(f"2. Hacker News 24시간 기준: {datetime.datetime.fromtimestamp(cutoff_24h_ts, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} 이후, points >= 30\n")

# -------------------------------------------------------------
# 1. GitHub Search API
# -------------------------------------------------------------
print("--------------------------------------------------")
print("[1] GitHub Search API 조회")
print("--------------------------------------------------")

gh_url = f"https://api.github.com/search/repositories?q=created:%3E{cutoff_48h_iso}+stars:%3E=50&sort=stars&order=desc&per_page=100"
gh_repos = []
try:
    req = urllib.request.Request(gh_url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        gh_data = json.loads(resp.read().decode('utf-8'))
        total_count = gh_data.get('total_count', 0)
        items = gh_data.get('items', [])
        print(f"GitHub 결과: 총 {total_count}개 저장소 발견 (가져온 개수: {len(items)}개)")
        for it in items:
            gh_repos.append({
                "name": it.get('full_name'),
                "url": it.get('html_url'),
                "stars": it.get('stargazers_count'),
                "forks": it.get('forks_count'),
                "created_at": it.get('created_at'),
                "description": it.get('description'),
                "language": it.get('language')
            })
except Exception as e:
    print(f"GitHub API Error: {e}")

# 만약 50개 기준 말고 다른 기준(30개, 20개)도 비교 통계 확인
for threshold in [100, 50, 30, 20]:
    cnt_url = f"https://api.github.com/search/repositories?q=created:%3E{cutoff_48h_iso}+stars:%3E={threshold}&per_page=1"
    try:
        req = urllib.request.Request(cnt_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            d = json.loads(resp.read().decode('utf-8'))
            print(f"  * [참고] 최근 48시간 내 생성 & Stars >= {threshold}: 총 {d.get('total_count', 0)}개")
    except Exception as e:
        pass

print("\n--- GitHub Stars >= 50 상세 목록 ---")
for i, r in enumerate(gh_repos):
    print(f"[{i+1}] {r['name']} ({r['language']}) - ⭐ {r['stars']}개 | Forks: {r['forks']}")
    print(f"    생성일: {r['created_at']} | 링크: {r['url']}")
    print(f"    설명: {r['description']}")

# -------------------------------------------------------------
# 2. Hacker News Algolia API
# -------------------------------------------------------------
print("\n--------------------------------------------------")
print("[2] Hacker News (최근 24시간, Upvotes/Points >= 30)")
print("--------------------------------------------------")

# A) Show HN 먼저 조회
hn_show_url = f"https://hn.algolia.com/api/v1/search_by_date?tags=show_hn&numericFilters=created_at_i>{cutoff_24h_ts},points>=30&hitsPerPage=100"
hn_shows = []
try:
    req = urllib.request.Request(hn_show_url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        d = json.loads(resp.read().decode('utf-8'))
        hn_shows = d.get('hits', [])
        print(f"Show HN 결과: 총 {len(hn_shows)}개 (points >= 30)")
except Exception as e:
    print(f"Hacker News Show HN Error: {e}")

print("\n--- Show HN (Points >= 30) 목록 ---")
for i, h in enumerate(hn_shows):
    created = datetime.datetime.fromtimestamp(h.get('created_at_i', 0), tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')
    print(f"[{i+1}] {h.get('title')} (🔺 {h.get('points')} pts, 💬 {h.get('num_comments')} comments)")
    print(f"    등록: {created} UTC | URL: {h.get('url')}")
    print(f"    HN 링크: https://news.ycombinator.com/item?id={h.get('objectID')}")

# B) 전체 Story 중 Points >= 30 & URL이 github.com 이거나 오픈소스 관련인 것
hn_story_url = f"https://hn.algolia.com/api/v1/search_by_date?tags=story&numericFilters=created_at_i>{cutoff_24h_ts},points>=30&hitsPerPage=100"
hn_stories_github = []
try:
    req = urllib.request.Request(hn_story_url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        d = json.loads(resp.read().decode('utf-8'))
        all_stories = d.get('hits', [])
        print(f"\n전체 HN Story 중 Points >= 30: 총 {len(all_stories)}개")
        for s in all_stories:
            url = s.get('url', '') or ''
            title = s.get('title', '') or ''
            if 'github.com' in url.lower() or 'show hn' in title.lower():
                hn_stories_github.append(s)
        print(f"  -> 그 중 GitHub 링크 또는 Show HN 관련: {len(hn_stories_github)}개")
except Exception as e:
    print(f"Hacker News Story Error: {e}")

print("\n--- HN Story 중 GitHub 링크 포함 목록 ---")
for i, h in enumerate(hn_stories_github):
    created = datetime.datetime.fromtimestamp(h.get('created_at_i', 0), tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M')
    print(f"[{i+1}] {h.get('title')} (🔺 {h.get('points')} pts, 💬 {h.get('num_comments')} comments)")
    print(f"    등록: {created} UTC | URL: {h.get('url')}")
    print(f"    HN 링크: https://news.ycombinator.com/item?id={h.get('objectID')}")
