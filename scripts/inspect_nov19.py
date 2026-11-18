# -*- coding: utf-8 -*-
import json
import subprocess
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parent.parent

# 1. Inspect top unseen trending candidates
trending_candidates = [
    "jingyaogong/minimind",
    "agent-substrate/substrate",
    "HKUDS/CLI-Anything",
    "google-labs-code/stitch-skills",
    "ethanplusai/sellbird",
    "XiaoYouChR/Ghost-Downloader-3",
    "cursor/plugins",
    "DeanChensj/jiangshan-map",
    "colbymchenry/codegraph",
    "esengine/estella",
    "opensandbox-group/OpenSandbox",
    "TencentCloud/CubeSandbox",
    "malisper/pgrust",
    "vercel/eve",
    "sveltejs/svelte",
]

# Also check if any trending repo was seen >14 days ago vs <=14 days ago
with open(REPO_ROOT / "history_seen_projects.md", "r", encoding="utf-8") as f:
    hist = f.read()

print("=== CHECKING TRENDING REPOS VIA GH API ===")
for repo in trending_candidates:
    res = subprocess.run(["gh", "api", f"repos/{repo}"], capture_output=True, text=True)
    if res.returncode == 0:
        d = json.loads(res.stdout)
        lic = (d.get("license") or {}).get("spdx_id") or "None"
        hp = d.get("homepage") or ""
        print(f"{repo} | stars={d.get('stargazers_count')} | license={lic} | lang={d.get('language')} | hp={hp} | created={d.get('created_at')} | updated={d.get('pushed_at')}")
        print(f"   desc: {d.get('description')}")
    else:
        print(f"{repo} | ERROR: {res.stderr.strip()[:80]}")

# 2. Check minor GH candidates (filter out spam/empty/broken repos)
minor_gh_candidates = [
    # B1 0~10h
    "mitsuhiko/tvpipe",
    "padmk/bruse",
    "OlehDatsyk/accessiscan-ai",
    "3d3dcanada/stella-scope-community",
    "Spartakusovec/apogee",
    "krmbzds/phrack-tui",
    "Eric031212/agent-ringleader",
    "haseeb-heaven/e-journal",
    "padmk/backstage",
    "feoren/hangar-server",
    "D3XSIM/kalkan",
    "Arta48/termind-desktop",
    "THZoria/NX2_Firmware",
    "bogdan239/uberdesigner-studio",
    # B2 10~20h
    "sfewer-r7/CVE-2026-123007",
    "geerlingguy/chronytop",
    "pookjw/Clocky",
    "eddiezywang/wemail",
    "howznguyen/phonedesk",
    "Nova-Silicon/AnalogLayoutWorld",
    "codewith-aditya/metaphor-bridge",
    "r-a-y-z-e-r/ecp5_emu",
    "fakawangzhan/bookworm-cloudflare",
    "ntu0831/mini-agent",
    # B3 20~30h
    "ChrisTitusTech/lg-debloat",
    "ikow/java4shell-poc",
    "comp-work/gke-sandboxes",
    "shaarmander/mobicats-jewels",
    "Tpojka/neleceni",
    "trbrnt/Veil",
    "apple-aiml-research/ml-fastframes",
    "Dipshet/GracemeriaRecomp",
    "Ssbullock/pcb-layout-llm",
    "behzadea12/Paqet-Panel",
    "JL-GUO/skill-siphon",
]

print("\n=== CHECKING MINOR GH REPOS VIA GH API ===")
for repo in minor_gh_candidates:
    res = subprocess.run(["gh", "api", f"repos/{repo}"], capture_output=True, text=True)
    if res.returncode == 0:
        d = json.loads(res.stdout)
        lic = (d.get("license") or {}).get("spdx_id") or "None"
        sz = d.get("size", 0)
        print(f"{repo} | ★{d.get('stargazers_count')} | size={sz}KB | lic={lic} | lang={d.get('language')} | hp={d.get('homepage') or ''} | desc={(d.get('description') or '')[:90]}")
    else:
        print(f"{repo} | ERROR")
