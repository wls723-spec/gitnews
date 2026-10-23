# -*- coding: utf-8 -*-
"""
Apply deep minor items and remove unnecessary header text in news/2026-10-22.html
"""

import sys
import re
from pathlib import Path
from generate_deep_minor_section import deep_minor_items

sys.stdout.reconfigure(encoding='utf-8')

html_path = Path(r"c:\Program Files\1a\src\gitnews\news\2026-10-22.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Build HTML items
html_items = []
for it in deep_minor_items:
    gh_btn = f'''<a href="{it['gh_url']}" target="_blank" class="project-link github">
      <i data-lucide="github"></i>
      <span>저장소 방문하기</span>
    </a>''' if it['gh_url'] else ""

    hn_btn = f'''<a href="{it['hn_url']}" target="_blank" class="project-link youtube" style="background:#fff7ed; color:#c2410c; border-color:#ea580c;">
      <i data-lucide="message-square"></i>
      <span>Hacker News 토론보기</span>
    </a>''' if it['hn_url'] else ""

    # Clean multi-line strings
    comm_clean = "<br><br>".join([line.strip() for line in it['community_reaction'].strip().split("\n\n") if line.strip()])
    mech_clean = "<br><br>".join([line.strip() for line in it['mechanism'].strip().split("\n\n") if line.strip()])
    use_clean = "<br><br>".join([line.strip() for line in it['use_case'].strip().split("\n\n") if line.strip()])
    future_clean = "<br><br>".join([line.strip() for line in it['future_outlook'].strip().split("\n\n") if line.strip()])

    item_html = f'''      <!-- [{it['badge']}] {it['title']} -->
      <div class="minor-item" id="minor-{it['id']}">
        <div class="minor-summary-bar" onclick="toggleMinorItem(this.parentElement)">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge {it['badge_class']}">{it['badge']}</span>
              <span class="minor-metric">{it['stars']}</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> {it['time']}</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> {it['velocity']}</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">{it['title']}</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">{it['sub']}</span>
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
              <p class="minor-detail-subheadline">{it['sub']}</p>
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
              <div class="schematic-title"><i data-lucide="git-commit" class="schematic-icon"></i> {it['box_title']}</div>
              <div class="minor-box-flow">{it['box_content']}</div>
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

# New Minor Section HTML WITHOUT the unnecessary header texts requested by user!
new_minor_section = f'''    <!-- ==========================================================================
         실시간 극초기 레이더 마이너 브리핑 (18선 콤팩트 줄노트 아코디언)
         ========================================================================== -->
    <section class="minor-radar-section" id="minor-radar">
      <div class="minor-items-container">
{items_joined}
      </div>
    </section>'''

# Replace existing <section class="minor-radar-section" ... </section>
pattern = re.compile(r'<section class="minor-radar-section".*?</section>', re.DOTALL)
if pattern.search(html_content):
    html_content = pattern.sub(new_minor_section, html_content)
    print("Replaced existing minor-radar-section with new deep content (Header texts removed)!")
else:
    print("ERROR: Could not find existing minor-radar-section to replace!")

# Additional CSS adjustments for the new headlines and sections
additional_css = """
/* Minor Section Headline & Typography Enhancements */
.minor-headline-text {
  font-family: var(--font-title);
  font-size: 1.35rem;
  font-weight: 700;
  color: #111827;
  letter-spacing: -0.01em;
  flex-shrink: 0;
}

.minor-sub-text {
  font-family: var(--font-body);
  font-size: 0.98rem;
  color: #4b5563;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.minor-item:hover .minor-headline-text {
  color: #b45309;
}

.minor-detail-headline {
  font-family: var(--font-title);
  font-size: 1.7rem;
  font-weight: 700;
  color: #0f172a;
  line-height: 1.3;
  margin-bottom: 0.4rem;
}

.minor-detail-subheadline {
  font-family: var(--font-body);
  font-size: 1.05rem;
  font-weight: 700;
  color: #64748b;
  margin-bottom: 1.25rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px dashed #cbd5e1;
}

.minor-story-section {
  margin-bottom: 1.2rem;
}

.minor-section-tag {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  font-family: var(--font-title);
  font-size: 1.2rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.45rem;
}

.minor-paragraph {
  font-family: var(--font-body);
  font-size: 1.02rem;
  color: #334155;
  line-height: 1.8;
}
"""

if ".minor-headline-text" not in html_content:
    html_content = html_content.replace("</style>", f"{additional_css}\n</style>", 1)
    print("Appended new minor CSS styles into <style> block.")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully updated {html_path.name}! New size: {len(html_content):,} chars")
