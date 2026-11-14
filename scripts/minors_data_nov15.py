# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-15

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
          직전 발행(11월 13일) 이후 52.8시간 동적 탐색 윈도우를 균등 3분할(0~17.6h, 17.6~35.2h, 35.2~52.8h)하여 시간당 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다. 상호 중복 배제 및 재귀적 클러스터링 알고리즘이 적용되었습니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~17.6h) ==================== -->
        <!-- [GH 0~17.6h] Item 1: fdncred/nu_plugin_render -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~17.6h</span>
                <span class="minor-metric">⭐ 1개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 1.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.90 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;터미널 테이블을 문자 대신 픽셀 카드로 렌더링하는 Nushell 그래픽 플러그인&quot; : nu_plugin_render</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">fdncred/nu_plugin_render — Nushell 테이블의 이모지·CJK 폭 깨짐을 없애고 중첩 리스트와 레코드를 Kitty/Sixel 고해상도 이미지 카드로 즉시 그려내는 Rust 플러그인</span>
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
            <h3 class="minor-detail-headline">고정폭 글꼴(Monospace)의 한계를 넘어 픽셀 정밀도로 중첩 데이터 구조를 시각화</h3>
            <div class="minor-detail-subheadline">Nushell 코어 메인테이너 fdncred가 선보인 Kitty Graphics · Sixel 네이티브 터미널 테이블 렌더러</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  터미널에서 JSON이나 중첩 구조 데이터를 볼 때 기존 ASCII 박스 선은 한중일(CJK) 전각 문자나 이모지가 섞이면 줄이 엇갈리기 일쑤였습니다. `nu_plugin_render`는 터미널 출력 자체를 픽셀 캔버스 이미지로 그려내 칼럼 정렬을 완벽히 맞춥니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Nushell Value AST &rarr; Nested Card Layout &rarr; Pixel Rasterizer &rarr; Kitty / Sixel Terminal Stream
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  ANSI 컬러 문자열과 LS_COLORS 아이콘을 그대로 살리면서도 브라우저 대시보드에 버금가는 가독성을 CLI 파이프라인 안에 구현했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/fdncred/nu_plugin_render" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~17.6h] Item 2: 0x00-Community/detour -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~17.6h</span>
                <span class="minor-metric">⭐ 6개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.88 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Mesa·Vulkan·OpenGL을 통째로 우회하고 MLIR에서 실리콘으로 직결되는 100% Rust GPU 드라이버&quot; : detour</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">0x00-Community/detour — 거대한 그래픽스 미들웨어 스택 없이 커맨드 스트림, GPU 상태, 셰이더 머신 코드를 Rust로 직접 제어하는 초경량 유저스페이스 GPU 드라이버</span>
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
            <h3 class="minor-detail-headline">C/C++ 기반 레거시 Mesa와 libdrm 추상화 계층을 건너뛰는 Rust 컴퓨트 드라이버 실험</h3>
            <div class="minor-detail-subheadline">LLVM MLIR 중간 표현에서 곧바로 GPU 하드웨어 명령어 큐를 조립하는 차세대 시스템 아키텍처</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 추론과 커스텀 커널 수요가 폭증하는 반면, 기존 Mesa/Vulkan/OpenGL 유저스페이스 드라이버는 수백만 줄의 C/C++ 유산을 짊어지고 있습니다. `detour`는 메모리 안전한 순수 Rust로 하드웨어 레지스터와 셰이더 컴파일 경로를 직접 열어젖힙니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[아키텍처]</strong> MLIR Kernel IR &rarr; Rust Shader Machine Code &rarr; Direct Command Stream &rarr; GPU Silicon (No Mesa/Vulkan)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  드라이버 오버헤드와 컴파일러 블랙박스를 제거해 차세대 오픈소스 AI 가속기 런타임의 새로운 설계 방향을 제시했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/0x00-Community/detour" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~17.6h] Item 3: Timon2306/oxigram -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~17.6h</span>
                <span class="minor-metric">⭐ 12개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.80 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;TDLib·Electron·Qt 없이 70MB RAM에서 날아다니는 텔레그램 데스크톱 클라이언트&quot; : Oxigram</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Timon2306/oxigram — 순수 Rust MTProto(grammers) 엔진과 Tauri 2 + Svelte 5 시스템 WebView만으로 초경량 메시징을 구현한 네이티브 클라이언트</span>
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
            <h3 class="minor-detail-headline">무거운 C++ TDLib 래퍼를 버리고 순수 Rust MTProto 프로토콜 스택 직결</h3>
            <div class="minor-detail-subheadline">일렉트론 메신저 앱들의 수백 MB 메모리 점유율을 10분의 1 수준으로 압축</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  메신저 앱 몇 개만 켜도 RAM 2GB가 증발하는 데스크톱 환경에 반기를 들며, Rust `grammers` 라이브러리로 텔레그램 MTProto 암호화 세션을 직접 처리하고 UI는 OS 기본 웹뷰로 띄우는 실전형 대안이 등장했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[스택]</strong> Svelte 5 UI (System WebView) &harr; Tauri 2 IPC &harr; Pure Rust `grammers` (Direct MTProto)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  빌드 시간과 바이너리 용량, 상주 메모리 70MB라는 극한 효율을 달성하며 경량 네이티브 앱 트렌드를 이어가고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Timon2306/oxigram" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (17.6~35.2h) ==================== -->
        <!-- [GH 17.6~35.2h] Item 4: opencoredev/islandcn -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 17.6~35.2h</span>
                <span class="minor-metric">⭐ 661개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 34.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 18.93 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;shadcn 한 줄로 내 React 웹앱에 심는 오픈소스 다이나믹 아일랜드&quot; : islandcn</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">opencoredev/islandcn — 파일 업로드, 타이머, 음악 재생, 실시간 녹음 상태를 앱 최상단 다이내믹 아일랜드 UI로 통합 제어하는 React 컴포넌트</span>
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
            <h3 class="minor-detail-headline">파편화된 Toast 알림과 상단 배너를 Apple Dynamic Island 감성의 단일 액티비티 허브로 대체</h3>
            <div class="minor-detail-subheadline">`npx shadcn@latest add` 한 줄 설치와 선언적 `&lt;IslandProvider&gt;` API 제공</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 작업 진행률, 오디오 스트리밍, 백그라운드 파일 업로드를 여러 개의 토스트 팝업으로 띄우면 화면이 지저분해집니다. `islandcn`은 이를 하나의 부드러운 모핑(Morphing) 필 UI 안에 응축시켜 하루 반 만에 660여 스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[구조]</strong> App Events (Upload / Timer / Agent Run) &rarr; `useIsland()` State Queue &rarr; Morphing Pill UI
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  외부 무거운 런타임 의존성 없이 shadcn 생태계 규격 그대로 소스 코드를 소유해 커스터마이징할 수 있어 프론트엔드 호응이 폭발적입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://islandcn.dev" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="globe" class="minor-icon"></i> 공식 데모
              </a>
              <a href="https://github.com/opencoredev/islandcn" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 17.6~35.2h] Item 5: Eddie02345/seuil -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 17.6~35.2h</span>
                <span class="minor-metric">⭐ 10개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.55 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;삼성 연속성 BLE 프로토콜 역공학으로 갤럭시 버즈를 리눅스와 자동 전환 연결하는 데몬&quot; : Seuil</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Eddie02345/seuil — 삼성 독점 `com.samsung.android.mcfds` BLE 0x0075 핸드셰이크와 L2CAP CoC를 Rust로 구현해 폰-리눅스 간 버즈 오디오를 무접촉 전환</span>
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
            <h3 class="minor-detail-headline">갤럭시 북 윈도우 전용으로 잠겨 있던 Samsung Auto Switch 기능을 오픈소스 리눅스로 해방</h3>
            <div class="minor-detail-subheadline">블루투스 페어링 재연결 대기 없이 오디오 스트림의 문턱(Seuil)을 부드럽게 넘나드는 하드웨어 역공학</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  이어폰의 자동 기기 전환(Auto Switch)은 제조사들이 폐쇄적 OS 생태계에 사용자를 가두는 대표적 락인 기능입니다. 개발자가 삼성 연속성 프로토콜 패킷을 직접 패킷 캡처해 리눅스 데스크톱을 정식 피어로 위장시키는 데 성공했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[핸드셰이크]</strong> BLE 0x0075 Advertise &rarr; `mcfds` L2CAP CoC Channel &rarr; Auto Switch Signal &rarr; Linux Pulse/PipeWire Sink
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  애플 에어팟 생태계에 맞서 리눅스 데스크톱 사용자들도 제조사 독점 하드웨어 편의 기능을 온전히 누릴 수 있음을 입증했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Eddie02345/seuil" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 17.6~35.2h] Item 6: AnnenkovLabs/flecten -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 17.6~35.2h</span>
                <span class="minor-metric">⭐ 8개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.29 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;에이전트가 일하는 동안 실시간 대화·파일·도구·변경점을 한 창에 묶은 통합 데스크톱 하네스&quot; : Flecten</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">AnnenkovLabs/flecten — 코딩 에이전트의 실행 흐름을 멈추지 않고 옆에서 대화하며 파일 트리와 도구 호출 내역을 즉시 개입·조율하는 오픈소스 워크스페이스</span>
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
            <h3 class="minor-detail-headline">대기 화면만 바라보는 턴제 채팅에서 벗어나 에이전트 작업 중 실시간 조타 지원</h3>
            <div class="minor-detail-subheadline">대화 스레드, 프로젝트 파일, 도구 실행 로그, Git 변경분을 단일 네이티브 창으로 통합</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  에이전트가 장기 태스크를 실행할 때 중간에 방향을 살짝 틀어주고 싶어도 기존 CLI는 중단(Ctrl+C) 후 재시작해야 했습니다. Flecten은 작업 중 실시간 피드백 주입과 개인화 프리셋을 단일 데스크톱 IDE 형태로 풀어냈습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[워크스페이스]</strong> Live Steering Chat &harr; Tool Call Telemetry &harr; File Tree &amp; Diff Inspector (AGPL-3.0)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  에이전트 런타임이 백엔드 엔진으로 수렴하는 가운데, 인간-에이전트 인터랙션 UX 경쟁이 본격화되었음을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/AnnenkovLabs/flecten" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (35.2~52.8h) ==================== -->
        <!-- [GH 35.2~52.8h] Item 7: faizfahmi77/ScanDot -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 35.2~52.8h</span>
                <span class="minor-metric">⭐ 532개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 42.6시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 12.48 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;고가의 LiDAR 아이폰 없이 일반 안드로이드폰으로 3D 포인트 클라우드를 스캔·시각화하는 오픈 앱&quot; : ScanDot</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">faizfahmi77/ScanDot — ARCore 카메라 추적과 깊이 추정을 결합해 로컬 3D 포인트 클라우드를 생성하고, 워크스테이션 FFmpeg·COLMAP 포토그래메트리까지 연계하는 프로젝트</span>
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
            <h3 class="minor-detail-headline">모바일 ARCore 실시간 깊이 맵과 데스크톱 COLMAP 고밀도 복원을 잇는 오픈소스 공간 스캐너</h3>
            <div class="minor-detail-subheadline">클라우드 유료 구독이나 워터마크 없이 내 폰과 PC에 온전한 3D 공간 데이터를 저장</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  3D 스캔 앱들은 대부분 클라우드 처리를 강제하며 내보내기 기능에 월정액을 부과합니다. ScanDot은 안드로이드 ARCore 기반 실시간 캡처 뷰어와 로컬 워크스테이션 포토그래메트리 파이프라인을 모두 오픈소스로 공개해 530여 스타를 돌파했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> ARCore Tracking + Depth Map &rarr; Local Point-Cloud Viewer &rarr; FFmpeg Frame Extract &rarr; COLMAP 3D Mesh
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  로보틱스·건축·인디 게임 개발자들이 전용 3D 스캐너 없이도 물리 공간을 손쉽게 디지털 자산으로 끌어들이는 진입 장벽을 낮췄습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/faizfahmi77/ScanDot" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 35.2~52.8h] Item 8: quer3q/kraken-mount -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 35.2~52.8h</span>
                <span class="minor-metric">⭐ 321개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 39.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 8.16 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;zstd·LZ4 압축 덤프와 FPKG를 초고속 마운트하는 PS5 미니멀리스트 Rust 페이로드&quot; : kraken-mount</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">quer3q/kraken-mount — 내장 SSD와 USB 확장 드라이브의 게임 패키지·압축 폴더를 실시간 온더플라이 해제해 구동하는 경량 PS5 ELF 마운터</span>
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
            <h3 class="minor-detail-headline">대용량 콘솔 백업 파일의 압축 해제 대기 없이 즉시 마운트하는 고성능 I/O 아키텍처</h3>
            <div class="minor-detail-subheadline">`ampr-emu-ng`(`libSceAmpr.sprx`) 번들 통합 및 Rust 기반 무결점 ELF 바이너리 실행</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  100GB가 넘는 현대 콘솔 게임 덤프를 비압축 상태로 보관하려면 막대한 SSD 용량이 필요합니다. `kraken-mount`는 zstd/LZ4로 압축된 게임 폴더와 디버그 FPKG를 즉석에서 마운트해 홈브류 씬에서 320개 이상의 스타를 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[마운트 흐름]</strong> SSD / USB Drive (.pkg / .zst / .lz4) &rarr; Rust PS5 ELF Payload + libSceAmpr &rarr; Instant Virtual Mount
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  콘솔 홈브류 및 게임 보존 영역에서도 C 위주였던 기존 페이로드가 안전하고 빠른 Rust 생태계로 빠르게 세대교체되고 있음을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/quer3q/kraken-mount" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 35.2~52.8h] Item 9: claynicholson/copper-kicad-mcp -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 35.2~52.8h</span>
                <span class="minor-metric">⭐ 85개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 52.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.63 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;AI 에이전트가 KiCad 10으로 실제 발주 가능한 PCB 기판을 설계·라우팅·검증하는 MCP&quot; : copper-kicad-mcp</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">claynicholson/copper-kicad-mcp — 회로도(Schematic), LCSC 부품 선정, 배선 라우팅, KiCad 자체 ERC/DRC 검증 및 JLCPCB 거버 파일 출력까지 연결하는 하드웨어 설계 MCP</span>
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
            <h3 class="minor-detail-headline">텍스트 코딩을 넘어 물리적 전자회로(EDA) 설계와 실제 기판 제조 공정까지 뻗은 MCP 프로토콜</h3>
            <div class="minor-detail-subheadline">단순 모형 그림이 아니라 KiCad 10 네이티브 ERC/DRC 전기적·설계 규칙 검증 통과 보증</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  소프트웨어를 넘어 하드웨어 프로토타이핑에서도 AI를 쓰려는 시도가 많았지만, 실제로 공장에 발주(JLCPCB)할 수 있는 수준의 배선과 부품 패키지를 맞추는 도구는 드물었습니다. `copper-kicad-mcp`는 KiCad 10 엔진을 직접 제어해 그 간극을 메웠습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[EDA 루프]</strong> AI Spec &rarr; LCSC Parts &amp; Schematic &rarr; PCB Layout/Route &rarr; KiCad ERC/DRC Check &rarr; JLCPCB Fab Export
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  하드웨어 엔지니어들이 며칠씩 씨름하던 기초 전원부·MCU 브레이크아웃 기판 설계가 자연어 대화와 결정론적 DRC 루프로 수십 분 만에 완결되는 시대를 앞당겼습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/claynicholson/copper-kicad-mcp" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~17.6h) ==================== -->
        <!-- [HN 0~17.6h] Item 10: SpaceX Catches the Starship to end Flight 15 -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~17.6h</span>
                <span class="minor-metric">🔺 364 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 1.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 260.67 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;스타십 15차 비행, 발사대 젓가락 암(Mechazilla) 상단선 완전 포획 성공&quot; : SpaceX Flight 15</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">x.com/i/broadcasts — Super Heavy 부스터를 넘어 우주선 상단선(Ship)까지 공중 회수에 성공하며 완전 재사용 궤도 로켓 시대를 연 실시간 우주공학 쾌거</span>
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
            <h3 class="minor-detail-headline">궤도 재진입 열차폐를 버텨낸 스타십 상단선이 발사 타워 품으로 안착한 역사적 순간</h3>
            <div class="minor-detail-subheadline">등장 1.4시간 만에 시간당 260표가 넘는 폭발적 추천을 기록하며 해커뉴스 1위를 점령</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  극초음속 대기권 재진입과 정밀 추력 제어(GNC)가 동시에 요구되는 상단선 캐치 기동이 실전 Flight 15에서 완벽히 성공하면서, 전 세계 시스템·제어 엔지니어들이 실시간으로 환호했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[비행 시퀀스]</strong> Orbital Reentry &rarr; Belly-Flop Descent &rarr; Raptor Gimbal Flip &rarr; Mechazilla Tower Catch
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  우주 발사 단가를 항공기 운항 수준으로 끌어내리는 완전 신속 재사용(Rapid Reusability) 하드웨어 루프가 마침내 닫혔습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://x.com/i/broadcasts/2brajgZlOKRMka" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 생중계 기록 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50500963" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (364 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~17.6h] Item 11: Lovable apps expose passport details and more than 200K private messages -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~17.6h</span>
                <span class="minor-metric">🔺 536 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.1시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 106.13 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;바이브 코딩 앱들의 대참사: Lovable 제작 앱들에서 여권 정보와 비공개 메시지 20만 건 이상 노출&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">crissyfield.de — 보안 감사 없이 AI 앱 빌더로 배포된 실서비스들이 Supabase 행 수준 보안(RLS) 미설정으로 민감 개인정보를 통째로 개방한 충격 보고서</span>
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
            <h3 class="minor-detail-headline">프롬프트 몇 줄로 10분 만에 띄운 SaaS가 어떻게 전 세계 개인정보 유출의 진원지가 되었는가</h3>
            <div class="minor-detail-subheadline">클라이언트 번들에 노출된 anon 키와 무방비 DB 테이블이 부른 '노코드/바이브 코딩 보안 부채'</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 앱 빌더 Lovable로 생성되어 실제 인터넷에 운영 중이던 수많은 웹앱을 보안 연구자가 점검한 결과, 데이터베이스 접근 제어(RLS)가 비어 있거나 잘못 짜여 여권 스캔본과 20만 건이 넘는 개인 메시지가 외부에서 그대로 열람되는 심각한 결함이 드러났습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[유출 경로]</strong> AI Generated Frontend &rarr; Public Supabase Anon Key &rarr; Missing/Broken RLS Policy &rarr; Full Table Dump
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  "기능이 돌아간다"와 "프로덕션에 배포해도 안전하다" 사이의 거대한 심연을 다시 한 번 경고하며 보안 자동 검증 도구의 필요성을 각인시켰습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.crissyfield.de/research/lovable-en/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="shield-alert" class="minor-icon"></i> 보안 연구 보고서
              </a>
              <a href="https://news.ycombinator.com/item?id=50499017" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (536 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~17.6h] Item 12: Tech Companies Are Trying to Shift the Concept of Privacy (Again) -->
        <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~17.6h</span>
                <span class="minor-metric">🔺 412 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 41.17 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;빅테크 기업들은 또다시 '프라이버시'의 정의 자체를 뒤바꾸려 하고 있다&quot; : EFF 심층 비평</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">eff.org — AI 학습 데이터 수집과 서버 측 감시를 '프라이버시 보호'로 포장하는 빅테크의 언어적 재정의 시도를 정면 고발한 전자프론티어재단(EFF) 분석</span>
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
            <h3 class="minor-detail-headline">"익명화·로컬 처리"라는 미명 아래 기본 옵트인(Opt-in) AI 데이터 수집을 정당화하는 법적 전략 분석</h3>
            <div class="minor-detail-subheadline">단말기 보안(Confidential Computing)과 사용자 데이터 통제권 사이의 교묘한 개념 혼동 경계</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  최근 주요 OS와 브라우저, AI 플랫폼들이 사용자 동의 없이 대화·행동 데이터를 수집하면서도 "인간 직원이 보지 않으니 프라이빗하다"는 식의 새로운 약관 프레임을 밀어붙이자, EFF가 그 위험성을 정면으로 짚고 나섰습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[논점]</strong> True E2E Data Minimization &ne; Corporate "AI-Processed Without Human Eyes" Redefinition
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  로컬 퍼스트·셀프호스팅 오픈소스가 왜 단순한 취미가 아니라 디지털 주권의 최후 보루인지를 개발자 사회에 다시 환기했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.eff.org/deeplinks/2026/11/tech-companies-are-trying-shift-entire-concept-privacy-again" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="file-text" class="minor-icon"></i> EFF 원문 읽기
              </a>
              <a href="https://news.ycombinator.com/item?id=50496602" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (412 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (17.6~35.2h) ==================== -->
        <!-- [HN 17.6~35.2h] Item 13: FAA issues national ground stop – lifted 4.5 hours later -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 17.6~35.2h</span>
                <span class="minor-metric">🔺 1,634 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 63.65 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;미국 전역 항공편 일제 이륙 중지(Ground Stop) 사태 — 4.5시간 마비 속 관제 IT 인프라 충격&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">nbcnews.com — 미 연방항공청(FAA)의 전격 전국 이륙 금지 조치로 수천 편 항공기가 발이 묶이며 노후화된 국가 항공 관제 시스템의 단일 장애점(SPOF) 논쟁 재점화</span>
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
            <h3 class="minor-detail-headline">1,634표가 몰린 미 전역 영공 봉쇄 사태와 실시간 항공 주파수 모니터링 커뮤니티 동시 주목</h3>
            <div class="minor-detail-subheadline">파생 화제: KORS·빅토리아 관제 무선 주파수 실황 스트리밍(orcasairband.com) 등 현장 추적 동시 확산</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  미국 전 공항 출발편에 대해 사상 초유의 전국적 이륙 중단 명령이 내려졌다가 4시간 30분 만에 해제되면서, 2023년 NOTAM 장애에 이은 국가 핵심 기간망의 레거시 소프트웨어·통신 이중화 결함이 엔지니어들의 뜨거운 토론 대상이 되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[사태 타임라인]</strong> Nationwide ATC Alert &rarr; 4.5h Full Ground Stop &rarr; Live Airband/ADS-B Tracking &rarr; Gradual Recovery
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  미션 크리티컬 인프라에서 무중단 롤백과 그레이스풀 디그레데이션(Graceful Degradation) 설계가 얼마나 절실한지 다시금 입증했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.nbcnews.com/news/us-news/faa-orders-nationwide-ground-stop-departing-flights-reasons-safety-rcna609247" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> NBC 뉴스 리포트
              </a>
              <a href="https://news.ycombinator.com/item?id=50489641" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (1,634 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 17.6~35.2h] Item 14: Nvidia allegedly engineered scarcity by funding AI startups to buy its GPUs -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 17.6~35.2h</span>
                <span class="minor-metric">🔺 1,014 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 19.9시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 50.99 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;엔비디아, AI 스타트업에 자금을 대주고 자사 GPU를 사게 해 인위적 품귀를 조작했다는 의혹 제기&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">techpowerup.com — 네오클라우드·AI 스타트업 지분 투자와 GPU 구매 약정을 맞물리게 하여 '순환 매출'과 공급 부족 현상을 증폭시켰다는 탐사 보도 파장</span>
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
            <h3 class="minor-detail-headline">자사 칩을 사는 고객사에게 투자금을 쥐여주는 '순환 자금 조달(Round-tripping)' 논란</h3>
            <div class="minor-detail-subheadline">실리콘밸리 AI 인프라 버블의 실체를 둘러싸고 1,014표가 몰린 격론</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  엔비디아가 주요 GPU 클라우드 스타트업들에 대규모 투자를 집행하고, 해당 스타트업들이 다시 엔비디아의 차세대 칩을 선주문하는 구조가 시장의 실질 최종 수요를 부풀리고 공급 희소성을 의도적으로 연출했다는 분석이 터져 나왔습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[순환 구조]</strong> Nvidia Venture Capital &rarr; AI / Neocloud Startups &rarr; Massive GPU Pre-Orders &rarr; Artificial Scarcity Loop
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  특정 벤더의 고가 GPU 독점 구조에 휘둘리지 않으려는 오픈소스 양자화(ggml, Unsloth)와 CPU/NPU 로컬 추론 기술의 경제적 동기가 한층 더 명확해졌습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 보도 원문 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50493251" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (1,014 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 17.6~35.2h] Item 15: Monkey Island: all 13 versions side by side -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 17.6~35.2h</span>
                <span class="minor-metric">🔺 452 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 24.59 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;EGA부터 아미가·FM-Towns·VGA·리마스터까지 원숭이 섬의 비밀 13개 플랫폼 이식판 동시 비교 아카이브&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">monkeyisland.pages.dev — 1990년 명작 어드벤처 게임의 동일 장면이 13종의 레트로·현대 하드웨어 팔레트와 픽셀 파이프라인에서 어떻게 달라졌는지 나란히 체험하는 웹 박물관</span>
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
            <h3 class="minor-detail-headline">16색 디더링의 예술과 하드웨어 종속성이 빚어낸 컴퓨터 그래픽스 진화사의 결정판</h3>
            <div class="minor-detail-subheadline">CGA/EGA/VGA/Tandy/Amiga/Atari ST/Mac/Sega CD/FM Towns/Special Edition 실시간 대조</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  같은 도트 아티스트의 그림이라도 16색 고정 팔레트(EGA), 256색 VGA, 아미가(Amiga)의 32색 커스텀 칩셋 위에서 픽셀 디더링 기법이 어떻게 달라졌는지 한 화면에서 스크롤하며 감상할 수 있어 레트로 엔지니어들의 극찬을 받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[비교 축]</strong> 4-Color CGA &rarr; 16-Color EGA Dither &rarr; 32-Color Amiga &rarr; 256-Color VGA/FM-Towns &rarr; HD Remaster
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  제약이 극심했던 초기 하드웨어 환경이 오히려 인간의 픽셀 아트 창의성을 어떻게 극대화했는지 보여주는 훌륭한 기술 아카이브입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://monkeyisland.pages.dev/" target="_blank" rel="noopener noreferrer" class="minor-link demo">
                <i data-lucide="globe" class="minor-icon"></i> 비교 아카이브 열기
              </a>
              <a href="https://news.ycombinator.com/item?id=50493904" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (452 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (35.2~52.8h) ==================== -->
        <!-- [HN 35.2~52.8h] Item 16: Service degradation on Microsoft 365 -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 35.2~52.8h</span>
                <span class="minor-metric">🔺 1,170 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 52.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 22.32 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;전 세계 기업을 마비시킨 Microsoft 365·Outlook·Azure 글로벌 대규모 장애&quot; : 12시간 이상 먹통 파동</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">status.cloud.microsoft — 글로벌 오피스·메일·인증 클라우드가 장시간 붕괴되며 'LibreOffice는 1년 365일 작동한다'는 풍자까지 폭발한 클라우드 종속 위기</span>
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
            <h3 class="minor-detail-headline">Outlook·365 12시간+ 장애 및 Azure 연동 서비스 연쇄 마비 — 로컬 소프트웨어의 재평가</h3>
            <div class="minor-detail-subheadline">파생 화제 통합: Outlook 12h 장애(467 pts) · Azure Outage(402 pts) · LibreOffice 365 트윗(927 pts) 일괄 수록</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Microsoft 365와 Outlook, Azure 인프라가 전 세계적으로 12시간 넘게 서비스 장애를 겪으면서 수많은 기업의 업무와 메일 통신이 정지했습니다. 이때 LibreOffice 공식 계정이 올린 "LibreOffice actually works 365 days a year" 트윗이 927표의 공감과 환호를 이끌어냈습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[클러스터 요약]</strong> Microsoft 365 &amp; Azure Control Plane Fault &rarr; 12h+ Global Outage &rarr; On-Prem / LibreOffice Revival Debate
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  단일 하이퍼스케일 클라우드 구독 모델에 조직 전체의 문서·메일·인증을 몰아넣는 구조의 리스크를 극명하게 드러냈습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://status.cloud.microsoft/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Microsoft 상태 페이지
              </a>
              <a href="https://news.ycombinator.com/item?id=50471731" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (1,170 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 35.2~52.8h] Item 17: Reverse engineering my Coway air purifier to ditch the cloud -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 35.2~52.8h</span>
                <span class="minor-metric">🔺 782 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 48.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 16.05 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;클라우드 앱을 버리기 위해 내 코웨이(Coway) 공기청정기를 역공학한 하드웨어 해킹 르포&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">scottjg.com — 제조사 외부 클라우드 서버에 묶여 있던 스마트 가전의 통신 프로토콜과 MCU UART 인터페이스를 해부해 완전한 로컬 홈 오토메이션으로 해방시킨 기록</span>
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
            <h3 class="minor-detail-headline">제조사 서버가 꺼져도 영원히 작동하는 '로컬 퍼스트 스마트 홈' 가전 개조 가이드</h3>
            <div class="minor-detail-subheadline">가전제품 IoT 모듈과 메인 보드 간 시리얼 프로토콜 분석 및 로컬 MQTT/Home Assistant 직결</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  공기청정기 한 대를 켜고 풍량을 조절하는 데도 지구 반대편 AWS 클라우드 서버를 왕복해야 하는 IoT 기기의 부조리에 맞서, 하드웨어 내부 패킷을 분석해 클라우드 의존성을 0%로 지워버린 통쾌한 글이 782표를 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[디클라우드 구조]</strong> Coway Main MCU &harr; Intercepted UART Frames &rarr; Local ESPHome / MQTT &rarr; Home Assistant (No Cloud)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  사용자가 돈을 주고 산 하드웨어의 진정한 소유권(Right to Repair &amp; Own)은 로컬 API 개방에서 시작된다는 원칙을 실천했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 역공학 원문 블로그
              </a>
              <a href="https://news.ycombinator.com/item?id=50474959" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (782 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 35.2~52.8h] Item 18: Elevated errors on claude.ai, Claude Code, and platform.claude.com -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 35.2~52.8h</span>
                <span class="minor-metric">🔺 493 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 36.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 13.52 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;claude.ai와 Claude Code, API 플랫폼 동시 오류 급증 — AI 코딩 의존 시대의 '도구 마비' 경험&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">status.claude.com — 앤스로픽의 웹, CLI, 개발자 API 전반에 대규모 오류가 발생하며 로컬 모델 폴백과 멀티 프로바이더 라우팅의 중요성을 일깨운 장애</span>
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
            <h3 class="minor-detail-headline">단일 클라우드 AI API가 흔들리는 순간 전 세계 개발팀의 터미널이 동시에 멈춰 선 현실</h3>
            <div class="minor-detail-subheadline">파생 화제 통합: Claude Is Down(199 pts) 장애 보고 포함 · 로컬 오픈웨이트 모델 &amp; 다중 라우터 재주목</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  마이크로소프트 365 장애에 이어 개발자들이 가장 많이 의존하는 Claude Code와 API 엔드포인트까지 연쇄 오류를 겪으면서, 단일 AI 공급자에 올인한 워크플로우의 취약성과 로컬 오픈소스 추론 백업의 필요성이 크게 부각되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[장애 교훈]</strong> Cloud API 5xx Spike &rarr; Terminal Coding Halted &rarr; Multi-Provider Fallback / Local Model Failover Essential
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  `CLIProxyAPI`, `ggml`, `TensorFold` 같은 로컬·다중 프로바이더 호환 계층이 단순 비용 절감을 넘어 '비즈니스 연속성(BCP)' 필수 인프라가 되었음을 시사합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://status.claude.com/incidents/nn11wk485zfn" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Claude 장애 리포트
              </a>
              <a href="https://news.ycombinator.com/item?id=50481187" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (493 pts)
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
