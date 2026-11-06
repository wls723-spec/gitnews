# -*- coding: utf-8 -*-
# Story 3: longbridge/gpui-kit (HERO 3)

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 3] longbridge/gpui-kit -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_gpui_kit.png" alt="longbridge gpui-kit" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="layout" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #3</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 디스코드도 일렉트론을 버리는 시대의 명답</span>
              <span class="platform-tag">GitHub Trending #3</span>
              <span class="platform-tag">longbridge / gpui-kit</span>
            </div>
            
            <h2 class="article-headline">
              "일렉트론 탈출 러시, Zed의 GPU 엔진을 품다" — 러스트 데스크톱 프레임워크 GPUI Kit
            </h2>

            <div class="article-subheadline">
              Metal과 Vulkan 직결 GPU 가속으로 120FPS 네이티브 데스크톱 앱 구축… 75개 이상의 엔터프라이즈 컴포넌트, WebAssembly, AccessKit 접근성 지원으로 무장한 차세대 UI 표준
            </div>
            <p class="article-snippet">
              오늘 해커뉴스 1위를 달군 'Discord의 Electron 폐기' 선언과 맞물려 전 세계 시스템 개발자들의 시선을 강탈한 longbridge/gpui-kit. Zed 에디터를 구동하던 극강의 GPUI 엔진을 상용 애플리케이션 프레임워크로 승화시킨 아키텍처를 해부합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 디스코드마저 일렉트론을 버렸다
            </h3>
            <p>
              오늘 테크 생태계의 가장 뜨거운 화두 중 하나는 단연 <strong>"디스코드(Discord)가 공식적으로 일렉트론을 버리고 자체 네이티브 앱으로 전환하여 RAM 사용량을 대폭 절감했다"</strong>는 더 버지(The Verge)의 특종 보도였다. 
              수백 메가바이트의 메모리를 집어삼키고 배터리를 갉아먹는 크로미움 기반 데스크톱 앱의 시대가 마침내 종언을 고하고 있음을 상징하는 사건이었다.
            </p>
            <p>
              그렇다면 개발자들은 무엇으로 차세대 데스크톱 앱을 만들어야 할까? 
              이 질문에 가장 완벽한 기술적 해답을 제시한 프로젝트가 오늘 깃허브 트렌딩 3위에 오른 <strong>longbridge/gpui-kit</strong>이다. 
              세상에서 가장 빠른 코드 에디터로 꼽히는 <strong>Zed를 지탱하는 순수 GPU 가속 렌더링 엔진인 GPUI</strong> 위에, 누구나 즉시 상용 앱을 조립할 수 있는 75개 이상의 풍성한 컴포넌트 생태계를 얹어 오픈소스로 내놓은 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 웹 기술의 타협 없는 순수 60~120FPS GPU 직결
            </h3>
            <p>
              기존의 크로스 플랫폼 GUI 프레임워크(Electron, Tauri, Flutter)는 결국 웹뷰를 띄우거나 별도의 가상 머신 계층을 거쳐야 했다. 
              하지만 GPUI Kit의 철학은 근본부터 다르다.
            </p>

            <div class="editorial-quote">
              <p>
                "GPUI는 비디오 게임 엔진처럼 동작한다. 
                DOM 트리나 CSS 엔진을 흉내 내지 않고, 맥OS에서는 <strong>Metal</strong>, 윈도우와 리눅스에서는 <strong>Vulkan</strong> 그래픽스 파이프라인을 직접 제어하여 모니터 주사율의 한계까지 UI를 그려낸다."
              </p>
              <small>— longbridge/gpui-kit 공식 설계 철학</small>
            </div>

            <p>
              메모리 점유율은 30MB 미만, 앱 기동 시간은 0.05초. 
              수만 줄의 텍스트가 담긴 테이블을 마우스 휠로 아무리 빠르게 튕겨도 단 한 프레임의 드롭(Frame Drop)조차 발생하지 않는다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 엔지니어링: 75개 컴포넌트와 풀스택 인프라
            </h3>
            <p>
              GPUI Kit가 단순한 장난감 렌더러를 넘어 상용 소프트웨어 프레임워크로 인정받는 이유는 엔터프라이즈급 완성도에 있다:
            </p>
            <ul>
              <li><strong>75개 이상의 검증된 컴포넌트:</strong> 버튼, 모달, 탭 같은 기본 위젯은 물론, 수백만 행을 가상화 처리하는 고성능 데이터 그리드, 복합 텍스트 에디터, 트리 뷰, 드롭다운을 기본 탑재.</li>
              <li><strong>AccessKit 기반 완전한 접근성:</strong> 스크린 리더와 운영체제 접근성 트리(Accessibility Tree)를 완벽 지원하여 글로벌 엔터프라이즈 표준 준수.</li>
              <li><strong>WebAssembly(Wasm) 크로스 타깃:</strong> 데스크톱뿐만 아니라 웹 브라우저에서도 Wasm으로 컴파일되어 동일한 120FPS 성능으로 동작.</li>
              <li><strong>선택적 자바스크립트 확장 런타임:</strong> 플러그인 생태계를 위해 V8/QuickJS 런타임을 임베드하여 샌드박스 확장 기능을 손쉽게 추가 가능.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="git-branch" style="color:#0ea5e9;"></i> GPUI Kit 네이티브 GPU 가속 렌더링 파이프라인
                </span>
                <span class="schematic-badge">METAL & VULKAN GPU ACCELERATION</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">Rust State & Data Model</div>
                  <div class="step-tech">Zero-Cost Memory Borrowing</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">GPUI GPU 셰이더 직접 투하</div>
                  <div class="step-tech">Direct Metal / Vulkan Pipeline (No DOM)</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">120FPS 버터 네이티브 앱</div>
                  <div class="step-tech">&lt;30MB RAM / 0.05s Instant Startup</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 비교:</strong> 웹 브라우저 엔진 전체를 띄워야 했던 과거의 일렉트론 방식과 달리, 단일 러스트 바이너리가 GPU 셰이더 코어를 직접 제어하여 극단적인 반응성과 자원 절약을 동시에 달성합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="layers"></i> 4. 소프트웨어 엔지니어링 생태계에 미치는 파장
            </h3>
            <p>
              슬랙, 노션, 스포티파이 등 수많은 빅테크 데스크톱 앱들이 일렉트론의 무거움으로 사용자들의 불만을 사온 상황에서, 
              디스코드의 네이티브 전환 소식과 GPUI Kit의 성숙은 "이제 러스트로 데스크톱 앱을 만드는 것이 실현 가능한 표준"이라는 확신을 심어주었다. 
              금융 트레이딩 터미널, 실시간 오디오/비디오 에디터, AI 에이전트 관제 콘솔 등 극한의 성능을 요구하는 분야에서 주류로 부상하고 있다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="monitor" style="color:#10b981;"></i> GPUI Kit 공식 웹사이트 & 컴포넌트 쇼케이스
                </span>
                <span class="media-showcase-badge demo">LIVE DEMO CAPTURE</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_gpui_kit.png" alt="GPUI Kit Live Website & Components" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 75종 컴포넌트 갤러리:</strong> gpui-kit.com 공식 포털에서 제공하는 고성능 GPU 가속 데스크톱 UI 위젯과 엔터프라이즈 컴포넌트 명세.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="check-circle"></i> 5. 결론: 네이티브 앱의 위대한 귀환
            </h3>
            <p>
              하드웨어 성능이 좋아졌다고 해서 소프트웨어가 게을러져도 된다는 변명은 끝났다. 
              GPUI Kit는 컴퓨터 본연의 속도를 되찾아주며, 진정한 장인정신을 갖춘 소프트웨어 엔지니어들에게 가장 강력하고 매력적인 무기를 선물했다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://gpui-kit.com" target="_blank" class="project-link demo">
                  <i data-lucide="sparkles" style="width:16px;height:16px;"></i> 공식 웹사이트 & 문서
                </a>
                <a href="https://github.com/longbridge/gpui-kit" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
