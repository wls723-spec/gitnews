# -*- coding: utf-8 -*-
# Story 5: crmne/zapfast (HERO 5)

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 5] crmne/zapfast -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_zapfast.jpg" alt="crmne zapfast" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #5</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 500MB 일렉트론을 25MB로 끝장낸 Rust 메신저</span>
              <span class="platform-tag">GitHub Trending #5</span>
              <span class="platform-tag">crmne / zapfast</span>
            </div>
            
            <h2 class="article-headline">
              "채팅창 하나에 RAM 500MB는 죄악이다" — Rust와 egui로 빚어낸 초경량 메신저 ZapFast
            </h2>

            <div class="article-subheadline">
              무거운 크로미움 웹뷰를 완전히 걷어내고 순수 러스트 즉시 모드 GUI로 재구축… 메모리 점유율 95% 절감, 즉각적인 키 입력 반응성, libsignal 종단간 암호화 직접 통신 구현
            </div>
            <p class="article-snippet">
              일렉트론(Electron) 기반 데스크톱 메신저들의 만성적인 메모리 폭식과 버벅임에 반기를 든 오픈소스 'ZapFast'. 순수 Rust와 egui 즉시 모드 그래픽스 엔진으로 25MB RAM만으로 쾌적하게 구동되는 네이티브 앱의 설계 비밀을 파헤칩니다.
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
              <i data-lucide="flame"></i> 1. 리드: 만연한 '일렉트론 슬롭(Slop)'에 던진 반기
            </h3>
            <p>
              슬랙, 디스코드, 왓츠앱, 노션… 오늘날 현대인의 컴퓨터에서 실행되는 대부분의 데스크톱 앱은 겉만 앱일 뿐, 실상은 거대한 크로미움(Chromium) 브라우저 엔진과 노드(Node.js) 런타임을 통째로 감싼 일렉트론 래퍼다. 
              단순한 텍스트 메시지를 주고받는 메신저 하나가 500MB에서 심하면 1GB 이상의 메모리를 집어삼키고, 노트북 배터리를 빠르게 갉아먹는다.
            </p>
            <p>
              이에 지친 시스템 엔지니어들이 오늘 깃허브 트렌딩 5위로 끌어올린 프로젝트가 바로 <strong>crmne/zapfast</strong>다. 
              ZapFast는 왓츠앱(WhatsApp)의 모든 기능을 지원하면서도 웹뷰를 단 한 줄도 쓰지 않고, <strong>순수 러스트(Rust)와 즉시 모드 GUI 라이브러리인 egui</strong>로 바닥부터 다시 작성된 네이티브 클라이언트다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 500MB에서 25MB로, 95% 메모리 다이어트
            </h3>
            <p>
              ZapFast를 실행했을 때 작업 관리자(Task Manager)에 찍히는 수치는 충격적이다.
            </p>

            <div class="editorial-quote">
              <p>
                "공식 일렉트론 왓츠앱 클라이언트가 600MB의 RAM을 차지할 때, ZapFast는 <strong>단 20~25MB의 메모리</strong>만으로 완벽하게 동작한다. 
                시작 속도는 0.1초 미만이며, 키보드를 누르는 순간 글자가 화면에 찍히는 레이턴시는 0에 수렴한다."
              </p>
              <small>— crmne/zapfast 프로젝트 릴리즈 노트</small>
            </div>

            <p>
              이것은 수치상의 차이만이 아니다. 수천 개의 메시지가 오가는 대화방을 스크롤할 때 느껴지는 버벅임(Jank)이 완전히 사라지고, 고주사율 모니터에서도 버터처럼 매끄러운 120FPS 프레임레이트를 유지한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: egui 즉시 모드 렌더링과 libsignal 직결
            </h3>
            <p>
              ZapFast의 극단적인 효율성은 두 가지 핵심 기술적 선택에서 나온다:
            </p>
            <ul>
              <li><strong>egui (Immediate-mode GUI):</strong> 무거운 웹 DOM 트리나 가상 DOM 디핑(Diffing) 대신, 비디오 게임 엔진처럼 매 프레임 UI를 화면 버퍼에 직접 그리는 즉시 모드 렌더링 방식 채택. 메모리 오버헤드가 거의 없고 복잡한 상태 관리가 사라짐.</li>
              <li><strong>러스트 네이티브 네트워크 & Signal 프로토콜:</strong> 웹소켓을 통한 왓츠앱 다중 기기 프로토콜과 종단간 암호화(libsignal E2EE)를 러스트로 직접 파싱하여 C 바인딩 수준의 극상 성능 구현.</li>
              <li><strong>경량 로컬 SQLite 캐시:</strong> 메시지 히스토리와 미디어 인덱스를 경량 SQLite로 관리하여 디스크 I/O 병목을 제거.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="git-branch" style="color:#0ea5e9;"></i> ZapFast 네이티브 러스트 렌더링 파이프라인
                </span>
                <span class="schematic-badge">NATIVE RUST VS ELECTRON ARCHITECTURE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">러스트 네이티브 소켓 & E2EE</div>
                  <div class="step-tech">libsignal E2EE Protocol Parser</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">egui 즉시 모드 GPU 렌더링</div>
                  <div class="step-tech">Zero DOM / 60~120FPS Direct Frame</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">메모리 25MB 극저지연 UX</div>
                  <div class="step-tech">Pure Rust Binary (No Chromium/V8)</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 비교:</strong> 무거운 V8 자바스크립트 엔진과 크로미움 렌더러를 완전히 도려내고, 단일 정적 컴파일된 러스트 바이너리가 운영체제 그래픽스와 네트워크 소켓을 직접 제어합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="heart"></i> 4. 개발자 생태계의 반응: '장인정신의 승리'
            </h3>
            <p>
              해커뉴스(HN)와 레딧의 개발자들은 ZapFast의 등장에 뜨거운 찬사를 보내고 있다. 
              <em>"우리는 언제부터 텍스트 몇 줄 표시하는 데 기가바이트 단위의 램을 당연하게 여기게 되었는가?"</em>라는 자성의 목소리와 함께, 웹 기술 편의주의에 젖어 있던 데스크톱 소프트웨어 개발 풍토에 신선한 충격을 주었다는 평가다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="monitor" style="color:#10b981;"></i> ZapFast 공식 러스트 데스크톱 인터페이스
                </span>
                <span class="media-showcase-badge demo">NATIVE UI PREVIEW</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/thumb_zapfast.jpg" alt="ZapFast native UI" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 네이티브 GUI의 품격:</strong> 군더더기 없는 미니멀한 UI와 25MB 미만의 경이로운 리소스 사용량으로 완성된 데스크톱 메신저.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="flag"></i> 5. 시사점: 네이티브 앱 르네상스의 신호탄
            </h3>
            <p>
              ZapFast는 러스트와 즉시 모드 GUI가 단순히 임베디드나 게임 툴용에 그치지 않고, 일반 엔드유저용 상용 소프트웨어의 훌륭한 대안이 될 수 있음을 증명했다. 
              일렉트론의 독점에 지친 개발자들에게 진정한 성능 최적화의 미학을 일깨워주는 프로젝트다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://github.com/crmne/zapfast" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
