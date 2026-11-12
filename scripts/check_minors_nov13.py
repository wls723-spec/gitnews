import json
from pathlib import Path

with open("history_seen_projects.md", "r", encoding="utf-8") as f:
    seen = f.read().lower()

with open("candidates_nov13.json", "r", encoding="utf-8") as f:
    cand = json.load(f)

# Main 5 stories to exclude
main_slugs = ["super-odyssey-pc-recomp", "open-orange", "zigzag", "relax", "stela"]

def is_seen(name):
    n = name.lower()
    return n in seen or any(s in n for s in main_slugs)

# Buckets
b1_gh, b2_gh, b3_gh = [], [], []
b1_hn, b2_hn, b3_hn = [], [], []

# Filter out spam repositories in GitHub new
spam_keywords = ["rpocket", "respocket", "resp-", "cheat", "aimbot", "spoofer", "keygen", "crack", "torrent", "free-robux", "setup-guide", "blooket", "deadlock", "driver-booster"]

for it in cand["gh_new"]:
    name = it["full_name"]
    desc = (it["desc"] or "").lower()
    if is_seen(name):
        continue
    if any(k in name.lower() or k in desc for k in spam_keywords):
        continue
    age = it["age_h"]
    if age < 10:
        b1_gh.append(it)
    elif age < 20:
        b2_gh.append(it)
    elif age <= 30:
        b3_gh.append(it)

for it in cand["hn"]:
    title = it["title"]
    url = it["url"] or ""
    if is_seen(title) or is_seen(url):
        continue
    age = it["age_h"]
    if age < 10:
        b1_hn.append(it)
    elif age < 20:
        b2_hn.append(it)
    elif age <= 30:
        b3_hn.append(it)

print(f"GH Pool (Clean): B1={len(b1_gh)}, B2={len(b2_gh)}, B3={len(b3_gh)}")
print(f"HN Pool: B1={len(b1_hn)}, B2={len(b2_hn)}, B3={len(b3_hn)}")

print("\n--- Top GH B1 (0~10h) ---")
for x in b1_gh[:10]:
    print(f"  {x['full_name']} (★{x['stars']}, vel={x['velocity']}, age={x['age_h']}h): {x['desc'][:80]}")

print("\n--- Top GH B2 (10~20h) ---")
for x in b2_gh[:10]:
    print(f"  {x['full_name']} (★{x['stars']}, vel={x['velocity']}, age={x['age_h']}h): {x['desc'][:80]}")

print("\n--- Top GH B3 (20~30h) ---")
for x in b3_gh[:10]:
    print(f"  {x['full_name']} (★{x['stars']}, vel={x['velocity']}, age={x['age_h']}h): {x['desc'][:80]}")

print("\n--- Top HN B1 (0~10h) ---")
for x in b1_hn[:10]:
    print(f"  {x['title']} (pts={x['points']}, vel={x['velocity']}, age={x['age_h']}h): {x['url'][:70]}")

print("\n--- Top HN B2 (10~20h) ---")
for x in b2_hn[:10]:
    print(f"  {x['title']} (pts={x['points']}, vel={x['velocity']}, age={x['age_h']}h): {x['url'][:70]}")

print("\n--- Top HN B3 (20~30h) ---")
for x in b3_hn[:10]:
    print(f"  {x['title']} (pts={x['points']}, vel={x['velocity']}, age={x['age_h']}h): {x['url'][:70]}")
