# -*- coding: utf-8 -*-
# Story 3: cursor/plugins

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] cursor/plugins                                   -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_cursor_plugins.jpg" alt="Cursor Plugins Official Specification Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="puzzle" style="width:12px;height:12px;fill:#fff;"></i> AGENT ECOSYSTEM</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ede9fe; border-color:#7c3aed; color:#5b21b6;">🧩 AI IDE가 '앱스토어형 에이전트 OS'로 진화하는 표준 청사진</span>
              <span class="platform-tag">GitHub Trending #2 (Unseen) &amp; Cursor Official</span>
              <span class="platform-tag">cursor / plugins</span>
            </div>

            <h2 class="article-headline">
              "코드 에디터의 시대는 끝났다, 이제는 에이전트 플러그인 OS다" — 보안감사·병렬오케스트레이션·기억엔진을 표준화한 'Cursor Plugins'
            </h2>

            <div class="article-subheadline">
              독립 디렉터리 매니페스트(.cursor-plugin/plugin.json) 기반 공식 플러그인 규격 및 Thermos(심층 보안감사)·Orchestrate(클라우드 병렬 에이전트)·Continual Learning(AGENTS.md 메모리)·PR Review Canvas·Google Workspace 통합 공개 (+261스타/일, 누적 18,084스타)
            </div>
            <p class="article-snippet">
              불과 1년 전만 해도 AI 코딩 도구의 경쟁력은 "자동완성이 얼마나 똑똑한가"였지만, 이제 전쟁터는 "에이전트에게 어떤 워크플로우·기억·보안 규율·사내 도구를 꽂아줄 수 있는가"로 완전히 이동했습니다. 오늘 하루에만 261스타를 추가하며 누적 18,084스타를 넘어선 공식 저장소 <strong>cursor/plugins</strong>는 Cursor 팀과 엔지니어들이 실전에서 사용하는 고급 에이전트 오케스트레이션, 심층 브랜치 감사(<code>thermos</code>), 자동 학습 메모리(<code>continual-learning</code>), 사내 SaaS 연동을 표준 플러그인 규격으로 공개하며 차세대 개발자 마켓플레이스 패권 경쟁에 불을 붙였습니다.
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
              <i data-lucide="flame"></i> 1. 리드: <code>.cursor-plugin</code> 폴더 하나가 바꾸는 팀 전체의 엔지니어링 규율
            </h3>
            <p>
              과거의 IDE 확장 프로그램(VS Code Extension)은 문법 하이라이팅이나 린터 아이콘을 그려주는 수동적인 UI 부속품이었다. 그러나 <code>cursor/plugins</code> 저장소 루트에 나열된 디렉터리들의 면면은 전혀 다른 시대의 도래를 알린다. <code>thermos</code>(병렬 서브에이전트 기반 핵폭탄급 보안·품질 PR 감사), <code>orchestrate</code>(플래너·워커·검증자 분업을 통한 대규모 클라우드 에이전트 팬아웃), <code>continual-learning</code>(대화 로그에서 고신호 인사이트만 추려 <code>AGENTS.md</code>를 점진적으로 갱신), <code>pr-review-canvas</code>(중요도 순 리뷰 캔버스).
            </p>
            <p>
              오늘 하루에만 <strong>+261스타(누적 18,084스타, 2,000+ 포크)</strong>를 모은 이 저장소는 단순한 코드 모음집이 아니다. Cursor가 자체 내부 팀 워크플로우(<code>cursor-team-kit</code>)와 외부 SaaS 연동(Gmail·Google Drive·Calendar·Docs·Sheets·Slides·Ads·Sabre 등), 심지어 경쟁 도구인 <code>.claude-plugin</code> 호환 레이어까지 한데 묶어 <strong>AI 에이전트 시대의 표준 패키지 매니페스트</strong>를 제시한 공식 청사진이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 프롬프트 복붙의 종말과 '이식 가능한 에이전트 역량'의 탄생
            </h3>
            <p>
              지금까지 개발자들은 좋은 에이전트 작업 방식(예: "코드 작성 전 알고리즘 먼저 검증하고, Figma UI는 시각적 심판 에이전트로 검사하라")을 발견해도 블로그 글이나 사내 노션에 프롬프트 몇 줄을 적어 공유하는 원시적인 단계에 머물렀다. <code>cursor/plugins</code>는 이 암묵지를 스킬(Skills), 서브에이전트(Subagents), 훅(Hooks), MCP 커넥터, 전용 캔버스 UI를 포함한 <strong>하나의 버전 관리되는 독립 디렉터리</strong>로 패키징한다.
            </p>

            <div class="editorial-quote">
              <p>
                "각 플러그인은 저장소 루트에서 자체 <code>.cursor-plugin/plugin.json</code> 매니페스트를 갖는 독립 디렉터리다. <strong>단순한 도구가 아니라 팀의 리뷰 기준, 기억 갱신 루프, 병렬 클라우드 실행 규율까지 코드로 배포한다.</strong>"
              </p>
              <small>— cursor/plugins 공식 플러그인 사양 및 마켓플레이스 아키텍처</small>
            </div>

            <p>
              특히 주목할 점은 <code>agent-compatibility</code>와 <code>cli-for-agent</code> 같은 메타 플러그인들이다. 에이전트가 저장소를 스캔해 문서와 실제 구동 방식이 일치하는지 감사하고, 인간이 아니라 AI 에이전트가 실수 없이 실행할 수 있는 CLI 설계 원칙(<code>--dry-run</code>, 멱등성, 예시가 포함된 도움말)까지 플러그인 형태로 내장하고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: <code>plugin.json</code> 매니페스트와 멀티 에이전트 코어 플러그인 해부
            </h3>
            <p>
              <code>cursor/plugins</code> 생태계는 단일 매니페스트 규격 아래에서 개발 수명주기의 4대 핵심 영역을 모듈화했다:
            </p>
            <ul>
              <li><strong>자기 진화 메모리 &amp; 루프 (<code>continual-learning</code> · <code>ralph-loop</code> · <code>advisor</code>):</strong> 세션 트랜스크립트를 추적해 불필요한 잡음 없이 핵심 규칙만 <code>AGENTS.md</code>에 반영하며, 반복적 자기 참조 루프(Ralph Wiggum 기법)와 막히는 지점·완료 선언 직전 더 강력한 모델에게 자문을 구하는 <code>advisor</code> 훅을 통합한다.</li>
              <li><strong>병렬 감사 및 클라우드 오케스트레이션 (<code>thermos</code> · <code>orchestrate</code> · <code>pstack/dyl-stack</code>):</strong> <code>thermos</code>는 여러 서브에이전트를 병렬 투입해 보안 취약점과 코드 품질 루브릭을 가혹하게 채점한 뒤 머지 가능한 PR까지 생성하며, <code>orchestrate</code>는 대규모 작업을 플래너-워커-검증자 파이프라인으로 팬아웃한다.</li>
              <li><strong>인간-에이전트 캔버스 &amp; 플랫폼 확장 (<code>pr-review-canvas</code> · <code>docs-canvas</code> · <code>origin-apps</code> · <code>third_party</code>):</strong> 방대한 PR Diff를 중요도별 인터랙티브 캔버스로 시각화하고, Cursor Origin API 웹훅/OAuth 스펙과 Google Workspace MCP/플러그인을 즉시 연결한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Cursor Plugins 표준 매니페스트 및 4대 에이전트 워크플로우 레이어</span>
                <span class="schematic-badge">.cursor-plugin/plugin.json · Modular Subagents &amp; Skills · 2,000+ Forks</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Manifest &amp; Tooling</div>
                  <div class="schematic-desc">
                    독립 디렉터리 + <code>plugin.json</code> 규격<br>
                    <code>create-plugin</code> 스캐폴딩 &amp; 유효성 검증<br>
                    <code>cli-for-agent</code>(멱등성·dry-run 표준)<br>
                    <code>cursor-sdk</code> · <code>origin-apps</code> API
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Autonomous Orchestration</div>
                  <div class="schematic-desc">
                    <code>orchestrate</code>: 플래너·워커·검증자 팬아웃<br>
                    <code>thermos</code>: 병렬 보안·품질 하드코어 감사<br>
                    <code>continual-learning</code>: <code>AGENTS.md</code> 기억<br>
                    <code>advisor</code>: 핵심 의사결정 상위 모델 자문
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Canvas UI &amp; SaaS Bridge</div>
                  <div class="schematic-desc">
                    <code>pr-review-canvas</code> 중요도별 Diff 시각화<br>
                    <code>docs-canvas</code> 탐색형 문서 캔버스<br>
                    Google Workspace 7종 + Sabre 등 <code>third_party</code><br>
                    <code>.claude-plugin</code> 크로스 하네스 호환
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">cursor/plugins 공식 저장소 실화면 — 50명 기여자·508 브랜치·표준 플러그인 트리</span>
              </div>
              <img src="../assets/images/demo_cursor_plugins.png" alt="Cursor Plugins Official Repository Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/cursor/plugins 실화면: 루트에 배치된 <code>.cursor-plugin</code>, <code>.claude-plugin</code>, <code>advisor</code>, <code>continual-learning</code>, <code>cursor-team-kit</code> 등 독립 플러그인 디렉터리와 공식 마켓플레이스 구조를 확인할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 플랫폼 패권 전쟁: VS Code 마켓플레이스를 넘어선 '에이전트 스킬' 표준 싸움
            </h3>
            <p>
              과거 Microsoft가 VS Code Extension Marketplace를 장악함으로써 에디터 생태계의 패권을 거머쥐었듯, 지금 AI 코딩 플랫폼 진영(Cursor, Claude Code, OpenCode, Antigravity)은 <strong>"개발자의 팀 워크플로우와 사내 도구 연결을 누구의 플러그인 포맷 위에 올릴 것인가"</strong>를 두고 치열한 표준 선점전을 벌이고 있다.
            </p>
            <ul>
              <li><strong>크로스 하네스 호환의 신호탄:</strong> 흥미롭게도 <code>cursor/plugins</code> 저장소 최상단에 <code>.cursor-plugin</code>과 나란히 <code>.claude-plugin</code> 폴더가 공존하고 <code>pstack</code> 같은 플러그인이 Claude Code 설치까지 지원하는 모습은, 생태계가 결국 특정 IDE 독점이 아닌 <strong>이식 가능한 오픈 에이전트 플러그인 규격</strong>으로 수렴하고 있음을 시사한다.</li>
              <li><strong>팀 지식의 자산화:</strong> <code>dyl-stack</code>이나 <code>cursor-team-kit</code>처럼 최고 시니어 엔지니어의 디버깅·리뷰 철학 자체를 플러그인으로 배포할 수 있게 되면서, 기업의 핵심 엔지니어링 경쟁력이 개인의 두뇌가 아닌 '공유 가능한 플러그인 저장소'로 이동하고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 미래의 IDE는 코드 편집창이 아니라 플러그인을 조율하는 관제탑이다
            </h3>
            <p>
              타이핑을 대신해 주는 자동완성의 시대는 이미 지나갔다. 이제 엔지니어의 생산성은 어떤 에이전트 스킬과 검증 훅, 기억 루프를 내 작업실에 결합하느냐에 달려 있다.
            </p>
            <p>
              508개의 브랜치가 쉴 새 없이 움직이는 <code>cursor/plugins</code>는 에이전트 코딩의 다음 10년이 단일 모델의 지능 경쟁이 아니라, 살아 숨 쉬는 오픈 플러그인 생태계의 조합 경쟁이 될 것임을 선명하게 보여준다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Cursor+plugins+marketplace+agent+skills" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/cursor/plugins" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
