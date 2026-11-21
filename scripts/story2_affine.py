# -*- coding: utf-8 -*-
# Story 2: toeverything/AFFiNE

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] toeverything/AFFiNE                              -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_affine.jpg" alt="AFFiNE Local-First Hyper-Fused Workspace Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="layers" style="width:12px;height:12px;fill:#fff;"></i> LOCAL-FIRST OS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#dbeafe; border-color:#2563eb; color:#1e40af;">✍️ Notion + Miro 구독을 하나로 지우는 로컬 퍼스트 캔버스</span>
              <span class="platform-tag">GitHub Trending #1 (Unseen) &amp; affine.pro</span>
              <span class="platform-tag">toeverything / AFFiNE</span>
            </div>

            <h2 class="article-headline">
              "문서와 화이트보드의 이분법을 끝내다" — 내 디스크에 데이터를 100% 소유하며 Notion·Miro를 단일 CRDT 엔진에 융합한 'AFFiNE'
            </h2>

            <div class="article-subheadline">
              BlockSuite 모듈형 블록·Edgeless 무한 캔버스·멀티뷰 데이터베이스·Canvas AI 마인드맵/프로토타이핑과 Rust 기반 로컬 퍼스트 CRDT 동기화(OctoBase) 및 셀프호스팅을 통합 (+577스타/일, 누적 76,248스타)
            </div>
            <p class="article-snippet">
              아이디어를 구상할 때는 Miro 화이트보드를, 문서를 정리할 때는 Notion을, 일정을 관리할 때는 Linear나 Airtable을 오가며 매달 팀원당 수십 달러의 클라우드 구독료를 내던 지식 노동자들의 피로가 임계점에 달했습니다. 오늘 하루에만 577개의 스타를 끌어모으며 GitHub 일간 트렌딩 최상단에 오른 <strong>toeverything/AFFiNE</strong>는 문서(Page)와 무한 화이트보드(Edgeless)를 동일한 블록 트리 위에서 버튼 하나로 넘나들고, 모든 데이터를 클라우드 인질이 아닌 내 로컬 디스크에 영구 저장하는 차세대 오픈소스 지식 운영체제입니다.
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
              <i data-lucide="flame"></i> 1. 리드: 탭 4개를 오가던 기획서와 클라우드 장애 앞의 무기력함
            </h3>
            <p>
              제품 스펙 하나를 쓰기 위해 개발자와 디자이너가 여는 브라우저 탭은 끝이 없다. 아키텍처 다이어그램을 그리려 Miro나 FigJam을 띄우고, 그 링크를 복사해 Notion 문서에 임베드한 뒤, 다시 데이터베이스 표에 일정을 옮겨 적는다. 만약 클라우드 서비스가 장애를 일으키거나 팀 요금제 정책을 바꾸는 순간, 수년간 쌓아온 팀의 두뇌는 내보내기(Export)조차 버거운 거대한 사일로에 갇힌다.
            </p>
            <p>
              오늘 하루 <strong>+577스타(누적 76,248스타)</strong>를 기록하며 글로벌 트렌딩의 중심에 다시 선 <strong>toeverything/AFFiNE</strong>는 바로 이 '도구의 파편화'와 '클라우드 데이터 소유권 상실'이라는 두 가지 족쇄를 정면으로 겨냥한다. Page 모드에서 작성하던 마크다운 텍스트와 칸반 데이터베이스가 클릭 한 번에 무한 화이트보드(Edgeless) 위의 살아있는 카드로 펼쳐지고, 반대로 캔버스 위의 스티커 노트와 다이어그램이 즉시 정돈된 문서로 합쳐지는 경험은 기존 SaaS들이 흉내 내지 못한 아키텍처적 돌파구다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "블록을 재발명하지 말고, 문서와 캔버스의 물리 법칙을 통합하라"
            </h3>
            <p>
              시중의 많은 생산성 앱들이 화이트보드 기능을 흉내 내기 위해 문서 안에 '캔버스 임베드 위젯'을 끼워 넣는 수준에 머물렀다면, AFFiNE는 밑바닥 데이터 모델부터 다르게 설계했다. 모든 텍스트, 표, 스티커 메모, 임베드 웹페이지, 프레젠테이션 슬라이드가 동일한 **BlockSuite** 원자 블록으로 정의된다.
            </p>

            <div class="editorial-quote">
              <p>
                "우리는 도구를 만들고, 그 다음엔 도구가 우리를 만든다. <strong>당신의 데이터는 클라우드가 아니라 언제나 당신의 디스크 위에 있어야 하며</strong>, 문서와 화이트보드와 표는 하나의 캔버스 안에서 자유롭게 변신해야 한다."
              </p>
              <small>— toeverything/AFFiNE 로컬-퍼스트 하이퍼퓨즈 워크스페이스 철학</small>
            </div>

            <p>
              여기에 멀티모달 <strong>Canvas AI</strong>가 결합되면서 작업 흐름은 한층 극적으로 변한다. 긴 보고서 초안을 한 번의 프롬프트로 구조화된 마인드맵이나 발표용 슬라이드 덱으로 변환하고, 캔버스 위에 스케치한 UI 아이디어를 곧바로 프로토타입 웹 코드로 생성하며, 이 모든 과정을 로컬 크로스플랫폼 앱(macOS·Windows·Linux·웹)에서 오프라인 상태로도 지연 없이 수행한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: BlockSuite 에디터 커널 &amp; OctoBase Rust CRDT 동기화 해부
            </h3>
            <p>
              AFFiNE이 오프라인 즉시 반응성과 다중 사용자 실시간 협업이라는 상반된 목표를 동시에 달성한 비결은 TypeScript 프론트엔드와 Rust 코어가 결합된 로컬-퍼스트 스택에 있다:
            </p>
            <ul>
              <li><strong>BlockSuite 하이퍼퓨즈 블록 엔진:</strong> Yjs 호환 CRDT 상태 모델 위에서 동작하는 개방형 에디터 프레임워크로, 동일한 문서 트리(Doc Tree)를 선형 스크롤 페이지 뷰(Page)와 2D 무한 좌표 평면(Edgeless) 두 가지 렌더러로 실시간 투영한다.</li>
              <li><strong>OctoBase 로컬 퍼스트 CRDT 스토리지(Rust):</strong> 모든 편집 연산이 먼저 로컬 SQLite/IndexedDB에 즉시 커밋되어 네트워크 지연 0ms를 보장하며, 인터넷이 연결되거나 팀원이 접속하면 Rust 기반 CRDT 병합 엔진(<code>OctoBase</code>)이 충돌 없이 델타만 동기화한다.</li>
              <li><strong>멀티모달 AI &amp; 원클릭 Docker 셀프호스팅:</strong> 공식 <code>docs.affine.pro/self-host-affine</code> 가이드를 통해 사내 서버나 개인 NAS에 완전 독립형 협업 인스턴스를 구축할 수 있어 민감한 R&amp;D 문서나 기업 전략 보드의 외부 유출을 원천 차단한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">AFFiNE 로컬-퍼스트 하이퍼퓨즈 문서·캔버스 CRDT 아키텍처</span>
                <span class="schematic-badge">TypeScript + Rust · BlockSuite + OctoBase CRDT · Self-Hostable</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Unified BlockSuite Kernel</div>
                  <div class="schematic-desc">
                    단일 블록 트리(텍스트·표·카드·슬라이드)<br>
                    Page(문서) ↔ Edgeless(무한 캔버스) 즉시 전환<br>
                    멀티뷰 DB(칸반·테이블) &amp; 링크드 페이지<br>
                    프레젠테이션 슬라이드 캔버스 내장
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Local-First CRDT Sync</div>
                  <div class="schematic-desc">
                    로컬 디스크 우선 저장 (오프라인 100% 동작)<br>
                    Rust 기반 <strong>OctoBase</strong> CRDT 무충돌 병합<br>
                    델타 동기화로 대역폭·지연시간 최소화<br>
                    실시간 멀티유저 커서·공동 편집 지원
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Canvas AI &amp; Self-Hosting</div>
                  <div class="schematic-desc">
                    아티클 → 마인드맵·슬라이드 자동 요약<br>
                    원프롬프트 UI 프로토타입 코드 생성<br>
                    데스크톱 네이티브 + Docker 사내 구축<br>
                    서드파티 블록·플러그인 확장 에코시스템
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">AFFiNE 공식 웹 플랫폼 실화면 — 문서·화이트보드·데이터베이스 통합 워크스페이스</span>
              </div>
              <img src="../assets/images/demo_affine.png" alt="AFFiNE Official Platform Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ affine.pro 공식 플랫폼 실화면: "Write, Draw, Plan, All at Once. With AI." — 문서 작성, 무한 화이트보드 드로잉, 데이터베이스 일정 관리를 단일 로컬-퍼스트 워크스페이스에서 즉시 실행하고 라이브 데모(app.affine.pro)로 체험할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: Notion·Miro·Airtable의 '복합 구독세'를 해체하다
            </h3>
            <p>
              엔터프라이즈 SaaS 시장에서 Notion, Miro, Airtable은 각자 강력한 네트워크 효과를 구축해 왔지만, 팀 규모가 커질수록 3개 도구를 동시에 구독하는 '워크스페이스 중복 과금'과 AI 기능 추가에 따른 시트당 요금 인상, 그리고 데이터 주권 규제(GDPR·금융·국방망 폐쇄환경)라는 구조적 약점을 안고 있다.
            </p>
            <ul>
              <li><strong>원자적 블록 통합의 경제학:</strong> 문서와 화이트보드, 데이터베이스가 분리되어 있을 때는 팀이 매번 두세 개의 유료 시트를 결제해야 했지만, AFFiNE은 이를 하나의 오픈소스 코어로 합치면서 중소규모 팀과 프라이버시 중심 기업들의 SaaS 이탈 수요를 정면으로 흡수하고 있다.</li>
              <li><strong>데이터베이스 없는 락인(Lock-in) 해방:</strong> 독점 클라우드 포맷 대신 로컬 파일과 셀프호스팅을 표준으로 삼음으로써, AI 에이전트 시대에도 기업 내부 지식 베이스가 특정 SaaS 벤더의 API 가격 정책에 종속되지 않도록 방어막을 제공한다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 도구가 흩어질수록 생각도 흩어진다 — 이제 내 디스크가 스튜디오다
            </h3>
            <p>
              생각의 흐름은 선형적인 텍스트 문서와 비선형적인 화이트보드 스케치를 끊임없이 오간다. 도구가 그 경계를 가로막고 구독료를 요구하던 시대는 서서히 저물고 있다.
            </p>
            <p>
              7만 6천여 명의 개발자와 크리에이터가 선택한 AFFiNE은 클라우드 시대의 당연했던 전제를 뒤집는다. 가장 강력한 협업 공간은 타인의 서버가 아니라, 내 컴퓨터 디스크 위에서 시작해 세상과 안전하게 동기화되는 로컬-퍼스트 캔버스다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=AFFiNE+open+source+Notion+Miro+alternative" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://app.affine.pro" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 라이브 웹 데모 체험
              </a>
              <a href="https://github.com/toeverything/AFFiNE" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
