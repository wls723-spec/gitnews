import urllib.request
import json
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0'}
now = datetime.datetime.now(datetime.timezone.utc)
cutoff_30h_dt = now - datetime.timedelta(hours=30)
cutoff_30h_iso = cutoff_30h_dt.strftime('%Y-%m-%dT%H:%M:%SZ')

gh_url = f"https://api.github.com/search/repositories?q=created:%3E{cutoff_30h_iso}+stars:%3E=10&sort=stars&order=desc&per_page=100"
items = json.loads(urllib.request.urlopen(urllib.request.Request(gh_url, headers=headers)).read().decode('utf-8'))['items']

b1, b2, b3 = [], [], []
for it in items:
    name = it['full_name']
    desc = it.get('description') or ''
    if '.github' in name or 'cheat' in desc.lower() or 'aimbot' in desc.lower() or 'roblox' in desc.lower() or 'skin-changer' in desc.lower():
        continue
    created_dt = datetime.datetime.fromisoformat(it['created_at'].replace('Z', '+00:00'))
    hours = (now - created_dt).total_seconds() / 3600.0
    if hours > 30.0: continue
    stars = it['stargazers_count']
    rate = stars / max(hours, 0.2)
    entry = {'name': name, 'stars': stars, 'hours': hours, 'rate': rate, 'desc': desc, 'is_php': 'php2shell' in name.lower() or 'cve-2026' in name.lower()}
    if 0 <= hours < 10: b1.append(entry)
    elif 10 <= hours < 20: b2.append(entry)
    elif 20 <= hours <= 30: b3.append(entry)

for b in [b1, b2, b3]: b.sort(key=lambda x: x['rate'], reverse=True)

print("=== [GitHub 동일 주제(PHP 취약점) 단일화 & 고유 프로젝트 승격 결과] ===")
print("\n[구간 1 (0~10시간 전)]")
for x in [r for r in b1 if not r['is_php']][:3]:
    print(f"-> {x['name']} | ⭐ {x['stars']}개 | 🕒 {x['hours']:.1f}h | ⚡ {x['rate']:.1f}스타/h | {x['desc'][:60]}")

print("\n[구간 2 (10~20시간 전)]")
for x in [r for r in b2 if not r['is_php']][:3]:
    print(f"-> {x['name']} | ⭐ {x['stars']}개 | 🕒 {x['hours']:.1f}h | ⚡ {x['rate']:.1f}스타/h | {x['desc'][:60]}")

print("\n[구간 3 (20~30시간 전)] (1위는 PHP 비상사태 대표로 ikow 유지, 2·3위는 고유 프로젝트 승격)")
php_top = [r for r in b3 if r['is_php']][0]
print(f"-> [보안 이슈 대표] {php_top['name']} | ⭐ {php_top['stars']}개 | 🕒 {php_top['hours']:.1f}h | ⚡ {php_top['rate']:.1f}스타/h | {php_top['desc'][:60]}")
for x in [r for r in b3 if not r['is_php']][:2]:
    print(f"-> {x['name']} | ⭐ {x['stars']}개 | 🕒 {x['hours']:.1f}h | ⚡ {x['rate']:.1f}스타/h | {x['desc'][:60]}")
