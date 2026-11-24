# -*- coding: utf-8 -*-
# Story 5: malisper/pgrust (Postgres Rewritten in Rust with Gravity JIT Engine)

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] malisper/pgrust : Postgres Rewritten in Rust     -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_pgrust.jpg" alt="pgrust Postgres Rewritten in Rust Gravity JIT Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="database" style="width:12px;height:12px;"></i> RUST DB &amp; WASM REPL</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🐘 ClickHouse보다 최대 3배 빠른 Rust Postgres · ★6,049</span>
              <span class="platform-tag">GitHub Rust Trending &amp; WASM</span>
              <span class="platform-tag">malisper / pgrust</span>
            </div>

            <h2 class="article-headline">
              "ClickHouse보다 최대 3배 빠른 100% 호환 Rust Postgres" — Gravity JIT 엔진과 OOM 해방을 선언한 'pgrust'
            </h2>

            <div class="article-subheadline">
              Postgres 18.6 유선 프로토콜·SQL 문법을 완벽 호환하면서 x86·ARM·WASM을 겨냥한 Lisp IR 기반 Gravity 벡터라이즈드 JIT 엔진, 풀 MVCC 컬럼형 스토리지(pgrcolumnar), 자동 메모리 관리자, 브라우저 내 WASM 서버까지 구현 (AGPL-3.0)
            </div>
            <p class="article-snippet">
              "올림픽급 트랜잭션 안정성을 갖춘 PostgreSQL이지만, 수억 건의 분석 쿼리를 돌릴 때면 여전히 ClickHouse나 DuckDB로 데이터를 복제해야 한다." 이 낡은 공식을 Rust로 0부터 다시 써 내려가며 깨뜨린 프로젝트 <strong>malisper/pgrust</strong>(<strong>★6,049</strong>)가 오늘 GitHub Rust 트렌딩에 다시금 불을 지폈습니다. 최신 <code>v0.4-beta</code>에서는 Lisp 기반 중간표현(IR)으로 재작성한 신규 <strong>Gravity JIT 쿼리 엔진</strong>을 탑재해 ClickBench에서 <strong>ClickHouse보다 최대 3배</strong>, 기존 Postgres 로우 스토어 위에서도 <strong>최대 5배</strong> 빠른 속도를 내며, 수천 건의 장애 원인이었던 OOM 킬러 문제까지 통합 메모리 예산으로 정면 해결했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 브라우저 주소창 안에서 부팅되는 '2026년형 Postgres'
            </h3>
            <p>
              <code>pgrust.com</code>에 접속하면 설치 과정도, 도커 컨테이너도 없이 웹 브라우저 탭 하나 안에서 완전한 PostgreSQL 호환 서버가 WebAssembly로 즉시 부팅된다. 터미널에서 <code>psql</code>이나 기존 ORM, 드라이버를 그대로 찔러 넣어도 PostgreSQL 18.6과 똑같은 와이어 프로토콜과 SQL 시맨틱스로 응답한다.
            </p>
            <p>
              하지만 그 내부는 30년 된 C 코드베이스와 완전히 다른 짐승이다. 개발자 Michael Malis는 기존의 C 기반 PostgreSQL을 부분 패치하거나 확장(Extension)으로 땜질하는 대신, <em>"2026년에 PostgreSQL을 처음부터 다시 설계한다면 어떤 모습일까?"</em>라는 질문을 던지고 코드 한 줄 한 줄을 Rust로 다시 작성해 올렸다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: OLTP와 OLAP의 이원화 비용, 그리고 'Postgres 장애의 4대 기사' 종식
            </h3>
            <p>
              현대 백엔드 팀들은 데이터베이스 하나로 버티지 못해 Postgres에서 CDC 파이프라인을 깔고 ClickHouse나 Snowflake 같은 별도 분석 엔진으로 데이터를 옮겨 이중 운영 비용을 치른다. 게다가 운영 중인 Postgres는 복잡한 <code>work_mem</code>·공유 버퍼 튜닝이 조금만 어긋나도 단일 폭주 쿼리가 OS의 OOM(Out-Of-Memory) 킬러를 불러와 데이터베이스 전체를 셧다운시키곤 한다.
            </p>

            <div class="editorial-quote">
              <p>
                "Gravity는 ClickHouse보다 최대 3배 빠른 신규 벡터라이즈드 JIT 엔진이며, Postgres 로우 스토어 위에서도 최대 5배 빠르게 동작한다. <strong>하나의 통합 메모리 예산이 버퍼 풀·컬럼 캐시·실행 중인 쿼리를 통제해 OS OOM 킬러가 DB 전체를 죽이는 비극을 막는다.</strong>"
              </p>
              <small>— Michael Malis, pgrust v0.4-beta 릴리스 노트 및 아키텍처 명세</small>
            </div>

            <p>
              이 프로젝트가 최근 다시 폭발적인 관심을 끄는 또 하나의 이유는 개발자가 공개한 에세이 <em>"AI가 JIT 컴파일러의 경제학을 어떻게 바꾸는가(How AI Changes the Economics of JIT Compilers)"</em>다. 과거에는 소수의 거대 상용 DB 벤더만 감당하던 고성능 다중 아키텍처 JIT 쿼리 엔진 개발을, AI 코딩 도구와 정형 검증 테스트 하네스의 결합으로 1인·소규모 팀이 실전 수준으로 밀어붙일 수 있게 된 시대의 단면이기 때문이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Lisp IR 기반 Gravity JIT와 풀 MVCC 컬럼형 인덱스
            </h3>
            <p>
              <code>pgrust</code>가 호환성과 극한의 분석 성능을 동시에 거머쥔 핵심 기술 기둥은 크게 세 가지다:
            </p>
            <ul>
              <li><strong>Gravity 벡터라이즈드 푸시 기반 JIT (Lisp IR):</strong> 기존 v0.2 엔진이 ARM64만 지원하며 ClickHouse를 18.5% 앞서는 데 그쳤다면, <code>v0.4-beta</code>의 Gravity는 자체 설계한 저수준 <strong>Lisp 기반 중간표현(IR)</strong>을 도입해 <strong>x86·ARM·WASM</strong> 3대 타깃으로 최적화된 네이티브 기계어를 즉석 생성한다. 이를 통해 Postgres의 복잡한 타입 시스템과 NULL 시맨틱스를 유지하면서도 전용 분석 엔진인 ClickHouse보다 최대 3배 빠른 처리량을 달성했다.</li>
              <li><strong>풀 MVCC <code>pgrcolumnar</code> &amp; 로우 스토어 하이브리드:</strong> 기존 Postgres 컬럼형 확장들은 행 단위 업데이트가 느리거나 Append-only 제약, 인덱스 부재에 시달렸다. <code>pgrcolumnar</code>는 완전한 MVCC 트랜잭션을 지원해 동시 읽기와 쓰기를 보장하며, 기존 로우 스토어 테이블 위에도 컬럼형 인덱스를 직접 얹어 데이터 이관 없는 HTAP를 구현한다.</li>
              <li><strong>스레드 기반 동시성 &amp; 쿼리 스케줄러:</strong> 프로세스 포크(Fork) 모델 대신 스레드 기반 아키텍처와 공정 쿼리 스케줄러, <code>jsonb</code> 네이티브 통계, 그리고 <code>work_mem</code> 수동 튜닝이 필요 없는 통합 자동 메모리 관리자를 탑재해 폭주 쿼리 하나가 서버 전체를 마비시키는 현상을 구조적으로 차단한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">pgrust Gravity JIT · MVCC Columnar · 자동 메모리 통합 아키텍처</span>
                <span class="schematic-badge">Postgres 18.6 Wire Compatible · Pure Rust · AGPL-3.0</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Drop-in PG 18.6 Front</div>
                  <div class="schematic-desc">
                    기존 <code>psql</code> · ORM · 드라이버 무수정<br>
                    <code>bin/postgres</code> · <code>initdb</code> 독립 바이너리<br>
                    스레드 기반 동시성 &amp; 쿼리 스케줄러<br>
                    브라우저 내 WebAssembly REPL 즉시 실행
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Gravity Vectorized JIT</div>
                  <div class="schematic-desc">
                    저수준 Lisp IR → x86 / ARM / WASM 컴파일<br>
                    Push 기반 벡터 실행 + 어셈블리 최적화<br>
                    ClickBench: ClickHouse 대비 최대 <strong>3×</strong> 고속<br>
                    기존 로우 스토어 쿼리 최대 <strong>5×</strong> 가속
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Unified Storage &amp; OOM Guard</div>
                  <div class="schematic-desc">
                    <code>pgrcolumnar</code> 풀 MVCC 동시 읽기/쓰기<br>
                    로우 테이블 위 직접 얹는 컬럼형 인덱스<br>
                    버퍼 풀·캐시·쿼리 단일 메모리 예산 통제<br>
                    수동 <code>work_mem</code> 제거 및 OOM 킬러 방지
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">pgrust.com 공식 웹 REPL 실화면 — 브라우저 WebAssembly 위에서 즉석 구동되는 Rust Postgres 엔진</span>
              </div>
              <img src="../assets/images/demo_pgrust.png" alt="pgrust Browser WebAssembly Postgres Server" class="showcase-img">
              <p class="showcase-caption">
                ▲ pgrust.com 실화면: 설치 없이 웹 브라우저 내 WASM으로 컴파일된 pgrust 서버와 Gravity JIT 엔진, 릴리스 바이너리 배포 안내.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: '재작성의 경제학'과 클라우드 OLAP 시장의 압박
            </h3>
            <p>
              수십 년간 데이터베이스 시장은 "OLTP는 Postgres/MySQL, OLAP은 Snowflake/ClickHouse/BigQuery"라는 분업 구조로 수십조 원대 매출을 나눠 가졌다. <code>pgrust</code>가 <code>AGPL-3.0</code>과 월간 폐쇄형 드롭을 버리고 공개 연속 개발(Developing in the open)로 전환한 것은, "Postgres 드라이버를 꽂은 채 곧바로 초고속 컬럼형 분석까지 처리하고 싶다"는 개발자들의 오랜 염원을 정확히 겨냥한다.
            </p>
            <ul>
              <li><strong>100% 호환의 공포와 가능성:</strong> 호환성은 데이터베이스 생태계에서 가장 강력한 무기다. 기존 Postgres 확장과 C ABI 100% 대체까지는 아직 갈 길이 남아 있지만, 리드-리플리카나 분석용 사이드카 자리에서 기존의 무거운 CDC+DW 파이프라인을 단일 바이너리 <code>pgrust</code>로 치환하려는 실험만으로도 상용 클라우드 DW 벤더들에게는 불편한 균열이 된다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 코끼리가 제트 엔진을 달았을 때
            </h3>
            <p>
              데이터베이스 역사는 오랫동안 "안정성을 원하면 속도를 포기하고, 분석 속도를 원하면 호환성을 포기하라"는 타협의 연속이었다. 그러나 안전과 성능을 모두 노리는 Rust, 그리고 AI가 낮춘 컴파일러 제작 비용이 만나자, 수십 년 묵은 코끼리(PostgreSQL)의 등 위에 제트 엔진이 달리기 시작했다.
            </p>
            <p>
              브라우저 탭 하나에서 <code>psql</code> 명령이 번개처럼 돌아가는 오늘의 풍경은, 머지않아 우리가 데이터를 두 곳으로 복사하던 시절을 낯선 유물처럼 돌아보게 될 것임을 암시한다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/watch?v=7L_nG3EBjck" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://pgrust.com" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 브라우저 WASM 데모 실행
              </a>
              <a href="https://github.com/malisper/pgrust" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
