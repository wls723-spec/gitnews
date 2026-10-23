with open('news/2026-10-22.html', 'rb') as f:
    raw = f.read()

import re
matches = [m.start() for m in re.finditer(b'toggleMinorItem', raw)]
for m in matches:
    print('Raw bytes near toggleMinorItem:')
    print(raw[m-50:m+300])
