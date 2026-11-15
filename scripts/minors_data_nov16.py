# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-16

FULL_MINORS_SECTION = """
    <!-- ========================================================== -->
    <!-- [SECTION 9] 실시간 극초기 레이더 (마이너 브리핑 18선) -->
    <!-- ========================================================== -->
    <section class="minor-radar-section" id="minor-radar">
      <div class="minor-radar-header">
        <div class="minor-title-group">
          <span class="aggro-tag" style="background:#fef08a; border-color:#ca8a04; color:#854d0e;">⚡ 실시간 극초기 레이더</span>
          <h2 class="minor-section-title">갓 태어난 극초신성 &amp; 실시간 급상승 유망주 18선</h2>
        </div>
        <p class="minor-section-desc">
          직전 발행(11월 15일) 이후 30시간 동적 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다. 봇넷 스팸·중복 이력 배제 및 재귀적 동일 주제 클러스터링 알고리즘이 적용되었습니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: Quavon-dev/tarn-browser -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 10개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 2.6시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 3.92 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Electron·텔레메트리 없이 macOS·Windows·Linux·iOS·Android 네이티브 UI를 얹은 순수 Rust 프라이버시 브라우저&quot; : Tarn</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Quavon-dev/tarn-browser — 트래커·광고 차단 Shield, HTTPS-Only Strict, 자바스크립트 완전 차단 Lockdown 모드를 내장한 크로스플랫폼 Rust 브라우저</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">구글·애플 웹 래퍼의 텔레메트리와 무거운 Electron을 거부하는 Rust 네이티브 브라우저</h3>
            <div class="minor-detail-subheadline">GPL-3.0-or-later 오픈소스 · 3단계 보안 프로파일(Shield / Strict / Lockdown) 및 Split View 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 브라우저와 각종 광고 추적기가 웹을 무겁게 만드는 가운데, 계정 로그인이나 원격 텔레메트리 없이 5대 데스크톱·모바일 플랫폼에서 각 OS 네이티브 UI로 동작하는 Rust 기반 경량 브라우저 실험이 개발자들의 시선을 끌고 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[보안 계층]</strong> Shield (Tracker/Ad Block) &rarr; Strict (HTTPS-Only &amp; No Referrer) &rarr; Lockdown (JS Off &amp; Zero Site Data)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  Link Peek, Reader 모드, Split View 같은 파워유저 기능을 로컬 네트워크 격리 원칙과 함께 Rust 코어 하나로 통합했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Quavon-dev/tarn-browser" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: manuelgscom/inside-llm -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 6개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.50 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Q2_K와 Q8_0 양자화 모델이 정확히 어느 토큰에서 갈라지는지 브라우저에서 실시간 투시하는 디버거&quot; : inside-llm</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">manuelgscom/inside-llm — llama.cpp 엔진 위에서 두 GGUF 모델의 토큰별 확률 분포·탈락 후보·샘플러 컷오프를 나란히 시각화</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">양자화 손실과 샘플링 파라미터의 블랙박스를 토큰 단위 확률 지형으로 해부</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · CUDA/Vulkan 가속 `llama.cpp` 연동 · 베이스 모델 vs 파인튜닝 모델 비교 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  로컬 LLM 사용자들이 4비트/2비트 양자화 GGUF를 돌릴 때 "정확히 언제 논리가 무너지는가"를 감으로만 추측해왔습니다. `inside-llm`은 실제 추론 엔진에서 나오는 토큰 확률과 샘플러 체인 필터링 결과를 그대로 브라우저 대시보드에 펼쳐 보입니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[분석 루프]</strong> Dual GGUF (`Q2_K` vs `Q8_0`) &rarr; `llama.cpp` Logits &rarr; Sampler Filter Trace &rarr; Token Divergence Diff
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  양자화 포맷 검증뿐 아니라 파인튜닝 전후의 행동 변화나 프롬프트 온도(Temperature)·Top-P 튜닝에 정량적 X-ray를 제공합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/manuelgscom/inside-llm" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: davidwow1024/disk-map -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 7개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.45 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;`.gitignore`를 기본 존중하며 `tree`·`du`·`find`를 멀티스레드 Rust로 통합한 초고속 디스크 분석 CLI&quot; : disk-map</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">davidwow1024/disk-map — 논리·물리 용량 측정과 글롭/정규식 검색을 단일 병렬 순회로 처리하는 크로스플랫폼 저장공간 맵퍼</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">`node_modules`와 빌드 아티팩트를 스마트하게 거르며 소스 트리와 용량을 동시에 시각화</h3>
            <div class="minor-detail-subheadline">crates.io 등록 완료 · 멀티코어 병렬 디렉터리 워커 · `LS_COLORS` 및 테이블/트리 듀얼 뷰</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  개발 프로젝트에서 실제 코드 용량과 Git 추적 대상 파일 구성을 파악하려 할 때, 전통적인 `du`나 `tree`는 `.gitignore` 규칙을 몰라 수만 개 캐시 파일까지 훑느라 느리고 잡음이 많았습니다. `disk-map`은 이를 Rust 병렬 엔진으로 해결합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Multi-Thread Walker &rarr; `.gitignore` / Exclude Filter &rarr; Logical &amp; Physical Size Calc &rarr; Tree / Table View
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  Linux·macOS·Windows 네이티브 바이너리로 제공되어 CI 컨테이너나 코딩 에이전트의 코드베이스 사전 컨텍스트 파악 도구로도 유용합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/davidwow1024/disk-map" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: Dart-veider01/TradingAgents-crypto -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 140개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.3시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 11.36 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;멀티 에이전트 리서치 데스크의 매수·매도 토론을 7대 암호화폐 거래소 API로 직결한 오픈 데스크&quot; : TradingAgents Crypto</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Dart-veider01/TradingAgents-crypto — 강세/약세 애널리스트 토론·리스크 심사를 거쳐 `bytx` 단일 호출로 바이낸스·OKX 등 데모/실전 주문 연동</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">리서치 레이어(TradingAgents)와 거래소 실행 레이어(`bytx`)의 분리 설계</h3>
            <div class="minor-detail-subheadline">Binance · Bybit · OKX · KuCoin · Bitget · BingX 통합 · 기본 데모 샌드박스 안전장치</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  기존 멀티 에이전트 트레이딩 프레임워크가 보고서 출력에 머물렀다면, 이 프로젝트는 포트폴리오 매니저의 최종 판단을 통합 실행 드라이버 `bytx`에 연결해 거래소 데모 계좌에서 즉각 전략을 검증할 수 있게 확장했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[의사결정]</strong> Analysts &rarr; Bull vs Bear Debate &rarr; Risk &amp; PM Decision &rarr; `bytx` Unified Driver (Demo Default)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  거래소별 파편화된 주문 API를 단일 인터페이스로 추상화하고, 실계좌 전환 전 데모 실행을 기본값으로 강제해 안전성을 챙겼습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Dart-veider01/TradingAgents-crypto" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: linggan121/lingling-desktop-pet -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 14개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.39 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;파일을 드래그해 던지고 숫자만 답하면 이미지·PDF·오피스를 로컬 변환해 주는 AI 데스크톱 펫&quot; : 灵灵 (Lingling)</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">linggan121/lingling-desktop-pet — 내장 로컬 엔진으로 HEIC/30+ 이미지·문서 표 CSV 추출·폴더 감시 자동 변환을 수행하는 Windows 펫 에이전트</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">단순 관상용 데스크톱 펫에 실용적 로컬 파일 파이프라인과 Ollama 연동을 결합</h3>
            <div class="minor-detail-subheadline">MIT 오픈소스 · 파일 내용 인식형 메뉴 제안 · 폴더 실시간 감시(`converted/` 자동 출력)</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  PDF 분할이나 이미지 WebP 변환을 위해 매번 의심스러운 웹 변환 사이트에 파일을 올리는 대신, 바탕화면 구석에 떠 있는 펫 아이콘에 파일을 끌어다 놓고 번호(`1`, `2`)만 누르면 로컬 엔진이 즉시 변환을 마칩니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[인터랙션]</strong> Drag &amp; Drop File &rarr; Content-Aware Menu &rarr; Built-in Local Engine (Image/PDF/Office) or Ollama Chat
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  API 키 없이도 모든 파일 작업이 오프라인으로 완결되며, 필요 시 DeepSeek·Ollama 등 OpenAI 호환 엔드포인트를 붙여 대화형 지시도 처리합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/linggan121/lingling-desktop-pet" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: SyscallBrain/ratclone -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 7개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 11.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.62 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;Vim 키바인딩으로 S3·GDrive 등 클라우드 스토리지를 듀얼 패널로 넘나드는 `rclone` Rust TUI&quot; : ratclone</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">SyscallBrain/ratclone — `Ratatui`와 `rclone` v1.68+를 결합해 터미널 SSH 환경에서도 클라우드 간 복사·탐색을 키보드로 제어</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">외우기 힘든 `rclone` 플래그와 원격 경로를 직관적인 듀얼 패널 파일 매니저로</h3>
            <div class="minor-detail-subheadline">MIT 라이선스 · Rust 1.88+ · `Ratatui` 기반 리눅스 네이티브 터미널 UI</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  헤드리스 리눅스 서버나 원격 SSH 세션에서 수십 개 오브젝트 스토리지와 클라우드 드라이브를 관리할 때 매번 `rclone lsd`, `rclone copy` 명령어를 치는 수고를 덜어주는 Vim 스타일 TUI가 등장했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[TUI 엔진]</strong> Vim Keybindings &rarr; Ratatui Dual-Pane State &rarr; `rclone` v1.68+ Backend &rarr; Cross-Remote Transfer
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  웹 GUI(`rclone rcd`)를 포트 포워딩으로 열지 않고도 가볍고 빠르게 원격 스토리지 간 데이터 이동을 검증할 수 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/SyscallBrain/ratclone" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: yetanotherbrowser/yab -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 230개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 10.08 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;기본은 초경량 WebKit, 필요할 땐 탭별로 Chromium 전환 + 프라이빗 탭과 격리된 AI 에이전트 탭&quot; : Yab</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">yetanotherbrowser/yab — macOS 15.4+ 네이티브 Swift 브라우저에 애플 실리콘용 듀얼 엔진과 iOS/Android 컴패니언을 결합</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">배터리 효율의 WebKit과 확장성의 Chromium을 한 창에 공존시킨 macOS 브라우저</h3>
            <div class="minor-detail-subheadline">엔진 내장형 광고 차단기 · `⇧⌘H` 요소 영구 숨김 · 개인 탭 접근이 차단된 전용 AI 에이전트 탭</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  무거운 크로미움 기반 AI 브라우저들이 배터리와 램을 집어삼키는 데 지친 맥 사용자들을 위해, 평상시엔 가벼운 WebKit을 쓰다가 크롬 확장·DevTools가 필요한 사이트만 Apple Silicon Chromium 엔진으로 돌리는 듀얼 아키텍처를 선보였습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[듀얼 엔진]</strong> Swift Native Shell &rarr; WebKit (Default) / Chromium (Per-Tab) + Isolated Agent Tabs (Zero Private Access)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  AI 에이전트가 브라우저를 조작할 때도 사용자가 열람 중인 사적 탭을 절대 보지 못하도록 탭 단위 권한 벽을 세운 점이 돋보입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/yetanotherbrowser/yab" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: cnrad/interspace -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 134개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 20.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.67 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;120Hz ProMotion 맥북에서 1초간 입력을 씹던 데스크톱 스페이스 전환 애니메이션을 즉각 반응으로 바꾼 앱&quot; : Interspace</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">cnrad/interspace — macOS 14+의 답답한 스페이스 슬라이드 잠금을 제거하고 손가락 추종·즉시 키 입력 전환을 구현한 Swift 유틸</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">주사율에 비례해 느려지던 애플 Mission Control 전환 지연의 구조적 결함 해결</h3>
            <div class="minor-detail-subheadline">Apple Silicon &amp; Intel 지원 · 무애니메이션 즉시 전환 및 전환 중 연속 단축키 입력 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  macOS의 데스크톱 전환 애니메이션은 120Hz 디스플레이에서 60Hz 대비 두 배 가까이 입력 대기 시간이 길어져 전환 직후 타이핑과 클릭이 무시되는 고질병이 있었습니다. `Interspace`는 사용자 맞춤 고속 전환으로 이 마찰을 없앴습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[입력 최적화]</strong> 3-Finger Swipe / Hotkey &rarr; Interspace Instant Transition &rarr; Zero Input Lock on Arrival
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  한 번의 스와이프로 여러 데스크톱을 연속 통과하거나 애니메이션 도중 즉시 다음 데스크톱으로 점프할 수 있어 다중 작업 속도가 비약적으로 빨라집니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/cnrad/interspace" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: bc160201983/GoW-Ascension-Recomp -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 129개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.9시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.63 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;에뮬레이터 없이 PS3 PowerPC PPU·SPU 코드를 C/C++로 정적 재컴파일한 Windows 네이티브 포트&quot; : GoW-Ascension-Recomp</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">bc160201983/GoW-Ascension-Recomp — 저작권 에셋 0% 클린룸 툴체인과 Direct3D 12 RSX 렌더러로 PS3 명작을 네이티브 PC 실행</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">악명 높은 PS3 셀(Cell) 프로세서 PPU/SPU 아키텍처를 정적 AOT 재컴파일로 정복</h3>
            <div class="minor-detail-subheadline">사용자 소유 정품 디스크 덤프 전용 · `ps3kit` 시스템 런타임 + Direct3D 12 그래픽스 변환</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  스위치(ARM64)와 N64를 넘어 가장 난해한 콘솔 중 하나로 꼽히던 PS3의 비대칭 멀티코어(PPU+SPU) 게임 바이너리까지 정적 재컴파일로 Windows 네이티브 C/C++ 코드로 번역하는 툴체인이 오픈소스로 공개되며 큰 화제를 모았습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[재컴파일]</strong> User PS3 Dump (PPU/SPU) &rarr; AOT C/C++ Translator &rarr; `ps3kit` Runtime + D3D12 RSX &rarr; Native Win64 Exe
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  저장소 내 저작권 코드·텍스처·오디오를 일절 포함하지 않는 클린룸 변환 도구 방식을 취해 콘솔 소프트웨어 보존 공학의 새 이정표를 세웠습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/bc160201983/GoW-Ascension-Recomp" target="_blank" rel="noopener noreferrer" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: House members stock trades test -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 92 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 30.69 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;미 하원의원 주식 거래 8,900건 전수 분석: 그들은 정말 시장을 이기는가?&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">arkanumdata.com — 의회 공시 거래 8,900건의 수익률을 통계 검증한 결과와 '중앙값 vs 극단적 내부자 알파·공시 지연' 논쟁</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">대중적 통념을 8,900건의 공시 데이터로 검증하고 통계적 함정까지 파고든 HN 토론</h3>
            <div class="minor-detail-subheadline">96개 댓글 폭발 · 중앙값(Median) 수익률 해석과 공시 날짜/시각 누락 한계 정밀 지적</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  정치인의 주식 거래가 항상 시장을 압도한다는 통념에 대해, 8,900건의 실제 하원의원 거래 데이터를 계량 분석한 리포트가 공개되며 Hacker News에서 치열한 통계 방법론 토론이 벌어졌습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[데이터 논점]</strong> 8,900 Disclosure Records &rarr; Median Return Test vs Tail Alpha Outliers &amp; Reporting Lag Bias
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  토론에서는 공시 제도가 정확한 체결 시각을 숨기는 한계와, 평균적 의원(Median)이 아닌 핵심 상임위 소수의 초과 수익(Tail Alpha)을 분리해 봐야 한다는 데이터 사이언스 통찰이 쏟아졌습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://arkanumdata.com/research/house-trades" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 리포트
              </a>
              <a href="https://news.ycombinator.com/item?id=50510005" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (92 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: Vulcan rocket fails during return-to-flight launch -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 60 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 2.1시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 28.03 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;ULA 벌컨(Vulcan) 로켓 비행 복귀 발사 중 추락 — 아마존 위성 40기 전량 손실&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">space.com — ULA 벌컨 센타우르 복귀 미션 실패로 아마존 Leo 저궤도 위성 40기가 소실되며 Blue Origin BE-4 엔진 신뢰성 도마 위</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">SpaceX 스타링크 대항마 구축에 제동이 걸린 ULA와 아마존 저궤도 위성망</h3>
            <div class="minor-detail-subheadline">부스터 1단 결함 추정 보도 · Blue Origin New Glenn 발사 일정 연쇄 타격 우려</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  ULA의 차세대 주력 로켓 벌컨 센타우르(Vulcan Centaur)가 비행 복귀 발사에서 실패해 아마존의 인터넷 위성 40기를 잃었습니다. 상단(Centaur)이나 고체 부스터가 아닌 1단 부스터 또는 BE-4 엔진 결함 가능성이 거론되며 우주 산업계가 술렁이고 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파급 연쇄]</strong> Vulcan Booster Anomaly &rarr; 40 Amazon Satellites Lost &rarr; BE-4 Engine Scrutiny &rarr; New Glenn / ULA Risk
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  Starship 15차 발사 성공 직후 터진 경쟁사 발사 실패로, 궤도 발사 시장의 SpaceX 1강 독주 체제가 더욱 굳어질 위기에 처했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.space.com/space-exploration/launches-spacecraft/ula-vulcan-centaur-return-to-flight-amazon-leo-internet-satellite-launch" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 보도 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50510442" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (60 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: Things That Turbo Pascal Is Smaller Than -->
        <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 175 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.0시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 19.39 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;오늘날 웹페이지 배너 이미지 하나보다 작은 컴파일러+IDE: Turbo Pascal이 더 작은 것들&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">prog21.dadgum.com — 360KB 플로피 디스크 시절 통합개발환경의 경이로움을 통해 현대 소프트웨어 비대화를 반성하는 고전 에세이 재점화</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">수백 MB의 `node_modules`와 Electron 시대에 다시 읽는 39KB 컴파일러의 미학</h3>
            <div class="minor-detail-subheadline">88개 댓글 공감 · Claude Code용 Turbo Vision UI(`tvclaude`) 등 레트로 경량화 영감 확산</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  완전한 에디터와 초고속 원패스 컴파일러를 합쳐도 고작 수십 KB였던 Turbo Pascal을 현대의 거대한 PNG 아이콘·웹 번들과 비교한 글이 HN에서 다시 175표를 받으며, AI 시대의 소프트웨어 효율성과 단순성에 대한 성찰을 불러일으켰습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[대조]</strong> 360KB Floppy Era (Full IDE + Compiler in KB) vs Modern Multi-GB Electron / Node Bloat
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  댓글에서는 AI 코딩 에이전트 덕분에 바닥 원리(First Principles)부터 간결하고 극도로 빠른 OS·TUI(예: Turbo Vision 스타일 Claude Code UI `tvclaude`)를 새로 짤 기회가 왔다는 논의가 이어졌습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://prog21.dadgum.com/116.html" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 에세이
              </a>
              <a href="https://news.ycombinator.com/item?id=50506894" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (175 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: Lutnick Pushed to Weaken Chip Rules -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 439 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 11.1시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 39.60 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;미 상무장관 러트닉, 가족 기업과 겹치는 AI 칩 수출 규제 완화를 직접 압박했다는 NYT 폭로&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">nytimes.com — 말레이시아 데이터센터 투자 및 캔터 피츠제럴드 이해충돌이 반도체 수출 통제 정책에 개입했다는 의혹으로 439표 폭주</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">국가안보 명분의 GPU 수출 규제가 정경유착 이해충돌에 흔들린다는 지정학적 스캔들</h3>
            <div class="minor-detail-subheadline">189개 댓글 격론 · AI 컴퓨팅 인프라 공급망과 칩 규제 정책 투명성 논쟁</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  미국의 AI 반도체 수출 통제 규칙이 동남아 데이터센터 투자 이해관계와 맞물려 완화 압력을 받았다는 뉴욕타임스 보도가 나오자, 엔지니어·스타트업 커뮤니티에서 글로벌 GPU 할당 정책의 공정성에 대한 거센 비판이 일었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[정책 쟁점]</strong> Export Control Rule &rarr; Family/Firm Datacenter Overlap &rarr; Regulatory Weakening Pressure &rarr; Governance Crisis
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  AI 칩 수급과 클라우드 리전 확장이 기술 경쟁을 넘어 정치적 로비에 좌우되는 현실을 적나라하게 드러냈습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.nytimes.com/2026/11/15/us/politics/lutnick-pushed-to-weaken-chip-rules-that-overlap-with-his-family-business.html" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> NYT 보도 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50506180" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (439 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: Understanding Positional Embeddings in Modern LLMs -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 184 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.47 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;현대 LLM의 위치 임베딩 완전 정복 — RoPE에서 최신 장문 컨텍스트 변형까지&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">magazine.sebastianraschka.com — 세바스찬 라슈카의 코드·직관 중심 LLM Positional Embedding 아키텍처 심층 해설</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">어텐션이 토큰 순서를 인식하는 수학적·구현적 메커니즘의 명쾌한 해부</h3>
            <div class="minor-detail-subheadline">구현 코드부터 군 표현론(Group Representation) 기하학 토론까지 이어진 ML 기술 노트</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  백만 토큰급 컨텍스트 창이 일상이 되면서, 트랜스포머의 절대 위치 임베딩이 어떻게 회전 위치 임베딩(RoPE)과 장문 확장 기법으로 진화했는지 밑바닥 코드 레벨에서 정리한 라슈카의 신작 아티클이 높은 호응을 얻었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[진화 축]</strong> Sinusoidal / Learned Absolute &rarr; Relative Bias &rarr; Rotary (RoPE) &rarr; Long-Context Scaling
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  추론 엔진(llama.cpp/vLLM)에서 KV 캐시 메모리와 컨텍스트 외삽 성능을 튜닝하는 엔지니어들에게 핵심 기초 지침을 제공합니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://magazine.sebastianraschka.com/p/understanding-positional-embeddings" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 기술 아티클
              </a>
              <a href="https://news.ycombinator.com/item?id=50506376" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (184 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: Why did some Apollo missions carry a grenade launcher? -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 211 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 13.7시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 15.45 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;아폴로 달 탐사선은 왜 유탄 발사기(Mortar)를 싣고 갔을까? — 달 지진파 능동 탐사 공학&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">space.stackexchange.com — 달 표면 아래 지질 구조를 파악하기 위해 아폴로 14·16호에 실렸던 능동 지진 실험(ASE) 발사체 비화</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">달에서 폭약을 원격 발사해 지진파 반사 신호를 측정하려던 1970년대 NASA 하드웨어</h3>
            <div class="minor-detail-subheadline">141개 댓글 화제 · Active Seismic Experiment(ASE)와 진공·저중력 탄도학 설계</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  우주비행사가 무기가 아닌 과학 장비로 '유탄 발사기'를 들고 갔다는 흥미로운 제목 이면에는, 사람이 접근하기 위험한 거리까지 폭발물을 쏘아 보내 달 지각의 지진파 속도를 계측하려던 정교한 아폴로 공학이 숨어 있었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[탐사 원리]</strong> Lunar Mortar Launch &rarr; Controlled Impact &rarr; Geophone Array &rarr; Subsurface Crust Profiling
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  극한 환경에서의 물리 계측 자동화와 아폴로 시대 NASA 엔지니어들의 거침없는 실험 정신을 다시금 환기시켰습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://space.stackexchange.com/questions/37775" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> StackExchange 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50505271" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (211 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: Court denies motion to dismiss DRAM price fixing case -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 481 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 21.5시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 22.42 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;미 연방법원, 삼성·SK하이닉스·마이크론 DRAM 가격 담합 소송 기각 신청 기각 — 본안 심리 진입&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">litnews.ai — 로컬 LLM 워크스테이션 램 가격이 천정부지로 치솟는 와중에 메모리 3사 반독점 집단소송 생존으로 481표 돌파</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">대용량 RAM 비용 폭등에 시달리는 AI 개발자·연구자들의 분노가 폭발한 반독점 뉴스</h3>
            <div class="minor-detail-subheadline">211개 댓글 격론 · 256GB RAM 워크스테이션 구축비 4,000~5,000달러 급등 체감 토로</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 서버용 HBM 수요와 공급 조절 속에 일반 PC·서버용 DRAM 가격마저 급등하자, 메모리 3사(삼성·SK하이닉스·마이크론)를 상대로 한 가격 담합 소송이 법원의 기각 문턱을 넘었다는 소식에 개발자들의 이목이 집중됐습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[소송 경과]</strong> Garciaguirre Class Action &rarr; Motion to Dismiss Denied &rarr; Discovery Phase (Supply &amp; Pricing Scrutiny)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  로컬 LLM과 온프레미스 서버를 직접 조립하려는 연구자·스타트업에게 메모리 독과점 구조가 곧 컴퓨팅 민주화의 병목임을 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://litnews.ai/articles/garciaguirre-samsung-sk-hynix-micron-dram-conspiracy-suit-survives-dismissal" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 판결 리포트
              </a>
              <a href="https://news.ycombinator.com/item?id=50502988" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (481 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: EFF Appeals Court ALPR Warrant -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 332 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 20.8시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 16.00 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;자동 번호판 인식(ALPR) 망 무영장 추적은 위헌 — EFF 항소법원에 영장 의무화 의견서 제출&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">eff.org — 미국 전역에 깔린 Flock 등 AI 번호판 카메라 네트워크의 상시 동선 추적에 수정헌법 제4조 적용 요구</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">컴퓨터 비전과 클라우드 DB가 만든 '영장 없는 전국민 이동 기록부'에 제동</h3>
            <div class="minor-detail-subheadline">109개 댓글 지지 · 뉴햄프셔 주법(비적중 번호판 3분 내 삭제 의무) 대안 모델 주목</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  민간 업체가 도로 곳곳에 설치한 AI 번호판 인식기(ALPR) 네트워크가 시민 전체의 이동 경로를 영구 저장하고 경찰이 영장 없이 조회하는 관행에 대해, 전자프런티어재단(EFF)이 항소법원에 정면으로 위헌 판단을 촉구했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[헌법 쟁점]</strong> Interconnected ALPR Grid &rarr; Persistent Driver Tracking &rarr; Fourth Amendment &quot;Search&quot; &rarr; Warrant Mandate
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  엣지 AI 카메라와 중앙 클라우드 감시망을 구축할 때 '데이터 최소 보존(3분 내 폐기)'과 영장 기반 접근 제어가 필수 법적 기준으로 부상하고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.eff.org/deeplinks/2026/11/were-asking-appeals-court-require-warrant-alpr-searches" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> EFF 성명 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50503255" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (332 pts)
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: How did Woz write the Apple 1 BASIC before building the computer? -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 308 pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 24.4시간 전 등록</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 12.63 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;워즈니악은 어떻게 컴퓨터를 만들기도 전에 Apple 1 BASIC을 종이 위에 손으로 짰을까?&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">retrocomputing.stackexchange.com — 어셈블러도 하드웨어도 없던 시절, 6502 기계어 바이트를 손으로 직접 계산해 짠 전설의 제작기</span>
              </div>
            </div>
            <div class="minor-summary-right">
              <div class="minor-toggle-btn" role="button" aria-expanded="false">
                <span class="minor-btn-text">메모 펼치기</span>
                <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
              </div>
            </div>
          </div>
          <div class="minor-detail-content" onclick="event.stopPropagation()">
            <h3 class="minor-detail-headline">컴파일러·디버거·시뮬레이터 없이 오직 뇌와 종이만으로 완결한 8비트 인터프리터</h3>
            <div class="minor-detail-subheadline">161개 댓글 감탄 · 6502 핸드 어셈블링(Hand Assembly)과 분기 오프셋 암산 기법 회고</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  AI 코딩 에이전트가 몇 초 만에 수천 줄을 생성하고 테스트해 주는 시대에 역설적으로, 스티브 워즈니악이 6502 CPU 명령어 표만 보고 종이에 어셈블리와 16진수 옵코드를 손으로 직접 번역해 Apple 1 BASIC을 완성했던 일화가 엔지니어들의 경외감을 자아냈습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[핸드 어셈블링]</strong> Paper Logic &rarr; 6502 Opcode Manual Translation &rarr; Hex Branch Offset Calc &rarr; Direct RAM Entry
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  두 번째 개발 머신을 살 돈이 없던 초기 컴퓨터 개척자들이 어떻게 머릿속에 CPU 상태 기계를 완벽히 에뮬레이션하며 코드를 검증했는지 생생하게 보여줍니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://retrocomputing.stackexchange.com/questions/17957" target="_blank" rel="noopener noreferrer" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> Q&amp;A 원문
              </a>
              <a href="https://news.ycombinator.com/item?id=50501594" target="_blank" rel="noopener noreferrer" class="minor-link hn-discuss">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론 (308 pts)
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
