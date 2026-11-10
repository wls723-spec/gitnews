# -*- coding: utf-8 -*-
# Story 2: homeassistant-ai/ha-mcp (홈 어시스턴트 공식 MCP 서버)

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 2] homeassistant-ai/ha-mcp : 로컬 스마트홈 AI 혁신 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_hamcp.jpg" alt="Home Assistant MCP Server" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="home" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #2</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 빅테크 클라우드 종속 탈출</span>
              <span class="platform-tag">GitHub Trending & 6.5k Stars</span>
              <span class="platform-tag">homeassistant-ai / ha-mcp</span>
            </div>
            
            <h2 class="article-headline">
              빅테크 클라우드 없이 내 집을 지휘하는 로컬 AI 집사 — 'ha-mcp', Claude와 ChatGPT를 87개 스마트홈 도구로 직결하다
            </h2>

            <div class="article-subheadline">
              '인터넷 끊겨도 작동하는 스마트홈' 철학과 FastMCP의 결합: 조명·냉난방·CCTV·에너지 센서를 AI 에이전트와 제로 레이턴시로 묶어낸 오픈소스 혁명
            </div>
            <p class="article-snippet">
              아마존 알렉사와 구글 홈의 일방적인 유료 구독화와 빈번한 클라우드 다운타임에 질린 사용자들이 오픈소스 홈 어시스턴트(Home Assistant)로 대거 망명하고 있습니다. 오늘 공개된 'ha-mcp'는 앤스로픽이 제정한 모델 컨텍스트 프로토콜(MCP)을 기반으로, 87개 이상의 스마트홈 엔티티 제어 도구를 Claude 및 ChatGPT 데스크톱에 실시간 공급하는 공식 인프로세스 통합 서버입니다. 외부 클라우드 통신 없이 폐쇄망에서도 자율 스마트홈 에이전트를 가동합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 클라우드가 끊기면 불도 켜지 못하는 스마트홈의 비극
            </h3>
            <p>
              "죄송합니다. 현재 네트워크에 연결할 수 없습니다." 
              퇴근 후 집에 들어와 불을 켜달라고 외쳤을 때, 거실 스피커에서 흘러나오는 이 기계음만큼 허탈한 순간은 없다. 
              수백만 원을 들여 스마트 조명과 온도조절기, 도어록을 설치했건만, 
              아마존 AWS나 구글 클라우드에 장애가 발생하면 집 전체가 거대한 '먹통 깡통'으로 전락하는 현실.
            </p>
            <p>
              해커뉴스에서 오늘 600개 이상의 업보트를 받으며 폭발적 공감을 산 글 
              <em>"Smart home devices should work without the internet(스마트홈은 인터넷 없이도 작동해야 한다)"</em>은 
              이러한 클라우드 독점의 취약점을 정면으로 겨냥했다. 
              그리고 같은 시각, 깃허브 트렌딩 1위에 오르며 6,500개의 스타를 돌파한 <strong>ha-mcp</strong>는 
              이 분노에 대한 가장 완벽한 기술적 응답을 제시했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 거실의 IoT 기기들이 LLM의 네이티브 팔다리가 되다
            </h3>
            <p>
              지금까지 AI와 스마트홈의 결합은 실망스러웠다. 
              빅테크 스피커는 사전에 녹음된 수십 개의 정형화된 명령어만 알아들었고, 
              조금만 복잡한 맥락("비가 오니까 거실 창문 닫고 제습기 켜줘, 그리고 30분 뒤에 조명 어둡게 해줘")을 던지면 오류를 뱉어냈다.
            </p>

            <div class="editorial-quote">
              <p>
                "그동안 우리는 스마트홈을 위해 빅테크 클라우드에 사생활을 팔아넘겨야 했다. 
                <strong>ha-mcp는 FastMCP 프로토콜을 이용해 홈 어시스턴트 내부에서 87개의 초정밀 센서와 액추에이터 제어 함수를 직접 익스포트한다.</strong> 
                Claude Desktop이나 로컬 LLM은 단 한 번의 프롬프트로 집안의 모든 상태를 파악하고 수학적 오차 없이 가전을 제어한다."
              </p>
              <small>— Home Assistant AI 통합 코어 팀 릴리즈 노트</small>
            </div>

            <p>
              사용자가 Claude Code나 로컬 Ollama 모델에게 "오늘 밤 거실 전기세 절감 모드로 전환하고, 고양이 급식기 상태 확인해줘"라고 말하면, 
              ha-mcp는 즉시 실시간 전력 사용량 엔티티와 서보 모터 센서를 조회해 최적의 자동화 스크립트를 작성하고 실행한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 메커니즘: FastMCP 런타임과 87개 제로 오버헤드 툴셋
            </h3>
            <p>
              ha-mcp의 기술적 완성도는 홈 어시스턴트 v2026.11 코어 아키텍처와 완벽하게 밀착되어 있다:
            </p>
            <ul>
              <li><strong>인프로세스(In-Process) FastMCP 아키텍처:</strong> 별도의 외부 프록시나 무거운 노드 프로세스 없이, 홈 어시스턴트 내부 파이썬 런타임에서 직접 FastMCP 서버를 구동하여 마이크로초 단위의 반응 속도 구현.</li>
              <li><strong>87개 동적 함수 호출(Tool Calling) 인터페이스:</strong> `ha_call_service`, `ha_get_state`, `ha_render_template`, `ha_subscribe_events` 등 홈 어시스턴트의 모든 REST/WebSocket API를 엄격한 타입 안정성을 갖춘 MCP 도구로 변환.</li>
              <li><strong>에이전트 보호 샌드박스:</strong> 도어록 해제나 보안 알람 해제 등 민감한 물리적 제어 명령은 에이전트 임의 실행을 차단하고 2단계 로컬 승인 절차를 강제하는 안전 가드레일 내장.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">ha-mcp 로컬 자율 스마트홈 오케스트레이션 파이프라인</span>
                <span class="schematic-badge">MCP Protocol Flow</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">AI Client Layer</div>
                  <div class="schematic-desc">
                    Claude Desktop / Cursor<br>
                    로컬 LLM (Ollama, llama.cpp)<br>
                    자연어 의도 파싱 & 다단계 추론
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">ha-mcp Server (FastMCP)</div>
                  <div class="schematic-desc">
                    87개 도구 자동 발견 및 노출<br>
                    보안 가드레일 & 권한 승인 검증<br>
                    로컬 인프로세스 초저지연 브리지
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Home Assistant Core</div>
                  <div class="schematic-desc">
                    Zigbee, Z-Wave, Matter 기기<br>
                    실시간 이벤트 버스 & 상태 저장소<br>
                    100% 오프라인 로컬 작동 보장
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Home Assistant ha-mcp 공식 문서 및 대시보드 런타임</span>
              </div>
              <img src="../assets/images/demo_hamcp.png" alt="Home Assistant ha-mcp Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ homeassistant-ai.github.io/ha-mcp 라이브 뷰: HACS 원클릭 마켓플레이스 통합과 Claude 데스크톱 연동을 통해 87개의 스마트홈 액추에이터 도구가 실시간 바인딩되는 공식 아키텍처 인터페이스.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 플랫폼 주권: 거대 구독 모델의 붕괴
            </h3>
            <p>
              아마존과 구글은 최근 알렉사와 구글 어시스턴트에 생성형 AI를 탑재한다는 명목으로 월 10~20달러의 유료 구독 요금제를 도입하려 하고 있다. 
              그러나 ha-mcp의 등장은 이러한 빅테크의 '스마트홈 유료 구독 인질극'을 단번에 무력화한다.
            </p>
            <p>
              사용자는 이미 보유한 고성능 LLM 구독(Claude Pro 등)이나 심지어 집안의 RTX 그래픽카드에서 돌아가는 무료 오픈소스 모델을 
              단 하나의 오픈소스 플러그인으로 홈 어시스턴트에 직결할 수 있게 되었다. 
              가장 내밀한 공간인 가정의 프라이버시 데이터를 외부 서버에 단 한 조각도 전송하지 않는다는 안도감은 어떤 상용 서비스도 제공할 수 없는 절대적 해자다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 내 집의 열쇠는 내 손에
            </h3>
            <p>
              집이란 세상에서 가장 안전하고 사적인 요새여야 한다. 
              외부 클라우드의 허락을 받아야만 불을 켜고 문을 잠그는 기형적인 구조는 스마트홈의 미래가 될 수 없다. 
              오픈 프로토콜 MCP와 완전한 로컬 제어가 만난 ha-mcp는, 
              진정한 스마트홈이란 인터넷 회선이 끊어지는 날에도 따뜻하게 나를 맞아주는 공간임을 명료하게 일깨우고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Home+Assistant+MCP+Claude+integration" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://homeassistant-ai.github.io/ha-mcp/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> ha-mcp 공식 문서 바로가기
              </a>
              <a href="https://github.com/homeassistant-ai/ha-mcp" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
