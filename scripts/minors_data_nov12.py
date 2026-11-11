# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-12

FULL_MINORS_SECTION = """
    <!-- ========================================================== -->
    <!-- [SECTION 9] 실시간 극초기 레이더 (마이너 브리핑 18선) -->
    <!-- ========================================================== -->
    <section class="minor-radar-section" id="minor-radar">
      <div class="minor-radar-header">
        <div class="minor-title-group">
          <span class="aggro-tag" style="background:#fef08a; border-color:#ca8a04; color:#854d0e;">⚡ 실시간 극초기 레이더</span>
          <h2 class="minor-section-title">갓 태어난 극초신성 & 실시간 급상승 유망주 18선</h2>
        </div>
        <p class="minor-section-desc">
          직전 발행(11월 11일) 이후 30시간 동적 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다. 상호 중복 배제 및 재귀적 클러스터링 알고리즘이 적용되었습니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: SsKanDon/blender-ai-mcp-addon -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 46개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.4시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 8.57 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;블렌더 3D 뷰포트를 멀티 에이전트와 직결하다&quot; : blender-ai-mcp-addon</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">SsKanDon/blender-ai-mcp-addon — Blender 3D를 위한 AI 어시스턴트 및 MCP 서버: 비주얼 챗, 씬 객체 조작, 파이썬 스크립트 자율 생성 및 멀티 에이전트 작업 파이프라인</span>
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
            <h3 class="minor-detail-headline">복잡한 3D UI 메뉴 대신 자연어로 조명, 카메라, 메시 기하학을 실시간 수정하는 툴셋</h3>
            <div class="minor-detail-subheadline">Blender Python API를 FastMCP 프로토콜로 추상화하여 모델 제어 및 렌더링 파이프라인 자동화</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  3D 그래픽스 소프트웨어는 방대한 기능 메뉴와 가파른 학습 곡선으로 초심자에게 진입장벽이 높았습니다. 이 프로젝트는 LLM 에이전트가 사용자의 자연어 지시를 받아 씬 구조를 읽고, 조명 각도와 재질 셰이더를 즉시 조작할 수 있도록 MCP 엔드포인트를 제공합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> LLM Visual Chat &rarr; FastMCP Server &rarr; Blender Python IPC &rarr; 3D Viewport Realtime Update
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  단순한 텍스트 챗봇을 넘어 3D 뷰포트의 실시간 렌더 버퍼와 기하학 구조를 직접 조작하는 공간 인터랙션 에이전트의 가능성을 입증했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/SsKanDon/blender-ai-mcp-addon" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: filipe-campos/walph -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 6개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.12 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Claude Code를 내장한 초경량 크로스플랫폼 데스크톱 IDE&quot; : walph</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">filipe-campos/walph — 복잡한 확장 프로그램 설정 없이 단일 앱에서 Claude Code 터미널 세션, 파일 탐색기, 실시간 diff 프리뷰를 결합한 네이티브 개발 환경</span>
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
            <h3 class="minor-detail-headline">무거운 VS Code를 덜어내고 코딩 에이전트 터미널과 코드 트리를 1대1로 직결한 미니멀 작업공간</h3>
            <div class="minor-detail-subheadline">Webview 기반 초경량 쉘 위에서 Claude Code의 실행 승인, 파일 변경 감지, 깃 상태를 일원화</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  기존 무거운 일렉트론 IDE 환경에서 코딩 에이전트를 터미널로만 띄우면 파일 변경 사항을 한눈에 파악하기 어렵고, 매번 에디터를 번갈아 확인해야 했습니다. Walph는 에이전트와 인간 개발자의 시각적 싱크를 맞추는 데 집중했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Claude Code Daemon &rarr; Native PTY Session &rarr; In-App Diff Inspector &rarr; Zero-Latency Save
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  에이전트가 주도하고 인간이 승인하는 새로운 개발 흐름에 맞춘 전용 도구의 필요성을 증명했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/filipe-campos/walph" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: atunfrito/tuna-fonts -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 10개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.44 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;계정 가입도 텔레메트리도 없는 100% 로컬 윈도우 폰트 매니저&quot; : tuna-fonts</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">atunfrito/tuna-fonts — 클라우드 동기화와 유료 구독을 강요하는 기존 폰트 도구의 거품을 걷어낸 Windows 10/11 전용 오픈소스 글꼴 관리 스튜디오</span>
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
            <h3 class="minor-detail-headline">시스템 폰트 디렉토리를 깨끗하게 유지하며 수만 개의 OTF/TTF 글꼴을 가상 활성화</h3>
            <div class="minor-detail-subheadline">로컬 SQLite 기반 초고속 프리뷰 엔진과 서체 패밀리 태깅 기능 제공</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  상용 글꼴 관리 프로그램들이 비싼 월간 구독료를 요구하고 사용자 활동을 추적하는 것에 반발하여, 완전한 프라이버시와 무설정 단일 실행을 지향하는 오픈소스 도구로 탄생했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Local Font Directory &rarr; Fast FreeType Rasterizer &rarr; Temporary Windows Font Loading &rarr; No Registry Bloat
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  윈도우 레지스트리를 오염시키지 않고 필요할 때만 글꼴을 메모리에 동적 로드하는 효율적인 리소스 관리 구조를 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/atunfrito/tuna-fonts" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: snicolast/SegaRally2Native -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 82개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.54 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;전설의 레이싱 명작 Sega Rally 2의 무에뮬레이션 PC 네이티브 포트&quot; : SegaRally2Native</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">snicolast/SegaRally2Native — 레거시 아케이드/윈도우 98 바이너리를 현대 64비트 아키텍처와 DirectX 12/Vulkan 네이티브 런타임으로 이식한 정적 재컴파일러</span>
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
            <h3 class="minor-detail-headline">30fps 프레임 잠금을 해제하고 와이드스크린과 현대 게이밍 휠 컨트롤러를 네이티브 지원</h3>
            <div class="minor-detail-subheadline">바이너리 정적 디컴파일과 C++ 리패키징을 거쳐 최신 윈도우 11에서 무결점 144Hz 구동 달성</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  1998년 출시된 명작 세가 랠리 2는 윈도우 10/11에서 호환성 문제와 해상도 한계로 정상 실행이 불가능했습니다. 에뮬레이터 없이 기계어를 현대 C++로 재작성하는 정적 재컴파일 기술이 적용되어 네이티브 PC 게임으로 부활했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Model 3 / Win98 x86 ASM &rarr; Static Decompilation &rarr; Modern C++ Subsystems &rarr; 4K 144Hz Vulkan Rendering
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  고전 소프트웨어를 에뮬레이션 오버헤드 없이 영구 보존하고 현대 하드웨어의 최대 성능을 끌어내는 리컴파일 기법의 우수성을 입증했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/snicolast/SegaRally2Native" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: nestho/impacket-rs -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 31개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 17.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.74 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;파이썬 침투 테스트 전설 Impacket을 순수 Rust로 전면 재설계하다&quot; : impacket-rs</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">nestho/impacket-rs — 느린 파이썬 의존성과 메모리 취약점을 탈피하고 SMB, DCE/RPC, Kerberos 프로토콜을 메모리 안전한 고성능 Rust로 구현한 레드팀 도구</span>
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
            <h3 class="minor-detail-headline">외부 파이썬 인터프리터 없이 단일 바이너리로 구동되는 차세대 네트워크 프로토콜 분석 라이브러리</h3>
            <div class="minor-detail-subheadline">Tokio 비동기 런타임 기반의 초고속 패킷 처리와 강력한 타입 안정성 확보</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  오랜 기간 보안 업계의 표준이던 파이썬 Impacket은 복잡한 환경 의존성과 실행 속도 문제로 타깃 환경에 배포하기 까다로웠습니다. Rust 포팅을 통해 의존성 제로의 독립 실행 파일로 재탄생했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Network Socket &rarr; Rust Zero-Copy Parser &rarr; Async Tokio Stream &rarr; Memory-Safe SMB/RPC Exchange
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  보안 침투 및 인증 테스트 파이프라인에서 메모리 안전성과 10배 이상의 처리 속도 향상을 동시에 제공합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/nestho/impacket-rs" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: AbdoSarmini/claude-usage-widget-for-windows-taskbar -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 21개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.64 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;윈도우 11 작업표시줄에서 클로드 5시간 쿼터와 주간 한도를 실시간 확인&quot; : claude-usage-widget</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">AbdoSarmini/claude-usage-widget-for-windows-taskbar — 브라우저 대시보드를 매번 열 필요 없이 작업표시줄 시스템 트레이에서 Claude 잔여 토큰과 리셋 카운트다운을 표시하는 초경량 유틸리티</span>
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
            <h3 class="minor-detail-headline">코딩 에이전트 작업 중 갑작스러운 Rate Limit 차단을 사전에 방지하는 실시간 위젯</h3>
            <div class="minor-detail-subheadline">세션 쿠키를 안전하게 로컬 보관하며 앤스로픽 사용량 엔드포인트를 주기적으로 가볍게 폴링</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Claude Code 등 대형 에이전트로 작업할 때 사용량 한도 초과 시점이 예측되지 않아 작업 흐름이 끊기던 불편함을 해소하기 위해 등장한 실용적 오픈소스입니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Anthropic API Usage Check &rarr; Local Background Worker &rarr; Windows Taskbar Notification Bar
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  개발자의 주의를 분산시키지 않고 작업 환경의 가장자리에서 핵심 리소스 상태를 가시화하는 세심한 UX를 구현했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/AbdoSarmini/claude-usage-widget-for-windows-taskbar" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: MZULALI/xj-scanner -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 111개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 29.7시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.73 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;3달러 아두이노로 90년대 지프(Jeep) 엔진 컴퓨터를 해킹해 AI로 진단하다&quot; : xj-scanner</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">MZULALI/xj-scanner — 1991~1995년 구형 지프 차량의 비표준 OBD-I ECU 직렬 버스를 $3 아두이노 나노로 역공학하여 노트북에서 실시간 센서 로그와 DTC 에러를 AI로 진단</span>
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
            <h3 class="minor-detail-headline">값비싼 전용 스캐너 없이 올드카 ECU의 독점 시리얼 프로토콜을 해독하는 오픈 하드웨어</h3>
            <div class="minor-detail-subheadline">Arduino Nano + Python CLI + 로컬 LLM 결합으로 센서 이상 패턴과 정비 가이드 자동 산출</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  1996년 이전 생산된 구형 지프(XJ 체로키 등)는 표준 OBD-II가 없어 고장 진단 장비가 수백 달러에 달했습니다. 개발자는 아두이노 나노로 직렬 통신 핀을 탭핑하고 오픈소스 파이썬 드라이버를 개발해 문제를 해결했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> 1990s Jeep SCI Bus &rarr; $3 Arduino Nano &rarr; USB Serial &rarr; Python Telemetry & AI Diagnostic Agent
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  단돈 3달러의 저가 하드웨어와 AI 에이전트를 결합해 클래식 자동차 정비의 독점 장벽을 허문 대표적인 실천 사례입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/MZULALI/xj-scanner" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: ichitaso/Regitela -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 84개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.26 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;worse_query 취약점 기반 탈옥 없는 iOS 시스템 파일 탐색기 &amp; 툴박스&quot; : Regitela</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">ichitaso/Regitela — 순정 iOS 27 환경에서 파일 샌드박스를 우회해 시스템 숨김 캐시를 정리하고 고급 설정을 트윅할 수 있는 차세대 관리 도구</span>
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
            <h3 class="minor-detail-headline">애플의 엄격한 앱 샌드박스를 우회하여 장치 내부 스토리지를 탐색하는 네이티브 Swift 앱</h3>
            <div class="minor-detail-subheadline">worse_query 취약점을 활용한 시스템 디렉토리 읽기/쓰기 및 유령 캐시 일괄 삭제 기능 구현</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  탈옥(Jailbreak)이 불가능해진 최신 iOS 버전에서 연구자들과 파워 유저들이 파일 시스템에 직접 접근할 수 있는 통로로 주목받고 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> worse_query Exploit &rarr; Sandbox Bypass &rarr; Native Swift File Manager &rarr; Clean Storage
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  폐쇄적인 모바일 OS에서 보안 취약점을 합법적 사용자 편의와 시스템 최적화 도구로 승화시킨 흥미로운 성과입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/ichitaso/Regitela" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: MSNightmare/SignDrop -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 179개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.4시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.52 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Windows CLFS 인증 취약점을 뚫고 SYSTEM 권한을 탈취하는 0day PoC&quot; : SignDrop</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">MSNightmare/SignDrop — 윈도우 공통 로그 파일 시스템(CLFS) 커널 드라이버의 서명 검증 레이스 컨디션을 이용해 일반 사용자 권한을 SYSTEM 권한으로 즉시 승격하는 실전 익스플로잇</span>
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
            <h3 class="minor-detail-headline">최신 윈도우 11 환경에서도 여전히 잔존하는 커널 레벨 LPE 공격 벡터의 실체 증명</h3>
            <div class="minor-detail-subheadline">CLFS.sys 로그 블록 헤더 변조 및 가상 주소 테이블 조작을 통한 토큰 스왑 기술 적용</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  CLFS 드라이버는 마이크로소프트가 수차례 패치를 적용했음에도 여전히 복잡한 헤더 파싱 로직 때문에 로컬 권한 상승(LPE)의 온상으로 지목되어 왔습니다. 이번 연구는 잔여 공격 표면을 입증했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Low-Privilege Process &rarr; CLFS Log Block Manipulation &rarr; Kernel Token Overwrite &rarr; SYSTEM Shell Dropped
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  엔터프라이즈 보안 관제 팀에게 EDR 탐지 우회 기법의 세부 원리를 공개하고 사전 방어 룰셋을 정비할 기회를 제공합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/MSNightmare/SignDrop" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: United Airlines AI Agent Ban -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 169점</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 1.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 123.45 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;유나이티드 항공, AI 에이전트의 항공권 자동 대리 예매 전면 차단 선언&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">cbsnews.com — 웹 스크래핑과 컴퓨터 유즈(CUA) 에이전트가 최저가 항공권을 자동 탐색·결제하는 트래픽이 폭증하자 약관을 개정하고 봇 접속을 원천 차단한 첫 대형 항공사</span>
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
            <h3 class="minor-detail-headline">플랫폼의 부가 서비스 판매를 우회하는 자율 에이전트와 항공사 비즈니스 모델의 정면 충돌</h3>
            <div class="minor-detail-subheadline">수하물 추가, 좌석 지정 등 고수익 유료 옵션을 건너뛰는 최적화 봇에 대한 전방위 법적·기술적 방어선 구축</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 사건의 본질</div>
                <p class="minor-paragraph">
                  소비자를 대신해 웹사이트를 직접 클릭하고 결제까지 완료하는 AI 대리인(Agentic Shopper)이 현실화되자, 항공사들은 소비자의 화면 체류 시간과 충동구매에 기대던 전통적인 e커머스 매출 구조가 붕괴할 것을 우려하고 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[갈등 구조]</strong> AI CUA Agent (최저가 단일 결제) vs Airline Platform (좌석·보험 번들 판매 방어)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 산업적 파장</div>
                <p class="minor-paragraph">
                  향후 호텔, 공연 티켓, 렌터카 등 모든 예약 플랫폼으로 'AI 대리 예매 차단' 약관이 확산될 것이라는 신호탄으로 평가됩니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/" target="_blank" class="minor-link web">
                <i data-lucide="external-link" class="minor-icon"></i> 뉴스 원문 보기
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: Jane Street Datacenter Alarm -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 360점</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.1시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 58.70 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;연기 감지기 오작동으로 뉴욕 유일 데이터센터가 침수될 뻔한 제인 스트리트의 사고&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">michael.bacarella.com — 월스트리트 최고 퀀트 트레이딩 하우스 제인 스트리트가 건물 소방 감지기 오경보로 가스/수손 소화 설비가 터질 뻔했던 절체절명의 인프라 위기 회고록</span>
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
            <h3 class="minor-detail-headline">나노초 단위 고주파 매매(HFT) 인프라조차 물리적 센서 오류 하나에 전사 중단 위기를 맞을 수 있다는 교훈</h3>
            <div class="minor-detail-subheadline">먼지와 습기로 인한 광학 센서 오작동이 수천억 원 규모 거래 중단 사태로 번질 뻔한 경위 공개</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 사건의 본질</div>
                <p class="minor-paragraph">
                  소프트웨어의 무결성과 삼중화 페일오버를 갖췄더라도, 물리적 시설(서버룸 소화 배관, 연기 감지기)의 단일 장애점(SPOF)이 어떻게 전산망 전체를 마비시킬 수 있는지를 적나라하게 보여준 인프라 엔지니어링의 필독 사례입니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[위기 전개]</strong> Dust in Optical Detector &rarr; False Smoke Trigger &rarr; Halon Fire System Countdown &rarr; Emergency Abort
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  금융 및 미션 크리티컬 데이터센터의 물리적 안전 제어 시스템에 대한 독립 수동 오버라이드 절차의 중요성을 재환기했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/" target="_blank" class="minor-link web">
                <i data-lucide="external-link" class="minor-icon"></i> 기술 블로그 읽기
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: Safe Sand WebGL2 -->
        <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 270점</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.1시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 29.60 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;플러그인 없이 브라우저에서 60FPS로 쏟아지는 초사실적 모래 물리 시뮬레이션&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">av.github.io/safe-sand — WebGL2와 컴퓨트 셰이더를 활용해 수십만 개의 독립 모래 알갱이 마찰과 붕괴 역학을 웹 브라우저에서 실시간 렌더링하는 오픈 그래픽스 실험</span>
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
            <h3 class="minor-detail-headline">브라우저가 고사양 게임 엔진 수준의 연속체 입자 물리(MPM)를 지연 없이 소화함을 입증</h3>
            <div class="minor-detail-subheadline">GPU 텍스처 버퍼에 위치와 속도를 저장하고 프래그먼트 셰이더로 충돌 적분을 병렬 연산</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 사건의 본질</div>
                <p class="minor-paragraph">
                  과거 고성능 워크스테이션에서만 가능하던 입자 유체 및 과립 역학(Granular Dynamics)을 순수 웹 표준 기술만으로 가볍게 구현하여 전 세계 인터랙티브 그래픽스 개발자들을 매료시켰습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> GPU Texture State &rarr; WebGL2 Compute Pass &rarr; Particle Interaction Kernel &rarr; 60FPS Canvas Render
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  웹 기반 시각화 및 웹 게임 엔진에서 무거운 물리 라이브러리를 경량 셰이더 연산으로 대체할 수 있는 고효율 레퍼런스를 제시했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://av.github.io/safe-sand/" target="_blank" class="minor-link web">
                <i data-lucide="external-link" class="minor-icon"></i> 실시간 데모 체험
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: Maya Site Discovered by AI -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 893점</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 83.54 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;AI 에이전트 군단이 공개 라이다(LiDAR) 지도를 뒤져 미지의 마야 고대 유적을 발견하다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">pietromiotti.com — 고고학자 피에트로 미오티가 자율 에이전트들에게 멕시코 밀림의 오픈 지형 고도 데이터를 분석시켜 학계에 기록되지 않은 미발굴 마야 피라미드와 광장을 최초 식별</span>
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
            <h3 class="minor-detail-headline">인간 연구자가 수십 년간 찾지 못한 고고학적 지형 패턴을 수시간 만에 발굴한 과학적 쾌거</h3>
            <div class="minor-detail-subheadline">디지털 표고 모델(DEM) 필터링과 비전 에이전트 파이프라인으로 열대우림 수목을 제거하고 고대 구조물 검출</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 사건의 본질</div>
                <p class="minor-paragraph">
                  멕시코 국립통계지리정보원(INEGI)의 방대한 오픈 라이다 데이터를 AI 에이전트들에게 분할 배분하여, 빽빽한 정글 수풀 아래 숨겨진 직각 벽면과 마야 고유의 건축 축(Axis)을 자율 식별하도록 했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Open LiDAR Elevation Data &rarr; Tree Canopy Filter &rarr; Vision Agent CNN &rarr; Unmapped Maya City Found
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  기초 과학 데이터가 공개되어 있을 때 자율 AI가 인류의 지식 지평을 실제로 넓힐 수 있음을 증명한 가장 감동적인 사례로 꼽힙니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://pietromiotti.com/latest/maya-site" target="_blank" class="minor-link web">
                <i data-lucide="external-link" class="minor-icon"></i> 발견 리포트 전문 보기
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: Weight Space LP -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 227점</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.3시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 22.09 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;역전파 학습 없이 선형 계획법(LP)으로 신경망 가중치 공간을 직접 수술하다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">nathan.rs — 거대 신경망을 수십억 번 경사하강법으로 재훈련하지 않고, 수학적 선형 계획법 제약 조건만으로 모델 내부의 특정 지식과 행동을 정밀 제어·성형하는 획기적 논문</span>
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
            <h3 class="minor-detail-headline">학습의 확률적 불안정성을 극복하고 최적화 솔버로 가중치를 직접 프로그래밍하는 새로운 시도</h3>
            <div class="minor-detail-subheadline">ReLU 활성화 함수의 볼록 폴리토프 기하학을 활용해 특정 입출력 매핑을 단 한 번의 LP 해법으로 주입</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 사건의 본질</div>
                <p class="minor-paragraph">
                  신경망을 '블랙박스 확률 기계'로 취급하던 통념에서 벗어나, 고전 최적화 기법인 심플렉스/내부점 알고리즘으로 가중치를 직접 수정하여 환각을 교정하고 안전 제약을 강제할 수 있는 이론적 기반을 마련했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Behavioral Constraint Equations &rarr; Simplex LP Solver &rarr; Direct Weight Modification &rarr; Zero-Retraining Alignment
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  거대 언어 모델의 지식 편집(Knowledge Editing)과 정렬 작업을 고비용 파인튜닝 없이 즉시 완료할 수 있는 기하학적 돌파구를 열었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://nathan.rs/posts/weight-space-lp/" target="_blank" class="minor-link web">
                <i data-lucide="external-link" class="minor-icon"></i> 기술 아티클 읽기
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: Voltage Glitching A100 -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 245점</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 20.47 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;하드웨어 전압 글리칭으로 암호화폐 채굴 카드의 잠긴 엔비디아 A100을 부활시키다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">blog.kate.land — 디스플레이 포트와 텐서 코어가 펌웨어로 잠겨 버려진 폐 채굴 전용 가속기(CMP 시리즈)에 마이크로초 단위 전압 글리칭을 가해 정품 A100으로 속이고 드라이버 잠금을 해제한 실전 하드웨어 해킹</span>
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
            <h3 class="minor-detail-headline">하드웨어 보안 퓨즈와 벤더의 인위적 제품 티어 다운그레이드 방벽을 무력화한 오픈 하드웨어 연구</h3>
            <div class="minor-detail-subheadline">FPGA 기반 펄스 제너레이터로 부팅 시점 VCORE 레일을 순간 쇼트시켜 인증 체크 우회 달성</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 사건의 본질</div>
                <p class="minor-paragraph">
                  엔비디아가 채굴 전용으로 팔았던 저가형 CMP 가속기는 사실 정규 A100과 동일한 실리콘 다이를 탑재하고 있었습니다. 연구자는 전압 글리칭으로 펌웨어 무결성 검증을 건너뛰어 풀스펙 AI 연산 가속기로 탈바꿈시켰습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> CMP Mining Card &rarr; Precise Microsecond Voltage Drop &rarr; Skip Fuse Check &rarr; Authentic A100 Driver Loaded
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  전자 폐기물로 버려질 뻔한 구형 하드웨어를 수리하고 재활용할 수 있는 하드웨어 리버스 엔지니어링의 위력을 증명했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/" target="_blank" class="minor-link web">
                <i data-lucide="external-link" class="minor-icon"></i> 해킹 기술 블로그 보기
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: Scion Kei Truck in America -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 552점</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 26.9시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 20.50 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;토요타 사이언(Scion) 브랜드 부활: 미국 시장을 겨냥한 초소형 경형 전기 트럭(Kei Truck) 공개&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">theautopian.com — 2016년 단종되었던 청년 타깃 브랜드 Scion을 부활시키고, 비싸고 거대한 픽업트럭 일색인 미국 시장에 2천만 원대 실용적인 미니 전기 트럭을 투입하는 토요타의 파격 행보</span>
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
            <h3 class="minor-detail-headline">과대화된 미국 픽업트럭 시장에서 일본식 경차(Kei Car) 유틸리티에 대한 북미 소비자들의 열망 폭발</h3>
            <div class="minor-detail-subheadline">도심 주행과 소상공인 화물 운송에 최적화된 컴팩트 전동화 플랫폼으로 틈새시장 공략</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 사건의 본질</div>
                <p class="minor-paragraph">
                  미국의 보행자 안전 기준과 배기가스 규제 때문에 수입이 금지되었던 일본 경트럭의 수요가 북미에서 폭발하자, 토요타가 미국 연방 안전 기준(FMVSS)을 충족하는 전용 전기 경트럭을 직접 기획했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[시장 전환]</strong> 8,000lb Monster Pickups &rarr; Consumer Fatigue &rarr; Scion EV Kei Truck (Compact, Safe, $20k)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 산업적 파장</div>
                <p class="minor-paragraph">
                  자동차 제조사들이 크고 무거운 고가 차량만 만들던 관성에서 벗어나, 진정한 실용성과 지속 가능성을 추구하는 계기가 될 것으로 기대됩니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.theautopian.com/scion-is-back-and-its-going-to-sell-a-kei-truck-in-america/" target="_blank" class="minor-link web">
                <i data-lucide="external-link" class="minor-icon"></i> 기사 전문 보기
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: Apple New Mac App Local AI -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 508점</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 20.03 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;애플, 맥에서 오픈소스 로컬 AI 모델을 클릭 한 번으로 돌리는 신규 전용 앱 준비&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">9to5mac.com — 복잡한 터미널 명령어(Ollama, HuggingFace 등) 없이도 일반 사용자가 로컬 파운데이션 모델을 다운로드하고 하드웨어 통합 메모리로 실행할 수 있는 macOS 공식 네이티브 앱 개발 정황 포착</span>
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
            <h3 class="minor-detail-headline">애플 실리콘의 통합 메모리 우위를 앞세워 온디바이스 AI 생태계의 대중화를 직접 장악하려는 전략</h3>
            <div class="minor-detail-subheadline">Metal 및 MLX 프레임워크와 결합하여 비개발자도 프라이빗 로컬 인텔리전스를 원클릭 향유</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 사건의 본질</div>
                <p class="minor-paragraph">
                  M4 칩셋의 강력한 NPU와 대용량 통합 메모리를 갖춘 맥 하드웨어를 진정한 '개인용 AI 워크스테이션'으로 포지셔닝하려는 애플의 소프트웨어 생태계 확장 계획이 유출되었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[아키텍처]</strong> Native Mac GUI &rarr; Apple MLX Runtime &rarr; Unified Memory Zero-Copy &rarr; Private Local Intelligence
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  오픈소스 로컬 모델 구동이 더 이상 엔지니어만의 전유물이 아니라 대중적인 운영체제 기본 기능으로 편입되는 변곡점을 예고합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/" target="_blank" class="minor-link web">
                <i data-lucide="external-link" class="minor-icon"></i> 단독 보도 읽기
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: Tracking Anthropic Vulnerabilities -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 447점</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 24.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 18.26 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;앤스로픽의 AI 보안 전담 조직 'Glasswing'이 탐지한 제로데이 취약점 현황과 익스플로잇 추적기&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">vulncheck.com — 사이버 방어 목적으로 구성된 앤스로픽 연구팀이 프론티어 AI를 이용해 오픈소스 및 상용 인프라에서 발견한 수십 개의 미공개 고위험 제로데이 취약점과 책임 있는 공개 절차 보고서</span>
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
            <h3 class="minor-detail-headline">AI 기반 자율 보안 분석이 인간 화이트햇 해커의 취약점 발굴 속도를 수백 배 앞지르기 시작한 현실</h3>
            <div class="minor-detail-subheadline">다양한 C/C++ 오픈소스 라이브러리의 버퍼 오버플로우와 로직 결함을 사전 탐지하고 패치 유도</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 사건의 본질</div>
                <p class="minor-paragraph">
                  앤스로픽의 보안 하네스 Glasswing 프로젝트는 AI가 복잡한 C 코드베이스를 탐색하여 수십 년간 숨겨져 있던 제로데이를 찾아내는 능력을 입증하며, 방어자와 공격자 사이의 군비 경쟁을 가속화하고 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[프로세스]</strong> Glasswing AI Scanner &rarr; Deep Code Path Verification &rarr; Zero-Day Triaging &rarr; Responsible Vendor Disclosure
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  소프트웨어 벤더들에게 AI 시대의 초고속 공격에 대응하기 위한 보안 패치 공시 주기 단축을 강제하고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.vulncheck.com/blog/anthropic-glasswing-november-update" target="_blank" class="minor-link web">
                <i data-lucide="external-link" class="minor-icon"></i> 취약점 보고서 보기
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
