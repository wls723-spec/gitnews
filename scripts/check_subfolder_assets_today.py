import subprocess
import json
import sys

res = subprocess.run(["gh", "api", "repos/vectorize-io/hindsight/contents/hindsight-docs/static/img"], capture_output=True, text=True, encoding="utf-8")
if res.returncode == 0:
    items = json.loads(res.stdout)
    print("Hindsight img:", [it['name'] for it in items])

res2 = subprocess.run(["gh", "api", "repos/nightly-labs/openbot/contents/apps"], capture_output=True, text=True, encoding="utf-8")
if res2.returncode == 0:
    items2 = json.loads(res2.stdout)
    print("OpenBot apps:", [it['name'] for it in items2])
