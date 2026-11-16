# -*- coding: utf-8 -*-
# Story 5: ModernRelay/omnigraph

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] ModernRelay/omnigraph                            -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_omnigraph.jpg" alt="Omnigraph Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="git-branch" style="width:12px;height:12px;fill:#fff;"></i> RUST GRAPH DB</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#fef3c7; border-color:#d97706; color:#92400e;">🌿 에이전트 브랜치 그래프 DB</span>
              <span class="platform-tag">GitHub Trending (Rust) &amp; omnigraph.dev</span>
              <span class="platform-tag">ModernRelay / omnigraph</span>
            </div>

            <h2 class="article-headline">
              "에이전트가 DB에 직접 덮어쓰지 않고 Git처럼 브랜치를 딴다" — Rust 기반 오브젝트 스토리지 네이티브 그래프 DB 'Omnigraph'
            </h2>

            <div class="article-subheadline">
              S3·R2 위 Lance 오픈 포맷, .pg 타입 온톨로지, Graph+Vector+BM25 하이브리드 RRF 검색, 3-Way 머지 브랜칭 및 Cedar 보안 정책까지 단일 Rust 런타임에 통합 (2,835스타)
            </div>
            <p class="article-snippet">
              여러 AI 에이전트가 수주일에 걸쳐 회사의 지식 그래프를 동시에 읽고 고치는 '장기(Long-Horizon) 에이전트' 환경에서는, 누군가 잘못된 노드를 덮어쓰는 순간 전체 기억이 오염됩니다. Rust 트렌딩 228스타(누적 2,835스타)를 기록한 <strong>ModernRelay/omnigraph</strong>는 S3 오브젝트 스토리지 위의 버전 관리형 <strong>Lance</strong> 포맷에 그래프·벡터 ANN·전문 검색을 결합하고, 에이전트마다 Git 스타일 브랜치를 열어 검토 후 3-Way 병합하게 만든 차세대 에이전트 메모리 인프라입니다.
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
              <i data-lucide="flame"></i> 1. 리드: 무상태 에이전트가 공유하는 '상태 저장소'의 비명
            </h3>
            <p>
              오늘날 대부분의 에이전트 메모리 솔루션은 단일 챗봇의 대화 로그를 벡터 DB에 욱여넣는 수준에 머물러 있다. 하지만 실제 기업 현장에서 코딩 에이전트, 리서치 에이전트, 운영 에이전트 수십 개가 하나의 회사 지식 베이스(Company Brain)나 이슈 의존성 그래프를 동시에 다루기 시작하면 곧바로 재앙이 터진다.
            </p>
            <p>
              스키마 없는 JSON 문서는 필드가 제각각 오염되고, 한 에이전트가 진행하던 미완성 추론 결과가 메인 데이터베이스에 그대로 노출되며, 권한 통제 없이 잘못된 쓰기가 발생해도 되돌릴 방법이 없다. Rust 생태계에서 급부상하며 누적 <strong>2,835스타</strong>를 돌파한 <strong>ModernRelay/omnigraph</strong>는 바로 이 '멀티 에이전트 공유 월드 모델' 문제를 데이터베이스 엔진의 뿌리부터 다시 설계했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 스토리지-연산 분리 × Git 브랜칭 × 통합 하이브리드 검색
            </h3>
            <p>
              <code>Omnigraph</code>가 기존 그래프 DB(Neo4j 등)나 단순 벡터 스토어와 결정적으로 다른 점은 <strong>코드 저장소(Git), 인프라 선언형 배포(Terraform), 그리고 멀티모달 검색 엔진</strong>의 핵심 철학을 하나의 Rust 바이너리에 녹여냈다는 것이다.
            </p>

            <div class="editorial-quote">
              <p>
                "에이전트와 UI는 영속 상태의 얇은 무상태(Stateless) 소비자가 된다. 에이전트는 <code>main</code>에 직접 쓰는 대신 <strong>작업별 브랜치를 열어 변경을 제안하고 3-Way 병합으로 승인</strong>받으며, 모든 쓰기는 서버 측 Cedar 보안 정책과 <code>.pg</code> 타입 온톨로지의 검증을 통과한다."
              </p>
              <small>— ModernRelay Omnigraph 아키텍처 명세 (MIT 오픈소스 · Lance 오픈 포맷)</small>
            </div>

            <p>
              여기에 Zed 에디터를 만든 GPU 가속 Rust UI 프레임워크인 <strong>GPUI</strong>로 제작한 네이티브 데스크톱 앱 <code>Omnigraph Studio</code>까지 함께 제공되어, 개발자가 브랜치에 추가·변경·삭제된 그래프 노드를 테이블과 캔버스 위에서 즉각 시각적으로 리뷰한 뒤 병합할 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Lance 포맷, .pg 온톨로지, RRF 멀티모달 검색, Cedar 정책
            </h3>
            <p>
              <code>Omnigraph</code>가 S3나 Cloudflare R2 같은 값싼 오브젝트 스토리지 위에서도 고성능과 엄격한 정합성을 동시에 달성하는 네 가지 핵심 엔진 구조는 다음과 같다:
            </p>
            <ul>
              <li><strong>오브젝트 스토리지 네이티브 &amp; Lance 오픈 포맷:</strong> 컴퓨트 서버와 스토리지를 완전히 분리했다. 로컬 디스크부터 AWS S3, Cloudflare R2, MinIO/RustFS, Azure까지 그래프 데이터와 Blob 값을 버전 관리되는 오픈 <strong>Lance</strong> 포맷으로 저장한다.</li>
              <li><strong><code>.pg</code> 타입 온톨로지 &amp; Git 스타일 브랜치:</strong> <code>.pg</code> 스키마 파일이 노드/엣지 타입·키·제약조건을 정의하며 매 쓰기마다 강제 검증한다. 에이전트는 <code>omnigraph branch create --from main agent/ingest-42</code>로 격리 브랜치를 파고, 전체 그래프에 대해 3-Way 머지와 타임 트래블(Time Travel)을 수행한다.</li>
              <li><strong>단일 런타임 통합 검색 + Cedar 정책 + IaC 배포:</strong> 하나의 쿼리 런타임 안에서 <strong>그래프 탐색 + 벡터 ANN + BM25 전문 검색 + RRF(Reciprocal Rank Fusion)</strong>를 동시 실행한다. 모든 변경(Mutation)에는 서버 측 <strong>Cedar</strong> 정책과 베어러 인증이 강제되며, <code>cluster.yaml</code>과 <code>.gq</code> 저장 쿼리를 <code>cluster plan / apply</code>로 무중단 배포한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Omnigraph 오브젝트 스토리지 네이티브 &amp; 에이전트 브랜치 아키텍처</span>
                <span class="schematic-badge">Rust · Lance Format · MIT</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Governance &amp; Declarative IaC</div>
                  <div class="schematic-desc">
                    <code>.pg</code> 강타입 온톨로지 스키마 검증<br>
                    서버 측 <strong>Cedar</strong> 정책(매 Mutation 강제)<br>
                    <code>cluster.yaml</code> + <code>.gq</code> 저장 쿼리<br>
                    <code>cluster plan</code> / <code>apply</code> 무중단 반영
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Branching &amp; Hybrid Retrieval</div>
                  <div class="schematic-desc">
                    에이전트별 격리 브랜치 · 3-Way 머지<br>
                    그래프 탐색 + 벡터 ANN + BM25<br>
                    Reciprocal Rank Fusion(RRF) 단일 실행<br>
                    GPUI 네이티브 <strong>Omnigraph Studio</strong> 리뷰
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Open Object Storage Layer</div>
                  <div class="schematic-desc">
                    스토리지·컴퓨트 완전 분리(Stateless 노드)<br>
                    버전 관리형 <strong>Lance</strong> 오픈 포맷 &amp; Blob<br>
                    AWS S3 · Cloudflare R2 · MinIO · 로컬<br>
                    내장 <code>omnigraph skill export</code> 지원
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Omnigraph Studio 공식 데스크톱 앱 &amp; 브랜치 디프 뷰 (omnigraph.dev/studio)</span>
              </div>
              <img src="../assets/images/demo_omnigraph.png" alt="Omnigraph Studio GPUI Native Desktop App" class="showcase-img">
              <p class="showcase-caption">
                ▲ omnigraph.dev/studio 공식 포털 화면: Zed의 GPUI 프레임워크로 작성된 네이티브 Rust 앱에서 에이전트 브랜치가 추가·수정·삭제한 그래프 레코드를 테이블과 캔버스로 리뷰하고 병합한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 데이터 인프라 재편: RAG의 다음 단계는 '버전 관리되는 컨텍스트 그래프'
            </h3>
            <p>
              지난 2년간 기업 AI 인프라 시장은 비싼 상용 벡터 DB와 무거운 JVM 기반 레거시 그래프 DB 사이에서 양분되어 있었다. 하지만 에이전트가 단순 검색(Read-only RAG)을 넘어 스스로 기업 지식과 실험 로그를 기록(Write)하기 시작하자, 두 진영 모두 '버전 관리와 스키마 안전성'이라는 치명적 빈틈을 드러냈다.
            </p>
            <ul>
              <li><strong>오픈 포맷(Lance) 기반 데이터 주권:</strong> 벤더 종속적인 바이너리 DB 파일 대신 S3 위의 오픈 Lance 포맷을 채택해, 동일한 그래프 데이터를 ML 학습·평가 파이프라인과 공유할 수 있다.</li>
              <li><strong>네이티브 에이전트 온보딩:</strong> 바이너리 자체에 <code>omnigraph skill export</code>를 내장해, CLI 버전과 정확히 일치하는 운영 플레이북을 Claude Code나 Codex에 즉시 주입한다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 인간이 코드에 Git을 썼듯, 에이전트는 기억에 브랜치를 쓴다
            </h3>
            <p>
              수십 명의 개발자가 하나의 코드베이스에서 충돌 없이 일할 수 있었던 비밀은 천재적인 기억력이 아니라 Git 브랜치와 Pull Request라는 협업 프로토콜 덕분이었다.
            </p>
            <p>
              Omnigraph는 바로 그 검증된 소프트웨어 협업 모델을 AI 에이전트의 기억 장치로 옮겨놓았다. 에이전트들이 각자의 브랜치 위에서 자유롭게 가설을 세우고 지식을 엮은 뒤, 인간의 리뷰와 정책 게이트를 거쳐 <code>main</code>에 병합되는 세계—장기 자율 에이전트 시대의 진짜 데이터베이스는 바로 이런 모습일 것이다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=ModernRelay+omnigraph+graph+database" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://www.omnigraph.dev/studio" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> Omnigraph Studio 공식 사이트
              </a>
              <a href="https://github.com/ModernRelay/omnigraph" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
