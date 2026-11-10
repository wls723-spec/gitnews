# -*- coding: utf-8 -*-
# Story 4: GoogleChrome/modern-web-guidance (구글 크롬 팀의 코딩 에이전트 지침)

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 4] GoogleChrome/modern-web-guidance : 웹 표준 & 에이전트 혁신 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_modernweb.jpg" alt="Modern Web Guidance by Google Chrome" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="compass" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #4</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 크롬·엣지·파이어폭스·MDN 연합</span>
              <span class="platform-tag">Show HN & Google Chrome</span>
              <span class="platform-tag">GoogleChrome / modern-web-guidance</span>
            </div>
            
            <h2 class="article-headline">
              2019년 자바스크립트에 갇힌 코딩 에이전트를 해방하라 — 구글 크롬 팀, 낡은 라이브러리 슬롭을 끝장낼 'Modern Web Guidance' 전격 공개
            </h2>

            <div class="article-subheadline">
              LLM 학습 데이터의 레거시 패턴 오염을 타파하고, 네이티브 Dialog·Popover·CSS Subgrid 등 최신 브라우저 프리미티브로 코드 80%를 날려버리는 표준 혁명
            </div>
            <p class="article-snippet">
              자율 코딩 에이전트에게 모달 창 하나를 만들어 달라고 하면, 2019년 시절의 무거운 React 서드파티 라이브러리와 복잡한 z-index 트릭, 수십 줄의 보일러플레이트 자바스크립트를 토해내는 현상이 일상이 되었습니다. 구글 크롬, 마이크로소프트 엣지, 모질라, MDN 팀이 공동으로 결성한 컨소시엄이 오늘 'Modern Web Guidance'를 오픈소스로 발표했습니다. 코딩 에이전트의 컨텍스트 창에 직접 최신 브라우저 내장 플랫폼 프리미티브를 주입하여 군더더기 코드를 원천 차단합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 최신 AI가 왜 7년 전 구닥다리 코드를 짤까?
            </h3>
            <p>
              Claude 3.7 Sonnet이든 GPT-4.5든, 오늘날 가장 뛰어난 최신 프론티어 LLM에게 "간단한 팝업 툴팁과 모달 다이얼로그를 구현해줘"라고 명령해 보라. 
              놀랍게도 모델은 2018년에나 쓰이던 외부 라이브러리(`react-modal` 등)를 npm에 설치하라고 권고하거나, 
              바닐라 JS에서 수동으로 `event.stopPropagation()`과 키보드 포커스 트랩(Focus Trap) 코드를 수십 줄씩 작성하며 끙끙댄다.
            </p>
            <p>
              이유는 자명하다. 거대 언어 모델의 학습 코퍼스에 2015~2020년 시절의 방대한 레거시 자바스크립트 저장소들이 압도적으로 많이 쌓여있기 때문이다. 
              브라우저에는 이미 1줄로 구현 가능한 초고속 네이티브 `<dialog>` 태그와 `popover` 속성이 표준으로 탑재되어 있음에도, 
              AI 에이전트들은 스스로 '2019년의 기억의 늪'에 빠져 끝없는 코드 슬롭(Code Slop)을 양산해왔다. 
              오늘, 구글 크롬 팀이 이를 단번에 뜯어고치기 위한 공식 프로젝트 <strong>modern-web-guidance</strong>를 공개했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 브라우저 4대 거인이 에이전트를 위해 뭉쳤다
            </h3>
            <p>
              이 프로젝트의 위용은 참여 주체에서부터 드러난다. 
              구글 크롬뿐만 아니라 마이크로소프트 엣지(Edge), 모질라 파이어폭스(Firefox), 그리고 전 세계 웹 개발자의 성경인 MDN 팀이 
              하나의 깃허브 저장소에 모여 컨소시엄을 구성했다. 
              브라우저 제조사들이 AI 에이전트의 지능을 표준 플랫폼으로 유도하기 위해 단체 행동에 나선 역사상 최초의 사례다.
            </p>

            <div class="editorial-quote">
              <p>
                "코딩 에이전트는 웹 브라우저가 지난 5년 동안 얼마나 강력하고 우아하게 진화했는지 모른 채, 
                여전히 무거운 폴리필과 레거시 의존성 체인을 만들어내고 있다. 
                <strong>Modern Web Guidance는 에이전트가 코드를 한 줄 쓰기 전에, 최신 웹 플랫폼의 네이티브 프리미티브와 접근성 규격을 에이전트의 컨텍스트 창에 직접 주입한다.</strong> 
                우리는 수백만 줄의 불필요한 번들 자바스크립트를 웹에서 삭제할 것이다."
              </p>
              <small>— 구글 크롬 웹 플랫폼 팀 & 해커뉴스 론칭 스레드 발췌</small>
            </div>

            <p>
              개발자는 단 한 줄의 CLI 명령어(`npx modern-web-guidance@latest install`)로 Claude Code, Cursor, Windsurf 등에 
              이 가이드를 에이전트 스킬로 설치할 수 있으며, 에이전트는 작업 착수 전 자동으로 최신 웹 가이던스를 검색(`search`)하고 반영한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 메커니즘: 에이전트 컨텍스트 주입과 정적 레거시 스캐너
            </h3>
            <p>
              Modern Web Guidance는 단순한 정적 문서 모음이 아니다. AI 에이전트가 즉각 소화할 수 있도록 고안된 인터랙티브 툴체인이다:
            </p>
            <ul>
              <li><strong>Agent-Targeted 가이던스 검색 CLI:</strong> 에이전트가 "animate a dialog backdrop" 같은 자연어 쿼리를 던지면, 낡은 CSS 애니메이션 트릭 대신 최신 `:popover-open`, `@starting-style`, `transition-behavior: allow-discrete` 등 최신 스펙을 단 몇 줄의 압축된 가이드로 반환.</li>
              <li><strong>레거시 패턴 정적 스캐너 (`legacy-scan`):</strong> 기존 코드베이스 전체를 스캔하여 낡은 `resize` 이벤트 리스너를 네이티브 `ResizeObserver`나 CSS 컨테이너 쿼리로, 복잡한 드래그 앤 드롭을 HTML Drag and Drop API로 자동 리팩토링할 타깃을 검출.</li>
              <li><strong>브라우저 호환성 실시간 벤치마크 매핑:</strong> Baseline 규격을 기반으로 모든 주요 모던 브라우저에서 95% 이상 지원되는 안전한 API만 우선 추천하여 호환성 버그 제로 달성.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Modern Web Guidance 에이전트 컨텍스트 주입 파이프라인</span>
                <span class="schematic-badge">Platform Guidance Engine</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Coding Agent Query</div>
                  <div class="schematic-desc">
                    Claude Code / Cursor 프롬프트<br>
                    "반응형 모달 & 툴팁 구현 요청"<br>
                    기존 LLM의 2019년 편향 차단
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Modern Web Guidance CLI</div>
                  <div class="schematic-desc">
                    npx search & retrieve 엔진<br>
                    Chrome/Edge/MDN 표준 지식 주입<br>
                    최신 Baseline API & 패턴 번들
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Modern Platform Output</div>
                  <div class="schematic-desc">
                    네이티브 &lt;dialog&gt; & popover<br>
                    CSS @starting-style 전환<br>
                    서드파티 의존성 제로화 달성
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">구글 크롬 개발자 공식 문서 포털 라이브 뷰</span>
              </div>
              <img src="../assets/images/demo_modernweb.png" alt="Google Chrome Modern Web Guidance Portal" class="showcase-img">
              <p class="showcase-caption">
                ▲ developer.chrome.com/docs/modern-web-guidance 공식 뷰: 크롬 팀이 제정한 코딩 에이전트용 웹 프리미티브 명세와 벤치마크 평가 대시보드 런타임.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 웹 생태계 영향: 무거운 npm의 황혼
            </h3>
            <p>
              지난 10년간 웹 프론트엔드는 npm 패키지 의존성의 거대한 무게에 짓눌려왔다. 
              단순한 폼 유효성 검사나 날짜 선택기를 위해 수십 메가바이트의 라이브러리를 다운로드받는 기형적인 구조가 상식이 되었다. 
              AI 에이전트의 보급은 이러한 '의존성 폭탄'을 더욱 악화시킬 위험이 있었다.
            </p>
            <p>
              구글과 브라우저 제조사들이 발 빠르게 에이전트의 뇌 속에 네이티브 표준을 직접 이식함으로써, 
              웹은 다시 가볍고 빠르며 접근성이 뛰어난 본래의 모습으로 회귀할 기회를 얻었다. 
              웹 성능 최적화와 번들 다이어트를 고민하던 글로벌 기업들에게는 수억 원의 인프라 비용 절감으로 이어지는 중대한 분기점이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 기계에게 올바른 문법을 가르치는 일
            </h3>
            <p>
              AI 에이전트가 소프트웨어를 작성하는 시대일수록, 에이전트가 참조하는 '기본 토대'의 순수성이 결정적인 차이를 만든다. 
              더 이상 구시대의 낡은 보일러플레이트로 미래의 소프트웨어를 더럽힐 수는 없다. 
              브라우저 거인들이 함께 쏘아 올린 Modern Web Guidance는, 
              인공지능과 현대 웹 표준이 만났을 때 소프트웨어가 얼마나 날렵하고 아름다워질 수 있는지를 명징하게 보여준다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Google+Chrome+Modern+Web+Guidance+coding+agents" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://developer.chrome.com/docs/modern-web-guidance" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> 크롬 개발자 공식 문서 바로가기
              </a>
              <a href="https://github.com/GoogleChrome/modern-web-guidance" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
