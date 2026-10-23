#!/usr/bin/env python3
"""
시각화 라이브러리 앙상블 관리 및 자동 다운로더
(Mermaid, ECharts, Prism, Lucide, Rough, KaTeX 등)
"""

import os
import sys
import argparse
import urllib.request

# 기본 시각화 라이브러리 앙상블 목록 (CDN -> 로컬 저장)
DEFAULT_LIBRARIES = {
    # 1. 다이어그램 & 아키텍처
    "mermaid.min.js": "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js",
    # 2. 벤치마크 & 지표 비교 차트
    "echarts.min.js": "https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js",
    # 3. 손그림 감성 스케치
    "rough.min.js": "https://cdn.jsdelivr.net/npm/roughjs@4.5.2/bundled/rough.js",
    # 4. 코드 하이라이팅 (Prism.js + Theme)
    "prism.min.js": "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js",
    "prism-python.min.js": "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js",
    "prism-bash.min.js": "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-bash.min.js",
    "prism-tomorrow.min.css": "https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css",
    # 5. 모던 테크 아이콘
    "lucide.min.js": "https://cdn.jsdelivr.net/npm/lucide@latest/dist/umd/lucide.min.js",
    # 6. AI 논문 수식 렌더링 (KaTeX)
    "katex.min.js": "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js",
    "katex.min.css": "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css",
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBS_DIR = os.path.join(BASE_DIR, "assets", "libs")

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)

def download_file(filename, url, target_dir):
    ensure_dir(target_dir)
    target_path = os.path.join(target_dir, filename)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    print(f"[*] Downloading {filename} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as res, open(target_path, "wb") as f:
            f.write(res.read())
        print(f"[+] Successfully saved: {target_path} ({os.path.getsize(target_path)} bytes)")
        return True
    except Exception as e:
        print(f"[-] Failed to download {filename}: {e}", file=sys.stderr)
        return False

def sync_defaults():
    print(f"=== 시각화 앙상블 라이브러리 전체 동기화 시작 -> {LIBS_DIR} ===")
    success_count = 0
    for filename, url in DEFAULT_LIBRARIES.items():
        if download_file(filename, url, LIBS_DIR):
            success_count += 1
    print(f"=== 완료: {success_count}/{len(DEFAULT_LIBRARIES)} 개 라이브러리 준비 완료 ===")

def main():
    parser = argparse.ArgumentParser(description="Visual Libs Ensemble Manager")
    parser.add_argument("--sync", action="store_true", help="Download all default ensemble libraries")
    parser.add_argument("--add", nargs=2, metavar=("FILENAME", "URL"), help="Add and download a custom library (e.g. chart.min.js https://...)")
    parser.add_argument("--list", action="store_true", help="List installed libraries")
    
    args = parser.parse_args()
    
    if args.add:
        filename, url = args.add
        download_file(filename, url, LIBS_DIR)
    elif args.list:
        if os.path.exists(LIBS_DIR):
            files = os.listdir(LIBS_DIR)
            print(f"Installed in {LIBS_DIR}:")
            for f in files:
                sz = os.path.getsize(os.path.join(LIBS_DIR, f))
                print(f" - {f} ({sz // 1024} KB)")
        else:
            print("No libraries downloaded yet.")
    else:
        sync_defaults()

if __name__ == "__main__":
    main()
