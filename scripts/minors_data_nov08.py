# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.minors_gh_nov08 import GH_MINORS
from scripts.minors_hn_nov08 import HN_MINORS

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
          직전 발행(11월 6일) 이후 약 53시간 동적 탐색 윈도우를 균등 3분할(0~18h, 18~35h, 35~53h)하여 시간당 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다. 상호 중복 배제 및 재귀적 클러스터링 알고리즘이 적용되었습니다.
        </p>
      </div>

      <div class="minor-items-container">
"""

MINORS_FOOTER = """
      </div>
    </section>
"""

FULL_MINORS_SECTION = MINORS_HEADER + GH_MINORS + HN_MINORS + MINORS_FOOTER

if __name__ == '__main__':
    print(f"minors_data_nov08 assembled successfully. Length: {len(FULL_MINORS_SECTION):,} characters.")
