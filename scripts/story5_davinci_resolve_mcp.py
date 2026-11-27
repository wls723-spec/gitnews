# -*- coding: utf-8 -*-
# Story 5: samuelgursky/davinci-resolve-mcp

STORY_5_HTML = r"""
      <!-- ========================================================== -->
      <!-- [HERO 5] samuelgursky/davinci-resolve-mcp                  -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_davinci_resolve_mcp.jpg" alt="DaVinci Resolve 390 MCP Tools AI Video Editing Control Panel Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="film" style="width:12px;height:12px;fill:#fff;"></i> CREATOR AI #5</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🎬 +67★/d (★4,458) · 390개 MCP 툴로 영상 편집·색보정·Fusion까지 AI가 직접 제어</span>
              <span class="platform-tag">GitHub Trending &amp; Video Post-Production</span>
              <span class="platform-tag">samuelgursky / davinci-resolve-mcp</span>
            </div>

            <h2 class="article-headline">
              "무료판의 파이썬 잠금 장벽까지 로컬 브릿지로 넘은 390개 영상 편집 툴" — AI가 DaVinci Resolve 타임라인과 컬러 그레이딩을 직접 조작하는 'davinci-resolve-mcp'
            </h2>

            <div class="article-subheadline">
              Blackmagic DaVinci Resolve 스크립팅 API를 100% 커버(93.6% 실기 검증)해 타임라인 편집·미디어 풀 정리·리뷰 마커·색보정·Fusion·Fairlight를 AI 에이전트에 연결하고, 소스 원본 무결성을 보장하는 로컬 웹 제어판과 무료판 인앱 브릿지까지 구현한 MCP 서버 (v5.7.1 · MIT)
            </div>
            <p class="article-snippet">
              영상 편집 소프트웨어에서 AI를 쓰려면 클라우드 서비스에 수십 GB 원본 영상을 올리거나, 고가의 폐쇄형 AI 플러그인 구독료를 내야 했습니다. <strong>samuelgursky/davinci-resolve-mcp</strong>는 업계 표준 NLE인 DaVinci Resolve 공식 스크립팅 API를 <strong>100% 커버(390개 세분화 툴 / 37개 복합 툴)</strong>해 Claude·Cursor·Codex 같은 에이전트가 내 PC의 Resolve를 직접 조종하게 만듭니다. 여기에 원본 파일을 절대 건드리지 않는 <strong>소스 세이프 미디어 분석 제어판</strong>과 Blackmagic 무료판의 외부 스크립팅 제한을 우회하는 HMAC 로컬 브릿지 기술까지 담아 +67★/d로 급상승했습니다(★<strong>4,458</strong>).
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
              <i data-lucide="flame"></i> 1. 리드: <code>npx davinci-resolve-mcp setup</code> 한 줄로 깨어난 편집실의 AI 조수
            </h3>
            <p>
              수백 개의 컷이 흩어진 다큐멘터리 촬영 원본 폴더를 받아 들었을 때, 편집자의 가장 고된 노동은 예술적 컷 편집이나 색보정이 아니다. 클립마다 메타데이터를 달고, 미디어 풀 빈(Bin)을 정리하고, 감독의 피드백을 타임코드 마커로 옮기고, 4K와 프록시 렌더 큐를 세팅하는 지루한 반복 작업이다. <code>npx davinci-resolve-mcp setup</code>을 실행하면 Python 가상환경과 Resolve 경로를 자동 감지해 Claude Desktop, Claude Code, Cursor, VS Code, Windsurf, Zed, Codex CLI 설정까지 한 번에 꽂아 준다.
            </p>
            <p>
              연결이 끝나면 편집자는 대화창에 이렇게 적기만 하면 된다: <em>"현재 Resolve 프로젝트의 미디어를 인벤토리화하고, 소스 클립을 분석해 무음 구간과 오디오 피크에 마커를 찍은 뒤 타임라인 러프 컷을 구성해 줘."</em> AI는 클라우드로 영상을 1바이트도 업로드하지 않은 채 내 워크스테이션에서 돌아가는 DaVinci Resolve의 타임라인, 컬러 페이지, Fusion, Fairlight를 실시간으로 제어한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '블랙박스 클라우드 AI 편집' vs '프로 NLE 직접 제어'
            </h3>
            <p>
              웹 기반 AI 영상 편집 서비스들이 우후죽순 쏟아졌지만, 실제 방송·영화·유튜브 프로덕션 현장은 여전히 Adobe Premiere Pro와 Blackmagic DaVinci Resolve를 떠나지 않는다. 프로 작업자에게 필요한 것은 장난감 같은 웹 타임라인이 아니라, 이미 색보정 LUT과 오디오 버스가 깔려 있는 로컬 프로젝트 파일 안에서 정확하게 작동하는 지능형 부조종사다.
            </p>

            <div class="editorial-quote">
              <p>
                "DaVinci Resolve 공식 스크립팅 API를 <strong>100% 커버(실기 검증률 93.6%)</strong>하며, 37개 복합(Compound) 툴과 390개 전체 툴 모드를 모두 제공한다. 소스 미디어는 철저히 읽기 전용(Read-Only)으로만 다루며 모든 분석 인덱스와 결과는 로컬 제어판에서 투명하게 검증된다."
              </p>
              <small>— samuelgursky/davinci-resolve-mcp v5.7.1 명세 &amp; API Coverage 리포트 (★4,458 · MIT)</small>
            </div>

            <p>
              특히 주목할 대목은 AI 에이전트의 고질병인 <strong>'컨텍스트 윈도우 폭발'</strong>을 정면으로 해결한 설계다. 390개에 달하는 Resolve API 함수를 모두 LLM 프롬프트에 밀어 넣으면 토큰만 낭비되므로, 기본 모드에서는 관련 작업을 액션 파라미터로 묶은 <strong>37개 복합 툴</strong>만 노출해 가볍게 돌리고, 정밀 제어가 필요할 때만 <code>--full</code> 플래그로 390개 전체 툴을 여는 이원화 전략을 택했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 이중 서버 모드, 소스 세이프 로컬 제어판, 그리고 무료판 HMAC 브릿지
            </h3>
            <p>
              이 프로젝트가 단순한 API 래퍼를 넘어 v5.7.1까지 200여 건의 이슈를 돌파하며 완성도를 끌어올린 비결은 세 가지 아키텍처 장치에 있다:
            </p>
            <ul>
              <li><strong>37개 복합 툴 / 390개 풀 툴 &amp; 오프라인 18툴:</strong> 편집, 미디어 풀 조직, 렌더 설정, 리뷰 마커, 컬러 그레이딩, Fusion 노드, Fairlight 오디오, 프로젝트 수명주기 관리를 아우른다. 오프라인 분석용 18개 고급 툴이 별도로 존재해 Resolve가 실행 중이지 않을 때도 클립 인덱스 검색과 샷 분석 리포트 편집을 수행한다.</li>
              <li><strong>토큰 보호형 로컬 웹 제어판(<code>src.control_panel</code>):</strong> 실행 시 <code>http://127.0.0.1:8765/#token=…</code> 형태의 1회용 액세스 토큰 URL이 열리며, 현재 연결된 Resolve 프로젝트의 클립 상태·시퀀스·오프라인/온라인 여부·인덱스 크기를 한눈에 감사할 수 있다. 모든 원본 미디어는 철저히 Read-Only로 잠겨 원본 손상 사고를 막는다.</li>
              <li><strong>무료판(Free Edition) 인앱 루프백 브릿지(HMAC + One-Use Nonce):</strong> Blackmagic은 유료 Studio 버전 구매자에게만 외부 프로세스의 <code>scriptapp("Resolve")</code> 접속을 허용한다. 이에 저자는 Resolve 내부의 <code>Workspace &gt; Scripts</code> 메뉴를 통해 실행되는 소형 브릿지 스크립트를 설치해, 살아 있는 <code>resolve</code> 객체를 HMAC 서명과 일회용 난스(Nonce)로 보호된 로컬 루프백 소켓으로 재노출하는 정공법을 구현했다(macOS에서는 <code>PYTHON3HOME</code> 및 비버전명 <code>python3</code> 심볼릭 링크 자동 진단 프리플라이트까지 내장).</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">davinci-resolve-mcp 듀얼 트랜스포트 &amp; 소스 세이프 제어 아키텍처</span>
                <span class="schematic-badge">37 Compound / 390 Full Tools · 100% API Coverage · HMAC Bridge</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Agent &amp; MCP Mode</div>
                  <div class="schematic-desc">
                    Claude · Cursor · Codex · Zed · Windsurf 연동<br>
                    <strong>Compound (37툴):</strong> 컨텍스트 토큰 절약<br>
                    <strong>Full (390툴):</strong> Edit·Color·Fusion·Fairlight<br>
                    <strong>Offline (18툴):</strong> 로컬 샷 분석 인덱스 조회
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Dual Transport &amp; Bridge</div>
                  <div class="schematic-desc">
                    <strong>Studio Edition:</strong> 공식 External Scripting 직결<br>
                    <strong>Free 20.x~21.0.x:</strong> 인앱 <code>resolve_bridge</code> 실행<br>
                    루프백 전용 + HMAC 서명 + 1회용 Nonce 인증<br>
                    macOS <code>PYTHON3HOME</code> &amp; <code>libpython</code> 프리플라이트
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Source-Safe Control Panel</div>
                  <div class="schematic-desc">
                    <code>127.0.0.1:8765/#token=...</code> 로컬 브라우저 UI<br>
                    원본 미디어 <strong>Read-Only</strong> 강제 잠금<br>
                    활성 프로젝트·클립·시퀀스·인덱스 실시간 검사<br>
                    분석 리포트 인라인 수정 &amp; 검색 인덱스 갱신
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">davinci-resolve-mcp 로컬 웹 제어판 실화면 — 프로젝트 감사·인덱스·Read-Only 안전 상태</span>
              </div>
              <img src="../assets/images/demo_davinci_resolve_mcp.png" alt="DaVinci Resolve MCP Local Browser Control Panel Overview UI" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/samuelgursky/davinci-resolve-mcp 공식 제어판 UI(docs/images/control-panel/01-overview.png): 활성 프로젝트, 클립·시퀀스 상태, 검색 인덱스 및 Source media read-only 안전 잠금 표시 화면.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 &amp; 플랫폼 게이트키핑: Resolve 21.1의 파이썬 봉쇄와 '숨바꼭질'
            </h3>
            <p>
              이 프로젝트의 릴리스 노트에는 NLE 거대 벤더와 오픈소스 에이전트 생태계 사이의 미묘한 긴장감이 고스란히 기록돼 있다. Blackmagic은 본래 외부 프로세스 스크립팅만 유료 Studio(295달러)로 제한하고 내부 <code>Workspace &gt; Scripts</code> 메뉴는 무료판에도 열어두고 있었다. 그러나 <strong>Resolve 21.1 업데이트에서 무료판의 Scripts 메뉴가 아예 <code>.py</code> 파일 목록 자체를 가리기 시작</strong>하면서(이슈 #203, 단 Lua 스크립트는 여전히 목록에 노출됨) 무료판 브릿지 경로가 위협받는 상황이 벌어졌다.
            </p>
            <ul>
              <li><strong>크리에이티브 소프트웨어의 해자 재편:</strong> 과거 영상 편집 툴의 해자는 복잡한 버튼과 단축키 숙련도였다. 이제 MCP를 통해 자연어로 색보정·컷·마커를 자동화하는 시대가 열리면서, 소프트웨어 벤더들이 자사 API와 스크립팅 런타임을 무료 사용자에게 어디까지 열어둘 것인가가 새로운 비즈니스 분기점이 되고 있다.</li>
              <li><strong>클라우드 종속 없는 프라이버시 편집:</strong> 미공개 영화·광고·기업 내부 영상은 보안 계약상 외부 클라우드 AI 서비스로 절대 반출할 수 없다. 로컬 MCP와 오프라인 인덱스 검색 구조는 보안 규정을 준수하면서도 AI 자동화를 도입하려는 스튜디오들의 유일한 해법이다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 타임라인은 이제 마우스가 아니라 대화로 자른다
            </h3>
            <p>
              마우스로 프레임을 1칸씩 밀어 맞추고 수백 개의 클립 이름을 손으로 고치던 편집실의 야근 풍경이 바뀌고 있다. 390개의 정밀한 MCP 도구가 연결된 순간, AI는 영상을 대신 만들어주는 대체재가 아니라 편집자의 의도를 0.1초 만에 타임라인과 노드 트리에 옮겨 심는 가장 유능한 어시스턴트 에디터(AE)가 된다.
            </p>
            <p>
              소프트웨어의 기능을 100% API로 열어둔 대가, 그리고 그 API를 가장 안전한 로컬 제어판과 연결한 장인정신이 만났을 때 크리에이티브 툴의 새로운 10년이 열린다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=davinci+resolve+mcp+server+ai+editing" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/samuelgursky/davinci-resolve-mcp" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
