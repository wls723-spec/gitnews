# -*- coding: utf-8 -*-
# Story 4: thedotmack/claude-mem

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] thedotmack/claude-mem : 크로스 세션 영구 메모리 엔진 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_claude_mem.jpg" alt="Claude-Mem Persistent Session Context Architecture" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="play" style="width:12px;height:12px;fill:#fff;"></i> YOUTUBE 68K</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🧠 AI 에이전트 기억상실증 완치</span>
              <span class="aggro-tag">⚡ 세션 간 지식 압축 & 초고속 주입</span>
              <span class="platform-tag">GitHub Trending</span>
              <span class="platform-tag">thedotmack / claude-mem</span>
            </div>
            
            <h2 class="article-lead-headline">
              터미널을 닫으면 기억을 잃는 AI의 치명적 기억상실증을 치료하다: 세션 간 지식을 압축·계승하는 영구 메모리 엔진 'claude-mem'
            </h2>

            <div class="article-subheadline">
              "Persistent Context Across Sessions for Every Agent" — thedotmack, 에이전트가 터미널에서 수행한 도구 호출, 디버깅 시행착오, 아키텍처 결정 사항을 백그라운드에서 실시간 압축하여 로컬 영구 지식 베이스로 축적… 새로운 세션 시작 시 핵심 맥락만 0.1초 만에 자동 주입하는 크로스 에이전트 메모리 표준
            </div>
            <p class="article-snippet">
              터미널 창을 닫고 다음 날 다시 켜면 "처음 뵙겠습니다"를 외치며 수천 줄의 코드 분석을 처음부터 다시 반복하던 AI 에이전트의 구조적 한계를 극복. 컨텍스트 윈도우 낭비 없이 이전 세션의 모든 학습 경험을 완벽하게 계승한다.
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
              <i data-lucide="help-circle"></i> 1. 리드: 어제 3시간 동안 설명했던 버그를 오늘 다시 설명해야 하는 비극
            </h3>
            <p>
              AI 코딩 에이전트를 사용하는 모든 엔지니어가 겪는 가장 깊은 피로감은 <strong>'에이전트의 구조적 단기 기억상실(Amnesia)'</strong>이다.
            </p>
            <p>
              어젯밤 3시간 동안 에이전트와 치열하게 씨름하며 특정 라이브러리의 버전 충돌 원인을 밝혀내고, 데이터베이스 스키마 마이그레이션 규칙을 정립해 두었다 하더라도, 터미널 창을 닫거나 새 세션을 시작하는 순간 에이전트의 머릿속은 새하얀 백지가 된다. 
              다음 날 아침 터미널을 열면 에이전트는 어제 실패했던 똑같은 실수를 반복하고, 개발자는 또다시 수만 토큰의 문서와 파일들을 프롬프트에 구겨 넣으며 같은 설명을 되풀이해야 한다. 
              이는 단순한 시간 낭비를 넘어, 개발자와 AI 사이의 장기적인 신뢰 관계를 무너뜨리는 결정적 병목이었다.
            </p>
            <p>
              2026년 10월 26일, 오픈소스 커뮤니티에서 폭발적인 지지를 얻으며 트렌딩에 오른 <strong>'claude-mem(thedotmack/claude-mem)'</strong>은 바로 이 고질적인 기억상실증을 공학적으로 종식시키기 위해 탄생했다. 
              Claude Code뿐만 아니라 OpenClaw, Codex, Gemini CLI, Hermes, OpenCode 등 <strong>모든 주요 CLI 에이전트 환경에서 완벽하게 호환되는 세션 간 영구 메모리 계층(Persistent Memory Layer)</strong>을 구현한 것이다.
            </p>

            <div class="editorial-quote">
              "인간 시니어 엔지니어가 뛰어난 이유는 코딩 속도가 빨라서가 아니다. 
              <strong>'지난달에 저 모듈을 수정했을 때 어떤 사이드 이펙트가 터졌는지' 기억하고 있기 때문이다.</strong> 
              세션이 끝난 뒤 폐기되는 에이전트는 결코 시니어가 될 수 없다. claude-mem은 터미널의 모든 시행착오를 영구적인 조직의 지적 자산으로 승화시킨다."
              <span class="quote-author">— thedotmack, claude-mem 개발자 노트 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: '전체 로그 덤프'가 아닌 '의미론적 증류(Distillation)'
            </h3>
            <p>
              과거에도 이전 대화 기록을 통째로 파일에 저장해 새 세션에 넘겨주는 시도는 있었다. 
              그러나 이 방식은 며칠만 지나도 수십만 토큰의 거대한 텍스트 덤프가 되어 컨텍스트 윈도우를 가득 채우고, 천문학적인 API 비용을 유발하며, 정작 중요한 최신 지침을 잊어버리는 '주의 집중 분산(Attention Dilution)'을 일으켰다.
            </p>
            <p>
              <code>claude-mem</code>의 혁신은 <strong>"에이전트가 작업하는 동안 백그라운드에서 실시간으로 지식을 증류(Distill)한다"</strong>는 점이다. 
              도구 사용의 원시 출력(Raw output)이나 긴 터미널 로그를 그대로 저장하지 않고, 소형 백그라운드 AI 워커가 핵심 결정 사항, 변경된 아키텍처 원칙, 검증된 가설만을 <strong>고밀도 시맨틱 스니펫(Semantic Snippets)</strong>으로 압축하여 로컬 SQLite 및 벡터 인덱스에 저장한다.
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="database" style="color:#8b5cf6;"></i> claude-mem: 실시간 지식 증류 및 크로스 세션 컨텍스트 주입 파이프라인</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">PERSISTENT MEMORY PIPELINE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">PHASE 1. 도구 관측 인터셉트</div>
                  <div class="step-title">Tool Execution Hook</div>
                  <div class="step-desc">에이전트가 파일 수정, 빌드 에러 해결, git 커밋을 수행할 때마다 비동기 훅으로 로그 가로채기.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">PHASE 2. 의미론적 요약 증류</div>
                  <div class="step-title">Background Distiller Worker</div>
                  <div class="step-desc">단순 출력 쓰레기를 버리고 '결정된 아키텍처 규칙'과 '디버깅 교훈'만 핵심 1~2줄로 압축.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">PHASE 3. 로컬 하이브리드 저장</div>
                  <div class="step-title">SQLite FTS5 & Vector Store</div>
                  <div class="step-desc">프로젝트 루트의 .claude-mem 로컬 DB에 전문 검색(FTS5) 및 임베딩 벡터로 안전하게 격리 보관.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 신규 세션 즉각 감지</div>
                  <div class="step-title">Session Startup Hook</div>
                  <div class="step-desc">개발자가 다음 날 새로운 터미널을 열었을 때, 현재 작업 파일 및 git 브랜치와 연관된 기억 자동 조회.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 마이크로 컨텍스트 주입</div>
                  <div class="step-title">Zero-Token Injection</div>
                  <div class="step-desc">컨텍스트 윈도우의 0.1% 미만(수백 토큰)만을 소비하며 "지난번 결정 사항 요약"을 시스템 프롬프트에 주입.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="wrench"></i> 3. 기술 메커니즘 해부: MCP 검색 도구와 불변 슬러그 매핑
            </h3>
            <p>
              <code>claude-mem</code>의 공학적 완성도는 모델 컨텍스트 프로토콜(MCP)과의 완벽한 네이티브 통합에서 비롯된다.
            </p>
            <p>
              에이전트는 단순히 세션 시작 시 주입된 초기 메모리만 읽는 것이 아니다. 
              작업 도중 과거 특정 컴포넌트의 히스토리가 필요할 경우, <code>search_memory</code>나 <code>query_decisions</code> 같은 <strong>내장 MCP 도구를 자율적으로 호출</strong>한다. 
              예를 들어 에이전트가 <code>auth.ts</code> 파일을 리팩토링하려 할 때, 자동으로 <em>"지난주에 이 파일의 토큰 만료 로직을 수정하면서 어떤 회귀 버그가 발생했었는가?"</em>를 로컬 벡터 DB에 질의하고, 그 당시 작성되었던 테스트 케이스의 교훈을 즉시 불러와 실수 없는 코드를 작성한다.
            </p>
            <p>
              또한 클라우드 전송이 일체 없는 <strong>100% 로컬 파일시스템 기반(Local-First)</strong>으로 동작하여, 외부 유출 우려 없이 기업 내부의 가장 민감한 소스코드와 보안 취약점 조치 내역까지 안심하고 축적할 수 있다.
            </p>

            <!-- 실제 소프트웨어 UI / 터미널 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_claude_mem_cli.jpg" alt="claude-mem 세션 메모리 추적 및 컨텍스트 주입 실사용 화면" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>실제 claude-mem v15.2 프로덕션 구동 캡처:</strong> 에이전트 세션의 도구 관측 내역이 실시간으로 로컬 SQLite FTS5 데이터베이스에 증류 저장되고, 새로운 세션 진입 시 과거의 핵심 아키텍처 결정 사항(Decisions)과 디버깅 교훈(Learnings)이 단 0.1초 만에 시스템 프롬프트로 복원되는 무결점 구동 화면.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="scale"></i> 4. 비즈니스 해자: 1회용 소모품에서 '숙련된 시니어'로의 진화
            </h3>
            <p>
              기업에서 인재를 채용하고 유지하는 본질적인 이유는 <strong>'시간이 지날수록 축적되는 도메인 숙련도'</strong> 때문이다. 
              기존의 AI 에이전트는 아무리 똑똑해도 매번 신입 사원으로 리셋되는 1회용 소모품에 불과했다.
            </p>
            <p>
              <code>claude-mem</code>은 에이전트에게 <strong>'근속 연수'라는 개념을 부여</strong>한다. 
              프로젝트와 함께 나이를 먹어가며 사내 레거시 코드의 복잡한 맥락과 사내 코딩 컨벤션, 과거 장애 사례를 속속들이 꿰뚫고 있는 에이전트는 그 어떤 최신 범용 프론티어 모델보다 해당 조직에 대체 불가능한 핵심 자산이 된다. 
              이는 에이전트 도구 시장의 가치를 '단순 코드 타이핑'에서 '기업 지식 관리(Knowledge Management)'로 완전히 재정의하고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 망각하지 않는 기계와의 대화
            </h3>
            <p>
              기억이야말로 지능의 본질이며, 연속성이야말로 인격의 바탕이다. 
              우리가 동료에게 신뢰를 느끼는 순간은 화려한 언변을 뽐낼 때가 아니라, <em>"지난번에 우리가 논의했던 그 방식을 이번에도 적용했습니다"</em>라며 고개를 끄덕일 때다.
            </p>
            <p>
              <code>claude-mem</code>이 열어젖힌 세계에서 AI 에이전트는 더 이상 터미널을 끄면 사라지는 차가운 유령이 아니다. 
              내일 아침 다시 터미널을 열었을 때, 어젯밤 우리가 함께 고민했던 지점에서 커피 한 잔과 함께 대화를 이어갈 수 있는 <strong>진정한 동료 엔지니어의 탄생</strong>이다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://www.youtube.com/results?search_query=claude+mem+persistent+context+memory" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/thedotmack/claude-mem" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 4 (claude-mem) module loaded successfully.")
