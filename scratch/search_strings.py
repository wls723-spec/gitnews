import os

targets = [
    '데일리 오픈소스 필드 메모',
    '손으로 끄적이듯 정리한 심층 기술 메모입니다',
    '심층 르포 기사 수록',
    '테크 저널리즘 인텔리전스 데스크',
    '손글씨 심층 메모 읽기'
]

for root, dirs, files in os.walk(r'c:\Program Files\1a\src\gitnews'):
    if 'scratch' in root or '.git' in root:
        continue
    for f in files:
        if f.endswith(('.html', '.md', '.js', '.css')):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                for t in targets:
                    if t in c:
                        print(f'{os.path.relpath(path, r"c:\Program Files\1a\src\gitnews")}: contains "{t}"')
