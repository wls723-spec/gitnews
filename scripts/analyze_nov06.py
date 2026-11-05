# -*- coding: utf-8 -*-
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SEEN_FILE = REPO_ROOT / "history_seen_projects.md"
CANDIDATES_FILE = REPO_ROOT / "candidates_nov06.json"

with open(SEEN_FILE, "r", encoding="utf-8") as f:
    seen = f.read().lower()

with open(CANDIDATES_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

print("=== 1. TOP UNSEEN TRENDING ===")
unseen_trending = []
for it in data.get("trending", []):
    name = it["name"]
    short_name = name.split("/")[-1].lower()
    if name.lower() not in seen and short_name not in seen:
        unseen_trending.append(it)

unseen_trending.sort(key=lambda x: x["stars_today"], reverse=True)
for it in unseen_trending[:15]:
    desc = it["desc"][:80]
    print(f"- {it['name']} (★{it['stars_today']} today) [{it['lang']}]: {desc}")

print("\n=== 2. TOP UNSEEN NEW GITHUB REPOS (By Velocity) ===")
unseen_gh = []
for it in data.get("gh_new", []):
    name = it["full_name"]
    short_name = name.split("/")[-1].lower()
    if name.lower() not in seen and short_name not in seen:
        unseen_gh.append(it)

unseen_gh.sort(key=lambda x: x["velocity"], reverse=True)
for it in unseen_gh[:15]:
    desc = it["desc"][:80]
    print(f"- {it['full_name']} (★{it['stars']}, vel: {it['velocity']}/h, age: {it['age_h']}h) [{it['lang']}]: {desc}")

print("\n=== 3. TOP HACKER NEWS STORIES (By Points / Velocity) ===")
hn_list = data.get("hn", [])
hn_list.sort(key=lambda x: x["points"], reverse=True)
for it in hn_list[:15]:
    title = it["title"][:80]
    print(f"- {title} (pts: {it['points']}, vel: {it['velocity']}/h): {it['url'][:60]}")
