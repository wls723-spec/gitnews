import json
from pathlib import Path

with open("history_seen_projects.md", "r", encoding="utf-8") as f:
    seen = f.read().lower()

with open("candidates_nov05.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== TOP TRENDING (UNSEEN) ===")
unseen_trending = []
for it in data["trending"]:
    name = it["name"]
    short_name = name.split("/")[-1].lower()
    if name.lower() not in seen and short_name not in seen:
        unseen_trending.append(it)

unseen_trending.sort(key=lambda x: x["stars_today"], reverse=True)
for it in unseen_trending[:15]:
    desc = it["desc"][:75]
    print(f"- {it['name']} (★{it['stars_today']} today) [{it['lang']}]: {desc}")

print("\n=== TOP NEW GITHUB REPOS (UNSEEN) ===")
unseen_gh = []
for it in data["gh_new"]:
    name = it["full_name"]
    short_name = name.split("/")[-1].lower()
    if name.lower() not in seen and short_name not in seen:
        unseen_gh.append(it)

unseen_gh.sort(key=lambda x: x["velocity"], reverse=True)
for it in unseen_gh[:15]:
    desc = it["desc"][:75]
    print(f"- {it['full_name']} (★{it['stars']}, vel: {it['velocity']}/h, age: {it['age_h']}h): {desc}")

print("\n=== TOP HN STORIES ===")
for it in data["hn"][:15]:
    title = it["title"][:75]
    print(f"- {title} (pts: {it['points']}, vel: {it['velocity']}/h): {it['url'][:60]}")
