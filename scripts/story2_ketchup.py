# -*- coding: utf-8 -*-
# Story 2: BenchUp3D/editor (KetchUp) - Rust + WebGPU 3D CAD Revolution

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 2] BenchUp3D/editor (KetchUp) : Hacker News 1위 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_ketchup.jpg" alt="KetchUp Open-source 3D CAD Editor" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="box" style="width:12px;height:12px;fill:#fff;"></i> HN 726 PTS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag highlight-badge">⚡ 해커뉴스 726점 폭발적 화제작</span>
              <span class="aggro-tag">🔥 트림블 스케치업 구독 독점을 허문 Rust 3D</span>
              <span class="platform-tag">Hacker News & GitHub</span>
              <span class="platform-tag">BenchUp3D / KetchUp (editor)</span>
            </div>
            
            <h2 class="article-headline">
              트림블 스케치업(SketchUp)의 구독 독점에 마침표를 찍다 — 브라우저에서 60FPS로 폭주하는 Rust + WebGPU 3D CAD 'KetchUp'
            </h2>

            <div class="article-subheadline">
              설치 없는 순수 웹 Wasm/WebGPU 런타임, 실시간 불리언(Boolean) 메시 연산, 스마트 목재 재단표(Cut List) 자동 생성까지 품은 100% 무료 3D 가구·목공 스튜디오
            </div>
            <p class="article-snippet">
              연간 수십만 원의 구독료와 클라우드 강제로 메이커와 목공 장인들의 원성을 사온 트림블(Trimble) 스케치업의 아성에 도전하는 파괴적 오픈소스 3D 모델러 'KetchUp(BenchUp)'이 해커뉴스 726포인트를 기록하며 화제의 중심에 섰습니다. Rust와 WebGPU로 빚어낸 무결점 60FPS 렌더링 파이프라인과 브라우저 네이티브 CAD의 진면목을 조명합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 전 세계 메이커들이 스케치업을 버리고 환호한 이유
            </h3>
            <p>
              건축가, 인테리어 디자이너, 그리고 공방의 목공 장인들에게 스케치업(SketchUp)은 수십 년간 대체 불가능한 공기와 같았다. 
              그러나 2012년 트림블이 구글로부터 스케치업을 인수한 이후, 영구 라이선스는 폐지되었고 웹 버전은 기능이 강제 거세되었으며, 
              연간 수백 달러에 달하는 악명 높은 구독 모델이 사용자들의 목을 조여왔다. 
              간단한 의자 하나를 모델링하고 목재 재단 치수를 뽑기 위해 매달 구독료를 상납해야 하는 현실에 창작자들의 피로감은 극에 달해 있었다.
            </p>
            <p>
              오늘 해커뉴스를 발칵 뒤집어놓은 <strong>BenchUp3D/editor (프로젝트명: KetchUp)</strong>은 
              이 답답한 상업 CAD 시장에 던져진 통쾌한 한 방이다. 
              회원가입도, 프로그램 설치도 없이 웹 브라우저 주소창에 URL 하나만 치면 
              <strong>0.5초 만에 풀 3D CAD 작업 공간이 열리고, 수만 개의 폴리곤을 지닌 복잡한 가구 모델이 60FPS로 부드럽게 회전</strong>한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 브라우저가 전문가용 CAD 워크스테이션이 되다
            </h3>
            <p>
              웹 브라우저 기반 CAD는 항상 "느리고, 불안정하며, 장난감 수준"이라는 편견이 지배적이었다. 
              자바스크립트 가비지 컬렉션(GC)으로 인한 프레임 드롭과 구형 WebGL의 셰이더 한계 때문이었다. 
              하지만 KetchUp은 <strong>Rust 코어 엔진을 WebAssembly로 컴파일하고 차세대 그래픽 표준인 WebGPU로 직접 파이프라인을 뚫어냄</strong>으로써 
              네이티브 데스크톱 앱을 능가하는 서브밀리초 반응 속도를 달성했다.
            </p>

            <div class="editorial-quote">
              <p>
                "수십 년간 스케치업의 무료 영구 라이선스를 그리워하던 커뮤니티의 오랜 갈증이 마침내 해소되었다. 
                <strong>WebGPU와 Rust의 조합은 무거운 상용 독점 CAD 소프트웨어가 구축해 둔 '데스크톱 설치 해자'를 한순간에 날려버렸다.</strong> 
                브라우저 탭 하나가 가장 강력한 가구 설계 및 재단 최적화 워크스테이션이 되었다."
              </p>
              <small>— Hacker News 726 Pts 최상위 추천 리뷰어 발췌</small>
            </div>

            <p>
              단순한 3D 도형 뷰어에 그치지 않는다. 
              부재(Member)의 치수를 입력하면 원자재 합판에서 가장 손실을 적게 내는 재단 배치도(Cut-List Optimization)를 실시간으로 연산해내며, 
              볼트와 장부맞춤(Mortise and Tenon) 결합부를 자동으로 파내는 전문 목공 CAD 연산 기능을 완벽히 탑재했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Rust WebAssembly와 WebGPU 컴퓨트 셰이더의 만남
            </h3>
            <p>
              KetchUp이 상용 CAD 못지않은 반응성과 정확도를 브라우저 내에서 구현해낸 3대 핵심 엔지니어링 메커니즘은 다음과 같다:
            </p>
            <ul>
              <li><strong>WebGPU 다이렉트 렌더 파이프라인:</strong> WebGL의 단일 스레드 병목을 벗어나, 브라우저가 GPU 하드웨어 큐에 직접 커맨드 버퍼를 제출. 복잡한 3D 가구 모델의 그림자(Shadow Mapping), 엠비언트 오클루전(SSAO), 실시간 와이어프레임 앤티에일리어싱을 60FPS 무지연 렌더링.</li>
              <li><strong>Rust bvh & CSG(Constructive Solid Geometry) 엔진:</strong> 목재에 홈을 파거나 구멍을 뚫는 3D 불리언 불 연산을 Wasm 고속 메모리 상에서 실행. 경계 볼륨 계층 구조(BVH) 트리를 통해 메시 충돌 감지를 나노초 단위로 완료.</li>
              <li><strong>로컬 퍼스트(Local-First) 프라이버시 아키텍처:</strong> 설계 도면 파일은 클라우드 서버로 단 1바이트도 전송되지 않으며, 브라우저의 OPFS(Origin Private File System)와 로컬 디스크에 안전하게 저장·익스포트(OBJ, STL, DXF 지원).</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">KetchUp WebAssembly/WebGPU 제로 레이턴시 CAD 파이프라인</span>
                <span class="schematic-badge">Hardware Direct Bridge</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">User Input / Canvas</div>
                  <div class="schematic-desc">
                    포인터 락 & 6자유도 카메라 제어<br>
                    스마트 스냅(Endpoint, Midpoint)<br>
                    0-latency UI 레이어 (Slint/Wasm)
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Rust Wasm Core</div>
                  <div class="schematic-desc">
                    BVH 가속 공간 분할 & CSG 연산<br>
                    실시간 목재 재단(Cut-list) 솔버<br>
                    GC 없는 결정론적 메모리 관리
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">WebGPU Backend</div>
                  <div class="schematic-desc">
                    컴퓨트 셰이더 기반 버텍스 변환<br>
                    하드웨어 다이렉트 60FPS 렌더링<br>
                    DXF / STL / GLTF 원스톱 익스포트
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">KetchUp (BenchUp) 실제 브라우저 WebGPU 3D 모델링 런타임</span>
              </div>
              <img src="../assets/images/demo_ketchup.png" alt="KetchUp 3D CAD Live Demo" class="showcase-img">
              <p class="showcase-caption">
                ▲ benchup3d.github.io/editor 실구동 화면: 설치 없이 브라우저에서 즉시 실행되는 3D 뷰포트, 정밀 그리드 스냅 시스템, 부재별 치수 패널 및 실시간 3D 가구 모델링 인터페이스.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 독점 상용 CAD 생태계에 던지는 법적·상업적 경고
            </h3>
            <p>
              오토데스크(Autodesk)와 트림블(Trimble) 같은 레거시 CAD 제국들은 그동안 포맷 호환성과 무거운 바이너리 기술을 방패 삼아 
              폐쇄적인 라이선스 카르텔을 유지해왔다. 
              그러나 웹 브라우저가 WebGPU라는 네이티브급 그래픽 API를 정식 표준화하고 Rust 생태계가 성숙하면서, 
              수십 년간 축적된 상용 CAD의 기술적 해자는 순식간에 평탄화되고 있다.
            </p>
            <p>
              KetchUp은 오픈소스(GPL/MIT)로 배포되어 누구나 자사 공방에 맞춤형으로 수정하거나 
              CNC 머신 및 3D 프린터 파이프라인에 직결할 수 있다. 
              상업용 라이선스 단속 공문과 무리한 구독료 인상에 시달리던 전 세계 중소 제작소와 팹랩(FabLab)들에게 
              이 프로젝트는 대체재가 아닌 완전한 '기술적 독립 선언'이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 창작의 도구는 소유되어야 한다
            </h3>
            <p>
              "우리가 만드는 물건의 설계도를 왜 매달 남의 서버에 월세를 내며 그려야 하는가?" 
              KetchUp의 개발진이 던진 이 소박하고 근본적인 질문은 수많은 엔지니어들의 심장을 때렸다. 
              고성능 그래픽과 강력한 언어가 브라우저라는 가장 자유로운 플랫폼을 만났을 때 독점의 벽은 허물어진다. 
              KetchUp은 오픈소스가 어떻게 거대 소프트웨어 공룡의 족쇄를 풀어내는지를 가장 우아하게 증명해냈다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=BenchUp3D+KetchUp+Rust+WebGPU+CAD" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://benchup3d.github.io/editor/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> WebGPU 웹 CAD 즉시 체험하기
              </a>
              <a href="https://github.com/BenchUp3D/editor" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
