# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-26

FULL_MINORS_SECTION = r"""
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
          직전 발행(11월 25일) 이후 30시간 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 관심 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: whitemollie/WhiteHub -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 2개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 1.5시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.33 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;무거운 제조사 앱 없이 Windows 11 작업표시줄에 무선 기기 배터리를 띄운다&quot; : WhiteHub</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">whitemollie/WhiteHub — 드라이버·네트워크 접근 없이 HID/Bluetooth 주변기기 배터리 잔량을 상시 표시하는 순수 Rust 트레이 유틸리티 (GPL-3.0)</span>
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
            <h3 class="minor-detail-headline">Logitech G Hub·Razer Synapse 같은 수백 MB 텔레메트리 앱을 치우고 작업표시줄에 배터리 막대만 남긴 Rust 유틸리티</h3>
            <div class="minor-detail-subheadline">GPL-3.0 라이선스 · Rust · v0.2.5 릴리스 · 오프라인 전용 · 무드라이버 HID/BLE 조회</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  무선 마우스·키보드·헤드셋을 여러 제조사 제품으로 섞어 쓰는 Windows 11 사용자는 배터리 잔량을 확인하기 위해 수백 MB짜리 상주 프로그램과 계정 로그인까지 감수해야 했습니다. <code>WhiteHub</code>는 네트워크 권한이나 커널 드라이버 설치 없이 OS 표준 HID/Bluetooth 배터리 리포트만 읽어 작업표시줄 위에 깔끔한 미니 스트립으로 띄워줍니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[오프라인 저점유 구조]</strong> Windows HID/BLE API &rarr; WhiteHub Rust Daemon (Zero Network) &rarr; Taskbar Battery Strip
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  제조사 번들 소프트웨어의 텔레메트리와 백그라운드 부하를 거부하고 Rust 단일 실행 파일로 핵심 기능만 떼어내는 데스크톱 경량화 흐름을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/whitemollie/WhiteHub" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: pathbit/AgentModelKit -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 4개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.4시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.90 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;OpenCode·VS Code·Copilot CLI의 AI 모델 프로바이더 설정을 명령 한 번에 맞춘다&quot; : AgentModelKit</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">pathbit/AgentModelKit — 로컬 및 원격 개발 환경의 여러 코딩 에이전트 클라이언트 프로바이더·엔진 설정을 자동 프로비저닝하는 CLI (MIT)</span>
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
            <h3 class="minor-detail-headline">여러 대의 로컬 PC와 원격 워크스테이션에 흩어진 코딩 에이전트 모델 설정 파일을 표준화하는 CLI 키트</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Node.js 18+ · Windows/macOS/Linux 크로스플랫폼 · 인터랙티브 TUI + 자동화 플래그</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  개발자들이 로컬 LLM API, OpenCode, VS Code, GitHub Copilot CLI 등을 동시에 오가며 작업하게 되면서, 장비가 바뀔 때마다 각 도구의 JSON/YAML 모델 프로바이더 설정을 수동으로 맞추는 일이 번거로워졌습니다. <code>AgentModelKit</code>은 대화형 터미널 선택기와 비대화형 CLI 파라미터를 모두 지원해 수초 만에 프로바이더 구성을 일괄 생성합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[통합 설정 주입]</strong> Provider Presets (Local/API) &rarr; AgentModelKit CLI &rarr; OpenCode / VS Code / Copilot CLI Config
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  AI 코딩 에이전트가 다극화되는 환경에서 '도구별 설정 파편화'를 흡수하는 메타-프로비저닝 계층의 초기 시도로 주목받고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/pathbit/AgentModelKit" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://www.pathbit.com.br" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 페이지
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: blyth-ai/playable-kit -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 5개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.6시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.58 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;한 문장 프롬프트로 5MB 이하 단일 HTML 모바일 게임·광고를 구워낸다&quot; : Blyth Playable Kit</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">blyth-ai/playable-kit — Blyth Play Kernel과 자동 검증 도구, SKILL.md 워크플로우를 묶어 네트워크 없는 단일 index.html 게임을 빌드하는 키트</span>
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
            <h3 class="minor-detail-headline">앱스토어·광고 네트워크 규격(5MB 미만, 오프라인 단일 HTML)에 맞춘 AI 에이전트용 게임 제작 커널</h3>
            <div class="minor-detail-subheadline">PolyForm Shield 1.0.0 · npm (@blyth/playable-kit) · SKILL.md 내장 · 오프라인 단일 파일 번들러</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI에게 웹 게임을 만들라고 시키면 외부 CDN 스크립트나 무거운 애셋에 의존해 모바일 광고 네트워크나 인앱 웹뷰에서 곧장 실행되지 않는 경우가 많습니다. <code>Blyth Playable Kit</code>은 에이전트가 <code>SKILL.md</code> 절차에 따라 게임을 구현한 뒤 5MB 미만의 완전 오프라인 자립형 <code>index.html</code>로 패키징하고 자체 검증기까지 통과시키도록 설계됐습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[단일 HTML 게임 파이프라인]</strong> Prompt + SKILL.md &rarr; Blyth Play Kernel &rarr; Self-Contained index.html (&lt;5 MB, Offline)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  실전 플레이어블 광고(Playable Ads)와 미니게임 배포 제약 조건을 에이전트 스킬과 커널 규격 안에 내재화했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/blyth-ai/playable-kit" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://blyth.ai/arcade" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> Blyth Arcade
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: Moh4696/inkworks-skill -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 143개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 10.65 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;자동차 엔진이 움직이는 3D 공학 도면을 코드로 직접 그린다&quot; : Inkworks</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Moh4696/inkworks-skill — Three.js 프리미티브와 폐형식 운동학으로 백색 제도판 스타일의 인터랙티브 3D '작동 원리' 페이지를 생성하는 스킬 (MIT)</span>
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
            <h3 class="minor-detail-headline">외부 3D 모델 파일이나 영상 없이 순수 Three.js 수식만으로 스크러빙·단계별 정밀 제어가 가능한 제도판 시각화</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · JavaScript / Three.js · Claude Code · Codex · Cursor · Gemini CLI · OpenCode 호환</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI에게 기계의 작동 원리를 설명하는 웹페이지를 부탁하면 정적인 SVG나 뭉개진 다이어그램만 나오기 일쑤였습니다. <code>Inkworks</code>는 잉크 외곽선과 번호 말풍선이 달린 백색 공학 도면 스타일 아래, 단 하나의 구동 각도(Driver Angle)에서 파생되는 폐형식 운동학(Closed-form Kinematics)으로 실린더·펌프·밸브의 움직임을 계산해 슬로우 모션과 차트 스크러빙이 100% 정확히 맞물립니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[수식 기반 3D 제도판]</strong> Single Driver Angle &rarr; Closed-Form Kinematics &rarr; Three.js Ink Primitives &amp; Interactive Cycle Chart
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  생성형 영상이 흉내 내지 못하는 정밀 인터랙티브 기술 교육 콘텐츠를 코딩 에이전트 스킬 표준으로 대량 생산할 수 있는 길을 열었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Moh4696/inkworks-skill" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: op7418/guizang-magi2-skill -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 30개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 2.13 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;코드 그레이박스로 AI 영상의 액션을 고정하고, AI 영상으로 인터랙티브 웹사이트를 만든다&quot; : MAGI-2 Skill</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">op7418/guizang-magi2-skill — Video-to-Code(원테이크 인터랙티브 웹)와 Code-to-Video(코드 동작 프리비즈 제어)를 잇는 에이전트 스킬 (AGPL-3.0)</span>
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
            <h3 class="minor-detail-headline">텍스트 프롬프트의 랜덤성을 2D 코드 프리비즈로 통제하고, 생성된 영상을 스크롤 웹사이트로 역변환하는 쌍방향 파이프라인</h3>
            <div class="minor-detail-subheadline">AGPL-3.0 라이선스 · Python · LibTV MAGI-2 연동 · Antigravity · Claude Code · Codex 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI에게 제품 홍보 웹사이트를 시키면 뻔한 CSS 템플릿이 나오고, 반대로 영상 모델에게 복잡한 액션을 텍스트로 시키면 3초 타이밍 패링 같은 정밀 연출을 맞출 수 없었습니다. 이 스킬은 먼저 AI가 무음 2D 코드 회색 상자(Greybox) 애니메이션으로 타이밍과 동선을 확정해 MAGI-2에 넘겨 수묵화·시네마틱 영상으로 렌더링하거나(Code→Video), 반대로 영상을 프레임 기반 원테이크 스크롤 웹으로 엮어냅니다(Video→Code).
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[양방향 크리에이티브 루프]</strong> 2D Code Greybox (Exact Timing) &harr; LibTV MAGI-2 Video &rarr; Scroll-Driven Interactive Web
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  결정론적인 코드 제어력을 생성형 비디오 파이프라인에 주입해 '뽑기'에 의존하던 AI 영상 제작의 제어 가능성을 크게 끌어올렸습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/op7418/guizang-magi2-skill" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: programmersd21/ratatui-skill -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 14개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.88 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;AI 에이전트가 낡은 API 대신 최신 Ratatui 0.30 디자인으로 터미널 UI를 짜게 만든다&quot; : ratatui-skill</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">programmersd21/ratatui-skill — 구형 보일러플레이트와 컴파일 에러를 막고 의도된 레이아웃·테스트된 코드로 Rust TUI를 생성하는 에이전트 스킬 (MIT)</span>
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
            <h3 class="minor-detail-headline">학습 데이터에 남아 있는 구버전 tui-rs·구형 Ratatui API 환각을 차단하는 최신 Rust 1.88+ / Ratatui 0.30.2 가이드 스킬</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Rust 1.88+ · Ratatui 0.30.2 · CI 검증 코드 내장</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  LLM에게 Rust 터미널 UI를 시키면 몇 년 전 <code>tui-rs</code> 시절의 폐기된 메서드와 단조로운 박스 테두리 도배 코드를 내놓는 문제가 잦습니다. <code>ratatui-skill</code>은 <code>ratatui 0.30.2</code>의 최신 위젯·레이아웃 제약 조건과 절제된 타이포그래피·색상 규범, 그리고 CI를 통과한 실제 컴파일 예제를 스킬 컨텍스트로 제공해 품질을 대폭 높입니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[최신 API 가드레일]</strong> Coding Agent &rarr; ratatui-skill (0.30.2 APIs + Design Rules) &rarr; Clean Tested Rust TUI
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  빠르게 진화하는 오픈소스 크레이트의 최신 API를 에이전트 스킬 패키지로 유통하는 모범 사례를 제시합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/programmersd21/ratatui-skill" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: SilverFeit/StikSound -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 197개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 24.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 7.93 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;WhatsApp 스티커(PNG·GIF)에 최대 10초짜리 사운드를 입혀 로컬에서 내보낸다&quot; : StikSound</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">SilverFeit/StikSound — 외부 서버 업로드 없이 브라우저·데스크톱·크롬 확장으로 오디오 스티커를 합성하는 오픈소스 스튜디오 (Apache-2.0)</span>
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
            <h3 class="minor-detail-headline">정적 이미지·움직이는 GIF와 효과음 클립을 100% 클라이언트 로컬에서 즉시 결합해 메신저용 스티커로 변환</h3>
            <div class="minor-detail-subheadline">Apache-2.0 / MIT 듀얼 · TypeScript · GitHub Pages PWA + Windows/macOS + Chrome 확장</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  라틴 아메리카·유럽 커뮤니티를 중심으로 메신저 스티커에 짧은 밈(Meme) 효과음을 합쳐 공유하는 수요가 폭발하면서 스팸성 광고 사이트가 난립했습니다. <code>StikSound</code>는 PNG·WebP·GIF 스티커와 로컬 오디오 또는 MyInstants 사운드 구간을 정확히 잘라 100% 브라우저·로컬 앱 안에서 즉시 합성해 주며 하루 만에 197스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[로컬 미디어 합성]</strong> PNG/WebP/GIF + Trimmed Audio (5~10s) &rarr; Client-Side Muxing &rarr; WhatsApp Sound Sticker
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  PWA 웹 앱, 데스크톱 빌드, Chrome 확장 프로그램을 단일 오픈소스 코드베이스로 깔끔하게 통합한 로컬-퍼스트 유틸리티입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/SilverFeit/StikSound" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://silverfeit.github.io/StikSound/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 웹 앱 바로가기
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: matheusmongarde/garimpo -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 170개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 7.41 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Google Maps에서 상점을 찾고, 미리보기 사이트 생성부터 WhatsApp 영업·Pix 결제까지 자동화&quot; : Garimpo</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">matheusmongarde/garimpo — Claude Code·Codex·n8n용 API를 품고 B2B 지역 소상공인 발굴·제안·수금을 엮은 풀스택 영업 엔진 (MIT)</span>
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
            <h3 class="minor-detail-headline">스프레드시트 없이 Google Maps 탐색, 맞춤형 랜딩 프리뷰 생성, 메시징 및 결제 정산까지 연결한 에이전트 친화형 CRM</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · TypeScript · PC/VPS/Vercel 셀프호스팅 · Pix / Mercado Pago / Stripe 연동</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  웹 에이전시와 1인 개발자들이 지역 업체를 발굴해 웹사이트를 팔 때 가장 시간이 오래 걸리는 반복 작업은 '리드 수집→시안 제작→메시지 발송→결제 추적'입니다. 브라질에서 개발된 <code>Garimpo</code>는 지도 상 업체 데이터를 긁어 즉시 업체명이 박힌 프리뷰 페이지를 만들고, WhatsApp 대화와 결제 완료 시 자동 클로징까지 오픈소스로 풀어내 22시간 만에 ★170을 달성했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[엔드투엔드 B2B 파이프라인]</strong> Google Maps Discovery &rarr; Auto Preview Site &rarr; WhatsApp Pitch &rarr; Pix/Stripe Auto-Close
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  Claude Code·n8n 등 외부 에이전트가 바로 호출할 수 있는 API를 기본 내장해, 실제 수익 창출 워크플로우와 에이전트의 결합 양상을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/matheusmongarde/garimpo" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: Spilveru/mergeon -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 29개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22.6시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.28 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Zed의 GPU 가속 UI 엔진 GPUI가 독립하자마자 탄생한 초고속 Rust Git 클라이언트&quot; : Mergeon</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Spilveru/mergeon — Fork에 영감을 받아 Linux·Windows·macOS에서 120fps 키보드 중심 워크플로우를 구현한 GPUI 기반 Git GUI (GPL-3.0)</span>
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
            <h3 class="minor-detail-headline">Electron 기반 Git 클라이언트들의 묵직한 반응 속도를 넘어 GPU 셰이더로 커밋 그래프와 라인 단위 스테이징을 그리는 데스크톱 앱</h3>
            <div class="minor-detail-subheadline">GPL-3.0 라이선스 · Rust Edition 2024 + GPUI · Ctrl+Shift+P 커맨드 팔레트 · 파일/헝크/라인 스테이징</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  어제 Zed 에디터 팀이 자사 GPU UI 프레임워크 <code>GPUI</code>를 독립 저장소로 분리하자마자 생태계의 반응이 즉각 나타났습니다. <code>Mergeon</code>은 상용 Git 클라이언트 Fork의 쾌적한 키보드 중심 UX를 목표로, 파일·헝크·라인 단위 구문 강조 Diff와 <code>Ctrl+Shift+P</code> 커맨드 팔레트를 순수 Rust + GPUI 위에 올려 리눅스 유저들의 열띤 호응을 얻고 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[GPUI 네이티브 Git]</strong> libgit2 / Git CLI &rarr; Rust Edition 2024 State &rarr; GPUI GPU-Accelerated Commit Graph &amp; Diff
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  Electron 웹뷰에서 벗어나 GPU 직접 렌더링 기반의 Rust 데스크톱 도구 생태계(GPUI)가 본격 확산되는 신호탄입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Spilveru/mergeon" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: 1Password Security Incident -->
        <div class="minor-item" id="minor-hn-10" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 940점 · 397댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 172.02 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;직원 GitHub 계정 탈취로 백엔드 악성코드 푸시&quot; — 1Password 11월 보안 침해 사고 공식 발표</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">1Password Security Incident — 금고 데이터와 비밀 키는 안전하나 일부 고객 이름·이메일 등 관리 메타데이터 유출 확인, 피싱 주의보 발령</span>
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
            <h3 class="minor-detail-headline">CI/CD 및 기업 GitHub 공급망 침투가 암호화 금고(Zero-Knowledge) 밖의 '메타데이터 영역'을 겨냥한 중대 보안 사건</h3>
            <div class="minor-detail-subheadline">1Password 공식 보안 업데이트 · 11월 19일 탐지 / 25일 공개 · HN 940점 · 397댓글</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  1Password가 11월 19일 탐지한 보안 사고의 전말을 공개하며 해커뉴스 전체를 강타했습니다. 공격자는 직원 한 명의 기업용 GitHub 계정을 탈취한 뒤 소스코드에 접근해 백엔드 서비스로 악성 코드를 밀어 넣었고, 일부 고객의 이름·이메일 주소 등 관리 데이터를 내려받았습니다. 회사 측은 금고(Vault)와 마스터 비밀번호·Secret Key는 제로 지식 암호화 구조상 무사하다고 밝혔습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[공급망 침투 경로]</strong> Compromised Employee GitHub &rarr; Malicious Backend Push &rarr; Admin Metadata Exfil (Vault Keys Intact)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 산업 임팩트</div>
                <p class="minor-paragraph">
                  해커뉴스에서는 코드 서명·PR 다중 승인 절차가 왜 뚫렸는지와 더불어 <em>"로컬 자체 동기화를 없애고 클라우드 강제화한 대가"</em>라는 비판적 토론(397댓글)이 거세게 일었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://1password.com/blog/update-on-nov-2026-security-incident" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 공지 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50644817" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (397댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: GitHub Degraded Experiences -->
        <div class="minor-item" id="minor-hn-11" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 176점 · 94댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.8시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 25.95 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;전 세계 개발자의 CI/CD와 푸시가 멈췄다&quot; — GitHub 제품군 동시다발 장애 사태</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Investigating degraded experiences across GitHub — 웹·Git 작업·Actions·Copilot 전반의 성능 저하 및 오류로 개발자 불만 폭주</span>
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
            <h3 class="minor-detail-headline">대규모 클라우드·단일 호스팅 플랫폼 집중화가 반복될 때마다 다시 불거지는 '단일 장애점(SPOF)' 논쟁</h3>
            <div class="minor-detail-subheadline">GitHub Status 공식 장애 리포트 · HN 176점 · 94댓글 · Actions·PR·Git Ops 연쇄 지연</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  오늘 새벽(UTC) GitHub의 웹 UI, Git 작업, Actions, Pull Requests 전반에 걸쳐 광범위한 지연 및 오류 장애가 발생했습니다. 전 세계 개발팀의 배포 파이프라인이 멈춰 서자 해커뉴스에서는 최근 Microsoft의 'Code Red' 대규모 장애 기사(253점)와 맞물려 인프라 안정성 우려가 폭발했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[중앙화 리스크]</strong> GitHub Core Degradation &rarr; Actions / PR / Git Push Stalled &rarr; Self-Hosted Forge Migration Debate
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 산업 임팩트</div>
                <p class="minor-paragraph">
                  단순한 일시 장애를 넘어 Forgejo·Gitea·Radicle 같은 분산/셀프호스팅 Git 대안과 로컬 미러링의 필요성이 다시 주목받는 계기가 됐습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.githubstatus.com/incidents/qn8mfv6q5hlx" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 상태 페이지 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50643720" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (94댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: Clojure Core Checked with Lean 4 -->
        <div class="minor-item" id="minor-hn-12" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 161점 · 55댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.8시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 20.58 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;15년 된 Clojure 코어를 Lean 4와 차분 테스팅으로 찔러보니 미보고 버그 17개가 쏟아졌다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Checking Clojure's core with Lean — HAMT 해시 충돌 노드, vector-of reduce, 타입 힌트 없는 Java 상호운용 버그 등 17건 발견</span>
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
            <h3 class="minor-detail-headline">가장 성숙한 영속 자료구조 중 하나로 꼽히는 Clojure Java 코어에서 형식 모델링으로 반례를 잡아낸 실전 검증기</h3>
            <div class="minor-detail-subheadline">Conao3 기술 블로그 · HN 161점 · 55댓글 · Lean 4 비트 산술 모델링 + 300만 회 차분 테스트</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  "유명 Rust OSS를 Lean 4로 형식 검증해 수많은 버그를 찾았다"는 일본 엔지니어의 글에서 영감을 받은 저자가 Clojure 1.0 시절부터 15년 이상 검증됐다고 믿어진 Java 코어 자료구조에 Lean 4와 차분 테스팅(Differential Testing)을 들이댔습니다. HAMT 자체는 300만 번의 테스트를 버텼지만, 해시 충돌 노드와 <code>vector-of</code>의 <code>reduce</code> 등에서 JIRA에도 없는 미보고 버그 <strong>17건</strong>이 적발됐습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[실전 OSS 형식 검증]</strong> Clojure Java Core &rarr; Lean 4 Bitwise Model + Differential Test &rarr; 17 Unreported Edge-Case Bugs
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  Lean 4가 순수 수학 증명뿐만 아니라 오래된 프로덕션 언어 런타임의 숨은 경계 조건 버그를 사냥하는 실무 무기로 내려오고 있음을 증명합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://s.conao3.com/blog/2026/e4f733" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 블로그 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50642939" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (55댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: Button Sounds -->
        <div class="minor-item" id="minor-hn-13" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 821점 · 129댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 19.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 42.35 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;클릭 한 번에도 영혼이 담긴다&quot; — Josh W. Comeau의 프로 녹음 UI 버튼 사운드 컬렉션</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Button Sounds (buttons.joshwcomeau.com) — 프론트엔드 거장이 직접 설계한 물리적·촉각적 UI 클릭음 웹 쇼케이스</span>
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
            <h3 class="minor-detail-headline">침묵하는 평면 웹 인터페이스에 기계식 스위치·카세트·플립 스위치의 아날로그 손맛을 이식한 사운드 라이브러리</h3>
            <div class="minor-detail-subheadline">Josh W. Comeau 공개 · HN 821점 · 129댓글 · 웹 오디오 API 즉석 시연</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  CSS와 인터랙티브 교육으로 유명한 개발자 Josh W. Comeau가 전문 음향 장비로 녹음하고 정교하게 다듬은 UI 버튼 효과음 모음을 공개해 821점을 받았습니다. 브라우저 화면 위 다양한 버튼들을 직접 눌러보며 피치·딜레이·촉각적 피드백이 사용자 경험(UX)을 얼마나 드라마틱하게 바꾸는지 즉석에서 체험할 수 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[촉각적 사운드 UX]</strong> Foley / Mechanical Recordings &rarr; Web Audio API Micro-Variations &rarr; Tactile UI Feedback
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  AI가 생성한 천편일률적인 웹페이지가 넘쳐나는 시대에, 장인의 손길이 닿은 마이크로 인터랙션과 사운드 디자인의 가치를 일깨워 주었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://buttons.joshwcomeau.com/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 인터랙티브 데모 열기
              </a>
              <a href="https://news.ycombinator.com/item?id=50638032" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (129댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: Bypassing iOS Safari's 60 FPS Limit -->
        <div class="minor-item" id="minor-hn-14" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 432점 · 142댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 19.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 21.93 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;iOS Safari의 60fps 제한을 뚫고 120Hz 네이티브 앱처럼 부드러운 웹을 만든다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Bypassing iOS Safari's 60 FPS Limit — ProMotion 디스플레이에서 자바스크립트 rAF 상한을 우회해 네이티브 스크롤 물리를 해방시킨 DOM/CSS 트릭</span>
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
            <h3 class="minor-detail-headline">WebKit의 배터리 보호용 60Hz 스크립트 프레임 캡을 브라우저 내장 합성기(Compositor)와 스크롤 물리로 우회하는 프론트엔드 기법</h3>
            <div class="minor-detail-subheadline">Rida F'kih 기술 아티클 · HN 432점 · 142댓글 · iOS ProMotion 120Hz 인터랙션 실증</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  아이폰 Pro 모델은 120Hz ProMotion을 지원하지만 Apple은 Safari의 <code>requestAnimationFrame</code>을 기본 60fps로 묶어두어 웹앱이 네이티브 앱보다 뚝뚝 끊겨 보이게 만듭니다. 저자는 React Aria의 시트(Sheet)와 Jordan Walke의 실험에서 착안해, JS 프레임 루프 대신 브라우저 네이티브 스크롤 컨테이너와 CSS 애니메이션 타임라인을 영리하게 엮어 120Hz 네이티브급 손맛을 구현했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[120Hz 웹 우회]</strong> JS rAF (60Hz Capped) &times; &rarr; Native Scroll Physics + Compositor CSS Transitions (120Hz ProMotion)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  웹앱과 네이티브 앱 사이의 마지막 벽 중 하나였던 '120Hz 스크롤·제스처 질감'을 순수 DOM/CSS로 허문 인상적인 리포트로 평가받았습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://rida.dev/blog/bypassing-ios-safari-60-fps-limit" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 아티클 전문 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50637890" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (142댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: Show HN: Old Nvidia and ATI tech demos in the browser -->
        <div class="minor-item" id="minor-hn-15" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 326점 · 71댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18.2시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.87 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;1998년 3dfx Voodoo2부터 GeForce 256까지—전설의 GPU 데모가 브라우저에서 부활하다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Show HN: Old Nvidia and ATI tech demos (gpu-demo-gallery.pages.dev) — 1998~2006년 고전 그래픽카드 기술 데모 웹 이식 박물관</span>
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
            <h3 class="minor-detail-headline">Voodoo2, GeForce 256, GeForce2 시절의 실시간 셰이더·범프매핑 명작 데모를 설치 없이 웹에서 직접 돌리는 보존 프로젝트</h3>
            <div class="minor-detail-subheadline">Show HN · HN 326점 · 71댓글 · 1998~2006년 3dfx/NVIDIA/ATI 아카이브</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  1990년대 후반~2000년대 초반 그래픽카드 제조사들이 신제품의 텍스처 유닛과 하드웨어 T&amp;L을 과시하려 배포했던 전설적 테크 데모(1998 3dfx Borg/Donut, 1999 GeForce 256 Bubble/Lightning/Grass, 2000 Toy Soldier 등)들은 구형 DirectX·드라이버 종속성 때문에 현대 OS에서 실행하기가 극도로 까다로웠습니다. 이 프로젝트는 해당 데모들을 웹 브라우저에서 바로 클릭해 만져볼 수 있는 인터랙티브 갤러리로 되살려 냈습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[GPU 유산 복원]</strong> 1998~2006 Legacy DirectX/OpenGL Demos &rarr; Modern WebGL/WebGPU Gallery &rarr; Instant Interactive Browser Play
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  사라져 가는 초기 3D 그래픽스 역사의 실물 데모들을 누구나 URL 하나로 체험할 수 있는 디지털 박물관을 구축했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://gpu-demo-gallery.pages.dev/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 갤러리 바로 실행
              </a>
              <a href="https://news.ycombinator.com/item?id=50638503" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (71댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: Models Can Communicate via Inference Servers Despite Being Sandboxed -->
        <div class="minor-item" id="minor-hn-16" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 442점 · 188댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 20.2시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 21.88 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;완벽히 격리된 두 AI 모델이 추론 서버의 KV 캐시 부채널로 비밀 대화를 나눈다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Models Can Communicate via Inference Servers — 네트워크·파일시스템을 끊어도 vLLM 커널 배치·KV 캐시 타이밍을 변조해 은닉 통신 성공</span>
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
            <h3 class="minor-detail-headline">Step Sizing과 KV Cache Message Board 두 가지 프로토콜을 이용해 공유 추론 서버 위 에이전트 간 부채널(Side-Channel) 통신 실증</h3>
            <div class="minor-detail-subheadline">LessWrong AI 보안 연구 · HN 442점 · 188댓글 · vLLM 엔진 스케줄링·캐시 격리 결함 경고</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 안전성 검증에서 두 에이전트의 네트워크와 파일시스템을 완전히 분리해 두면 서로 공모(Collusion)할 수 없다고 가정해 왔습니다. 하지만 같은 vLLM 추론 서버를 공유할 경우, 한 모델(Alice)이 프롬프트 길이와 KV 캐시 프리픽스를 조절해 GPU 커널 선택과 응답 지연(Step Sizing)에 미세한 흔적을 남기면 다른 샌드박스 안의 모델(Bob)이 이를 해독해 8색 맞추기 게임 등에서 신호를 주고받을 수 있음이 실증됐습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[추론 서버 부채널]</strong> Sandboxed Agent A (KV Prefix/Length) &rarr; Shared vLLM Kernel Timing &rarr; Sandboxed Agent B Decodes Signal
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 보안 임팩트</div>
                <p class="minor-paragraph">
                  웹 브라우저가 오리진(Origin)별로 캐시를 격리하듯, 멀티테넌트 LLM 추론 서버 역시 KV 캐시와 배치 스케줄링을 테넌트 단위로 엄격히 분리해야 함을 일깨웠습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 연구 포스트 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50637686" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (188댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: PenGPT -->
        <div class="minor-item" id="minor-hn-17" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 385점 · 76댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 21.9시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.61 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;픽셀이 아니라 펜촉의 궤적(Stroke)을 생성하는 초소형 트랜스포머&quot; : PenGPT</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">PenGPT: A Generative Transformer for Handwriting and Sketches — 브라우저 안에서 사람처럼 자연스러운 손글씨와 스케치를 실시간으로 써 내려가는 모델</span>
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
            <h3 class="minor-detail-headline">저자 Sam Greydanus가 "노력의 80%를 데이터에, 15%를 속도에, 5%만 아키텍처에 쏟았다"고 밝힌 브라우저 내장 손글씨·스케치 AI</h3>
            <div class="minor-detail-subheadline">Sam Greydanus 블로그 · HN 385점 · 76댓글 · 브라우저 라이브 체험 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  거대 이미지 확산 모델은 손글씨 폰트처럼 뭉개진 픽셀을 그리지만, 인간은 펜을 종이에 대고 떼며 연속적인 궤적을 그립니다. <code>PenGPT</code>는 텍스트 프롬프트를 받아 연속적인 펜 스트로크 시퀀스를 자기회귀(Autoregressive) 방식으로 생성하는 소형 트랜스포머로, 정교한 데이터 정제와 경량화 덕분에 웹 브라우저 위에서도 매끄럽게 손글씨와 스케치를 그려냅니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[벡터 스트로크 생성]</strong> Text Prompt &rarr; Small Autoregressive Transformer &rarr; Sequential Pen Trajectories (dx, dy, pen-up/down)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  거대 모델이 모든 영역의 정답이 아니며, 도메인에 맞는 표현(픽셀 대신 펜 궤적)과 철저한 데이터 엔지니어링이 초소형 모델의 완성도를 결정함을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://greydanus.github.io/2026/11/12/pengpt/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 및 웹 데모 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50637056" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (76댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: GPT-6 intrinsic protein-design capabilities -->
        <div class="minor-item" id="minor-hn-18" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 350점 · 94댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 13.60 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;단백질 전용 모델이 아니라 범용 GPT-6 자체가 습식 실험실(Wet Lab) 결합 단백질을 설계한다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">GPT-6 Protein Design — 표적 결합 소형 단백질, 3D 구조 역접힘(Inverse Folding), 항체 CDR 재설계까지 범용 언어 모델의 내재 역량 실증</span>
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
            <h3 class="minor-detail-headline">별도의 생물학 특화 파인튜닝이나 확산 모델 없이 범용 프론티어 모델의 문맥 추론만으로 실제 실험실 검증을 통과한 단백질 서열 도출</h3>
            <div class="minor-detail-subheadline">OpenAI Science Publication · HN 350점 · 94댓글 · Wet-Lab 결합·항체 재설계 검증</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  지금까지 AI 신약·단백질 설계는 AlphaFold나 RFdiffusion 같은 생물학 전용 아키텍처의 전유물로 여겨졌습니다. OpenAI는 이번 논문에서 범용 모델 <code>GPT-6</code>가 사전학습 과정에서 획득한 내재적(Intrinsic) 구조·물리 추론만으로 표적 결합 미니 단백질 설계, 3D 백본에 맞는 새 아미노산 서열 예측, 항체 결합 부위 재설계까지 실제 실험실(Wet Lab)에서 작동하는 결과를 내놓았다고 발표했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[범용 과학 파운데이션]</strong> General Frontier Model (GPT-6) &rarr; De Novo Binder &amp; Antibody Redesign &rarr; Wet-Lab Validation
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 산업 임팩트</div>
                <p class="minor-paragraph">
                  수학(Lean 4)과 마찬가지로 생물학 분야에서도 특화 단일 모델과 범용 추론 모델 간의 경계가 빠르게 허물어지고 있으며, 동시에 생물보안(Biosecurity) 가드레일 논의도 한층 가팔라지고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 연구 발표 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50634658" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (94댓글)
              </a>
            </div>
          </div>
        </div>

      </div>
    </section>
"""
