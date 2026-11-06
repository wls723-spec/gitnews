# -*- coding: utf-8 -*-
# Story 1: tembo/voxl (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] tembo/voxl : 오늘의 메인 기사 (COVER STORY) -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_voxl.png" alt="tembo voxl remote desktop" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔥 VNC·RDP의 딜레이를 파괴한 60FPS 브라우저 원격 스트리밍</span>
              <span class="platform-tag">GitHub Breakthrough</span>
              <span class="platform-tag">tembo / voxl</span>
            </div>
            
            <h2 class="main-lead-headline">
              <span id="hero-title">브라우저가 곧 운영체제가 되다 — Rust와 WebCodecs로 빚어낸 60FPS 초저지연 데스크톱 'voxl'</span>
            </h2>

            <div class="article-subheadline">
              무거운 VNC 뷰어와 상용 RDP의 버벅거림을 종식… H.264 실시간 인코딩과 웹소켓 스트림, 브라우저 하드웨어 가속 WebCodecs 직결로 입력 랙을 제로에 수렴시킨 차세대 오픈소스 스트리머
            </div>
            <p class="article-snippet">
              X11, macOS, 윈도우 데스크톱 화면을 초당 60프레임 H.264 비디오로 압축해 브라우저로 쏘아 올리는 초경량 Rust 도구 'voxl'. 별도 앱 설치 없이 링크 클릭만으로 오디오, 마이크, 양방향 클립보드, 파일 전송까지 완결하는 클라우드 워크스페이스의 미래를 조명합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 수십 년간 엔지니어를 괴롭혀온 '원격 데스크톱의 랙(Lag)'
            </h3>
            <p>
              원격 서버나 개발용 가상머신(VM)에 접속해 그래픽 화면을 띄워야 할 때마다 엔지니어들은 깊은 탄식을 내뱉곤 했다. 
              전통적인 VNC(Virtual Network Computing)는 화면이 조금만 바뀌어도 CPU가 치솟으며 마우스 커서가 뚝뚝 끊겼고, 
              마이크로소프트의 독점 RDP나 상용 도구(TeamViewer, AnyDesk)는 전용 클라이언트를 강제하거나 과도한 라이선스 비용을 요구했다.
            </p>
            <p>
              오늘 깃허브 트렌딩 1위에 직행하며 전 세계 개발자들을 환호하게 만든 <strong>tembo/voxl</strong>은 이 해묵은 병목을 가장 우아한 웹 표준 기술로 산산조각 냈다. 
              별도의 프로그램 설치 없이, <strong>크롬이나 사파리 브라우저 창 하나만 열면 리눅스, 맥, 윈도우의 4K 데스크톱이 네이티브 게임처럼 부드러운 60FPS로 펼쳐지는 기적</strong>을 일궈낸 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 브라우저는 이제 완벽한 하드웨어 비디오 디코더다
            </h3>
            <p>
              과거 브라우저 기반 원격 접속(noVNC 등)이 느렸던 이유는 캔버스(HTML5 Canvas)에 수천 장의 JPEG 이미지를 자바스크립트로 일일이 그려 넣는 비효율적인 방식 때문이었다. 
              하지만 현대 브라우저는 완전히 달라졌다.
            </p>

            <div class="editorial-quote danger">
              <p>
                "우리는 더 이상 자바스크립트로 픽셀을 쪼개지 않는다. 
                Rust로 작성된 초경량 서버가 화면을 H.264 스트림으로 인코딩하고, 브라우저는 최신 <strong>WebCodecs API</strong>를 통해 GPU 하드웨어에서 0.001초 만에 비디오 프레임을 직접 풀어낸다."
              </p>
              <small>— Tembo voxl 코어 엔지니어링 릴리즈 노트</small>
            </div>

            <p>
              <code>cargo install voxl-server</code> 명령 하나로 설치하고 터미널에서 실행하면 즉시 보안 서명된 일회용 웹 링크가 출력된다. 
              이 링크를 브라우저에 붙여넣는 순간, 고해상도 모니터 전체가 웹 탭 안에 한 치의 지연 없이 미러링된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: H.264 파이프라인과 초저지연 양방향 I/O
            </h3>
            <p>
              voxl이 상용 원격 솔루션을 능가하는 기술적 비결은 러스트의 극단적 메모리 제어와 현대 웹 표준의 절묘한 결합이다:
            </p>
            <ul>
              <li><strong>H.264 실시간 하드웨어 인코딩:</strong> libyuv와 x264 라이브러리를 바인딩하여 데스크톱 프레임버퍼를 즉각 압축. 네트워크 대역폭에 따라 동적으로 비트레이트와 해상도를 실시간 적응.</li>
              <li><strong>단일 웹소켓(WebSocket) 멀티플렉싱:</strong> 비디오 스트림뿐만 아니라 마우스 좌표, 키보드 이벤트, 양방향 클립보드 동기화, 마이크/오디오(Opus 코덱), 파일 드래그 앤 드롭 전송까지 단 하나의 바이너리 웹소켓 세션에서 다중화 처리.</li>
              <li><strong>WebCodecs 기반 클라이언트 디코딩:</strong> 웹 브라우저 내장 WebCodecs <code>VideoDecoder</code>를 호출하여 브라우저 메인 스레드 블로킹 없이 GPU 가속 디코딩 완결.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="git-branch" style="color:#0ea5e9;"></i> voxl 초저지연 웹 원격 데스크톱 파이프라인
                </span>
                <span class="schematic-badge">WEBRTC & WEBCODECS ACCELERATION</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">데스크톱 프레임 버퍼 캡처</div>
                  <div class="step-tech">X11 / macOS CoreGraphics / Windows DDA</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">Rust H.264 고속 인코딩</div>
                  <div class="step-tech">libyuv + x264 + Opus Audio Encoder</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">브라우저 WebCodecs 직결</div>
                  <div class="step-tech">Hardware GPU Decoding (60FPS Zero-Lag)</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 원리:</strong> 기존 VNC의 캔버스 렌더링 한계를 벗어나 유튜브나 넷플릭스를 재생하듯 브라우저의 GPU 비디오 디코더를 원격 화면에 직접 연결함으로써 반응 속도를 물리 모니터 수준으로 끌어올립니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="monitor"></i> 4. 클라우드 개발 환경의 패러다임 전환
            </h3>
            <p>
              voxl의 등장은 최근 급부상한 AI 에이전트 환경과도 완벽하게 맞아떨어진다. 
              도커(Docker) 컨테이너나 헤드리스 클라우드 인스턴스 안에서 AI 에이전트(Claude Code, Antigravity)가 웹 브라우저나 데스크톱 GUI를 조작하는 모습을, 개발자가 자기 노트북 브라우저 탭에서 실시간으로 감시하고 마우스로 개입할 수 있기 때문이다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="monitor" style="color:#10b981;"></i> voxl 실제 저장소 및 스트리밍 파이프라인
                </span>
                <span class="media-showcase-badge demo">OFFICIAL REPO PREVIEW</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_voxl.png" alt="voxl remote desktop in action" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 공식 벤치마크 & 퀵스타트:</strong> H.264 인코더와 WebCodecs 디코더 파이프라인으로 60FPS 브라우저 스트리밍을 달성한 공식 아키텍처.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="zap"></i> 5. 시사점: 설치형 소프트웨어의 완전한 웹 귀속
            </h3>
            <p>
              더 이상 복잡한 VPN과 포트 포워딩, 무거운 VNC 클라이언트를 설치할 필요가 없다. 
              voxl은 고성능 시스템 프로그래밍 언어인 Rust와 현대 브라우저의 강력한 미디어 파이프라인이 만났을 때 어떤 마법이 일어날 수 있는지를 증명한 올해 최고의 인프라 소프트웨어다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://github.com/tembo/voxl" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
