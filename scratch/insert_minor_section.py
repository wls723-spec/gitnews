# -*- coding: utf-8 -*-
import sys
import re
from pathlib import Path
from build_minor_section import minor_items

sys.stdout.reconfigure(encoding='utf-8')

html_path = Path(r"c:\Program Files\1a\src\gitnews\news\2026-10-22.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# 1. Minor Section CSS
minor_css = """
/* ==========================================================================
   MINOR EMERGING RADAR SECTION (18 Items Minimal Accordion List)
   실시간 극초기 레이더 마이너 브리핑 (18선 콤팩트 줄노트 아코디언)
   ========================================================================== */
.minor-radar-section {
  margin-top: 4rem;
  padding-top: 2.5rem;
  border-top: 3px dashed var(--border-sketch);
}

.minor-radar-header {
  margin-bottom: 2rem;
}

.minor-title-group {
  display: flex;
  align-items: center;
  gap: 0.85rem;
  flex-wrap: wrap;
  margin-bottom: 0.75rem;
}

.minor-section-title {
  font-family: var(--font-title);
  font-size: 2rem;
  font-weight: 700;
  color: var(--ink-primary);
  line-height: 1.3;
}

.minor-section-desc {
  font-family: var(--font-body);
  font-size: 1.05rem;
  color: var(--ink-secondary);
  line-height: 1.6;
}

.minor-items-container {
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}

.minor-item {
  background: var(--bg-card);
  border: 1.8px solid var(--border-sketch);
  border-radius: var(--sketch-border-sm);
  box-shadow: 3px 3.5px 0px var(--border-sketch);
  transition: all 0.2s ease;
  overflow: hidden;
}

.minor-item:hover {
  border-color: #0f172a;
  box-shadow: 4px 5px 0px var(--border-sketch);
}

.minor-item.active {
  background: #ffffff;
  border-color: #b45309;
  box-shadow: 4px 5px 0px #b45309;
}

.minor-summary-bar {
  padding: 0.95rem 1.25rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  user-select: none;
  background: #ffffff;
  transition: background-color 0.15s ease;
}

.minor-summary-bar:hover {
  background-color: #fefce8;
}

.minor-summary-left {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  flex: 1;
  min-width: 0;
}

.minor-meta-badges {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.minor-badge {
  font-family: var(--font-hand);
  font-size: 0.95rem;
  font-weight: 700;
  padding: 0.15rem 0.55rem;
  border-radius: var(--sketch-border-sm);
  border: 1.2px solid var(--border-sketch);
  line-height: 1.2;
}

.minor-badge.badge-gh {
  background: #f3e8ff;
  color: #6b21a8;
  border-color: #9333ea;
}

.minor-badge.badge-hn {
  background: #ffedd5;
  color: #c2410c;
  border-color: #ea580c;
}

.minor-metric {
  font-family: var(--font-body);
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--ink-primary);
  background: #f1f5f9;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
}

.minor-time, .minor-velocity {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  font-family: var(--font-body);
  font-size: 0.88rem;
  color: var(--ink-secondary);
}

.minor-icon {
  width: 14px;
  height: 14px;
}

.minor-title-line {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  font-size: 1.05rem;
  color: var(--ink-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.minor-repo-name {
  font-family: var(--font-title);
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
  flex-shrink: 0;
}

.minor-dash {
  color: #94a3b8;
  flex-shrink: 0;
}

.minor-summary-text {
  font-family: var(--font-body);
  font-size: 0.98rem;
  color: #475569;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.minor-summary-right {
  flex-shrink: 0;
}

.minor-toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  background: #fff;
  border: 1.5px solid var(--border-sketch);
  border-radius: var(--sketch-border-sm);
  padding: 0.35rem 0.75rem;
  font-family: var(--font-hand);
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--ink-primary);
  cursor: pointer;
  box-shadow: 2px 2px 0px var(--border-sketch);
  transition: all 0.15s ease;
}

.minor-toggle-btn:hover {
  background: #f8fafc;
  transform: translate(-1px, -1px);
  box-shadow: 3px 3px 0px var(--border-sketch);
}

.minor-toggle-icon {
  width: 16px;
  height: 16px;
  transition: transform 0.2s ease;
}

.minor-item.active .minor-toggle-icon {
  transform: rotate(180deg);
}

.minor-detail-content {
  display: none;
  padding: 1.5rem 1.6rem;
  background: #faf8f5;
  border-top: 1.5px dashed var(--border-sketch);
}

.minor-item.active .minor-detail-content {
  display: block;
  animation: minorFadeIn 0.25s ease-out;
}

@keyframes minorFadeIn {
  from { opacity: 0; transform: translateY(-4px); }
  to { opacity: 1; transform: translateY(0); }
}

.minor-detail-headline {
  font-family: var(--font-title);
  font-size: 1.5rem;
  font-weight: 700;
  color: #0f172a;
  margin-bottom: 1rem;
  line-height: 1.35;
}

.minor-story-body {
  margin-bottom: 1.25rem;
}

.minor-paragraph {
  font-family: var(--font-body);
  font-size: 1.02rem;
  color: #334155;
  line-height: 1.75;
  margin-bottom: 0.75rem;
}

.minor-schematic {
  margin: 1.25rem 0;
  background: #ffffff;
  border: 1.5px solid var(--border-sketch);
  border-radius: var(--sketch-border-sm);
  padding: 1.1rem 1.3rem;
  box-shadow: 3px 3px 0px rgba(0,0,0,0.06);
}

.minor-box-flow {
  font-family: var(--font-body);
  font-size: 0.98rem;
  line-height: 1.7;
  color: #1e293b;
  background: #f8fafc;
  padding: 0.85rem 1.1rem;
  border-radius: 6px;
  border-left: 4px solid #b45309;
}

.minor-links-bar {
  display: flex;
  gap: 0.75rem;
  flex-wrap: wrap;
  margin-top: 1.25rem;
  padding-top: 1rem;
  border-top: 1px solid #e2e8f0;
}
"""

# 2. Build HTML items
html_items = []
for it in minor_items:
    gh_btn = f'''<a href="{it['gh_url']}" target="_blank" class="project-link github">
      <i data-lucide="github"></i>
      <span>저장소 방문하기</span>
    </a>''' if it['gh_url'] else ""

    hn_btn = f'''<a href="{it['hn_url']}" target="_blank" class="project-link youtube" style="background:#fff7ed; color:#c2410c; border-color:#ea580c;">
      <i data-lucide="message-square"></i>
      <span>Hacker News 토론보기</span>
    </a>''' if it['hn_url'] else ""

    item_html = f'''      <!-- [{it['platform']}] {it['repo']} -->
      <div class="minor-item" id="minor-{it['id']}">
        <div class="minor-summary-bar" onclick="toggleMinorItem(this.parentElement)">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge {it['platform_class']}">{it['platform']}</span>
              <span class="minor-metric">{it['metric_icon']} {it['metric_val']}</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> {it['time_ago']}</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> {it['velocity']}</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-repo-name">{it['repo']}</strong>
              <span class="minor-dash">—</span>
              <span class="minor-summary-text">{it['snippet']}</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <button class="minor-toggle-btn" type="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </button>
          </div>
        </div>

        <div class="minor-detail-content">
          <div class="minor-detail-inner">
            <div class="minor-headline-box">
              <h3 class="minor-detail-headline">{it['title']}</h3>
            </div>
            
            <div class="minor-story-body">
              <p class="minor-paragraph"><strong>[현장 상황 및 배경]</strong> {it['bg']}</p>
              <p class="minor-paragraph"><strong>[핵심 기술 메커니즘]</strong> {it['mechanism']}</p>
            </div>

            <div class="schematic-container minor-schematic">
              <div class="schematic-title"><i data-lucide="cpu" class="schematic-icon"></i> {it['box_title']}</div>
              <div class="minor-box-flow">{it['box_content']}</div>
            </div>

            <div class="minor-story-body">
              <p class="minor-paragraph"><strong>[핵심 의의 및 관전 포인트]</strong> {it['stakes']}</p>
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

minor_section_html = f'''    <!-- ==========================================================================
         실시간 극초기 레이더 마이너 브리핑 (18선 콤팩트 줄노트 아코디언)
         ========================================================================== -->
    <section class="minor-radar-section" id="minor-radar">
      <div class="minor-radar-header">
        <div class="minor-title-group">
          <span class="aggro-tag" style="background:#e0e7ff; color:#3730a3; border-color:#6366f1;">⚡ 실시간 극초기 레이더</span>
          <h2 class="minor-section-title">오늘 갓 태어난 오픈소스 & 화제작 (마이너 18선)</h2>
        </div>
        <p class="minor-section-desc">
          최근 30시간 내 생성·등록된 프로젝트 중 시간당 증가율(속도) 순으로 3개 구간(0~10h, 10~20h, 20~30h)을 정밀 선별하고, 동일 주제를 재귀적으로 묶어 완성한 고유 18선 마이너 브리핑입니다.
        </p>
      </div>

      <div class="minor-items-container">
{items_joined}
      </div>
    </section>'''

# 3. Minor Toggle JS
minor_js = """
    // 마이너 아코디언 아이템 토글
    function toggleMinorItem(item) {
      item.classList.toggle('active');
      const btn = item.querySelector('.minor-toggle-btn');
      const btnText = item.querySelector('.minor-btn-text');
      const isExpanded = item.classList.contains('active');
      if (btn) btn.setAttribute('aria-expanded', isExpanded ? 'true' : 'false');
      if (btnText) {
        btnText.textContent = isExpanded ? '메모 접기 ▲' : '메모 펼치기';
      }
      if (window.lucide) lucide.createIcons();
    }
"""

# Check CSS insertion point
if ".minor-radar-section" not in html_content:
    # insert before </style>
    html_content = html_content.replace("</style>", f"{minor_css}\n</style>", 1)
    print("Inserted Minor CSS into <style>")

# Check Section insertion point (before <footer>)
if '<section class="minor-radar-section"' not in html_content:
    footer_pos = html_content.find("<!-- 푸터 -->")
    if footer_pos != -1:
        html_content = html_content[:footer_pos] + minor_section_html + "\n\n    " + html_content[footer_pos:]
        print("Inserted Minor Section HTML before <footer>")
    else:
        print("ERROR: Could not find <!-- 푸터 -->")

# Check JS insertion point (before </script> at the bottom)
if "function toggleMinorItem" not in html_content:
    last_script_end = html_content.rfind("</script>")
    if last_script_end != -1:
        html_content = html_content[:last_script_end] + minor_js + "\n  " + html_content[last_script_end:]
        print("Inserted Minor JS into bottom <script>")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully updated {html_path.name}! New size: {len(html_content):,} chars")
