# -*- coding: utf-8 -*-
# Story 3: Th0rgal/satmux

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 3] Th0rgal/satmux : 기내 와이파이 지옥 탈출 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_satmux.jpg" alt="satmux GEO inflight wifi TCP multiplexer" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="plane" style="width:12px;height:12px;fill:#fff;"></i> VIRAL HACK</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 1만 미터 상공 600ms 위성 랙을 1초로 단축한 네트워크 해킹</span>
              <span class="platform-tag">GitHub Rocket</span>
              <span class="platform-tag">Th0rgal / satmux</span>
            </div>
            
            <h2 class="article-lead-headline">
              비행기 안 600ms 지연시간을 산산조각 내다 — 순수 파이썬 BBR 멀티플렉서 'satmux'
            </h2>

            <div class="article-subheadline">
              기내 Wi-Fi의 끔찍한 3-way 핸드셰이크 지연을 단 1회의 RTT로 압축… 외부 라이브러리 의존성 제로(Zero Deps)의 표준 라이브러리만으로 40초 로딩 웹사이트를 2초 만에 렌더링
            </div>
            <p class="article-snippet">
              정지궤도(GEO) 위성을 거치는 항공기 기내 Wi-Fi의 620ms 왕복 지연 탓에 웹 서핑이 불가능했던 고통을 해결한 오픈소스 도구 'satmux'가 등장했습니다. 지상 중계 서버와의 영구 BBR TCP 파이프라인과 1-RTT 그라운드 TLS 프록시를 순수 파이썬 표준 라이브러리만으로 구현하여 상공에서의 체감 속도를 20배 이상 끌어올린 기상천외한 네트워크 엔지니어링을 파헤칩니다.
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
              <i data-lucide="flame"></i> 1. 리드: 1만 미터 상공에서 터지는 엔지니어의 분노
            </h3>
            <p>
              장거리 국제선 비행기에 탑승해 거금을 들여 기내 Wi-Fi(Inmarsat GX, Viasat, Panasonic)를 결제한 순간을 기억하는가? 
              스피드테스트를 돌려보면 다운로드 속도는 10~20Mbps로 그럭저럭 나오는데, 
              정작 일반 웹사이트나 깃허브, 슬랙을 열려고 하면 브라우저 탭의 로딩 휠이 30초에서 1분 동안 빙빙 돌다 타임아웃 오류를 뱉어내기 일쑤다.
            </p>
            <p>
              이 기괴한 현상의 주범은 대역폭이 아니라 <strong>정지궤도 위성과의 물리적 거리(지상 36,000km)로 인해 발생하는 600~800ms의 극단적인 왕복 지연시간(RTT)</strong>이다. 
              오늘 깃허브와 해커뉴스에서 네트워크 엔지니어들을 열광시킨 <strong>Th0rgal/satmux</strong>는 
              수십 년간 항공사 통신망이 방치해온 이 핸드셰이크 병목을 순수 파이썬 표준 라이브러리(Zero Dependencies)만으로 완전히 해결해 낸 통쾌한 네트워크 해킹이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 현대 웹의 '수십 개 TCP 연결'이 위성 망을 죽이는 메커니즘
            </h3>
            <p>
              현대 웹페이지는 평균 50~100개의 서브 리소스(이미지, CSS, 스크립트, 광고 트래커)를 포함한다. 
              브라우저가 이 리소스들을 가져오기 위해 수십 개의 TCP 연결을 열 때마다 일어나는 일은 지옥 그 자체다:
            </p>

            <div class="editorial-quote danger">
              <p>
                "DNS 쿼리(1 RTT) + TCP 3-way 핸드셰이크(1 RTT) + TLS 핸드셰이크(1~2 RTT) + HTTP 요청/응답(1 RTT). 
                단 하나의 도메인에 연결하는 데만 최소 4~5번의 RTT가 소모된다. 
                <strong>RTT가 620ms라면 첫 바이트(TTFB)를 받기도 전에 이미 3초가 증발하고, 10개 도메인이 얽히면 40초가 훌쩍 넘어간다.</strong>"
              </p>
              <small>— satmux 벤치마크 분석 보고서</small>
            </div>

            <p>
              satmux의 창시자는 인말새트 GX Ka-band(SITA 암스테르담 지상국 경유, 620ms RTT) 환경에서 실측 테스트를 진행했다. 
              순수 브라우저로 접속 시 42초가 걸리던 고용량 웹사이트가 <strong>satmux 터널을 통과하는 순간 단 2.1초 만에 완벽히 렌더링</strong>되는 기적이 입증되었다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: 단일 Warm BBR TCP 터널과 1-RTT Ground-TLS
            </h3>
            <p>
              satmux가 외부 패키지 하나 없이 파이썬 기본 모듈(socket, ssl, zlib, select)만으로 지연시간을 95% 단축시킨 비밀은 전송 계층의 재설계다:
            </p>
            <ul>
              <li><strong>단일 지속 BBR TCP 연결 풀:</strong> 항공기 안의 satmux 클라이언트와 지상 서버(AWS/GCP/VPS) 사이에 단 하나의 영구 TCP 연결을 맺고 구글 BBR 혼잡 제어 알고리즘을 적용. 패킷 손실이 잦은 위성 링크에서도 슬로우 스타트(Slow Start) 없이 최대 윈도우 크기를 상시 유지.</li>
              <li><strong>지상 위임 TLS (Ground-TLS Relay):</strong> 브라우저가 보내는 수십 개의 HTTPS 연결을 항공기 로컬 프록시가 가로채 단일 satmux 프레임으로 다중화(Multiplexing)하여 지상으로 전송. 무거운 TLS 핸드셰이크는 지상 초고속 망에서 1ms 만에 완결.</li>
              <li><strong>인라인 zlib 바이트스트림 압축:</strong> 텍스트, HTML, JSON 페이로드를 위성 업링크/다운링크 구간에서 실시간 압축하여 페이로드 크기를 60% 이상 축소.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="network" style="color:#0ea5e9;"></i> satmux GEO 기내 위성 와이파이 가속 파이프라인
                </span>
                <span class="schematic-badge">1-RTT GROUND-TLS MULTIPLEXING</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">로컬 SOCKS5/HTTP 가로채기</div>
                  <div class="step-tech">In-Flight Laptop (127.0.0.1:8080)</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">단일 지속 BBR TCP + zlib</div>
                  <div class="step-tech">Single Tunnel over 620ms GEO Satellite Link</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">지상 중계국 고속 TLS 핸드셰이크</div>
                  <div class="step-tech">Fast Ground Server Relay (1-RTT Direct Fetch)</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 원리:</strong> 비행기 안에서 수십 개의 TCP/TLS 연결을 개별적으로 위성으로 쏘아 올리지 않고, 지상에 미리 열어둔 단 하나의 따뜻한(Warm) BBR TCP 파이프라인에 모든 트래픽을 밀어 넣어 왕복 왕복 횟수를 1회로 봉인합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-check"></i> 4. 비즈니스 해자: 엔지니어링이 통신 재벌의 나태함을 이기다
            </h3>
            <p>
              항공 위성 통신 시장을 독점해온 글로벌 통신사들은 승객들에게 편당 수만 원의 고액 요금을 징수하면서도, 
              이러한 전송 계층 프록시 최적화를 전혀 도입하지 않았다. 
              승객들이 인터넷이 느려 불평할 때마다 "위성 거리 때문"이라는 변명만 되풀이해 왔다.
            </p>
            <p>
              satmux는 한 엔지니어가 비행기 좌석에서 작성한 단 몇백 줄의 파이썬 코드만으로도 
              수조 원을 들인 위성 통신망의 실효 체감 속도를 즉각 20배 개선할 수 있음을 입증했다. 
              원격 개발자, 디지털 노마드, 해외 출장자들에게 이 도구는 기내 필수 생존 장비가 되었다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="terminal" style="color:#10b981;"></i> satmux 실측 벤치마크 및 저장소 아키텍처
                </span>
                <span class="media-showcase-badge demo">OFFICIAL REPO PREVIEW</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_satmux.png" alt="satmux benchmark and repo" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 실측 벤치마크 로그:</strong> 인말새트 620ms Ka-band 환경에서 단일 BBR 멀티플렉싱을 통해 로딩 시간을 42초에서 2.1초로 단축한 공식 측정 결과.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="zap"></i> 5. 키커: 물리학의 한계를 비틀어내는 오픈소스의 마법
            </h3>
            <p>
              빛의 속도와 36,000km라는 물리적 거리를 바꿀 수는 없다. 
              하지만 그 공간을 오가는 데이터의 규칙을 바꾸는 것은 오직 엔지니어의 창의력에 달려 있다. 
              satmux는 네트워크 프로토콜의 본질을 꿰뚫어 보는 자가 세상을 어떻게 바꾸는지를 보여주는 올해 가장 통쾌한 해킹이다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://github.com/Th0rgal/satmux" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
