# -*- coding: utf-8 -*-
# Story 2: D4Vinci/Scrapling (HERO 2)

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 2] D4Vinci/Scrapling -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_scrapling.jpg" alt="D4Vinci Scrapling" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #2</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 WAF 통곡의 벽을 허무는 단 한 줄의 세션</span>
              <span class="platform-tag">GitHub Trending #2</span>
              <span class="platform-tag">D4Vinci / Scrapling</span>
            </div>
            
            <h2 class="article-headline">
              "Cloudflare와 DataDome을 단 한 줄로 뚫다" — 차세대 스텔스 스크래퍼 Scrapling
            </h2>

            <div class="article-subheadline">
              무거운 헤드리스 브라우저 오버헤드를 걷어내고 초고속 HTTP 요청으로 안티봇 보호막을 우회… JA4 핑거프린트 위장, 어댑티브 요소 트래킹, MCP 서버 내장으로 AI 에이전트 크롤링의 신기원을 열다
            </div>
            <p class="article-snippet">
              Cloudflare Turnstile과 복잡한 안티봇 챌린지를 무력화하며 단일 요청부터 대규모 동시성 크롤링까지 단일 라이브러리로 통합한 D4Vinci의 Scrapling. 기존 Selenium과 Playwright의 자원 낭비를 극복한 스텔스 아키텍처를 해부합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 웹 스크래퍼를 질식시키던 안티봇 WAF의 시대
            </h3>
            <p>
              현대 웹에서 데이터를 긁어오는 작업은 고통스러운 고문이 되었다. 
              Cloudflare Turnstile, DataDome, Akamai, PerimeterX 같은 지능형 WAF(웹 방화벽)들이 TLS 핸드셰이크의 사소한 핑거프린트 불일치나 브라우저 자동화 흔적(<code>navigator.webdriver</code>)을 감지하는 순간 가차 없이 403 Forbidden이나 무한 캡차의 늪으로 밀어 넣기 때문이다.
            </p>
            <p>
              이를 뚫기 위해 개발자들은 Playwright나 Selenium 같은 무거운 크롬 브라우저 인스턴스를 수십 개씩 띄워야 했고, 이는 엄청난 RAM 낭비와 CPU 병목을 유발했다. 
              오늘 깃허브 트렌딩 2위에 오르며 하루에만 2,000개가 넘는 스타를 쓸어 담은 <strong>D4Vinci/Scrapling</strong>은 바로 이 지점을 혁신한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 브라우저를 띄우지 않고도 브라우저처럼 위장하다
            </h3>
            <p>
              Scrapling의 철학은 단순하다: <em>"정말 필요한 경우가 아니라면 무거운 브라우저를 띄우지 마라. 브라우저인 척 완벽하게 속여라."</em>
            </p>

            <div class="editorial-quote">
              <p>
                "Scrapling은 초고속 HTTP 요청, 스텔스 브라우징, 지능형 파싱, 그리고 대규모 동시성 크롤링을 단 하나의 라이브러리로 응축했다. 
                단 한 줄의 요청부터 웹사이트 전체를 깨끗한 마크다운으로 추출하는 풀스케일 크롤링까지 완결한다."
              </p>
              <small>— Karim Shoair (D4Vinci), Scrapling 메인 개발자</small>
            </div>

            <p>
              Scrapling은 정적 페이지 수집을 위한 초고속 HTTP 세션부터, 자바스크립트 렌더링이 필수적인 동적 인터랙션, 백그라운드 API 호출 인터셉트, 프록시 로테이션, AutoThrottle, 그리고 일시정지/재개(Pause/Resume) 기능을 매끄러운 단일 API로 통일했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: JA4 핑거프린트 모방과 어댑티브 요소 트래킹
            </h3>
            <p>
              Scrapling이 WAF의 감시망을 무력화하는 기술적 비결은 두 가지다:
            </p>
            <ul>
              <li><strong>스텔스 TLS & HTTP/2 핑거프린트 에뮬레이션:</strong> 실제 최신 크롬/사파리 브라우저의 TLS 암호화 스위트(Cipher Suites) 순서와 JA3/JA4 해시값, HTTP/2 SETTINGS 프레임을 정밀하게 복제하여 방화벽의 핑거프린팅 탐지를 단일 HTTP 요청 레벨에서 회피.</li>
              <li><strong>어댑티브 요소 트래킹(Adaptive Element Tracking):</strong> 대상 사이트의 마크업이나 클래스명이 동적으로 변경되어도, 주변 맥락과 텍스트 패턴을 학습하여 타깃 엘리먼트를 지속 추적하는 파서 아키텍처 내장.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="git-branch" style="color:#0ea5e9;"></i> Scrapling 고속 스텔스 바이패스 파이프라인
                </span>
                <span class="schematic-badge">STEALTH SCRAPING PIPELINE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">JA4/TLS 핑거프린트 위장</div>
                  <div class="step-tech">Stealth HTTP Client (No Headless Browser)</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">Turnstile & WAF 인터셉트 우회</div>
                  <div class="step-tech">Auto Session & Cookie State Sync</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">마크다운 추출 & MCP 에이전트 서빙</div>
                  <div class="step-tech">Adaptive Parser / MCP Server Protocol</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 흐름:</strong> 수백 MB의 헤드리스 크롬 프로세스를 구동하지 않고도, 네트워크 레이어에서 브라우저 핑거프린트를 완전 재현하여 방화벽을 통과하고 즉시 정제된 데이터를 에이전트에 전달합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="terminal"></i> 4. AI 에이전트를 위한 MCP 서버 내장
            </h3>
            <p>
              Scrapling의 또 다른 강력한 강점은 <strong>AI 에이전트 생태계와의 완벽한 융합</strong>이다. 
              내장된 MCP(Model Context Protocol) 서버와 Agent Skill 덕분에, Claude Code나 Cursor 같은 AI 코딩 에이전트가 별도의 파이프라인 구축 없이 <code>scrapling mcp</code> 명령 하나로 웹 전체를 자유롭게 브라우징하고 필요한 정제 마크다운을 컨텍스트로 끌어올 수 있다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="monitor" style="color:#10b981;"></i> Scrapling 공식 스텔스 아키텍처 & 아티팩트
                </span>
                <span class="media-showcase-badge demo">LIVE DEMO CAPTURE</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_scrapling.png" alt="D4Vinci Scrapling Architecture" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 고속 크롤링 파이프라인:</strong> 프록시 로테이션과 어댑티브 파서가 결합되어 대규모 데이터 수집 시 발생하던 차단율을 극소화합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="alert-triangle"></i> 5. 봇 방어와 크롤링의 끝나지 않는 군비경쟁
            </h3>
            <p>
              Scrapling의 등장은 안티봇 보안 벤더들에게 또 다른 숙제를 안겨주었다. 
              그러나 프로젝트 측도 명시하듯, 웹사이트의 이용약관(ToS)과 robots.txt 준수, 데이터 프라이버시 법률 준수는 온전히 개발자의 책임이다. 
              자원 소모를 90% 이상 줄인 이 우아한 파이썬 스크래퍼는 크롤링 엔지니어링의 새로운 기준점으로 자리 잡고 있다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://github.com/D4Vinci/Scrapling" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
