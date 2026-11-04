# -*- coding: utf-8 -*-
# Story 1: deepseek-ai/dsh-superagent-prototype (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] deepseek-ai/dsh-superagent-prototype : 오늘의 메인 기사 (COVER STORY) -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_deepseek_superagent.jpg" alt="DeepSeek SuperAgent Prototype" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔥 빅테크 독점을 허무는 딥시크의 차세대 에이전트 전격 오픈소스화</span>
              <span class="platform-tag">GitHub Breakthrough</span>
              <span class="platform-tag">deepseek-ai / dsh-superagent-prototype</span>
            </div>
            
            <h2 class="main-lead-headline">
              <span id="hero-title">빅테크의 독점적 에이전트 장벽을 깨부수는 딥시크의 반격: 완전 자율 소프트웨어 엔지니어 프로토타입 전격 공개</span>
            </h2>

            <div class="article-subheadline">
              "인간의 주의 집중은 최소화하고, 엔지니어링 가치는 극대화한다" — DeepSeek-V2/V3로 전 세계 AI 지형을 뒤흔든 딥시크가 내부 핵심 자율 코딩 에이전트 『dsh-superagent』를 전격 오픈소스로 공개… 단일 저장소에 상주하며 GitHub 이슈와 사내 메신저(Feishu) 이벤트를 감지해 격리 샌드박스에서 버그 수정, 테스트 검증, PR 발행까지 무인 완결하는 차세대 에이전트 아키텍처
            </div>
            <p class="article-snippet">
              수십 번의 질문과 토큰 낭비로 개발자의 집중력을 파괴하던 기존 코파일럿의 한계를 정면 돌파. '인간의 주의 집중 비용(Attention Budget)'을 1차 원리로 삼아 침묵 속에 결과를 만들어내는 DeepSeek Harness 기반 자율 슈퍼에이전트의 충격.
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
              <i data-lucide="flame"></i> 1. 리드: 사내 메신저의 침묵과 새벽 3시에 홀로 열린 완벽한 PR
            </h3>
            <p>
              2026년 가을, 개발자들을 가장 지치게 만드는 것은 코드 작성 그 자체가 아니다. 
              역설적이게도 '스마트하다'고 자처하는 AI 코딩 어시스턴트들이 쏟아내는 수많은 질문과 확인 요청이다. 
              "이 파일을 수정해도 될까요?", "API 키를 다시 확인해주세요", "함수 이름을 추천해 드릴까요?" 등의 알림이 분 단위로 슬랙과 IDE를 뒤덮으며 엔지니어들의 딥 워크(Deep Work) 맥락을 산산조각 냈다.
            </p>
            <p>
              그런데 지난 주말, 글로벌 오픈소스 생태계를 발칵 뒤흔든 저장소 하나가 깃허브에 올라왔다. 
              바로 <strong>deepseek-ai/dsh-superagent-prototype</strong>이다. 
              공개 직후 단 이틀 만에 7,000개 이상의 스타를 쓸어 담은 이 프로젝트는 딥시크 내부 엔지니어링 팀이 매일 실제 프로덕션 개발에 사용하는 <strong>단일 저장소 전속 자율 소프트웨어 엔지니어 시스템</strong>이다.
            </p>
            <p>
              이 에이전트는 사용자와 시시콜콜 대화하지 않는다. 
              개발자가 사내 메신저(Feishu)나 깃허브 이슈에서 <code>@superagent 결제 웹훅 재시도 로직에 지수 백오프 적용해줘</code>라고 단 한 줄 남기면, 에이전트는 즉시 격리된 샌드박스를 띄워 저장소를 복제하고, 버그의 재현 테스트를 작성하며, 48개의 테스트를 통과시킨 후 깨끗한 Pull Request 번호(#451)를 메신저 스레드에 회신하고 조용히 사라진다. 
              그 사이 인간에게 묻는 불필요한 질문은 정확히 <strong>'0회'</strong>였다.
            </p>

            <div class="editorial-quote danger">
              "팀 전체를 대신해 행동할 수 있는 에이전트는 팀 전체의 주의 집중을 낭비할 수도 있습니다. 
              <strong>우리의 핵심 원칙은 단 하나입니다: 인간의 주의 집중은 최소한으로 소모하고, 엔지니어링 가치는 최대한으로 제공하라.</strong> 
              누군가 반드시 결정해야 하거나 결과를 바로 사용할 수 있을 때만 말하십시오. 그 외의 모든 순간에 에이전트는 침묵해야 합니다."
              <span class="quote-author">— DeepSeek SuperAgent 철학 매니페스토 (000-philosophy.md) 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: '말 많은 챗봇'의 종말과 침묵하는 자율성(Attention Budget)의 시대
            </h3>
            <p>
              빅테크들이 월 20~30달러짜리 대화형 코파일럿을 앞다퉈 출시하며 "AI와 페어 프로그래밍하라"고 외칠 때, 딥시크는 근본적으로 다른 질문을 던졌다: 
              <strong>"왜 엔지니어가 코드 한 줄 고치려고 AI와 잡담을 나누고 있어야 하는가?"</strong>
            </p>
            <p>
              dsh-superagent는 거시적 소프트웨어 엔지니어링의 패러다임을 '상호작용적 채팅'에서 <strong>'비동기 위임형 자율 런타임(Asynchronous Autonomous Delegation)'</strong>으로 완전히 전환시킨다. 
              이 시스템의 핵심 가치는 AI의 벤치마크 점수가 아니라 <strong>'주의 집중 예산(Attention Budget)'</strong>의 엄격한 통제다. 
              작업 허가 목록(Allowed List)에 없는 비인가 요청은 자동으로 무시되고, 승인된 작업은 <code>MasterAssessor</code> 엔진이 작업 범위와 리스크를 단독 판정한 후 백그라운드 워커에 직결된다.
            </p>
            <p>
              독점 폐쇄형 모델을 가진 OpenAI나 Anthropic이 자사 웹 UI 안으로 사용자를 가두려 하는 반면, 딥시크는 팀이 이미 일하고 있는 도구인 <strong>GitHub과 엔터프라이즈 메신저</strong> 속으로 에이전트 런타임을 투명하게 이식해 버렸다.
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-title">
                <i data-lucide="git-merge"></i> DeepSeek SuperAgent: 주의 집중 최소화 기반 자율 엔지니어링 파이프라인
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <span class="schematic-badge">단계 1: 이벤트 리스닝</span>
                  <strong>Webhook & Trigger</strong>
                  <div class="schematic-desc">
                    GitHub Issue/PR 및 Feishu 채널에서 비동기 이벤트 수신. 인가된 사용자 명단과 사전 정의된 정책 룰셋 기반 엄격한 진입 검증
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 2: 평가 & 티켓 발행</span>
                  <strong>MasterAssessor</strong>
                  <div class="schematic-desc">
                    요청의 작업 범위, 보안 위험도, 변경 허용 디렉토리를 자율 평가. 단일 구체적 Work Item(Ticket) 생성 및 우선순위 큐 적재
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 3: 샌드박스 자율 실행</span>
                  <strong>DshExecutor Runtime</strong>
                  <div class="schematic-desc">
                    /tmp 하위에 격리된 워크스페이스 세션 스폰. Git 브랜치 생성 &rarr; 코드 수정 &rarr; 테스트 실행 &rarr; 실패 시 자가 디버깅 루프 수행
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 4: 비동기 회신</span>
                  <strong>Outbox Delivery</strong>
                  <div class="schematic-desc">
                    작업 완료 시 재현 로그를 첨부한 GitHub PR 오픈. 원본 메신저 스레드에 핵심 결과만 단문 보고 후 고아 프로세스 즉시 전원 소멸
                  </div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="layers"></i> 3. 기술 메커니즘: MasterAssessor, DshExecutor, 그리고 안전 격리 세션
            </h3>
            <p>
              dsh-superagent의 아키텍처는 놀라울 정도로 정교하고 실용적이다. 
              시스템은 크게 <strong>엔진(Engine), 평가자(MasterAssessor), 실행자(DshExecutor), 보관소(Store), 아웃박스(Outbox)</strong>의 5개 핵심 레이어로 분리되어 있다.
            </p>
            <p>
              가장 돋보이는 모듈은 <code>MasterAssessor</code>다. 
              일반적인 에이전트는 사용자의 프롬프트를 받자마자 무분별하게 툴을 호출하다가 권한 오류나 무한 루프에 빠진다. 
              반면 dsh-superagent의 Assessor는 요청이 들어오면 먼저 프로젝트의 정책(Policy) 파일과 대조한다. 
              수정 대상이 결제나 인증 모듈처럼 민감한 영역인지, 허용된 디렉토리 스코프 안에 있는지를 수학적 규칙 기반으로 평가한 뒤 신뢰도(Confidence) 점수를 매긴다.
            </p>
            <p>
              작업이 승인되면 <code>DshExecutor</code>가 독립된 디렉토리를 생성하고 DeepSeek의 최신 코딩 모델을 가동한다. 
              모델은 <code>read_file</code>, <code>edit_file</code>, <code>run_command</code> 등 최소한의 프리미티브 도구만을 사용해 점진적으로 코드를 수정하며, 반드시 프로젝트의 로컬 테스트 슈트(예: <code>pnpm test</code>)를 통과할 때까지 자가 교정(Self-Correction)을 반복한다. 
              사람의 개입이 필요한 유일한 순간은 '배포 승인'이나 '모호한 비즈니스 룰 선택' 같은 결정적 분기점뿐이며, 이마저도 웹 제어 패널(localhost:3000)을 통해 단 한 번의 클릭으로 처리된다.
            </p>

            <!-- 실구동 미디어 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_deepseek_superagent.jpg" alt="DeepSeek SuperAgent Web Panel and Terminal Verification" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="monitor"></i> <strong>[실구동 아키텍처 캡처]</strong> DeepSeek Harness 위에서 구동되는 dsh-superagent 관제 콘솔 화면. 좌측 패널에는 MasterAssessor가 실시간으로 수신한 티켓 큐와 리스크 평가 배지가 표시되며, 우측 패널에는 격리된 샌드박스에서 테스트를 자동 통과시키고 Feishu와 GitHub PR로 결과를 비동기 납품하는 실행 로그가 실시간 전개되고 있다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 거버넌스: 빅테크의 월 구독료 해자와 에이전트 주권
            </h3>
            <p>
              마이크로소프트와 깃허브는 깃허브 코파일럿 워크스페이스(Copilot Workspace)를 통해 개발팀의 전 워크플로우를 애저(Azure) 클라우드 안에 묶어두려 한다. 
              좌석당 수십 달러의 월 구독료는 물론이고, 기업의 민감한 사내 코드베이스가 빅테크의 독점 서버로 전송되어야만 한다.
            </p>
            <p>
              dsh-superagent의 전격 오픈소스화는 이 폐쇄적 비즈니스 모델의 명치를 직격한다:
            </p>
            <ul>
              <li><strong>사내 인프라 완전 자립형 배포:</strong> 도커 컨테이너나 단일 온프레미스 노드에서 구동되며, 사내 프라이빗 GitLab/GitHub 엔터프라이즈와 로컬 오픈소스 LLM(DeepSeek-Coder 등)을 연결해 외부 데이터 유출을 원천 차단한다.</li>
              <li><strong>플랫폼 종속성 탈피:</strong> 특정 에이전트 벤더의 독점 클라우드 API에 얽매이지 않고, 오픈 규격인 DeepSeek Harness 번들 구조를 통해 팀의 요구에 맞게 프롬프트, 도구, 룰셋을 100% 커스터마이징할 수 있다.</li>
              <li><strong>개발자 피로도 경제학:</strong> 엔지니어 1인의 일일 집중력 비용(Cognitive Cost)을 금액으로 환산할 때, 챗봇과의 소모적 핑퐁을 없애고 비동기 PR로 결과를 받는 워크플로우는 엔터프라이즈 생산성을 수 배 이상 끌어올린다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 침묵 속에서 증명되는 진짜 지능
            </h3>
            <p>
              진짜 뛰어난 시니어 엔지니어는 말이 많지 않다. 
              요구사항의 본질을 정확히 꿰뚫고, 아무도 보지 않는 곳에서 묵묵히 코드를 고치며, 완벽하게 통과한 테스트와 명쾌한 PR로 자신의 존재를 증명한다.
            </p>
            <p>
              딥시크의 <code>dsh-superagent</code>는 AI 에이전트가 나아가야 할 궁극의 진화 방향을 제시한다. 
              화려한 챗봇 UI와 끊임없는 텍스트의 범람 뒤에 숨어 있던 거품이 걷히고, 이제 '인간의 주의를 빼앗지 않는 침묵의 자율성'이 소프트웨어 공학의 새로운 표준으로 자리 잡기 시작했다.
            </p>

          </div> <!-- .editorial-content -->

          <!-- 기사 하단 고시인성 액션 링크 바 -->
          <div class="article-links-bar">
            <a href="https://www.youtube.com/results?search_query=DeepSeek+SuperAgent+Autonomous+Coding" target="_blank" rel="noopener noreferrer" class="project-link youtube">
              <i data-lucide="play" style="width:16px;height:16px;fill:currentColor;"></i> 유튜브 관련 리뷰보기
            </a>
            <a href="https://github.com/deepseek-ai/dsh-superagent-prototype" target="_blank" rel="noopener noreferrer" class="project-link github">
              <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
            </a>
          </div>

        </div> <!-- .article-detail -->
      </article>
"""
