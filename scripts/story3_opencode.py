# -*- coding: utf-8 -*-
# Story 3: anomalyco/opencode

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] anomalyco/opencode                               -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_opencode.jpg" alt="OpenCode Open Source AI Coding Agent Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="terminal" style="width:12px;height:12px;fill:#fff;"></i> 228K★ AGENT ENGINE</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dcfce7; border-color:#16a34a; color:#166534;">⚡ 22만 8천 스타 돌파 · 클로드 코드·커서에 맞선 오픈소스 에이전트 1강</span>
              <span class="platform-tag">GitHub Trending &amp; opencode.ai</span>
              <span class="platform-tag">anomalyco / opencode</span>
            </div>

            <h2 class="article-headline">
              "특정 AI 기업에 내 터미널을 종속시키지 않는다" — 22만 8천 스타와 3만 포크로 오픈소스 코딩 에이전트의 제국을 세운 'OpenCode'
            </h2>

            <div class="article-subheadline">
              Tab 키로 전환하는 build/plan 이중 에이전트와 @general 서브에이전트, Rust CLI(cli-rs)·TUI·클라이언트-서버 데몬·데스크톱 베타(.dmg/.exe/.AppImage) 및 GUI 플러그인 생태계 통합 (+187스타/일, 누적 228,597스타, MIT)
            </div>
            <p class="article-snippet">
              코딩 에이전트가 개발자의 주력 작업 환경이 되면서, 주요 AI 연구소들은 각자의 비공개 CLI와 월 구독형 IDE 안에 개발자를 가두려 경쟁하고 있습니다. 누적 <strong>228,597개의 스타와 31,062개의 포크(금일 +187스타)</strong>를 기록하며 오픈소스 진영의 거대한 구심점이 된 <strong>anomalyco/opencode</strong>는 MIT 라이선스 아래 <code>build</code>·<code>plan</code> 모드 분리, 클라이언트-서버 세션 분리, Rust 기반 고속 CLI, 그리고 크로스플랫폼 데스크톱 앱까지 하나의 모노레포로 통합하며 '벤더 중립 코딩 하네스'의 표준을 세웠습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 6만 5천 번째 PR이 멈추지 않고 머지되는 오픈소스 군단
            </h3>
            <p>
              오늘 자정 무렵에도 <code>anomalyco/opencode</code> 저장소에는 65,500번대가 넘는 풀 리퀘스트(<code>#65525</code>, <code>#65624</code>)가 분 단위로 병합됐다. 22만 8천여 개의 스타와 3만 1천여 개의 포크라는 숫자는 단순한 인기 투표를 넘어, 전 세계 개발자들이 자발적으로 유지보수하는 거대한 에이전트 운영체제가 실제로 굴러가고 있음을 보여주는 지표다.
            </p>
            <p>
              초기 AI 코딩 도구는 특정 모델 회사가 제공하는 폐쇄형 바이너리를 그대로 쓰는 것 외에 선택지가 없었다. 프롬프트 템플릿을 뜯어보거나, 회사 내부 로컬 모델·다른 프로바이더로 즉시 전환하거나, 세션 상태를 로컬 SQLite와 데몬 서버로 분리해 원격 데스크톱과 연결하고 싶어도 소스가 닫혀 있었다. <strong>OpenCode</strong>는 바로 그 '블랙박스 하네스'를 MIT 오픈소스로 전면 개방하며 폭풍 성장했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "CLI에서 시작해 클라이언트-서버 에이전트 OS로 진화하다"
            </h3>
            <p>
              OpenCode가 v0.1 시절의 단순 터미널 래퍼를 벗어나 v1.19.x와 <code>opencode-v2</code> 세대로 넘어오며 주목받는 결정적 이유는 <strong>에이전트 실행 계층과 UI 계층의 완벽한 분리</strong>다. 터미널(TUI)에서 돌리던 작업을 그대로 데스크톱 앱이나 브라우저 세션 UI로 이어받고, 사내 프로세스 데몬으로 상주시킬 수 있다.
            </p>

            <div class="editorial-quote">
              <p>
                "OpenCode는 기본 전체 권한의 <strong>build</strong> 에이전트와 읽기 전용 분석·명령 승인을 강제하는 <strong>plan</strong> 에이전트를 Tab 한 번으로 오가며, 복잡한 탐색은 내부 <strong>@general</strong> 서브에이전트에 위임한다."
              </p>
              <small>— anomalyco/opencode 공식 에이전트 아키텍처 (MIT License)</small>
            </div>

            <p>
              실제 코드베이스 탐색이나 리팩터링 전에는 <code>plan</code> 모드로 파일 수정을 원천 차단하고 bash 실행 전 승인을 받다가, 설계가 확정되는 순간 <code>Tab</code> 키로 <code>build</code> 모드로 넘겨 구현을 밀어붙이는 워크플로는 프로덕션 개발자들 사이에서 가장 안전한 휴먼-인-더-루프(Human-in-the-loop) 패턴으로 정착했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Build/Plan/General 3단 에이전트와 30여 패키지 모노레포 해부
            </h3>
            <p>
              <code>anomalyco/opencode</code> 저장소의 <code>packages/</code> 디렉터리는 이 프로젝트가 단순 CLI가 아니라 풀스택 에이전트 플랫폼임을 증명한다:
            </p>
            <ul>
              <li><strong>이중 모드 + 서브에이전트 분리(<code>build</code> / <code>plan</code> / <code>@general</code>):</strong> 기본 <code>build</code> 에이전트는 전체 편집·실행 권한을 갖고, <code>plan</code> 에이전트는 파일 쓰기를 기본 거부하며 bash 명령마다 사용자 허가를 요구한다. 다단계 검색이나 광범위한 코드 파악이 필요할 때는 메시지에서 <code>@general</code> 서브에이전트를 호출해 메인 컨텍스트 오염을 막는다.</li>
              <li><strong>클라이언트-서버 분리 &amp; 상태 영속화(<code>server</code>·<code>sdk</code>·<code>effect-drizzle-sqlite</code>):</strong> 에이전트 코어(<code>core</code>, <code>ai</code>, <code>codemode</code>)가 백그라운드 서버와 프로세스 데몬(<code>process-daemon</code>) 위에서 실행되고, 상태는 <code>effect-drizzle-sqlite</code> 계층에 영속화된다. 덕분에 TUI(<code>tui</code>)뿐만 아니라 macOS(arm64/x64 DMG)·Windows(exe)·Linux(.deb/.rpm/AppImage) 네이티브 데스크톱 앱(<code>desktop</code>)과 웹 세션 UI(<code>session-ui</code>)가 동일한 SDK·프로토콜(<code>sdk</code>, <code>protocol</code>)로 통신한다.</li>
              <li><strong>Rust CLI(<code>cli-rs</code>) &amp; 확장 플러그인(<code>plugin</code>·<code>gui-plugins</code>):</strong> 고성능 Rust CLI 엔트리포인트와 브라우저·GUI 플러그인 시스템, HTTP 리코더·시뮬레이션 하네스(<code>http-recorder</code>, <code>simulation</code>)까지 내장해 엔터프라이즈 환경의 재현성과 확장성을 동시에 확보했다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">OpenCode Build/Plan 에이전트 분리 &amp; 클라이언트-서버 데스크톱 아키텍처</span>
                <span class="schematic-badge">TypeScript + Rust(cli-rs) · MIT · 228.5k★ · TUI + Desktop Beta</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Multi-Surface Clients</div>
                  <div class="schematic-desc">
                    고속 터미널 UI (<code>tui</code> + <code>cli-rs</code>)<br>
                    네이티브 Desktop App (macOS·Win·Linux)<br>
                    웹 <code>session-ui</code> &amp; SDK 클라이언트<br>
                    <code>opencode.ai/v2/install</code> 원클릭 배포
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Agent Harness &amp; Modes</div>
                  <div class="schematic-desc">
                    <code>Tab</code> 전환: <strong>build</strong>(실행) ↔ <strong>plan</strong>(읽기전용)<br>
                    <code>@general</code> 서브에이전트 탐색 위임<br>
                    <code>codemode</code> &amp; <code>patchmark</code> 정밀 편집<br>
                    <code>plugin</code> / <code>gui-plugins</code> 도구 확장
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Daemon &amp; State Core</div>
                  <div class="schematic-desc">
                    <code>server</code> + <code>process-daemon</code> 상시 세션<br>
                    <code>effect-drizzle-sqlite</code> 로컬 상태 저장<br>
                    <code>http-recorder</code>·<code>simulation</code> 테스트 추적<br>
                    멀티 프로바이더·로컬 모델 자유 교체
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">opencode.ai 공식 플랫폼 실화면 — TUI·데스크톱 앱 통합 오픈소스 코딩 에이전트</span>
              </div>
              <img src="../assets/images/demo_opencode.png" alt="OpenCode Official Platform Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ opencode.ai 실화면: 22만 8천여 스타를 돌파한 오픈소스 코딩 에이전트 OpenCode의 공식 랜딩 인터페이스 및 v2 CLI·데스크톱 베타 배포 환경.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: '에이전트 하네스 락인'에 맞서는 개방형 클라이언트 전쟁
            </h3>
            <p>
              모델 자체의 지능 격차가 점차 좁혀지면서 빅테크 AI 기업들의 진짜 수익 해자는 '가장 똑똑한 모델'에서 <strong>'개발자가 매일 8시간을 머무르는 독점 에이전트 하네스'</strong>로 이동하고 있다. 독점 하네스를 쓰면 자사 모델만 기본 탑재되고 워크플로 데이터도 벤더 서버에 남는다.
            </p>
            <ul>
              <li><strong>모형과 하네스의 디커플링:</strong> OpenCode(MIT)는 하네스 계층을 완전히 무료·오픈소스로 풀어버림으로써 개발자가 오늘 작업은 Claude로, 내일 리팩터링은 GPT나 오픈웨이트 로컬 모델로 자유롭게 스위칭해도 단축키와 세션 기록, 플러그인 생태계를 그대로 유지하게 만든다.</li>
              <li><strong>데스크톱 앱 확장 승부수:</strong> 터미널에 익숙한 시니어 엔지니어뿐만 아니라 GUI를 선호하는 개발자층까지 <code>opencode-desktop</code> 베타로 끌어안으면서, Cursor 같은 유료 AI IDE의 가장 직접적인 오픈소스 대항마로 부상했다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 코딩 에이전트의 주인은 모델 공급사가 아니라 코드를 쓰는 개발자다
            </h3>
            <p>
              6만 5천 건을 넘어선 풀 리퀘스트와 3만여 개의 포크가 증명하듯, 개발 도구 역사상 가장 빠른 혁신은 언제나 개발자가 직접 자신의 도구를 뜯어고칠 수 있을 때 일어났다.
            </p>
            <p>
              모델이 상품화(Commoditization)되는 시대, 당신의 터미널과 데스크톱을 지키는 최후의 자유는 결국 '내가 교체할 수 있는 오픈소스 하네스'를 쥐고 있는가에 달려 있다.
            </p>

            <div class="project-links">
              <a href="https://opencode.ai" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> OpenCode 공식 사이트
              </a>
              <a href="https://www.youtube.com/results?search_query=OpenCode+open+source+AI+coding+agent" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/anomalyco/opencode" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
