# -*- coding: utf-8 -*-
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

REPO_ROOT = Path(__file__).resolve().parent.parent
CANDIDATES_FILE = REPO_ROOT / "candidates_nov08.json"
SEEN_FILE = REPO_ROOT / "history_seen_projects.md"

with open(SEEN_FILE, "r", encoding="utf-8") as f:
    seen = f.read().lower()

with open(CANDIDATES_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Main 5 stories slugs/names to exclude from minors
main_stories_names = {
    "milind-soni/openmausbot", "openmausbot",
    "mitchellh/ghostty", "libghostty", "ghostty",
    "th0rgal/satmux", "satmux",
    "voyager-so/vork", "vork",
    "cjpais/handy", "handy"
}

def is_excluded(name):
    n = name.lower()
    if n in seen or any(s in seen for s in n.split("/")):
        return True
    if any(m in n for m in main_stories_names):
        return True
    # Filter out spam
    spam = ["steam-idler", "minecraft-afk", "discord-quest", "crypto", "unlocker", "crack", "torrent", "fonetrans", "solidworks", "soundpad", "sheerid"]
    if any(s in n for s in spam):
        return True
    return False

# Buckets: 0~18h, 18~36h, 36~54h
b1_gh, b2_gh, b3_gh = [], [], []
for it in data.get("gh_new", []):
    name = it["full_name"]
    if is_excluded(name):
        continue
    age = it["age_h"]
    if 0 <= age < 18:
        b1_gh.append(it)
    elif 18 <= age < 36:
        b2_gh.append(it)
    elif 36 <= age <= 56:
        b3_gh.append(it)

# Also check trending repos with ages or velocity if needed
print("=== GITHUB BUCKET 1 (0~18h) ===")
b1_gh.sort(key=lambda x: x["velocity"], reverse=True)
for it in b1_gh[:10]:
    print(f"- {it['full_name']} (★{it['stars']}, vel: {it['velocity']}/h, age: {it['age_h']}h): {it['desc'][:70]}")

print("\n=== GITHUB BUCKET 2 (18~36h) ===")
b2_gh.sort(key=lambda x: x["velocity"], reverse=True)
for it in b2_gh[:10]:
    print(f"- {it['full_name']} (★{it['stars']}, vel: {it['velocity']}/h, age: {it['age_h']}h): {it['desc'][:70]}")

print("\n=== GITHUB BUCKET 3 (36~54h) ===")
b3_gh.sort(key=lambda x: x["velocity"], reverse=True)
for it in b3_gh[:10]:
    print(f"- {it['full_name']} (★{it['stars']}, vel: {it['velocity']}/h, age: {it['age_h']}h): {it['desc'][:70]}")

# HN Buckets
b1_hn, b2_hn, b3_hn = [], [], []
for it in data.get("hn", []):
    title = it["title"]
    url = it.get("url") or ""
    if is_excluded(title) or is_excluded(url):
        continue
    # Filter generic news, only tech/open-source/eng
    age = it["age_h"]
    if 0 <= age < 18:
        b1_hn.append(it)
    elif 18 <= age < 36:
        b2_hn.append(it)
    elif 36 <= age <= 56:
        b3_hn.append(it)

print("\n=== HN BUCKET 1 (0~18h) ===")
b1_hn.sort(key=lambda x: x["velocity"], reverse=True)
for it in b1_hn[:10]:
    print(f"- {it['title']} (pts: {it['points']}, vel: {it['velocity']}/h, age: {it['age_h']}h): {it['url'][:60]}")

print("\n=== HN BUCKET 2 (18~36h) ===")
b2_hn.sort(key=lambda x: x["velocity"], reverse=True)
for it in b2_hn[:10]:
    print(f"- {it['title']} (pts: {it['points']}, vel: {it['velocity']}/h, age: {it['age_h']}h): {it['url'][:60]}")

print("\n=== HN BUCKET 3 (36~54h) ===")
b3_hn.sort(key=lambda x: x["velocity"], reverse=True)
for it in b3_hn[:10]:
    print(f"- {it['title']} (pts: {it['points']}, vel: {it['velocity']}/h, age: {it['age_h']}h): {it['url'][:60]}")
