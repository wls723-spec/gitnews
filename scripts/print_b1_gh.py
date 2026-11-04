# -*- coding: utf-8 -*-
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, str(Path(__file__).resolve().parent))
import process_minors_nov03 as pm

print(f"Bucket 1 (0~10h) has {len(pm.b1_gh)} items:")
for i, r in enumerate(pm.b1_gh[:10]):
    print(f"  {i+1}. {r['full_name']} ({r['language']}) | {r['stars']} stars | {r['age_h']:.1f}h | Vel: {r['velocity']:.1f}/h")
    print(f"     {r['description']}")
