# -*- coding: utf-8 -*-
import urllib.request
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
urls = [
    'https://agent-browser.dev/desktop',
    'https://anoma.ly/hex',
    'https://github.com/Donchitos/Claude-Code-Game-Studios'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as r:
            html = r.read().decode('utf-8', errors='ignore')
            og = re.findall(r'<meta[^>]+property=[\'"]og:image[\'"][^>]+content=[\'"]([^\'"]+)[\'"]', html)
            if not og:
                og = re.findall(r'<meta[^>]+content=[\'"]([^\'"]+)[\'"][^>]+property=[\'"]og:image[\'"]', html)
            print(f"URL {u}: OG={og}")
    except Exception as e:
        print(f"URL {u} failed: {e}")
