# -*- coding: utf-8 -*-
# Story 3: pingdotgg/t3code

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] pingdotgg/t3code : 멀티 에이전트 원격 컨트롤 서피스 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_t3code.jpg" alt="T3 Code Agent Control Surface" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="smartphone" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #3</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 터미널 감옥에서 해방된 자율 코딩 에이전트의 모바일 지휘소</span>
              <span class="platform-tag">Weekly Sensation</span>
              <span class="platform-tag">pingdotgg / t3code</span>
            </div>
            
            <h2 class="article-headline">
              스마트폰 하나로 로컬 코딩 에이전트 군단을 지휘한다: Theo의 'T3 Code' 원격 하네스
            </h2>

            <div class="article-subheadline">
              Claude Code, Codex, Antigravity, Cursor를 단일 화면에 결집… 무거운 데스크톱 화면을 벗어나 침대와 카페에서 스마트폰으로 풀스택 에이전트 루프를 통제하는 오픈소스 인터페이스 혁명
            </div>
            <p class="article-snippet">
              주간 1만 2천 스타를 폭발적으로 쓸어 담은 테오 브라운(Theo Browne)의 야심작 'T3 Code'. 사용자의 PC에서 구동되는 모든 AI 코딩 에이전트를 모바일 앱(iOS/Android)과 웹에서 안전하게 감독하고 승인하는 원격 에이전트 오케스트레이션 런타임을 심층 조명합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 개발자를 터미널 앞에 묶어두던 에이전트의 역설
            </h3>
            <p>
              "AI 에이전트가 코딩을 대신해 주는데, 왜 나는 여전히 터미널 창 앞을 떠나지 못하고 있는가?" 
              최근 Claude Code, Codex CLI, Cursor Agent 등을 사용하는 시니어 개발자들이 공통으로 느끼던 역설적인 피로감이었다. 
              에이전트가 수천 줄의 코드를 작성하고 테스트를 돌리는 동안, 개발자는 혹시나 에이전트가 위험한 명령을 실행할까 봐, 혹은 다음 승인 프롬프트를 띄운 채 멍하니 멈춰 있을까 봐 모니터 앞을 지키는 '터미널 경비원' 신세가 되었다.
            </p>
            <p>
              개발 생태계의 유명 인플루언서이자 풀스택 거장 <strong>테오 브라운(Theo Browne, t3.gg)</strong>이 공개한 <strong>pingdotgg/t3code</strong>는 바로 이 질문에 대한 가장 완벽하고 통쾌한 기술적 대답이다. 
              공개 직후 단 일주일 만에 12,500개 이상의 스타를 모으며 글로벌 개발 커뮤니티를 뒤흔든 T3 Code는, 에이전트의 실행 공간(로컬 머신)과 인간의 감독 공간(스마트폰, 태블릿, 브라우저)을 완벽히 분리해냈다.
            </p>
            <p>
              이제 개발자는 카페에서 커피를 마시거나 침대에 누워 스마트폰을 켜고, 집 안 데스크톱에서 병렬로 질주하는 수많은 에이전트들을 마치 스타크래프트 사령관처럼 여유롭게 지휘할 수 있게 되었다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '에이전트 하네스 컨트롤 서피스(Agent Harness Control Surface)'
            </h3>
            <p>
              T3 Code는 새로운 LLM 모델이나 독자적인 챗봇이 아니다. 
              이미 사용자가 결제하고 컴퓨터에 설치해 둔 수많은 상용/오픈소스 에이전트 구독—<strong>Claude Code, OpenAI Codex, Cursor, Grok Build, Google Antigravity, OpenCode</strong>—을 하나로 묶어내는 <strong>'메타 하네스 조종석(Meta-Harness Cockpit)'</strong>이다.
            </p>

            <div class="editorial-quote">
              <p>
                "우리가 원했던 것은 폐쇄적인 클라우드 에디터가 아니다. 
                내 컴퓨터에서 내가 신뢰하는 권한으로 에이전트가 돌되, <strong>그것을 제어하는 인간의 손길은 어디서나 자유로워야 한다.</strong> 
                T3 Code는 인간이 키보드 노동자에서 고수준 디렉터로 전환하는 조종간이다."
              </p>
              <small>— Theo Browne, T3 Code 릴리즈 선언문</small>
            </div>

            <p>
              핵심 가치는 '제로 벤더 락인'과 '완전한 오픈 소스'다. 
              복잡한 클라우드 SaaS에 코드베이스를 업로드하지 않고, 사용자의 로컬 워크스테이션에서 구동되는 초경량 데몬과 종단간 암호화(E2EE) 터널을 통해 iOS, Android 네이티브 앱 및 웹 브라우저로 연결된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 프로세스 추상화 레이어와 인터랙티브 승인 프로토콜
            </h3>
            <p>
              T3 Code가 여러 상용 CLI 에이전트들을 매끄럽게 통제할 수 있는 비결은 <strong>'가상 PTY 프로세스 가상화'</strong>와 <strong>'구조화된 이벤트 버스'</strong> 아키텍처에 있다.
            </p>

            <!-- 순수 HTML+CSS 다이어그램: T3 Code 컨트롤 서피스 아키텍처 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-tag">ARCHITECTURE SCHEMATIC</span>
                <span class="schematic-title">T3 Code 원격 하네스 컨트롤 서피스 토폴로지</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-card" style="border-left: 4px solid #8b5cf6;">
                  <div class="schematic-card-title" style="color: #6d28d9;">로컬 호스트 (Local Daemon)</div>
                  <div class="schematic-step">PTY 프로세스 격리: Claude Code / Codex / Antigravity 실행</div>
                  <div class="schematic-step">로컬 파일 시스템 & Git Worktree 감시 데몬</div>
                  <div class="schematic-step">도구 호출(Bash, File Edit) 인터셉트 및 권한 큐잉</div>
                  <div class="schematic-step">초경량 WebSocket / WebRTC E2EE 터널 브리지</div>
                </div>
                <div class="schematic-card" style="border-left: 4px solid #06b6d4;">
                  <div class="schematic-card-title" style="color: #0e7490;">원격 클라이언트 (Mobile & Web App)</div>
                  <div class="schematic-step">iOS / Android 네이티브 햅틱 피드백 UI</div>
                  <div class="schematic-step">실시간 스트리밍 터미널 렌더러 (xterm.js 네이티브 래핑)</div>
                  <div class="schematic-step">인터랙티브 결재 카드: 'rm -rf' 등 위험 명령 1-Tap 승인</div>
                  <div class="schematic-step">Diff 뷰어 및 모바일 음성 프롬프트 인터페이스</div>
                </div>
              </div>
              <p class="schematic-desc">
                ▲ 데스크톱에서 실행되는 CLI 도구들을 표준화된 JSON-RPC 프로토콜로 추상화하여, 스마트폰 알림 창에서 단 한 번의 터치로 에이전트의 코드 수정을 승인하거나 거절할 수 있다.
              </p>
            </div>

            <div class="media-showcase-box">
              <img src="../assets/images/demo_t3code.png" alt="T3 Code mobile and web control surface" class="showcase-img">
              <div class="showcase-caption">
                <strong>▲ T3 Code 공식 멀티플랫폼 컨트롤 서피스 개요:</strong> 
                모바일 앱(iOS/Android)과 일렉트론 데스크톱, 반응형 웹 앱을 통해 로컬 머신의 활성 에이전트 세션을 실시간 모니터링하며, 터미널 표준 입출력을 아름다운 리치 컴포넌트로 재해석하여 보여준다.
              </div>
            </div>

            <p>
              특히 돋보이는 부분은 <strong>'인터랙티브 승인 카드(Action Approval Cards)'</strong> 시스템이다. 
              에이전트가 데이터베이스 마이그레이션이나 프로덕션 브랜치 푸시와 같은 고위험 작업을 시도할 때, 모바일 기기에 진동과 함께 작업의 시각적 Diff와 예상 리스크가 정돈된 카드로 전송된다. 
              개발자는 산책 중에도 스마트폰의 지문 인증 한 번으로 작업을 승인하거나 피드백을 녹음해 전달할 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 독점적 클라우드 AI 에디터 진영의 위기
            </h3>
            <p>
              T3 Code의 돌풍은 Cursor, Replit, GitHub Workspace 등 '에디터 자체를 클라우드로 이전해 월 수십 달러의 구독료를 징수하려는' 빅테크 SaaS 기업들의 비즈니스 모델에 치명타를 날린다. 
              개발자들은 이미 소유하고 있는 로컬 머신의 강력한 GPU와 CPU, 그리고 기존 CLI 구독만으로도 최고의 원격 모바일 경험을 누릴 수 있기 때문이다.
            </p>
            <p>
              또한 기업 입장에서도 민감한 소스코드를 외부 클라우드 에디터 서버에 동기화할 필요 없이, 사내 보안 인트라넷 내부에서 폐쇄망 원격 에이전트 조종관을 구축할 수 있다는 강력한 보안상의 해자를 제공한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 엔지니어는 이제 책상을 벗어난다
            </h3>
            <p>
              과거 소프트웨어 엔지니어의 상징은 모니터 세 대와 기계식 키보드가 놓인 어두운 책상이었다. 
              그러나 에이전트가 손발이 되어 코드를 작성하는 시대에, 인간에게 필요한 것은 키보드가 아니라 '판단'과 '방향성'이다.
            </p>
            <p>
              T3 Code는 엔지니어를 물리적 책상의 족쇄에서 풀어주었다. 
              공원 벤치에서, 출퇴근 지하철 안에서, 혹은 저녁 식탁에서 주머니 속 스마트폰을 가볍게 탭하는 것만으로 거대한 소프트웨어 아키텍처가 스스로 진화한다. 
              개발의 공간과 시간이 근본적으로 재정의되고 있다.
            </p>

            <div class="project-links-bar">
              <a href="https://t3.codes" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i>
                <span>T3 Code 공식 다운로드 & 웹앱</span>
              </a>
              <a href="https://www.youtube.com/results?search_query=theo+t3+code+agent+harness" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i>
                <span>유튜브 관련 리뷰보기</span>
              </a>
              <a href="https://github.com/pingdotgg/t3code" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i>
                <span>GitHub 저장소 방문 (+44.5k)</span>
              </a>
            </div>

          </div>
        </div>
      </article>
"""
