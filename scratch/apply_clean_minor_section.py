# -*- coding: utf-8 -*-
"""
Apply clean, fully HTML-escaped minor radar section to news/2026-10-22.html
"""

import sys
import html
import re
from pathlib import Path
from generate_deep_minor_section import deep_minor_items

sys.stdout.reconfigure(encoding='utf-8')

html_path = Path(r"c:\Program Files\1a\src\gitnews\news\2026-10-22.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

def clean_and_escape(text):
    lines = [line.strip() for line in text.strip().split("\n\n") if line.strip()]
    escaped_lines = [html.escape(l, quote=True) for l in lines]
    return "<br><br>".join(escaped_lines)

html_items = []
for it in deep_minor_items:
    gh_btn = f'''<a href="{it['gh_url']}" target="_blank" class="project-link github">
      <svg class="lucide" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path><path d="M9 18c-4.51 2-5-2-7-2"></path></svg>
      <span>저장소 방문하기</span>
    </a>''' if it['gh_url'] else ""

    hn_btn = f'''<a href="{it['hn_url']}" target="_blank" class="project-link youtube" style="background:#fff7ed; color:#c2410c; border-color:#ea580c;">
      <i data-lucide="message-square"></i>
      <span>Hacker News 토론보기</span>
    </a>''' if it['hn_url'] else ""

    safe_title = html.escape(it['title'], quote=True)
    safe_sub = html.escape(it['sub'], quote=True)
    safe_box_title = html.escape(it['box_title'], quote=True)
    safe_box_content = html.escape(it['box_content'], quote=True)

    comm_clean = clean_and_escape(it['community_reaction'])
    mech_clean = clean_and_escape(it['mechanism'])
    use_clean = clean_and_escape(it['use_case'])
    future_clean = clean_and_escape(it['future_outlook'])

    item_html = f'''      <!-- [{it['badge']}] {safe_title} -->
      <div class="minor-item" id="minor-{it['id']}" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge {it['badge_class']}">{it['badge']}</span>
              <span class="minor-metric">{it['stars']}</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> {it['time']}</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> {it['velocity']}</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">{safe_title}</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">{safe_sub}</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>

        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <div class="minor-detail-inner">
            <div class="minor-headline-box">
              <h3 class="minor-detail-headline">{safe_title}</h3>
              <p class="minor-detail-subheadline">{safe_sub}</p>
            </div>
            
            <div class="minor-story-body">
              <div class="minor-story-section">
                <h4 class="minor-section-tag"><i data-lucide="flame" style="color:#ef4444;"></i> 현장 상황 및 커뮤니티 반응</h4>
                <p class="minor-paragraph">{comm_clean}</p>
              </div>

              <div class="minor-story-section">
                <h4 class="minor-section-tag"><i data-lucide="cpu" style="color:#3b82f6;"></i> 핵심 기술 메커니즘</h4>
                <p class="minor-paragraph">{mech_clean}</p>
              </div>
            </div>

            <div class="minor-schematic">
              <div class="schematic-title"><i data-lucide="git-commit" class="schematic-icon"></i> {safe_box_title}</div>
              <div class="minor-box-flow">{safe_box_content}</div>
            </div>

            <div class="minor-story-body">
              <div class="minor-story-section">
                <h4 class="minor-section-tag"><i data-lucide="check-circle-2" style="color:#10b981;"></i> 실전 활용 시나리오 (어디에 써먹을까?)</h4>
                <p class="minor-paragraph">{use_clean}</p>
              </div>

              <div class="minor-story-section">
                <h4 class="minor-section-tag"><i data-lucide="trending-up" style="color:#8b5cf6;"></i> 앞으로 어떻게 될 것인가? (미래 전망 및 파급력)</h4>
                <p class="minor-paragraph">{future_clean}</p>
              </div>
            </div>

            <div class="minor-links-bar">
              {gh_btn}
              {hn_btn}
            </div>
          </div>
        </div>
      </div>'''
    html_items.append(item_html)

items_joined = "\n\n".join(html_items)

new_minor_section = f'''    <!-- ==========================================================================
         실시간 극초기 레이더 마이너 브리핑 (18선 콤팩트 줄노트 아코디언)
         ========================================================================== -->
    <section class="minor-radar-section" id="minor-radar">
      <div class="minor-items-container">
{items_joined}
      </div>
    </section>'''

# Replace section
pattern = re.compile(r'<section class="minor-radar-section".*?</section>', re.DOTALL)
if pattern.search(html_content):
    html_content = pattern.sub(new_minor_section, html_content)
    print("Replaced minor-radar-section with 100% clean, escaped HTML items!")
else:
    print("ERROR: Could not find minor-radar-section!")

# Ensure script block is clean and complete
new_script_block = """  <script>
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

    // 개별 메인 기사 카드 클릭 시 토글
    function toggleArticle(card) {
      card.classList.toggle('active');
      const actionText = card.querySelector('.article-action span');
      if (actionText) {
        actionText.textContent = card.classList.contains('active') ? '메모 접기 ▲' : '메모 펼치기';
      }
    }

    // 마이너 아코디언 아이템 토글 (클릭 시 펼침/접힘 완벽 보장)
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

    // 전체 펼치기 / 접기 버튼 (메인 기사 + 마이너 18선 전체 동시 토글)
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
  </script>"""

script_matches = list(re.finditer(r'<script>(\s*lucide\.createIcons\(\);.*?</script>)', html_content, re.DOTALL))
if script_matches:
    last_match = script_matches[-1]
    start = last_match.start()
    end = last_match.end()
    html_content = html_content[:start] + new_script_block + html_content[end:]
    print("Updated application script block!")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully saved {html_path.name}! New size: {len(html_content):,} chars")
