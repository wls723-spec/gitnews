# -*- coding: utf-8 -*-
import urllib.request
import json
import sys
import os

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def check_repo(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}"
    readme_url = f"https://api.github.com/repos/{repo_full_name}/readme"
    print(f"\n==========================================")
    print(f"Checking: {repo_full_name}")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"Stars: {data.get('stargazers_count'):,} | Forks: {data.get('forks_count'):,}")
            print(f"Desc: {data.get('description')}")
            print(f"Homepage: {data.get('homepage')}")
            print(f"Language: {data.get('language')}")
            print(f"Topics: {data.get('topics')}")
            print(f"Created: {data.get('created_at')} | Updated: {data.get('updated_at')}")
    except Exception as e:
        print(f"Error fetching repo info: {e}")

    try:
        req = urllib.request.Request(readme_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            rdata = json.loads(resp.read().decode('utf-8'))
            import base64
            content = base64.b64decode(rdata.get('content', '')).decode('utf-8', errors='ignore')
            print(f"--- README Preview (first 1000 chars) ---")
            print(content[:1000])
    except Exception as e:
        print(f"Error fetching README: {e}")

repos_to_check = [
    "deepseek-ai/dsh-superagent-prototype",
    "ashayas/icloud-s3",
    "affaan-m/ECC",
    "beenuar/AiSOC",
    "patch-gg/pixelfx",
    "Leonxlnx/taste-skill",
    "Arjun-Ingole/hop",
    "pollen-robotics/microduck",
    "arpanjot-coding/AVault",
    "anomalyco/hex"
]

for r in repos_to_check:
    check_repo(r)
