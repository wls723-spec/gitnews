# -*- coding: utf-8 -*-
# Story 2: firecrawl/firecrawl

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] firecrawl/firecrawl                              -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_firecrawl.jpg" alt="Firecrawl Web Data Infrastructure Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="flame" style="width:12px;height:12px;fill:#fff;"></i> AGENT DATA INFRA</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ffedd5; border-color:#ea580c; color:#9a3412;">🔥 웹 전체를 에이전트용 지식 파이프라인으로</span>
              <span class="platform-tag">GitHub Trending &amp; firecrawl.dev</span>
              <span class="platform-tag">firecrawl / firecrawl</span>
            </div>

            <h2 class="article-headline">
              로컬 단일 바이너리부터 550개 데이터 프로바이더까지: AI 에이전트의 눈과 손을 완성한 'Firecrawl'
            </h2>

            <div class="article-subheadline">
              DB·컨테이너 없이 내 PC에서 <code>localhost:3002</code>로 즉시 도는 <code>firecrawl-local</code>, API 키 없는 월 1,000크레딧 Keyless, 그리고 브라우저 직접 조작 <code>Interact</code>까지 (+795스타/일, 누적 204,133스타)
            </div>
            <p class="article-snippet">
              JavaScript로 무장한 현대 웹페이지를 긁어오려다 봇 차단과 깨진 DOM 앞에서 좌절하는 것은 모든 AI 에이전트 개발자의 통과의례였습니다. 오늘 하루 795스타를 보태며 누적 20만4천 스타를 돌파한 <strong>firecrawl/firecrawl</strong>은 단순한 HTML-to-Markdown 변환기를 넘어섰습니다. Rust 기반 로컬 단일 바이너리(<code>firecrawl-local</code>)로 MCP와 로컬 API를 1초 만에 띄우고, 클라우드에서는 실시간 브라우저 조작(<code>Interact</code>)과 550여 개 데이터 소스 허브 'Alexandria'까지 단일 API로 통합했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: <code>cargo install firecrawl-local</code> 한 줄이 바꿔놓은 개발자의 아침
            </h3>
            <p>
              불과 1년 전만 해도 사내 AI 에이전트에 웹 크롤링 기능을 붙이려면 Redis 큐와 PostgreSQL, Playwright 워커 풀을 Docker Compose로 엮고 프록시 로테이션과 싸워야 했다. 그런데 지금 개발자들은 터미널에 단 두 줄만 입력한다. <code>cargo install firecrawl-local</code>과 <code>firecrawl-local init</code>.
            </p>
            <p>
              순식간에 내 머신에 설치된 Claude Code, Cursor, Windsurf, Gemini CLI, Codex 설정 파일이 백업되고 로컬 MCP 서버가 꽂힌다. <code>firecrawl-local serve</code>를 치면 포트 <code>3002</code>에서 상용 Firecrawl v2 API와 100% 호환되는 엔드포인트가 API 키도, 데이터베이스도, 도커 컨테이너도 없이 즉시 살아난다. 오늘 하루 795스타가 추가되며 누적 204,133스타에 도달한 <strong>firecrawl/firecrawl</strong>이 왜 에이전트 시대의 사실상 표준 '웹 지식 인프라'로 불리는지 단적으로 보여주는 장면이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "스크래핑"에서 "자율 웹 상호작용 + 550개 데이터 허브"로의 도약
            </h3>
            <p>
              LLM에게 날것의 HTML을 그대로 먹이는 것은 토큰 낭비이자 환각의 지름길이다. Firecrawl의 진화는 3단계로 웹 데이터의 판을 바꿨다. 첫째, 96%의 실제 동적 웹을 뚫고 P95 3.4초 만에 토큰 효율적인 마크다운과 구조화 JSON으로 정제한다. 둘째, 단순 읽기(<code>Scrape/Crawl/Map</code>)를 넘어 <code>Interact</code> API로 에이전트가 페이지 안에서 검색어를 입력하고 버튼을 클릭하게 만든다. 셋째, <strong>Firecrawl Alexandria</strong>를 통해 오픈 웹 크롤링을 넘어 550개 이상의 전문 데이터 프로바이더를 단일 호출로 연결했다.
            </p>

            <div class="editorial-quote">
              <p>
                "가입도 API 키도 필요 없는 <strong>Firecrawl Keyless</strong>로 매달 1,000크레딧을 무료로 열고, 내 머신의 Chrome과 <code>FIRECRAWL_CLOUD=off</code> 옵션만으로도 모든 스크래핑과 PDF·오피스 문서 파싱을 100% 로컬에서 완결할 수 있다."
              </p>
              <small>— Firecrawl v2.5+ 하이브리드 로컬·클라우드 아키텍처 명세 (AGPL-3.0)</small>
            </div>

            <p>
              여기에 URL조차 주지 않고 <em>"Notion의 요금제를 찾아 구조화된 JSON으로 가져와"</em>라고 프롬프트만 던지면 에이전트가 스스로 검색하고 탐색해 출처(<code>sources</code>)까지 반환하는 <code>/v2/agent</code> 엔드포인트가 더해지며 검색 엔진과 스크래퍼의 경계가 완전히 허물어졌다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 로컬-클라우드 하이브리드 파이프라인 해부
            </h3>
            <p>
              Firecrawl 저장소(<code>apps/local</code> 및 <code>apps/api</code>)는 개인 개발자의 노트북부터 대규모 프로덕션 클러스터까지 동일한 SDK 코드가 매끄럽게 이식되도록 3단 하이브리드 아키텍처를 취한다:
            </p>
            <ul>
              <li><strong>무의존 Rust 바이너리 (<code>firecrawl-local</code>):</strong> 정적 페이지는 즉각 파싱하고, JavaScript 렌더링이 필요한 사이트는 사용자 PC에 이미 설치된 Chrome/Chromium을 재사용하며 PDF 및 Office 문서까지 로컬에서 직접 분해한다.</li>
              <li><strong>자동 폴백 &amp; 에어갭 모드 (<code>FIRECRAWL_CLOUD=off</code>):</strong> 로컬에서 막힌 단일 페이지 스크래핑만 무계정 Cloud로 우회(결과에 <code>"source": "firecrawl-cloud"</code> 명시)하거나, 보안이 민감한 사내망에서는 환경변수 하나로 외부 통신을 완벽히 차단한다.</li>
              <li><strong>상태 유지 인터랙션 &amp; Alexandria 허브:</strong> <code>scrape_id</code> 기반으로 세션을 붙잡아 자연어 프롬프트로 DOM을 조작(<code>interact</code>)하고, <code>liveViewUrl</code>로 실시간 관제하며 550+ 외부 데이터 프로바이더를 통합 질의한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Firecrawl 하이브리드 웹 지식 인프라 아키텍처</span>
                <span class="schematic-badge">AGPL-3.0 · Local Rust Binary + Cloud v2 API</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Firecrawl Local</div>
                  <div class="schematic-desc">
                    <code>cargo install firecrawl-local</code><br>
                    <code>init</code> → Claude/Cursor/Codex MCP 자동 주입<br>
                    <code>localhost:3002</code> (DB·Docker 제로)<br>
                    로컬 Chrome + PDF/Office 파싱
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. v2 Action &amp; Agent Engine</div>
                  <div class="schematic-desc">
                    <code>Scrape / Crawl / Map</code> (P95 3.4s)<br>
                    <code>Interact</code> 세션 기반 브라우저 클릭·입력<br>
                    <code>Agent</code> URL 없는 자율 웹 탐색<br>
                    Pydantic/Zod 스키마 기반 구조화 JSON
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Cloud &amp; Alexandria</div>
                  <div class="schematic-desc">
                    <strong>Keyless:</strong> 가입 없이 월 1,000크레딧<br>
                    <strong>Alexandria:</strong> 550+ 전문 데이터 허브<br>
                    <code>apps/api</code> 자체 큐·워커 셀프호스팅<br>
                    동적 웹 96% 커버리지 &amp; 마크다운 정제
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Firecrawl 공식 웹 인터페이스 &amp; 지식 인프라 플랫폼</span>
              </div>
              <img src="../assets/images/demo_firecrawl.png" alt="Firecrawl Official Interface Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ firecrawl.dev 공식 플랫폼 실화면: 단일 API와 로컬 바이너리를 통해 웹 스크래핑, 실시간 브라우저 상호작용(Interact), 550+ 데이터 프로바이더(Alexandria)를 통합 제공한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 검색 독점 기업들의 '폐쇄형 웹 인덱스'에 맞선 오픈 게이트웨이
            </h3>
            <p>
              AI 에이전트가 웹의 최대 소비자로 떠오르면서, 대형 검색 엔진들은 API 접근 비용을 올리고 크롤링 봇을 봉쇄하며 자체 AI 검색 답변으로 트래픽을 가두고 있다. Firecrawl이 AGPL-3.0 코어를 유지한 채 Rust 로컬 바이너리(<code>firecrawl-local</code>)와 Keyless 무가입 진입 장벽을 밀어붙인 전략은 정확히 이 지점을 파고든다.
            </p>
            <ul>
              <li><strong>개발자 락인 해방:</strong> <code>api_url="http://localhost:3002"</code> 한 줄만 바꾸면 로컬 테스트에서 프로덕션 클라우드, 혹은 사내 <code>apps/api</code> 자체 구축 클러스터로 코드 수정 없이 전환된다.</li>
              <li><strong>토큰 경제학 최적화:</strong> 불필요한 CSS·광고·보일러플레이트를 걷어낸 클린 마크다운은 RAG와 에이전트 컨텍스트 비용을 극적으로 절감시킨다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 인간이 읽는 웹에서, 에이전트가 읽는 웹으로
            </h3>
            <p>
              지난 30년간 웹은 인간의 눈을 위한 HTML과 CSS로 진화해 왔다. 그러나 앞으로 웹 트래픽의 절반 이상은 인간의 브라우저가 아니라 AI 에이전트의 컨텍스트 윈도우를 통과하게 될 것이다.
            </p>
            <p>
              20만4천 개의 스타를 모은 Firecrawl은 그 거대한 번역 계층의 가장 뜨거운 최전선에 서 있다. 웹페이지가 존재하는 한, 그것을 가장 깨끗한 지식으로 증류해 내는 파이프라인이 곧 다음 세대 AI 애플리케이션의 혈관이 된다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Firecrawl+AI+agent+MCP+local+tutorial" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://www.firecrawl.dev/playground" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> Firecrawl 플레이그라운드
              </a>
              <a href="https://github.com/firecrawl/firecrawl" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
