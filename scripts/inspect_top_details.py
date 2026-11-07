# -*- coding: utf-8 -*-
import subprocess
import json

repos = [
    "mitchellh/ghostty",
    "cjpais/Handy",
    "milind-soni/OpenMausBot",
    "blader/humanizer",
    "AgriciDaniel/claude-seo",
    "Vincentwei1021/video-shotcraft",
    "sostenesfreitas/ocarina-recomp",
    "voyager-so/vork",
    "Th0rgal/satmux",
    "herdrdev/herdr",
    "multica-ai/multica",
    "can1357/oh-my-pi",
    "lfnovo/open-notebook",
    "leepokai/Codync",
]

for r in repos:
    cmd = ["gh", "api", f"repos/{r}"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        data = json.loads(res.stdout)
        print(f"=== {r} ===")
        print(f"Stars: {data.get('stargazers_count')} | Forks: {data.get('forks_count')} | Created: {data.get('created_at')} | Lang: {data.get('language')}")
        print(f"Desc: {data.get('description')}")
        print(f"Homepage: {data.get('homepage')}")
    else:
        print(f"=== {r} FAILED ===")
