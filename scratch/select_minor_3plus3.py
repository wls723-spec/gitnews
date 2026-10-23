import urllib.request
import json
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')
headers = {'User-Agent': 'Mozilla/5.0'}

now = datetime.datetime.now(datetime.timezone.utc)
cutoff_48h = (now - datetime.timedelta(hours=48)).strftime('%Y-%m-%dT%H:%M:%SZ')
cutoff_24h_ts = int((now - datetime.timedelta(hours=24)).timestamp())

print(f"=== 기준 시각 (UTC): {now.strftime('%Y-%m-%d %H:%M:%S')} ===")
print(f"GitHub: {cutoff_48h} 이후 생성")
print(f"Hacker News: {datetime.datetime.fromtimestamp(cutoff_24h_ts, tz=datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S')} 이후\n")

# 1. GitHub 최근 48시간 스타 상위 20개 가져오기
gh_url = f"https://api.github.com/search/repositories?q=created:%3E{cutoff_48h}+stars:%3E=50&sort=stars&order=desc&per_page=30"
gh_items = []
try:
    req = urllib.request.Request(gh_url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        gh_data = json.loads(resp.read().decode('utf-8'))
        gh_items = gh_data.get('items', [])
except Exception as e:
    print(f"GitHub Error: {e}")

# 스팸/단순 PoC 복붙 필터링 플래그
def is_valid_project(repo):
    name = repo.get('full_name', '').lower()
    desc = (repo.get('description') or '').lower()
    # 게임 핵, 스팸 .github 레포
    if '.github' in name or 'cheat' in desc or 'aimbot' in desc or 'hack' in desc or 'roblox' in desc:
        return False
    # 보안 PoC는 연구용으로 유효할 수 있지만 단발성 exploit 보다는 실질적 오픈소스 프로젝트를 우선
    return True

print("=== [GitHub 상위 후보군 (생성 48시간 이내, 스타 순)] ===")
valid_gh = [r for r in gh_items if is_valid_project(r)]
for i, r in enumerate(valid_gh[:10]):
    created_dt = datetime.datetime.fromisoformat(r['created_at'].replace('Z', '+00:00'))
    hours_ago = (now - created_dt).total_seconds() / 3600
    print(f"[{i+1}] {r['full_name']} ({r.get('language')}) | ⭐ {r['stargazers_count']:,}개 | {hours_ago:.1f}시간 전 생성 ({r['created_at'][:16]})")
    print(f"    URL: {r['html_url']}")
    print(f"    설명: {r.get('description')}\n")

# 2. Hacker News 최근 24시간 보트 상위 가져오기
# Show HN + 일반 GitHub 링크 스토리 모두 포함하여 points 순 정렬
hn_url = f"https://hn.algolia.com/api/v1/search_by_date?tags=(story,show_hn)&numericFilters=created_at_i>{cutoff_24h_ts},points>=20&hitsPerPage=100"
hn_hits = []
try:
    req = urllib.request.Request(hn_url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        d = json.loads(resp.read().decode('utf-8'))
        hn_hits = d.get('hits', [])
except Exception as e:
    print(f"HN Error: {e}")

# 중복 제거 및 points 높은 순 정렬
hn_hits.sort(key=lambda x: x.get('points', 0), reverse=True)

print("=== [Hacker News 상위 후보군 (최근 24시간, Upvote 순)] ===")
# Show HN 및 GitHub/오픈소스 프로젝트 중심
hn_candidates = []
for h in hn_hits:
    url = h.get('url') or ''
    title = h.get('title') or ''
    is_show = 'show hn' in title.lower()
    is_gh = 'github.com' in url.lower()
    
    # Show HN이거나, GitHub 프로젝트 링크인 경우
    if is_show or is_gh:
        hn_candidates.append(h)

for i, h in enumerate(hn_candidates[:10]):
    created_dt = datetime.datetime.fromtimestamp(h['created_at_i'], tz=datetime.timezone.utc)
    hours_ago = (now - created_dt).total_seconds() / 3600
    print(f"[{i+1}] {h.get('title')} | 🔺 {h.get('points')} pts (💬 {h.get('num_comments')}) | {hours_ago:.1f}시간 전 등록")
    print(f"    URL: {h.get('url')}")
    print(f"    HN: https://news.ycombinator.com/item?id={h.get('objectID')}\n")
