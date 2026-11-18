# -*- coding: utf-8 -*-
# Story 3: HKUDS/CLI-Anything

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] HKUDS/CLI-Anything                               -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_cli_anything.jpg" alt="CLI-Anything Agent-Native Software Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="terminal" style="width:12px;height:12px;fill:#fff;"></i> 59K STARS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ffedd5; border-color:#ea580c; color:#9a3412;">🕹️ 세상의 모든 GUI 앱을 AI CLI로 개조</span>
              <span class="platform-tag">GitHub Trending &amp; CLI-Hub</span>
              <span class="platform-tag">HKUDS / CLI-Anything</span>
            </div>

            <h2 class="article-headline">
              "오늘의 소프트웨어는 인간을 위해 만들었지만, 내일의 사용자는 AI 에이전트다": 모든 데스크톱 앱을 CLI로 바꾸는 'CLI-Anything'
            </h2>

            <div class="article-subheadline">
              Blender·GIMP·QGIS·LibreOffice·Shotcut·Obsidian 등 거대한 GUI 소프트웨어를 구조화된 JSON 출력과 REPL을 갖춘 에이전트 네이티브 CLI 하네스로 자동 변환 (+384스타/일, 누적 59,685스타)
            </div>
            <p class="article-snippet">
              AI 에이전트에게 마우스 커서를 주고 화면 스크린샷을 찍어가며 Blender나 CAD 메뉴를 클릭하게 시키는 컴퓨터 유즈(Computer Use) 방식은 느리고 부정확하며 토큰을 태워 먹습니다. 홍콩대 데이터 사이언스 연구실(HKUDS)이 공개해 누적 59,685스타(오늘 +384스타)를 기록 중인 <strong>HKUDS/CLI-Anything</strong>은 정반대의 해법을 꺼냈습니다. 화면 픽셀을 억지로 읽는 대신, 소프트웨어 자체를 AI가 가장 잘 다루는 결정론적 CLI 하네스로 재포장해 버리는 것입니다.
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
              <i data-lucide="flame"></i> 1. 리드: 마우스 클릭을 흉내 내는 에이전트에서 '명령줄의 지배자'로
            </h3>
            <p>
              지난 1년간 빅테크 연구소들은 AI 에이전트에게 기존 데스크톱 소프트웨어를 쥐여주기 위해 비전 모델(VLM)을 동원했다. 화면을 캡처하고, "파일 메뉴의 X=142, Y=38 픽셀을 클릭하라"고 지시하는 방식이다. 하지만 OS 해상도가 조금만 바뀌거나 팝업 창이 하나 뜨면 에이전트는 길을 잃고, 영상 편집이나 3D 모델링 같은 정교한 작업에서는 끝없는 클릭 실수로 시간을 낭비한다.
            </p>
            <p>
              <strong>HKUDS/CLI-Anything</strong>(Apache-2.0)은 이 소모적인 픽셀 추론 게임을 단칼에 끝낸다. "인간에게는 GUI가 직관적이지만, LLM 코딩 에이전트에게는 구조화된 <code>--json</code> 출력과 자기 기술적(Self-describing) 헬프 명령어, REPL 세션을 갖춘 CLI가 천 배 더 직관적이다." 이 단순하고도 파괴적인 통찰이 Blender, GIMP, Audacity, QGIS, Shotcut, Calibre, Obsidian, n8n, Zoom까지 수십 종의 현업 소프트웨어를 단숨에 에이전트 손끝으로 끌어들였다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '스크린샷 추론' 대신 소프트웨어 내부 엔진에 직결되는 CLI-Hub 생태계
            </h3>
            <p>
              CLI-Anything의 진짜 위력은 개별 래퍼 몇 개를 짠 수준이 아니라, 어떤 소프트웨어든 에이전트용 CLI 하네스로 자동 생성·검증·배포하는 표준 방법론과 패키지 허브(<code>CLI-Hub</code>)를 구축했다는 데 있다.
            </p>

            <div class="editorial-quote">
              <p>
                "오늘날의 소프트웨어는 인간을 섬긴다. <strong>내일의 사용자는 에이전트(Agents)가 될 것이다.</strong> CLI-Anything은 단일 명령줄로 Claude Code, Cursor, OpenClaw, Pi, nanobot이 CAD·3D·영상·문서 도구를 100% 결정론적으로 조종하게 만든다."
              </p>
              <small>— HKUDS/CLI-Anything 공식 선언 및 테크 리포트 (arXiv:2606.03854)</small>
            </div>

            <p>
              저장소에 포함된 2,461개 이상의 유닛·E2E 테스트 통과 기록과 <code>pip install cli-anything-hub</code> → <code>cli-hub install &lt;name&gt;</code> 워크플로우는 이미 커뮤니티가 직접 새로운 소프트웨어 하네스를 PR로 기여하고 <code>npx skills add HKUDS/CLI-Anything</code>으로 전파하는 거대한 생태계 플라이휠을 형성했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 이중 출력 하네스, 보안 파싱, 그리고 궤적(Trajectory) 검증 루프
            </h3>
            <p>
              CLI-Anything 하네스는 단순한 셸 스크립트 별칭(Alias)이 아니라, 실제 소프트웨어의 헤드리스 백엔드와 프로젝트 파일 포맷을 정밀하게 제어하는 Python(Click ≥ 8.0) 엔지니어링 계층으로 설계됐다:
            </p>
            <ul>
              <li><strong>이중 모드 출력 &amp; REPL 상태 유지:</strong> 모든 하네스는 인간 가독형 출력과 에이전트 전용 기계 파싱(<code>JSON</code>) 출력을 동시에 지원한다. 상태 유지가 필요한 편집 작업에서는 REPL 세션과 실시간 프리뷰 루프를 열어 에이전트가 중간 산출물을 확인하며 수정할 수 있다.</li>
              <li><strong>보안 하드닝 &amp; 실제 바이너리 E2E 검증:</strong> XML/SVG/ODF/MLT/MusicXML 파싱 경로는 <code>defusedxml</code>로 XXE 공격을 차단하고, Sketch 토큰 파일은 경로 탈출(Path Traversal)과 심볼릭 링크 공격을 방어하며, SQLCipher 백업 강제 가드를 적용한다. 모든 하네스는 모의 객체(Mock)가 아닌 실제 설치된 Calibre·Blender·LibreOffice 바이너리 대상 E2E 테스트를 통과해야 머지된다.</li>
              <li><strong>통합 <code>skills/</code> &amp; <code>cli-hub</code> 레지스트리:</strong> 모든 <code>SKILL.md</code>가 최상위 표준 경로로 통합되어, 코딩 에이전트가 명령 한 번으로 새로운 도구의 문법과 실행 안전 규칙을 즉시 학습한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">CLI-Anything GUI-to-Agent CLI 하네스 변환 및 CLI-Hub 배포 구조</span>
                <span class="schematic-badge">Apache-2.0 · 2,461+ Tests Passing</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Agent &amp; Skill Layer</div>
                  <div class="schematic-desc">
                    Claude Code · Cursor · Hermes · Pi<br>
                    <code>npx skills add HKUDS/CLI-Anything</code><br>
                    <code>SKILL.md</code> 표준 계약으로 즉시 인지<br>
                    <code>cli-hub install &lt;app&gt;</code> 원클릭 설치
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Python Click Harness</div>
                  <div class="schematic-desc">
                    JSON + Human 이중 출력 계약<br>
                    REPL 상태 제어 및 궤적 프리뷰 루프<br>
                    <code>defusedxml</code>·백업 가드 보안 계층<br>
                    실제 앱 대상 Unit + E2E 검증(2,461건)
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Native App Backends</div>
                  <div class="schematic-desc">
                    Blender · QGIS · Shotcut · Audacity<br>
                    LibreOffice · Calibre · Obsidian · n8n<br>
                    3MF 3D 메시 · CAD · 자막·다이어그램<br>
                    픽셀 클릭 없이 무결점 산출물 렌더링
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">CLI-Hub 공식 레지스트리 포털 (hkuds.github.io/CLI-Anything)</span>
              </div>
              <img src="../assets/images/demo_cli_anything.png" alt="CLI-Anything CLI-Hub Portal" class="showcase-img">
              <p class="showcase-caption">
                ▲ CLI-Hub 웹 포털 실화면: 커뮤니티가 구축한 다양한 데스크톱 소프트웨어용 에이전트 네이티브 CLI 하네스와 공개 레지스트리를 검색하고 즉시 설치할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 소프트웨어 산업의 지각 변동: "SaaS API를 안 열어주면 CLI 하네스로 뚫는다"
            </h3>
            <p>
              그동안 레거시 데스크톱 소프트웨어 벤더들과 폐쇄형 SaaS 기업들은 비싼 엔터프라이즈 API 요금제를 따로 팔거나 에이전트 연동을 막아왔다. 하지만 CLI-Anything은 기존 소프트웨어의 로컬 바이너리·프로젝트 파일·로컬 REST 인터페이스를 에이전트용 CLI로 감싸버림으로써, 벤더의 공식 AI 애드온 구독 없이도 기존 툴체인을 완전 자동화할 길을 열어젖혔다.
            </p>
            <ul>
              <li><strong>컴퓨터 유즈(GUI 에이전트) 비용의 100배 절감:</strong> 매 스텝 고해상도 스크린샷을 비전 모델에 먹여 클릭 좌표를 찍는 대신, 한 줄의 CLI 명령과 JSON 응답만으로 작업을 끝내 토큰 비용과 지연시간을 극적으로 낮춘다.</li>
              <li><strong>오픈소스 앱 생태계의 역전:</strong> Blender, GIMP, QGIS 같은 오픈소스 데스크톱 앱들이 CLI-Anything을 타고 가장 강력한 AI 자동화 툴로 재탄생하고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 그래픽 유저 인터페이스(GUI)의 반세기 역사에 던지는 반문
            </h3>
            <p>
              제록스 파크(Xerox PARC)가 마우스와 아이콘을 발명한 뒤 40여 년간 소프트웨어의 발전은 '인간의 눈과 손가락'에 맞추는 과정이었다. 하지만 이제 소프트웨어 앞에서 명령을 내리는 주체가 터미널을 사랑하는 AI 에이전트로 이동하고 있다.
            </p>
            <p>
              CLI-Anything이 6만 스타 가까이 모으며 증명한 진실은 명쾌하다. 가장 미래적인 AI 자동화는 화려한 화면을 흉내 내는 로봇 팔이 아니라, 가장 오래되고 단단한 유닉스 철학—텍스트 스트림과 명령줄—로의 귀환이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=CLI-Anything+HKUDS+AI+Agent+CLI" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://hkuds.github.io/CLI-Anything/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> CLI-Hub 공식 포털
              </a>
              <a href="https://github.com/HKUDS/CLI-Anything" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
