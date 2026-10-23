# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.minors_gh import GH_MINORS
from scripts.minors_hn import HN_MINORS

MINORS_HEADER = """
    <!-- ========================================================== -->
    <!-- [SECTION 9] 실시간 극초기 레이더 (마이너 브리핑 18선) -->
    <!-- ========================================================== -->
    <section class="minor-radar-section" id="minor-radar">
      <div class="minor-radar-header">
        <div class="minor-title-group">
          <span class="aggro-tag" style="background:#fef08a; border-color:#ca8a04; color:#854d0e;">⚡ 실시간 극초기 레이더</span>
          <h2 class="minor-section-title">갓 태어난 극초신성 & 실시간 급상승 유망주 18선</h2>
        </div>
        <p class="minor-section-desc">
          최근 30시간을 10시간씩 3분할(0~10h, 10~20h, 20~30h)하여 시간당 증가율(Velocity) 순으로 엄선한 고유 프로젝트 리포트입니다. 상호 중복 배제 및 클러스터링 알고리즘이 적용되었습니다.
        </p>
      </div>

      <div class="minor-items-container">
"""

MINORS_FOOTER = """
      </div>
    </section>
"""

FULL_MINORS_SECTION = MINORS_HEADER + GH_MINORS + HN_MINORS + MINORS_FOOTER
