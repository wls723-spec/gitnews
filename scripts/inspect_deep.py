import urllib.request
import json
import sys
import os

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

repos = [
    "NVIDIA/OpenShell",
    "genspark-ai/genoffice",
    "anthropics/knowledge-work-plugins",
    "twentyhq/twenty",
    "shiyu-coder/Kronos",
    "trycua/cua",
    "max-sixty/worktrunk",
    "CopilotKit/OpenBot",
    "HKUDS/Vibe-Trading",
    "bowenliang123/dsh-context",
    "firecrawl/firecrawl",
    "oosexgang/hackios-xnu-kernel"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

for r in repos:
    print(f"\n==================== {r} ====================")
    # 1. API check
    api_url = f"https://api.github.com/repos/{r}"
    try:
        req = urllib.request.Request(api_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"Stars: {data.get('stargazers_count'):,} | Forks: {data.get('forks_count'):,} | Default Branch: {data.get('default_branch')}")
            print(f"Desc: {data.get('description')}")
            print(f"Homepage: {data.get('homepage')}")
            print(f"Topics: {data.get('topics')}")
            default_branch = data.get('default_branch', 'main')
    except Exception as e:
        print(f"API failed ({e}), trying raw...")
        default_branch = "main"

    # 2. Raw README
    for branch in [default_branch, "master", "main"]:
        found = False
        for name in ["README.md", "readme.md", "README.MD"]:
            raw_url = f"https://raw.githubusercontent.com/{r}/{branch}/{name}"
            try:
                req = urllib.request.Request(raw_url, headers=headers)
                with urllib.request.urlopen(req, timeout=5) as resp:
                    txt = resp.read().decode('utf-8', errors='ignore')
                    print(f"--- README ({branch}/{name}, {len(txt)} chars) ---")
                    lines = [ln for ln in txt.split('\n') if ln.strip()]
                    for ln in lines[:25]:
                        print("  ", ln[:120])
                    found = True
                    break
            except Exception:
                pass
        if found:
            break
