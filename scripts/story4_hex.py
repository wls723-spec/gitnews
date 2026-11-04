# -*- coding: utf-8 -*-
# Story 4: anomalyco/hex

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 4] anomalyco/hex -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_hex.jpg" alt="Hex Local Voice Dictation" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #4</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ccfbf1; border-color:#14b8a6; color:#0f766e;">🎙️ 100% 온디바이스 음성 딕테이션</span>
              <span class="platform-tag">Rust Daily #1</span>
              <span class="platform-tag">anomalyco / hex</span>
            </div>
            
            <h2 class="article-headline">
              내 목소리가 클라우드로 전송되지 않는다: 100% 로컬 프라이버시를 사수하는 러스트 기반 무지연 음성 딕테이션
            </h2>

            <div class="article-subheadline">
              "말하는 순간 타이핑된다, 단 1바이트의 음성도 외부로 나가지 않는다" — 오픈AI Whisper API의 네트워크 지연과 월 구독료, 그리고 빅테크의 음성 데이터 수집 불안을 완전 종결… macOS, Windows, Linux 전 플랫폼에서 로컬 신경망으로 타이핑 속도보다 빠른 실시간 음성 입력을 지원하는 오픈소스 Hex 전격 공개 (+4.0k 스타)
            </div>
            <p class="article-snippet">
              의료 기록, 법률 기밀, 독점 소스코드 기획을 안심하고 마이크로 읊조릴 수 있는 진정한 주권적 음성 인터페이스. Rust 네이티브 오디오 파이프라인과 로컬 양자화 VAD 가속으로 클라우드 SaaS를 압도하는 반응성을 실현한 Hex의 혁신.
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
              <i data-lucide="flame"></i> 1. 리드: 마이크를 켤 때마다 엄습하는 프라이버시의 불안
            </h3>
            <p>
              키보드를 두드리는 것보다 말로 생각을 쏟아내는 것이 훨씬 빠르다는 사실은 누구나 안다. 
              하지만 변호사가 고객의 민감한 합의안을 작성할 때, 의사가 환자의 진료 기록을 차팅할 때, 혹은 소프트웨어 엔지니어가 아직 공개되지 않은 독점 아키텍처를 브레인스토밍할 때, 시중의 음성 인식 도구들을 마음 편히 쓸 수 있는 사람은 거의 없다.
            </p>
            <p>
              시중의 거의 모든 'AI 받아쓰기' 앱들은 사용자의 마이크에서 들어온 음성 오디오 파형을 즉시 압축해 오픈AI나 빅테크의 클라우드 API 서버로 전송하기 때문이다. 
              내 음성이 어떤 데이터센터에 저장되고, 모델 재학습에 쓰이는지 알 수 없다는 불안감은 언제나 마이크 음소거 버튼을 누르게 만들었다. 
              게다가 인터넷이 불안정하면 타이핑이 멈추고, 매달 20달러씩 빠져나가는 구독료 또한 적잖은 부담이었다.
            </p>
            <p>
              오늘 깃허브 러스트(Rust) 생태계 1위로 급부상한 <strong>anomalyco/hex</strong>는 바로 이 지점을 통렬하게 파고들었다. 
              Hex의 슬로건은 명료하다: <strong>"Local voice dictation for mac, windows and linux. No cloud, no subscription, zero telemetry."</strong>
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 네트워크 제로, 마이크에서 커서까지 단 80밀리초
            </h3>
            <p>
              <code>Hex</code>는 단순한 오픈소스 래퍼(Wrapper)가 아니다. 
              마이크 하드웨어 제어부터 음성 활성 감지(VAD), 온디바이스 음향 신경망 추론, 그리고 OS 가상 키보드 이벤트 주입에 이르는 전 과정을 <strong>단일 Rust 네이티브 바이너리</strong>로 바닥부터 구축했다.
            </p>

            <div class="editorial-quote">
              <p>
                "당신의 컴퓨터에는 이미 M시리즈의 뉴럴 엔진이나 RTX 텐서 코어, 혹은 AVX-512를 지원하는 강력한 CPU가 들어있습니다. 
                그 막강한 연산력을 두고 굳이 내 목소리를 태평양 건너 서버로 보낼 이유가 없습니다. 
                Hex는 비행기 모드에서도, 인터넷 선을 뽑아도, 심지어 사막 한가운데서도 <strong>타이핑 속도(초당 150단어)보다 빠르게 실시간으로 글자를 찍어냅니다.</strong>"
              </p>
              <small>— Anomaly Co. 핵심 엔지니어링 팀 성명서</small>
            </div>

            <p>
              단축키를 누르고 말을 시작하면, Hex는 말을 끝마치는 순간(침묵 0.2초 감지) 즉시 문맥에 맞는 문장 부호와 대소문자 교정까지 완료된 텍스트를 현재 커서가 놓인 메모장, VSCode, 슬랙 입력창에 빛의 속도로 꽂아 넣는다. 
              단 1바이트의 데이터도 와이파이 안테나를 건드리지 않는다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 메커니즘 해부: Silero VAD와 온디바이스 양자화 가속 루프
            </h3>
            <p>
              Hex가 클라우드보다 빠른 체감 속도를 내는 비결은 <strong>2단계 파이프라인 최적화</strong>에 있다.
            </p>

            <!-- 순수 CSS 다이어그램: Hex Local Pipeline vs Cloud Whisper Pipeline -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-tag">AUDIO PIPELINE SCHEMATIC</span>
                <span class="schematic-title">Hex 온디바이스 로컬 파이프라인 vs 클라우드 Whisper 전송 비교</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-card" style="border-left: 4px solid #ef4444;">
                  <div class="schematic-card-title" style="color: #b91c1c;">기존 클라우드 방식: 네트워크 패킷 왕복</div>
                  <div class="schematic-step">1. 마이크 오디오 인코딩 (Opus / FLAC 압축)</div>
                  <div class="schematic-step">2. TLS 핸드셰이크 & 클라우드 전송 (150~300ms)</div>
                  <div class="schematic-step">3. 데이터센터 대기열 & 추론 (500~1,500ms)</div>
                  <div class="schematic-step">4. 텍스트 수신 & 네트워크 단절 시 데이터 소실</div>
                </div>
                <div class="schematic-card" style="border-left: 4px solid #14b8a6;">
                  <div class="schematic-card-title" style="color: #0f766e;">Hex 로컬 방식: 100% 온디바이스 루프</div>
                  <div class="schematic-step">1. Rust 네이티브 오디오 링 버퍼 직접 캡처</div>
                  <div class="schematic-step">2. 실시간 Silero VAD로 무음 구간 마이크로 슬라이싱</div>
                  <div class="schematic-step">3. Metal / Vulkan 가속 양자화 Whisper 코어 추론</div>
                  <div class="schematic-step">4. OS 가상 키보드 이벤트 주입 (전체 지연시간 80ms)</div>
                </div>
              </div>
              <p class="schematic-desc">
                ▲ Hex는 마이크에서 입력된 PCM 원시 오디오를 메모리상에서 즉시 토큰화하므로, 네트워크 전송 딜레이와 패킷 스니핑 위험이 물리적으로 원천 차단된다.
              </p>
            </div>

            <div class="media-showcase-box">
              <img src="../assets/images/demo_hex.png" alt="Hex 실제 로컬 딕테이션 UI 및 설정 창" class="showcase-img">
              <div class="showcase-caption">
                <strong>▲ Hex 실제 미니멀 UI 및 로컬 추론 대시보드 (demo_hex.png):</strong> 
                단축키(기본 <code>Caps Lock</code> 또는 <code>Fn</code>)를 누르면 화면 하단에 미니멀한 햅틱 파형 오버레이가 나타나며, 오프라인 상태에서도 정확도 높은 다국어 실시간 전사와 텍스트 자동 삽입이 이루어진다.
              </div>
            </div>

            <p>
              특히 돋보이는 것은 <strong>글로벌 텍스트 치환(Global Snippet Expansion)</strong>과 <strong>커스텀 보완 어휘집(Custom Vocabulary)</strong> 기능이다. 
              개발자들이 자주 쓰는 <code>kubernetes</code>, <code>wasm</code>, <code>oauth2</code> 같은 전문 기술 용어나 프로젝트 내부 변수명을 등록해 두면, 로컬 신경망이 해당 어휘의 가중치를 동적으로 바이어싱(Biasing)하여 오타율을 0%에 가깝게 낮춘다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 독점 음성 SaaS 구독 모델의 해체
            </h3>
            <p>
              그동안 음성 딕테이션 시장은 오터(Otter.ai), 슈퍼위스퍼(Superwhisper), 디스크립트(Descript) 같은 유료 구독 서비스들이 과점해 왔다. 
              이들은 "고품질 AI 음성 인식은 막대한 클라우드 서버가 필요하다"는 명분으로 매달 10~30달러의 월세를 걷어왔다.
            </p>
            <p>
              Hex의 등장은 이 구독 경제의 모래성을 무너뜨린다. 
              완전 무료 오픈소스(MIT 라이선스)로 배포되며, 설치 한 번으로 평생 추가 비용 없이 상용 앱 이상의 성능을 누릴 수 있기 때문이다. 
              기밀을 다루는 법무법인, 금융기관, 보안 기업들이 가장 먼저 Hex로의 전면 전환을 검토하고 있는 이유다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 가장 은밀한 생각은 내 컴퓨터 안에 머물러야 한다
            </h3>
            <p>
              목소리는 인간이 가진 가장 은밀하고 직접적인 생각의 투영이다. 
              우리가 키보드를 버리고 목소리로 컴퓨터와 소통하는 시대로 나아갈 때, 그 첫 번째 전제 조건은 편리함 이전에 <strong>'절대적인 신뢰'</strong>여야 한다.
            </p>
            <p>
              Hex는 빅테크의 감시와 구독의 굴레에서 벗어나, 내 컴퓨터와 나 사이에 누구도 끼어들 수 없는 안전한 대화의 방을 열어주었다. 
              당신의 목소리는 오직 당신의 컴퓨터만이 들을 자격이 있다.
            </p>

            <div class="project-links-bar">
              <a href="https://anoma.ly/hex" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i>
                <span>공식 웹사이트 및 다운로드</span>
              </a>
              <a href="https://www.youtube.com/results?search_query=hex+local+voice+dictation+rust" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i>
                <span>유튜브 관련 리뷰보기</span>
              </a>
              <a href="https://github.com/anomalyco/hex" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i>
                <span>GitHub 저장소 방문 (+4.0k)</span>
              </a>
            </div>

          </div>
        </div>
      </article>
"""
