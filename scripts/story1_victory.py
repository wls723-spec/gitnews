# -*- coding: utf-8 -*-
# Story 1: Marvisak/VIctory (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] Marvisak/VIctory : COVER STORY                    -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_victory.jpg" alt="VIctory Rust Xbox Series to Windows Compatibility Layer Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> COVER EXPLOSION #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🦀 25시간 만에 ★11,157 폭발 · GTA 6 Windows 직접 부팅 실증</span>
              <span class="platform-tag">GitHub Top Explosion &amp; HN Hot</span>
              <span class="platform-tag">Marvisak / VIctory</span>
            </div>

            <h2 class="main-lead-headline">
              <span id="hero-title">"GitHub 차단을 뚫고 부팅에 성공한 금단의 Rust 엔진" — Windows 위에서 GTA 6를 깨운 'VIctory'</span>
            </h2>

            <div class="article-subheadline">
              리드 개발자가 등교한 사이 전작 Leonida가 GitHub에서 차단된 직후, 게임 파일 0바이트·순수 Rust 12개 크레이트로 Xbox Series x86-64 실행 코드와 D3D12.X·셰이더 23,894개를 호스트 Direct3D 12·DXIL로 번역해 Windows 11에서 첫 미션 거리·차량·캐릭터까지 그려낸 호환 레이어 (★11,157 · GPL-3.0)
            </div>
            <p class="article-snippet">
              어제 한 고교생 리드 개발자가 학교에 간 사이 Python 기반 정적 리컴파일 프로젝트 <code>Leonida</code>가 GitHub에서 전면 차단(해커뉴스 <strong>324점·댓글 586개</strong>)되자, 오픈소스 호환 레이어 커뮤니티의 시선은 단숨에 <strong>Marvisak/VIctory</strong>로 쏠렸습니다. 순수 Rust(<code>GPL-3.0</code>)로 새로 설계된 이 프로젝트는 공개 <strong>25시간 만에 ★11,157(포크 1,628개)</strong>을 돌파했고, 파생 포크(<code>fxceless/victory-fork</code> ★1,474)에서는 NVIDIA RTX 4070 기준 프레임당 240~350ms(<strong>2.5~4fps</strong>)까지 끌어올리며 프롤로그 컷신과 세이브·로드, 패드 입력까지 실제로 구동해 내는 기염을 토했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 전작이 지워진 그날, PC 모니터 위에 뜬 바이스 시티의 거리
            </h3>
            <p>
              이번 주 오픈소스 씬에서 가장 극적인 장면은 24시간 간격으로 교차했다. 먼저 며칠 전까지 화제를 모았던 Xbox→PC 포팅 프로젝트 <code>ItsNotRexed/Leonida</code>가 리드 개발자의 등교 시간 도중 GitHub에서 갑자기 삭제되며 수많은 미병합 PR과 함께 증발했다. 그러나 차단 공지가 식기도 전인 오늘 새벽, 해커뉴스(<em>"GTA 6 Running on Windows"</em>, <strong>226점·댓글 252개</strong>)와 GitHub Search 1위를 동시에 집어삼킨 것은 완전히 다른 아키텍처로 무장한 Rust 프로젝트 <strong><code>Marvisak/VIctory</code></strong>였다.
            </p>
            <p>
              <code>VIctory</code>의 <code>README.md</code> 첫머리는 거창한 선전 문구 대신 냉정한 엔지니어링 로그로 채워져 있다. <em>"아직 플레이 가능한 수준은 아니다."</em> 그러나 바로 아래 표에는 충격적인 실증 기록이 나란히 적혀 있다. Windows 11(AMD RX 6700 XT) 환경에서 인트로 영상과 오디오가 재생되고, 시작 화면과 메뉴가 <strong>30fps</strong>로 돌아가며, 약 50초 로딩 끝에 첫 미션의 거리·빌딩·차량·캐릭터와 타이틀 카드까지 실제로 화면에 그려진 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 에뮬레이터가 아닌 '인프로세스 Rust 호환 레이어'가 바꾼 게임의 규칙
            </h3>
            <p>
              과거 콘솔 독점작을 PC로 가져오는 데는 수년의 CPU 명령어 에뮬레이션이 필요했다. 하지만 Xbox Series X|S는 본질적으로 PC와 동일한 <strong>x86-64 CPU 아키텍처</strong>와 Direct3D 12 파생 GPU API(<code>D3D12.X</code>) 위에서 움직인다. <code>VIctory</code>는 무거운 가상 머신이나 CPU 에뮬레이터를 끼우는 대신, 게임의 원본 x86-64 실행 바이너리를 Windows 프로세스 공간 안에 직접 매핑하고, 콘솔 전용 런타임과 GPU 명령어만 아래에서 통째로 바꿔치기하는 <strong>Wine식 네이티브 호환 레이어</strong>를 택했다.
            </p>

            <div class="editorial-quote">
              <p>
                "타이틀의 x86-64 코드는 우리 프로세스 안에서 수정 없이 그대로 실행된다. <strong>VIctory는 그 아래의 플랫폼 계층(xgameruntime, D3D12.X → host D3D12)을 공급하고, 셰이더 23,894개와 텍스처 타일링을 사전(translate --cache) 및 실행 시점에 DXIL로 번역할 뿐이다.</strong>"
              </p>
              <small>— Marvisak/VIctory 공식 아키텍처 문서(docs/architecture.md) 및 상태 보고서</small>
            </div>

            <p>
              이 구조가 가져온 파급력은 곧바로 생태계 폭증으로 이어졌다. 공개 하루 만에 포크 <strong>1,628개</strong>가 쏟아졌고, <code>fxceless/victory-fork</code>(★1,474)는 메시릿(Meshlet) 컬링 뷰 버그와 730개 컴퓨트 셰이더의 암묵적 밉레벨 DXIL 오류를 패치해 RTX 4070에서 프레임 시간을 3~6초에서 <strong>240~350ms(2.5~4fps)</strong>로 단축했다. <code>DesertGamer/VIctory-V2</code>, <code>ZigZagBoi1/ScarlettPort</code>, <code>boykopovar/AnyBox</code>, macOS용 <code>VIctory-macOS</code>까지 동시다발적으로 갈라지며 거대한 오픈소스 호환 레이어 군단을 형성하고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 12개 Rust 크레이트와 PE32+ 임포트 하이재킹·DXIL 셰이더 파이프라인
            </h3>
            <p>
              <code>VIctory</code>가 콘솔 실행 파일을 호스트 Windows 위에서 안전하게 속여 넘기는 방식은 치밀한 4단계 모듈 구조에 담겨 있다:
            </p>
            <ul>
              <li><strong>PE32+ 로더와 TLS 슬롯 리다이렉션 (<code>victory-pe</code> · <code>victory-loader</code>):</strong> 콘솔 실행 파일(`.exe`)은 정적 TLS(Thread Local Storage)를 슬롯 0으로 가정하지만, 호스트 프로세스 내부에 DLL처럼 매핑하면 다른 TLS 슬롯을 배정받는다. <code>victory-loader::tls</code>는 이 TLS 로드 명령을 동적으로 우회 재연결하고, <code>victory-loader::crash</code>는 예외 발생 시 <code>module+rva</code> 단위로 스택을 역추적해 <code>crashes.log</code>에 기록한다.</li>
              <li><strong>4단계 임포트 바인딩과 오프라인 HLE (<code>victory-hle</code>):</strong> 게임이 <code>dll!function</code>을 호출하면 ① <code>victory-hle::modules</code>의 콘솔 API 구현체가 최우선으로 가로채고, ② <code>HostPolicy</code>가 허용한 Windows DLL만 호스트로 통과시킨다. <code>xgameruntime.dll</code>에는 의사 핸들(Pseudo Handle)을 반환해 세이브 파일과 가상 드라이브를 <code>VICTORY_DATA_DIR</code>로 매핑하며, 네트워크 호출은 설계상 완전 차단(오프라인 콘솔 에뮬레이션)한다.</li>
              <li><strong>D3D12.X → 호스트 D3D12 및 DXIL 번역 (<code>victory-gpu</code> · <code>victory-shader</code>):</strong> <code>victory translate --cache --pipelines</code>로 콘솔 GPU 바이너리를 사전 번역하거나 첫 사용 시점에 캐싱한다. 이미 메시 셰이더 8,765/8,765개 전량, 버텍스/픽셀 12,550/12,592개, 컴퓨트 2,579/2,637개를 DXIL로 변환했으며, 콘솔 전용 타일링 텍스처 레이아웃을 호스트 GPU 포맷으로 디타일링한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">VIctory 인프로세스 Xbox Series → Windows 호환 파이프라인</span>
                <span class="schematic-badge">12 Rust Crates · Zero Game Assets · GPL-3.0</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. User Assets &amp; PE Loader</div>
                  <div class="schematic-desc">
                    사용자 보유 원본 Xbox Series 파일<br>
                    <code>victory-pe</code> · <code>victory-loader</code><br>
                    In-Process x86-64 직접 매핑<br>
                    정적 TLS 슬롯 리다이렉션 &amp; RVA 크래시 추적
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. HLE &amp; D3D12.X Shim</div>
                  <div class="schematic-desc">
                    <code>victory-hle</code>: <code>xgameruntime</code> 가상화<br>
                    <code>HostPolicy</code> 통과분만 Windows API 연결<br>
                    <code>victory-gpu</code>: D3D12.X → Host D3D12<br>
                    명령 리스트 · 가상 드라이브 <code>VICTORY_DATA_DIR</code>
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Shader &amp; Texture Cache</div>
                  <div class="schematic-desc">
                    <code>victory-shader</code>: 콘솔 GPU → DXIL<br>
                    Mesh 8,765 · VS/PS 12,550 · CS 2,579 번역<br>
                    <code>victory-formats</code>: 콘솔 타일링 디코딩<br>
                    <code>victory-pipeline</code> 콘텐츠 주소 캐시
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Marvisak/VIctory 저장소 실화면 — 셰이더·부팅 단계별 실증 매트릭스와 12개 Rust 크레이트 구조</span>
              </div>
              <img src="../assets/images/demo_victory.png" alt="Marvisak VIctory GitHub Repository Status and Architecture" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/Marvisak/VIctory 실화면: 인트로 영상·30fps 메뉴·50초 월드 로딩 및 23,894개 이상 셰이더 DXIL 번역 현황과 호환성 서브시스템 매트릭스.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 법적 분기점: DMCA 삭제로도 막지 못한 '클린룸 호환 레이어'와 콘솔 독점의 균열
            </h3>
            <p>
              해커뉴스 댓글 586개가 쏟아진 지점은 단순한 프레임 레이트가 아니라, 콘솔 산업과 저작권법의 정면 충돌이었다. 전작 <code>Leonida</code>가 DMCA/약관 이슈로 GitHub에서 내려가자마자, <code>VIctory</code>는 저장소 설계 단계부터 철저한 법적 방어선을 구축했다.
            </p>
            <ul>
              <li><strong><code>xtask</code> 에셋 가드와 Zero-Asset 원칙:</strong> 저장소 내 전용 크레이트인 <code>xtask</code>와 <code>victory-core</code>의 에셋 정책 가드는 게임 실행 파일, 텍스처, 셰이더 덤프 등 저작권이 걸린 데이터가 단 1바이트라도 커밋되지 않도록 git 훅 차원에서 감시한다. 사용자가 자신의 합법적 콘솔 백업본을 로컬에서 주입해야만 작동하는 순수 호환 계층이다.</li>
              <li><strong><em>Sony v. Connectix</em> 판례와 아키텍처의 역설:</strong> 2000년 미국 항소법원이 플레이스테이션 에뮬레이터(Virtual Game Station)에 대해 호환성 목적의 클린룸 재구현을 공정 이용(Fair Use)으로 인정한 이래, 하드웨어 호환 레이어 자체를 불법으로 규정하기는 어렵다. 더 근본적으로, 콘솔이 PC와 같은 x86-64·DirectX 변종 아키텍처를 채택한 이상 "PC 출시를 늦추는 기간제 독점"이라는 비즈니스 해자는 기술적으로 점점 더 얇아지고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 리포지토리를 하나 닫으면, 아키텍처가 열 개로 증식한다
            </h3>
            <p>
              아직 광선 추적(RT) 바운스 라이팅이 빠져 그림자 진 곳이 까맣게 나오고 초당 프레임도 한 자릿수에 머물러 있어, <code>VIctory</code>로 게임을 완주할 수는 없다. 그러나 불과 며칠 전까지만 해도 "콘솔 독점 기간 동안 PC에서는 불가능하다"고 여겨졌던 문턱은 이미 부서졌다.
            </p>
            <p>
              리포지토리 하나를 내릴 수는 있어도, 동일한 명령어셋 위에 세워진 오픈소스 호환 레이어의 집단 지능—오늘 하루에만 수천 개의 포크로 흩어져 각자의 GPU 위에서 셰이더 버그를 고쳐 올리는 개발자들의 행렬—을 멈출 방법은 없다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Marvisak+VIctory+GTA+6+Windows+Rust" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/Marvisak/VIctory" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
