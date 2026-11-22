# -*- coding: utf-8 -*-
# Story 5: colbymchenry/codegraph

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] colbymchenry/codegraph                           -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_codegraph.jpg" alt="CodeGraph Rust Semantic Code Knowledge Graph Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="network" style="width:12px;height:12px;fill:#fff;"></i> RUST CODE GRAPH</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#f3e8ff; border-color:#7e22ce; color:#581c87;">🕸️ 토큰 62%·비용 44% 절감 · grep 노가다를 끝낸 100% 로컬 Rust 코드 그래프</span>
              <span class="platform-tag">GitHub Trending &amp; MCP</span>
              <span class="platform-tag">colbymchenry / codegraph</span>
            </div>

            <h2 class="article-headline">
              "에이전트가 grep으로 파일 40개를 뒤지게 두지 마라" — 20개 언어 AST·호출 그래프를 로컬 SQLite에 박아 토큰을 62% 아끼는 'CodeGraph'
            </h2>

            <div class="article-subheadline">
              tree-sitter 기반 Rust 네이티브 커널이 심볼·호출 엣지·프레임워크 라우트(Express/FastAPI/Next/Axum 등)를 .codegraph/codegraph.db(SQLite+FTS5)에 사전 인덱싱, 단일 MCP 도구 codegraph_explore로 18종 코딩 에이전트 즉시 연결 (+101스타/일, 누적 78,414스타, MIT)
            </div>
            <p class="article-snippet">
              코딩 에이전트에게 "이 요청이 데이터베이스까지 어떻게 흐르는지" 묻거나 함수 시그니처를 고치라고 시키면, 에이전트는 수십 번씩 <code>grep</code>, <code>glob</code>, <code>Read</code>를 반복하며 컨텍스트 윈도우와 API 비용을 태웁니다. 오늘 하루 <strong>+101스타(누적 78,414스타)</strong>를 기록한 <strong>colbymchenry/codegraph</strong>는 <strong>Rust 커널</strong>로 20여 개 언어의 심볼과 동적 디스패치·프레임워크 라우트까지 100% 로컬 SQLite 지식 그래프로 사전 구축하고, <code>codegraph_explore</code> 단 하나의 MCP 도구로 정확한 호출 경로와 수정 파급 범위(Blast Radius)를 1회 호출로 건네 평균 <strong>토큰 62%·비용 44% 절감</strong>을 달성했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 탐색에만 43번의 툴 호출을 태우던 에이전트의 눈을 뜨게 하다
            </h3>
            <p>
              대형 코드베이스에서 코딩 에이전트가 비싸고 느려지는 진짜 이유는 모델의 코딩 실력이 부족해서가 아니다. 에이전트가 코드를 고치기 전에 '코드 구조 지도'를 매번 맨손으로 다시 그려야 하기 때문이다. 파일 하나를 열고 임포트를 확인한 뒤, 또 다른 파일을 <code>grep</code>으로 뒤지고, 인터페이스 구현체를 찾느라 수십 턴을 허비하는 동안 컨텍스트 창은 관련 없는 코드 조각들로 가득 찬다.
            </p>
            <p>
              <strong>colbymchenry/codegraph</strong>(누적 <strong>78,414스타</strong>, 최신 v1.6.4)는 이 원시적인 파일 크롤링을 끝내기 위해 태어났다. 코드가 바뀔 때마다 자동 동기화되는 로컬 시맨틱 지식 그래프를 미리 구워두어, 에이전트가 파일을 한 장씩 넘겨보는 대신 그래프 데이터베이스에 단 한 번 질의해 정확한 소스 코드와 호출 경로, 변경 영향 반경(Blast Radius)을 즉시 받아오게 만든다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "수많은 MCP 메뉴 대신 단 하나의 강력한 도구 'codegraph_explore'"
            </h3>
            <p>
              CodeGraph의 벤치마크 데이터는 정밀한 컨텍스트가 곧바로 돈과 속도로 직결됨을 보여준다. 7개 벤치마크 저장소 대상 재측정(2026-08)에서 CodeGraph를 연결한 에이전트는 일반 파일 탐색 에이전트 대비 평균 <strong>토큰 62% 감소, API 비용 44% 절감</strong>을 기록했으며, 특히 기존 에이전트가 28~43번의 툴 호출을 써야 했던 심층 구조 추적 질문에서는 비용 절감 폭이 <strong>57~78%</strong>까지 치솟았다.
            </p>

            <div class="editorial-quote">
              <p>
                "측정된 에이전트 행동 분석 결과, 좁은 기능의 도구 메뉴를 여러 개 던져주는 것보다 <strong>단 하나의 강력한 도구(<code>codegraph_explore</code>)를 제공하는 편이 오선택을 줄이고 매 세션 컨텍스트를 아낀다.</strong>"
              </p>
              <small>— colbymchenry/codegraph 공식 아키텍처 &amp; 벤치마크 보고서 (MIT License)</small>
            </div>

            <p>
              무엇보다 주목할 점은 <strong>정직한 정적 분석 커버리지 공개</strong>다. CodeGraph는 추상적 홍보 문구 대신 22개 언어별 오픈소스 대표 저장소에서 '교차 파일 의존성 해석률(Fair Coverage)'을 실측해 공개했다. Python(<code>psf/requests</code>)·PHP(<code>guzzle</code>)·Ruby(<code>sidekiq</code>)·SvelteKit은 <strong>100%</strong>, Go(<code>gin</code>) 96.6%, Kotlin(<code>okhttp</code>) 96.2%, TypeScript 95.8%, Swift(<code>Alamofire</code>) 95.3%, Rust(<code>ripgrep</code>) 86.7%를 기록했고, Express·Flask·Axum·Vapor·React Router 라우팅은 100%, FastAPI 98%까지 추적한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Rust tree-sitter 커널·SQLite FTS5·18종 에이전트 원클릭 배선
            </h3>
            <p>
              Node.js 설치조차 필요 없는 단일 자립형 바이너리(<code>install.sh</code> / <code>npm i -g @colbymchenry/codegraph</code>) 내부는 3단계 로컬 파이프라인으로 움직인다:
            </p>
            <ul>
              <li><strong>네이티브 Rust + tree-sitter 고속 추출 커널:</strong> 컴파일된 Rust 커널이 20여 개 언어의 소스 코드를 tree-sitter 문법 트리로 고속 파싱해 함수·클래스·메서드 노드와 호출(calls)·임포트(imports)·상속(extends)·구현(implements)·동적 디스패치 엣지를 추출한다. 단순 텍스트 <code>grep</code>이 놓치는 프레임워크 컨벤션 라우트와 iOS/React Native/Expo 크로스 브리지 호출까지 엣지로 엮는다.</li>
              <li><strong>로컬 SQLite + FTS5 지식 그래프(<code>.codegraph/codegraph.db</code>):</strong> 추출된 그래프와 심볼 참조 해석 결과는 외부 클라우드 DB가 아닌 프로젝트 루트의 로컬 SQLite 파일과 FTS5 전문 검색 인덱스에 저장되며, 코드가 수정되면 자동으로 증분 동기화된다.</li>
              <li><strong><code>codegraph install</code> 18종 에이전트 자동 연결:</strong> 설치 후 <code>codegraph install</code> 명령 한 줄이면 Claude Code, Cursor, Codex CLI, OpenCode, Antigravity IDE, Gemini CLI, Hermes Agent, Kiro, GitHub Copilot, Windsurf, Factory Droid, Pi 등 18개 주요 코딩 에이전트 설정을 자동 감지해 CodeGraph MCP 서버를 배선한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">CodeGraph Rust tree-sitter 추출 → SQLite 그래프 → 단일 MCP 도구 호출 구조</span>
                <span class="schematic-badge">Rust Kernel + TS · MIT · 78.4k★ · 62% Fewer Tokens</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Rust tree-sitter Kernel</div>
                  <div class="schematic-desc">
                    22개 언어 AST 파싱 &amp; 심볼/엣지 추출<br>
                    Express·FastAPI·Axum 등 라우트 인식<br>
                    iOS ↔ React Native/Expo 브리지 해석<br>
                    코드 변경 시 100% 로컬 자동 증분 동기화
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. SQLite + FTS5 Graph DB</div>
                  <div class="schematic-desc">
                    <code>.codegraph/codegraph.db</code> 로컬 저장<br>
                    심볼·호출 엣지·파일·FTS5 전문 색인<br>
                    호출 경로 추적 &amp; 수정 파급(Blast Radius)<br>
                    Python/Svelte 100% · TS 95.8% 커버리지
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Single-Tool MCP Bridge</div>
                  <div class="schematic-desc">
                    <code>codegraph_explore</code> 단 1개 도구 노출<br>
                    <code>codegraph install</code>로 18종 에이전트 배선<br>
                    Explore 서브에이전트 왕복 호출 제거<br>
                    평균 <strong>토큰 62%·API 비용 44%</strong> 절감
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">CodeGraph 공식 문서 플랫폼 실화면 — 20+ 언어 AST 그래프 및 18종 에이전트 MCP 연동</span>
              </div>
              <img src="../assets/images/demo_codegraph.png" alt="CodeGraph Official Documentation Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ colbymchenry.github.io/codegraph 실화면: Node.js 의존성 없는 자립형 Rust 커널 설치, 18종 코딩 에이전트 원클릭 MCP 연결, 언어별 교차 파일 커버리지 벤치마크.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: '무작정 컨텍스트 붓기'에서 '수술적 그래프 인출'로의 전환
            </h3>
            <p>
              그동안 AI 코딩 도구의 토큰 과금은 모델 회사들의 매출을 끌어올리는 동시에 기업 개발팀에는 월 수천 달러의 API 청구서로 돌아왔다. 특히 에이전트가 코드 구조를 모른 채 수십 번씩 파일을 읽는 탐색 비용은 순수한 비효율이었다.
            </p>
            <ul>
              <li><strong>로컬 MIT 코어 + 호스팅 PR 인텔리전스 플랫폼:</strong> CodeGraph는 로컬 그래프 엔진을 MIT로 완전 공개해 7만 8천 명의 개발자를 확보한 뒤, 모든 PR마다 "무엇을 테스트해야 하는지, 어떤 비즈니스 로직과 플로우가 깨질 수 있는지" 자동 분석해 주는 호스팅 플랫폼(<code>getcodegraph.com</code>)으로 자연스러운 상용화 다리를 놓았다.</li>
              <li><strong>프라이버시 완벽 보존:</strong> 기업 코드베이스가 외부 벡터 DB나 클라우드 인덱서로 업로드되지 않고 개발자 머신의 <code>.codegraph/codegraph.db</code>에만 머무르기 때문에 보안 심사가 까다로운 사내 모노레포에서도 즉시 도입할 수 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 에이전트 시대의 컴파일러는 코드를 기계어로만 바꾸지 않는다, 지식으로 바꾼다
            </h3>
            <p>
              인간 개발자가 IDE의 '정의로 이동(Go to Definition)'과 호출 계층 트리에 의지해 코딩하듯, AI 에이전트에게도 무작위 문자열 검색(grep)이 아니라 컴파일러 수준의 시맨틱 그래프가 필요했다.
            </p>
            <p>
              코드가 커질수록 에이전트가 멍청해지고 비싸지던 오래된 고민 앞에서, <code>CodeGraph</code>는 정갈한 답을 내놓는다. 모델 창을 무조건 키우기 전에, 먼저 코드의 지도를 그려 손에 쥐여주라.
            </p>

            <div class="project-links">
              <a href="https://colbymchenry.github.io/codegraph/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> CodeGraph 공식 문서
              </a>
              <a href="https://www.youtube.com/results?search_query=CodeGraph+colbymchenry+MCP+AI+coding+agent" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/colbymchenry/codegraph" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
