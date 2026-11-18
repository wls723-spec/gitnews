# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-19

FULL_MINORS_SECTION = """
    <!-- ========================================================== -->
    <!-- [SECTION 9] 실시간 극초기 레이더 (마이너 브리핑 18선) -->
    <!-- ========================================================== -->
    <section class="minor-radar-section" id="minor-radar">
      <div class="minor-radar-header">
        <div class="minor-title-group">
          <span class="aggro-tag" style="background:#fef08a; border-color:#ca8a04; color:#854d0e;">⚡ 실시간 극초기 레이더</span>
          <h2 class="minor-section-title">갓 태어난 극초신성 &amp; 실시간 급상승 유망주 18선</h2>
        </div>
        <p class="minor-section-desc">
          직전 발행(11월 18일) 이후 30시간 동적 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다. 스팸·빈 저장소·기발행 중복 이력 배제 및 재귀적 동일 주제 클러스터링 알고리즘이 적용되었습니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: mitsuhiko/tvpipe -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 21개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.6시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 2.09 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Flask 창시자 Armin Ronacher의 초저지연 AirPlay·Google Cast 미러링 CLI&quot; : tvpipe</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">mitsuhiko/tvpipe — URL 재생이 아닌 실시간 미러링 프로토콜로 어떤 영상·오디오든 TV에 즉각 전송하는 Rust Apache-2.0 도구</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">Apple TV와 Chromecast를 터미널 한 줄로 통합하는 초저지연 실시간 캐스팅 파이프</h3>
            <div class="minor-detail-subheadline">Apache-2.0 라이선스 · Rust 기반 · AirPlay 페어링 및 Google Cast·브라우저 탭 동시 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  스마트 TV로 로컬 미디어나 화면을 쏠 때, 기존 캐스팅 툴은 HTTP URL을 넘겨 TV가 다시 받아오게 하거나 큰 버퍼링 지연을 유발했습니다. Flask 창시자로 유명한 Armin Ronacher(<code>mitsuhiko</code>)가 AirPlay와 Google Cast의 실시간 미러링 프로토콜을 직접 구현해 공개한 Rust CLI가 9.6시간 만에 21스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[미러링 루프]</strong> <code>tvpipe discover</code> &rarr; <code>tvpipe pair</code> &rarr; Real-Time AirPlay / Cast Stream (&lt;1s Latency)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  에어플레이와 크롬캐스트 양대 폐쇄 생태계의 실시간 스트리밍 핸드셰이크를 단일 Rust 바이너리로 녹여내, 스크립트 자동화와 홈랩 미디어 제어에 즉시 활용 가능합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://mitsuhiko.github.io/tvpipe" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 매뉴얼
              </a>
              <a href="https://github.com/mitsuhiko/tvpipe" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: 3d3dcanada/stella-scope-community -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 11개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.11 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Klipper·Prusa·FlashForge 3D 프린터 팜 전체를 3D 뷰와 블랙박스 비행기록장치로 통합 관제&quot; : Stella Scope</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">3d3dcanada/stella-scope-community — 수십 대 프린터의 상태를 한 화면에 띄우고 모든 출력 순간을 녹화·리플레이하는 Rust AGPL-3.0 콕핏</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">출력 실패 원인을 항공기 블랙박스처럼 되감아 분석하는 3D 프린트 팜 관제실</h3>
            <div class="minor-detail-subheadline">AGPL-3.0 라이선스 · Rust v0.6.3 공개 · Klipper·Prusa·FlashForge 멀티 벤더 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  여러 대의 3D 프린터를 동시에 돌리는 팜 운영자들은 제조사마다 제각각인 웹 UI를 오가며 출력 실패 원인을 추측해야 했습니다. <code>stella-scope-community</code>는 팜 전체를 단일 3D 팜 월(Farm Wall)로 시각화하고 모든 텔레메트리를 재생 가능한 비행 기록으로 남깁니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[팜 관제]</strong> Klipper / Prusa / FlashForge Telemetry &rarr; Rust Flight Recorder &rarr; Unified 3D Farm Wall &amp; Replay
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  실시간 모니터링과 사후 텔레메트리 리플레이를 통합해, 제조 하드웨어 자동화의 디버깅 효율을 크게 높여주는 오픈소스 현장 툴입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://3d3d.ca/software/stella" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 페이지
              </a>
              <a href="https://github.com/3d3dcanada/stella-scope-community" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: Spartakusovec/apogee -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 1개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 1.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.97 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Wayland Sway 타일링 WM 위에 macOS·GNOME급 통합 데스크톱 셸을 얹는 단일 Rust 바이너리&quot; : Apogee</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Spartakusovec/apogee — 상단 바·독·Spotlight 검색·알림·Wi-Fi·설정 앱까지 단 하나의 Rust+GTK 4 프로세스로 통합</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">파편화된 Sway 설정 파일과 수십 개 데몬을 단 하나의 GTK 4 통합 셸로 압축</h3>
            <div class="minor-detail-subheadline">Rust + GTK 4 기반 · Sway 1.11+ 타일링 유지 · 일체형 독·런처·시스템 설정</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  리눅스 Sway 사용자는 Waybar, Rofi, Mako, 설정 유틸리티 등 대여섯 개의 별도 프로그램을 조립하느라 큰 설정 피로를 겪습니다. 공개 1시간 만에 레이더에 포착된 <code>Apogee</code>는 Sway의 타일링 본체를 유지하면서도 모든 데스크톱 UI 요소를 단일 프로그램에 묶어냈습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[단일 셸]</strong> Sway Wayland Compositor &harr; Single Rust+GTK4 Process (Bar + Dock + Spotlight + Settings)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  IPC 오버헤드와 파편화된 테마 불일치를 없애고, 타일링 윈도우 매니저의 효율성과 완성형 데스크톱의 편의성을 동시에 추구하는 흥미로운 시도입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Spartakusovec/apogee" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: geerlingguy/chronytop -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 110개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 19.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 5.53 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Jeff Geerling이 만든 btop 감성의 chrony NTP 타임 서버 실시간 TUI 모니터&quot; : chronytop</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">geerlingguy/chronytop — 초당 NTP 요청 그래프·Rate-limit 클라이언트·소스 추적·대역폭을 터미널에서 실시간 시각화하는 Go MIT 도구</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">텍스트 명령어(chronyc)만 뚫어져라 보던 NTP 서버 운영자를 위한 미려한 btop 스타일 대시보드</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Go 기반 · Linux chrony 4.0+ 실시간 패널 리사이징·토글 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  인프라 자동화의 거장 제프 기얼링(Jeff Geerling)이 자체 NTP 타임 서버 운영 중 <code>chronyc</code> 텍스트 출력의 한계를 느끼고 직접 만든 <code>btop</code> 스타일 TUI 대시보드가 20시간 만에 110스타를 돌파했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[NTP 관제]</strong> <code>chronyc</code> Metrics &amp; Server Stats &rarr; Go TUI Engine &rarr; Live RPS Graph, Rate-Limited Clients &amp; Drift View
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  별도 웹 모니터링 스택(Prometheus/Grafana) 없이도 SSH 접속만으로 분산 시스템 시간 동기화 이상과 NTP 증폭/남용 클라이언트를 즉시 포착할 수 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/geerlingguy/chronytop" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: pookjw/Clocky -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 68개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.61 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;탈옥도 시스템 파일 변조도 없이 모든 Apple Watch 페이스를 띄우는 앱&quot; : Clocky</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">pookjw/Clocky — watchOS 기종·지역 제한에 묶여 있던 애플 워치 페이스를 Objective-C 네이티브 앱 내부에서 해금하는 GPL-3.0 프로젝트</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">MobileGestalt 수정 없이 애플의 '기종별 워치 페이스 잠금'을 우회한 watchOS 해킹 연구</h3>
            <div class="minor-detail-subheadline">GPL-3.0 라이선스 · Objective-C · 모든 watchOS 버전 호환</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  애플은 Hermès 에디션이나 Ultra 전용 워치 페이스를 일반 Apple Watch에서 쓰지 못하도록 소프트웨어로 엄격히 잠가두었습니다. <code>Clocky</code>는 위험한 탈옥이나 <code>MobileGestalt</code> 변조 없이 앱 샌드박스 내부에서 원하는 워치 페이스를 구동하는 방법을 공개해 14.8시간 만에 68스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[하드웨어 해금]</strong> Standard watchOS App Sandbox &rarr; Native Face Presentation Bridge &rarr; Render Restricted Watch Faces
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  제조사가 인위적으로 묶어둔 하드웨어-소프트웨어 기능 잠금을 역공학으로 탐구하며 사용자 커스터마이징 권리를 확장한 사례로 주목받고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/pookjw/Clocky" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: eddiezywang/wemail -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 68개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 16.5시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.13 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;클라우드 사서함 업로드 없이 내 PC SQLite로 동기화하는 로컬 우선 AI 이메일 클라이언트&quot; : WeMail</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">eddiezywang/wemail — IMAP/SMTP 메일을 로컬 DB에 저장하고 원하는 AI로 요약·라벨링·답장 초안·투두 추출을 자동화하는 Apache-2.0 앱</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">제3자 클라우드 서버에 회사 메일 토큰을 넘기지 않는 프라이버시 중심 AI 메일 워크벤치</h3>
            <div class="minor-detail-subheadline">Apache-2.0 라이선스 · TypeScript / Electron 41 · macOS &amp; Windows 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  기존 AI 이메일 앱들은 요약 기능을 제공하는 대가로 사용자의 전체 메일함을 자체 클라우드에 미러링해 보안 우려가 컸습니다. <code>WeMail</code>은 표준 IMAP/SMTP로 내 PC SQLite에만 메일을 동기화한 뒤 사용자가 지정한 AI 파이프라인을 로컬에서 스케줄링해 68스타를 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[로컬 AI 메일]</strong> IMAP/SMTP Sync &rarr; Local SQLite Store &rarr; User-Selected LLM Pipeline (Summary / Tags / Draft / Todo)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  데이터 주권을 지키는 로컬-퍼스트(Local-First) 아키텍처와 멀티스텝 에이전트 트리아지 워크플로우를 매끄럽게 결합한 오픈소스 대안입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://eddiezywang.github.io/wemail/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 웹사이트
              </a>
              <a href="https://github.com/eddiezywang/wemail" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: ChrisTitusTech/lg-debloat -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 170개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.73 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;거실 LG 스마트 TV의 광고·프로모션·백그라운드 블로트웨어를 안전하게 걷어내는 디블로터&quot; : lg-debloat</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">ChrisTitusTech/lg-debloat — 루팅된 LG webOS 2+ TV에서 Plex·YouTube는 살리고 홍보 배너와 선로딩 앱만 가역적으로 숨기는 MIT 스크립트</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">수백만 원짜리 TV가 거대한 광고판이 된 시대에 되찾는 '내 거실 화면의 통제권'</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Python + OpenSSH · 변경 이력 기록 및 원클릭 원복(Undo) 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  유명 테크 크리에이터 크리스 타이터스(Chris Titus)가 최신 스마트 TV OS의 노골적인 홈 화면 광고와 백그라운드 앱 사전 로딩을 억제하기 위해 공개한 <code>lg-debloat</code>가 25시간 만에 170스타를 기록하며 폭발적인 공감을 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[TV 클리닝]</strong> Root SSH to LG webOS &rarr; Disable Promo Flags &amp; Preload &rarr; Save Undo Snapshot (Keep Plex/YouTube)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  시스템 앱을 무작정 삭제해 벽돌을 만드는 대신 안전하게 숨기고 비공개 롤백 로그를 남겨, 가전제품 소유권(Right to Own) 운동의 실용적 도구가 되었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/ChrisTitusTech/lg-debloat" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: comp-work/gke-sandboxes -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 59개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.5시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 2.14 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;유료 샌드박스 SaaS(시간당 16.6¢)의 1/8 가격(1.9¢)으로 돌리는 셀프호스팅 GKE 에이전트 샌드박스&quot; : gke-sandboxes</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">comp-work/gke-sandboxes — 내 구글 클라우드 GKE 위에서 gVisor와 파일시스템 스냅샷 기반 수면·재개를 구현하는 Apache-2.0 인프라</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">Daytona·E2B 대비 88% 저렴한 시간당 1.9센트로 에이전트 전용 리눅스 환경 구축</h3>
            <div class="minor-detail-subheadline">Apache-2.0 라이선스 · TypeScript · gVisor 격리 + 유휴 시 스토리지 비용만 과금</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  에이전트용 클라우드 샌드박스 상용 SaaS들이 2 vCPU/4 GB 기준 시간당 16.6센트 수준의 높은 마진을 붙이는 가운데, 자체 GCP 프로젝트의 GKE와 gVisor를 조합해 비용을 시간당 약 1.9센트까지 낮춘 구현체가 등장해 59스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[초저가 샌드박스]</strong> Agent Task &rarr; GKE gVisor Sandbox (~1.9¢/h) &harr; Sleep Filesystem Snapshot (Storage Only)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  사용자가 자리를 비우면 샌드박스를 재우고 동일 ID로 복원하는 단순 명쾌한 패턴으로, 클라우드 에이전트 인프라의 '셀프호스팅 회귀' 흐름을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/comp-work/gke-sandboxes" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: Tpojka/neleceni -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 56개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.92 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;TV 뉴스 유튜브 스트림 속 특정 인물 자막을 OCR로 실시간 감지해 자동 음소거하는 크롬 확장&quot; : Neleceni</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Tpojka/neleceni — 화면 하단 발언자 이름표를 실시간 판독해 내가 지정한 정치인·패널이 나올 때만 소리를 끄는 MIT 브라우저 확장</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">영상 자막(Chyron) 인식 기반 실시간 '발언자 선택적 음소거'라는 기발한 브라우저 해킹</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · TypeScript · Chrome Web Store 공식 배포</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  실시간 유튜브 뉴스 방송을 틀어두고 일하다가 특정 정치인이나 패널이 등장할 때마다 손으로 음소거를 누르던 불편을 해결하기 위해, 세르비아 개발자가 방송 자막 배너의 이름을 실시간 추적해 오디오를 자동 차단하는 확장을 공개해 56스타를 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[영상 필터링]</strong> YouTube Video Frame &rarr; On-Screen Chyron OCR Match &rarr; Auto Mute / Unmute Audio Tab
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  거창한 서버 백엔드 없이 클라이언트 측 영상 프레임 인식만으로 정보 피로를 제어하는 '개인 맞춤형 마이크로 소프트웨어'의 매력을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://chromewebstore.google.com/detail/neleceni/ffkbnnalhdnnnaeemojkmgpajmaagnjl" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Chrome Web Store
              </a>
              <a href="https://github.com/Tpojka/neleceni" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: Gemini 4 Neon -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 239 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 1.2시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 199.41 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;구글 딥마인드, 초고속·고효율 차세대 플래그십 라인업 'Gemini 4 Neon' 전격 공개&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">blog.google — 공개 1.2시간 만에 239점·233댓글 폭발, '이번 달에만 벌써 4번째 모델 릴리즈'라며 술렁이는 AI 업계</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">초당 200포인트 속도로 HN을 점령한 구글의 파상 공세 'Gemini 4 Neon'</h3>
            <div class="minor-detail-subheadline">1.2시간 만에 233개 댓글 · 프론티어 모델 출시 주기 가속화 논쟁</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  구글이 Gemini 4 시리즈의 신형 모델 'Gemini 4 Neon'을 발표하자마자 Hacker News에서 시간당 199.41포인트라는 압도적 속도로 1위에 올랐습니다. 최근 연속적인 모델 공개 릴레이와 맞물려 커뮤니티의 이목이 집중됐습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[모델 공세]</strong> Gemini 4 Series Cadence &rarr; Gemini 4 Neon Launch &rarr; Speed/Cost Frontier Benchmark Shift
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  개발자들은 "구글의 릴리즈 속도가 이번 달에만 네 번째"라며 놀라움을 표했고, 에이전트 워크플로우에서의 지연시간·추론 단가 경쟁이 한층 격화될 것으로 내다봤습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 구글 공식 발표
              </a>
              <a href="https://news.ycombinator.com/item?id=50552424" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (239 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: Unauthenticated RCE in Nginx (Wiz) + CVE-2026-123007 cluster -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 958 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 128.85 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;전 세계 웹 서버의 심장 Nginx에서 무인증 원격 코드 실행(HTTP/2 RCE, CVE-2026-123007) 발견&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">wiz.io — 958점·442댓글 초비상, GitHub PoC(sfewer-r7)와 익스플로잇(NGINX2Root)까지 연쇄 공개된 인터넷 인프라 위기</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">HTTP/2 정수 언더플로우를 타고 Nginx 방문자에서 호스트 루트까지 뚫리는 치명적 RCE</h3>
            <div class="minor-detail-subheadline">442개 댓글 · 파생 생태계(sfewer-r7/CVE-2026-123007 PoC · NGINX2Root) 클러스터 통합 · 즉시 패치 권고</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  보안 기업 Wiz가 Nginx HTTP/2 구현체의 정수 언더플로우 기반 무인증 원격 코드 실행(RCE) 취약점을 공개하자마자, GitHub의 Rapid7 연구원(<code>sfewer-r7/CVE-2026-123007</code>, ★91)의 PoC와 <code>NGINX2Root</code>(HN 93점) 등 파생 익스플로잇이 몇 시간 만에 쏟아지며 전 세계 인프라 팀에 비상이 걸렸습니다. (동일 사건 파생 항목 일괄 통합)
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[취약점 경로]</strong> Malformed HTTP/2 Frame &rarr; Nginx Integer Underflow &rarr; Heap Corruption &rarr; Unauthenticated RCE
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  리버스 프록시와 인그레스 게이트웨이 앞단에 깔린 Nginx 특성상 방화벽을 관통해 직접 노출되는 경우가 많아, 즉각적인 버전 업그레이드와 HTTP/2 완화 조치가 필수적입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Wiz 보안 분석 원문
              </a>
              <a href="https://github.com/sfewer-r7/CVE-2026-123007" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> PoC 저장소 참고
              </a>
              <a href="https://news.ycombinator.com/item?id=50547374" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (958 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: Microsoft Ignite 2026 Seven New Models + MAI Code 2 cluster -->
        <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 380 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 57.34 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;마이크로소프트 Ignite 2026, 자체 AI 파운데이션 7종(MAI Code 2·Flash 포함) 가성비 공세&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">microsoft.ai — 380점·262댓글, OpenAI 의존에서 벗어나 독자 MAI 모델군 가격 경쟁력을 전면 배치한 MS의 승부수</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">GPT-6 Luna 대비 65% 단가를 내세운 'MAI Code 2 Flash' 등 MS 독자 모델 라인업 총출동</h3>
            <div class="minor-detail-subheadline">262개 댓글 · MAI Code 2 &amp; Code 2 Flash(415 pts) 발표 클러스터 통합 · 추론 가격 전쟁</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  마이크로소프트가 Ignite 2026에서 자체 개발한 신규 모델 7종과 코딩 특화 모델 <code>MAI Code 2</code> 및 <code>Code 2 Flash</code>(HN B3 415점 통합)를 동시 발표하며, 프론티어급 성능을 훨씬 낮은 추론 비용으로 제공하겠다고 선언해 380점을 기록했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[독자 모델 전략]</strong> Microsoft AI (MAI) 7-Model Suite &rarr; MAI Code 2 / Flash &rarr; 35% Lower Inference Cost
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  개발자들은 <code>MAI Code 2 Flash</code>의 가격 효율성이 코딩 에이전트 뿐 아니라 범용 에이전트 루프 전반에서 토큰 비용을 낮출 잠재력에 주목했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://microsoft.ai/news/microsoft-ignite-2026/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> MS Ignite 발표
              </a>
              <a href="https://news.ycombinator.com/item?id=50548021" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (380 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: AI is killing All About Berlin -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 744 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 16.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 46.57 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;AI 검색 요약이 독립 전문 정보 사이트를 죽이고 있다: 'All About Berlin' 운영자의 절규&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">nicolasbouliane.com — 744점·678댓글 대격론, 구글 AI 답변으로 검색 트래픽 40%가 증발하며 흔들리는 웹의 생태계</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">1차 검증 가이드를 긁어가 답변만 띄우는 AI 시대, 누가 여전히 원본 문서를 업데이트할 것인가</h3>
            <div class="minor-detail-subheadline">678개 댓글 폭발 · '구글 AI 답변 트래픽 40% 감소' 현상과 맞물린 오픈웹 지속가능성 위기</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  수년간 베를린 정착과 비자·세무 가이드를 직접 취재해 올리던 유명 독립 사이트 운영자가 AI 요약으로 인한 검색 유입 급감과 수익 붕괴 데이터를 공개하자 744점·678댓글이 몰렸습니다. 같은 날 올라온 검색 트래픽 40% 감소 리포트와 맞물려 큰 반향을 일으켰습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[웹 생태계 역설]</strong> Human Updates Primary Guide &rarr; AI Scraping &amp; Zero-Click Answer &rarr; Traffic -40% &rarr; Source Dies
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  AI가 인용할 최신 1차 정보 자체를 생산하는 독립 퍼블리셔들이 고사할 경우, 결국 LLM 응답의 신선도와 정확도까지 동반 추락하는 '모래성 딜레마'가 공론화됐습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://nicolasbouliane.com/blog/death-by-ai" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 운영자 포스트모텀 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50542705" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (744 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: Codeberg.org Not Reachable (NameSilo Domain Suspension cluster) -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 293 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 23.02 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;비영리 오픈소스 Git 호스팅 'Codeberg.org', 레지스트라(NameSilo) 계정에서 도메인이 돌연 정지·소실돼 전면 불통&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">codebergstatus — 293점·295댓글, DNS 레코드 증발로 수만 오픈소스 저장소가 멈추며 불거진 도메인 단일 장애점 논란</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">아무리 완벽히 셀프호스팅해도 도메인 레지스트라 버튼 하나에 서비스 전체가 증발하는 현실</h3>
            <div class="minor-detail-subheadline">295개 댓글 · DNS 소실·도메인 이슈 후속 스레드 클러스터 통합 · 유럽/비영리 인프라 레지스트라 리스크</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  GitHub의 비영리 대안으로 각광받던 <code>Codeberg.org</code>가 DNS에서 완전히 사라지는 초유의 장애가 발생했습니다. Codeberg 측은 도메인 등록기관인 NameSilo 계정에서 도메인이 사라지고 일방 정지(Suspended)된 사실을 확인하며 긴급 대응에 나섰습니다. (관련 DNS 소실 및 도메인 이슈 보고 통합)
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[단일 장애점]</strong> NameSilo Registrar Suspension &rarr; <code>codeberg.org</code> DNS Vanishes &rarr; Global Git/CI Outage
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  커뮤니티에서는 <code>.org</code>와 미국 기반 저가 레지스트라의 자동화된 남용 신고·정지 시스템이 핵심 오픈소스 인프라를 마비시킬 수 있다며, 이중 도메인 및 레지스트라 보안 잠금의 필요성을 강하게 제기했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://social.anoxinon.de/@codebergstatus/117636437840688845" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Codeberg 공식 상태 공지
              </a>
              <a href="https://news.ycombinator.com/item?id=50544261" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (293 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: Energy-Based Reasoners (385x / 1000x cluster) -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 293 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.3시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 22.07 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;자기회귀 CoT 없이 에너지 최소화로 추론하는 'Energy-Based Reasoners', 추론 효율 385배 달성&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">energy-based-reasoners.github.io — 293점, 수백 토큰을 줄줄이 생성하는 대신 연속 에너지 지형 수렴으로 추론 비용을 혁명하는 연구</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">토큰 낭비형 사고 사슬(CoT)의 대안으로 떠오른 에너지 기반 비자기회귀 추론 아키텍처</h3>
            <div class="minor-detail-subheadline">49개 댓글 · arXiv:2611.17309(고전 에너지 1000배 속도 비교) 클러스터 통합 · 비전형 추론 패러다임</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  LLM의 테스트 타임 연산을 늘리기 위해 수천 개의 사고 토큰을 순차 생성하는 방식이 병목에 부딪히자, 해 공간의 에너지 함수를 최소화해 답으로 수렴하는 <code>Energy-Based Reasoners</code>(추론 효율 385배)와 관련 고전 에너지 추론 논문(<code>arXiv:2611.17309</code>, 1,000배 빠름)이 동시에 HN의 주목을 받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[에너지 추론]</strong> Constraint / Problem State &rarr; Iterative Energy Minimization (Non-Autoregressive) &rarr; 385x Efficient Solution
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  댓글에서는 현재의 EBR 벤치마크가 범용 언어 추론과 다른 조합 최적화 성격이라는 신중론과 함께, 그럼에도 토큰 순차 생성 패권을 흔들 차세대 잠재 아키텍처라는 기대가 교차했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://energy-based-reasoners.github.io/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 프로젝트 페이지
              </a>
              <a href="https://news.ycombinator.com/item?id=50543989" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (293 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: Quad9's withdrawal from France -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 879 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 24.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 35.82 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;비영리 DNS 리졸버 Quad9의 프랑스 철수: 인터넷 발칸화를 예고하는 탄광 속 카나리아&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">blog.cloudflare.com — 879점·427댓글, 불법 복제 차단을 이유로 DNS 리졸버에 검열 의무를 부과한 법원 명령의 파장</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">저작권 단체의 DNS 차단 명령에 무너지는 중립적 글로벌 인터넷 인프라</h3>
            <div class="minor-detail-subheadline">427개 댓글 · B1 후속 분석('DNS 리졸버는 저작권 단속처가 아니다', 532 pts) 통합 · 인터넷 거버넌스 위기</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  스위스 비영리 보안 DNS 서비스 Quad9이 프랑스의 반복적인 저작권 DNS 차단 명령과 법적 부담을 견디지 못하고 프랑스 시장에서 철수하자, 클라우드플레어가 "자유로운 글로벌 인터넷이 국가별 인터넷으로 쪼개지는 시작점"이라며 강하게 경고해 879점을 기록했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[인프라 위축]</strong> National Copyright Blocking Order &rarr; Non-Profit DNS Resolver Forced Exit &rarr; Fragmented Internet
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  인터넷의 가장 기초적인 주소록(DNS)을 콘텐츠 검열 기관으로 강제할 때 결국 소규모·비영리 인프라부터 고사하고 거대 독점 사업자만 남게 된다는 거버넌스 경고가 이어졌습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://blog.cloudflare.com/quad9-withdrawal-from-france/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Cloudflare 분석 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50538994" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (879 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: Nvidia stopped disclosing Singapore sales as revenues hit $104B -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 656 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 22.19 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;엔비디아, 매출 1,040억 달러 돌파 시점에 돌연 '싱가포르 매출 공시' 중단&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">ft.com — 656점·295댓글, 수출 통제 우회 허브 의혹이 집중되던 싱가포르 청구 비중을 재무제표에서 지운 지정학적 파장</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">미국 GPU 수출 규제와 싱가포르 경유 논란 한복판에서 사라진 지역별 매출 주석</h3>
            <div class="minor-detail-subheadline">295개 댓글 · Financial Times 단독 분석 · AI 반도체 공급망 투명성 논쟁</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  엔비디아의 전체 매출이 1,040억 달러를 돌파한 최신 공시에서 그동안 시장과 규제 당국의 예의주시 대상이었던 싱가포르향 매출 분리 공시가 돌연 제외되었다는 파이낸셜타임스(FT) 보도가 656점을 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[지정학 리스크]</strong> $104B Revenue Milestone &rarr; Singapore Breakdown Omitted &rarr; Export Control Scrutiny Intensifies
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  글로벌 AI 데이터센터용 GPU 물류가 청구지(Billing)와 실제 물리적 클러스터 설치지 간의 괴리를 안고 있는 구조 속에서, 칩 수출 통제와 클라우드 우회 접근을 둘러싼 공방이 더욱 거세지고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.ft.com/content/dbde7a30-548c-4f9d-a4be-7898a0c24dcf" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Financial Times 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50534631" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (656 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: Microsoft's ONNX Runtime has disappeared from GitHub -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 449 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 23.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 19.14 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;스타 2만2천 개짜리 핵심 AI 추론 엔진 'Microsoft ONNX Runtime', GitHub에서 돌연 증발&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">github.com/microsoft/onnxruntime — 449점·97댓글, 사전 예고 없는 저장소 404화로 전 세계 CI·평가 파이프라인 연쇄 중단</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">대체 불가 표준 오픈소스 저장소가 아무 경고 없이 사라졌을 때 드러난 공급망 취약성</h3>
            <div class="minor-detail-subheadline">97개 댓글 · CI/CD 빌드 장애 보고 쇄도 · 오픈소스 미러링 및 벤더 의존성 성찰</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  수많은 로컬 AI 앱과 모델 평가 파이프라인이 의존하는 핵심 크로스플랫폼 추론 엔진 <code>microsoft/onnxruntime</code>(★22,000+)이 아무런 사전 공지 없이 GitHub에서 접근 불가(사라짐) 상태가 되면서 449점을 기록했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[빌드 쇼크]</strong> <code>microsoft/onnxruntime</code> Goes Dark &rarr; Upstream Git Fetch Fails &rarr; Global AI Eval &amp; CI Pipelines Break
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  엔지니어들은 "아침에 평가 파이프라인이 줄줄이 깨져서야 저장소가 사라진 걸 알았다"며, 핵심 오픈소스 의존성은 반드시 내부 Git 미러와 고정 릴리즈 아티팩트 캐시를 두어야 한다는 뼈아픈 교훈을 공유했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/microsoft/onnxruntime" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> 대상 저장소 확인
              </a>
              <a href="https://news.ycombinator.com/item?id=50539610" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (449 pts)
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
