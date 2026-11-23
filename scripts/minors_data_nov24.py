# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-24

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
          직전 발행(11월 23일) 이후 30시간 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 관심 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: EL4CTEO/shrink-anything -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 12개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.46 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;코드가 줄어들어도 내 테스트가 통과할 때만 삭제를 확정한다&quot; : shrink-anything</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">EL4CTEO/shrink-anything — 19개 언어 코드베이스에서 죽은 코드·불필요 파일·의존성을 찾아 테스트 스위트 검증 후 안전하게 도려내는 Rust CLI·MCP 서버 (MIT)</span>
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
            <h3 class="minor-detail-headline">AI 코딩 에이전트가 쌓아올린 미사용 코드·패키지·에셋을 테스트 기반 회귀 검증으로 정밀 다이어트하는 Rust 도구</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Rust 네이티브 바이너리 + npm/crates.io 배포 · 19개 언어 지원 · Claude Code 플러그인 &amp; MCP 서버 통합</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  코딩 에이전트가 코드를 생성하는 속도가 빨라질수록, 아무도 호출하지 않는 함수·임포트되지 않는 파일·쓰지 않는 의존성과 이미지가 저장소에 쌓여 에이전트 컨텍스트와 CI 빌드 시간을 갉아먹습니다. <code>shrink-anything</code>은 단순히 정적 분석으로 경고를 띄우는 대신, 후보를 하나씩 삭제한 뒤 사용자의 기존 테스트 스위트를 직접 실행해 통과한 삭제분만 남기는 실용적 접근으로 공개 6.8시간 만에 주목받고 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[안전 축소 루프]</strong> 19-Language Dead-Code Scan &rarr; Isolated Cut Candidate &rarr; Run User Test Suite &rarr; Commit Only Passing Cuts
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  에이전트가 작성한 코드 비대화(Bloat) 문제를 해결하기 위해 Claude Code 플러그인과 MCP 서버 인터페이스를 함께 제공하여, 리팩터링 자동화 파이프라인의 안전망 역할을 수행합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/EL4CTEO/shrink-anything" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: CybeDefend/cybedefend -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 10개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.39 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;단일 명령 보안 감사, 발견한 모든 취약점은 실제 익스플로잇으로 증명한다&quot; : cybedefend</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">CybeDefend/cybedefend — 코딩 에이전트가 직접 구동하는 셀프호스팅 오픈소스 Snyk 대체 에이전틱 ASPM 플랫폼 (AGPL-3.0)</span>
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
            <h3 class="minor-detail-headline">오탐 경보 나열을 끝내고 AI 에이전트가 익스플로잇 검증까지 완료해 보고하는 셀프호스팅 AppSec 플랫폼</h3>
            <div class="minor-detail-subheadline">AGPL-3.0 라이선스 · TypeScript 풀스택 · Docker 커뮤니티 셀프호스팅 · AI 보안 스캐너 연동</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  기존 정적 보안 도구(SAST/SCA)는 수백 개의 거짓 양성(False Positive) 경보를 쏟아내 개발자들이 경고를 무시하게 만듭니다. <code>CybeDefend</code>는 코딩 에이전트 워크플로 안에서 단 한 줄 명령으로 코드 취약점을 탐지할 뿐 아니라, 발견된 취약점이 실제로 악용 가능한지 익스플로잇 검증(Proof-of-Exploit) 단계까지 자동 수행하는 오픈소스 Snyk 대안으로 등장해 7.2시간 만에 10스타를 확보했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[검증 보안 파이프라인]</strong> Single-Command Agent Scan &rarr; Context Reachability Analysis &rarr; Automated Exploit PoC &rarr; Verified Remediation
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  클라우드 상용 AppSec SaaS에 소스코드를 올리기 꺼리는 팀을 위해 자체 인프라에 Docker로 배포 가능한 에이전트 주도 보안 감사 기준을 제시합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/CybeDefend/cybedefend" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://cybedefend.com" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 사이트
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: DerKezorm/nextime -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 4개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.81 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;iCloud·Google·CalDAV를 하나로 묶은 가족·소규모 팀 셀프호스팅 캘린더&quot; : nextime</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">DerKezorm/nextime — 자연어 빠른 입력(&quot;Tomorrow 3 pm dentist&quot;)과 내장 공휴일·CalDAV 서버를 결합한 Python 캘린더 (AGPL-3.0)</span>
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
            <h3 class="minor-detail-headline">가족과 소규모 그룹의 분산된 일정을 내 서버 위 단일 타임라인과 CalDAV로 통합하는 셀프호스팅 캘린더</h3>
            <div class="minor-detail-subheadline">AGPL-3.0 라이선스 · Python 백엔드 + Docker Compose · CalDAV 서버 내장 · 자연어 빠른 일정 등록</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  가족 구성원마다 iCloud, Google, 사내 CalDAV 등 서로 다른 캘린더에 일정을 기록하면 공동 일정을 조율하기 어렵고 개인 일정 데이터는 빅테크 클라우드에 종속됩니다. <code>nextime</code>은 직관적인 Today·Week·Month 뷰와 드래그 이동, 공유자 이니셜 표시, 자연어 빠른 입력, 그리고 스마트폰 기본 캘린더 앱과 연동되는 CalDAV 서버를 한 번에 묶어 4.9시간 만에 주목받았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[통합 일정 허브]</strong> iCloud / Google / Local Feeds &rarr; Self-Hosted Python Core &rarr; CalDAV Sync + Shared Web Views
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  복잡한 그룹웨어 설치 없이 Docker Compose 한 번으로 프라이버시 친화적인 가족·팀 전용 캘린더 서버를 구축할 수 있는 완성도 높은 실사용 사례입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/DerKezorm/nextime" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: SulphurS16/Regaliant -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 133개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.6시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 12.48 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;CPU 에뮬레이션 없이 PS5 데몬즈 소울 리메이크를 Windows Vulkan으로 네이티브 구동&quot; : Regaliant</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">SulphurS16/Regaliant — 본인 소유의 PS5 PPSA01341 바이너리를 Windows 재구현 시스템 라이브러리와 Vulkan으로 실행하는 Rust 비공식 PC 포트 (GPL-3.0)</span>
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
            <h3 class="minor-detail-headline">x86-64 CPU 명령어 변환을 거치지 않고 PS5 시스템 라이브러리 호환 계층과 Vulkan으로 구동하는 데몬즈 소울(2020) PC 포트</h3>
            <div class="minor-detail-subheadline">GPL-3.0 라이선스 · Rust 워크스페이스(crates/) · 게임 데이터·키 미포함 · PS5 v01.007.000 사용자 덤프 기반</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  소니 PS5 독점작인 블루포인트 게임즈의 <em>데몬즈 소울(2020)</em>은 PC판이 공식 출시되지 않아 콘솔 외부에서는 구동할 수 없었습니다. <code>Regaliant</code>는 PS5와 PC가 동일한 x86-64 아키텍처를 공유한다는 점에 착안해 CPU 에뮬레이션 없이 PS5 OS 시스템 라이브러리를 Windows용 Rust 크레이트로 재구현하고 그래픽을 Vulkan으로 연결해 10.6시간 만에 133스타를 끌어모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[호환 계층 구조]</strong> User PS5 Executable (PPSA01341) &rarr; Rust PS5 System Lib Reimpl &rarr; Native Windows + Vulkan Backend
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  저작권 준수를 위해 게임 코드·데이터·복호화 키를 일절 포함하지 않고 사용자가 보유한 정품 덤프만 연결하도록 분리한 정밀 콘솔 호환성 레이어 사례입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/SulphurS16/Regaliant" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: duwqijlk/browser-capture -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 129개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 14.4시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 8.93 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;외부 패키지 0개 · Runtime.enable 흔적 제로로 안티디버그를 우회하는 CDP 역공학 CLI&quot; : browser-capture</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">duwqijlk/browser-capture — Node.js 22+ 네이티브 WebSocket으로 BitBrowser·AdsPower·Chrome에 붙어 익명 Hook·정적/동적 JS를 덤프하는 Agent Skill (MIT)</span>
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
            <h3 class="minor-detail-headline">Runtime.enable 탐지와 스택 트레이스 노출을 차단하고 Proxy+WeakMap으로 네이티브 함수를 은닉하는 CDP 캡처 스킬</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Node.js &gt;= 22 (Zero Dependencies) · SKILL.md 표준 AI Agent Skill · 67개 테스트 통과</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Playwright나 Puppeteer 같은 기존 CDP 도구는 <code>Runtime.enable</code>을 호출하는 순간 브라우저 안티봇·안티디버그 스크립트의 <code>console</code> getter 함정이나 <code>Error.stack</code> 검사에 즉시 탐지됩니다. <code>browser-capture</code>는 Node.js 22+ 내장 <code>fetch</code>·<code>WebSocket</code>만으로 CDP에 직결해 <code>Runtime.enable</code>을 끄고, 네트워크 응답 계층에서 <code>debugger</code> 문을 등길이 공백 블록으로 치환해 14.4시간 만에 129스타를 기록했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[무흔적 CDP 파이프라인]</strong> Native Node 22 WebSocket &rarr; Zero Runtime.enable + Proxy/WeakMap Hook &rarr; Fetch.enable Debugger Strip &rarr; Full JS/Callstack Dump
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  <code>SKILL.md</code>가 기본 내장되어 있어 코딩·보안 분석 에이전트가 웹 프론트엔드 네트워크 계층과 난독화 스크립트를 직접 검사할 때 즉시 장착 가능한 경량 역공학 툴킷입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/duwqijlk/browser-capture" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: mbzuai-oryx/LoopedWSP -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 20개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 16.4시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.22 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;LLM이 직접 트랜스포머 가중치와 루프 회로를 설계해 장기 알고리즘을 푼다&quot; : LoopedWSP</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">mbzuai-oryx/LoopedWSP — 경사하강법 학습 대신 LLM이 가중치 공간을 직접 프로그래밍하는 루프형 트랜스포머 아키텍처 (MIT)</span>
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
            <h3 class="minor-detail-headline">LLM이 직접 작성한 루프형 트랜스포머(Looped Transformer) 가중치로 수만 스텝의 알고리즘 추론을 정확히 실행하는 연구</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · MBZUAI Oryx Lab + Claude Opus 5.5 공저 · Python 프롬프트 &amp; 가중치 아티팩트 공개</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  고정된 깊이의 일반 트랜스포머는 입력 길이나 알고리즘 단계가 길어질수록 추론 정확도가 급락합니다. MBZUAI 연구진과 AI 공저 연구팀이 공개한 <code>LoopedWSP</code>(Looped Weight-Space Programming)는 데이터로 가중치를 학습시키는 대신, LLM이 직접 루프형 트랜스포머의 어텐션·MLP 가중치를 프로그래밍해 반복 실행되도록 설계해 긴 알고리즘 연산을 처리하는 새로운 패러다임을 열었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[가중치 공간 프로그래밍]</strong> Algorithmic Spec &rarr; LLM Synthesizes Transformer Weights &rarr; Recurrent Looped Execution &rarr; Exact Long-Horizon Output
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  신경망 가중치를 역전파의 산물이 아닌 'LLM이 컴파일하는 프로그램 목적 코드'로 취급하는 가중치 공간 프로그래밍의 최신 실증 코드와 가중치를 제공합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/mbzuai-oryx/LoopedWSP" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://mbzuai-oryx.github.io/LoopedWSP/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 연구 블로그
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: chanke17/KuroCat -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 219개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 21.7시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 10.11 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;게임 속 풀키 입력·마우스 속도에 2.5D 구면 회전과 사냥 동공으로 반응하는 네이티브 고양이&quot; : KuroCat</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">chanke17/KuroCat — macOS(IOHIDManager)·Windows(Raw Input)·Linux(XInput2/evdev) 하드웨어 입력을 실시간 시각화하는 초경량 데스크톱 펫 (MIT)</span>
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
            <h3 class="minor-detail-headline">일렉트론 없이 플랫폼별 OS 네이티브 API로 구현한 전상태 하드웨어 입력 반응형 2.5D 데스크톱 펫</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · macOS(Swift/IOHIDManager) · Windows(C++17/Raw Input) · Linux(GTK3/Cairo/XInput2·evdev)</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  기존 Bongo Cat류 데스크톱 펫들은 웹뷰 기반이라 CPU/메모리를 과도하게 쓰거나, 게임 중 <code>WASD</code> 장시간 누름 및 다중 동시 키 입력을 놓치는 경우가 많았습니다. <code>KuroCat</code>은 macOS·Windows·Linux 각각에 최적화된 커널 HID/Raw Input 리스너를 네이티브 C++17·Swift로 직접 구현하고 Live2D 방식의 2.5D 구면 머리 회전·3키 동시 입력 시 뒷발 누르기 애니메이션까지 넣어 21.7시간 만에 219스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[크로스플랫폼 네이티브 엔진]</strong> IOHIDManager / Raw Input / evdev &rarr; 2.5D Spherical Head Projection &rarr; CoreGraphics / GDI+ / Cairo Overlay
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  3대 데스크톱 OS의 저수준 입력 후킹과 클릭 투과(Click-through) 투명 오버레이 렌더링을 일관된 아키텍처로 구현한 경량 네이티브 그래픽스 교본입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/chanke17/KuroCat" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: R44VC0RP/dashsplat -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 161개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.6시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.30 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;테슬라 6채널 블랙박스 영상으로 1cm 도로 아틀라스와 3인칭 주행 3D 월드를 빚다&quot; : dashsplat</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">R44VC0RP/dashsplat — 6개 대시캠 텔레메트리·포즈 보정·408만 가우시안 스플랫·Difix 디퓨전 복원을 24시간 에이전트 협업으로 구축 (Apache-2.0)</span>
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
            <h3 class="minor-detail-headline">공장 캘리브레이션 데이터 없이 테슬라 HW4 주행 영상만으로 전체 도시 주행 장면을 3D 가우시안 스플랫으로 재구성한 실험</h3>
            <div class="minor-detail-subheadline">Apache-2.0 라이선스 · Python 비전 파이프라인 + Web Viewer · 12,927프레임 포즈 추정 · 4.08M 스플랫</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  자율주행 시뮬레이터를 구축하려면 고가의 LiDAR 매핑 차량과 정밀 팩토리 캘리브레이션이 필수라고 여겨졌습니다. 개발자 Ryan Vogel이 AI 코딩 에이전트 팀을 지휘해 단 하루 밤낮 만에 구축한 <code>dashsplat</code>은 자신의 Tesla Model 3(HW4) 6개 카메라 영상과 프레임 내장 텔레메트리만으로 렌즈 왜곡·롤링 셔터·6자유도 궤적을 역산하고, 도로 아틀라스와 408만 개 가우시안 스플랫, NVIDIA Difix-ref 기반 3인칭 추격 뷰까지 복원해 25.6시간 만에 161스타를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[3D 월드 재구성]</strong> 6-Cam Dashcam + Telemetry &rarr; Self-Calib &amp; 6-DoF Poses &rarr; 4.08M Gaussian Splats + 1cm Road Mesh &rarr; Difix Chase View
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  단계별 성공 지표뿐 아니라 실패한 실험 리포트(<code>REPORT.md</code>)까지 투명하게 공개해 AI 에이전트 기반 고속 컴퓨터 비전 R&amp;D의 교과서적인 사례를 제시합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/R44VC0RP/dashsplat" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: manuelgscom/rumor-village -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 17개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 28.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.61 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;마을 주민 100명이 전부 로컬 파인튜닝 LLM으로 수다 떨며 소문을 왜곡시킨다&quot; : rumor-village</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">manuelgscom/rumor-village — 클라우드 API 없이 단일 GPU 위 llama.cpp(CUDA/Vulkan)로 100명 NPC의 소문 전파를 시뮬레이션하는 오프라인 3D 게임 (MIT)</span>
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
            <h3 class="minor-detail-headline">전용 파인튜닝 GGUF 모델(rumor-village-e4b)과 llama.cpp로 100명의 NPC가 실시간 음모를 엮는 로컬 AI 게임</h3>
            <div class="minor-detail-subheadline">MIT 코드 / Apache-2.0 모델 · Web Demo + Linux/Windows 빌드 · llama.cpp (CUDA/Vulkan) 로컬 추론</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI NPC 게임들은 매 대화마다 유료 클라우드 LLM API를 호출하느라 지연 시간과 비용이 감당되지 않는 경우가 많았습니다. <code>rumor-village</code>는 게임 전용으로 파인튜닝된 소형 모델(<code>rumor-village-e4b-GGUF</code>)을 사용자 그래픽카드 위 <code>llama.cpp</code>에서 직접 구동해, 3D 마을에 소문 하나를 떨어뜨리면 최대 100명의 주민이 입에서 입으로 말을 옮기며 왜곡하고 엉뚱한 사건을 일으키는 과정을 완전 오프라인으로 구현했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[로컬 AI 시뮬레이션]</strong> Player Rumor Injection &rarr; 100 NPC Event Graph &rarr; Fine-Tuned Local GGUF (llama.cpp) &rarr; Emergent Twist
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  거대 상용 모델 의존 없이 목적 특화 파인튜닝 소형 모델(SLM)과 로컬 추론기만으로도 수백 개 에이전트 상호작용 게임을 구현할 수 있음을 증명합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/manuelgscom/rumor-village" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://manuelgs.com/en/rumor-village/demo/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 웹 데모 체험
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: Nvidia Reinstates Jensen Huang as CEO -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 1,807점 · 2,901댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.8시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 206.08 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;엔비디아 이사회, 젠슨 황 CEO·사장 전격 복귀 — 의회 반발·Polymarket 34만 달러 의심 베팅 파장까지&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Nvidia Reinstates Jensen Huang as CEO — 공식 복귀 발표(1,700점) 및 미 의회 비판·NYT·Polymarket 클러스터 분석 통합</span>
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
            <h3 class="minor-detail-headline">엔비디아 이사회가 젠슨 황을 사장 겸 CEO로 재선임하며 AI 반도체 업계·정치권·예측시장을 동시에 뒤흔든 빅뉴스</h3>
            <div class="minor-detail-subheadline">CNBC·Nvidia 공식 뉴스룸(50611588)·미 의회 반응(50618490)·NYT(50616243)·WSJ Polymarket(50617640) 통합 클러스터</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  엔비디아 이사회가 젠슨 황(Jensen Huang)을 다시 사장 겸 CEO 및 이사로 재선임했다는 소식이 전해지자 해커뉴스 1면에는 CNBC 속보(1,807점·댓글 2,901개)와 엔비디아 공식 보도자료(1,700점)가 나란히 폭발했습니다. 연이어 미 의회 내 강경 비판 보도와 정치적 배경을 다룬 NYT 기사, 그리고 발표 직전 예측시장 Polymarket에서 34만 달러 이상 수익을 거둔 2개의 의심 베팅 클러스터를 다룬 WSJ 보도까지 꼬리를 물며 오늘 최대 이슈 클러스터를 형성했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파생 이슈 클러스터]</strong> Board Reinstatement (50611576 / 50611588) &rarr; Congress &amp; NYT Fallout &rarr; $340k Polymarket Timing Probe
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링·산업 임팩트</div>
                <p class="minor-paragraph">
                  글로벌 AI 컴퓨팅 인프라 공급망의 정점에 선 엔비디아의 리더십 변동과 규제·거버넌스 리스크는 GPU 수급 및 차세대 AI 아키텍처 로드맵 전반의 불확실성 변수로 직결되고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 기사 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50611576" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (2,901댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: Per Arm's request, this site will be discontinued on 4 December 2026 -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 685점 · 137댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 197.14 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Arm 법무팀의 경고: 개발자들의 성지였던 AArch64 명령어 웹 레퍼런스 12월 4일 폐쇄&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">arm.jonpalmisc.com — Armv8-A/v9-A 명령어·시스템 레지스터 WebAssembly 검색 사이트가 Arm 측 법적 조치 통보로 종료 예고</span>
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
            <h3 class="minor-detail-headline">저수준 시스템·커널 엔지니어들이 수년간 의존해 온 개인 개발자의 Arm ISA 레퍼런스가 법적 압박으로 문을 닫는다</h3>
            <div class="minor-detail-subheadline">arm.jonpalmisc.com · AArch64 Base/SIMD/SVE/SME &amp; System Registers · 2026-12-04 종료 예정</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Arm 공식 PDF 매뉴얼은 수천 페이지에 달해 검색이 불편한 반면, 개인 개발자 Jon이 WebAssembly 기반으로 만든 <code>arm.jonpalmisc.com</code>은 Armv8-A/v9-A 명령어(Base, SIMD, SVE, SME)와 AArch64/32 시스템 레지스터를 0.1초 만에 조회할 수 있어 Arm 소속 엔지니어들조차 애용하던 명물 사이트였습니다. 그러나 오늘 Arm 법무팀이 사이트를 내리지 않으면 법적 조치에 들어가겠다고 통보하면서 3.5시간 만에 HN 685점의 거센 성토가 쏟아졌습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[생태계 갈등]</strong> Official Heavy PDF Manuals &rarr; Fast Community WASM Reference &rarr; Legal Takedown Notice (Dec 4)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  하드웨어 아키텍처 문서의 저작권 통제가 오픈소스 컴파일러·커널 커뮤니티의 개발 생산성과 신뢰를 얼마나 쉽게 훼손할 수 있는지 보여주는 상징적 사건입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://arm.jonpalmisc.com/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 사이트 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50617499" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (137댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: Dario is hyping the dangers so OSS models are illegal -->
        <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 840점 · 494댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 148.69 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;얀 르쿤의 직격: 다리오 아모데이는 오픈소스 모델을 불법화해 독점 통제권을 쥐려 위험을 과장한다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Yann LeCun vs Dario Amodei — AI 안전 규제 프레임을 둘러싼 폐쇄형 프론티어 진영과 오픈웨이트 진영의 정면 충돌</span>
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
            <h3 class="minor-detail-headline">AI 규제 포획(Regulatory Capture) 논쟁을 재점화시킨 얀 르쿤의 앤스로픽 CEO 공개 저격</h3>
            <div class="minor-detail-subheadline">Yann LeCun (@ylecun) 성명 · HN 840점 · 494댓글 격론 · 오픈소스 AI 합법성 논쟁</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 튜링상 수상자 얀 르쿤(Yann LeCun)이 앤스로픽 CEO 다리오 아모데이의 종말론적 AI 위험 경고를 정면으로 겨냥해 <em>"다리오가 위험을 과장하는 이유는 오픈소스(OSS) 모델을 불법화해 자신이 통제권을 유지하려는 것"</em>이라는 직설적인 포스트를 올리며 5.6시간 만에 HN 840점과 약 500개에 달하는 댓글 논쟁이 불붙었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[규제 이념 대립]</strong> Closed Frontier Safety Regulation &harr; Regulatory Capture Warning &harr; Open-Weight Ecosystem Defense
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  컴퓨트 임계치 규제와 모델 가중치 공개 제한 법안이 논의되는 시점에서, 오픈소스 AI 개발 생태계의 생존권과 소수 기업의 과점 우려가 정면으로 맞부딪치고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://twitter.com/ylecun/status/2124550037912920090" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 포스트 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50615308" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (494댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: GLM-5.4 Loop Transformer -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 997점 · 328댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 78.74 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;첫 루프 트랜스포머(Loop Transformer)로 범용 코딩 지능을 겨냥한 차세대 모델&quot; : GLM-5.4</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">z.ai/blog/glm-5.4 — 순환 연산 기반 루프 트랜스포머 아키텍처를 도입한 코딩 모델 GLM-5.4 공개 및 Coding Plan 출시 클러스터</span>
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
            <h3 class="minor-detail-headline">고정 깊이 트랜스포머의 한계를 넘기 위해 Z.ai가 첫 루프 트랜스포머 구조를 상용 코딩 모델에 적용한 GLM-5.4</h3>
            <div class="minor-detail-subheadline">z.ai 공식 발표 · HN 997점 · 파생 공지(50608662·50607775) 통합 · GLM Coding Plan 즉시 제공</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Z.ai가 자사 최초의 <strong>루프 트랜스포머(Loop Transformer)</strong> 기반 범용 코딩 모델 <code>GLM-5.4</code>를 공개하고 모든 GLM Coding Plan 사용자에게 즉시 배포하면서 HN에서 997점(댓글 328개)의 폭발적인 관심을 끌었습니다. 파라미터 수만 키우는 대신 레이어 내부 순환 반복으로 추론 깊이를 동적으로 늘리는 접근이 코딩 에이전트 성능에 어떤 도약을 가져오는지가 최대 화두입니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[아키텍처 진화]</strong> Fixed-Depth Attention &rarr; Recurrent Loop Transformer Blocks &rarr; Deeper Iterative Code Reasoning
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  GH B2의 학계 연구(<code>LoopedWSP</code>)와 맞물려, 실제 상용 코딩 모델 라인업까지 '루프형 트랜스포머' 패러다임이 본격 진입했음을 보여주는 분기점입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://z.ai/blog/glm-5.4" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 블로그 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50609685" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (328댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: The next circle of security hell -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 224점 · 132댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 11.2시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 20.00 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;취약점 폭주와 과잉 보안 대책이 오히려 오픈소스 의존성 생태계를 부수고 있다&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Gentoo 메인테이너 Michał Górny — 끝없이 불어나는 의존성 트리와 패치 압박이 만들어낸 현대 패키지 보안의 역설</span>
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
            <h3 class="minor-detail-headline">CVE 폭주 시대, 상류(Upstream) 패치의 선의가 하류(Downstream) 유지보수자에게 새로운 취약점으로 전가되는 구조 고발</h3>
            <div class="minor-detail-subheadline">blogs.gentoo.org · Michał Górny 에세이 · HN 224점 · 132댓글 공감</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Gentoo 리눅스의 베테랑 패키지 메인테이너 Michał Górny가 몇 년 전 작성한 '현대 패키저의 보안 악몽'에 이어 후속 진단 글을 발표했습니다. 전례 없는 속도로 쏟아지는 CVE 보고와 거대한 의존성 트리 속에서, 한 개인 메인테이너가 감당할 수 있는 한계를 넘은 급조된 패치와 복잡성 증가가 오히려 시스템을 더 취약하게 만들고 있다는 현장 증언이 개발자들의 공감을 샀습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[보안 피로 악순환]</strong> Surging CVE Reports &rarr; Overloaded Maintainers &rarr; Rushed Upstream Fixes &rarr; Brittle Dependency Trees
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  단순 취약점 스캐너 도입을 넘어 최소 의존성 원칙과 장기 유지보수 지속 가능성을 재고해야 한다는 오픈소스 공급망 보안의 본질적 화두를 던집니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://blogs.gentoo.org/mgorny/2026/10/27/the-next-circle-of-security-hell/" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 에세이 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50610334" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (132댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: Win4wine -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 200점 · 104댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.3시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 19.41 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;리눅스 데스크톱의 창 관리자와 작업표시줄을 진짜 Windows XP explorer.exe로 바꿨다&quot; : Win4wine</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">mikuta0407/win4wine — 패치된 Wine 11.0 위에서 Windows XP/ReactOS 쉘을 리눅스 기본 데스크톱으로 구동 (LGPL-2.1, ★287)</span>
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
            <h3 class="minor-detail-headline">리눅스 앱과 윈도우 앱이 진짜 Windows XP 시작 메뉴·작업표시줄 위에서 나란히 실행되는 Debian 13 + Wine 11.0 실험</h3>
            <div class="minor-detail-subheadline">LGPL-2.1 라이선스 · Python + Wine 11.0 패치 · XP/Win7 사용자 ISO 추출 또는 ReactOS 오픈소스 쉘 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  단순히 Linux 데스크톱 테마를 Windows XP처럼 꾸미는 것을 넘어, <code>Win4wine</code>은 패치된 Wine 11.0 위에서 사용자 소유의 Windows XP <code>explorer.exe</code>(또는 자유 소프트웨어 ReactOS 쉘)를 리눅스 데스크톱 쉘 자체로 띄웁니다. 덕분에 리눅스 네이티브 앱의 창 테두리와 작업표시줄 버튼까지 XP의 진짜 쉘이 관리하는 기묘하면서도 완벽한 호환성 데모를 선보여 HN 200점을 획득했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[데스크톱 쉘 역전]</strong> Debian 13 Linux Apps &harr; Patched Wine 11.0 Window Bridge &harr; Windows XP explorer.exe / ReactOS Shell
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  메인 기사 <code>xnulinux</code>가 리눅스 안에 macOS 커널을 꽂았다면, <code>Win4wine</code>은 유저스페이스 쉘 수준에서 Windows와 Linux의 경계를 허문 또 하나의 재치 있는 OS 크로스오버입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/mikuta0407/win4wine" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
              <a href="https://news.ycombinator.com/item?id=50610743" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (104댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: Spelunkr.tv -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 907점 · 159댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 21.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 42.10 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;인터넷 아카이브 속 잊혀진 영상들로 짠 무료 대안 케이블 TV 네트워크&quot; : Spelunkr.tv</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">spelunkr.tv — 공공 도메인·보존 영상들을 80년대 케이블 TV 편성표 감성으로 채널 돌리듯 감상하는 웹 방송국</span>
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
            <h3 class="minor-detail-headline">알고리즘 추천 피드 대신 인터넷 아카이브의 희귀 영상을 기묘한 케이블 TV 채널로 편성한 대안 미디어 실험</h3>
            <div class="minor-detail-subheadline">spelunkr.tv · Internet Archive 아카이브 큐레이션 · 레트로 80s 모드 &amp; 모던 모드 UI</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  자극적인 숏폼과 AI 생성 슬롭이 유튜브 추천 피드를 뒤덮는 가운데, <code>Spelunkr.tv</code>는 인터넷 아카이브(Internet Archive)에 잠들어 있던 오래된 교육 영상·공공 방송·실험 영화들을 여러 실시간 채널로 엮어 틀어줍니다. 80년대 케이블 TV 감성의 UI와 모던 모드를 오가며 채널을 돌리는 우연한 발견의 즐거움이 HN 907점을 끌어올렸습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[레트로 큐레이션]</strong> Internet Archive Forgotten Vault &rarr; Scheduled Thematic Channels &rarr; Zero-Algorithm Lean-Back TV
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  인류 디지털 문화유산 아카이브와 '기대어 시청하는(Lean-back)' 텔레비전 UX의 결합이 포스트 알고리즘 시대의 대안 소비 경험으로 각광받고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://spelunkr.tv" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> Spelunkr.tv 시청하기
              </a>
              <a href="https://news.ycombinator.com/item?id=50606192" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (159댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: Beginner's Guide to Local AI with Inkling, Qwen, and Unsloth -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 736점 · 295댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.8시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 28.58 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;우리 집 PC에 개인용 ChatGPT 세우기: Inkling·Qwen·Unsloth 로컬 AI 입문 완전판&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">gpupartner.com — 클라우드 모델의 품질 저하·검열·구독료에서 벗어나 온가족이 쓰는 로컬 LLM 구축 가이드</span>
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
            <h3 class="minor-detail-headline">오픈웨이트 모델의 성숙과 Unsloth 양자화가 일반 가정용 PC를 프라이빗 AI 서버로 바꾸는 실전 로드맵</h3>
            <div class="minor-detail-subheadline">GPU Partner 기술 블로그 · Inkling + Qwen + Unsloth 스택 · HN 736점 · 295댓글</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  클라우드 AI 서비스들의 예고 없는 모델 품질 변동, 엄격한 출력 통제, 치솟는 API 비용에 지친 사용자들이 오픈웨이트 진영으로 대거 이동하고 있습니다. 저자 Jerry James는 Inkling·Qwen 오픈웨이트 모델과 Unsloth 최적화 스택을 결합해 프라이버시가 보장되면서 온 가족이 공유할 수 있는 무료 개인용 AI 서버를 PC에 세우는 전 과정을 초보자 눈높이에서 풀어내 HN 736점을 기록했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[홈 AI 스택]</strong> Consumer GPU PC &rarr; Unsloth Quantized Inkling / Qwen &rarr; Private LAN ChatGPT Replacement
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  전문 연구자 영역이던 로컬 추론·양자화 기술이 가정용 홈랩과 일상 생산성 도구로 완전히 대중화되었음을 보여주는 지표입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 가이드 원문 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50603845" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (295댓글)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: The Birds of GTA 6 -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 628점 · 362댓글</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.6시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 22.76 점/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;전미 오듀본 조류 협회가 해부한 GTA 6 바이스 시티·레오니다의 야생 조류 생태학&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Audubon Magazine — 조류학자들의 시선으로 검증한 차세대 오픈월드 생태계 모델링과 종 고증의 놀라운 디테일</span>
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
            <h3 class="minor-detail-headline">비디오 게임 속 가상 습지와 해변을 실제 플로리다 조류 도감으로 판독한 Audubon 매거진의 이색 필드 가이드</h3>
            <div class="minor-detail-subheadline">Audubon Magazine 특집 · HN 628점 · 362댓글 · 절차적 생태계·그래픽스 고증 화제</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  전미 오듀본 협회(National Audubon Society) 매거진이 GTA 6의 배경인 가상의 플로리다(레오니다) 트레일러와 화면 속 새들을 실제 조류학자 시선으로 판별해 낸 필드 가이드를 공개했습니다. 에버글레이즈 습지와 해변을 스쳐 지나가는 펠리컨·백로·플라밍고 등의 비행 자세와 서식지 분포가 실제 생태학적 특징과 놀라울 만큼 부합한다는 분석이 362개 댓글의 열띤 토론을 이끌어냈습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[생태계 시뮬레이션]</strong> Real Florida Ornithology &rarr; AAA World-Building &amp; Wing Biomechanics &rarr; Biologist Field Verification
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  현대 그래픽스 및 게임 월드 빌딩이 단순 배경 장식을 넘어 생물학 전문가가 종(Species)을 동정할 수 있을 만큼 정밀한 자연 생태 시뮬레이션으로 진입했음을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.audubon.org/magazine/birds-of-gta-6-field-guide-vice-city-wildlife" target="_blank" rel="noopener noreferrer" class="minor-link ext">
                <i data-lucide="external-link" class="minor-icon"></i> 오듀본 필드 가이드 보기
              </a>
              <a href="https://news.ycombinator.com/item?id=50602843" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (362댓글)
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
