import urllib.request
import json
import datetime
import sys

sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0'}
now = datetime.datetime.now(datetime.timezone.utc)
ts_now = int(now.timestamp())
ts_10h = int((now - datetime.timedelta(hours=10)).timestamp())
ts_20h = int((now - datetime.timedelta(hours=20)).timestamp())
ts_30h = int((now - datetime.timedelta(hours=30)).timestamp())

def get_hn_tools(min_ts, max_ts):
    url = f'https://hn.algolia.com/api/v1/search_by_date?tags=(story,show_hn)&numericFilters=created_at_i>{min_ts},created_at_i<={max_ts},points>=10&hitsPerPage=100'
    items = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read().decode('utf-8'))['hits']
    res = []
    for it in items:
        title = it.get('title') or ''
        url_link = it.get('url') or ''
        is_show = 'show hn' in title.lower()
        is_gh = 'github.com' in url_link.lower()
        if is_show or is_gh:
            created_dt = datetime.datetime.fromtimestamp(it['created_at_i'], tz=datetime.timezone.utc)
            h = (now - created_dt).total_seconds() / 3600.0
            pts = it.get('points', 0)
            res.append({'title': title, 'pts': pts, 'h': h, 'rate': pts/max(h,0.2), 'url': url_link, 'id': it.get('objectID'), 'is_show': is_show})
    res.sort(key=lambda x: x['rate'], reverse=True)
    return res

for name, mn, mx in [('구간 1 (0~10시간 전)', ts_10h, ts_now), ('구간 2 (10~20시간 전)', ts_20h, ts_10h), ('구간 3 (20~30시간 전)', ts_30h, ts_20h)]:
    print(f"\n=== Hacker News [Show HN & 오픈소스 프로젝트] {name} ===")
    tools = get_hn_tools(mn, mx)
    for i, it in enumerate(tools[:3]):
        tag = "[Show HN]" if it['is_show'] else "[GitHub]"
        print(f"[{i+1}위] {tag} {it['title']}")
        print(f"      🔺 {it['pts']} pts | 🕒 {it['h']:.1f}시간 전 | ⚡ {it['rate']:.1f} pts/h")
        print(f"      URL: {it['url']}")
        print(f"      HN: https://news.ycombinator.com/item?id={it['id']}")
