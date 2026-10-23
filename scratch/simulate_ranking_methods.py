import urllib.request
import json
import datetime
import sys
import math

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0'}
now = datetime.datetime.now(datetime.timezone.utc)
cutoff = (now - datetime.timedelta(hours=24)).strftime('%Y-%m-%dT%H:%M:%SZ')
url = f'https://api.github.com/search/repositories?q=created:%3E{cutoff}+stars:%3E=20&sort=stars&order=desc&per_page=50'

req = urllib.request.Request(url, headers=headers)
items = json.loads(urllib.request.urlopen(req).read().decode('utf-8'))['items']

scored = []
for it in items:
    name = it['full_name']
    desc = it.get('description') or ''
    # 스팸 필터
    if '.github' in name or 'cheat' in desc.lower() or 'aimbot' in desc.lower() or 'roblox' in desc.lower() or 'cve-2026' in name.lower() or 'php2shell' in name.lower():
        continue
    stars = it['stargazers_count']
    created_dt = datetime.datetime.fromisoformat(it['created_at'].replace('Z', '+00:00'))
    hours = max((now - created_dt).total_seconds() / 3600, 0.1)
    
    # 1. 단순 속도 (Velocity) = stars / (hours + 0.5)
    velocity = stars / (hours + 0.5)
    
    # 2. Hacker News Gravity = stars / (hours + 2)^1.5
    hn_score = stars / math.pow(hours + 2, 1.5)
    
    scored.append({
        'name': name,
        'stars': stars,
        'hours': hours,
        'velocity': velocity,
        'hn_score': hn_score,
        'desc': desc
    })

print("=== [공식 1: Hacker News Time-Decay Gravity 점수 순] ===")
scored.sort(key=lambda x: x['hn_score'], reverse=True)
for i, s in enumerate(scored[:5]):
    print(f"[{i+1}] {s['name']} | ⭐ {s['stars']}개 | 🕒 {s['hours']:.1f}시간 전 | 속도: {s['velocity']:.1f}스타/h | 점수: {s['hn_score']:.2f}")
    print(f"    설명: {s['desc'][:80]}")

print("\n=== [공식 2: 단순 시간당 속도 (Velocity) 순] ===")
scored.sort(key=lambda x: x['velocity'], reverse=True)
for i, s in enumerate(scored[:5]):
    print(f"[{i+1}] {s['name']} | ⭐ {s['stars']}개 | 🕒 {s['hours']:.1f}시간 전 | 속도: {s['velocity']:.1f}스타/h")
    print(f"    설명: {s['desc'][:80]}")

print("\n=== [공식 3: 시간대별 리그제 (Time Buckets)] ===")
# 0~6시간, 6~14시간, 14~24시간
b1 = [s for s in scored if s['hours'] <= 8]
b2 = [s for s in scored if 8 < s['hours'] <= 16]
b3 = [s for s in scored if s['hours'] > 16]

b1.sort(key=lambda x: x['stars'], reverse=True)
b2.sort(key=lambda x: x['stars'], reverse=True)
b3.sort(key=lambda x: x['stars'], reverse=True)

print("🥇 [극초신성 리그: 0~8시간 이내 생성 중 최고 스타]")
if b1:
    print(f"   -> {b1[0]['name']} | ⭐ {b1[0]['stars']}개 | {b1[0]['hours']:.1f}시간 전 | {b1[0]['desc'][:80]}")
else:
    print("   -> 해당 시간대 후보 없음")

print("🥈 [급상승 리그: 8~16시간 이내 생성 중 최고 스타]")
if b2:
    print(f"   -> {b2[0]['name']} | ⭐ {b2[0]['stars']}개 | {b2[0]['hours']:.1f}시간 전 | {b2[0]['desc'][:80]}")

print("🥉 [안정형 리그: 16~24시간 이내 생성 중 최고 스타]")
if b3:
    print(f"   -> {b3[0]['name']} | ⭐ {b3[0]['stars']}개 | {b3[0]['hours']:.1f}시간 전 | {b3[0]['desc'][:80]}")
