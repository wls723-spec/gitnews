# -*- coding: utf-8 -*-
# Story 4: cathrynlavery/diagram-design

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] cathrynlavery/diagram-design                     -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_diagram_design.jpg" alt="Diagram Design Editorial SVG Skill Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="pen-tool" style="width:12px;height:12px;fill:#fff;"></i> NO MERMAID SLOP</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#fef3c7; border-color:#d97706; color:#92400e;">🎨 "그림자도, 못생긴 Mermaid도 없다"</span>
              <span class="platform-tag">GitHub Trending &amp; diagramdesign.dev</span>
              <span class="platform-tag">cathrynlavery / diagram-design</span>
            </div>

            <h2 class="article-headline">
              AI가 그려주는 촌스러운 둥근 박스 다이어그램을 끝장낸다: 51종 에디토리얼 HTML+SVG 스킬 'Diagram Design'
            </h2>

            <div class="article-subheadline">
              4px 그리드·1px 헤어라인·단일 강조색 미학에 웹사이트 팔레트 자동 온보딩, CI 겹침 검증, Mermaid/draw.io/Excalidraw 역변환까지 결합한 MIT 에이전트 스킬 (+332스타/일, 누적 68,592스타)
            </div>
            <p class="article-snippet">
              블로그 글이나 기술 제안서에 넣을 아키텍처 도해 하나를 만들 때마다, AI가 뱉어내는 투박한 기본 Mermaid 차트와 싸우거나 Figma를 열어 30분을 허비해 본 경험은 누구나 있습니다. 오늘 332스타를 추가하며 누적 68,592스타를 기록한 <strong>cathrynlavery/diagram-design</strong>은 "모델에게 부족했던 것은 지능이 아니라 디자인 안목(Taste)"이라는 통찰에서 출발해, 빌드 도구도 JS 의존성도 없는 순수 1개 파일 HTML+SVG 에디토리얼 다이어그램 51종을 에이전트의 손끝에 쥐여줍니다.
            </p>
            <div class="article-action">
              <span>메모 펼치기</span>
              <i data-lucide="chevron-down" class="chevron-icon"></i>
            </div>
          </div>
        </div>

        <div class="article-detail" onclick="event.stopPropagation()">
          <div class="editorial-content">

            <h3 class="editorial-section-title">
              <i data-lucide="flame"></i> 1. 리드: <code>npx skills add cathrynlavery/diagram-design</code>, 그리고 사라진 Figma 30분
            </h3>
            <p>
              에이전트에게 <em>"프론트엔드, 백엔드, 데이터베이스, Redis 캐시 구조도 그려줘"</em> 혹은 <em>"https://내사이트.com 브랜드 톤에 맞춰 온보딩해줘"</em>라고 말 한마디만 건넨다. 몇 초 뒤 에이전트는 도해 유형을 결정하고 계획을 브리핑한 뒤, 브라우저에서 더블클릭만으로 즉시 열리는 단 하나의 <code>.html</code> 파일을 써 내려간다.
            </p>
            <p>
              디자이너이자 LittleMight의 창업자 캐스린 레이버리(Cathryn Lavery)가 블로그 도해를 직접 그리다 지쳐 만들어 MIT 라이선스로 공개한 <strong>cathrynlavery/diagram-design</strong>이 누적 68,592스타(오늘 +332스타)를 넘어섰다. Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, Qoder, Pi 등 Agent Skills 표준을 읽는 모든 코딩 호스트에 단 한 줄로 이식되며, 개발자 문서의 시각적 품격을 단숨에 스위스 에디토리얼 매거진 수준으로 끌어올리고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "그림자 금지, 밀도 4/10, 가장 높은 품질의 행동은 삭제다"
            </h3>
            <p>
              기존 AI 다이어그램이 'AI 슬롭(Slop)'처럼 보이는 이유는 명확하다. 제멋대로인 둥근 사각형, 과도한 드롭 섀도우, 의미 없는 무지개색 배지, 그리고 텍스트와 화살표가 서로 겹쳐 깨지는 자동 레이아웃 때문이다. 레이버리는 이 문제를 AI 모델 탓으로 돌리지 않고, 자신의 디자인 규칙을 철저한 <strong>제약 명세(<code>references/style-guide.md</code>)</strong>로 번역해 스킬에 심었다.
            </p>

            <div class="editorial-quote">
              <p>
                "모델은 이미 내용을 이해하고 있었다. 빠진 것은 오직 안목(Taste)이었다. <strong>가장 수준 높은 디자인 결정은 대개 삭제(Deletion)다.</strong> 모든 노드는 존재 이유를 증명해야 하며, 강조색(Tangerine)은 독자가 가장 먼저 봐야 할 단 1~2곳에만 허락된다."
              </p>
              <small>— cathrynlavery/diagram-design 에디토리얼 디자인 원칙 (목표 밀도 4/10)</small>
            </div>

            <p>
              이 철학은 단순한 Flow/Sequence 차트를 넘어 Wardley Map, Sankey, Architecture Delta(Before·Changes·After), 2:1 등축 분해도(Exploded Axonometric), 데이터베이스 스키마, Service Blueprint, SBGN 생물학 다이어그램까지 무려 51개 도해 유형(각각 Minimal Light / Minimal Dark / Full-Editorial 3가지 변형)을 일관된 시각 언어로 통제한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 4px 그리드 좌표계, 브랜드 프로파일링, CI 겹침 검증
            </h3>
            <p>
              이 스킬이 단순한 프롬프트 조각이 아닌 이유는, 도해를 '텍스트'가 아니라 <strong>검증 가능한 기하학적 SVG 산출물</strong>로 다루는 엔지니어링 체계 덕분이다:
            </p>
            <ul>
              <li><strong>엄격한 에디토리얼 토큰 &amp; 4px 그리드:</strong> 모든 좌표가 4px 그리드 위에 정렬되고 1px 헤어라인과 그림자 제로(No Shadows) 규칙을 따른다. 기본 팔레트(화이트 스모크 용지 + 젯 블랙 잉크 + WCAG 4.5:1 대비를 통과한 탠저린 포인트) 외에도 대상 웹사이트 URL에서 컬러와 폰트를 추출해 <code>~/.diagram-design/profiles/</code>에 브랜드 프로파일로 영구 저장한다.</li>
              <li><strong>무의존 단일 자립형 HTML+SVG:</strong> 빌드 스텝, 외부 CDN 이미지, 자바스크립트 런타임 의존성 없이 인라인 SVG 1개 파일로 완결되며, <code>/export-diagram</code>으로 즉시 PNG·SVG로 추출한다.</li>
              <li><strong>역방향 마이그레이션 &amp; CI 레이아웃 감사:</strong> 기존의 낡은 <code>/import-mermaid</code>, <code>/import-plantuml</code>, <code>/import-excalidraw</code>, draw.io 파일을 에디토리얼 스타일로 재작도하고, CI 스크립트로 텍스트 겹침(Overlaps)과 영역 잘림(Clipping)을 자동 검출한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Diagram Design 51종 에디토리얼 SVG 생성 및 브랜드 온보딩 구조</span>
                <span class="schematic-badge">MIT · 4px Grid · Zero JS/Build Dependency</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Brand Onboarding &amp; Import</div>
                  <div class="schematic-desc">
                    대상 사이트 URL 컬러·폰트 추출<br>
                    <code>~/.diagram-design/profiles/</code> 저장<br>
                    Mermaid · draw.io · Excalidraw 가져오기<br>
                    51종 도해 타입 자동 매핑
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Editorial SVG Synthesis</div>
                  <div class="schematic-desc">
                    4px 좌표 그리드 + 1px 헤어라인<br>
                    그림자 0% · 밀도 4/10 · 단일 강조색<br>
                    2:1 등축 분해도(Exploded Axonometric)<br>
                    Light / Dark / Full-Editorial 3변형
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Geometry CI &amp; Export</div>
                  <div class="schematic-desc">
                    노드 겹침(Overlap)·클리핑 자동 검증<br>
                    단일 자립형 <code>.html</code> 파일 출력<br>
                    <code>/export-diagram</code> 고해상도 SVG/PNG<br>
                    Claude · Cursor · Codex · Pi 호환
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Diagram Design 공식 51종 인터랙티브 갤러리 실화면</span>
              </div>
              <img src="../assets/images/demo_diagram_design.png" alt="Diagram Design Live Gallery Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ cathrynlavery.github.io/diagram-design 라이브 갤러리 실화면: 51종의 아키텍처, 시퀀스, 등축 분해도(Exploded), 워들리 맵 등을 Light·Dark·Full-Editorial 모드로 즉시 탐색할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 디자인 도구의 재편: SaaS 다이어그램 툴과 '텍스트-투-슬롭' 사이의 새로운 지대
            </h3>
            <p>
              지금까지 기술 도해 시장은 두 극단으로 나뉘어 있었다. Git PR에서 Diff가 가능하지만 미적으로 투박한 Mermaid/PlantUML, 그리고 미적이지만 손으로 일일이 박스를 끌어야 하는 유료 Figma/Miro/Lucidchart다. 레이버리 역시 README에서 솔직히 선을 긋는다. 매 스프린트마다 코드처럼 텍스트 Diff를 해야 하는 Git 문서는 여전히 Mermaid의 영역이지만, <strong>"세상에 발행하고 설득해야 하는 도해"</strong>는 이제 에이전트가 직접 에디토리얼 SVG로 깎아내는 시대가 열렸다.
            </p>
            <ul>
              <li><strong>Agent Skills 생태계의 수익화와 오픈 코어:</strong> 스킬 본체는 MIT로 전면 개방하면서, 상표와 공식 마켓플레이스 신뢰도를 지키는 표준 배포 모델의 모범을 보여준다.</li>
              <li><strong>'좋은 안목'의 코드화(Codified Taste):</strong> 숙련된 아트 디렉터의 감각이 마크다운 규칙과 CI 기하학 검사기로 압축되어 누구나 <code>npx skills add</code> 한 줄로 호출할 수 있는 자산으로 변모했다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 안목(Taste)도 이제 오픈소스 의존성으로 설치한다
            </h3>
            <p>
              수많은 AI 도구가 생성 속도를 자랑하며 인터넷에 똑같은 둥근 사각형과 그라데이션 쓰레기를 쏟아내고 있다. 그 홍수 속에서 독자의 시선을 붙잡는 것은 결국 절제된 여백과 단 한 줄의 정확한 강조선이다.
            </p>
            <p>
              6만8천 명의 개발자가 <code>diagram-design</code>에 별표를 던진 이유는 단순하다. 우리는 이제 AI에게 코드를 짜게 하는 것을 넘어, '부끄럽지 않은 미적 감각'을 패키지로 설치하는 법을 배우기 시작했다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=diagram-design+claude+code+skill+editorial+svg" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://cathrynlavery.github.io/diagram-design/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 51종 라이브 갤러리
              </a>
              <a href="https://github.com/cathrynlavery/diagram-design" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
