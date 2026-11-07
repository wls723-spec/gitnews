# -*- coding: utf-8 -*-
# Story 2: mitchellh/ghostty & libghostty 1.0

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 2] mitchellh/ghostty : libghostty 1.0 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_ghostty.jpg" alt="Ghostty and libghostty terminal library" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="terminal" style="width:12px;height:12px;fill:#fff;"></i> HN TOP #2</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 하시코프 창업자의 3년 집념이 빚어낸 시스템 공학의 걸작</span>
              <span class="platform-tag">Hacker News 1,007 Pts</span>
              <span class="platform-tag">mitchellh / ghostty</span>
            </div>
            
            <h2 class="article-lead-headline">
              모든 소프트웨어에 네이티브 GPU 터미널을 심다 — 미첼 하시모토의 'libghostty 1.0' 전격 공개
            </h2>

            <div class="article-subheadline">
              테라폼과 배그런트를 창조한 거장의 귀환… 50년 묵은 VT100 터미널 에뮬레이터를 현대적 GPU 가속 C 라이브러리로 분리하여 에디터, 게임, IDE 어디든 단 1줄로 임베딩
            </div>
            <p class="article-snippet">
              하시코프(HashiCorp) 창업자 미첼 하시모토가 3년간 개발해온 초고속 터미널 고스티(Ghostty)의 코어 엔진을 독립 C 라이브러리 'libghostty 1.0'으로 릴리즈했습니다. 무거운 Electron 웹뷰(xterm.js)나 구형 C 라이브러리에 얽매여 있던 전 세계 개발 도구 생태계에 120FPS 네이티브 터미널의 새 지평이 열렸습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 전설적 시스템 빌더가 다시 터미널을 잡았을 때
            </h3>
            <p>
              인프라 자동화 도구 테라폼(Terraform)과 배그런트(Vagrant)를 만들고 유니콘 기업 하시코프를 일궈냈던 미첼 하시모토(Mitchell Hashimoto)가 경영 일선에서 물러난 뒤 시작한 프로젝트는 뜻밖에도 '터미널 에뮬레이터'였다. 
              수많은 이들이 "왜 이미 넘쳐나는 터미널을 또 만드는가?"라고 의아해했지만, 그의 시선은 단순한 터미널 창 너머를 바라보고 있었다.
            </p>
            <p>
              그 3년간의 집념이 오늘 마침내 <strong>libghostty 1.0</strong>이라는 역사적인 결실로 공개되었다. 
              해커뉴스에서 1,000개가 넘는 업보트를 기록하며 폭발적 반응을 이끌어낸 이 릴리즈는, 
              Ghostty의 강력한 GPU 렌더링, 정교한 ANSI/VT 파서, 유니코드 15.1 텍스트 셰이핑 엔진을 <strong>어떤 프로그래밍 언어(C, C++, Rust, Swift, Go, Python)에서든 직접 호출할 수 있는 순수 C 호환 라이브러리</strong>로 완전히 분리해낸 기술적 쾌거다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 일렉트론 xterm.js의 늪에서 탈출할 열쇠
            </h3>
            <p>
              현대 IDE와 텍스트 에디터(VS Code, Cursor 등)가 내장 터미널을 구현할 때 선택할 수 있는 대안은 극도로 제한적이었다. 
              웹뷰(Webview) 안에 캔버스 기반의 무거운 자바스크립트 라이브러리인 <code>xterm.js</code>를 띄워 수백 메가바이트의 RAM을 소모하거나, 
              수십 년 전에 멈춘 구형 C 라이브러리(libvterm)를 가져다 불완전한 유니코드와 폰트 깨짐을 감수해야 했다.
            </p>

            <div class="editorial-quote danger">
              <p>
                "터미널 에뮬레이션은 결코 가벼운 작업이 아니다. 
                VT 상태 기계(State Machine), 대체 스크린 버퍼, 쌍방향 PTY 통신, 양방향 텍스트(BiDi), 폰트 글리프 합자와 GPU 파이프라인이 얽혀 있다. 
                <strong>libghostty는 이 모든 복잡성을 완벽히 캡슐화하여 단일 API 호출로 120FPS 네이티브 렌더링을 제공한다.</strong>"
              </p>
              <small>— 미첼 하시모토, 'Libghostty 1.0' 아키텍처 회고록</small>
            </div>

            <p>
              이제 신생 에디터(Zed 등)부터 게임 엔진, 데이터베이스 GUI, 심지어 모바일 앱까지 개발자들은 터미널 파서를 바닥부터 다시 짤 필요 없이 <code>libghostty</code> 단 하나만 링크하면 최첨단 GPU 가속 터미널 뷰를 즉시 손에 쥘 수 있게 되었다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: Zig 코어와 플랫폼 네이티브 렌더러의 결합
            </h3>
            <p>
              libghostty 1.0이 여타 터미널 라이브러리를 압도하는 기술적 구조는 다음과 같다:
            </p>
            <ul>
              <li><strong>Zig 기반 무결점 VT100/Xterm 파서:</strong> Paul Flo Williams의 파서 상태 기계를 엄격히 구현하고 수십만 개의 퍼징(Fuzzing) 테스트를 통과한 초고속 파서 코어가 메모리 안전성을 담보.</li>
              <li><strong>HarfBuzz 결합 고정밀 텍스트 셰이핑:</strong> Nerd Font 글리프 아이콘, 다국어 합자(Ligatures), 이모지, RTL(오른쪽에서 왼쪽 쓰기) 텍스트를 깨짐 없이 서브픽셀 단위로 정밀 배치.</li>
              <li><strong>플랫폼 분리형 렌더링 백엔드:</strong> macOS의 Metal, 리눅스/윈도우의 OpenGL/Vulkan 셰이더와 직접 연동되는 렌더러 인터페이스를 제공하여 GPU 메모리에서 프레임을 직접 합성.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="layers" style="color:#0ea5e9;"></i> libghostty 1.0 임베디드 아키텍처 스택
                </span>
                <span class="schematic-badge">STANDALONE EMBEDDABLE C LIBRARY</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">POSIX PTY / Process I/O</div>
                  <div class="step-tech">Raw Byte Stream (ANSI / VT Escape Codes)</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">Zig Core Parser & State Engine</div>
                  <div class="step-tech">Unicode 15.1 + HarfBuzz Text Shaping</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">GPU Render Target (Metal / OpenGL)</div>
                  <div class="step-tech">Zero-Copy Surface Direct Embedding (120FPS)</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 원리:</strong> 터미널 에뮬레이터의 I/O, 상태 기계, 폰트 셰이핑, GPU 렌더링 파이프라인을 완전히 모듈화하여 제3자 애플리케이션의 윈도우 서피스(Surface)에 직접 바인딩할 수 있도록 설계되었습니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-check"></i> 4. 비즈니스 해자: 소프트웨어 도구 생태계의 기본 벽돌이 되다
            </h3>
            <p>
              미첼 하시모토가 만든 소프트웨어들의 공통점은 언제나 '전 세계 엔지니어링 생태계의 기초 인프라'가 되었다는 사실이다. 
              Vagrant가 가상 머신 개발 환경을 표준화했고, Terraform이 클라우드 인프라 코드를 표준화했듯, 
              <code>libghostty</code>는 향후 10년간 등장할 모든 차세대 IDE, AI 코딩 에이전트 인터페이스, 원격 워크스페이스의 터미널 표준으로 자리 잡을 가능성이 농후하다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="terminal" style="color:#10b981;"></i> Ghostty 공식 포털 & GPU 가속 터미널 인터페이스
                </span>
                <span class="media-showcase-badge demo">OFFICIAL SITE PREVIEW</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_ghostty.png" alt="Ghostty terminal official interface" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 공식 홈페이지 & 아키텍처:</strong> GPU 가속과 플랫폼 네이티브 UI를 결합한 Ghostty 터미널 에뮬레이터 공식 포털.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="zap"></i> 5. 키커: 장인의 손끝에서 탄생한 영원한 유산
            </h3>
            <p>
              "우리는 복잡한 것을 쉽게 만들기 위해, 가장 깊은 바닥의 코드를 가장 단단하게 벼려야 한다." 
              미첼 하시모토가 50년의 터미널 역사를 현대 하드웨어 위에 다시 쓴 libghostty 1.0은 시스템 소프트웨어 장인 정신이 무엇인지를 전 세계 엔지니어들에게 증명해 보인 역작이다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://ghostty.org" target="_blank" class="project-link demo">
                  <i data-lucide="globe" style="width:16px;height:16px;"></i> 공식 웹사이트 방문
                </a>
                <a href="https://github.com/mitchellh/ghostty" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
