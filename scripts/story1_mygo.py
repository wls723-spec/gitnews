# -*- coding: utf-8 -*-
# Story 1: egoist/mygo (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = r"""
      <!-- ========================================================== -->
      <!-- [HERO 1] egoist/mygo : COVER STORY                         -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_mygo.jpg" alt="MyGo Pure Go Cross-Platform Native GPU and WebView Desktop Framework Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> COVER STORY #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🚀 +135★/d (★7,054) · cgo 없는 7MB 단일 Go 데스크톱·모바일 앱</span>
              <span class="platform-tag">GitHub Trending &amp; Go Systems</span>
              <span class="platform-tag">egoist / mygo</span>
            </div>

            <h2 class="main-lead-headline">
              <span id="hero-title">"Electron의 300MB 껍데기와 cgo 컴파일 지옥을 동시에 끝내다" — 단일 7MB Go 바이너리로 GPU 네이티브 UI와 웹뷰를 모두 그리는 'MyGo'</span>
            </h2>

            <div class="article-subheadline">
              cgo 없이 순수 Go만으로 macOS·Windows·Linux·iOS·Android 바이너리(~7MB)를 크로스 컴파일하고, Metal·Direct3D·OpenGL 직결 네이티브 UI(~44MB RAM)와 OS 내장 웹뷰(~62MB RAM)를 한 창에서 자유롭게 혼합하는 차세대 데스크톱·모바일 프레임워크 (MIT)
            </div>
            <p class="article-snippet">
              데스크톱 앱을 만들 때마다 개발자들은 잔인한 양자택일에 내몰렸습니다. Electron은 거대한 Chromium을 통째로 실어 날라 메모리 수백 MB를 삼키고, 기존 Go·Rust 프레임워크(Wails·Tauri)는 cgo나 C/Rust 툴체인 크로스 컴파일 장벽에 부딪히곤 했습니다. <strong>egoist/mygo</strong>는 <strong>cgo가 완전히 0인 순수 Go</strong>만으로 단일 ~7MB 실행 파일을 뽑아내면서도, 웹 개발자를 위한 <strong>OS 내장 웹뷰 + 자동 생성 TypeScript IPC</strong>와 극한의 성능을 원하는 개발자를 위한 <strong>GPU 직결 네이티브 UI(<code>package ui</code>)</strong>를 한 프레임워크 안에 통합했습니다(★<strong>7,054</strong>·+135★/d).
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
              <i data-lucide="flame"></i> 1. 리드: <code>go run ... init -template native my-app</code> 한 줄이 무너뜨린 크로스 컴파일의 성벽
            </h3>
            <p>
              맥북에서 Windows용 GUI 앱이나 리눅스용 데스크톱 유틸리티를 빌드하려 할 때, Go 개발자라면 누구나 똑같은 벽을 마주한다. 서버 바이너리는 <code>GOOS=windows go build</code> 한 줄이면 3초 만에 떨어지지만, 화면에 창 하나를 띄우려는 순간 C 바인딩(<code>cgo</code>)과 플랫폼별 SDK, WebView2/WebKitGTK 헤더, 그리고 Rust·Node·Xcode가 얽힌 지옥문이 열린다. 결국 많은 팀이 항복하고 Electron에 React를 얹어 150MB짜리 '메모장'을 배포한다.
            </p>
            <p>
              프론트엔드 도구 생태계에서 <code>tsup</code>·<code>esbuild</code> 생태계 기여자로 유명한 <strong>egoist</strong>가 내놓은 <strong><code>MyGo</code></strong>(v0.10.0)는 이 낡은 체념을 정면으로 부순다. <code>go run github.com/egoist/mygo/cmd/mygo@latest init -template native my-app</code>을 치고 실행하면, 웹뷰도 HTML도 JavaScript도 없이 순수 Go 함수가 곧바로 Metal·Direct3D·OpenGL 위에서 60fps+ GPU 네이티브 창을 그려낸다. 게다가 원한다면 같은 앱, 심지어 같은 창 안에 OS 기본 웹뷰를 함께 끼워 넣을 수도 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 왜 '웹뷰 전용'도 '네이티브 전용'도 아닌 하이브리드 순수 Go인가
            </h3>
            <p>
              지난 몇 년간 데스크톱 프레임워크 시장은 두 진영으로 쪼개져 있었다. Tauri·Wails는 OS 내장 웹뷰(WKWebView·WebView2·WebKitGTK)로 바이너리를 줄였지만 여전히 UI는 HTML/CSS/JS에 묶여 있어 창 열림 지연과 웹뷰 프로세스 메모리(~60~120MB)를 피할 수 없었다. 반대로 Fyne·Slint·GPUI 같은 네이티브 툴킷은 웹 생태계의 방대한 컴포넌트(차트, 리치 에디터, Tailwind)를 포기하거나 C/Rust 의존성을 감수해야 했다.
            </p>

            <div class="editorial-quote">
              <p>
                "하나의 MyGo 창은 두 가지 인터페이스 중 하나를 보여주고, <strong>하나의 앱 혹은 하나의 창이 둘을 섞을 수도 있다.</strong> 순수 Go 네이티브 UI는 GPU 위에 직접 그려져 창이 즉시 열리고(메모리 ~44MB, 유휴 CPU 0%), 웹뷰 창은 Go 서비스로부터 TypeScript 클라이언트를 자동 생성해 타입 안전하게 통신한다."
              </p>
              <small>— egoist/mygo 아키텍처 명세 &amp; 공식 벤치마크 (v0.10.0 · ★7,054 · MIT)</small>
            </div>

            <p>
              결정적인 차별점은 <strong>어느 쪽을 택하든 <code>cgo</code>가 전혀 필요 없다</strong>는 사실이다. 리눅스 CI 서버나 맥북 한 대에서 macOS·Windows·Linux 데스크톱 바이너리는 물론, iOS와 Android 앱까지 동일한 Go 코드베이스로 빌드하고 시뮬레이터·실기기 라이브 리로드를 돌릴 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Zero-cgo 듀얼 렌더링 엔진과 타입 자동 생성 IPC
            </h3>
            <p>
              <code>MyGo</code>가 단 <code>~7MB</code> 단일 바이너리 안에 데스크톱·모바일 크로스플랫폼 GUI와 패키징·자동 업데이트 파이프라인까지 모두 우겨넣을 수 있는 기술적 비밀은 세 층위에 있다:
            </p>
            <ul>
              <li><strong>GPU 직결 Go UI 툴킷(<code>package ui</code>):</strong> 뷰를 <code>func(c *ui.Context)</code> 상태 함수로 선언하면 MyGo가 매 프레임을 계산해 macOS Metal, Windows Direct3D, Linux OpenGL로 직접 래스터화한다. Flexbox·Grid 레이아웃, IME 입력기 지원 텍스트 편집, 가상화 리스트, SVG 아이콘, 스크린 리더 접근성, 창 없이 도는 뷰 단위 테스트는 물론 모든 플랫폼에 <code>glass</code> 플러그인으로 Liquid Glass 질감까지 입힌다.</li>
              <li><strong>OS 웹뷰 + 제로 보일러플레이트 TypeScript IPC:</strong> <code>mygo.Bind(Greeter{})</code>로 Go 구조체 메서드를 바인딩하면 빌드 타임에 프론트엔드용 <code>./mygo</code> TypeScript 클라이언트가 자동 생성된다. 프론트엔드는 <code>await Greeter.greet("Ada")</code>처럼 호출하고, Go 채널 기반 스트리밍과 타입드 이벤트를 주고받는다. 심지어 네이티브 UI 창 내부에 웹 페이지를 임베드해 네이티브 메뉴·다이얼로그 아래에서 동작하게 섞는 것도 지원한다.</li>
              <li><strong>네이티브 OS 통합 &amp; 원스톱 배포 파이프라인:</strong> 시스템 트레이, 전역 단축키, 딥링크, 파일 연결, Now Playing 및 미디어 키 제어, 시스템 강조색 감지 같은 데스크톱 API를 모두 품었으며, macOS <code>.app</code>/<code>.dmg</code>(공증·코드 서명 포함), Windows 인스톨러, <code>.deb</code>/<code>.rpm</code>/Arch <code>PKGBUILD</code>, Sparkle 스타일 델타 자동 업데이트 창까지 기본 내장한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">MyGo Zero-cgo 듀얼 UI &amp; 크로스플랫폼 빌드 파이프라인</span>
                <span class="schematic-badge">Pure Go (No CGO) · ~7 MB Binary · 0% Idle CPU</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Pure Go Core &amp; Dual View</div>
                  <div class="schematic-desc">
                    <strong>Native UI:</strong> <code>ui.Context</code> 선언형 Go 뷰 (~44 MB RAM)<br>
                    <strong>Web UI:</strong> WKWebView / WebView2 / WebKitGTK (~62 MB)<br>
                    <strong>Hybrid:</strong> 단일 창 내 네이티브 메뉴 + 웹뷰 혼합<br>
                    <strong>Zero CGO:</strong> C 컴파일러 없이 전 OS 크로스 빌드
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. GPU Rasterizer &amp; Typed IPC</div>
                  <div class="schematic-desc">
                    Metal / Direct3D / OpenGL 직접 GPU 드로잉<br>
                    <code>mygo.Bind(Service{})</code> &rarr; TS 클라이언트 자동 생성<br>
                    Go 채널 실시간 스트리밍 &amp; 타입드 이벤트 버스<br>
                    가상화 리스트 · IME 입력 · Liquid Glass 플러그인
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Desktop, Mobile &amp; Ship</div>
                  <div class="schematic-desc">
                    macOS / Windows / Linux + iOS / Android 동시 지원<br>
                    트레이 · 단축키 · 미디어 키 · 파일 감시 OS API<br>
                    DMG 공증 · Win Installer · DEB/RPM/PKGBUILD<br>
                    서명된 Sparkle 스타일 델타 자동 업데이트 내장
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">mygo.run 공식 실화면 — 단일 ~7MB 바이너리·~44MB 네이티브 메모리·0% 유휴 CPU 벤치마크</span>
              </div>
              <img src="../assets/images/demo_mygo.png" alt="MyGo Official Website Showing Benchmarks and Native UI Example" class="showcase-img">
              <p class="showcase-caption">
                ▲ mygo.run 실화면: Go 1.27+ 및 Bun 기반의 즉시 실행 워크플로우와 ~7MB 바이너리, 네이티브 UI ~44MB / 웹뷰 포함 ~62MB 메모리, 유휴 CPU 0% 실측 지표.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 &amp; 생태계 분기점: Electron·Wails·Tauri 삼국지에 균열을 내다
            </h3>
            <p>
              오랫동안 데스크톱 클라이언트 시장은 '자바스크립트(Electron)'와 '러스트(Tauri)'의 양강 구도였다. Go 진영은 백엔드와 CLI·인프라(Docker, Kubernetes, Terraform)를 장악하고도 데스크톱 UI에서만큼은 Wails의 웹뷰 의존과 <code>cgo</code> 빌드 복잡성 때문에 변방에 머물러 있었다.
            </p>
            <ul>
              <li><strong>1인 개발자·인프라 팀의 풀스택 클라이언트 탈환:</strong> AI 코딩 에이전트 시대에 로컬 백엔드·MCP 서버·TUI 데몬을 Go로 짜는 팀이 폭증하면서, 프론트엔드를 붙이기 위해 Node.js나 Rust를 별도 학습하지 않고도 기존 Go 코드에 즉시 네이티브 UI와 자동 업데이트까지 얹을 수 있는 수요가 폭발하고 있다.</li>
              <li><strong>모바일과 데스크톱의 경계 소멸:</strong> iOS App Store와 Google Play 빌드까지 한 프레임워크에서 공식 지원하는 점은, React Native·Flutter가 차지하던 중소형 유틸리티 및 AI 컴패니언 앱 시장에서도 Go 단일 스택의 실전 채택 가능성을 열어젖힌다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 가벼움은 타협이 아니라 아키텍처의 승리다
            </h3>
            <p>
              사용자의 16GB 노트북 램을 채팅 앱과 메모장 서너 개가 몽땅 집어삼키는 시대, 7MB짜리 단일 바이너리가 44MB의 메모리로 0% 유휴 점유율을 지키며 즉시 창을 여는 모습은 일종의 해방감을 준다.
            </p>
            <p>
              웹의 유연함이 필요하면 OS 웹뷰를 빌려 쓰고, 날것의 속도가 필요하면 Go 함수가 직접 GPU를 호출한다. <code>MyGo</code>는 '크로스플랫폼은 원래 무겁고 느리다'는 업계의 핑계를 조용히 무효화하고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=egoist+mygo+golang+desktop+app" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://mygo.run" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> 공식 문서 &amp; 벤치마크
              </a>
              <a href="https://github.com/egoist/mygo" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
