# -*- coding: utf-8 -*-
# Story 2: herdrdev/herdr (Rust AI Agent Runtime & Terminal Multiplexer)

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 2] herdrdev/herdr : 자율 코딩 에이전트의 런타임 OS -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_herdr.jpg" alt="herdr coding agent runtime" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> RUST #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 코딩 에이전트들의 tmux를 넘어선 전용 런타임</span>
              <span class="platform-tag">GitHub Trending</span>
              <span class="platform-tag">herdrdev / herdr</span>
            </div>
            
            <h2 class="article-headline">
              코딩 에이전트들의 멀티플렉서 OS — 세션이 끊겨도 멈추지 않는 단일 Rust 바이너리 런타임 'herdr'
            </h2>

            <div class="article-subheadline">
              노트북을 닫아도 백그라운드 서버에서 에이전트는 계속 코딩 중… 다중 SSH 서버 창 통합, '진행/대기/차단' 패널 상태 판별, 에이전트 간 소켓 통신 API까지 탑재
            </div>
            <p class="article-snippet">
              터미널 창을 닫거나 SSH 연결이 끊어지는 순간 수십 분간 작업하던 AI 에이전트 세션이 증발해 버리는 고질적인 문제를 해결한 혁신적인 에이전트 전용 런타임 'herdr'가 일간 4만 9천 스타를 모으며 글로벌 1위에 올랐습니다. Claude Code, Pi, Codex, Cursor를 단일 터미널에서 군단처럼 지휘하는 Rust 아키텍처를 분석합니다.
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
              <i data-lucide="flame"></i> 1. 리드: "터미널을 닫았더니 에이전트가 죽어버렸다"
            </h3>
            <p>
              2026년 가을, 소프트웨어 개발자들의 일상은 AI 코딩 에이전트(Claude Code, Codex, Pi, Opencode 등)에 수십 개의 작업을 병렬로 맡겨두고 자리를 비우는 패턴으로 완전히 재편되었다. 
              하지만 개발자들이 매일 마주하는 가장 치명적인 좌절은 터미널의 취약함이었다. 
              퇴근길에 노트북을 닫거나, 카페 와이파이가 불안정해 SSH 파이프가 끊어지는 순간, 
              백그라운드에서 빌드와 테스트를 수행하던 에이전트 프로세스가 모조리 킬(Kill) 신호를 받고 사망하는 사태가 반복된 것이다.
            </p>
            <p>
              기존의 tmux나 screen은 인간을 위해 설계된 도구였기에, 
              에이전트가 어떤 상태인지(코드를 컴파일 중인지, 사용자의 확인 질문에 막혀 대기 중인지)를 전혀 구분하지 못했다. 
              오늘 전 세계 개발자 커뮤니티의 폭발적인 갈채를 받은 <strong>herdrdev/herdr</strong>는 바로 이 지점에서 탄생한 <strong>'AI 코딩 에이전트 전용 차세대 런타임 OS'</strong>다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 에이전트를 감싸지 않고 터미널을 소유하다
            </h3>
            <p>
              herdr의 철학은 명료하다: <strong>"에이전트를 래핑(Wrap)하거나 개조하지 마라. 그들이 살아 숨 쉬는 터미널을 소유(Own)하라."</strong> 
              Electron이나 무거운 웹 기술을 일체 배제하고 단 하나의 초고속 Rust 네이티브 바이너리로 구동되는 herdr는, 
              기존에 쓰던 모든 에이전트 CLI를 그대로 실행하면서도 완벽한 탈착(Detach)과 재연결(Attach) 내구성을 제공한다.
            </p>

            <div class="editorial-quote">
              <p>
                "우리는 하루에도 수십 번씩 여러 대의 리모트 서버와 로컬 환경을 오가며 코딩 에이전트를 굴린다. 
                <strong>herdr는 어떤 에이전트가 인간의 응답을 기다리며 멈춰있는지(Blocked), 어떤 에이전트가 순조롭게 작업 중인지(Working) 한눈에 알려주는 최초의 에이전트 관제탑</strong>이다."
              </p>
              <small>— herdr 오픈소스 엔지니어링 블로그</small>
            </div>

            <p>
              개발자는 `ctrl+b q` 한 번으로 가볍게 세션을 분리하고 퇴근할 수 있으며, 
              집에 도착해 노트북을 열고 `herdr`를 입력하는 즉시 수십 개 에이전트의 터미널 창과 분할 레이아웃이 100% 동일하게 복원된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: 에이전트 네이티브 소켓 API와 지능형 상태 머신
            </h3>
            <p>
              herdr가 단순한 터미널 멀티플렉서를 뛰어넘는 이유는 에이전트와 양방향으로 대화하는 시스템 아키텍처에 있다:
            </p>
            <ul>
              <li><strong>소켓 기반 Agent-to-Agent 소통 버스:</strong> herdr 내부에서 동작하는 에이전트는 CLI와 UNIX 소켓 API를 통해 다른 창의 에이전트를 직접 스폰(Spawn)하거나 메시지를 전달할 수 있다. 프론트엔드 에이전트가 백엔드 에이전트에게 API 스펙 완성을 요청하고 대기하는 진정한 분업이 터미널 레벨에서 구현된다.</li>
              <li><strong>휴리스틱 패널 상태 모니터링:</strong> 터미널 PTY 출력 스트림의 정지 패턴과 ANSI 프롬프트 시퀀스를 분석하여, 각 패널을 `Working`, `Blocked`, `Idle`의 3가지 상태로 실시간 판별. 인간의 확인 질문을 기다리는 패널에는 시각적 알림을 자동 발송한다.</li>
              <li><strong>크로스 머신 단일 윈도우 오케스트레이션:</strong> 로컬 터미널과 원격 클라우드 인스턴스(AWS, GCP, Hetzner)의 SSH 연결을 단일 herdr 윈도우 안에 결합하여, 네트워크 단절 시에도 각 노드의 에이전트가 독자적으로 백그라운드 작업을 완수하도록 보장한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="monitor" style="color:#0ea5e9;"></i> herdr 단일 Rust 바이너리 에이전트 런타임 아키텍처
                </span>
                <span class="schematic-badge">RUST AGENT MULTIPLEXER</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">CLI & GUI</div>
                  <div class="step-label">Unified TUI Client</div>
                  <div class="step-tech">Prefix Keys + Mouse Split & Drag</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">DAEMON</div>
                  <div class="step-label">herdr Background Server</div>
                  <div class="step-tech">State Machine (Working / Blocked / Idle)</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">AGENTS</div>
                  <div class="step-label">Isolated PTY Terminals</div>
                  <div class="step-tech">Claude Code, Pi, Codex + Socket IPC</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 원리:</strong> 클라이언트 창이 닫혀도 백그라운드 데몬 서버가 에이전트들의 PTY 세션을 지속 유지하며, 소켓 API를 통해 복수의 에이전트가 서로의 패널을 제어하고 협동 작업을 수행하도록 런타임을 제공합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-check"></i> 4. 비즈니스 해자 및 산업적 파장: 도구의 중심이 인간에서 에이전트로
            </h3>
            <p>
              herdr의 부상은 개발 인프라 시장에서 중요한 패러다임 전환을 상징한다. 
              지금까지의 IDE와 터미널(VS Code, iTerm2, WezTerm)은 오직 '인간 사용자의 키보드 타이핑'만을 위해 최적화되어 있었다. 
              그러나 herdr는 개발 도구의 1차 사용자가 인간뿐만 아니라 '스스로 터미널을 다루는 자율 AI 에이전트'로 바뀌었음을 직시하고 만든 도구다.
            </p>
            <p>
              무거운 웹 브라우저 기반 SaaS 에이전트 플랫폼 대신, 
              개발자의 기존 터미널 워크플로우에 무마찰(Zero-friction)로 녹아드는 오픈소스 Rust 바이너리라는 점에서 기업 보안 감사와 온프레미스 도입 장벽을 완전히 허물었다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="terminal" style="color:#10b981;"></i> herdr 공식 인터페이스 및 에이전트 멀티패널 분할
                </span>
                <span class="media-showcase-badge demo">HERDR OFFICIAL INTERFACE</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_herdr.png" alt="herdr agent runtime dashboard in action" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 공식 웹 인터페이스:</strong> 복수의 코딩 에이전트 세션을 분할 관리하고 원격 머신과 로컬 작업을 하나로 결합하는 herdr의 공식 TUI 작업 공간.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="zap"></i> 5. 키커: 자리를 비워도 멈추지 않는 개발의 시대
            </h3>
            <p>
              "우리는 코드를 직접 짜는 프로그래머에서, 밤새 멈추지 않고 작업하는 에이전트 팀을 조율하는 오케스트라 지휘자로 진화하고 있다." 
              herdr가 마련한 든든한 런타임 위에서, 개발자들은 마침내 터미널이 끊길까 전전긍긍하는 두려움 없이 진짜 비동기 자율 개발의 자유를 누리게 되었다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://herdr.dev" target="_blank" class="project-link demo">
                  <i data-lucide="globe" style="width:16px;height:16px;"></i> 공식 웹사이트 방문
                </a>
                <a href="https://github.com/herdrdev/herdr" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
