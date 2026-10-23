import urllib.request
import json
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
now = datetime.datetime.now(datetime.timezone.utc)

cutoff_10h_dt = now - datetime.timedelta(hours=10)
cutoff_20h_dt = now - datetime.timedelta(hours=20)
cutoff_30h_dt = now - datetime.timedelta(hours=30)

ts_now = int(now.timestamp())
ts_10h = int(cutoff_10h_dt.timestamp())
ts_20h = int(cutoff_20h_dt.timestamp())
ts_30h = int(cutoff_30h_dt.timestamp())

# ==============================================================================
# 1. GITHUB REPOSITORIES (30시간)
# ==============================================================================
print("GitHub 30시간 데이터 수집 중...")
gh_items = []
# 100개씩 2페이지 가져오기
for page in [1, 2]:
    gh_url = f"https://api.github.com/search/repositories?q=created:%3E{cutoff_30h_dt.strftime('%Y-%m-%dT%H:%M:%SZ')}+stars:%3E=10&sort=stars&order=desc&per_page=100&page={page}"
    try:
        req = urllib.request.Request(gh_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            d = json.loads(resp.read().decode('utf-8'))
            gh_items.extend(d.get('items', []))
    except Exception as e:
        print(f"GH Error page {page}: {e}")

def is_spam(repo):
    name = repo.get('full_name', '').lower()
    desc = (repo.get('description') or '').lower()
    if '.github' in name or 'cheat' in desc or 'aimbot' in desc or 'hack' in desc or 'roblox' in desc or 'skin-changer' in desc:
        return True
    return False

gh_list = []
for it in gh_items:
    if is_spam(it):
        continue
    created_dt = datetime.datetime.fromisoformat(it['created_at'].replace('Z', '+00:00'))
    hours = (now - created_dt).total_seconds() / 3600.0
    if hours > 30.0:
        continue
    stars = it['stargazers_count']
    rate = stars / max(hours, 0.2)
    gh_list.append({
        'name': it['full_name'],
        'stars': stars,
        'hours': hours,
        'rate': rate,
        'url': it['html_url'],
        'desc': it.get('description') or 'No description',
        'lang': it.get('language') or 'Unknown'
    })

# ==============================================================================
# 2. HACKER NEWS STORIES (각 10시간 구간별 정밀 쿼리)
# ==============================================================================
print("Hacker News 각 구간별 정밀 수집 중...")

def fetch_hn(min_ts, max_ts):
    items = []
    # story, show_hn 태그
    url = f"https://hn.algolia.com/api/v1/search_by_date?tags=(story,show_hn)&numericFilters=created_at_i>{min_ts},created_at_i<={max_ts},points>=10&hitsPerPage=100"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            d = json.loads(resp.read().decode('utf-8'))
            items = d.get('hits', [])
    except Exception as e:
        print(f"HN Error ({min_ts}~{max_ts}): {e}")
    
    parsed = []
    for it in items:
        created_dt = datetime.datetime.fromtimestamp(it['created_at_i'], tz=datetime.timezone.utc)
        hours = (now - created_dt).total_seconds() / 3600.0
        points = it.get('points', 0)
        rate = points / max(hours, 0.2)
        parsed.append({
            'title': it.get('title', ''),
            'points': points,
            'comments': it.get('num_comments', 0),
            'hours': hours,
            'rate': rate,
            'url': it.get('url') or '',
            'hn_url': f"https://news.ycombinator.com/item?id={it.get('objectID')}",
            'is_show': 'show hn' in it.get('title', '').lower(),
            'is_gh': 'github.com' in (it.get('url') or '').lower()
        })
    parsed.sort(key=lambda x: x['rate'], reverse=True)
    return parsed

hn_b1 = fetch_hn(ts_10h, ts_now)
hn_b2 = fetch_hn(ts_20h, ts_10h)
hn_b3 = fetch_hn(ts_30h, ts_20h)

# ==============================================================================
# 출력 함수
# ==============================================================================
print("\n" + "#"*80)
print("🚀 [GITHUB] 30시간 3분할 (각 10h) x 시간당 Star 증가율 Top 3 (총 9개)")
print("#"*80)

def display_gh_section(title, min_h, max_h):
    subset = [r for r in gh_list if min_h <= r['hours'] < max_h]
    subset.sort(key=lambda x: x['rate'], reverse=True)
    print(f"\n📌 {title} (후보 {len(subset)}개 중 1~3위)")
    print("-" * 75)
    for i, r in enumerate(subset[:3]):
        print(f"  [{i+1}위] {r['name']} ({r['lang']})")
        print(f"       ⭐ {r['stars']:,}개 | 🕒 {r['hours']:.1f}시간 전 생성 | ⚡ 시간당 {r['rate']:.1f} 스타/h")
        print(f"       링크: {r['url']}")
        print(f"       설명: {r['desc'][:90]}")
    
    # 만약 php2shell 중복 제외 대안이 있다면 보여주기
    non_cve = [r for r in subset if 'php2shell' not in r['name'].lower() and 'cve-2026' not in r['name'].lower()]
    if non_cve and any('php2shell' in r['name'].lower() for r in subset[:3]):
        print(f"       💡 [소프트웨어/도구 1위 대안]: {non_cve[0]['name']} (⭐ {non_cve[0]['stars']}개, ⚡ {non_cve[0]['rate']:.1f}스타/h)")

display_gh_section("구간 1: 갓 태어난 극초신성 (0 ~ 10시간 전 생성)", 0, 10)
display_gh_section("구간 2: 검증된 급상승 로켓 (10 ~ 20시간 전 생성)", 10, 20)
display_gh_section("구간 3: 하루 누적 챔피언 (20 ~ 30시간 전 생성)", 20, 30)

print("\n" + "#"*80)
print("💬 [HACKER NEWS] 30시간 3분할 (각 10h) x 시간당 Upvote 증가율 Top 3 (총 9개)")
print("#"*80)

def display_hn_section(title, bucket):
    print(f"\n📌 {title} (후보 {len(bucket)}개 중 1~3위)")
    print("-" * 75)
    for i, r in enumerate(bucket[:3]):
        tag = "[Show HN]" if r['is_show'] else ("[GitHub]" if r['is_gh'] else "[Story]")
        print(f"  [{i+1}위] {tag} {r['title']}")
        print(f"       🔺 {r['points']} pts (💬 {r['comments']}) | 🕒 {r['hours']:.1f}시간 전 등록 | ⚡ 시간당 {r['rate']:.1f} 업보트/h")
        print(f"       링크: {r['url']}")
        print(f"       HN토론: {r['hn_url']}")

display_hn_section("구간 1: 방금 불붙은 화제작 (0 ~ 10시간 전 등록)", hn_b1)
display_hn_section("구간 2: 반나절 열풍 토론 (10 ~ 20시간 전 등록)", hn_b2)
display_hn_section("구간 3: 하루 누적 탑스토리 (20 ~ 30시간 전 등록)", hn_b3)
