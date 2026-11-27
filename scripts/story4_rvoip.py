# -*- coding: utf-8 -*-
# Story 4: eisenzopf/rvoip

STORY_4_HTML = r"""
      <!-- ========================================================== -->
      <!-- [HERO 4] eisenzopf/rvoip                                   -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_rvoip.jpg" alt="Pure Rust SIP WebRTC SRTP and AI Voice Agent Stack Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="phone-call" style="width:12px;height:12px;fill:#fff;"></i> RUST TELECOM #4</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🦀 HN 162점 · 외부 미디어 서버 없이 Rust 크레이트 1개로 SIP·WebRTC·AI 음성 통합</span>
              <span class="platform-tag">Hacker News &amp; Rust Communications</span>
              <span class="platform-tag">eisenzopf / rvoip</span>
            </div>

            <h2 class="article-headline">
              "SIP 프록시, RTP 엔진, WebRTC 게이트웨이를 따로 띄우던 시대는 끝났다" — 통신망 전체를 단일 Rust 라이브러리로 삼킨 'rvoip'
            </h2>

            <div class="article-subheadline">
              SIP 시그널링, RTP/SRTP 미디어, WebRTC, Media over QUIC(MoQ), 음성 AI 에이전트(Vapi·ASR/TTS·vCon)를 하나의 통화 모델로 통합하고, 단일 AWS 프로세스에서 초당 8,348콜(SIP/TLS)과 11,200 동시 통화(TLS+SRTP)를 돌파한 Rust 실시간 통신 스택 (v0.5.1 · MIT)
            </div>
            <p class="article-snippet">
              실시간 음성·영상 서비스나 AI 보이스 에이전트를 구축하려면 Asterisk·FreeSWITCH·Kamailio·RTPengine 같은 거대한 C/C++ 데몬들을 줄줄이 엮고 설정 파일과 씨름해야 했습니다. <strong>eisenzopf/rvoip</strong>는 별도의 외부 프록시나 미디어 서버가 아니라 <strong>애플리케이션 바이너리에 직접 링크하는 순수 Rust 크레이트 워크스페이스(47개 크레이트)</strong>로 설계되어, SIP 전화·브라우저 WebRTC·QUIC 미디어 팬아웃·AI 음성 에이전트를 단일 API로 처리합니다(HN <strong>162점</strong>·★<strong>522</strong>).
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
              <i data-lucide="flame"></i> 1. 리드: <code>cargo run -p rvoip-sip --example endpoint_local_call</code> 한 줄로 도는 통신국
            </h3>
            <p>
              통신(Telecom) 소프트웨어는 오랫동안 현대 소프트웨어 공학의 섬이었다. 1990년대 후반과 2000년대에 C로 작성된 Asterisk, FreeSWITCH, Kamailio, OpenSIPS가 시장을 장악했고, 개발자가 음성 통화 하나를 앱에 붙이려 해도 거대한 리눅스 데몬을 깔고, 수천 줄짜리 XML 다이얼플랜을 작성하고, NAT 트래버설과 SRTP 암호화 게이트웨이를 별도 프로세스로 띄워 소켓으로 이어 붙여야 했다. 메모리 오염 취약점(C/C++ 버퍼 오버플로)은 덤이었다.
            </p>
            <p>
              Rust 기반 실시간 통신 플랫폼 <strong><code>rvoip</code></strong>(v0.5.1)는 그 거대한 서버 랙을 통째로 <code>Cargo.toml</code> 안의 라이브러리 의존성 한 줄로 압축해 버렸다. 노트북에 Rust 외에 아무런 PBX도 데몬도 설치하지 않은 상태에서 <code>Endpoint::builder()</code>로 발신자·수신자를 띄워 루프백 통화를 성립시키고, 동일한 크레이트가 그대로 Asterisk·FreeSWITCH·Jambonz·Kamailio·OpenSIPS와의 릴리스 게이트 상호운용성 검증을 통과한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 왜 AI 보이스 에이전트 시대에 '라이브러리형 통신 스택'이 폭주하는가
            </h3>
            <p>
              최근 음성 AI 에이전트(고객센터 AI, 실시간 통역, Amazon Connect 연동) 수요가 폭증하면서 기존의 무거운 사설교환기(PBX) 아키텍처는 한계에 부딪혔다. Twilio 같은 CPaaS에 분당 요금을 내거나 무거운 미들웨어 서버 3~4개를 관리하는 대신, LLM 파이프라인을 돌리는 Rust/웹 서비스 프로세스 안에서 곧장 SIP 트렁크와 브라우저 WebRTC, 그리고 차세대 <strong>Media over QUIC(MoQ)</strong>까지 직접 종단(Terminate)하고 싶어 하는 수요가 폭발한 것이다.
            </p>

            <div class="editorial-quote">
              <p>
                "<code>rvoip</code>는 애플리케이션 옆에 따로 배포하는 서버가 아니라 <strong>라이브러리 그 자체</strong>다. 시그널링, 미디어, 코덱, NAT 트래버설, 보안, 대화 모델이 모두 워크스페이스 내 Rust 크레이트로 통합되어, 별도 SIP 프록시나 RTP 엔진 없이 코드에서 곧바로 와이어(Wire)로 통화가 나간다."
              </p>
              <small>— eisenzopf/rvoip 공식 아키텍처 명세 &amp; RFC 7502 벤치마크 리포트 (HN 162점 · ★522)</small>
            </div>

            <p>
              성능 수치도 장난 수준이 아니다. 단일 AWS <code>c8i.4xlarge</code>(16 vCPU, 32 GiB) 가상머신에서 단일 <code>rvoip</code> 프로세스를 돌려 RFC 7501/7502 벤치마크를 측정한 결과, 시그널링 전용 SIP/TLS에서 <strong>초당 8,348콜(CPS)</strong>(p50 셋업 지연 1ms), G.711 미디어를 동반한 <strong>TLS+SRTP 10초 통화에서 초당 1,124콜(동시 통화 약 11,200회선)</strong>을 실패 0건으로 버텨냈다. 과부하 2배 상황에서도 최대 처리량을 유지한 채 초과 호만 빠른 503 응답으로 쳐내고 부하가 줄면 즉시 회복한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 47개 모듈형 크레이트와 단일 통화 모델(Orchestrator)
            </h3>
            <p>
              <code>rvoip</code> 워크스페이스는 내부적으로 47개의 정교한 크레이트로 나뉘어 있지만, 사용자는 목적에 따라 단 1개의 진입점 크레이트만 <code>Cargo.toml</code>에 추가하면 된다:
            </p>
            <ul>
              <li><strong>계층 분리형 고성능 텔레포니 코어(<code>rvoip-sip</code>):</strong> RFC 7502 인증 및 주요 상용/오픈소스 교환기(Asterisk·FreeSWITCH·Kamailio·OpenSIPS·Jambonz)와의 자동화된 상호운용성 테스트 증적을 동반한 릴리스 게이트 제품이다. SIP over UDP/TCP/TLS, RTP/SRTP(SDES), hold/DTMF/전달, IVR, B2BUA, 트렁크 게이트웨이를 순수 Rust 비동기(Tokio)로 구현했다.</li>
              <li><strong>단일 오케스트레이터 파사드(<code>rvoip</code> + <code>Orchestrator</code>):</strong> <code>features = ["app"]</code>를 켜면 일반 전화망(SIP) 발신자와 브라우저(WebRTC) 발신자를 하나의 공통 통화 모델로 연결한다. 여기에 <code>vapi</code> 피처를 붙이면 호스티드 음성 AI 에이전트와 직결되고, <code>voip-3</code> 피처를 켜면 자체 ASR/TTS/대화 파이프라인과 통화 녹음·전자서명된 <strong>vCon(가상 대화 컨테이너)</strong> 저장까지 한 번에 연결된다.</li>
              <li><strong>차세대 QUIC 미디어 &amp; 엔터프라이즈 인증 생태계:</strong> WebSocket/WebTransport 기반 UCTP 제어, <code>rvoip-moq</code>를 통한 Media over QUIC 대규모 미디어 팬아웃, Amazon Connect A2A 브리지(<code>rvoip-amazon-a2a</code>), 그리고 Keycloak·LDAP·Redis·Postgres vCon·STIR/SHAKEN(발신번호 변작 방지)·IMS AKA·SAML/WebAuthn 확장 크레이트까지 레고 블록처럼 조합할 수 있다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">rvoip 단일 프로세스 다중 프로토콜(SIP·WebRTC·MoQ·AI) 통신 스택</span>
                <span class="schematic-badge">47 Rust Crates · RFC 7502 Verified · 8,348 CPS</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Multi-Transport Edge</div>
                  <div class="schematic-desc">
                    <strong>Telephony:</strong> SIP (UDP/TCP/TLS) + RTP / SRTP<br>
                    <strong>Browser:</strong> WebRTC (DTLS-SRTP) &amp; WebTransport<br>
                    <strong>Next-Gen:</strong> Media over QUIC (<code>rvoip-moq</code>)<br>
                    STIR/SHAKEN · NAT 트래버설 내장
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Unified Call Orchestrator</div>
                  <div class="schematic-desc">
                    외부 SIP 프록시·RTPengine <strong>0개</strong> (단일 바이너리)<br>
                    1,124 CPS TLS+SRTP &middot; ~11,200 동시 통화<br>
                    p50 셋업 지연 <code>1 ms</code> &middot; 2x 과부하 방어(503)<br>
                    Asterisk / FreeSWITCH / Kamailio 상호운용 검증
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Voice-AI &amp; Enterprise</div>
                  <div class="schematic-desc">
                    커스텀 ASR/TTS 파이프라인 &amp; Vapi 연동<br>
                    Amazon Connect A2A 브리지 &amp; 서명된 vCon 기록<br>
                    Keycloak · LDAP · Redis · Postgres 확장<br>
                    <code>rvoip-client</code> 모바일·임베디드 SDK 제공
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">github.com/eisenzopf/rvoip 실화면 — AWS c8i.4xlarge RFC 7501/7502 벤치마크 표</span>
              </div>
              <img src="../assets/images/demo_rvoip.png" alt="rvoip RFC 7501 7502 Benchmark Results on AWS c8i.4xlarge" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/eisenzopf/rvoip 실화면: 단일 프로세스 기준 SIP/TLS 8,348 CPS, TLS+SRTP G.711 동시 통화 약 11,200콜, p50 1ms 지연을 기록한 공식 RFC 7502 실측표.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 &amp; 산업 분기점: CPaaS 종속과 C/C++ 레거시 통신 장비를 정조준하다
            </h3>
            <p>
              해커뉴스 토론에서도 엔지니어들이 가장 반긴 대목은 "예전엔 서버를 서너 개씩 따로 띄워야 했는데 훨씬 편해졌다"는 점과 더불어, C/Go 진영이 독점하던 통신 코어에 메모리 안전한 Rust 기반의 릴리스 게이트 대안이 등장했다는 사실이었다.
            </p>
            <ul>
              <li><strong>음성 AI 인프라의 수직 통합:</strong> 분당 과금형 CPaaS(Twilio 등)를 거치지 않고 BulkVS 같은 도매 SIP 트렁크에 직접 <code>rvoip</code> 바이너리를 꽂으면, 지연시간(Latency)을 극한으로 줄이면서 통신 원가를 수십 분의 일로 낮춘 자체 AI 보이스 게이트웨이를 즉시 구축할 수 있다.</li>
              <li><strong>투명한 한계 공개가 만든 엔지니어링 신뢰:</strong> 저자는 v0.5.1 문서에 B2BUA 중계 모드, 트랜스코딩, WebRTC(DTLS-SRTP) 부하, 장애 조치(Failover)는 아직 RFC 7502 수치로 측정되지 않았음을 명확히 선을 그어 적었다. 과장 없는 릴리스 증적 공개 방식 자체가 통신사(Carrier) 엔지니어들의 신뢰를 얻는 무기다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 전화망이 서버가 아니라 '함수'가 될 때
            </h3>
            <p>
              데이터베이스가 거대한 오라클 서버에서 앱 안의 SQLite 라이브러리로 들어왔을 때 세상이 바뀌었듯, 전화와 실시간 미디어도 거대한 교환기 데몬에서 앱 코드 안의 라이브러리로 내려오고 있다.
            </p>
            <p>
              <code>cargo add rvoip</code> 한 줄 뒤에 8,000 CPS짜리 통신국과 AI 음성 에이전트 관문이 동시에 따라붙는 시대. <code>rvoip</code>는 30년 묵은 C 기반 텔레포니의 성벽에 Rust의 정밀한 쐐기를 박아 넣었다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=rvoip+rust+sip+voip+webrtc+voice+ai" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://docs.rs/rvoip/0.5.1/rvoip/" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> 공식 Rust Docs.rs API
              </a>
              <a href="https://github.com/eisenzopf/rvoip" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
