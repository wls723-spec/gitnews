# -*- coding: utf-8 -*-
# Story 3: GenOffice

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] genspark-ai/genoffice : 세계 최초 오픈소스 AI 오피스 스위트 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_genoffice.jpg" alt="GenOffice Open Source AI Office Suite" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="play" style="width:12px;height:12px;fill:#fff;"></i> YOUTUBE 65K</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">📄 세계 최초 오픈소스 AI 오피스 스위트</span>
              <span class="platform-tag">GitHub Trending TypeScript</span>
              <span class="platform-tag">genspark-ai / genoffice</span>
            </div>
            
            <h2 class="article-headline">
              마이크로소프트 365의 500억 달러 구독 장벽에 균열을 내다: 세계 최초 오픈소스 AI 오피스 'GenOffice'
            </h2>

            <div class="article-subheadline">
              "Word, Excel, PowerPoint and PDF files, edited by you and your AI" — 워드, 엑셀, 파워포인트를 마이크로소프트 클라우드 전송 없이 로컬에서 바이너리 네이티브 편집… Claude Code, Cursor, Codex 연동 CLI 및 MCP 스킬 기본 탑재 (BYOK 지원)
            </div>
            <p class="article-snippet">
              마이크로소프트 코파일럿(Copilot)의 월 30달러 강제 과금과 기밀 데이터 유출 불안을 일거에 종식시킨 오픈소스 오피스 제품군. 복잡한 엑셀 수식 계산과 파워포인트 슬라이드 마스터, 워드 서식을 개발자의 터미널 코딩 에이전트가 직접 제어한다.
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
              <i data-lucide="file-spreadsheet"></i> 1. 오피스 독점의 감옥: 왜 우리는 마크다운으로 도망쳐야 했는가
            </h3>
            <p>
              현대 비즈니스의 모든 부(富)와 의사결정은 마이크로소프트 오피스 3종 세트—워드(<code>.docx</code>), 엑셀(<code>.xlsx</code>), 파워포인트(<code>.pptx</code>)—위에서 돌아간다. 
              하지만 AI 혁명이 시작된 이래, 개발자들과 AI 에이전트들은 이 세 가지 포맷 앞에서 언제나 무력한 장님 신세였다. 
              오피스 오픈 XML(OOXML) 규격은 수십 년간 축적된 레거시 태그와 복잡한 ZIP 압축 구조체로 얽혀 있어, 거대 언어 모델이 조금만 수식을 건드려도 파일 전체가 깨져 열리지 않는 'XML 파괴 참사'가 일어났기 때문이다.
            </p>
            <p>
              결국 전 세계의 수많은 개발자와 에이전트들은 마크다운(Markdown)과 CSV라는 초라한 텍스트 껍데기로 도망쳐야 했다. 
              하지만 비즈니스 현장의 경영진과 고객사들은 마크다운 문서를 읽지 않는다. 그들은 정교한 셀 서식과 계산 수식이 박힌 진짜 엑셀 파일과 브랜드 템플릿이 적용된 파워포인트 발표 자료를 요구한다. 
              마이크로소프트는 이 틈새를 틀어쥐고 기업 고객들에게 <strong>"월 30달러의 M365 Copilot을 추가 구독하고 모든 사내 문서를 우리 애저(Azure) 클라우드로 올려보내라"</strong>고 강요해 왔다. 
              이 500억 달러 독점 요새에 정면 도전장을 던진 오픈소스 프로젝트가 바로 <strong>GenOffice(genspark-ai/genoffice)</strong>다.
            </p>

            <div class="editorial-quote danger">
              "우리는 마이크로소프트의 클라우드 구독 감옥에 갇힌 전 세계 오피스 워커와 개발자들을 해방하고자 합니다. 
              당신의 사내 재무 제표와 인수합병(M&A) 기밀 문서를 왜 실리콘밸리 빅테크 서버로 전송해야 합니까? 
              <strong>GenOffice는 완벽한 로컬 환경에서, 당신이 소유한 API 키(BYOK)만으로, 터미널의 코딩 에이전트가 진짜 바이너리 .xlsx와 .docx를 직접 뜯어고치게 만듭니다.</strong>"
              <span class="quote-author">— 메릭(Merrick), GenOffice 프로젝트 리드</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 브라우저 웹 앱과 터미널 에이전트의 완전한 결합
            </h3>
            <p>
              GenOffice의 파괴력은 단순한 리브레오피스(LibreOffice) 같은 대체 뷰어가 아니라는 데 있다. 
              현대적인 반응형 웹 UI(Docs, Sheets, Slides, PDF, Markdown 에디터)를 브라우저에서 독립 제공하는 동시에, <strong>Claude Code, Cursor, Codex가 로컬 터미널에서 즉시 호출할 수 있는 <code>genoffice</code> CLI와 공식 에이전트 스킬(MCP 서버)</strong>을 완벽하게 내장하고 있다.
            </p>
            <p>
              이제 개발자는 터미널에서 <code>claude</code>를 켜고 <em>"지난 분기 재무제표 엑셀 파일 열어서 매출 15% 이상 성장한 부서만 녹색 하이라이트하고 연간 복합성장률(CAGR) 수식을 C열에 추가해줘"</em>라고 말하기만 하면 된다. 
              에이전트는 GenOffice 엔진을 통해 백그라운드에서 바이너리 파일을 직접 조작하고, 인간은 브라우저에서 실시간으로 그 수식과 표가 렌더링되는 모습을 눈으로 검증한다.
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="cpu" style="color:#3b82f6;"></i> GenOffice: 로컬 바이너리 오피스 파일 제어 및 에이전트 스킬 아키텍처</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">ZERO-CLOUD OFFICE ENGINE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">PHASE 1. 바이너리 인메모리 로딩</div>
                  <div class="step-title">Local Office Files</div>
                  <div class="step-desc">로컬 디스크의 실제 .docx, .xlsx, .pptx 파일을 클라우드 업로드 없이 로컬 브라우저/터미널 메모리에 직접 적재.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">PHASE 2. 무결점 XML 파싱</div>
                  <div class="step-title">Deterministic OOXML Engine</div>
                  <div class="step-desc">Office Open XML 규격의 ZIP 컨테이너를 무손실 해체하고 셀 스타일, 수식 의존성 트리(Formula Tree)를 메모리 상에 구축.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">PHASE 3. 에이전트 스킬 통신</div>
                  <div class="step-title">CLI & MCP Bridge</div>
                  <div class="step-desc">Claude Code, Codex, Cursor가 Model Context Protocol(MCP)을 통해 셀 조작, 단락 교체, 슬라이드 템플릿 제어.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 실시간 브라우저 렌더링</div>
                  <div class="step-title">Local Canvas GUI</div>
                  <div class="step-desc">에이전트가 수정한 문서의 변경 사항(Tracked Changes)과 수식 연산 결과를 로컬 브라우저 UI에서 0ms 즉각 시각화.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 결정론적 바이너리 저장</div>
                  <div class="step-title">Native Binary Export</div>
                  <div class="step-desc">MS 오피스 365 데스크톱 앱에서 100% 오류 없이 열리는 순정 규격의 바이너리 파일로 즉각 패키징 및 로컬 저장.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="code-2"></i> 3. 기술 메커니즘 해부: 수식 엔진 내장과 무손실 바이너리 패치
            </h3>
            <p>
              GenOffice가 기술적으로 독보적인 이유는 단순한 텍스트 치환기가 아니라 <strong>'순수 자바스크립트/웹어셈블리 기반의 풀스택 오피스 런타임'</strong>을 밑바닥부터 구현했기 때문이다:
            </p>
            <p>
              첫째, <strong>순정 엑셀 계산 엔진(Calculation Engine)의 내장</strong>이다. 에이전트가 <code>VLOOKUP</code>, <code>XLOOKUP</code>, <code>INDEX/MATCH</code>, <code>SUMIFS</code> 같은 복잡한 수식을 삽입하면, GenOffice는 파일을 닫기 전 내부 수식 그래프를 순회하며 계산 캐시(<code>v</code> 태그)를 자동으로 갱신한다. 따라서 사용자가 나중에 엑셀 데스크톱 앱에서 열었을 때 수식 에러나 계산 지연이 전혀 발생하지 않는다.
            </p>
            <p>
              둘째, <strong>변경 이력 추적(Track Changes)과 주석의 네이티브 보존</strong>이다. 기업 환경에서 법무 검토를 할 때 가장 중요한 기능은 누가 어느 문장을 수정했는지 표시하는 '빨간 줄(Redline)'이다. GenOffice는 워드의 <code>w:ins</code>, <code>w:del</code> 태그를 완벽하게 지원하여, AI 에이전트가 제안한 수정안이 인간 검토자에게 깔끔한 제안 모드로 전달된다.
            </p>
            <p>
              셋째, <strong>운영체제 전반을 아우르는 크로스 플랫폼 CLI</strong>다. macOS, Windows, Linux를 모두 지원하며, <code>npx genoffice edit report.docx</code> 한 줄로 터미널과 에디터가 즉시 동기화된다.
            </p>

            <!-- 실제 소프트웨어 UI / 터미널 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_genoffice_editor.jpg" alt="GenOffice 오픈소스 오피스 제품군 웹 에디터 및 CLI 연동 화면" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>GenOffice 실구동 웹 인터페이스:</strong> 워드(Docs), 엑셀(Sheets), 파워포인트(Slides), PDF 에디터가 단일 로컬 환경에서 통합 구동되는 모습. 터미널의 Claude Code 에이전트가 로컬 <code>.xlsx</code> 수식과 <code>.docx</code> 계약서 변경 이력을 실시간으로 동기화 수정.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="dollar-sign"></i> 4. 비즈니스 해자: 500억 달러 구독 제국의 균열
            </h3>
            <p>
              마이크로소프트의 기업가치 중 가장 탄탄한 기둥은 연간 500억 달러가 넘는 M365 상용 구독 매출이다. 
              기업들은 보안과 포맷 호환성 때문에 울며 겨자 먹기로 천문학적인 라이선스 비용을 지불해 왔다. 
              그러나 GenOffice의 등장은 전 세계 수많은 중소기업과 스타트업에게 <strong>"비싼 클라우드 오피스 구독료를 내지 않고도, 자체 보유한 오픈소스 LLM이나 저렴한 API로 최고 수준의 AI 오피스 자동화를 누릴 수 있다"</strong>는 강력한 대안을 제시한다. 
              이는 사무 생산성 소프트웨어 시장의 무게중심이 독점 벤더의 클라우드에서 '사용자 소유의 로컬 에이전트'로 이동하는 결정적 변곡점이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="check-circle"></i> 5. 키커: 문서의 주인은 소프트웨어가 아니라 인간이다
            </h3>
            <p>
              우리의 사고와 지식, 비즈니스의 역사가 특정 거대 기업의 폐쇄적인 파일 포맷과 클라우드 서버에 영원히 볼모로 잡혀 있을 이유는 없다. 
              GenOffice는 인공지능 시대의 생산성 도구가 지향해야 할 참된 가치가 <strong>'완전한 로컬 자립성'</strong>과 <strong>'투명한 데이터 주권'</strong>에 있음을 증명하고 있다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://genoffice.ai/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 웹 데모 바로 체험
              </a>
              <a href="https://www.youtube.com/results?search_query=genoffice+ai+office+suite" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/genspark-ai/genoffice" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 3 ready.")
