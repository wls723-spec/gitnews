# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.story1_llama_modchip import STORY_1_HTML
from scripts.story2_herdr import STORY_2_HTML
from scripts.story3_video_shotcraft import STORY_3_HTML
from scripts.story4_project_nomad import STORY_4_HTML
from scripts.story5_oh_my_pi import STORY_5_HTML
from scripts.minors_data_nov09 import FULL_MINORS_SECTION

out_path = REPO_ROOT / "news" / "2026-11-09.html"
out_path.parent.mkdir(parents=True, exist_ok=True)

masthead_html = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GitNews 데일리 오픈소스 & AI 트렌드 | 2026-11-09</title>
  
  <link rel="stylesheet" href="../assets/css/memo_theme.css">
  <script src="../assets/libs/lucide.min.js"></script>
  <script src="../assets/libs/rough.min.js"></script>
  <script src="../assets/libs/rough-notation.js"></script>
</head>
<body>
  <div class="container">
    
    <!-- 간결하고 세련된 신문 제호(Masthead) 헤더 -->
    <header class="header-hero">
      <div class="masthead-container" style="display:inline-flex; flex-direction:column; align-items:flex-end; max-width:100%;">
        <h1 class="site-title" style="margin-bottom:0.25rem;">GitNews 데일리 오픈소스 & AI 트렌드</h1>
        <div class="site-date-sub" style="font-family:'Gowun Dodum', var(--font-hand, sans-serif); font-size:1.05rem; font-weight:700; color:#4b5563; letter-spacing:0.02em; display:inline-flex; align-items:center; gap:0.35rem; padding-right:0.35rem;">
          <i data-lucide="calendar" style="width:15px;height:15px;color:#f59e0b;"></i> 2026-11-09 발행
        </div>
      </div>
    </header>

    <!-- 메인 5대 기사 피드 그리드 -->
    <div class="news-grid">
"""

footer_scripts_html = """
    </div> <!-- .news-grid -->

    <!-- Section 9 Minor Radar -->
""" + FULL_MINORS_SECTION + """

  </div> <!-- .container -->

  <script>
    lucide.createIcons();

    // Rough Notation 손글씨 하이라이트 & 손그림 밑줄
    window.addEventListener('DOMContentLoaded', () => {
      try {
        if (window.RoughNotation) {
          const title = document.getElementById('hero-title');
          if (title) {
            const annotation = RoughNotation.annotate(title, {
              type: 'underline',
              color: '#f59e0b',
              strokeWidth: 4,
              iterations: 2
            });
            annotation.show();
          }

          document.querySelectorAll('.editorial-quote strong').forEach((el, idx) => {
            if (idx < 6) {
              const a = RoughNotation.annotate(el, {
                type: 'highlight',
                color: '#fef08a',
                multiline: true,
                iterations: 1
              });
              a.show();
            }
          });
        }
      } catch (e) {
        console.warn('RoughNotation init error:', e);
      }
    });

    // 메인 5대 기사 아코디언 토글 (상호 배타 없음, 개별 토글)
    function toggleArticle(card) {
      card.classList.toggle('active');
      const actionText = card.querySelector('.article-action span');
      if (actionText) {
        actionText.textContent = card.classList.contains('active') ? '메모 접기 ▲' : '메모 펼치기';
      }
    }

    // 마이너 아코디언 토글
    function toggleMinorItem(item) {
      item.classList.toggle('active');
      const btnText = item.querySelector('.minor-btn-text');
      const toggleBtn = item.querySelector('.minor-toggle-btn');
      const isExpanded = item.classList.contains('active');
      if (btnText) {
        btnText.textContent = isExpanded ? '메모 접기 ▲' : '메모 펼치기';
      }
      if (toggleBtn) {
        toggleBtn.setAttribute('aria-expanded', isExpanded);
      }
    }
  </script>
</body>
</html>
"""

full_html = masthead_html + STORY_1_HTML + STORY_2_HTML + STORY_3_HTML + STORY_4_HTML + STORY_5_HTML + footer_scripts_html

with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"✓ Successfully generated: {out_path} ({len(full_html):,} bytes)")
