# -*- coding: utf-8 -*-
# Story 1: os6/nospeaker (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] os6/nospeaker : COVER STORY                       -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_nospeaker.jpg" alt="nospeaker MacBook Force Touch Trackpad Haptic Voice Synthesis Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> COVER EXPLOSION #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔊 10.7시간 만에 ★348 폭주 · 스피커 0%로 유리 트랙패드가 노래한다</span>
              <span class="platform-tag">GitHub Newcomer #1 &amp; Hardware Hack</span>
              <span class="platform-tag">os6 / nospeaker</span>
            </div>

            <h2 class="main-lead-headline">
              <span id="hero-title">"맥북 스피커를 꺼도 트랙패드가 노래한다" — 애플 비공개 햅틱 API를 뚫어 유리판을 4,000Hz 스피커로 바꾼 역발상 'nospeaker'</span>
            </h2>

            <div class="article-subheadline">
              macOS 비공개 프레임워크 MultitouchSupport(MTActuationCreateFromDictionary·MTActuationActuate)를 런타임에 dlopen으로 직접 호출, macOS say 음성의 10ms 단위 F1+F2 포먼트를 98Hz~3,951Hz 사인파로 변환해 Force Touch 트랙패드 모터로 합성·재생 (MIT, Apple Developer ID 공증)
            </div>
            <p class="article-snippet">
              맥북의 볼륨을 완전히 음소거(Mute)로 내렸는데도 책상 위 알루미늄 바디와 유리 트랙패드에서 또렷한 사람 목소리와 랩, 멜로디가 흘러나옵니다. 공개 <strong>10.7시간 만에 348개의 스타(시간당 +32.5스타)</strong>를 쓸어 담은 Swift 프로젝트 <strong>os6/nospeaker</strong>는 애플이 공개 API 뒤에 단 3가지 고정 클릭 패턴으로만 묶어둔 Taptic/Force Touch 햅틱 액추에이터를 비공개 <code>MultitouchSupport</code> 프레임워크 직결로 해방시키며 "하드웨어의 진짜 한계는 실리콘이 아니라 OS 추상화 계층에 있다"는 사실을 극적으로 증명했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 음소거된 맥북의 유리판 위에서 깨어난 두 번째 성대
            </h3>
            <p>
              오늘 새벽 개발자 커뮤니티 타임라인을 뒤흔든 실험은 거창한 GPU 클러스터가 아니라 단 한 줄의 터미널 명령(<code>curl -fsSL a90.com/nospeaker | sh</code>)에서 시작됐다. 안내 문구는 단 세 줄이다. <em>"맥의 소리를 꺼라(Mute your Mac). 책상 위에 올려놓아라. 손가락을 유리에서 떼라."</em> 그리고 1분 30초간의 쇼가 시작되는 순간, 스피커 그릴이 완전히 침묵한 맥북의 Force Touch 트랙패드에서 낮고 선명한 음성과 비트가 울려 퍼진다.
            </p>
            <p>
              2015년 이후 출시된 모든 맥북과 Magic Trackpad 2 이상 모델에는 물리적인 클릭 버튼이 없다. 사용자가 누를 때 느끼는 딸깍임은 유리판 아래 장착된 소형 리니어 공진 액추에이터(LRA) 햅틱 모터가 만들어내는 정교한 착각이다. <strong>os6/nospeaker</strong>는 이 모터가 원래 설계된 짧은 탭(Tap) 용도를 넘어 <strong>초당 최대 4,000번(4kHz)</strong>까지 왕복 구동될 수 있다는 물리적 사실에 착안해, 트랙패드 유리 전체를 공명 진동판(Acoustic Diaphragm)으로 탈바꿈시켰다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "공개 API는 세 번의 클릭만 허락했지만, 물리 모터는 4kHz까지 노래할 수 있었다"
            </h3>
            <p>
              왜 지금까지 어떤 서드파티 앱도 트랙패드로 음성을 합성하지 못했을까? 애플의 공식 AppKit/CoreHaptics 공개 API(<code>NSHapticFeedbackManager</code>)가 개발자에게 허용하는 것은 <code>alignment</code>, <code>levelChange</code>, <code>generic</code>이라는 <strong>단 세 종류의 고정된 탭 프리셋</strong>뿐이기 때문이다. 임의의 주파수·진폭·지속시간을 지정해 연속 파형을 쏘아 올리는 인터페이스는 시스템 내부 비공개 영역에 봉인돼 있었다.
            </p>

            <div class="editorial-quote">
              <p>
                "트랙패드에는 스피커가 없다. 다만 유리 아래 작은 햅틱 모터가 있을 뿐이다. <strong>Apple의 공개 햅틱 API는 3가지 고정 탭만 제공하지만, MultitouchSupport를 통해 모터를 초당 4,000번 구동하면 유리 자체가 소리를 내는 목소리가 된다.</strong>"
              </p>
              <small>— os6/nospeaker 공식 아키텍처 설명 (MIT License · Apple Notarized Binary)</small>
            </div>

            <p>
              공개 10.7시간 만에 스타 348개를 돌파한 <code>nospeaker</code>는 단순한 장난감 해킹을 넘어, 거대 OS 벤더가 하드웨어 안전성과 배터리 보호라는 명분 아래 얼마나 두꺼운 소프트웨어 유리천장(API Wall)을 쳐두고 있는지를 드러낸다. 심지어 이 바이너리는 커널 패닉이나 <code>SIP(시스템 무결성 보호)</code> 해제 없이 <strong>Apple Developer ID 서명과 공증(Notarization)까지 통과한 순수 유저스페이스 Swift 바이너리</strong>로 배포됐다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: LPC 포먼트 추출과 MultitouchSupport 직결 파이프라인 해부
            </h3>
            <p>
              <code>nospeaker.swift</code> 소스코드를 열어보면, 음성을 직접 PCM 오디오로 보내는 대신 햅틱 모터의 제한된 대역폭과 듀티 사이클에 최적화된 <strong>초경량 포먼트 보코더(Formant Vocoder)</strong> 아키텍처가 드러난다:
            </p>
            <ul>
              <li><strong>인메모리 음성 생성 및 10ms 선형 예측(LPC) 포먼트 분해:</strong> macOS 내장 음성 엔진(<code>say</code>, <code>--voice</code> 옵션으로 모든 시스템 보이스 선택 가능)으로 텍스트를 메모리 버퍼에 발화한 뒤, 10밀리초(ms) 프레임마다 선형 예측 부호화(Linear Prediction)를 수행해 음성의 핵심 지문인 <strong>제1·제2 공명 주파수(F1 + F2 Formants)</strong>와 음량, 기본 피치(Pitch)를 추출한다.</li>
              <li><strong>피치 동기 사인파 재시작(Pitch-Synchronous Burst):</strong> 추출된 F1·F2 주파수를 두 개의 순수 사인파 톤으로 합성하되, 성대의 성문 파동처럼 매 피치 주기(Beat of the pitch)마다 위상을 재시작해 햅틱 모터가 인간 목소리 특유의 버즈(Buzz) 질감과 모음·자음 명료도를 구현하도록 설계했다.</li>
              <li><strong><code>dlopen</code> 런타임 심볼 바인딩 &amp; 98Hz~3,951Hz 공진 프로파일링:</strong> macOS의 <code>/System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport</code>를 런타임에 동적 로드해 <code>MTDeviceCreateList</code>, <code>MTActuatorCreateFromDeviceID</code>, <code>MTActuationCreateFromDictionary</code>, <code>MTActuationActuate</code> 심볼을 바인딩한다. 맥북 자체 마이크로 98Hz부터 3,951Hz까지 모든 반음(Semitone)의 음압과 순음도를 실측해 가장 잘 울리는 대역을 매핑했으며, 모터 정격 최대 출력은 절대 초과하지 않는다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">nospeaker 포먼트 추출 → 비공개 MultitouchSupport 햅틱 음성 합성 파이프라인</span>
                <span class="schematic-badge">Swift · MIT · 98Hz–3,951Hz · Zero Speakers Used</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. In-Memory Voice &amp; LPC</div>
                  <div class="schematic-desc">
                    macOS <code>say</code> 음성 메모리 버퍼 렌더링<br>
                    10ms 프레임 단위 선형 예측(LPC) 분석<br>
                    제1·제2 포먼트(<strong>F1 + F2</strong>) 추출<br>
                    기본 피치(Pitch) 및 진폭 엔벨로프 계산
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Pitch-Sync Tone Synthesis</div>
                  <div class="schematic-desc">
                    F1·F2를 2채널 사인파 톤 목록으로 변환<br>
                    피치 주기마다 파형 재시작(성대 질감 모사)<br>
                    <code>--sweep</code> 100Hz~4kHz 대역 응답 매핑<br>
                    정격 안전 한계 내 진폭 클램핑 유지
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. MultitouchSupport Actuation</div>
                  <div class="schematic-desc">
                    <code>dlopen</code>으로 비공개 프레임워크 동적 바인딩<br>
                    <code>MTActuationCreateFromDictionary</code> 패킷 생성<br>
                    <code>MTActuationActuate</code>로 4,000Hz 모터 구동<br>
                    Force Touch 유리판 진동 → 가청 음성 출력
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">os6/nospeaker 저장소 실화면 — 98Hz~3,951Hz 트랙패드 음향 응답 스펙트럼 &amp; 원클릭 실행</span>
              </div>
              <img src="../assets/images/demo_nospeaker.png" alt="os6 nospeaker GitHub Repository Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/os6/nospeaker 실화면: Apple Developer ID 서명 및 공증을 마친 단일 바이너리 구조와 맥북 내장 마이크로 실측한 98Hz~3,951Hz 트랙패드 햅틱 모터의 주파수별 음압·배음 분포, 10ms 포먼트 파이프라인.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 플랫폼 경계와 보안: 비공개 API의 역설과 '하드웨어 소유권' 논쟁
            </h3>
            <p>
              <code>nospeaker</code>의 등장은 하드웨어 커뮤니티에 두 가지 묵직한 질문을 던진다. 첫째는 <strong>"내가 구매한 노트북의 액추에이터를 OS 제조사가 막아둔 대역으로 구동할 권리"</strong>다. Apple Silicon Mac(M1~M5 Max, macOS 12+)에서 Intel Mac(macOS 13+)까지 Force Touch 트랙패드는 물리적으로 오디오 대역폭(100Hz~4kHz)을 재생할 능력을 갖추고 있었지만, 앱스토어 샌드박스와 공개 SDK 정책이 그 잠재력을 '3가지 클릭 효과'로만 봉인해 왔다.
            </p>
            <ul>
              <li><strong>macOS 업데이트 취약성과 앱스토어 불가:</strong> <code>MultitouchSupport.framework</code>는 문서화되지 않은 사설 프레임워크이므로 차기 macOS 마이너 업데이트에서도 심볼 시그니처가 바뀔 수 있으며, Mac App Store 심사에는 통과할 수 없다. 제작자가 소스코드(<code>nospeaker.swift</code>)와 공증된 CLI 릴리스(<code>a90.com/nospeaker</code>)를 MIT로 공개한 이유다.</li>
              <li><strong>초음파·측면 채널(Side-Channel) 시사점:</strong> 스피커 드라이버가 완전히 비활성화되거나 하드웨어 킬스위치로 차단된 에어갭(Air-gapped) 맥북에서도 트랙패드 햅틱 모터만으로 가청 대역 및 고주파 진동 신호를 생성할 수 있다는 점은 보안 연구자들 사이에서도 흥미로운 음향 측채널 사례로 재조명되고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 모든 하드웨어는 소프트웨어의 상상력이 닿기 전까지 잠들어 있다
            </h3>
            <p>
              수억 대의 맥북 사용자들은 지난 10년간 매일 손끝 아래의 유리판을 누르면서도 그 안에 작은 스피커 하나가 숨어 있다는 사실을 몰랐다. <code>nospeaker</code>는 새로운 칩을 납땜한 것도, 드라이버를 탈옥한 것도 아니다. 단지 10밀리초마다 목소리의 두 공명점을 읽어 잠자던 햅틱 모터에 사인파를 건넸을 뿐이다.
            </p>
            <p>
              스피커를 끈 적막한 책상 위에서 트랙패드가 스스로 말을 걸어오는 그 기이한 순간, 우리는 다시금 묻게 된다. 지금 당신의 책상 위 기기 안에는 아직 API로 열리지 않은 어떤 물리 법칙이 잠들어 있는가?
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=nospeaker+macbook+trackpad+talk+haptic" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/os6/nospeaker" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
