import subprocess
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

repos = [
    "vectorize-io/hindsight",
    "obra/superpowers",
    "valentderah/totk-pc-recomp",
    "jub0t/Concat",
    "nightly-labs/openbot",
    "KeygraphHQ/shannon",
    "beenuar/AiSOC",
    "AgriciDaniel/claude-seo",
    "Donchitos/Claude-Code-Game-Studios",
    "magnitudedev/magnitude"
]

for r in repos:
    print(f"\n{'='*60}\n=== REPO: {r} ===")
    res = subprocess.run(["gh", "repo", "view", r], capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        lines = res.stdout.splitlines()
        print("\n".join(lines[:45]))
    else:
        print(f"Error fetching {r}: {res.stderr}")
