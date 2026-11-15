# -*- coding: utf-8 -*-
# Story 1: dream-num/univer (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] dream-num/univer : COVER STORY                    -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_univer.jpg" alt="Univer AI Office SDK Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">📊 AI 오피스 엔진 독립 선언</span>
              <span class="platform-tag">GitHub Trending #1 &amp; univer.ai</span>
              <span class="platform-tag">dream-num / univer</span>
            </div>
            
            <h2 class="main-lead-headline">
              <span id="hero-title">MS 오피스·구글 워크스페이스의 성벽을 허무는 오픈소스 반란 'Univer': "인간과 AI 에이전트가 같은 시트 위에서 일한다"</span>
            </h2>

            <div class="article-subheadline">
              Canvas 렌더링·수식 엔진·크로스피처 실행취소·Node.js 헤드리스 연산까지 Apache-2.0으로 개방해 내 제품 안에 '직접 조립하는 AI 오피스' 시대를 연 차세대 Office SDK
            </div>
            <p class="article-snippet">
              기업용 AI 에이전트를 만들려는 개발팀이 가장 먼저 부딪히는 벽은 LLM 성능이 아니라 '문서와 스프레드시트'입니다. 수천 개 기업의 재무·재고·계약 데이터가 엑셀과 구글 시트 안에 갇혀 있는데, 정작 AI에게 셀을 읽고 수식을 고치며 사람과 나란히 협업하게 해줄 오픈소스 오피스 엔진은 존재하지 않았습니다. 하루 만에 1,041개의 스타를 쓸어 담으며 누적 25,556스타를 돌파한 'Univer'는 브라우저 Canvas 에디터부터 Node.js 헤드리스 계산, 그리고 AI 에이전트용 Facade API까지 통째로 개방하며 빅테크 오피스 독점에 정면 승부를 걸었습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 챗봇 창에 갇힌 AI, 엑셀 셀 하나 못 건드리는 기형적 현실
            </h3>
            <p>
              오늘날 수많은 기업이 수억 원을 들여 사내 AI 코파일럿을 구축하지만, 정작 실무자의 책상 위에서 벌어지는 풍경은 우스꽝스럽다. 직원이 브라우저 오른쪽 챗봇 창에 CSV 파일을 업로드하면 AI가 요약을 뱉어내고, 직원은 그 숫자를 다시 복사해 Microsoft 365나 Google Sheets의 셀에 손으로 붙여넣는다. 수식이 연쇄적으로 깨지거나 필터 범위가 어긋나도 AI는 화면 밖에서 무슨 일이 벌어지는지 전혀 알지 못한다.
            </p>
            <p>
              수십 년간 오피스 스위트는 빅테크가 클라우드 구독료(SaaS)와 포맷 독점(OOXML)으로 지배해온 난공불락의 성채였다. 바로 이 장벽을 정조준해 GitHub 일간 트렌딩 최상단(1,041 스타/일, 총 25,556 스타)을 점령한 프로젝트가 등장했다. 인간과 AI 에이전트가 동일한 데이터 모델과 수식 엔진 위에서 실시간으로 공동 작업할 수 있게 해주는 오픈소스 오피스 SDK, <strong>dream-num/univer</strong>다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '외부 SaaS 연동'이 아니라 '내 앱 내부의 오피스 커널'
            </h3>
            <p>
              Univer가 기존 오픈소스 에디터(단순 웹 테이블 라이브러리나 무거운 서버 사이드 오피스)와 궤를 달리하는 이유는 오피스를 독립된 '앱'이 아닌, <strong>어떤 웹·데스크톱·에이전트 제품에도 내장할 수 있는 아이소모픽(Isomorphic) 엔진</strong>으로 재설계했기 때문이다.
            </p>

            <div class="editorial-quote">
              <p>
                "에이전트와 애플리케이션이 <strong>동일한 워크북 스냅샷, 수식 엔진, Facade API 위에서 작동한다.</strong> 웹 UI에서 사용자가 입력 칸을 수정하면 AI가 계산 결과를 읽고, 반대로 AI가 셀 값을 바꾸면 브라우저의 수식과 차트가 즉각 재계산된다."
              </p>
              <small>— Univer Office SDK 아키텍처 명세 (Apache-2.0 오픈소스 코어 &amp; Isomorphic 설계 문서)</small>
            </div>

            <p>
              실제로 개발자는 단 몇 줄의 `UniverSheetsCorePreset` 코드만으로 자사 SaaS 안에 완벽한 스프레드시트와 리치 텍스트 문서 편집기를 띄울 수 있으며, 동일한 콘텐츠 플러그인과 수식 엔진을 브라우저 없이 **Node.js 헤드리스(Headless) 백엔드**나 워커 풀에서 그대로 돌려 에이전트가 대량의 견적서·재무제표를 검증하게 만들 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 3계층 플러그인 분리와 Command·Mutation·OT 아키텍처
            </h3>
            <p>
              수백만 셀과 복잡한 수식이 얽힌 오피스 엔진이 AI 에이전트의 동시 편집과 실행취소(Undo/Redo) 앞에서도 망가지지 않는 비결은 세 가지 정밀한 내부 설계에 있다:
            </p>
            <ul>
              <li><strong>논리(Logic)와 UI의 철저한 플러그인 분리:</strong> 예를 들어 `sheets-filter` 플러그인이 필터 범위와 규칙 상태를 소유하면, `sheets-filter-ui`는 패널·메뉴·단축키만 담당한다. 덕분에 동일한 도메인 로직이 브라우저 Canvas 렌더링과 Node.js 헤드리스 에이전트 서버 양쪽에서 100% 동일하게 실행된다.</li>
              <li><strong>Command · Mutation · Operation 3단계 명령 체계:</strong> 비즈니스 의도를 조율하는 `Command`, 직렬화 가능한 스냅샷(`IWorkbookData`/`IDocumentData`) 상태를 변경하는 `Mutation`, 패널 열림이나 스크롤 같은 일시적 상태만 바꾸는 `Operation`을 엄격히 분리했다. 필터 범위 안에 행을 삽입하면 기본 행 변경과 필터 범위 확장이 하나의 복합 Undo/Redo 기록으로 묶여 한 번에 되돌려진다.</li>
              <li><strong>Facade API (`univerAPI`) &amp; Worktree 협업 모델:</strong> 에이전트는 내부 DI 서비스에 직접 손대지 않고 `sheet.getRange('A1:D4').setValues(...)` 형태의 표준 Facade API와 타입드 이벤트(`BeforeCommandExecute`, `CommandExecuted`)를 호출한다. 상용 확장인 Server/AI SDK를 결합하면 OT(Operational Transformation) 변경셋 기반의 동시 협업, XLSX/DOCX/PPTX 양방향 변환, 심지어 에이전트가 **격리된 Worktree 초안**에서 문서를 고치고 시각적 렌더 런타임으로 레이아웃 겹침까지 자체 검사한 뒤 인간에게 병합 승인을 요청할 수 있다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Univer Office SDK 아이소모픽 엔진 &amp; AI 에이전트 결합 아키텍처</span>
                <span class="schematic-badge">Isomorphic Core · Apache-2.0</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Core &amp; Facade API Layer</div>
                  <div class="schematic-desc">
                    의존성 주입(DI) &amp; `DependentOn` 그래프<br>
                    직렬화 Unit 스냅샷(`IWorkbookData`)<br>
                    `univerAPI` 앱/에이전트 통합 인터페이스<br>
                    Command / Mutation / Operation 분리
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Isomorphic Execution Engines</div>
                  <div class="schematic-desc">
                    Canvas 고성능 레이아웃 &amp; 렌더링 엔진<br>
                    비동기 수식(Formula) 재계산 엔진<br>
                    브라우저 UI ↔ Node.js Headless 공유<br>
                    크로스피처 `IUndoRedoService` 보장
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Collaboration &amp; Agent Loop</div>
                  <div class="schematic-desc">
                    OT 기반 실시간 동시 편집 체인지셋<br>
                    OOXML (XLSX·DOCX·PPTX) 변환<br>
                    격리 Worktree 초안 작성 및 인간 승인<br>
                    Render Runtime 기반 시각적 린트 검증
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Univer 공식 라이브 스프레드시트 &amp; 앱 연동 데모 (univer.ai/demo/spreadsheets)</span>
              </div>
              <img src="../assets/images/demo_univer.png" alt="Univer Live Spreadsheet & AI Business Review Demo" class="showcase-img">
              <p class="showcase-caption">
                ▲ univer.ai/demo/spreadsheets 실구동 화면: Canvas 기반 고성능 스프레드시트 위에서 시나리오 입력 셀(+20.0%)을 조정하면 수식 엔진과 하단 웹 대시보드 카드가 실시간으로 동기화되어 재계산된다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 산업 지각변동: '시트 위에 얹는 AI'에서 'AI 네이티브 워크스페이스'로
            </h3>
            <p>
              그동안 B2B SaaS 기업들이 자체 제품에 엑셀 수준의 계산력과 협업 편집기를 넣으려면 Microsoft Graph API나 Google Workspace 임베딩에 종속되어 사용자 데이터 권한과 과금 통제권을 넘겨줘야 했다. Univer는 Web SDK 핵심 엔진(Sheets·Docs·수식·렌더링·Headless 처리)을 상업적 제약이 없는 **Apache-2.0 라이선스**로 풀어 이 진입 장벽을 깨부쉈다.
            </p>
            <ul>
              <li><strong>데이터 주권과 오픈 코어 전략:</strong> 기업은 핵심 문서 데이터와 인증·권한 체계를 외부 빅테크 클라우드로 내보내지 않고 자사 서버 안에 묶어둘 수 있다. 반면 고급 피벗·차트·실시간 OT 협업 서버·대규모 AI 워커 풀은 상용 확장 모듈로 분리해 지속 가능한 오픈 코어 비즈니스 모델을 구축했다.</li>
              <li><strong>에이전트 생태계 직결(`univer-cli` &amp; 하네스 통합):</strong> `univer-cli`, `univer-sdk-skills` 및 DeepSeek Harness·OpenClaw 연동 패키지까지 함께 공개되며, 코딩 에이전트가 단순 텍스트 파일이 아니라 살아 움직이는 재무 모델과 보고서 스냅샷을 직접 다루는 표준 기반이 마련되고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 20세기의 서류를 21세기의 API로 해방하다
            </h3>
            <p>
              인류가 가장 많이 쓰는 프로그래밍 언어는 파이썬도 자바스크립트도 아닌 '엑셀 수식'이다. 그동안 AI 혁명은 코드 에디터와 채팅창 바깥에 있던 이 거대한 스프레드시트 대륙을 우회해 지나갈 뿐이었다.
            </p>
            <p>
              Univer는 닫혀 있던 오피스의 심장부를 누구나 뜯어고치고 에이전트를 꽂을 수 있는 오픈소스 커널로 바꿔놓았다. 이제 소프트웨어 개발의 다음 격전지는 '어떤 LLM을 쓸 것인가'가 아니라, '그 에이전트에게 어떤 살아있는 작업 공간을 쥐여줄 것인가'로 옮겨가고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Univer+Office+SDK+open+source" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://univer.ai/demo/spreadsheets" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 라이브 데모 체험
              </a>
              <a href="https://github.com/dream-num/univer" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
