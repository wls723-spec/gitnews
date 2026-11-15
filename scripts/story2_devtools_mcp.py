# -*- coding: utf-8 -*-
# Story 2: ChromeDevTools/chrome-devtools-mcp

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] ChromeDevTools/chrome-devtools-mcp               -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_devtools_mcp.jpg" alt="Chrome DevTools MCP Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> CHROME OSS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dbeafe; border-color:#2563eb; color:#1e40af;">🔍 에이전트에게 크롬 개발자 도구를</span>
              <span class="platform-tag">GitHub Trending &amp; developer.chrome.com</span>
              <span class="platform-tag">ChromeDevTools / chrome-devtools-mcp</span>
            </div>
            
            <h2 class="article-headline">
              "눈 감고 프론트엔드 짜던 AI 시대는 끝났다" — 구글 공식 'Chrome DevTools MCP', 코딩 에이전트에게 실시간 브라우저 디버거를 쥐여주다
            </h2>

            <div class="article-subheadline">
              단순 스크린샷 봇을 넘어 Performance Trace 기록, CrUX 실사용자 데이터 병합, 소스맵 기반 콘솔 역추적까지 56,878 스타를 돌파한 Google Chrome 팀의 공식 MCP 서버 &amp; CLI
            </div>
            <p class="article-snippet">
              지금까지 AI 코딩 에이전트는 React 코드를 고친 뒤 "잘 작동할 겁니다"라고 추측만 할 뿐, 정작 브라우저에서 레이아웃이 깨지거나 메모리 누수가 발생해도 볼 방법이 없었습니다. 구글 Chrome DevTools 팀이 직접 내놓은 `chrome-devtools-mcp`는 Antigravity, Claude Code, Cursor, Gemini CLI 같은 에이전트에 실제 Chrome 개발자 도구의 두뇌를 MCP 프로토콜과 CLI로 직결하며 프론트엔드 자동 디버깅의 표준을 새로 쓰고 있습니다.
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
              <i data-lucide="flame"></i> 1. 리드: "빌드는 성공했는데 화면이 하얘요" — 맹인 코더 AI의 한계
            </h3>
            <p>
              프론트엔드 개발자들이 AI 에이전트를 쓰며 가장 답답해하는 순간은 "컴파일은 통과했는데 실제 브라우저를 열어보면 버튼이 겹치고 콘솔에 CORS 에러가 쏟아지는 상황"이다. 기존에도 Playwright나 Puppeteer로 스크린샷을 찍어주는 서드파티 툴은 많았지만, 정작 시니어 웹 엔지니어가 Chrome DevTools(F12)를 열어 확인하는 핵심 진단 데이터—네트워크 워터폴, 소스맵이 복원된 스택 트레이스, LCP 병목 트레이스, 힙 메모리 누수—에는 접근하지 못했다.
            </p>
            <p>
              오늘 하루 718개의 스타를 추가하며 누적 <strong>56,878 스타</strong>라는 압도적 지지를 받고 있는 <strong>ChromeDevTools/chrome-devtools-mcp</strong>는 브라우저 엔진 제조사인 구글 크롬 팀이 직접 "에이전트 시대의 F12 패널"을 MCP(Model Context Protocol) 표준으로 봉인 해제한 사건이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 실험실(Lab) 트레이스와 실사용자(CrUX) 필드를 한 번에 읽는 에이전트
            </h3>
            <p>
              `chrome-devtools-mcp`의 진짜 위력은 단순히 페이지를 클릭하고 캡처하는 '브라우저 원격 조종기'가 아니라는 데 있다. 이 도구는 Chrome DevTools Frontend의 트레이스 분석 엔진을 내장해, 에이전트가 직접 성능 프로파일을 녹화하고 병목 구간을 스스로 진단하게 만든다.
            </p>

            <div class="editorial-quote">
              <p>
                "코딩 에이전트가 Chrome DevTools를 직접 구동해 <strong>성능 트레이스를 기록하고 실행 가능한 최적화 인사이트를 추출하며, Google CrUX API를 통해 실제 사용자 경험(Field Data)과 실험실(Lab Data) 수치를 나란히 대조</strong>한다."
              </p>
              <small>— ChromeDevTools/chrome-devtools-mcp 공식 설계 및 아키텍처 문서</small>
            </div>

            <p>
              여기에 구글은 `a11y-debugging`(접근성 감사), `cookie-debugging`(쿠키·세션·인증 추적), `debug-optimize-lcp`(LCP 최적화), `memory-leak-debugging`(메모리 누수 추적) 등 **7종의 전용 Agent Skills**까지 함께 패키징해, 에이전트가 도구를 어떻게 조합해 원인을 좁혀가야 하는지 시니어 엔지니어의 디버깅 순서까지 통째로 이식했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Puppeteer 액션 제어 + DevTools 트레이스 엔진 + CrUX 텔레메트리 결합
            </h3>
            <p>
              `chrome-devtools-mcp`가 방대한 브라우저 내부 상태를 컨텍스트 낭비 없이 안정적으로 에이전트에게 전달하는 구조는 크게 세 층위로 돌아간다:
            </p>
            <ul>
              <li><strong>MCP 서버와 `chrome-devtools` CLI 이중 인터페이스:</strong> `npx -y chrome-devtools-mcp@latest`로 MCP 클라이언트에 즉시 붙이거나, 전역 설치된 `chrome-devtools` CLI(`navigate_page`, `take_screenshot`, `stop`)로 쉘 스크립트에서 제어할 수 있다. 도구 컨텍스트를 줄이고 싶을 때는 `--slim` 플래그로 최소 핵심 도구만 노출한다.</li>
              <li><strong>실행 자동 대기 &amp; 소스맵 콘솔 복원:</strong> Puppeteer 기반 액션 자동화가 DOM 안정화와 결과 대기를 자동으로 처리하며, 번들링·난독화된 프로덕션 코드에서 발생한 콘솔 에러도 소스맵(Source Map)을 적용한 원본 스택 트레이스로 복원해 에이전트가 정확한 소스 라인을 고치게 돕는다.</li>
              <li><strong>유연한 실행 격리 및 프라이버시 제어:</strong> `--headless`, `--isolated` 플래그로 일회성 샌드박스 브라우저를 띄우거나 실행 중인 Chrome 인스턴스의 WebSocket·Android 디버깅 포트에 연결한다. 사내 민감 환경에서는 `--no-performance-crux`와 `--no-usage-statistics` 플래그로 외부 CrUX 전송 및 사용 통계 수집을 완전히 차단할 수 있다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Chrome DevTools MCP 에이전트 폐쇄루프 디버깅 아키텍처</span>
                <span class="schematic-badge">MCP + DevTools Frontend + Puppeteer</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Agent &amp; Skill Layer</div>
                  <div class="schematic-desc">
                    Antigravity · Claude · Cursor · Gemini<br>
                    7종 특화 디버깅 Skills 탑재<br>
                    (`debug-optimize-lcp`, `memory-leak` 등)<br>
                    `--slim` 컨텍스트 경량 모드 지원
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">MCP Server &amp; CLI Bridge</div>
                  <div class="schematic-desc">
                    Puppeteer 기반 안정적 액션/대기 제어<br>
                    DevTools Frontend 성능 트레이스 분석<br>
                    소스맵 복원 콘솔 &amp; 네트워크 패킷 감시<br>
                    CrUX API 실사용자 지표 교차 검증
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Live Chrome Target</div>
                  <div class="schematic-desc">
                    Chrome / Chrome for Testing 제어<br>
                    `--headless` · `--isolated` 격리 실행<br>
                    실행 중 브라우저 WebSocket 및 Android 연결<br>
                    `--no-performance-crux` 보안 옵션
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Chrome for Developers 공식 문서 포털 (developer.chrome.com/docs/devtools/agents)</span>
              </div>
              <img src="../assets/images/demo_devtools_mcp.png" alt="Chrome DevTools for Agents Official Documentation" class="showcase-img">
              <p class="showcase-caption">
                ▲ developer.chrome.com/docs/devtools/agents 화면: 구글이 Antigravity 2.0, Gemini CLI, Claude Code, Cursor 등 AI 에이전트에게 라이브 브라우저 검사·성능 트레이싱 권한을 개방하는 공식 통합 가이드를 제공한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 보안 경고: QA와 APM 생태계의 재편, 그리고 MCP 프롬프트 인젝션
            </h3>
            <p>
              구글이 직접 브라우저 디버깅을 오픈소스 MCP 표준(Apache-2.0)으로 풀어버리면서, 기존에 "AI로 웹페이지 성능이나 접근성을 점검해준다"던 수많은 경량 QA·성능 감사 SaaS들의 해자가 급격히 옅어지고 있다. 개발팀의 IDE 안의 에이전트가 추가 과금 없이 크롬 본체의 트레이스 엔진을 바로 호출할 수 있게 되었기 때문이다.
            </p>
            <ul>
              <li><strong>치명적 보안 경계(Disclaimer):</strong> `chrome-devtools-mcp`는 브라우저 내부 DOM·쿠키·로컬 스토리지·네트워크 페이로드 전체를 MCP 클라이언트에 노출한다. 구글은 공식 문서를 통해 개인·금융 정보가 로그인된 일반 프로필이 아닌 격리된 테스트 프로필에서 구동할 것을 강력히 경고한다.</li>
              <li><strong>브라우저 서브에이전트(Subagent)의 표준 부품화:</strong> Gemini CLI의 브라우저 서브에이전트나 Antigravity 2.0처럼, 이제 차세대 AI 코딩 툴들은 자체 크롤러를 짜는 대신 `chrome-devtools-mcp`를 기본 내장 부품으로 탑재해 "코드 수정 → 브라우저 실행 → LCP/메모리 검증 → 재수정"의 자율 루프를 완성하고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 코딩 에이전트에게 '컴파일러' 다음으로 필요한 것은 '실시간 브라우저'였다
            </h3>
            <p>
              백엔드 코드가 단위 테스트를 통과하는 것으로 검증된다면, 웹 애플리케이션의 진실은 오직 살아 숨 쉬는 브라우저 런타임 안에서만 드러난다.
            </p>
            <p>
              수천만 웹 개발자의 밤샘 디버깅을 함께해온 F12 개발자 도구가 이제 인간이 아닌 AI 에이전트의 손에 쥐어졌다. 코드를 짜는 속도가 무한대로 빨라진 2026년, 소프트웨어 품질의 마지막 보루는 결국 브라우저 안에서 스스로를 검증할 줄 아는 에이전트의 손끝에 달려 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=chrome-devtools-mcp+Google" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://developer.chrome.com/docs/devtools/agents" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 가이드 방문
              </a>
              <a href="https://github.com/ChromeDevTools/chrome-devtools-mcp" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
