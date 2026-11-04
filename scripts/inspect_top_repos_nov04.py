# -*- coding: utf-8 -*-
import subprocess
import json
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

candidates = [
    "karpathy/nanochat",
    "p-e-w/heretic",
    "floci-io/floci",
    "FlashML-org/FreeToken",
    "pingdotgg/t3code",
    "KeygraphHQ/shannon",
    "cjpais/Handy",
    "Crosstalk-Solutions/project-nomad",
    "D4Vinci/Scrapling",
    "mattpocock/skills",
    "NVIDIA/auto-ontology",
    "lexmount/moli",
    "milind-soni/OpenMausBot"
]

for repo in candidates:
    print(f"\n{'='*70}\nREPO: {repo}\n{'='*70}")
    res = subprocess.run(["gh", "repo", "view", repo, "--json", "name,owner,description,stargazerCount,url,homepageUrl,openGraphImageUrl"], capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        info = json.loads(res.stdout)
        print(f"Name: {info.get('name')} | Owner: {info.get('owner', {}).get('login')} | Stars: {info.get('stargazerCount')}")
        print(f"Desc: {info.get('description')}")
        print(f"Homepage: {info.get('homepageUrl')}")
        print(f"OG Image: {info.get('openGraphImageUrl')}")
        
        # Get first 30 lines of README
        res_readme = subprocess.run(["gh", "repo", "view", repo], capture_output=True, text=True, encoding="utf-8")
        readme_lines = res_readme.stdout.splitlines()[:25]
        print("--- README PREVIEW ---")
        print("\n".join(readme_lines))
    else:
        print(f"Error fetching {repo}: {res.stderr.strip()}")
