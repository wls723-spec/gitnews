# -*- coding: utf-8 -*-
# Story 5: cjpais/Handy

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 5] cjpais/Handy : 100% 로컬 오프라인 딕테이션 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_handy.jpg" alt="Handy offline speech-to-text desktop app" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="mic" style="width:12px;height:12px;fill:#fff;"></i> RUST #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 단 1바이트의 음성도 빅테크 클라우드로 보내지 않는다</span>
              <span class="platform-tag">Rust Trending</span>
              <span class="platform-tag">cjpais / Handy</span>
            </div>
            
            <h2 class="article-lead-headline">
              비행기 모드에서도 0.1초 만에 타이핑하다 — Rust 기반 100% 오프라인 AI 음성 전사 'Handy'
            </h2>

            <div class="article-subheadline">
              클라우드 구독형 음성 전사 서비스(오터, 노타)에 마침표… Rust와 온디바이스 로컬 모델로 시스템 전역 글로벌 단축키 한 번에 마우스 커서 위치로 텍스트를 쏟아내는 완벽한 사생활 보호 도구
            </div>
            <p class="article-snippet">
              내 목소리와 회의 녹음이 빅테크 AI 학습용으로 무단 수집되는 공포를 끝장낼 100% 오프라인 데스크톱 앱 'Handy'가 Rust 트렌딩 1위에 올랐습니다. 네트워크가 완전히 차단된 상태에서도 로컬 Whisper 및 Moonshine 모델을 활용해 0.1초 만에 음성을 정확한 텍스트로 타이핑해 주는 온디바이스 딕테이션의 진가를 분석합니다.
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
              <i data-lucide="flame"></i> 1. 리드: "내 목소리는 누구의 서버로 가고 있는가?"
            </h3>
            <p>
              사내 기밀 회의, 변호사 상담, 의사의 환자 진료 메모, 혹은 머릿속에 번뜩인 신사업 아이디어를 음성 인식으로 받아 적을 때마다 
              가슴 한편에 찜찜한 불안감이 스친다. 
              상용 클라우드 음성 전사 서비스(Otter, Notta, 디스플레이 AI 비서 등)의 약관 구석에는 "서비스 개선 및 모델 학습을 위해 음성 데이터가 사용될 수 있다"는 독소 조항이 숨겨져 있기 때문이다.
            </p>
            <p>
              오늘 Rust 커뮤니티와 깃허브에서 찬사를 받으며 급부상한 <strong>cjpais/Handy</strong>는 
              이 사생활 침해 공포를 원천 차단하는 가장 우아한 해법이다. 
              <strong>네트워크 선을 뽑아버린 상태에서도, 시스템 전역 단축키 하나로 마이크 입력을 가로채 0.1초 만에 어떤 입력창에든 정확한 텍스트를 실시간으로 타이핑</strong>해 주는 순수 Rust 네이티브 애플리케이션이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 구독료 0원, 지연시간 0ms, 프라이버시 100%
            </h3>
            <p>
              기존에도 Whisper를 로컬에서 돌리는 파이썬 스크립트들이 있었지만, 
              기가바이트 단위의 무거운 PyTorch 런타임과 느린 시동 시간, 불안정한 단축키 연동 때문에 일상 업무에서 자연스럽게 쓰기에는 턱없이 부족했다.
            </p>

            <div class="editorial-quote danger">
              <p>
                "Handy는 파이썬 인터프리터도, 웹뷰도 사용하지 않는다. 
                Rust로 작성된 단일 바이너리가 백그라운드에서 15MB 남짓한 메모리만 점유하며 대기하다가, 
                <strong>사용자가 단축키를 누르고 말하는 순간 온디바이스 GPU/NPU를 깨워 무지연 실시간 텍스트로 변환</strong>한다."
              </p>
              <small>— Handy 오픈소스 프로젝트 아키텍처 개요</small>
            </div>

            <p>
              맥, 윈도우, 리눅스 어디서든 동작하며, 
              터미널, 노션, 슬랙, 크롬 브라우저 등 현재 포커스가 맞춰진 커서 위치에 가상 키보드 이벤트를 통해 즉각 타이핑되므로 
              별도의 복사-붙여넣기 과정조차 필요 없다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: Push-to-Talk 캡처와 로컬 텐서 런타임
            </h3>
            <p>
              Handy가 상용 음성 AI 서비스를 뛰어넘는 즉각적인 반응성을 실현한 기술적 구조는 다음과 같다:
            </p>
            <ul>
              <li><strong>OS 네이티브 글로벌 단축키 및 오디오 훅:</strong> cpal과 rdev 라이브러리를 통해 운영체제 레벨에서 마이크 스트림과 키보드 이벤트를 밀리초 단위로 가로챔. Push-to-Talk(누르고 말하기) 및 토글 모드 완벽 지원.</li>
              <li><strong>양자화 온디바이스 음성 모델 파이프라인:</strong> OpenAI Whisper(int8/int4) 및 Useful Sensors의 Moonshine 경량 모델을 내장하여, 고가의 외장 그래픽카드 없이 일반 노트북 CPU/NPU에서도 4배속 이상의 실시간 스트리밍 추론 완결.</li>
              <li><strong>가상 입력 주입(Enigo / uinput):</strong> 전사된 텍스트를 클립보드에 담아두지 않고 운영체제 가상 키보드 서브시스템을 통해 다이렉트로 타이핑 주입하여 애플리케이션 호환성 극대화.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="mic" style="color:#0ea5e9;"></i> Handy 로컬 온디바이스 음성 전사 파이프라인
                </span>
                <span class="schematic-badge">100% OFFLINE RUST ENGINE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">글로벌 키 & 마이크 훅</div>
                  <div class="step-tech">Rust cpal Raw Audio Buffer (Zero Cloud Telemetry)</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">로컬 텐서 STT 추론</div>
                  <div class="step-tech">On-Device Whisper / Moonshine (GPU & NPU Accelerated)</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">활성 커서 위치 직접 타이핑</div>
                  <div class="step-tech">Virtual Keyboard Injected Text Output (Zero Lag)</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 원리:</strong> 음성 신호가 컴퓨터 밖 인터넷 망으로 단 1바이트도 나가지 않고, 오디오 입력 &rarr; 로컬 모델 변환 &rarr; 텍스트 화면 주입까지 전 과정이 사용자 PC 메모리 내부에서 완결됩니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-check"></i> 4. 비즈니스 해자: 엄격한 규제 산업에서의 독보적 가치
            </h3>
            <p>
              병원, 법률 사무소, 금융 기관, 방위 산업체 등은 환자 진료 기록이나 고객 금융 정보의 외부 유출이 법적으로 엄격히 금지되어 있다. 
              이 때문에 의사나 변호사들은 편리한 AI 음성 전사의 혜택을 누리지 못하고 키보드를 직접 두드려야 했다.
            </p>
            <p>
              Handy는 외부 네트워크 통신 권한을 아예 배제함으로써 HIPAA, GDPR 등 세계에서 가장 엄격한 프라이버시 컴플라이언스를 100% 통과할 수 있는 유일한 대안이다. 
              월 수십 달러의 구독료를 요구하는 SaaS 시장을 로컬 소프트웨어가 단숨에 제압한 사례다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="monitor" style="color:#10b981;"></i> Handy 공식 홈페이지 & 데스크톱 인터페이스
                </span>
                <span class="media-showcase-badge demo">OFFICIAL SITE PREVIEW</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_handy.png" alt="Handy desktop application in action" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 공식 웹사이트 및 앱 시연:</strong> 복잡한 클라우드 가입 없이 다운로드 즉시 로컬 오프라인 음성 인식을 지원하는 Handy의 공식 포털.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="zap"></i> 5. 키커: 가장 강력한 보안은 연결을 끊는 것이다
            </h3>
            <p>
              "모든 데이터가 클라우드로 흘러들어가는 시대에, 당신의 목소리만큼은 오직 당신의 손끝과 로컬 디스크에만 머물러야 한다." 
              Handy는 진정한 기술의 발전이 편리함뿐만 아니라 인간의 존엄과 사생활을 지키는 방향으로 나아가야 함을 증명하는 걸작이다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://handy.computer" target="_blank" class="project-link demo">
                  <i data-lucide="globe" style="width:16px;height:16px;"></i> 공식 웹사이트 방문
                </a>
                <a href="https://github.com/cjpais/Handy" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
