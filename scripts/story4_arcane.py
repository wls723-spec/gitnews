# -*- coding: utf-8 -*-
# Story 4: getarcaneapp/arcane

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] getarcaneapp/arcane                              -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_arcane.jpg" alt="Arcane Modern Docker Management Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> GO + DOCKER</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#e0f2fe; border-color:#0284c7; color:#0c4a6e;">🐳 차세대 Go 도커 컨트롤 플레인</span>
              <span class="platform-tag">GitHub Trending &amp; getarcane.app</span>
              <span class="platform-tag">getarcaneapp / arcane</span>
            </div>

            <h2 class="article-headline">
              무겁고 유료화된 포트ainer 시대의 종말: Go 1.27·Docker Compose v5·GitOps를 품은 현대적 도커 관리기 'Arcane v3'
            </h2>

            <div class="article-subheadline">
              WebAuthn 패스키·OIDC 인증부터 Copacetic 취약점 패치·SBOM 투명성·S3/ECR 연동까지 BSD-3-Clause로 완전 개방한 풀스택 도커 대시보드 (9,294스타)
            </div>
            <p class="article-snippet">
              오랫동안 셀프호스팅과 홈랩, 중소 엔지니어링 팀의 도커 관리 웹 UI 시장은 낡은 UI와 상용 기능 잠금(Paywall) 사이에서 제자리걸음을 해왔습니다. 오늘 하루 654스타를 추가하며 9,294스타를 넘어선 <strong>getarcaneapp/arcane</strong>은 최신 Go 1.27 백엔드와 Docker Compose v5·Huma v2 OpenAPI 엔진 위에 WebAuthn 패스키, GitOps 자동 배포(<code>go-git</code>), 컨테이너 이미지 취약점 패치(Copacetic)까지 모두 BSD-3-Clause 오픈소스로 녹여냈습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 컨테이너는 2026년인데 관리 대시보드는 왜 2018년에 멈춰 있는가
            </h3>
            <p>
              쿠버네티스(Kubernetes)가 과도한 복잡성으로 중소규모 인프라 팀에게 피로감을 안기면서, 수많은 프로덕션 서비스와 사내 도구가 다시 '단일 노드 혹은 멀티 호스트 Docker Compose'로 회귀하고 있다. 하지만 막상 도커 환경을 웹으로 관리하려 들면 선택지는 낡고 둔중한 레거시 대시보드나 엔터프라이즈 라이선스 뒤에 핵심 보안·GitOps 기능을 숨긴 상용 툴뿐이었다.
            </p>
            <p>
              오늘 GitHub Go 및 전체 트렌딩에 동시 진입하며 하루 654스타(누적 9,294스타)를 쓸어 담은 <strong>getarcaneapp/arcane</strong> v3는 "누구나 쓰기 쉬우면서도 프로덕션 보안과 현대적 개발자 경험을 타협하지 않는 도커 관리기"라는 정면 승부수로 개발자 커뮤니티의 뜨거운 지지를 얻고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 단순 컨테이너 뷰어가 아닌 '엔터프라이즈급 셀프호스팅 플랫폼'
            </h3>
            <p>
              <code>Arcane v3</code>가 기존 경량 도커 UI들과 궤를 달리하는 지점은 아키텍처의 깊이에서 드러난다. <code>backend/go.mod</code>를 들여다보면 단순히 Docker 소켓에 REST 래퍼만 씌운 토이 프로젝트가 아니라, 클라우드 네이티브 보안과 인증 표준을 정공법으로 통합한 본격 인프라 제어 평면(Control Plane)임을 알 수 있다.
            </p>

            <div class="editorial-quote">
              <p>
                "모두를 위해 설계된 현대적 도커 관리. Arcane v3는 <strong>BSD-3-Clause 라이선스</strong> 아래 투명한 SBOM(소프트웨어 자재명세서) 공개와 Cosign 서명, 그리고 타협 없는 현대적 UI를 결합했다."
              </p>
              <small>— getarcaneapp/arcane v3 공식 저장소 &amp; 보안 투명성 명세 (getarcane.app)</small>
            </div>

            <p>
              특히 <code>getarcane.app/sbom</code>을 통해 릴리즈별 SBOM을 상시 공개하고 <code>cosign.pub</code> 기반 아티팩트 서명을 제공하는 행보는, 도커 소켓이라는 시스템 최고 권한을 다루는 관리 도구에서 공급망 신뢰성이 얼마나 치명적인지 정확히 꿰뚫은 설계다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Go 1.27 + Docker Compose v5 + GitOps·Copacetic 융합
            </h3>
            <p>
              <code>getarcane.dev/arcane/v3</code> 모노레포(Go 백엔드 + CLI + TypeScript/Vite 프론트엔드)를 지탱하는 핵심 기술 기둥은 세 가지다:
            </p>
            <ul>
              <li><strong>최신 Docker CLI v29 &amp; Compose v5 네이티브 엔진:</strong> <code>compose-go/v2</code>와 공식 <code>docker/compose/v5</code> 라이브러리를 백엔드에 직접 내장해, 외부 셸 스크립트 호출에 의존하던 기존 툴보다 스택 파싱·업데이트·WebSocket 실시간 로그 스트리밍(<code>coder/websocket</code>)이 훨씬 견고하다.</li>
              <li><strong>제로 트러스트 인증 &amp; 멀티 레지스트리(OIDC · WebAuthn · LDAP):</strong> <code>go-oidc/v3</code>, <code>go-webauthn</code> 패스키, 기업용 LDAP 인증을 기본 내장했으며, AWS ECR·S3 백업과 <code>google/go-containerregistry</code>를 직접 지원해 사내 레지스트리 인증 병목을 해소했다.</li>
              <li><strong>GitOps 동기화 &amp; Copacetic 자동 취약점 패치:</strong> <code>go-git/v5</code> 기반으로 Git 저장소의 Compose 선언과 실행 환경을 직접 동기화할 뿐 아니라, <code>getarcane.dev/copacetic</code> 통합으로 베이스 이미지 재빌드 대기 없이 컨테이너 OS 패키지 취약점을 신속히 패치할 수 있는 기반을 갖췄다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Arcane v3 풀스택 도커 컨트롤 플레인 아키텍처</span>
                <span class="schematic-badge">BSD-3-Clause · Go 1.27 + Vite</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Frontend &amp; Auth Layer</div>
                  <div class="schematic-desc">
                    Svelte/Vite 기반 다크·라이트 반응형 UI<br>
                    <code>Huma v2</code> 자동 생성 OpenAPI 스펙<br>
                    WebAuthn 패스키 · OIDC · LDAP 지원<br>
                    <code>coder/websocket</code> 실시간 콘솔·로그
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Go v3 Core &amp; GitOps</div>
                  <div class="schematic-desc">
                    <code>docker/cli v29</code> &amp; <code>compose/v5</code> 내장<br>
                    <code>go-git/v5</code> 선언형 스택 동기화<br>
                    <code>yamux</code> 멀티 호스트 에이전트 터널링<br>
                    <code>arcane</code> 전용 CLI 바이너리 연동
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Registry &amp; Supply Chain</div>
                  <div class="schematic-desc">
                    AWS ECR · S3 · <code>go-containerregistry</code><br>
                    <code>Copacetic</code> 컨테이너 취약점 패치 통합<br>
                    릴리즈 <code>SBOM</code> 공개 및 <code>Cosign</code> 검증<br>
                    Crowdin 다국어 커뮤니티 현지화
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">getarcaneapp/arcane v3 대시보드 및 공식 저장소 화면</span>
              </div>
              <img src="../assets/images/demo_arcane.png" alt="Arcane v3 Docker Management Dashboard and Repository" class="showcase-img">
              <p class="showcase-caption">
                ▲ getarcaneapp/arcane 공식 저장소 및 v3 대시보드 프리뷰: Go v3 백엔드와 Svelte/Vite UI, SBOM 투명성 링크 및 멀티 호스트 도커 관리 아키텍처를 확인할 수 있다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 라이선스 전략: BSD-3-Clause가 주는 안도감
            </h3>
            <p>
              인프라 관리 도구 시장에서 최근 가장 민감한 화두는 '라이선스 배신(Rug-pull)'이다. 핵심 관리 도구가 갑자기 BSL이나 AGPL, 혹은 유료 엔터프라이즈 전용 기능 분할로 돌아서면서 셀프호스터와 스타트업들이 대체재를 찾아 대이동하고 있다.
            </p>
            <ul>
              <li><strong>기업 도입 장벽이 없는 BSD-3-Clause:</strong> Arcane은 웹 대시보드, OIDC/패스키 인증, GitOps, CLI까지 모두 관대한 BSD-3-Clause로 개방해, 사내 플랫폼에 통합하거나 재배포하려는 기업 엔지니어링 팀에게 완벽한 법적 안전망을 제공한다.</li>
              <li><strong>'포스트 쿠버네티스' 단순화 물결의 수혜:</strong> 복잡한 K8s 클러스터 대신 소수의 고성능 베어메탈·VPS에서 Docker Compose로 서비스를 운영하는 팀이 늘수록, Arcane 같은 현대적 단일 컨트롤 플레인의 가치는 더욱 커진다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 인프라는 지루할수록, 도구는 투명할수록 좋다
            </h3>
            <p>
              도커는 이미 십여 년 된 기술이지만, 컨테이너를 다루는 사람의 경험과 보안 요구사항은 2026년 기준으로 완전히 달라졌다.
            </p>
            <p>
              패스키로 로그인하고, SBOM과 Cosign 서명을 확인한 뒤, Git 저장소에서 바로 Docker Compose v5 스택을 굴리는 경험—Arcane v3는 '보통의 개발자가 정말 원했던 현대적 도커 대시보드'가 어떤 모습이어야 하는지 깔끔한 Go 코드로 증명해 보이고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Arcane+Docker+Management+getarcane" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://getarcane.app" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 문서 포털
              </a>
              <a href="https://github.com/getarcaneapp/arcane" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
