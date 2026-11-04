#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
publish_site.py - GitNews 데일리 오픈소스 & AI 트렌드 자동 배포 및 아카이브 네비게이터 동기화 스크립트

역할:
1. news/ 디렉토리 내의 모든 YYYY-MM-DD.html 파일을 검색하여 최신순으로 정렬
2. 가장 최신 뉴스를 루트의 index.html로 배포 (메인 화면)
3. 모든 뉴스 페이지 최하단에 [📅 지난 뉴스 모아보기 (Past Issues)] 아카이브 네비게이터를 자동으로 생성 및 주입
4. index.html 및 news/*.html 간 상대 경로를 올바르게 연결
"""

import os
import re
import sys
from pathlib import Path

# Windows UTF-8 출력 보정
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parent.parent
NEWS_DIR = REPO_ROOT / "news"
INDEX_FILE = REPO_ROOT / "index.html"

# 아카이브 섹션 시작/끝 주석 마커
ARCHIVE_START_MARKER = "<!-- ========================================================== -->\n    <!-- [ARCHIVE NAVIGATOR START] 지난 호 모아보기 -->"
ARCHIVE_END_MARKER = "<!-- [ARCHIVE NAVIGATOR END] -->\n    <!-- ========================================================== -->"

def get_issue_dates():
    """news/ 폴더의 모든 YYYY-MM-DD.html 파일 날짜를 최신순으로 추출"""
    pattern = re.compile(r"^(\d{4}-\d{2}-\d{2})\.html$")
    dates = []
    for file_path in NEWS_DIR.glob("*.html"):
        m = pattern.match(file_path.name)
        if m:
            dates.append(m.group(1))
    dates.sort(reverse=True)
    return dates

def build_archive_html(current_date, is_index=False, all_dates=None):
    """
    현재 테마(memo_theme.css)에 어울리는 감성적인 아카이브 네비게이터 HTML 블록 생성
    """
    if all_dates is None:
        all_dates = []

    latest_date = all_dates[0] if all_dates else ""
    total_issues = len(all_dates)

    pills_html = []
    for d in all_dates:
        is_today = (d == latest_date)
        is_active = (d == current_date)

        # 링크 경로 계산
        if is_index:
            href = "./index.html" if is_today else f"./news/{d}.html"
        else:
            href = "../index.html" if is_today else f"./{d}.html"

        # 라벨 및 뱃지
        badge = " ⭐ 최신호" if is_today else ""
        active_class = " active-issue" if is_active else ""

        pills_html.append(f"""          <a href="{href}" class="archive-pill{active_class}" title="{d} 발행호 읽기">
            <span class="pill-date">{d}</span>{badge}
          </a>""")

    pills_rendered = "\n".join(pills_html)

    return f"""{ARCHIVE_START_MARKER}
    <section class="archive-navigator" id="past-issues">
      <style>
        .archive-navigator {{
          margin: 3.5rem 0 2rem 0;
          padding: 1.75rem 2rem;
          background: #fbf9f4;
          border: 2px dashed #d1d5db;
          border-radius: 12px;
          position: relative;
        }}
        .archive-header {{
          display: flex;
          align-items: center;
          justify-content: space-between;
          margin-bottom: 1.25rem;
          padding-bottom: 0.75rem;
          border-bottom: 2px solid #e5e7eb;
        }}
        .archive-title {{
          font-family: 'Gowun Dodum', sans-serif;
          font-size: 1.15rem;
          font-weight: 700;
          color: #1f2937;
          display: flex;
          align-items: center;
          gap: 0.5rem;
        }}
        .archive-meta-badge {{
          font-size: 0.8rem;
          font-weight: 600;
          color: #6b7280;
          background: rgba(0,0,0,0.05);
          padding: 0.25rem 0.65rem;
          border-radius: 9999px;
        }}
        .archive-grid {{
          display: flex;
          flex-wrap: wrap;
          gap: 0.65rem;
          align-items: center;
        }}
        .archive-pill {{
          display: inline-flex;
          align-items: center;
          gap: 0.35rem;
          padding: 0.45rem 0.95rem;
          background: #ffffff;
          color: #374151;
          font-family: 'Gowun Dodum', sans-serif;
          font-size: 0.9rem;
          font-weight: 600;
          text-decoration: none;
          border: 1.5px solid #e5e7eb;
          border-radius: 8px;
          box-shadow: 0 1px 2px rgba(0,0,0,0.04);
          transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .archive-pill:hover {{
          border-color: #f59e0b;
          color: #d97706;
          background: #fffbeb;
          transform: translateY(-2px);
          box-shadow: 0 4px 6px -1px rgba(245, 158, 11, 0.15);
        }}
        .archive-pill.active-issue {{
          background: #1f2937;
          color: #ffffff;
          border-color: #1f2937;
          font-weight: 700;
          box-shadow: 0 2px 4px rgba(31, 41, 55, 0.25);
        }}
        .archive-pill.active-issue:hover {{
          background: #374151;
          color: #fef08a;
          border-color: #374151;
        }}
        .archive-pill .pill-date {{
          font-variant-numeric: tabular-nums;
          letter-spacing: 0.02em;
        }}
      </style>
      
      <div class="archive-header">
        <div class="archive-title">
          <span>📅 지난 호 모아보기 (Past Issues)</span>
        </div>
        <span class="archive-meta-badge">총 {total_issues}회 발행 완료</span>
      </div>

      <div class="archive-grid">
{pills_rendered}
      </div>
    </section>
    {ARCHIVE_END_MARKER}"""

def inject_or_replace_archive(html_content, archive_html):
    """
    기존 아카이브 마커가 있으면 교체하고, 없으면 </div> <!-- .container --> 직전에 삽입
    """
    # 1. 이미 아카이브 마커가 존재하는 경우 교체
    pattern = re.compile(
        rf"{re.escape(ARCHIVE_START_MARKER)}.*?{re.escape(ARCHIVE_END_MARKER)}",
        re.DOTALL
    )
    if pattern.search(html_content):
        return pattern.sub(archive_html, html_content)

    # 2. 컨테이너 닫는 태그 직전에 삽입
    container_end_patterns = [
        r"(\s*</div>\s*<!--\s*\.container\s*-->)",
        r"(\s*</div>\s*<!--\s*container\s*-->)",
        r"(</div>\s*<script)"
    ]
    for p in container_end_patterns:
        match = re.search(p, html_content, re.IGNORECASE)
        if match:
            idx = match.start(1)
            return html_content[:idx] + "\n\n    " + archive_html + "\n" + html_content[idx:]

    # 3. 못 찾을 경우 </body> 직전에 삽입
    body_idx = html_content.find("</body>")
    if body_idx != -1:
        return html_content[:body_idx] + "\n" + archive_html + "\n" + html_content[body_idx:]

    return html_content + "\n" + archive_html

def publish():
    print("=" * 60)
    print("🚀 GitNews 웹 배포 및 지난 호 아카이브 동기화 시작")
    print("=" * 60)

    dates = get_issue_dates()
    if not dates:
        print("[ERROR] news/ 디렉토리에 YYYY-MM-DD.html 파일이 없습니다.")
        sys.exit(1)

    latest_date = dates[0]
    print(f"[*] 총 {len(dates)}개의 발행본 발견: {dates}")
    print(f"[*] 최신 발행본: {latest_date}")

    # 1. 루트 index.html 생성 (최신 기사 기반)
    latest_file = NEWS_DIR / f"{latest_date}.html"
    with open(latest_file, "r", encoding="utf-8") as f:
        latest_content = f.read()

    index_archive_html = build_archive_html(current_date=latest_date, is_index=True, all_dates=dates)
    index_content = inject_or_replace_archive(latest_content, index_archive_html)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"[✓] 메인 index.html 생성 완료! (최신: {latest_date})")

    # 2. news/*.html 모든 파일에 아카이브 네비게이터 동기화
    updated_count = 0
    for d in dates:
        news_file = NEWS_DIR / f"{d}.html"
        with open(news_file, "r", encoding="utf-8") as f:
            content = f.read()

        news_archive_html = build_archive_html(current_date=d, is_index=False, all_dates=dates)
        new_content = inject_or_replace_archive(content, news_archive_html)

        if new_content != content:
            with open(news_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated_count += 1

    print(f"[✓] news/ 아카이브 네비게이터 동기화 완료: {updated_count}개 파일 업데이트")
    print("=" * 60)
    print("🎉 웹 배포 준비가 성공적으로 완료되었습니다!")
    print(f"👉 로컬 메인: file://{INDEX_FILE}")
    print("=" * 60)

if __name__ == "__main__":
    publish()
