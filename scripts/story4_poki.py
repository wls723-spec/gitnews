# -*- coding: utf-8 -*-
# Story 4: JosssphZhou/poki (HERO 4)

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 4] JosssphZhou/poki -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_poki.png" alt="JosssphZhou poki" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="smartphone" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #4</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 탈옥 없는 실제 아이폰 조작의 기적</span>
              <span class="platform-tag">GitHub Trending #4</span>
              <span class="platform-tag">JosssphZhou / poki</span>
            </div>
            
            <h2 class="article-headline">
              "시뮬레이터는 끝났다, 실제 아이폰을 AI가 쥔다" — 탈옥 없는 모바일 에이전트 Poki
            </h2>

            <div class="article-subheadline">
              USB 케이블 연결만으로 실제 물리 iOS 기기를 사람처럼 조작… 로컬 MCP 서버 기반 화면 비전 분석과 네이티브 터치·스와이프로 모바일 테스트 자동화의 신기원을 열다
            </div>
            <p class="article-snippet">
              맥OS의 컴퓨터 유즈(Computer Use)를 넘어 스마트폰 영역으로 지능을 확장한 오픈소스 'Poki'. 탈옥(Jailbreak)이나 고가의 클라우드 팜 없이 서랍 속 아이폰을 AI 에이전트의 손발로 만들어주는 로컬 하네스를 심층 해부합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 컴퓨터 유즈를 넘어선 '폰 유즈(Phone Use)'의 갈증
            </h3>
            <p>
              앤트로픽의 클로드(Claude)가 마우스와 키보드로 데스크톱 컴퓨터를 다루는 'Computer Use'를 선보였을 때 전 세계가 열광했다. 
              하지만 전 세계 소프트웨어 트래픽의 70% 이상은 데스크톱이 아닌 모바일 스마트폰에서 발생한다. 
              수많은 모바일 앱 개발사와 QA 엔지니어들은 "왜 실제 아이폰을 AI가 직접 만져보게 할 수는 없는가?"라는 갈증에 시달려왔다.
            </p>
            <p>
              애플의 엄격한 보안 샌드박스 때문에 아이폰을 원격 제어하려면 기기를 해킹(탈옥)하거나, 비싼 클라우드 디바이스 팜(Device Farm)에 월 수백만 원을 지불해야 했다. 
              오늘 깃허브에 혜성처럼 등장한 오픈소스 <strong>JosssphZhou/poki</strong>는 이 모든 족쇄를 단번에 풀어헤쳤다. 
              <strong>탈옥 없이, 추가 하드웨어 없이, 일반 아이폰을 라이트닝/C타입 케이블로 꽂기만 하면 AI 에이전트가 화면을 보고 탭과 스크롤을 척척 수행</strong>하는 혁신적인 로컬 도구가 탄생한 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "Poki는 당신이 폰을 쓰듯 당신의 아이폰을 씁니다"
            </h3>
            <p>
              Poki의 접근 방식은 복잡한 프레임워크가 아닌 표준 <strong>MCP(Model Context Protocol)</strong> 기반이다.
            </p>

            <div class="editorial-quote danger">
              <p>
                "당신의 책상 위 아이폰을 연결하고 <code>poki start</code>를 입력하라. 
                배달 앱에서 주문을 넣고, 은행 앱의 잔고를 확인하고, 새로 개발한 플러터(Flutter)/스위프트(Swift) 앱의 UI 버그를 AI가 실시간으로 클릭하며 스스로 찾아낸다."
              </p>
              <small>— JosssphZhou, Poki 프로젝트 공식 쇼케이스</small>
            </div>

            <p>
              시뮬레이터가 잡지 못하는 실제 물리 하드웨어의 생체 인증 팝업, 카메라 권한 요청, 복잡한 푸시 알림 인터랙션까지 실제 사용자 시점에서 완벽하게 검증할 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: 비전 파서와 네이티브 드라이버 브릿지
            </h3>
            <p>
              Poki가 애플의 보안 장벽을 우회하지 않고 정식 프로토콜로 아이폰을 제어하는 구조는 다음과 같다:
            </p>
            <ul>
              <li><strong>WebDriverAgent 네이티브 브릿지:</strong> 애플 개발자 인증서를 통해 표준 XCTest 러너 기반의 초경량 통신 에이전트를 아이폰에 백그라운드 구동. 기기 루팅이나 탈옥이 일절 필요 없음.</li>
              <li><strong>실시간 비전 화면 파싱(Visual Grounding):</strong> 아이폰 화면을 캡처하여 비전 LLM에 주입, 터치해야 할 버튼의 정확한 화면 절대 좌표(X, Y)와 제스처 벡터(스와이프, 롱프레스, 핀치투줌)를 도출.</li>
              <li><strong>로컬 MCP 서버 연동:</strong> Claude Code, Cursor, Windsurf 등 어떤 에이전트라도 <code>tap_screen(x, y)</code>, <code>type_text(string)</code>, <code>swipe(direction)</code> 등의 도구를 즉시 호출 가능.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="git-branch" style="color:#0ea5e9;"></i> Poki 탈옥 없는 실제 아이폰 조작 파이프라인
                </span>
                <span class="schematic-badge">REAL IPHONE HARDWARE BRIDGE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">실물 아이폰 화면 실시간 캡처</div>
                  <div class="step-tech">USB Tunneling + Screen Buffer</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">에이전트 비전 분석 & 좌표 계산</div>
                  <div class="step-tech">Vision Grounding + MCP Protocol</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">네이티브 터치/스와이프 주입</div>
                  <div class="step-tech">XCTest Driver (Zero Jailbreak)</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 흐름:</strong> 탈옥 위험 없이 애플 공식 테스트 하네스를 통해 고속 USB 통신을 유지하며, AI 에이전트의 시각적 판단에 따라 밀리초 단위로 정확한 물리 제스처를 전달합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="smartphone"></i> 4. 모바일 QA 엔지니어링의 대격변
            </h3>
            <p>
              지금까지 모바일 앱 배포 전 회귀 테스트(Regression Test)는 수십 명의 테스터가 수백 대의 스마트폰을 손으로 직접 누르는 고된 노가다였다. 
              Poki는 여러 대의 실제 아이폰을 허브에 연결하고 "로그인부터 결제까지 전 과정을 테스트하고 실패한 화면을 캡처해 깃허브 이슈로 남겨줘"라는 자연어 명령 하나로 자율 모바일 테스트 팜을 구축할 수 있게 해준다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="monitor" style="color:#10b981;"></i> Poki 공식 웹사이트 & 실기기 제어 데모
                </span>
                <span class="media-showcase-badge demo">LIVE DEMO PREVIEW</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_poki.png" alt="Poki official website and iPhone in action" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ poki.bot 공식 라이브 데모:</strong> 탈옥 없는 실제 아이폰 위에서 AI 에이전트가 화면 맥락을 파악하고 네이티브 터치/스와이프를 수행하는 실기기 인터랙션.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-check"></i> 5. 결론: 손안으로 들어온 인공지능
            </h3>
            <p>
              소프트웨어의 종착지는 결국 사용자의 손에 쥐어진 스마트폰이다. 
              Poki는 데스크톱 모니터의 사각 프레임에 갇혀 있던 AI 에이전트에게 모바일 세상이라는 가장 넓은 날개를 달아준 기념비적인 프로젝트다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://poki.bot" target="_blank" class="project-link demo">
                  <i data-lucide="sparkles" style="width:16px;height:16px;"></i> 공식 웹사이트 poki.bot
                </a>
                <a href="https://github.com/JosssphZhou/poki" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
