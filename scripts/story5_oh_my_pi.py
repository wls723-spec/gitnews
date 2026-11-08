# -*- coding: utf-8 -*-
# Story 5: can1357/oh-my-pi (Pi Open-Source Coding Agent & IDE Harness)

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 5] can1357/oh-my-pi : IDE가 결합된 자립형 코딩 하네스 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_oh_my_pi.jpg" alt="oh-my-pi coding agent with IDE wired in" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> HN 662 PTS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 앤스로픽 종속을 벗어난 오픈 하네스 대이동</span>
              <span class="platform-tag">Hacker News & GitHub</span>
              <span class="platform-tag">can1357 / oh-my-pi (omp.sh)</span>
            </div>
            
            <h2 class="article-headline">
              "안녕 클로드, 반가워 파이" — 60개 모델과 LSP·DAP 디버거를 품은 8만 줄 Rust 코어 오픈 하네스 'oh-my-pi'
            </h2>

            <div class="article-subheadline">
              Claude Code의 폐쇄적 생태계와 잦은 정책 변경에 지친 개발자들의 집단 탈출… 31개 빌트인 도구, 14개 언어 서버(LSP) 연산, 완전한 무제한 BYOK 자율성
            </div>
            <p class="article-snippet">
              해커뉴스에서 660점 이상의 압도적 추천을 받으며 화제를 모은 "Goodbye Claude, hello Pi" 에세이와 함께, 오픈소스 코딩 에이전트 하네스 'oh-my-pi(omp.sh)'가 전 세계 개발자 생태계의 태풍의 눈으로 떠올랐습니다. 특정 빅테크 API에 갇히지 않고 IDE 심층 제어력을 회복하려는 오픈 하네스 혁명을 분석합니다.
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
              <i data-lucide="flame"></i> 1. 리드: "더 이상 빅테크의 기분에 휘둘릴 수 없다"
            </h3>
            <p>
              1년 전 Claude Code가 처음 등장했을 때, 개발자들은 마법을 목격한 듯 환호했다. 
              하지만 시간이 흐르며 구독 요금제 인상, 모호한 검열 필터링, 그리고 앤스로픽 서버가 먹통이 될 때마다 
              작업이 완전히 마비되는 '단일 실패 지점(Single Point of Failure)'의 고통이 쌓여갔다. 
              최근 골드만삭스를 비롯한 주요 기업들이 보안 우려로 Claude Code 사용을 전격 중단하고, 
              개발자 개인들 사이에서도 "빅테크의 독점 정원(Walled Garden)을 탈출하겠다"는 목소리가 거세졌다.
            </p>
            <p>
              이 분노와 열망이 마침내 임계점을 넘었다. 
              마리오 제크너(@mariozechner)의 오리지널 Pi 코어와 스텐실 랩스(Stencil Labs)가 완성한 
              <strong>can1357/oh-my-pi (omp.sh)</strong>는 출시 직후 해커뉴스 1위에 오르며 
              "진정으로 자유롭고, IDE 깊숙이 연결된 오픈소스 코딩 에이전트"의 표준으로 등극했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 8만 줄의 순수 Rust 코어가 증명한 압도적 속도
            </h3>
            <p>
              oh-my-pi는 단순한 프롬프트 래퍼가 아니다. 
              바닥부터 작성된 <strong>약 8만 줄(80k lines)의 순수 Rust 네이티브 코어 엔진과 초고속 Bun 런타임</strong>으로 구동되며, 
              단 1초 만에 초기화되어 터미널과 에디터에 밀착한다. 
              OpenAI, Anthropic, Gemini, DeepSeek, 로컬 Ollama를 아우르는 <strong>60개 이상의 LLM 공급자(Provider)</strong>를 지원하며, 
              자신이 가진 API 키나 로컬 가속기 모델을 마음대로 교체할 수 있다(BYOK).
            </p>

            <div class="editorial-quote">
              <p>
                "우리는 단일 기업의 API에 종속된 멍청한 터미널 봇을 원치 않는다. 
                <strong>oh-my-pi는 14개의 LSP 언어 서버 연산과 28개의 DAP 디버거 프로토콜을 에이전트의 손발로 직접 쥐여준 최초의 자율 하네스</strong>다. 
                에이전트가 코드의 타입 에러를 컴파일러보다 먼저 보고 스스로 중단점을 걸어 디버깅한다."
              </p>
              <small>— 'Goodbye Claude, hello Pi' 기술 분석 스레드 중</small>
            </div>

            <p>
              31개의 강력한 빌트인 도구가 기본 탑재되어 있어, 별도의 복잡한 MCP 서버 설정 없이도 
              파일 탐색, 시맨틱 검색, 서브셸 제어, 테스트 코드 실행을 물 흐르듯 수행한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: 언어 서버(LSP)와 디버그 어댑터(DAP)의 네이티브 결합
            </h3>
            <p>
              기존 코딩 에이전트들이 텍스트 파일 전체를 통째로 읽고 쓰며 토큰을 낭비할 때, 
              oh-my-pi는 진짜 인간 시니어 개발자처럼 IDE의 내부 프로토콜을 직접 두드린다:
            </p>
            <ul>
              <li><strong>14대 LSP 네이티브 조작:</strong> 파일 전체를 다시 읽지 않고도 Language Server Protocol을 통해 `Go to Definition`, `Find References`, `Hover Diagnostics`를 밀리초 단위로 쿼리. 토큰 낭비를 80% 줄이면서도 정확한 심볼 식별.</li>
              <li><strong>28대 DAP 디버깅 하네스:</strong> 실행 중인 프로그램에 브레이크포인트를 걸고, 변수 스택 프레임을 추적하며 런타임 에러의 근본 원인을 역추적(Step-in / Step-over).</li>
              <li><strong>Rust 네이티브 바이너리 배포:</strong> 번거로운 Node.js 의존성이나 전역 환경 오염 없이, `curl -fsSL https://omp.sh/install | sh` 한 줄로 맥과 리눅스 환경에 독립 바이너리로 즉시 안착.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="code" style="color:#0ea5e9;"></i> oh-my-pi 80k Rust 코어 및 IDE 결합 파이프라인
                </span>
                <span class="schematic-badge">RUST CORE IDE AGENT HARNESS</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">LAYER 1</div>
                  <div class="step-label">60+ LLM 백엔드 교체</div>
                  <div class="step-tech">BYOK (Anthropic, OpenAI, DeepSeek, Local)</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">LAYER 2</div>
                  <div class="step-label">80k Rust Core Runtime</div>
                  <div class="step-tech">31 Built-in Tools + Subshell Management</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">LAYER 3</div>
                  <div class="step-label">LSP & DAP 네이티브 통신</div>
                  <div class="step-tech">14 LSP Ops + 28 DAP Breakpoint Debugging</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 원리:</strong> 특정 클라우드 벤더의 통제된 가상머신에 갇히지 않고, 사용자의 로컬 IDE 내부 LSP 및 디버그 프로토콜을 80k Rust 코어로 직접 제어하여 토큰 비용과 개발 속도를 동시에 혁신합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-check"></i> 4. 비즈니스 해자 및 개발자 주권: 벤더 종속(Lock-in)의 종말
            </h3>
            <p>
              oh-my-pi의 폭발적 성장은 AI 시장에서 벤더 종속(Vendor Lock-in)의 시대가 저물고 있음을 시사한다. 
              월 20달러 구독료를 내고도 쿼터 제한에 걸려 작업이 중단되던 개발자들은 
              이제 더 저렴하고 빠른 DeepSeek나 로컬 가속기 모델로 단 1초 만에 스위칭할 수 있는 통제권을 되찾았다.
            </p>
            <p>
              사내 코드가 빅테크의 서버로 전송되는 것을 엄격히 금지하는 대기업 엔터프라이즈 환경에서도, 
              oh-my-pi는 100% 오픈소스 검증이 가능한 투명한 아키텍처를 앞세워 표준 코딩 하네스로 급부상하고 있다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="terminal" style="color:#10b981;"></i> oh-my-pi 공식 터미널 하네스 및 배포 인터페이스
                </span>
                <span class="media-showcase-badge demo">OMP.SH OFFICIAL PREVIEW</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_oh_my_pi.png" alt="oh-my-pi official portal and terminal interface" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 공식 웹 포털:</strong> 60개 이상의 LLM 공급자와 IDE 디버깅 프로토콜을 결합한 oh-my-pi(omp.sh)의 공식 배포 사이트 인터페이스.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="zap"></i> 5. 키커: 개발자의 주권은 오픈소스에서 나온다
            </h3>
            <p>
              "우리가 도구를 만들고, 그 후에는 도구가 우리를 만든다." 
              빅테크의 독점적 울타리에 갇혀 수동적으로 도구를 소비하던 시대는 끝났다. 
              oh-my-pi는 가장 날카롭고 투명한 오픈소스 하네스를 쥐고 자신의 코딩 주권을 지키려는 모든 엔지니어들의 든든한 날개가 되어줄 것이다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://omp.sh" target="_blank" class="project-link demo">
                  <i data-lucide="globe" style="width:16px;height:16px;"></i> 공식 웹사이트 방문
                </a>
                <a href="https://github.com/can1357/oh-my-pi" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
