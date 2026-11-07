# -*- coding: utf-8 -*-
import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CANDIDATES_FILE = REPO_ROOT / "candidates_nov08.json"
SEEN_FILE = REPO_ROOT / "history_seen_projects.md"

with open(SEEN_FILE, "r", encoding="utf-8") as f:
    seen_text = f.read().lower()

# Extract seen repository slugs or project names from table
import re
seen_projects = set(re.findall(r'\*\*([a-zA-Z0-9_\.-]+(?:/[a-zA-Z0-9_\.-]+)?)\*\*', seen_text))

with open(CANDIDATES_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

main_stories_names = {
    "openmausbot", "milind-soni/openmausbot",
    "ghostty", "mitchellh/ghostty", "libghostty",
    "satmux", "th0rgal/satmux",
    "vork", "voyager-so/vork",
    "handy", "cjpais/handy"
}

def is_spam(name, desc):
    s = (name + " " + desc).lower()
    spam_terms = [
        "steam-idler", "minecraft-afk", "discord-quest", "pre-configured environment",
        "spoofer", "cheat", "aimbot", "roblox", "free-robux", "crack", "torrent",
        "uttorent", "solidworks", "soundpad", "slideshow-video-maker", "sp-flash-tool",
        "imei-repair", "discord-server-cloner", "passfab", "ios-unlocker", "fonetrans",
        "sketchup", "crypto-portfolio", "sheeridverify"
    ]
    return any(k in s for k in spam_terms)

# 1. GitHub Candidates
gh_pool = []
seen_slugs = set()
for it in data.get("gh_new", []):
    fn = it["full_name"].lower()
    short = fn.split("/")[-1]
    if fn in seen_projects or short in seen_projects:
        continue
    if any(m == fn or m == short for m in main_stories_names):
        continue
    if is_spam(it["full_name"], it.get("desc", "")):
        continue
    if "ai--manus" in fn: # Recursive cluster: ai--manus bot spam
        continue
    if short in seen_slugs:
        continue
    seen_slugs.add(short)
    gh_pool.append(it)

# Also check trending repos that might be new or not seen
for it in data.get("trending", []):
    fn = it["name"].lower()
    short = fn.split("/")[-1]
    if fn in seen_projects or short in seen_projects:
        continue
    if any(m == fn or m == short for m in main_stories_names):
        continue
    if short in seen_slugs:
        continue
    # Check if not spam
    if not is_spam(it["name"], it.get("desc", "")):
        seen_slugs.add(short)
        # assign an estimated age/velocity for bucket consideration
        gh_pool.append({
            "full_name": it["name"],
            "stars": it["stars_today"],
            "velocity": it["stars_today"] / 24.0, # estimated
            "age_h": 20.0,
            "desc": it["desc"],
            "lang": it["lang"],
            "is_trending": True
        })

b1_gh = [x for x in gh_pool if 0 <= x.get("age_h", 0) < 18]
b2_gh = [x for x in gh_pool if 18 <= x.get("age_h", 0) < 36]
b3_gh = [x for x in gh_pool if 36 <= x.get("age_h", 0) <= 56]

print("=== GITHUB BUCKET 1 (0~18h) ===")
b1_gh.sort(key=lambda x: x["velocity"], reverse=True)
for it in b1_gh[:8]:
    print(f"- {it['full_name']} (★{it['stars']}, vel: {it['velocity']:.1f}/h, age: {it.get('age_h')}h) [{it.get('lang')}]: {it['desc'][:80]}")

print("\n=== GITHUB BUCKET 2 (18~36h) ===")
b2_gh.sort(key=lambda x: x["velocity"], reverse=True)
for it in b2_gh[:8]:
    print(f"- {it['full_name']} (★{it['stars']}, vel: {it['velocity']:.1f}/h, age: {it.get('age_h')}h) [{it.get('lang')}]: {it['desc'][:80]}")

print("\n=== GITHUB BUCKET 3 (36~54h) ===")
b3_gh.sort(key=lambda x: x["velocity"], reverse=True)
for it in b3_gh[:8]:
    print(f"- {it['full_name']} (★{it['stars']}, vel: {it['velocity']:.1f}/h, age: {it.get('age_h')}h) [{it.get('lang')}]: {it['desc'][:80]}")

# 2. Hacker News Candidates
hn_pool = []
for it in data.get("hn", []):
    title = it["title"]
    url = it.get("url") or ""
    # Check if not general news or politics
    if any(k in title.lower() for k in ["tesla", "cybertruck", "ipo", "law firm", "bank", "tribe", "batteries", "grey list", "words and phrases"]):
        continue
    if any(m in title.lower() or m in url.lower() for m in main_stories_names):
        continue
    hn_pool.append(it)

b1_hn = [x for x in hn_pool if 0 <= x["age_h"] < 18]
b2_hn = [x for x in hn_pool if 18 <= x["age_h"] < 36]
b3_hn = [x for x in hn_pool if 36 <= x["age_h"] <= 56]

print("\n=== HN BUCKET 1 (0~18h) ===")
b1_hn.sort(key=lambda x: x["velocity"], reverse=True)
for it in b1_hn[:8]:
    print(f"- {it['title']} (pts: {it['points']}, vel: {it['velocity']:.1f}/h, age: {it['age_h']}h): {it['url'][:70]}")

print("\n=== HN BUCKET 2 (18~36h) ===")
b2_hn.sort(key=lambda x: x["velocity"], reverse=True)
for it in b2_hn[:8]:
    print(f"- {it['title']} (pts: {it['points']}, vel: {it['velocity']:.1f}/h, age: {it['age_h']}h): {it['url'][:70]}")

print("\n=== HN BUCKET 3 (36~54h) ===")
b3_hn.sort(key=lambda x: x["velocity"], reverse=True)
for it in b3_hn[:8]:
    print(f"- {it['title']} (pts: {it['points']}, vel: {it['velocity']:.1f}/h, age: {it['age_h']}h): {it['url'][:70]}")
