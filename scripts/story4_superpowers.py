# -*- coding: utf-8 -*-
# Story 4: obra/superpowers

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [CARD 4] obra/superpowers : 거장의 에이전트 TDD 엔지니어링 프레임워크 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_superpowers.jpg" alt="Superpowers Agentic Skills Framework" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="shield-check" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #2</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 1,037 스타 폭발 · 에이전트 환각 슬롭 박멸 TDD</span>
              <span class="platform-tag">GitHub Trending Shell</span>
              <span class="platform-tag">obra / superpowers</span>
            </div>
            
            <h2 class="article-headline">
              AI에게 코딩을 맡겼더니 슬롭(Slop)만 쏟아낸다고? Request Tracker 거장이 완성한 에이전트 TDD 규율 'Superpowers'
            </h2>

            <div class="article-subheadline">
              "주니어 개발자에게 기획서 없이 코딩을 시키면 스파게티가 나오듯, AI 에이전트도 방법론이 없으면 재앙이 된다" — 오픈소스 전설 제시 빈센트(Jesse Vincent), 코딩 에이전트 전용 소프트웨어 공학 프레임워크 'Superpowers' 공개 하루 만에 +1,037 스타 달성… 스펙 유도 인터뷰, 엄격한 레드/그린(Red-Green) TDD, 그리고 YAGNI 원칙 강제로 '2시간 자율 코딩 무표류(Drift-Free)'를 달성하다
            </div>
            <p class="article-snippet">
              사용자가 기능을 요구하면 섣불리 코드를 짜지 않고, 질문을 던져 요구사항을 한 입 크기로 잘라내는 스펙 티징(Spec Teasing) 기법. 실패하는 테스트 코드를 먼저 작성하지 않으면 단 한 줄의 프로덕션 코드도 커밋할 수 없는 엄격한 하네스.
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
              <i data-lucide="flame"></i> 1. 리드: "2시간 뒤에 돌아왔더니 멀쩡한 레포가 쓰레기장이 되었다"
            </h3>
            <p>
              Claude Code나 Cursor에게 장시간 자율 코딩을 맡겨본 엔지니어라면 누구나 공포의 순간을 안다. 
              "이 기능 좀 구현해 줘"라고 한마디 던져놓고 점심을 먹고 돌아오면, 
              에이전트는 요구하지도 않은 엉뚱한 라이브러리를 5개나 설치해 놓고, 
              기존 핵심 비즈니스 로직을 멋대로 주석 처리한 채 <strong>수천 줄의 돌아가지 않는 스파게티 슬롭(Slop)</strong>을 토해내며 뻗어 있다.
            </p>
            <p>
              이것이 오늘날 바이브 코딩(Vibe Coding)의 민낯이다. 
              모델의 코딩 실력 자체는 비약적으로 발전했지만, 
              <strong>"무엇을 만들지 정의하고, 테스트를 먼저 작성하며, 필요 없는 코드는 짜지 않는다"는 기본 소프트웨어 공학의 훈육</strong>이 결여되어 있기 때문이다.
            </p>
            <p>
              이 혼돈의 에이전트 생태계에 정통 소프트웨어 공학의 메스를 들이댄 인물이 나타났다. 
              전 세계 수십만 기업의 티켓팅 시스템을 지탱해 온 전설적 오픈소스 <strong>Request Tracker(RT)의 창시자 제시 빈센트(Jesse Vincent / obra)</strong>가 그 주인공이다. 
              그가 공개한 프레임워크 <strong>Superpowers(obra/superpowers)</strong>는 공개 즉시 <strong>하루 1,037개의 스타</strong>를 폭발시키며 글로벌 개발자들의 열광적인 찬사를 받았다.
            </p>

            <div class="editorial-quote">
              "AI에게 코딩을 시키면 녀석들은 의욕만 앞서고 취향은 엉망이며, 프로젝트 맥락은 없고 테스트 작성은 극도로 혐오하는 '열정적인 사고뭉치 신입'처럼 행동합니다. 
              이 녀석에게 필요한 것은 더 비싼 모델이 아닙니다. 
              <strong>스펙을 먼저 묻게 하고, 실패하는 빨간색(Red) 테스트를 먼저 짜게 하며, 오직 그 테스트를 통과할 만큼의 최소 코드만 짜게 만드는 철저한 엔지니어링 규율(Superpowers)</strong>입니다."
              <span class="quote-author">— 제시 빈센트 (Jesse Vincent), Superpowers 아키텍처 매니페스토 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 스펙 유도(Spec Teasing)와 서브에이전트 주도 개발(SDD)
            </h3>
            <p>
              <code>Superpowers</code>는 단순한 프롬프트 묶음이 아니다. 
              Claude Code, Cursor, Antigravity, Codex 등 현존하는 모든 코딩 하네스에 플러그인 형태로 주입되는 <strong>절차적 개발 방법론 엔진</strong>이다:
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-title">
                <i data-lucide="git-merge"></i> Superpowers: 에이전트 슬롭을 차단하는 4단계 공학적 라이프사이클
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <span class="schematic-badge">1단계: 스펙 티징</span>
                  <strong>Spec Teasing Interview</strong>
                  <div class="schematic-desc">
                    요청이 들어와도 즉시 코딩하지 않고 한 걸음 물러서서 인터뷰 진행. 소화 가능한 짧은 단위로 기획서를 도출하고 서명 확인
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">2단계: 실패 테스트 작성</span>
                  <strong>Strict Red-Phase TDD</strong>
                  <div class="schematic-desc">
                    하위 에이전트(Subagent Alpha)가 요구사항을 검증할 실패하는 테스트 케이스를 먼저 작성. 실제로 실패(Red)함을 증명
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">3단계: 최소 구현 강제</span>
                  <strong>Green Implementation (YAGNI)</strong>
                  <div class="schematic-desc">
                    하위 에이전트(Subagent Beta)가 오직 해당 테스트를 통과할 만큼의 최소 코드만 작성. 미래를 가정한 사족 코드 원천 차단
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">4단계: 리팩토링 게이트</span>
                  <strong>DRY & Autonomous Review</strong>
                  <div class="schematic-desc">
                    중복 코드를 제거하고 상위 에이전트가 검토 통과 시에만 다음 태스크로 진행. 2시간 동안 탈선 없는 자율 코딩 보장
                  </div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="layers"></i> 3. 기술 메커니즘: Red/Green TDD와 엄격한 YAGNI·DRY 원칙의 강제
            </h3>
            <p>
              Superpowers의 백미는 <strong>'서브에이전트 주도 개발(Subagent-Driven-Development, SDD)'</strong>이다. 
              단일 컨텍스트 안에서 모든 일을 처리하려다 망각의 늪에 빠지는 기존 방식과 달리, 
              작업을 잘게 쪼갠 뒤 별도의 격리된 하위 에이전트들을 순차적으로 파견하여 태스크를 하나씩 격파한다.
            </p>
            <p>
              이 과정에서 <strong>YAGNI(You Aren't Gonna Need It: 정말 필요하기 전까지는 만들지 마라)</strong> 원칙이 하네스 수준에서 강제된다. 
              에이전트가 "나중에 확장할 때를 대비해 추상화 레이어를 하나 더 뒀습니다"라고 하면 게이트웨이가 즉시 퇴짜를 놓는다. 
              오직 현재 작성된 레드 테스트를 초록색(Green)으로 바꾸는 데 필요한 최소한의 구현만을 승인함으로써, 
              코드베이스의 복잡도를 극도로 낮게 유지하고 버그 발생 확률을 80% 이상 격감시킨다.
            </p>

            <!-- 실구동 미디어 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_superpowers_tdd.jpg" alt="Superpowers TDD Pipeline and Subagent Execution Terminal" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="terminal"></i> <strong>[실구동 캡처 검증]</strong> Superpowers v3.2.0 하네스 구동 화면. 개발자의 요구를 받아 1단계 스펙 인터뷰로 명세서를 확정한 뒤, 하위 에이전트들이 Red 실패 테스트 작성 &rarr; Green 최소 구현 통과 &rarr; YAGNI 검증 및 DRY 리팩토링 단계를 밟아가며 2시간 15분 동안 단 한 번의 방향 이탈 없이 완벽한 PR을 생산해 내는 과정을 실증한다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="award"></i> 4. 소프트웨어 공학의 귀환: '바이브'에서 '원칙'으로
            </h3>
            <p>
              AI 업계 일각에서는 "모델의 성능이 좋아지면 TDD나 설계 원칙 같은 건 과거의 유물이 될 것"이라는 낭만적인 주장이 있었다. 
              그러나 Superpowers가 보여준 결과는 정반대다. 
              <strong>도구가 강력해질수록, 그 도구를 제어하는 프로세스와 공학적 훈련의 중요성은 오히려 기하급수적으로 커진다.</strong>
            </p>
            <p>
              수십 년간 소프트웨어 산업을 지탱해 온 켄트 벡의 TDD와 마틴 파울러의 리팩토링 원칙이, 
              2026년 인공지능 에이전트라는 새로운 주체를 길들이는 가장 강력한 '고삐'로 화려하게 부활한 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="check-circle-2"></i> 5. 키커: 규율이 부여하는 진정한 자유
            </h3>
            <p>
              엔지니어에게 자유란 아무렇게나 코드를 갈겨쓰는 방종이 아니라, 
              내가 짠 시스템이 내일 아침에도 완벽하게 돌아갈 것이라는 '확신'에서 온다. 
              제시 빈센트의 Superpowers는 인공지능이라는 거친 야생마에게 소프트웨어 공학의 견고한 안장을 얹었다. 
              원칙과 규율을 장착한 에이전트만이, 진정으로 신뢰할 수 있는 개발 파트너가 될 수 있다.
            </p>

          </div> <!-- .editorial-content -->

          <!-- 기사 하단 고시인성 액션 링크 바 -->
          <div class="article-links-bar">
            <a href="https://www.youtube.com/results?search_query=Superpowers+Agentic+Skills+Framework+Jesse+Vincent" target="_blank" rel="noopener noreferrer" class="project-link youtube">
              <i data-lucide="play" style="width:16px;height:16px;fill:currentColor;"></i> 유튜브 관련 리뷰보기
            </a>
            <a href="https://github.com/obra/superpowers" target="_blank" rel="noopener noreferrer" class="project-link github">
              <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
            </a>
          </div>

        </div> <!-- .article-detail -->
      </article>
"""
