# -*- coding: utf-8 -*-
# Story 1: obra/superpowers (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] obra/superpowers : COVER STORY                    -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_superpowers.jpg" alt="Superpowers Agentic Software Engineering OS Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">⚡ 15대 AI 코딩 에이전트를 장악한 공학 OS</span>
              <span class="platform-tag">GitHub Trending &amp; Prime Radiant</span>
              <span class="platform-tag">obra / superpowers</span>
            </div>

            <h2 class="main-lead-headline">
              <span id="hero-title">"코드부터 짜지 마라" — AI 에이전트의 폭주를 멈추고 수 시간 자율 엔지니어링을 구현한 'Superpowers'</span>
            </h2>

            <div class="article-subheadline">
              Claude Code·Antigravity·Codex·Cursor·Gemini CLI·Hermes Agent까지 15대 하네스를 관통하며 브레인스토밍→Git Worktree→RED-GREEN TDD→서브에이전트 2단계 리뷰를 강제하는 스킬 OS (+2,029스타/일, 누적 322,035스타)
            </div>
            <p class="article-snippet">
              프롬프트 한 줄을 던지자마자 테스트도 설계도 없이 수백 줄의 스파게티 코드를 쏟아내는 AI 코딩 에이전트의 '성급한 폭주'에 개발자들이 반기를 들었습니다. 오늘 하루에만 2,029개의 스타를 추가하며 GitHub 전체 트렌딩 압도적 1위(누적 32만2천 스타)에 복귀한 <strong>obra/superpowers</strong>는 단순한 프롬프트 모음이 아닙니다. 에이전트가 코드를 단 한 줄 쓰기 전에 스스로 멈춰 서서 요구사항을 인터뷰하고, 격리된 Git Worktree를 파고, 실패하는 테스트부터 작성하게 만드는 완결형 소프트웨어 공학 운영체제입니다.
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
              <i data-lucide="flame"></i> 1. 리드: "리액트 할 일 앱 만들어줘"라고 말했는데 에이전트가 코딩을 거부했다
            </h3>
            <p>
              터미널을 열고 <code>Let's make a react todo list</code>라고 입력한다. 기존 코딩 에이전트라면 0.5초 만에 <code>App.tsx</code>를 생성하며 패키지를 설치하고 제멋대로 상태 관리 라이브러리를 욱여넣기 시작했을 것이다. 그러나 <strong>Superpowers</strong>가 탑재된 에이전트는 키보드에서 손을 뗀다. 대신 <code>using-superpowers</code> 부트스트랩이 세션 시작과 동시에 자동 발동하면서, 에이전트는 먼저 <code>brainstorming</code> 스킬을 호출해 묻는다. <em>"오프라인 동기화가 필요한가요, 다중 사용자 협업이 목표인가요?"</em>
            </p>
            <p>
              Request Tracker의 창시자이자 Prime Radiant의 제시 빈센트(Jesse Vincent)가 설계한 MIT 오픈소스 프레임워크 <strong>obra/superpowers</strong>가 오늘 하루에만 2,029스타(누적 322,035스타)를 끌어올리며 다시 GitHub 트렌딩 왕좌를 탈환했다. Anthropic의 Claude 공식 플러그인 마켓플레이스와 OpenAI Codex 공식 마켓플레이스, xAI Grok Build, Google Antigravity(<code>agy plugin install</code>), Cursor, Gemini CLI, Hermes Agent, Kimi Code, Qwen Code, Muse까지 무려 15개 이상의 메이저 코딩 하네스를 단일 스킬 규격으로 통합하며 사실상 'AI 에이전트 시대의 표준 소프트웨어 공학 헌법'으로 자리매김한 결과다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 왜 32만 명의 개발자가 '더 똑똑한 모델' 대신 '엄격한 절차'에 열광하는가
            </h3>
            <p>
              2026년 하반기, 모델의 단일 추론 능력은 이미 상향 평준화됐다. 병목은 모델의 지능이 아니라 <strong>'통제되지 않은 조급함'</strong>이다. 컨텍스트 창이 길어질수록 에이전트는 전체 아키텍처를 건너뛰고 눈앞의 파일만 고치며, 실패한 테스트를 가짜 목(Mock)으로 덮고, 계획 없이 코드를 늘려 나간다. Superpowers는 이 문제를 더 거대한 모델이 아닌 <strong>'강제적 워크플로우 게이트(Mandatory Gates)'</strong>로 돌파했다.
            </p>

            <div class="editorial-quote">
              <p>
                "열정은 넘치지만 감각도, 판단력도, 프로젝트 맥락도 없고 테스트 작성마저 싫어하는 <strong>주니어 엔지니어가 그대로 따라 할 수 있을 만큼 명쾌한 계획</strong>을 세워라. 테스트보다 먼저 작성된 코드는 가차 없이 삭제한다."
              </p>
              <small>— obra/superpowers 공식 아키텍처 철학 (RED-GREEN-REFACTOR &amp; YAGNI/DRY)</small>
            </div>

            <p>
              일단 사용자가 설계 문서에 서명하고 "진행해(Go)"를 외치면, 에이전트는 <code>subagent-driven-development</code> 모드로 돌입해 태스크마다 신선한 컨텍스트의 서브에이전트를 파견하고 2단계 코드 리뷰(스펙 준수 여부 → 코드 품질)를 통과할 때까지 수 시간 동안 계획에서 벗어나지 않고 자율 작업을 완수한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 7단계 강제 파이프라인과 자가 진단(Diagnosing) 루프
            </h3>
            <p>
              Superpowers의 핵심은 "권장 사항(Suggestion)"이 아니라 에이전트가 어떤 작업을 시작하든 자동으로 트리거되는 <strong>강제 상태 머신(State Machine)</strong>에 있다:
            </p>
            <ul>
              <li><strong>세션 부트스트랩 &amp; 브레인스토밍 (<code>using-superpowers</code> → <code>brainstorming</code>):</strong> <code>SessionStart</code> 훅이나 스킬 설명 주입을 통해 대화 시작과 동시에 부트스트랩이 걸리며, 구현 전 짧은 청크 단위의 설계 문서를 합의할 때까지 코드 수정을 차단한다.</li>
              <li><strong>격리된 작업 공간 &amp; 미세 태스크 분할 (<code>using-git-worktrees</code> → <code>writing-plans</code>):</strong> 설계 승인 직후 독립된 브랜치와 Git Worktree를 파서 클린 테스트 베이스라인을 확인한 뒤, 모든 작업을 2~5분 분량의 파일 경로·완전한 코드·검증 커맨드가 명시된 마이크로 태스크로 쪼갠다.</li>
              <li><strong>엄격한 RED-GREEN TDD &amp; 2단계 서브에이전트 리뷰:</strong> <code>test-driven-development</code> 스킬은 실패하는 테스트를 먼저 확인(RED)한 뒤 최소 구현(GREEN)을 강제하며, <code>requesting-code-review</code>가 치명적 결함 발견 시 다음 태스크 진행을 물리적으로 막는다. 세션이 꼬였을 때는 <code>diagnosing-superpowers</code>가 트랜스크립트를 라인 단위로 감사해 원인 리포트를 생성한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Superpowers 7단계 자율 소프트웨어 공학 파이프라인</span>
                <span class="schematic-badge">MIT License · 15+ Agent Harnesses</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Spec &amp; Isolation</div>
                  <div class="schematic-desc">
                    <code>brainstorming</code> 의도 인터뷰<br>
                    설계 문서(Design Doc) 서명<br>
                    <code>using-git-worktrees</code> 브랜치 격리<br>
                    클린 테스트 베이스라인 확보
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Plan &amp; Subagent TDD</div>
                  <div class="schematic-desc">
                    <code>writing-plans</code> 2~5분 태스크 분할<br>
                    <code>subagent-driven-development</code><br>
                    <code>RED → GREEN → REFACTOR</code> 강제<br>
                    테스트 선행 없는 코드 즉시 폐기
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Dual Review &amp; Ship</div>
                  <div class="schematic-desc">
                    1차: 스펙 준수(Spec Compliance)<br>
                    2차: 코드 품질(Code Quality) 게이트<br>
                    <code>verification-before-completion</code><br>
                    <code>finishing-a-development-branch</code>
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">obra/superpowers 공식 GitHub 저장소 &amp; 멀티 하네스 지원 현황</span>
              </div>
              <img src="../assets/images/demo_superpowers.png" alt="Superpowers Official Repository Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ obra/superpowers 공식 저장소 실화면: Claude Code, Antigravity, Codex, Cursor, Gemini CLI, Hermes Agent, Muse 등 모든 주요 에이전트 하네스에서 동일한 공학 워크플로우가 작동한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 산업 패권: 벤더 종속을 무력화한 '오픈 스킬 레이어'의 승리
            </h3>
            <p>
              Anthropic, OpenAI, Cursor, Google, xAI가 각자의 폐쇄형 마켓플레이스와 에이전트 UX로 개발자 락인(Lock-in)을 시도하는 동안, Superpowers는 정반대의 역학 관계를 만들어냈다. 하나의 MIT 오픈소스 저장소가 모든 벤더의 공식 플러그인 마켓플레이스에 동시에 입점함으로써, 개발자의 공학 노하우와 스킬 자산이 특정 AI 모델이나 IDE 벤더에 귀속되지 않고 이식 가능해졌기 때문이다.
            </p>
            <ul>
              <li><strong>스킬 평가(Evals)의 체계화:</strong> <code>superpowers-evals</code> 하네스를 통해 프롬프트 감각이 아니라 실제 에이전트 행동 테스트로 스킬 회귀(Regression)를 검증한다.</li>
              <li><strong>프라이버시 투명성:</strong> 선택적 비주얼 컴패니언 로고 텔레메트리마저 <code>SUPERPOWERS_DISABLE_TELEMETRY</code>나 Claude Code 옵트아웃 플래그로 즉시 차단할 수 있도록 투명하게 공개했다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 모델은 교체되지만, 규율은 남는다
            </h3>
            <p>
              내년이면 오늘의 최강 프론티어 모델도 구형이 될 것이다. 하지만 "설계 없이 코딩하지 않고, 실패하는 테스트 없이 구현을 믿지 않으며, 증거 없이 완료를 선언하지 않는다"는 소프트웨어 공학의 1차 원리는 바뀌지 않는다.
            </p>
            <p>
              32만 개의 스타가 증명하는 진실은 단순하다. AI 시대의 진정한 초능력(Superpowers)은 모델 파라미터 숫자가 아니라, 기계의 무한한 속도에 인간의 단단한 공학 규율을 씌우는 능력에서 나온다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=obra+superpowers+coding+agent+workflow" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/obra/superpowers" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
