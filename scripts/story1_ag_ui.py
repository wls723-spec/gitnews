# -*- coding: utf-8 -*-
# Story 1: ag-ui-protocol/ag-ui (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] ag-ui-protocol/ag-ui : COVER STORY                -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_ag_ui.jpg" alt="AG-UI Protocol Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔌 에이전트-앱 표준 프로토콜 1.0</span>
              <span class="platform-tag">GitHub Trending &amp; dojo.ag-ui.com</span>
              <span class="platform-tag">ag-ui-protocol / ag-ui</span>
            </div>

            <h2 class="main-lead-headline">
              <span id="hero-title">에이전트 시대의 HTTP가 열렸다: 구글·MS·아마존·오라클이 뭉친 오픈 프로토콜 'AG-UI 1.0'</span>
            </h2>

            <div class="article-subheadline">
              MCP(도구)와 A2A(에이전트 간 협업)의 마지막 퍼즐을 채우며, 어떤 AI 에이전트든 웹·모바일·터미널 UI와 양방향 이벤트 스트림으로 직결하는 오픈 표준 (18,900스타)
            </div>
            <p class="article-snippet">
              에이전트가 도구를 부르고 상태를 바꾸며 인간 승인을 기다리는 동안, 프론트엔드 개발자들은 프레임워크마다 제각각인 JSON 스트리밍 포맷을 일일이 땜질하느라 진땀을 빼왔습니다. 하루 790스타를 추가하며 누적 18,900스타를 돌파한 <strong>ag-ui-protocol/ag-ui</strong>는 정식 1.0 동결 스펙과 JSON Schema 기반 TypeScript·Python·.NET SDK를 앞세워 LangChain, CrewAI, Google ADK, Microsoft Agent Framework를 단 하나의 양방향 이벤트 파이프로 묶어냈습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 챗봇을 넘자마자 무너진 '프론트엔드 배관 공사'의 악몽
            </h3>
            <p>
              2025년 이후 수많은 엔지니어링 팀이 LangGraph, CrewAI, Google ADK 같은 에이전트 프레임워크를 도입했지만, 프로덕션 앱에 붙이는 순간 동일한 장벽에 부딪혔다. 전통적인 REST API의 요청-응답 모델이나 단순 텍스트 SSE(Server-Sent Events)로는 에이전트 시대의 인터랙션을 담을 수 없었기 때문이다.
            </p>
            <p>
              에이전트는 답변 도중 갑자기 도구를 호출하고, 클라이언트와 공유 중인 캔버스 상태를 부분 수정(JSON Patch)하며, 위험한 작업 앞에서는 실행을 멈추고 인간 승인(Human-in-the-Loop)을 요청한 뒤 서브에이전트까지 분기시킨다. 그 결과 백엔드 프레임워크가 바뀔 때마다 프론트엔드 스트리밍 파서를 통째로 다시 짜야 하는 기형적인 N×M 통합 비용이 발생했다. 이 파편화를 종식시키며 일간 790스타(누적 18,900스타)를 쓸어 담은 프로젝트가 바로 <strong>ag-ui-protocol/ag-ui</strong>다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: MCP와 A2A를 완성하는 '에이전트-사용자' 3축 표준의 마지막 조각
            </h3>
            <p>
              AG-UI 1.0 발표가 단순한 SDK 업데이트가 아니라 산업 분기점인 이유는, 이제 AI 에이전트 스택의 3대 통신 프로토콜이 완전히 정렬되었기 때문이다. 도구는 <strong>MCP</strong>가, 에이전트 간 협업은 <strong>A2A</strong>가, 그리고 에이전트와 실제 사용자가 만나는 앱 인터페이스는 <strong>AG-UI</strong>가 맡는 삼각 편대가 굳어지고 있다.
            </p>

            <div class="editorial-quote">
              <p>
                "에이전트는 요청/응답 모델에 맞지 않는다. AG-UI는 프레임워크별 커스텀 배선을 <strong>단 하나의 양방향 타입드 이벤트 스트림으로 대체한다.</strong> 백엔드를 어떤 프레임워크로 교체하든 웹, 모바일, 터미널, Slack 클라이언트는 단 한 줄도 바꿀 필요가 없다."
              </p>
              <small>— AG-UI 1.0 공식 아키텍처 명세 (JSON Schema 동결 스펙 &amp; MIT 라이선스)</small>
            </div>

            <p>
              실제로 AG-UI는 특정 벤더의 폐쇄형 위젯이 아니라 구글, 마이크로소프트, 아마존(AWS Strands), 오라클 및 CopilotKit 커뮤니티가 동참한 개방형 런타임 프로토콜이다. 심지어 구글의 <code>A2UI</code>나 <code>Open-JSON-UI</code> 같은 생성형 UI(Generative UI) 명세 페이로드까지 AG-UI 이벤트 스트림에 실어 나를 수 있도록 설계되었다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: JSON Schema 동결 스펙과 양방향 이벤트 루프
            </h3>
            <p>
              단 30줄의 FastAPI 서버와 TypeScript <code>HttpAgent</code> 클라이언트만으로 이기종 프레임워크를 연결할 수 있는 AG-UI 1.0의 핵심 메커니즘은 세 가지 기술적 기둥으로 작동한다:
            </p>
            <ul>
              <li><strong>단일 진실 원천(JSON Schema) 기반 다중 언어 SDK 코드 생성:</strong> AG-UI 1.0은 동결된 프로토콜 명세를 JSON Schema로 엄격히 정의하고, 여기에서 TypeScript(<code>@ag-ui/core</code>, <code>@ag-ui/client</code>), Python(<code>ag-ui-protocol</code>), .NET SDK를 자동 생성한다. 0.x 에이전트와 1.0 클라이언트 간 양방향 하위 호환성도 보장한다.</li>
              <li><strong>생명주기·메시지·도구·상태 델타를 아우르는 타입드 이벤트:</strong> 에이전트는 <code>RunStartedEvent</code>, <code>TextMessageStart/Content/EndEvent</code>, 도구 호출 스트리밍 이벤트, 상태 스냅샷 및 델타 이벤트를 <code>EventEncoder</code>를 통해 SSE 또는 바이너리 스트림으로 방출한다.</li>
              <li><strong>양방향 컨텍스트 주입(<code>RunAgentInput</code> &amp; Frontend Tools):</strong> 클라이언트는 단순 채팅 문자열만 보내는 것이 아니라 현재 앱 상태, 대화 스레드(<code>thread_id</code>), 그리고 브라우저 측에 등록된 프론트엔드 도구 목록을 매 실행마다 전달한다. 덕분에 에이전트가 클라이언트 UI 상태를 직접 읽고 사용자 승인 후 후속 턴을 이어간다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">에이전트 3대 프로토콜 스택 &amp; AG-UI 1.0 양방향 이벤트 아키텍처</span>
                <span class="schematic-badge">AG-UI 1.0 Spec · MIT</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Agent Backends (Any Framework)</div>
                  <div class="schematic-desc">
                    LangGraph · CrewAI · Mastra<br>
                    Google ADK · MS Agent Framework<br>
                    Pydantic AI · AWS Strands<br>
                    MCP(도구) &amp; A2A(에이전트 협업) 연동
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">AG-UI 1.0 Event Stream</div>
                  <div class="schematic-desc">
                    JSON Schema 동결 명세 &amp; <code>EventEncoder</code><br>
                    <code>RunStarted</code> / <code>TextMessageContent</code><br>
                    Tool Call Streaming · State Snapshot/Delta<br>
                    Generative UI (A2UI · MCP Apps) 전송
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">User Apps (Any Client)</div>
                  <div class="schematic-desc">
                    Web (React/CopilotKit) · Mobile<br>
                    CLI Terminal · Slack / Teams<br>
                    Human-in-the-Loop 중단 및 승인<br>
                    <code>HttpAgent</code> 양방향 상태 동기화
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">AG-UI 공식 프로토콜 문서 &amp; SDK 포털 (docs.ag-ui.com)</span>
              </div>
              <img src="../assets/images/demo_ag_ui.png" alt="AG-UI Protocol Official Documentation and SDK Portal" class="showcase-img">
              <p class="showcase-caption">
                ▲ docs.ag-ui.com 실구동 포털 화면: TypeScript·Python·.NET SDK와 동결된 1.0 프로토콜 스펙, 그리고 MCP·A2A·AG-UI 3대 에이전트 프로토콜 아키텍처 문서를 한눈에 탐색할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 표준 전쟁: 프레임워크 종속을 깨는 미들웨어 승부
            </h3>
            <p>
              과거 OpenAI Assistants API나 특정 클라우드 벤더의 독점 챗 위젯은 개발자가 한 번 UI를 붙이면 백엔드 모델과 오케스트레이션 엔진을 갈아타기 어렵게 만드는 강력한 '프론트엔드 락인(Lock-in)' 역할을 했다.
            </p>
            <ul>
              <li><strong>벤더 중립적 MIT 오픈 거버넌스:</strong> AG-UI는 프로토콜 코어를 MIT 라이선스로 전면 개방하고, <code>dojo.ag-ui.com</code>에 모든 주요 프레임워크의 레퍼런스 어댑터를 공개해 특정 기업의 사유 표준화를 원천 차단했다.</li>
              <li><strong>실시간 UI 경쟁의 재편:</strong> 백엔드 통신 규약이 표준화되면서, 이제 AI 앱의 승부처는 '스트리밍 파서 유지보수'가 아니라 도메인 맞춤형 생성형 UI, 협업 캔버스, 승인 워크플로우를 얼마나 정교하게 설계하느냐로 이동하고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 브라우저와 웹 서버를 이었던 HTTP처럼
            </h3>
            <p>
              웹 혁명이 폭발할 수 있었던 이유는 HTML과 HTTP라는 단순한 개방형 약속 덕분에 어떤 서버도 어떤 브라우저와 대화할 수 있었기 때문이다.
            </p>
            <p>
              MCP가 에이전트에게 손발을 달아주고 A2A가 에이전트끼리의 언어를 통일했다면, AG-UI 1.0은 마침내 에이전트를 인간의 화면으로 데려오는 공용어다. 백엔드 프레임워크 전쟁이 아무리 치열하게 바뀌어도, 사용자 앞단에서 살아 움직이는 표준 파이프 하나를 선점한 쪽이 차세대 AI 애플리케이션의 기본 배관이 될 것이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=AG-UI+protocol+agent+user+interaction" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://dojo.ag-ui.com" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 Dojo 라이브 데모
              </a>
              <a href="https://github.com/ag-ui-protocol/ag-ui" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
