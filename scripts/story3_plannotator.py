# -*- coding: utf-8 -*-
# Story 3: backnotprop/plannotator

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] backnotprop/plannotator                          -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_plannotator.jpg" alt="Plannotator Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> AGENT WORKSPACE</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dbeafe; border-color:#2563eb; color:#1e40af;">✍️ 터미널을 벗어난 에이전트 주석 데스크</span>
              <span class="platform-tag">GitHub Daily Trending & plannotator.ai</span>
              <span class="platform-tag">backnotprop / plannotator</span>
            </div>
            
            <h2 class="article-headline">
              "터미널 스크롤 지옥은 끝났다" — 모든 코딩 에이전트의 계획·Diff·HTML 시안을 브라우저에서 형광펜으로 첨삭해 되돌려 보내는 'Plannotator'
            </h2>

            <div class="article-subheadline">
              Claude Code, Codex, Gemini CLI, Pi, OpenCode와 비동기 'Plannotator Inbox'로 직결되어 계획서·코드 Diff·렌더링 아티팩트를 시각적으로 마킹하고 원클릭 피드백을 전송하는 로컬 리뷰 레이어
            </div>
            <p class="article-snippet">
              5개의 코딩 에이전트를 동시에 돌리다 보면, 좁은 터미널 창 위로 마크다운 계획서와 수백 줄의 코드 변경분, 승인 대기 질문이 뒤엉켜 정신이 혼미해집니다. 오늘 GitHub 일간 트렌딩을 점령한 'Plannotator'(11,073 스타)는 에이전트가 계획이나 결과물을 내놓는 즉시 로컬 브라우저에 깔끔한 첨삭 데스크와 통합 수신함(Inbox)을 띄워줍니다. 개발자는 계획서 문단이나 HTML UI 요소에 직접 빨간 펜으로 주석을 달아 버튼 한 번으로 에이전트의 다음 턴으로 꽂아 넣을 수 있습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 병렬 에이전트 시대의 역설 — "코드는 AI가 짜는데, 인간은 터미널 탭 8개를 오가며 허덕인다"
            </h3>
            <p>
              2026년 개발자의 책상 풍경은 1년 전과 완전히 달라졌다. 이제 혼자 일하는 개발자도 한쪽 창에서는 Claude Code가 백엔드 마이그레이션을 설계하고, 다른 창에서는 Codex가 테스트를 작성하며, 또 다른 세션에서는 Gemini CLI나 Pi가 프론트엔드 시안을 뽑아낸다.
            </p>
            <p>
              문제는 <strong>피드백 인터페이스(Review Surface)</strong>가 여전히 1970년대식 80칼럼 텍스트 터미널에 갇혀 있다는 점이다. 에이전트가 200줄짜리 마크다운 계획서를 출력했을 때 "3번 항목의 캐시 전략은 빼고 5번 API 스키마는 수정해줘"라고 다시 긴 채팅을 타이핑하는 일은 고문이나 다름없었다. <strong>backnotprop/plannotator</strong>는 바로 이 인간과 다중 에이전트 사이에 뚫린 거대한 UI 구멍을 메우며 등장했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 에이전트의 흐름을 끊지 않는 비동기 'Plannotator Inbox'의 등장
            </h3>
            <p>
              Plannotator가 기존 단순 Diff 뷰어나 에디터 확장과 다른 결정적 지점은 <strong>훅(Hook)·플러그인·MCP 기반의 양방향 제어권</strong>과 새롭게 추가된 <strong>Plannotator Inbox</strong>다. 에이전트가 의사결정이나 중간 산출물 검토를 요청해도 세션을 먹통으로 블로킹(Blocking)하지 않고 인박스에 스레드와 스크린샷을 쌓아둔 뒤 다음 작업을 이어가거나 대기한다.
            </p>

            <div class="editorial-quote">
              <p>
                "Plannotator Inbox는 당신과 멀티 에이전트 작업 사이에 빠져 있던 리뷰 레이어다. <strong>에이전트가 결정이나 계획, HTML 시안을 제안하거나 작업을 마치면 로컬 브라우저 창이 열리고, 당신은 문서와 Diff 위에 직접 마크업과 코멘트를 남겨 클릭 한 번으로 해당 에이전트 세션의 다음 턴으로 피드백을 되돌려 보낸다.</strong>"
              </p>
              <small>— Plannotator 공식 릴리즈 및 Inbox 아키텍처 문서</small>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 마크다운 계획서·Git/jj Diff·HTML 아티팩트를 아우르는 3대 리뷰 엔진
            </h3>
            <p>
              Plannotator는 클라우드 SaaS가 아닌 내 로컬 머신에서 돌아가는 경량 브라우저 서피스(`plannotator inbox`)와 터미널용 `herdr-annotate`로 구성되며, 사실상 현존 모든 에이전트 생태계와 연결된다:
            </p>
            <ul>
              <li><strong>인라인 계획 및 문서 주석:</strong> Claude Code, Codex, Copilot CLI, Gemini CLI, OpenCode, Kiro, Droid, Amp, DeepSeek Harness, Pi는 물론 개인 비서(Grok Bot, Muse, Hermes, OpenClaw)가 내놓은 마크다운 스펙을 노션이나 구글 독스처럼 드래그해 인라인 코멘트를 달아 구조화된 수정 지시로 변환.</li>
              <li><strong>다중 VCS 코드 리뷰 (Git, jj, p4):</strong> 로컬 변경 사항이나 원격 PR(GitHub/GitLab)의 파일 트리와 Side-by-Side Diff를 띄우고, 특정 코드 라인에 수정 제안을 적어 에이전트에게 즉시 재작업을 지시. Git뿐만 아니라 GitButler, Jujutsu(`jj`), Perforce(`p4`)까지 네이티브 지원.</li>
              <li><strong>실시간 HTML 아티팩트 첨삭 &amp; MCP 브릿지:</strong> 에이전트가 생성한 웹 UI 프로토타입이나 리포트 HTML을 실제 렌더링된 화면 위에서 클릭해 주석을 달고, 플러그인이 없는 에이전트도 `plannotator inbox mcp` 한 줄로 즉시 합류한다.</li>
            </ul>

            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Plannotator 양방향 Human-in-the-Loop 피드백 순환 구조</span>
                <span class="schematic-badge">Local Browser Surface + MCP Inbox</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Multi-Agent Producers</div>
                  <div class="schematic-desc">
                    Claude Code · Codex · Gemini CLI<br>
                    Pi · OpenCode · Hermes · OpenClaw<br>
                    Hooks / Plugins / MCP 프로토콜 연결<br>
                    계획(Plan) · Diff · HTML 시안 송신
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Plannotator Inbox &amp; Annotator</div>
                  <div class="schematic-desc">
                    로컬 통합 인박스(비동기 스레드 큐)<br>
                    문단별 인라인 마크업 &amp; 수정 요청<br>
                    Git / Jujutsu(jj) Side-by-Side Diff<br>
                    렌더링된 HTML 요소 직접 클릭 주석
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Structured Turn Injection</div>
                  <div class="schematic-desc">
                    인간 리뷰어의 첨삭 패킷 구조화<br>
                    요청했던 에이전트 세션 다음 턴 직결<br>
                    채팅 재설명 0초 · 승인/반려 원클릭<br>
                    팀 공유 및 내장 AI 보조 검토 지원
                  </div>
                </div>
              </div>
            </div>

            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Plannotator 공식 웹사이트(plannotator.ai) 및 인터랙티브 첨삭 데모</span>
              </div>
              <img src="../assets/images/demo_plannotator.png" alt="Plannotator Official Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ plannotator.ai 실구동 화면: 10여 종의 주요 AI 코딩 에이전트 플러그인 연동 구조와 플랜 첨삭·코드 리뷰·HTML 아티팩트 인박스 워크플로우.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 시장 재편: IDE가 독점하던 '코드 리뷰 UI'의 해체
            </h3>
            <p>
              지금까지 VS Code나 Cursor 같은 무거운 통합 개발 환경(IDE)은 "에이전트의 결과물을 눈으로 검토하려면 결국 에디터를 열어야 한다"는 점을 강력한 락인(Lock-in) 무기로 삼아왔다.
            </p>
            <ul>
              <li><strong>하네스 중립적(Harness-Agnostic) 리뷰 계층:</strong> Plannotator는 특정 AI 회사나 에디터에 종속되지 않는다. 개발자가 오늘 Claude Code를 쓰다 내일 Codex나 OpenCode로 갈아타도, 인간의 검토·승인 경험은 동일한 Plannotator 인박스 위에서 일관되게 유지된다.</li>
              <li><strong>프라이버시 제로 유출:</strong> 100% 로컬 서버로 구동되므로 기업의 미공개 설계 문서나 코드 Diff가 외부 리뷰 SaaS DB에 저장될 위험이 없다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 개발자는 더 이상 타이피스트가 아니라 '편집국장'이다
            </h3>
            <p>
              에이전트가 초고를 쓰고 코드를 짜는 시대, 시니어 개발자의 업무는 키보드로 문장을 길게 치는 일이 아니라 수십 개의 원고 위에 빨간 펜으로 핵심 방향을 긋고 "고쳐 와" 또는 "출고 승인" 도장을 찍는 편집국장의 역할로 진화했다.
            </p>
            <p>
              Plannotator는 그 편집국장의 책상 위에 놓인 가장 직관적인 빨간 펜이자, 터미널 창에 갇혀 있던 인간 감독관에게 시야와 통제권을 되돌려주는 가장 영리한 오픈소스 인터페이스다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/watch?v=XqFun9XCXPw" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://plannotator.ai" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹 포털 방문
              </a>
              <a href="https://github.com/backnotprop/plannotator" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
