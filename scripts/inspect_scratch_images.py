import os
from PIL import Image

scratch_dir = r"c:\Program Files\1a\src\gitnews\scratch"
for f in os.listdir(scratch_dir):
    p = os.path.join(scratch_dir, f)
    if os.path.isfile(p):
        try:
            im = Image.open(p)
            print(f"{f:30}: {im.size}, mode={im.mode}")
        except Exception as e:
            print(f"{f:30}: not an image ({e})")
