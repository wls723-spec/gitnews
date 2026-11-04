# -*- coding: utf-8 -*-
# Story 3: max-sixty/worktrunk (HERO 3)

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 3] max-sixty/worktrunk -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_worktrunk.jpg" alt="max-sixty worktrunk" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="git-branch" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #3</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 10개의 AI 에이전트를 동시 지휘하는 워크트리 혁신</span>
              <span class="platform-tag">GitHub Trending #3</span>
              <span class="platform-tag">max-sixty / worktrunk</span>
            </div>
            
            <h2 class="article-headline">
              "에이전트 하나만 기다리기엔 너무 느리다" — 병렬 AI 에이전트 오케스트레이터 Worktrunk
            </h2>

            <div class="article-subheadline">
              단일 CLI로 다중 AI 에이전트를 격리된 워크트리에 즉각 투입… 복잡한 git worktree 명령어를 브랜치처럼 단순화하고 CoW 빌드 캐시와 수명 주기 훅으로 병렬 개발의 병목을 해결하다
            </div>
            <p class="article-snippet">
              Claude Code나 Hermes 같은 자율 코딩 에이전트를 5~10개씩 병렬 구동할 때 발생하는 코드 충돌과 디렉토리 오염을 종식시킨 러스트(Rust) 기반 CLI 도구 Worktrunk. 에이전트 군단을 지휘하는 최신 워크스페이스 아키텍처를 분석합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 병렬 에이전트 시대, 단일 워킹 트리의 한계
            </h3>
            <p>
              Claude Code, OpenAI Operator, Antigravity 등 차세대 AI 코딩 에이전트들은 이제 사람의 감독 없이도 수십 분간 자율적으로 리팩토링과 테스트를 수행할 수 있다. 
              자연스럽게 개발자들의 작업 방식은 <strong>"에이전트 하나를 지켜보는 것"에서 "5~10개의 에이전트를 동시에 띄워 서로 다른 기능을 병렬로 개발시키는 것"</strong>으로 급변했다.
            </p>
            <p>
              하지만 치명적인 복병이 나타났다. 모든 에이전트가 단일 로컬 Git 리포지토리에서 작업할 경우 브랜치 체크아웃 시 미커밋 파일이 꼬이고, 테스트 파일이 서로의 변경 사항을 덮어쓰는 대혼란이 발생하기 때문이다. 
              Git의 내장 기능인 <code>git worktree</code>가 해법이지만, 타이핑해야 하는 명령어가 너무 길고 번거로웠다. 
              이를 가장 우아한 러스트(Rust) CLI로 재창조한 <strong>max-sixty/worktrunk</strong>가 엔지니어들 사이에서 열광적인 지지를 얻고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 브랜치만큼이나 가벼워진 워크트리 경험
            </h3>
            <p>
              기존에 새 워크트리를 만들려면 <code>git worktree add -b feat ../repo.feat</code>를 치고 다시 디렉토리를 이동해야 했다. 
              하지만 Worktrunk에서는 단 한 줄로 에이전트 실행까지 끝난다:
            </p>

            <div class="editorial-quote">
              <p>
                <code>wt switch -x claude -c feature-auth -- '사용자 인증 모듈 추가해줘'</code><br>
                <code>wt switch -x claude -c fix-pagination -- '페이지네이션 버그 수정해줘'</code>
              </p>
              <small>— Worktrunk 병렬 에이전트 실행 패턴 예시</small>
            </div>

            <p>
              <code>-x</code> 플래그를 통해 워크트리 생성 즉시 지정된 AI 에이전트(Claude Code 등)가 백그라운드에서 해당 프롬프트로 작업을 시작하며, 각각의 작업은 완벽하게 격리된 디렉토리에서 안전하게 실행된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 엔지니어링: CoW 빌드 캐시와 수명 주기 훅
            </h3>
            <p>
              독립된 워크트리를 여러 개 만들 때 가장 큰 문제는 <code>node_modules</code>나 러스트 <code>target/</code> 폴더 같은 수 GB 크기의 의존성이 중복 설치되는 문제다. 
              Worktrunk는 이를 해결하기 위해 두 가지 핵심 기술을 내장했다:
            </p>
            <ul>
              <li><strong>CoW (Copy-on-Write) 빌드 캐시 공유:</strong> 지원되는 파일 시스템에서 하드링크나 리플링크를 활용해 대용량 빌드 아티팩트를 워크트리 간에 즉각 공유하여 디스크 낭비와 컴파일 시간을 80% 이상 단축.</li>
              <li><strong>자동화 훅(Hooks) 파이프라인:</strong> 워크트리 생성 시점(<code>post-create</code>), 에이전트 작업 완료 후 머지 전(<code>pre-merge</code>), 머지 후 정리(<code>post-merge</code>) 단계마다 자동으로 테스트나 린터를 돌리는 이벤트 훅 지원.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="git-branch" style="color:#0ea5e9;"></i> Worktrunk 병렬 에이전트 워크스페이스 아키텍처
                </span>
                <span class="schematic-badge">PARALLEL AGENT ORCHESTRATION</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">격리 워크트리 생성 & 에이전트 투입</div>
                  <div class="step-tech">wt switch -x [agent] -c [branch]</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">CoW 빌드 캐시 및 훅 자동 구동</div>
                  <div class="step-tech">Shared Target / Reflink Cache</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">CI 스트리밍 감시 & 원클릭 머지</div>
                  <div class="step-tech">wt merge (Squash/Rebase/Cleanup)</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 원리:</strong> 각각의 AI 에이전트에게 온전한 Git 샌드박스를 제공하여 파일 충돌을 원천 방지하고, 작업이 끝나면 단 한 번의 명령으로 메인 브랜치에 스쿼시 머지 후 워크트리를 깔끔하게 정리합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="monitor"></i> 4. 인터랙티브 피커와 LLM 커밋 메시지
            </h3>
            <p>
              작업 중인 수많은 워크트리의 상태를 파악하는 것도 간편하다. 
              대화형 터미널 UI(Interactive Picker)를 통해 각 워크트리의 변경 Diff, 커밋 로그, 실시간 GitHub CI 빌드 상태, 열려있는 PR 코멘트를 스트리밍으로 프리뷰할 수 있다. 
              또한 <code>wt commit</code> 실행 시 코드 Diff를 요약해 완벽한 컨벤션의 LLM 커밋 메시지를 자동 생성한다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="monitor" style="color:#10b981;"></i> Worktrunk 터미널 데모 & 워크트리 스위처
                </span>
                <span class="media-showcase-badge demo">OFFICIAL CLI PREVIEW</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_worktrunk.png" alt="Worktrunk CLI in action" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 병렬 작업 관리 콘솔:</strong> 여러 브랜치의 작업 상태와 에이전트의 진행 경과를 하나의 터미널 창에서 매끄럽게 모니터링합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="check-circle-2"></i> 5. 미래 전망: 에이전틱 개발 표준 도구로의 도약
            </h3>
            <p>
              단일 에이전트의 생산성을 1이라고 한다면, 충돌 없는 병렬 에이전트 오케스트레이션은 5배, 10배의 레버리지를 만든다. 
              Worktrunk는 Git이라는 검증된 버전 관리 인프라 위에 가장 자연스러운 에이전트 협업 계층을 구축함으로써 현대 소프트웨어 엔지니어링의 패러다임을 한 단계 앞당겼다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://worktrunk.dev" target="_blank" class="project-link demo">
                  <i data-lucide="sparkles" style="width:16px;height:16px;"></i> 공식 웹사이트 & 문서
                </a>
                <a href="https://github.com/max-sixty/worktrunk" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
