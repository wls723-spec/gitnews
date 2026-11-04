import os
import sys
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.story1_gstack import STORY_1_HTML
from scripts.story2_sandbox import STORY_2_HTML
from scripts.story3_experiential import STORY_3_HTML
from scripts.story4_claudemem import STORY_4_HTML
from scripts.story5_videouse import STORY_5_HTML
from scripts.minors_data_oct26 import FULL_MINORS_SECTION

out_path = Path(r"c:\Program Files\1a\src\gitnews\news\2026-10-26.html")
out_path.parent.mkdir(parents=True, exist_ok=True)

masthead_html = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>GitNews 데일리 오픈소스 & AI 트렌드 | 2026-10-26</title>
  
  <link rel="stylesheet" href="../assets/css/memo_theme.css">
  <script src="../assets/libs/lucide.min.js"></script>
  <script src="../assets/libs/rough.min.js"></script>
  <script src="../assets/libs/rough-notation.js"></script>
</head>
<body>
  <div class="container">
    
    <!-- 간결하고 세련된 신문 제호(Masthead) 헤더 -->
    <header class="header-hero">
      <h1 class="site-title">GitNews 데일리 오픈소스 & AI 트렌드</h1>
    </header>

    <!-- 피드 제어 바 -->
    <div class="feed-controls" style="justify-content: flex-end;">
      <button class="btn-toggle-all" onclick="toggleAllArticles()">
        <i data-lucide="layers"></i> <span id="toggle-all-text">전체 메모 펼치기</span>
      </button>
    </div>

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
      const isExpanded = item.classList.contains('active');
      const btn = item.querySelector('.minor-toggle-btn');
      const btnText = item.querySelector('.minor-btn-text');
      if (btn) btn.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
      if (btnText) {
        btnText.textContent = isExpanded ? '메모 접기 ▲' : '메모 펼치기';
      }
    }

    // 전체 펼치기 / 접기 버튼 (메인 5개 + 마이너 18개 전체 일괄 제어)
    let allExpanded = false;
    function toggleAllArticles() {
      allExpanded = !allExpanded;
      const cards = document.querySelectorAll('.article-card');
      const minorItems = document.querySelectorAll('.minor-item');
      const toggleText = document.getElementById('toggle-all-text');
      
      cards.forEach(card => {
        const actionText = card.querySelector('.article-action span');
        if (allExpanded) {
          card.classList.add('active');
          if (actionText) actionText.textContent = '메모 접기 ▲';
        } else {
          card.classList.remove('active');
          if (actionText) actionText.textContent = '메모 펼치기';
        }
      });

      minorItems.forEach(item => {
        const btn = item.querySelector('.minor-toggle-btn');
        const btnText = item.querySelector('.minor-btn-text');
        if (allExpanded) {
          item.classList.add('active');
          if (btn) btn.setAttribute('aria-expanded', 'true');
          if (btnText) btnText.textContent = '메모 접기 ▲';
        } else {
          item.classList.remove('active');
          if (btn) btn.setAttribute('aria-expanded', 'false');
          if (btnText) btnText.textContent = '메모 펼치기';
        }
      });

      if (toggleText) {
        toggleText.textContent = allExpanded ? '전체 메모 접기' : '전체 메모 펼치기';
      }
    }
  </script>
</body>
</html>
"""

full_html = masthead_html + STORY_1_HTML + STORY_2_HTML + STORY_3_HTML + STORY_4_HTML + STORY_5_HTML + footer_scripts_html

with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Successfully generated initial HTML {out_path} ({len(full_html):,} characters)")
