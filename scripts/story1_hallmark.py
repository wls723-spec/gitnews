# -*- coding: utf-8 -*-
# Story 1: Nutlope/hallmark (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] Nutlope/hallmark : 오늘의 메인 기사 (COVER STORY) -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_hallmark.jpg" alt="Hallmark Anti-AI-Slop Design Skill" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔥 2,830 스타 폭발 · 보라색 그라디언트 슬롭 전면 선전포고</span>
              <span class="platform-tag">GitHub Trending #1</span>
              <span class="platform-tag">Nutlope / hallmark</span>
            </div>
            
            <h2 class="main-lead-headline">
              <span id="hero-title">AI 슬롭(Slop)의 범람을 저지하라: 천편일률적 보라색 그라디언트를 파괴하는 안티-슬롭 디자인 하네스 'Hallmark' 전격 공개</span>
            </h2>

            <div class="article-subheadline">
              "AI가 만든 티가 나는 순간 그 프로덕트는 즉시 싸구려로 전락한다" — Hassan El Mghari(Together AI), Claude Code·Cursor·Codex 전용 오픈소스 안티-슬롭 디자인 스킬 'Hallmark' 공개 하루 만에 +2,830 스타 폭풍 견인… 3단계 게이트(Floor·Reflex·Finish)와 헤드리스 브라우저 실시간 린팅으로 '공허한 AI 웹사이트'의 숨통을 끊다
            </div>
            <p class="article-snippet">
              제목 위의 뻔한 아이브로우 태그, 단어 하나에만 칠해진 무의미한 형광펜, 스크롤을 무시하는 허세 가득한 히어로 섹션, 아무것도 보내지 않는 가짜 구독 폼까지. 모델의 나태한 편향을 50개 실물 재질(Material)과 엄격한 브라우저 검증 파이프라인으로 봉쇄한 디자인 프론티어.
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
              <i data-lucide="flame"></i> 1. 리드: 전 세계 웹을 뒤덮은 'AI 슬롭(Slop)'의 악몽과 피로감
            </h3>
            <p>
              2026년 가을, 우리는 소프트웨어 역사상 가장 기괴한 시대를 통과하고 있다. 
              코딩 에이전트(Claude Code, Cursor, Codex 등)의 눈부신 진화로 누구나 3분 만에 풀스택 웹 애플리케이션을 찍어낼 수 있게 되었지만, 그 결과물로 채워진 인터넷은 참혹하다. 
              어디를 가나 똑같은 <strong>어두운 배경 위의 보라색-남색 그라디언트, 허공에 둥둥 떠 있는 반투명 유리(Glassmorphism) 카드, 제목 위마다 기계처럼 달라붙은 작은 대문자 아이브로우(Eyebrow) 라벨, 그리고 헤드라인 속 단 한 단어에만 칠해진 그라디언트 텍스트</strong>.
            </p>
            <p>
              사람들은 이를 <strong>'AI 슬롭(AI Slop: 인공지능이 게으르게 배설한 쓰레기 디자인)'</strong>이라 부른다. 
              더 심각한 문제는 이 슬롭이 프로덕트의 신뢰도를 파괴한다는 점이다. 
              벤처캐피털 투자자나 엔드유저는 페이지를 열자마자 0.5초 만에 "아, 이것도 AI가 대충 만든 양산형 프로덕트구나"를 직감하고 창을 닫아버린다.
            </p>
            <p>
              이 공허한 양산형 인터페이스의 범람에 제동을 걸기 위해, 전 세계 수백만 명이 사용하는 오픈소스 AI 도구들을 제작해 온 <strong>하산 엘 음가리(Hassan El Mghari, Together AI 엔지니어 겸 바이럴 메이커)</strong>가 결단을 내렸다. 
              그가 공개한 오픈소스 프로젝트 <strong>Hallmark(Nutlope/hallmark)</strong>는 출시 24시간 만에 <strong>하루 2,830개의 스타</strong>를 쓸어 담으며 깃허브 글로벌 트렌딩 1위에 등극했다.
            </p>

            <div class="editorial-quote danger">
              "모델에게 웹페이지를 만들라고 지시하면, 녀석들은 예외 없이 가장 게으르고 뻔한 'AI스러움'의 늪으로 미끄러져 들어갑니다. 
              제목 위의 사족 라벨, 화면을 벗어나는 거대한 히어로, DB 연결도 없는 가짜 이메일 폼... 
              <strong>Hallmark의 철학은 단순합니다. AI가 만든 티가 나는 모든 요소를 하네스 차원에서 원천 차단하고, 방문자가 실제 하러 온 '진짜 일(Job)'에만 화면을 집중시키는 것입니다.</strong>"
              <span class="quote-author">— 하산 엘 음가리 (Hassan El Mghari), Hallmark 아키텍처 선언문 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 'AI 티'를 박멸하는 3단계 검증 게이트와 50가지 실물 재질
            </h3>
            <p>
              <code>Hallmark</code>는 단순한 프롬프트 가이드가 아니다. 
              Claude Code나 Cursor가 웹페이지를 코딩할 때, 백그라운드에서 실시간 헤드리스 브라우저를 띄워 결과물을 인간 디자이너의 눈으로 역감사(Linting)하는 <strong>결정론적 디자인 하네스 엔진</strong>이다.
            </p>
            <p>
              대규모 언어 모델이 디자인 코드를 짤 때 가장 빈번하게 저지르는 7대 악덕(The 7 Tells of AI Slop)을 목록화하고, 이를 코드 생성 즉시 탈락시키는 <strong>3단계 게이트웨이(Tiered Gates)</strong> 아키텍처를 도입했다:
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="shield-check" style="color:#f59e0b;"></i> Hallmark: 3단계 안티-슬롭 검증 게이트 & 브라우저 린팅 파이프라인</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">DETERMINISTIC LINT ENGINE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">GATE 1. 절대 바닥 (Floor)</div>
                  <div class="step-title">배포 결격 사유 원천 차단</div>
                  <div class="step-desc">대비비 미달, 모바일 깨짐, 날조된 가짜 통계, 동작하지 않는 폼 제출 등 즉시 롤백 및 재작성 강제.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">GATE 2. 반사적 편향 (Reflex)</div>
                  <div class="step-title">AI 고유 습관 거부</div>
                  <div class="step-desc">제목 위 아이브로우, 헤드라인 속 단어 단독 채색, 사진만 나열된 빈 프레임, 거대 히어로 섹션 제거.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">GATE 3. 크래프트 마감 (Finish)</div>
                  <div class="step-title">물성(Material) 조율</div>
                  <div class="step-desc">종이, 잉크, 그리드, 타이포그래피 계층 등 50대 테마별 고유 질감과 755개 오픈 라이선스 사진 정밀 배치.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 헤드리스 실감사</div>
                  <div class="step-title">Headless Browser Review</div>
                  <div class="step-desc">Playwright/Chromium 세션에서 실제 뷰포트 렌더링 스크린샷 캡처 후 신선한 컨텍스트로 교차 검증.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 완결형 배포</div>
                  <div class="step-title">/hallmark redesign</div>
                  <div class="step-desc">기존 와이어링과 비즈니스 로직을 온전히 보존한 채, 최상급 테크 저널 수준의 웹으로 원클릭 리모델링.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="wrench"></i> 3. 기술 메커니즘 해부: '과업 중심(Job-to-be-Done)' 레이아웃과 감사의 눈
            </h3>
            <p>
              <code>Hallmark</code>의 가장 혁신적인 공학적 통찰은 <strong>"페이지의 존재 목적(Job)을 코드의 끝이 아니라 시작으로 삼는다"</strong>는 점이다.
            </p>
            <p>
              기존 LLM에게 예약 페이지를 만들라고 하면, 3페이지에 걸친 거창한 미사여구와 기능 소개를 늘어놓은 뒤 페이지 맨 끝 구석에 예약 버튼을 둔다. 
              그러나 <code>Hallmark</code>의 엔진은 <em>"예약 페이지는 예약하러 온 곳이고, 쇼핑몰은 물건을 사러 온 곳이며, 뉴스레터는 구독하러 온 곳이다"</em>라는 대원칙 아래, 
              <strong>핵심 액션(Primary Action)을 해당 카테고리가 요구하는 최상단에 배치하고 페이지 전체를 그 액션의 설득 과정으로 종결</strong>시킨다.
            </p>
            <p>
              더 나아가 개발자는 터미널에서 단 두 개의 명령어로 자신의 프로덕트를 완전히 탈바꿈할 수 있다:
            </p>
            <ul style="margin: 1rem 0 1.5rem 1.5rem; line-height: 1.8; color: var(--text-dark);">
              <li><code>/hallmark audit &lt;path&gt;</code>: 현재 페이지의 HTML/CSS를 스캔하여 7대 슬롭 요소, 접근성 결함, 여백 붕괴를 리포트 형태로 진단.</li>
              <li><code>/hallmark redesign &lt;path&gt;</code>: 기존 자바스크립트 핸들러와 API 연동 로직을 단 하나도 깨뜨리지 않은 채, 50대 테마(Dusk, Cobalt, Studio, Atelier 등)의 품격 있는 물성으로 전면 재건축.</li>
            </ul>

            <!-- 실제 소프트웨어 UI 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_hallmark_ui.jpg" alt="Hallmark의 안티-슬롭 디자인 시스템과 50대 머티리얼 테마 갤러리" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>Hallmark 공식 프로덕트 쇼케이스:</strong> Together AI와 하산 엘 음가리가 구축한 usehallmark.com 갤러리. 양산형 보라색 그라디언트를 완전 배제하고, 종이와 활자의 절제된 미학을 살린 50가지 머티리얼 테마와 헤드리스 브라우저 실시간 안티-슬롭 린팅 결과물을 한눈에 확인할 수 있다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="scale"></i> 4. 비즈니스 해자: 수천만 원짜리 디자인 에이전시 외주 시장의 격변
            </h3>
            <p>
              지금까지 실리콘밸리 스타트업들이 시드 투자를 유치한 뒤 가장 먼저 지출하던 돈은 전문 웹 디자인 에이전시(Design Agency)에 지불하는 수만 달러의 외주 비용이었다. 
              "AI가 짠 코드는 백엔드는 그럭저럭 돌아가도 프론트엔드가 너무 촌스러워서 외부에 공개할 수 없다"는 불신 때문이었다.
            </p>
            <p>
              그러나 <code>Hallmark</code>는 이 마지막 보루마저 허물어뜨리고 있다. 
              개인 개발자가 터미널에서 <code>/hallmark redesign</code>을 실행하는 것만으로, <strong>최고급 브랜딩 스튜디오가 수 주일에 걸쳐 납품하던 타이포그래피 균형, 여백 리듬, 실물 텍스처를 30초 만에 획득</strong>할 수 있게 되었다. 
              이는 에이전시의 존재 이유를 '단순 레이아웃 제작'에서 '극도로 고도화된 인터랙션 설계'로 강제 이동시키는 거대한 산업적 분기점이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 좋은 디자인은 기교가 아니라 '절제'다
            </h3>
            <p>
              레오나르도 다빈치는 <em>"단순함이야말로 궁극의 정교함이다(Simplicity is the ultimate sophistication)"</em>라고 말했다. 
              인공지능이 무한대의 코드를 쏟아낼 수 있는 시대에, 진정한 가치는 '무엇을 더 채워 넣는가'가 아니라 **'무엇을 과감히 덜어내는가'**에서 결정된다.
            </p>
            <p>
              천편일률적인 슬롭으로 뒤덮여 가던 개발 생태계에 <code>Hallmark</code>가 던진 메시지는 명확하다. 
              화려한 애니메이션과 화려한 그라디언트로 본질을 가리려 하지 마라. 
              사용자가 해결하고자 하는 문제를 가장 정갈하고 솔직한 활자로 전달할 때, 소프트웨어는 비로소 인간의 영혼과 공명한다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://www.usehallmark.com" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 웹사이트 및 테마 갤러리
              </a>
              <a href="https://www.youtube.com/results?search_query=hallmark+anti+ai+slop+design+hassan" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/Nutlope/hallmark" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 1 (hallmark) module loaded successfully.")
