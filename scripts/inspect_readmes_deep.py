# -*- coding: utf-8 -*-
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = Path(r"c:\Program Files\1a\src\gitnews\scratch")

tags = ["nanochat", "heretic", "t3code", "floci", "shannon"]

for tag in tags:
    fpath = scratch_dir / f"readme_{tag}.md"
    if fpath.exists():
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()
        print(f"\n{'='*60}\nTAG: {tag} ({len(text)} chars)\n{'='*60}")
        # Print first 50 lines
        lines = text.splitlines()[:45]
        print("\n".join(lines))
