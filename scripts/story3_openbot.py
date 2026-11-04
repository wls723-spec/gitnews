# -*- coding: utf-8 -*-
# Story 3: nightly-labs/openbot

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [CARD 3] nightly-labs/openbot : 로컬 퍼스트 AI 팀원 데스크톱 워크스페이스 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_openbot.jpg" alt="OpenBot Local AI Teammates Workspace" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="users" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #3</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 705 스타 폭발 · Codex·Claude·Grok 오케스트레이션</span>
              <span class="platform-tag">GitHub Trending TypeScript</span>
              <span class="platform-tag">nightly-labs / openbot</span>
            </div>
            
            <h2 class="article-headline">
              Codex, Claude, Grok을 하나의 데스크톱 사옥에 모으다: 로컬 퍼스트 AI 동료 워크스페이스 'OpenBot'
            </h2>

            <div class="article-subheadline">
              "브라우저 탭 10개를 띄우고 프롬프트를 복붙하던 시대는 끝났다" — Nightly Labs, 이기종 AI 에이전트들을 단일 로컬 데스크톱 워크스페이스에서 가동하는 오픈소스 협업 플랫폼 'OpenBot' 공개… 독립 작업 큐(FIFO Queue), 에이전트 간 직통 메신저(A2A Messaging), 샌드박스 임베디드 브라우저와 CUA 드라이버 결합으로 '1인 유니콘 기업'의 인프라를 완성하다
            </div>
            <p class="article-snippet">
              OpenAI, Anthropic, xAI, Google 등 서로 다른 빅테크 모델들을 하나의 로컬 채널에 소환하여 자율 위임(Delegation)과 피어 리뷰를 실행. 크래시 복구 보장 작업 큐와 컴퓨터 유즈(Computer Use) 자동화로 완성된 가상 사무실.
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
              <i data-lucide="flame"></i> 1. 리드: 파편화된 브라우저 창에서 허우적대는 개발자들의 비명
            </h3>
            <p>
              오늘날 개발자의 데스크톱 화면은 아수라장이다. 
              한쪽 모니터에는 Claude Code 터미널이 돌고 있고, 브라우저에는 ChatGPT 창 3개, Grok 검색창 2개, Cursor 에디터와 로컬 Ollama 콘솔이 어지럽게 널려 있다. 
              한 모델이 작성한 코드를 다른 모델에게 검토받으려면 개발자가 직접 마우스로 드래그해 복사하고 붙여넣는 <strong>'인간 컨베이어 벨트'</strong> 노릇을 해야만 한다.
            </p>
            <p>
              이 비효율을 타파하기 위해 클라우드 기반 멀티 에이전트 SaaS들이 쏟아져 나왔지만, 
              소스코드 유출에 극도로 민감한 기업과 개발자들은 값비싼 월 구독료와 외부 서버 데이터 전송이라는 치명적 리스크 앞에서 주저할 수밖에 없었다.
            </p>
            <p>
              이 분절된 에이전트 생태계를 하나의 매끄러운 <strong>로컬 퍼스트 데스크톱 앱(Local-First Desktop App)</strong>으로 통합한 오픈소스 <strong>OpenBot(nightly-labs/openbot)</strong>이 등장하며 깃허브 트렌딩을 강타했다. 
              오픈 첫날 <strong>705개 이상의 스타</strong>를 기록하며 개발자 커뮤니티의 폭발적인 지지를 이끌어냈다.
            </p>

            <div class="editorial-quote">
              "진짜 회사의 사무실을 생각해 보십시오. 기획자, 개발자, 보안 담당자가 각자 다른 전문성을 가지고 같은 슬랙 채널에서 대화하며 문서를 주고받습니다. 
              <strong>OpenBot은 내 컴퓨터 로컬 환경에 그런 가상 사무실을 차려줍니다. Claude가 아키텍처를 잡으면, Grok이 보안 취약점을 찌르고, Codex가 구현 코드를 짭니다. 인간은 결재권자로서 방향만 지시하면 됩니다.</strong>"
              <span class="quote-author">— Nightly Labs 창업팀 릴리즈 노트 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: A2A(에이전트 간) 직통 통신과 크래시 내성 작업 큐(FIFO Queue)
            </h3>
            <p>
              <code>OpenBot</code>의 핵심 차별점은 단순한 채팅 껍데기(UI Wrapper)가 아니라는 점이다. 
              각 에이전트에게 <strong>독립된 로컬 작업 공간(Workspace), 전용 메모리 컨텍스트, 그리고 시스템 수준의 작업 큐</strong>를 부여하는 하나의 독립 OS처럼 동작한다:
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-title">
                <i data-lucide="git-merge"></i> OpenBot: 로컬 퍼스트 AI 팀원 오케스트레이션 아키텍처
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <span class="schematic-badge">코어 1: 로컬 작업 큐</span>
                  <strong>크래시 복구 FIFO 큐</strong>
                  <div class="schematic-desc">
                    SQLite 트랜잭션 기반 작업 대기열. 시스템 충돌이나 정전 시에도 모든 에이전트의 진행 상태와 메시지를 100% 무손실 복구
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">코어 2: 이기종 어댑터</span>
                  <strong>Universal Agent Protocol</strong>
                  <div class="schematic-desc">
                    Codex, Claude Code, Grok CLI, Cursor, Cline, Gemini 및 로컬 Ollama/LM Studio를 단일 ACP 프로토콜로 추상화 연결
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">코어 3: 브라우저 격리</span>
                  <strong>CUA 드라이버 내장</strong>
                  <div class="schematic-desc">
                    샌드박스 크로미움 브라우저를 백그라운드에 상주시킨 후, 에이전트가 직접 마우스 커서와 키보드로 웹 UI를 클릭·검증하는 컴퓨터 유즈
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">코어 4: 협업 메커니즘</span>
                  <strong>Agent-to-Agent 채널</strong>
                  <div class="schematic-desc">
                    공유 채널 채팅에서 작업 소유자가 다른 에이전트에게 하위 태스크를 직접 위임(Delegation)하고 결과를 취합하는 협업 루프
                  </div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="layers"></i> 3. 기술 메커니즘: CUA 컴퓨터 유즈와 지능형 컨텍스트 압축
            </h3>
            <p>
              OpenBot이 기술적으로 찬사를 받는 대목은 <strong>내장된 CUA(Computer Use Agent) 드라이버</strong>다. 
              외부 클라우드 서비스에 의존하지 않고, 데스크톱 프로세스로 실행되는 자체 <code>cua-driver</code> 바이너리를 통해 macOS, Windows, Linux 환경에서 에이전트에게 격리된 브라우저 제어권을 부여한다. 
              에이전트가 작성한 프론트엔드 코드를 즉시 로컬 브라우저 창에 띄우고, 실제 버튼을 클릭하고 렌더링 상태를 OCR로 읽어 들여 스스로 시각적 버그를 잡는다.
            </p>
            <p>
              또한 장시간 협업 시 발생하는 '컨텍스트 윈도우 한계' 문제를 해결하기 위해 <strong>선제적 자동 컴팩션(Proactive Auto-Compaction)</strong> 기술을 적용했다. 
              토큰 한도의 80%에 도달하면 중요 의사결정 요약문과 현재 코드 브랜치 상태만을 정제하여 새로운 세션 헤더로 넘김으로써, 며칠 동안 쉬지 않고 돌아가는 무중단 자율 에이전트 파이프라인을 실현했다.
            </p>

            <!-- 실구동 미디어 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_openbot_workspace.jpg" alt="OpenBot Desktop Multi-Agent Workspace UI" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="layout"></i> <strong>[실구동 캡처 검증]</strong> OpenBot 데스크톱 v1.4.0 구동 화면. 좌측 사이드바의 AI 팀원 패널(Claude Code, Codex 5, Grok 3 등)과 중앙의 FIFO 로컬 작업 큐, 하단의 샌드박스 브라우저 CUA 실행 화면, 우측 #dev-channel에서 에이전트들이 실시간으로 코드 리뷰와 버그 패치를 조율하는 멀티 에이전트 협업 상황을 선명하게 보여준다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="trending-up"></i> 4. 비즈니스 임팩트: 1인 기업(Solo-Founder)의 슈퍼파워화
            </h3>
            <p>
              이 도구가 가져올 경제적 파급력은 '1인 기업'의 폭발적 확장이다. 
              기존에는 시드 투자를 유치하고 5~6명의 엔지니어를 고용해야만 가능했던 소프트웨어 개발, 인프라 배포, QA 검증, 보안 침투 테스트의 전 과정을 
              <strong>단 1명의 창업자가 OpenBot 안에서 4~5대의 AI 팀원 편대를 지휘하며 처리</strong>할 수 있게 되었다.
            </p>
            <p>
              특히 모든 대화 로그와 소스코드가 로컬 머신에 안전하게 머무르기 때문에, 
              데이터 유출을 극도로 경계하는 핀테크, 헬스케어, 보안 스타트업들이 클라우드 기반 도구 대신 채택할 수 있는 완벽한 오픈소스 대안으로 급부상하고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="zap"></i> 5. 키커: 오케스트레이터가 된 인간, 협동하는 지능의 네트워크
            </h3>
            <p>
              소프트웨어 개발의 본질이 '코드를 직접 타이핑하는 노동'에서 '지능 에이전트들의 오케스트라를 지휘하는 총감독'으로 진화하고 있다. 
              OpenBot은 특정 빅테크의 폐쇄적 생태계에 갇히지 않고, 현존하는 가장 강력한 두뇌들을 내 입맛대로 조합하여 협력시키는 열린 플랫폼의 힘을 웅변한다. 
              미래의 소프트웨어 회사는 빌딩이 아니라, 바로 당신의 로컬 데스크톱 창 안에서 깨어나고 있다.
            </p>

          </div> <!-- .editorial-content -->

          <!-- 기사 하단 고시인성 액션 링크 바 -->
          <div class="article-links-bar">
            <a href="https://www.youtube.com/results?search_query=OpenBot+Nightly+Labs+Local+AI+Teammates+Workspace" target="_blank" rel="noopener noreferrer" class="project-link youtube">
              <i data-lucide="play" style="width:16px;height:16px;fill:currentColor;"></i> 유튜브 관련 리뷰보기
            </a>
            <a href="https://github.com/nightly-labs/openbot" target="_blank" rel="noopener noreferrer" class="project-link github">
              <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
            </a>
          </div>

        </div> <!-- .article-detail -->
      </article>
"""
