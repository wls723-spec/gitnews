# -*- coding: utf-8 -*-
# Story 4: earendil-works/pi

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] earendil-works/pi                                -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_pi.jpg" alt="Pi Minimal Extensible Agent Harness Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="cpu" style="width:12px;height:12px;fill:#fff;"></i> COMPOSABLE HARNESS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#fef3c7; border-color:#d97706; color:#92400e;">🧩 12만 3천 스타 · OpenClaw·PiBot의 심장이 된 초미니멀 에이전트 커널</span>
              <span class="platform-tag">GitHub Trending &amp; pi.dev</span>
              <span class="platform-tag">earendil-works / pi</span>
            </div>

            <h2 class="article-headline">
              "당신을 도구에 맞추지 마라, 하네스를 당신의 워크플로에 맞춰 조립하라" — 12개 모듈형 패키지로 차세대 에이전트 생태계의 기반이 된 'Pi'
            </h2>

            <div class="article-subheadline">
              고정된 플랜 모드·서브에이전트를 비우는 대신 extensions·skills·themes·Pi packages로 자기 확장하는 코딩 하네스, 대화형 TUI·JSON/Print CLI·RPC·TypeScript SDK·Durable 실행·벤더 중립 Telemetry 통합 (+163스타/일, 누적 123,337스타, MIT)
            </div>
            <p class="article-snippet">
              요즘 공개되는 수많은 AI 에이전트 프로젝트의 설계도를 들여다보면 심심치 않게 등장하는 이름이 있습니다. 바로 <strong>earendil-works/pi</strong>입니다. 오늘 하루에만 <strong>163개의 스타(누적 123,337스타, 포크 15,913개)</strong>를 보태며 꾸준히 확산 중인 Pi는 무거운 내장 기능을 과감히 덜어낸 최소주의 에이전트 하네스입니다. 개발자가 자신에게 맞는 서브에이전트나 플랜 워크플로를 확장(Extension)과 스킬, RPC, TypeScript SDK로 직접 조립하도록 설계돼, <code>OpenClaw</code> 같은 거대 에이전트 플랫폼의 핵심 런타임으로도 채택됐습니다.
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
              <i data-lucide="flame"></i> 1. 리드: "플랜 모드도, 기본 서브에이전트도 일부러 뺐습니다"
            </h3>
            <p>
              대부분의 AI 코딩 도구는 릴리스 노트에 얼마나 많은 내장 기능을 욱여넣었는지 자랑하기 바쁘다. "자동 플랜 모드 탑재, 기본 5종 서브에이전트 내장, 고정된 UI 레이아웃 제공." 하지만 <strong>earendil-works/pi</strong>의 README 첫머리는 정반대의 선언으로 시작한다. <em>"Pi는 강력한 기본값을 제공하지만, 서브에이전트와 플랜 모드 같은 기능은 일부러 건너뜁니다. 당신이 원하는 것을 Pi에게 직접 만들라고 시키거나, 당신 방식대로 동작하는 패키지를 설치하세요."</em>
            </p>
            <p>
              이 도발적인 절제미는 역설적으로 폭발적인 생태계 팽창을 불러왔다. 누적 <strong>123,337스타와 15,913포크</strong>를 돌파한 Pi는 이제 혼자 쓰는 CLI를 넘어, <code>OpenClaw</code> 같은 대형 에이전트 프로젝트와 각종 데스크톱·모바일 봇 런타임이 밑바닥 엔진으로 가져다 쓰는 '에이전트계의 리눅스 커널' 같은 위상을 다지고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "블랙박스 비서가 아니라, 프로그래머블한 객체·에이전트 런타임"
            </h3>
            <p>
              엔지니어들이 기존의 올인원 코딩 툴에서 가장 답답해하는 지점은 '자동화 확장성'이다. CLI 창을 띄워놓고 사람이 채팅해야만 작동하는 도구는 CI 파이프라인이나 백그라운드 데몬, 사내 협업 플랫폼에 심기 어렵다. Pi는 처음부터 에이전트를 하나의 <strong>소프트웨어 컴포넌트</strong>로 취급했다.
            </p>

            <div class="editorial-quote">
              <p>
                "Pi를 워크플로에 맞춰라, 그 반대가 아니라. <strong>대화형으로 쓰든, Print/JSON 모드로 자동화하든, RPC로 원격 제어하든, TypeScript SDK로 앱을 짓든 모두 같은 코어 위에서 돌아간다.</strong>"
              </p>
              <small>— earendil-works/pi 공식 설계 선언 (MIT License)</small>
            </div>

            <p>
              실제로 Pi의 모노레포에는 단순 코딩 에이전트(<code>coding-agent</code>)뿐만 아니라 프로세스 간 객체 런타임(<code>@earendil-works/chord</code>), 벤더 중립 텔레메트리 규약(<code>@earendil-works/pi-telemetry</code>), 영속 실행(<code>durable</code>), 코드 모드(<code>codemode</code>), 평가 스위트(<code>evals</code>)까지 프로덕션 에이전트 제품 하나를 통째로 세울 수 있는 레고 블록이 들어있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 4중 실행 인터페이스 &amp; 12개 코어 패키지 모듈 해부
            </h3>
            <p>
              <code>@earendil-works/pi-coding-agent</code>(Node.js 22.19+ 및 Nix Flake 오프라인 빌드 완벽 지원)의 내부는 다음과 같은 모듈형 계층으로 나뉜다:
            </p>
            <ul>
              <li><strong>4가지 일관된 제어 인터페이스(TUI · JSON/Print · RPC · TS SDK):</strong> 사람과 마주 앉을 때는 <code>tui</code> 대화형 모드로, 셸 파이프라인에서는 Print/JSON 스트리밍 모드로, 다른 언어 프로세스(Python/Rust/Swift)에서 띄울 때는 <code>RPC</code> 프로토콜로, 웹/데스크톱 앱 내부에 녹일 때는 <code>TypeScript SDK</code>로 동일한 에이전트 루프를 호출한다.</li>
              <li><strong>Pi Packages &amp; <code>@earendil-works/chord</code> 객체 런타임:</strong> 확장(extensions), 스킬(skills), 프롬프트 템플릿, 테마를 하나의 'Pi 패키지'로 묶어 npm이나 git으로 즉시 공유한다. 여기에 포함된 <code>chord</code> 패키지는 HTTP, 워커, 웹·터미널 클라이언트 간 핫 리로드 플러그인과 문서 스토어를 연결하는 프로세스 간 객체 런타임 역할을 수행한다.</li>
              <li><strong>보안 핀닝 설치 &amp; Nix 재현성(<code>nix/model-catalog.json</code>):</strong> <code>curl -fsSL https://pi.dev/install.sh | sh</code> 인스톨러는 모든 전이 의존성(Transitive dependencies)을 엄격히 고정(Pinning)해 공급망 공격 위험을 줄이며, <code>npm install -g --ignore-scripts</code> 실행 시에도 라이프사이클 스크립트 없이 깔끔하게 구동된다. Nix 빌드 역시 오프라인 모델 카탈로그 핀을 내장해 어떤 CI 환경에서도 동일한 바이너리를 재현한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Pi 최소주의 모듈형 에이전트 하네스 &amp; 12대 패키지 아키텍처</span>
                <span class="schematic-badge">TypeScript + Nix · MIT · 123.3k★ · RPC &amp; SDK Ready</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Four Control Surfaces</div>
                  <div class="schematic-desc">
                    대화형 터미널(<code>tui</code>) &amp; <code>/login</code> 인증<br>
                    무인 자동화 Print / JSON 스트림 모드<br>
                    타 언어 브리지용 <strong>RPC</strong> 인터페이스<br>
                    앱 임베딩용 <strong>Pi TypeScript SDK</strong>
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Minimal Composable Core</div>
                  <div class="schematic-desc">
                    <code>agent</code> + <code>ai</code> + <code>mcp</code> + <code>codemode</code><br>
                    <code>durable</code>(장기 실행) &amp; <code>evals</code>(검증)<br>
                    Extensions·Skills·Templates 핫 조립<br>
                    Pi Packages (npm / git 즉시 공유)
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Runtime &amp; Supply Chain</div>
                  <div class="schematic-desc">
                    <code>@earendil-works/chord</code> 분산 객체 런타임<br>
                    <code>pi-telemetry</code> 벤더 중립 계측 스키마<br>
                    의존성 핀닝 인스톨러(<code>--ignore-scripts</code>)<br>
                    오프라인 <strong>Nix</strong> 재현성 빌드(ARM64/x64)
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">pi.dev 공식 플랫폼 실화면 — 최소주의 코어와 확장 패키지 기반 에이전트 하네스</span>
              </div>
              <img src="../assets/images/demo_pi.png" alt="Pi Agent Harness Official Platform Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ pi.dev 실화면: 12만 3천 스타를 기록한 Pi의 공식 포털 및 OpenClaw 연동, 의존성 핀닝 인스톨러, 12개 코어 패키지 문서 생태계.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 생태계 역학: "기능이 많은 도구"보다 "부품으로 쓰기 좋은 하네스"가 이긴다
            </h3>
            <p>
              에이전트 시장이 초기 데모 경쟁을 지나 사내 시스템·하드웨어·로봇·메신저와 결합하는 임베디드 단계로 접어들자, 거대하고 의견이 강한(Opinionated) 모놀리식 IDE는 오히려 걸림돌이 되고 있다. 자신만의 승인 게이트, 커스텀 메모리 DB, 특수 도메인 도구를 심으려 할 때마다 기존 하네스의 하드코딩된 루프와 싸워야 하기 때문이다.
            </p>
            <ul>
              <li><strong>OpenClaw부터 커스텀 하네스까지의 토대:</strong> Pi는 "하네스 자체를 고쳐 쓰는 데 최적화된 최소 커널"을 지향함으로써 수많은 파생 에이전트들의 공통 분모가 됐다. 여기에 <code>--ignore-scripts</code> 무결성 지원과 Nix 오프라인 빌드는 기업 보안팀이 오픈소스 에이전트를 사내망에 들이는 허들을 극적으로 낮춘다.</li>
              <li><strong>신규 기여자 보호와 거버넌스:</strong> 흥미로운 운영 방식도 눈에 띈다. 폭발적인 인기로 인한 AI 스팸 PR·이슈 폭주를 막기 위해 신규 기여자의 이슈/PR을 기본 자동 닫기(Auto-close) 처리한 뒤 메인테이너가 매일 선별 검토하는 방어 체계를 도입하며 품질을 지키고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 위대한 유닉스 철학이 AI 에이전트의 몸을 빌려 돌아왔다
            </h3>
            <p>
              "한 가지 일을 잘하는 작은 도구를 만들고, 파이프와 프로토콜로 조합하라." 50년 된 유닉스 철학이 가장 잘 통하는 영역이 바로 오늘날의 AI 코딩 에이전트다.
            </p>
            <p>
              모든 기능을 다 넣으려다 비대해지는 수많은 경쟁작 사이에서, 가장 중요한 것만 남기고 나머지를 확장 규약으로 열어둔 <code>Pi</code>는 묻고 있다. 당신의 에이전트는 남이 짜준 궤도를 돌고 있는가, 아니면 당신의 워크플로에 맞춰 스스로 진화하고 있는가?
            </p>

            <div class="project-links">
              <a href="https://pi.dev" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> Pi 공식 사이트
              </a>
              <a href="https://www.youtube.com/results?search_query=earendil+works+pi+coding+agent+OpenClaw" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/earendil-works/pi" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
