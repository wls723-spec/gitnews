# -*- coding: utf-8 -*-
# Story 5: t8y2/dbx

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] t8y2/dbx                                         -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_dbx.jpg" alt="DBX 25MB Rust 100+ Database Client Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="database" style="width:12px;height:12px;fill:#fff;"></i> 25MB RUST ENGINE</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ffedd5; border-color:#ea580c; color:#9a3412;">🗄️ 25MB Rust 바이너리로 100종 DB+MCP 통합 · DataGrip·DBeaver 대체제 (+95★/일)</span>
              <span class="platform-tag">GitHub Rust Trending &amp; dbxio.com</span>
              <span class="platform-tag">t8y2 / dbx</span>
            </div>

            <h2 class="article-headline">
              "무거운 일렉트론·JVM 대신 25MB Rust 한 방에 100개 DB를 얹었다" — AI 에이전트용 MCP까지 품은 초경량 데이터 워크벤치 'DBX'
            </h2>

            <div class="article-subheadline">
              MySQL·PostgreSQL·DuckDB·ClickHouse·Redis·MongoDB·Qdrant·Kafka·etcd 등 100여 종 DB 및 미들웨어 지원, 서명된 샌드박스 플러그인과 3단계 권한(read_only/safe_write/high_risk_write) Rust MCP 서버(@dbx-app/mcp-server) 통합 (+95스타/일, 누적 31,224스타, Apache-2.0)
            </div>
            <p class="article-snippet">
              SQL 쿼리 하나 날리려고 1GB에 육박하는 JVM 기반 IDE나 크로미움이 통째로 묶인 일렉트론 DB 클라이언트를 띄우던 시대에 균열이 가고 있습니다. 오늘 GitHub Rust 트렌딩에서 <strong>95개의 스타를 보태며 누적 31,224스타</strong>에 올라선 <strong>t8y2/dbx</strong>는 <strong>단 ~25MB 크기의 네이티브 앱</strong> 안에 100여 개 이상의 관계형·벡터·시계열·NoSQL·메시지 큐(Kafka/RabbitMQ) 드라이버와 DuckDB 기반 Parquet 즉시 미리보기, 그리고 클로드 코드·커서가 DB에 안전하게 접근할 수 있는 전용 <strong>Rust MCP 서버(<code>@dbx-app/mcp-server</code>)</strong>까지 통합해 데스크톱·Docker·CLI 전 영역을 공략하고 있습니다.
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
              <i data-lucide="flame"></i> 1. 리드: "왜 단순 쿼리 툴 하나 띄우는 데 RAM 2GB가 필요한가"
            </h3>
            <p>
              백엔드 엔지니어와 데이터 분석가의 노트북에서 가장 메모리를 많이 잡아먹는 주범 중 하나는 늘 데이터베이스 GUI 툴이었다. JetBrains DataGrip은 무거운 JVM 런타임을 띄워야 하고, DBeaver는 Eclipse RCP 프레임워크와 수많은 Java 드라이버 JAR에 묶여 있으며, 신생 웹 기반 DB 클라이언트들은 일렉트론(Bundled Chromium) 때문에 300~500MB 설치 용량과 수백 MB의 기본 RAM 점유를 당연하게 요구한다.
            </p>
            <p>
              오늘 Rust 트렌딩 상단에 오른 <strong>t8y2/dbx</strong>의 README 최상단 첫 문장은 바로 그 피로감을 한 줄로 찔렀다. <strong>"25 MB 안에 담긴 100개 이상의 데이터베이스. 번들된 크로미움 없음(No bundled Chromium)."</strong> Apache-2.0 오픈소스로 공개된 이 프로젝트는 이미 3만 1천 개 이상의 스타와 2,842개의 포크를 모으며, 단순 '가벼운 SQL 에디터'를 넘어 AI 에이전트가 DB를 안전하게 탐색·실행하는 관문으로 진화했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "인간의 SQL 워크벤치와 AI 에이전트의 MCP 서버가 하나로 합쳐졌다"
            </h3>
            <p>
              개발자가 데이터베이스 GUI에 접속해 테이블 스키마를 뒤지고 데이터를 수정하던 일의 상당 부분을 이제는 코딩 에이전트(Claude Code, Cursor, Windsurf, Codex)가 대신한다. 문제는 개발자가 에이전트용 MCP 서버마다 프로덕션 DB 비밀번호와 커넥션 문자열을 평문 환경변수로 흩뿌려 놓기 시작하면서 심각한 보안 사고 위험이 커졌다는 점이다.
            </p>

            <div class="editorial-quote">
              <p>
                "DBX Settings → MCP에서 연결 허용 목록(Allowlist)과 <strong>Read only</strong>, <strong>Data read/write</strong>, <strong>Full access</strong> 모드를 중앙 통제한다. <strong>클라이언트 설정 파일에는 권한 변수나 DB 접속 자격 증명을 중복으로 적어둘 필요가 없다.</strong>"
              </p>
              <small>— t8y2/dbx 공식 MCP 아키텍처 명세 (Apache-2.0 License)</small>
            </div>

            <p>
              DBX는 데스크톱 앱에 이미 등록·암호화해 둔 커넥션 프로필과 SSH 터널, 권한 정책을 그대로 재사용하는 전용 Rust MCP 바이너리(<code>@dbx-app/mcp-server</code>)를 분리 배포한다. 에이전트가 테이블을 조회할 뿐만 아니라, 필요하면 DBX UI 창에서 직접 해당 테이블을 띄워 인간에게 보여줄 수도 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 25MB 네이티브 코어·DuckDB 인메모리 프리뷰·서명된 사이드카 플러그인
            </h3>
            <p>
              25MB라는 믿기 힘든 체급 속에 100여 종의 데이터 시스템과 시각화 도구를 구겨 넣으면서도 안정성을 잃지 않은 비결은 세 가지 아키텍처 선택에 있다:
            </p>
            <ul>
              <li><strong>CodeMirror 6 + 가상 스크롤 + DuckDB 로컬 파일 엔진:</strong> 프론트엔드는 번들 크로미움 없이 OS 네이티브 웹뷰와 가상 스크롤 그리드를 결합해 대용량 결과셋을 처리한다. 로컬의 <code>Parquet</code>, <code>CSV</code>, <code>JSON</code> 파일을 창에 드래그 앤 드롭하면 내장된 <strong>DuckDB</strong> 엔진이 서버 연결 없이 즉시 SQL 프리뷰와 스키마 분석을 수행한다.</li>
              <li><strong>DB 넘어 미들웨어·벡터 DB까지 아우르는 100+ 커넥터 &amp; 서명 사이드카 플러그인:</strong> PostgreSQL·MySQL·SQLite·ClickHouse·Doris·CockroachDB 같은 SQL 엔진은 물론, Qdrant·Milvus·Weaviate(벡터 DB), Redis·MongoDB, Kafka·RocketMQ·RabbitMQ·Pulsar·MQTT(메시지 큐 토픽/컨슈머 그룹), Nacos·Consul·etcd(서비스 디스커버리)까지 통합했다. S3·Kubernetes·LDAP 확장은 서명 검증을 거친 뒤 <strong>독립 사이드카 프로세스로 샌드박싱 실행</strong>되는 Go/TS SDK 기반 플러그인 스토어로 분리해 코어 바이너리 비대화를 막았다.</li>
              <li><strong>3단계 중앙 통제 MCP 게이트웨이 &amp; 하이브리드 Web/Docker 모드:</strong> <code>npx @dbx-app/mcp-server</code>(또는 Node.js 없는 오프라인용 순수 Rust 바이너리)는 <code>read_only</code>, <code>safe_write</code>, <code>high_risk_write</code> 정책을 DBX 중앙 설정에 종속시킨다. 과거 환경변수(<code>DBX_MCP_ALLOW_WRITES=0</code>)로 쓰기를 막던 호환성은 유지하되, 환경변수로 중앙 쓰기 제한 정책을 절대 우회할 수 없도록 설계했으며, Docker 웹 백엔드(<code>DBX_WEB_URL</code>)와도 그대로 연동된다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">DBX 25MB 네이티브 코어 · 서명 사이드카 플러그인 · 3단 정책 MCP 아키텍처</span>
                <span class="schematic-badge">Rust · Apache-2.0 · 31.2k★ · ~25MB Binary · 100+ Connectors</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Multi-Surface 25MB Core</div>
                  <div class="schematic-desc">
                    Desktop (~25MB, No Chromium) · Docker · Web<br>
                    <code>@dbx-app/cli</code> 터미널/스크립트 워크플로<br>
                    CodeMirror 6 · ER 다이어그램 · Schema Diff<br>
                    내장 <strong>DuckDB</strong>로 Parquet/CSV/JSON 즉시 질의
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Central MCP &amp; AI Guard</div>
                  <div class="schematic-desc">
                    <code>@dbx-app/mcp-server</code> (독립 Rust 바이너리)<br>
                    <code>read_only</code> / <code>safe_write</code> / <code>high_risk_write</code><br>
                    연결 Allowlist 중앙 통제 &amp; 파괴적 SQL 확인창<br>
                    Claude·OpenAI·로컬 LLM 기반 AI SQL 어시스턴트
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. 100+ Engines &amp; Sandboxed Plugins</div>
                  <div class="schematic-desc">
                    RDBMS·Vector(Qdrant/Milvus)·Redis·MongoDB<br>
                    Kafka·Pulsar·MQTT 토픽 및 etcd/Consul 콘솔<br>
                    서명 검증된 Go/TS SDK 플러그인(S3·K8s·LDAP)<br>
                    독립 사이드카 프로세스 격리 + DBeaver/Navicat 임포트
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">dbxio.com 공식 플랫폼 실화면 — 25MB 초경량 Rust 멀티 데이터베이스 &amp; MCP 워크벤치</span>
              </div>
              <img src="../assets/images/demo_dbx.png" alt="DBX Official Platform Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ dbxio.com 실화면: 100여 개 데이터베이스·메시지 큐 통합 관리와 ER 다이어그램, AI SQL 어시스턴트, @dbx-app/mcp-server 정책 제어를 제공하는 DBX 공식 인터페이스.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 유료 상용 DB IDE 구독 모델에 가해진 '경량화 + MCP' 펀치
            </h3>
            <p>
              데이터베이스 GUI 시장은 오랫동안 TablePlus, Navicat, JetBrains DataGrip 같은 유료 상용 제품과 무거운 Java 기반 DBeaver가 양분해 왔다. DBX가 Apache-2.0 완전 오픈소스로 이 판을 흔드는 지점은 두 가지다:
            </p>
            <ul>
              <li><strong>기존 툴 사용자의 제로 마찰 이주(DBeaver/Navicat 임포트):</strong> DBX는 기존 DBeaver와 Navicat의 커넥션 프로필을 그대로 가져오는 임포터를 기본 탑재해 전환 비용을 0으로 낮췄다. 여기에 암호화된 설정 내보내기와 SSH 터널, 컬럼 단위 계보(Field Lineage) 분석 같은 유료 에디션 전용 기능들을 기본 포함시켰다.</li>
              <li><strong>개발자 도구 생태계의 새로운 해자 '에이전트 권한 평면':</strong> 앞으로 DB 클라이언트는 사람이 마우스로 테이블을 클릭하는 뷰어를 넘어, <strong>AI 에이전트가 프로덕션 데이터를 망가뜨리지 못하게 막는 정책 방화벽(MCP Policy Plane)</strong>이 된다. 데스크톱과 Docker 웹 백엔드 모두를 단일 Rust MCP 서버로 통제하는 DBX의 구조는 차세대 데이터 도구 경쟁의 핵심 해자를 정확히 선점하고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 도구가 25MB로 가벼워지자, 그 자리에 백 개의 엔진과 에이전트가 들어왔다
            </h3>
            <p>
              수백 메가바이트짜리 런타임을 얹고도 쿼리 창 하나 띄우는 데 버벅이던 시절을 돌아보면, Rust 네이티브 코어와 DuckDB, 샌드박스 사이드카의 조합이 만들어낸 25MB라는 숫자는 단순한 다이어트가 아니라 설계 철학의 승리다.
            </p>
            <p>
              사람에게는 빠른 SQL 격자와 ER 다이어그램을, AI 에이전트에게는 <code>read_only</code> 방패를 씌운 MCP 통로를 건네는 DBX는 이제 개발자 노트북에서 가장 먼저 켜지고 가장 늦게 닫히는 경량 데이터 허브로 자리 잡고 있다.
            </p>

            <div class="project-links">
              <a href="https://dbxio.com" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> DBX 공식 사이트
              </a>
              <a href="https://www.youtube.com/results?search_query=t8y2+dbx+rust+database+client+mcp" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/t8y2/dbx" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
