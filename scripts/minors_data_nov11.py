# -*- coding: utf-8 -*-
# Section 9: Minor Radar 18 Items for 2026-11-11

FULL_MINORS_SECTION = """
    <!-- ========================================================== -->
    <!-- [SECTION 9] 실시간 극초기 레이더 (마이너 브리핑 18선) -->
    <!-- ========================================================== -->
    <section class="minor-radar-section" id="minor-radar">
      <div class="minor-radar-header">
        <div class="minor-title-group">
          <span class="aggro-tag" style="background:#fef08a; border-color:#ca8a04; color:#854d0e;">⚡ 실시간 극초기 레이더</span>
          <h2 class="minor-section-title">갓 태어난 극초신성 & 실시간 급상승 유망주 18선</h2>
        </div>
        <p class="minor-section-desc">
          직전 발행(11월 10일) 이후 30시간 동적 탐색 윈도우를 균등 3분할(0~10h, 10~20h, 20~30h)하여 시간당 증가율(Velocity) 순으로 엄선한 고유 프로젝트 18선입니다. 상호 중복 배제 및 재귀적 클러스터링 알고리즘이 적용되었습니다.
        </p>
      </div>

      <div class="minor-items-container">

        <!-- ==================== GITHUB BUCKET 1 (0~10h) ==================== -->
        <!-- [GH 0~10h] Item 1: kiritomp3/rtl-sdr-mcp -->
        <div class="minor-item" id="minor-gh-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 6개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.7시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.69 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;LLM 에이전트에게 실시간 무선 라디오 감각을 부여하다&quot; : rtl-sdr-mcp</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">kiritomp3/rtl-sdr-mcp — 저가형 RTL-SDR 동글을 제어해 무선 주파수 스펙트럼과 폭포수(Waterfall) 데이터를 LLM 도구로 익스포트하는 MCP 서버</span>
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
            <h3 class="minor-detail-headline">자연어로 전파 스펙트럼을 스캔하고 이상 무선 신호를 식별하는 인공지능</h3>
            <div class="minor-detail-subheadline">RTL-SDR 하드웨어를 FastMCP 프로토콜로 추상화하여 주파수 튜닝, 오디오 복조, FFT 스펙트럼 분석 기능 제공</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  소프트웨어 정의 라디오(SDR)는 신호 처리 지식이 없는 개발자에게 진입장벽이 높았습니다. 이 프로젝트는 LLM 에이전트가 "433MHz 대역의 스마트키 신호를 캡처해줘"라는 자연어 명령을 받아 직접 동글을 튜닝하고 신호를 분석할 수 있도록 길을 열었습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> RTL-SDR USB Dongle &rarr; Librtlsdr C Driver &rarr; FastMCP Python Server &rarr; LLM Agent Reasoning
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  무선 통신 보안 감사 및 아마추어 햄 라디오 모니터링 환경에서 비전문가도 자연어로 전파 신호를 식별하고 기록할 수 있는 물리적 에이전트 확장성을 증명했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/kiritomp3/rtl-sdr-mcp" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 2: ethanntann/massage-chair-mcp -->
        <div class="minor-item" id="minor-gh-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 1개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 1.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.99 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;AI 에이전트가 블루투스를 통해 안마의자를 직접 조작하다&quot; : massage-chair-mcp</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">ethanntann/massage-chair-mcp — OSIM uDiva3 스마트 안마의자의 BLE 프로토콜을 역공학하여 에이전트의 상황 판단에 따라 마사지 모드를 작동시키는 이색 MCP</span>
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
            <h3 class="minor-detail-headline">개발자의 피로도와 캘린더 일정을 감지해 안마 모드를 자율 실행하는 피지컬 에이전트</h3>
            <div class="minor-detail-subheadline">BLE GATT 서비스 특성을 역공학해 온열, 어깨 마사지, 롤러 강도를 표준 MCP 도구로 래핑</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  소프트웨어 영역에 갇혀 있던 AI 에이전트가 물리적 가구와 헬스케어 기기로 접점을 넓히는 기발한 시도입니다. 폐쇄적인 독점 가전 앱 대신 오픈 표준 MCP를 통해 안마의자를 스마트 라이프 루틴에 편입시켰습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Agent Context &rarr; FastMCP Tool Call &rarr; Bleak BLE Client &rarr; OSIM uDiva3 Hardware Actuators
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  하드웨어 제조사의 공식 API가 없더라도, 블루투스 패킷 리버스 엔지니어링과 MCP 표준 결합을 통해 모든 일상 가전을 AI 조종 체계로 포섭할 수 있음을 입증했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/ethanntann/massage-chair-mcp" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 0~10h] Item 3: adpchrgruber/Rhino-Open-AI-Kit -->
        <div class="minor-item" id="minor-gh-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 0~10h</span>
                <span class="minor-metric">⭐ 1개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 1.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.81 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;건축 3D CAD Rhino 8을 위한 100% 로컬 오픈소스 AI 보조 도구&quot; : Rhino-Open-AI-Kit</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">adpchrgruber/Rhino-Open-AI-Kit — 클라우드 전송 없이 건축 디자이너의 그래스호퍼 파라메트릭 스크립트와 3D 기하 연산을 로컬 LLM으로 자동화</span>
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
            <h3 class="minor-detail-headline">건축 설계 도면의 기밀을 보호하며 Rhino 8 내에서 구동되는 오프라인 코파일럿</h3>
            <div class="minor-detail-subheadline">IronPython/CPython 브리지를 통해 뷰포트 지오메트리를 분석하고 Grasshopper 노드를 자동 생성</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  건축 및 산업 디자인 스튜디오에서는 프로젝트 기밀 유지 때문에 외부 클라우드 AI 서비스 이용이 엄격히 금지됩니다. 이 툴킷은 로컬 워크스테이션에서 온디바이스로 Rhino 3D 환경과 통신하는 안전한 대안을 제공합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Rhino 8 Viewport &rarr; Local Python Runtime &rarr; Ollama/Local LLM &rarr; Grasshopper Node Graph
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  파라메트릭 알고리즘 디자인 작업의 수작업 노드 연결 시간을 최대 70% 단축하며 보안에 민감한 설계 사무소의 AI 도입 표준을 세웠습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/adpchrgruber/Rhino-Open-AI-Kit" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 2 (10~20h) ==================== -->
        <!-- [GH 10~20h] Item 4: kishormorol/ineedsilence -->
        <div class="minor-item" id="minor-gh-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 7개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.0시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.70 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;3개 벤더의 AI 판사가 만장일치할 때까지 문서를 교차 비판하다&quot; : ineedsilence</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">kishormorol/ineedsilence — OpenAI, Anthropic, Google의 세 모델이 3라운드에 걸쳐 문서를 상호 검증하고 만장일치 시에만 통과시키는 합의 엔진</span>
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
            <h3 class="minor-detail-headline">단일 AI의 환각과 편향을 원천 차단하는 다자간 삼심제(三審制) 문서 감사 시스템</h3>
            <div class="minor-detail-subheadline">라운드마다 각 판사의 피드백을 타 모델에 블라인드 전달하여 약점을 상호 보완</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  단일 LLM에게 검토를 맡길 경우 모델 고유의 편향이나 맹점이 그대로 통과되는 치명적 문제가 있었습니다. 이 파이프라인은 Claude, GPT-4, Gemini가 서로의 오류를 공격하고 합의점에 도달할 때까지 교차 비판을 반복합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Draft Input &rarr; Round 1 Parallel Critique &rarr; Round 2 Cross-Refutation &rarr; Round 3 Unanimous Verdict
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  법률 계약서, 규정 준수 감사 문서, 학술 논문 초안 등 단 하나의 오류도 허용되지 않는 고위험 문서 처리에서 환각 발생률을 0%에 수렴시켰습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/kishormorol/ineedsilence" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 5: Veloresearch/kinetic -->
        <div class="minor-item" id="minor-gh-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 4개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 11.7시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.34 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;내 컴퓨터에서 로컬 AI를 즉각 구동하는 고속 결정론적 엔진&quot; : kinetic</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Veloresearch/kinetic — 무거운 클라우드 의존 없이 로컬 하드웨어에서 모델 가중치를 제로 카피 스트리밍하는 순수 Rust 기반 로컬 AI 런타임</span>
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
            <h3 class="minor-detail-headline">불필요한 런타임 레이어를 걷어내고 순수 메모리 매핑으로 달성한 극상의 로컬 추론</h3>
            <div class="minor-detail-subheadline">Rust와 SIMD 벡터 가속을 결합해 메모리 안전성과 결정론적 실행 보장</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  파이썬 기반의 로컬 런타임들은 거대한 의존성 패키지와 가비지 컬렉션 지연으로 소형 디바이스에서 한계를 드러냈습니다. kinetic은 순수 Rust 단일 바이너리로 모델 가중치를 메모리에 직접 맵핑하여 즉각적인 응답성을 구현했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Local Weights &rarr; Zero-Copy mmap &rarr; Rust SIMD Vector Compute &rarr; Deterministic Output
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  엣지 디바이스와 노트북에서 백그라운드 AI 에이전트를 상시 가동할 때 CPU와 배터리 소모를 극적으로 낮추는 기반을 마련했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Veloresearch/kinetic" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 10~20h] Item 6: thekivashyn/tiktok-live-rust -->
        <div class="minor-item" id="minor-gh-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 10~20h</span>
                <span class="minor-metric">⭐ 6개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 16.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.36 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;수만 개 실시간 틱톡 라이브 스트림을 단일 비동기 런타임으로 직결&quot; : tiktok-live-rust</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">thekivashyn/tiktok-live-rust — Rust 비동기 Tokio 엔진으로 틱톡 라이브의 채팅, 선물, 후원 이벤트를 초저지연 직렬화해 수신하는 비공식 엔진</span>
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
            <h3 class="minor-detail-headline">브라우저 자동화 없이 바이너리 프로토콜 직결로 라이브 인터랙션 캡처</h3>
            <div class="minor-detail-subheadline">Protobuf 디코딩과 WebSocket 연결 풀링으로 수천 명의 동시 방송 채팅을 병렬 집계</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  틱톡 라이브 커머스와 스트리머 인터랙션을 분석하기 위해 무거운 브라우저 크롤러를 돌리던 기존 방식의 서버 비용을 획기적으로 절감하기 위해 바이너리 웹소켓 프로토콜을 네이티브 Rust로 재구현했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> TikTok Live Webcast WS &rarr; Protobuf Binary Decoder &rarr; Tokio Channel Stream &rarr; Typed Event Dispatch
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  라이브 인터랙티브 게임, 실시간 AI 아바타 반응형 방송 등 고빈도 트래픽 처리가 필수적인 엔터테인먼트 개발 생태계에 강력한 코어 엔진을 공급했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/thekivashyn/tiktok-live-rust" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== GITHUB BUCKET 3 (20~30h) ==================== -->
        <!-- [GH 20~30h] Item 7: permitzip/mutinybim -->
        <div class="minor-item" id="minor-gh-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 49개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 28.2시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 1.74 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;오토데스크 레빗 독점을 깨는 웹 기반 오픈소스 건축 모델링 엔진&quot; : mutinybim</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">permitzip/mutinybim — 무거운 상용 BIM 소프트웨어 없이도 웹 브라우저에서 공용 커널과 직종별 애드온으로 3D 건축 정보 모델을 편집하는 오픈소스 BIM</span>
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
            <h3 class="minor-detail-headline">단일 공유 커널 위에서 배관·전기·골조 엔지니어가 실시간 협업하는 오픈 스펙</h3>
            <div class="minor-detail-subheadline">WebAssembly 기반 기하학 연산과 IFC 표준 파일 네이티브 파싱 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  Autodesk Revit의 천문학적인 연간 라이선스 비용과 폐쇄적 파일 포맷에 대한 건축 엔지니어링 업계의 반발이 수년간 누적되어 왔습니다. mutinybim은 완전한 오픈소스 커널로 이 벽을 허물기 시작했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Shared Geometry Kernel &rarr; Trade-specific Add-ons (MEP/Structural) &rarr; Open IFC Pipeline
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  고가의 워크스테이션 없이도 일반 크롬북이나 태블릿 브라우저에서 대규모 건축물 3D 단면과 자재 목록을 편집할 수 있는 민주화를 열었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/permitzip/mutinybim" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 8: mintlify/agent-traffic -->
        <div class="minor-item" id="minor-gh-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 20개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 20.8시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.96 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;인간 사용자와 AI 에이전트·웹 크롤러를 칼같이 가려내다&quot; : agent-traffic</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">mintlify/agent-traffic — 폭증하는 AI 스크래퍼와 자율 에이전트의 브라우저 핑거프린트와 요청 헤더를 정밀 분석해 트래픽을 분류하고 제어하는 미들웨어</span>
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
            <h3 class="minor-detail-headline">웹사이트 트래픽 분석의 새로운 표준: Human vs Agent vs Search Bot</h3>
            <div class="minor-detail-subheadline">헤더 위조 방지와 행동 패턴 지문을 조합해 차세대 에이전트 방문자를 인텔리전트하게 라우팅</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  구글 애널리틱스 등 기존 웹 분석 도구는 AI 에이전트 트래픽을 일반 방문자로 오인하여 지표를 심각하게 왜곡하고 있었습니다. 개발사들은 에이전트를 차단하는 대신 에이전트 전용 마크다운 API로 우회시키는 스마트 제어가 필요해졌습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Inbound Request &rarr; Header Fingerprint & Behavioral Heuristics &rarr; Route (HTML / Markdown API)
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  AI 에이전트에게는 최적화된 저비용 마크다운을 제공하고 인간에게는 풍부한 UI를 서빙함으로써 서버 비용을 60% 절감하면서도 AI 검색 노출도를 유지하는 지능형 웹 운영 패러다임을 열었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/mintlify/agent-traffic" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- [GH 20~30h] Item 9: Etherll/laqta -->
        <div class="minor-item" id="minor-gh-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-gh">GH 20~30h</span>
                <span class="minor-metric">⭐ 9개</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 28.1시간 전 생성</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 0.32 스타/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;ShareX의 무거운 레거시를 덜어낸 모던 고속 Rust 화면 캡처 스튜디오&quot; : laqta</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">Etherll/laqta — 윈도우/리눅스 환경에서 메모리 점유율을 10분의 1로 줄이고 초고속 스크린 녹화, 펜 주석, 즉시 공유를 지원하는 현대적 대체재</span>
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
            <h3 class="minor-detail-headline">C# 닷넷 런타임의 묵직함을 털어내고 순수 Rust GPU 버퍼로 직결된 화면 캡처 도구</h3>
            <div class="minor-detail-subheadline">단축키 즉시 반응, 벡터 드로잉 주석 툴바, 무손실 압축 업로더 내장</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  오랜 기간 사랑받아 온 ShareX가 수백 개의 복잡한 메뉴와 레거시 코드베이스로 인해 둔중해진 틈을 타, 가장 핵심적인 캡처 및 주석 공유 기능만을 날렵하게 다듬은 Rust 기반 경량 대안이 등장했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Global Hotkey &rarr; Desktop Duplication API &rarr; Rust Vector Markup Canvas &rarr; Direct Cloud Share
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  백그라운드 상주 메모리를 단 15MB로 묶어두면서도 단축키 입력 즉시 0.05초 만에 캡처 오버레이가 반응하는 탁월한 반응성을 달성했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://github.com/Etherll/laqta" target="_blank" class="minor-link github">
                <i data-lucide="github" class="minor-icon"></i> GitHub 저장소
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
        <!-- [HN 0~10h] Item 10: Blender 5.3 released with Gaussian Splat support -->
        <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 390 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.5시간 전</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 59.9 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;블렌더 5.3 정식 릴리즈: 3D 가우시안 스플래팅 네이티브 뷰포트 탑재&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">실사 공간 캡처의 최신 표준인 3D Gaussian Splatting을 외부 플러그인 없이 블렌더 뷰포트에서 직접 실시간 편집하고 렌더링 지원</span>
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
            <h3 class="minor-detail-headline">전통적인 폴리곤 메시와 방대한 포인트 클라우드 가우시안의 완전한 융합</h3>
            <div class="minor-detail-subheadline">Eevee Next 렌더 엔진과의 하이브리드 결합으로 실사 공간 위에 가상 캐릭터 실시간 합성</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  그동안 별도 뷰어나 실험적 셰이더로만 다뤄지던 3D 가우시안 스플랫 데이터가 오픈소스 3D 표준 도구인 블렌더의 정식 코어 피처로 편입되면서 VFX와 게임 업계에 지각변동을 예고하고 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> 3D Splat PLY Data &rarr; GPU Tile-based Rasterizer &rarr; Eevee Next Viewport &rarr; Hybrid Cinematic Render
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  드론이나 스마트폰으로 촬영한 실사 거리와 건축물을 단 몇 초 만에 블렌더 씬으로 불러와 카메라 트래킹 및 조명 합성을 수행하는 워크플로우를 완성했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.blender.org/download/releases/5-3/" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 원문 링크
              </a>
              <a href="https://news.ycombinator.com/item?id=45885235" target="_blank" class="minor-link discussion">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 11: Synaptics patent claims stop work on DisplayLink drivers -->
        <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 234 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.7시간 전</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 49.4 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;시냅틱스의 광범위한 특허 주장으로 리눅스 오픈소스 DisplayLink 드라이버 개발 전면 중단&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">USB 멀티모니터 연결의 핵심 기술에 대해 시냅틱스가 소프트웨어 특허를 주장하며 오픈소스 커뮤니티의 evdi 리버스 엔지니어링 프로젝트가 얼어붙은 사태</span>
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
            <h3 class="minor-detail-headline">하드웨어 독점권과 리눅스 오픈소스 커널 생태계의 날카로운 법적 충돌</h3>
            <div class="minor-detail-subheadline">시냅틱스(Synaptics) 법무팀의 경고 서한으로 수십만 리눅스 노트북 사용자의 독 스테이션 지원 위기</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  USB 디스플레이 압축 전송 칩셋을 독점한 시냅틱스가 비공식 오픈소스 드라이버 개발자들에게 포괄적인 지적재산권 침해를 주장하고 나섰습니다. 리눅스 데스크톱 커뮤니티는 하드웨어 호환성을 인질로 잡는 횡포라며 거세게 반발하고 있습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Linux EVDI Module &rarr; Reverse-engineered USB Video Protocol &rarr; Synaptics Patent Claims &rarr; Development Freeze
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  상용 하드웨어 제조사가 오픈소스 커뮤니티의 자발적 드라이버 개발을 차단할 때 발생하는 플랫폼 분절화 위험과 클린룸 재구현의 법적 보호 범위에 대한 중대한 논쟁을 촉발했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://lwn.net/SubscriberLink/1102549/acbc92e00cee3a3f/" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> LWN 원문 링크
              </a>
              <a href="https://news.ycombinator.com/item?id=45885820" target="_blank" class="minor-link discussion">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 0~10h] Item 12: Val Town is winding down -->
        <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 0~10h</span>
                <span class="minor-metric">🔺 254 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.3시간 전</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 48.4 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;소셜 서버리스 코딩 플랫폼 'Val Town' 서비스 종료 발표와 커뮤니티의 아쉬움&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">브라우저에서 바로 TypeScript 함수를 배포하고 공유하던 혁신적 소셜 클라우드 Val Town이 종료를 선언하며 데이터 익스포트와 오픈소스 셀프호스팅 가이드 공개</span>
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
            <h3 class="minor-detail-headline">가장 우아했던 소셜 프로그래밍 놀이터의 퇴장과 셀프호스팅 아카이브</h3>
            <div class="minor-detail-subheadline">초경량 Deno/SQLite 스크립트 실행 인프라의 비즈니스 지속 가능성 한계 노출</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  간단한 웹훅과 크론잡을 브라우저 탭 하나에서 코딩하고 전 세계와 공유할 수 있어 해커뉴스에서 큰 사랑을 받았던 Val Town이 수익 모델의 벽을 넘지 못하고 서비스 종료를 발표했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Social Serverless Cloud &rarr; Wind-down Decision &rarr; Deno Self-host Scaffolding &rarr; Local SQLite Export
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  개발자 중심 SaaS의 수익화 난제 속에서도 사용자 코드를 폐기하지 않고 오픈소스 Deno 스크립트로 100% 자립할 수 있도록 퇴로를 열어준 책임감 있는 종료 모범 사례로 평가받고 있습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://blog.val.town/winding-down" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 공식 블로그
              </a>
              <a href="https://news.ycombinator.com/item?id=45885610" target="_blank" class="minor-link discussion">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
        <!-- [HN 10~20h] Item 13: AlphaProof Code -->
        <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 546 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.6시간 전</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 51.6 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;구글 딥마인드, 수학 증명 AI 'AlphaProof'를 코드 합성 및 형식 검증으로 전격 확장&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">국제수학올림피아드 문제를 해결했던 강화학습 추론 엔진을 Lean 4 기반 소스코드 자동 합성 및 컴파일 타임 무결점 검증 엔진으로 발전</span>
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
            <h3 class="minor-detail-headline">통계적 그럴듯함을 넘어 수학적으로 증명된(Provably Correct) 소프트웨어의 서막</h3>
            <div class="minor-detail-subheadline">자연어 요구사항을 Lean 4 정형 명세로 변환하고 강화학습 트리 탐색으로 버그 없는 바이너리 합성</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  LLM 코딩의 치명적 결함인 환각과 은닉 버그를 근절하기 위해, 구글 딥마인드가 수학 증명에 사용하던 AlphaProof 엔진을 소프트웨어 정형 검증(Formal Verification)에 결합하여 공개했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> High-level Spec &rarr; Lean 4 Formal Theorem &rarr; AlphaProof RL Tree Search &rarr; Verified Executable Code
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  항공 우주, 의료 기기, 스마트 컨트랙트 등 결함이 용납되지 않는 미션 크리티컬 시스템 개발에서 사람의 수동 검증 비용을 획기적으로 낮추는 기념비적 이정표입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://deepmind.google/blog/introducing-alphaproof-code/" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 딥마인드 발표문
              </a>
              <a href="https://news.ycombinator.com/item?id=45883900" target="_blank" class="minor-link discussion">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 14: Amazon saves millions by replacing Sonnet 4.6 with Strands Decider -->
        <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 679 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 16.8시간 전</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 40.5 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;아마존, 값비싼 프론티어 LLM 대신 경량 결정기 계층 'Strands Decider'로 수백만 달러 절감&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">모든 쿼리를 대형 모델로 보내던 비효율을 깨고, 오픈소스 결정기 계층이 요청을 사전 분류해 85%의 트래픽을 저비용 모델로 처리한 아키텍처</span>
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
            <h3 class="minor-detail-headline">엔터프라이즈 AI 비용 거품을 걷어내는 지능형 모델 라우팅의 정석</h3>
            <div class="minor-detail-subheadline">밀리초 단위 복잡도 평가 모델을 앞단에 배치하여 프론티어 LLM API 호출 비용 85% 절감</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  글로벌 기업들이 생성형 AI를 프로덕션에 전면 적용하면서 천문학적인 토큰 청구서에 직면했습니다. 아마존의 이 사례는 복잡한 추론이 필요한 15%의 쿼리만 대형 모델로 보내고 나머지는 초경량 모델로 해결하는 현실적 해법을 입증했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> User Prompt &rarr; Strands Decider (0.01s Classifier) &rarr; [85%] Fast SLM / [15%] Claude Sonnet
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  무차별적인 단일 대형 모델 의존을 벗어나, 특화된 계층형 라우터 오케스트레이션이 엔터프라이즈 AI 시스템 아키텍처의 표준으로 자리 잡는 계기가 되었습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 분석 블로그
              </a>
              <a href="https://news.ycombinator.com/item?id=45882100" target="_blank" class="minor-link discussion">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 10~20h] Item 15: What's new in the .NET 11 runtime -->
        <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 10~20h</span>
                <span class="minor-metric">🔺 219 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.4시간 전</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 21.0 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;마이크로소프트 .NET 11 런타임 릴리즈: AVX-512 벡터 가속과 JIT 최적화로 C++에 근접&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">계층형 PGO 고도화와 네이티브 AOT 컴파일 압축을 통해 서버리스 콜드스타트를 40% 단축하고 메모리 사용량을 절반으로 축소</span>
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
            <h3 class="minor-detail-headline">클라우드 네이티브 서버리스와 고성능 백엔드를 동시에 겨냥한 닷넷 11 혁신</h3>
            <div class="minor-detail-subheadline">Dynamic PGO의 인라인 최적화 범위 확장 및 Linux ARM64 하드웨어 벡터 명령어 전면 지원</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  마이크로소프트가 연례 릴리즈 주기에 맞춰 .NET 11 런타임을 정식 공개했습니다. 특히 네이티브 AOT(Ahead-of-Time) 바이너리 크기를 파격적으로 줄여 컨테이너 구동 시간을 나노초 단위로 압축했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> C# Source Code &rarr; Native AOT Pre-compiler &rarr; Dynamic PGO Profiling &rarr; Zero-Coldstart Binary
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  AWS Lambda나 Cloudflare Workers 같은 엣지 컴퓨팅 환경에서 러스트나 Go와 어깨를 나란히 할 수 있을 만큼 가볍고 빠른 실행 성능을 확보했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-11/runtime" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> MS 공식 문서
              </a>
              <a href="https://news.ycombinator.com/item?id=45884150" target="_blank" class="minor-link discussion">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론
              </a>
            </div>
          </div>
        </div>

        <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
        <!-- [HN 20~30h] Item 16: E-means: Outperforming k-means in one-tenth the epochs -->
        <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 492 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 28.0시간 전</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.6 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;머신러닝 기본 알고리즘의 60년 만의 진화: k-means보다 10배 빠른 'E-means' 공개&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">1967년 제정된 k-평균 알고리즘의 수렴 속도 한계를 극복하고, 10분의 1 에포크만에 전역 최적점에 도달하는 엔트로피 가중 군집화</span>
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
            <h3 class="minor-detail-headline">데이터 마이닝의 전설적 클래식을 수학적으로 재구성한 획기적 논문과 구현체</h3>
            <div class="minor-detail-subheadline">엔트로피 감쇠 함수를 중심점 이동 벡터에 적용해 국소 최적점(Local Minima) 함정 회피</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  k-means는 모든 데이터 사이언티스트가 처음 배우는 필수 알고리즘이지만 수렴까지 수십 회의 반복 연산이 필요했습니다. E-means는 정보 엔트로피를 도입해 초기 중심점 설정 오류를 능동적으로 보정합니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> High-Dim Feature Vectors &rarr; Entropy-weighted Momentum Step &rarr; Fast Boundary Convergence &rarr; Final Clusters
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  수십억 건의 벡터 임베딩을 클러스터링해야 하는 대규모 RAG 데이터베이스의 인덱싱 시간을 90% 단축할 수 있는 기초 수학적 혁신입니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://e-means.github.io/" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 프로젝트 사이트
              </a>
              <a href="https://news.ycombinator.com/item?id=45878420" target="_blank" class="minor-link discussion">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 17: Show HN: Every satellite that passed over any place this week (watched.earth) -->
        <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 448 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 28.9시간 전</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 15.5 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;지구상의 모든 좌표 위를 지나간 인공위성 궤적과 촬영 사진을 역추적하다 : watched.earth&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">오픈 위성 궤도 데이터와 공개 지구 관측 위성 이미지를 결합해 전 세계 특정 장소의 실시간 위성 통과 기록을 보여주는 지도 플랫폼</span>
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
            <h3 class="minor-detail-headline">하늘 위에 누가 지나갔는지 누구나 열람할 수 있는 오픈 우주 인텔리전스</h3>
            <div class="minor-detail-subheadline">SGP4 궤도 전파 알고리즘과 Sentinel-2, Landsat 멀티스펙트럼 이미지 실시간 연동</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  과거에는 군사 정보기관이나 상용 위성 분석 기업만 접근할 수 있었던 위성 궤도 추적과 고해상도 지표면 촬영 타임라인을 모든 시민과 저널리스트가 무료로 탐색할 수 있는 웹 앱으로 개방했습니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Coordinates Input &rarr; SGP4 Orbital Propagation &rarr; Satellite Pass Matching &rarr; Multi-band Image Mosaic
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  산불 감시, 해양 오염 추적, 분쟁 지역 오픈소스 인텔리전스(OSINT) 조사관들에게 결정적인 시공간 증거 수집 도구를 제공했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://www.watched.earth" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> 웹사이트 바로가기
              </a>
              <a href="https://news.ycombinator.com/item?id=45878100" target="_blank" class="minor-link discussion">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론
              </a>
            </div>
          </div>
        </div>

        <!-- [HN 20~30h] Item 18: CUI – Native UI components for C -->
        <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
          <div class="minor-summary-bar">
            <div class="minor-summary-left">
              <div class="minor-meta-badges">
                <span class="minor-badge badge-hn">HN 20~30h</span>
                <span class="minor-metric">🔺 177 Pts</span>
                <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.2시간 전</span>
                <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 6.51 보트/h</span>
              </div>
              <div class="minor-title-line">
                <strong class="minor-headline-text">&quot;순수 C99로 작성된 초경량 네이티브 크로스플랫폼 UI 컴포넌트 프레임워크 : CUI&quot;</strong>
                <span class="minor-dash">—</span>
                <span class="minor-sub-text">무거운 C++이나 외부 툴킷 종속 없이 시스템 네이티브 드로잉 API를 직접 바인딩하여 200KB 미만 바이너리로 데스크톱 창을 띄우는 순수 C 라이브러리</span>
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
            <h3 class="minor-detail-headline">일렉트론과 거대 GUI 프레임워크의 비만에 맞선 미니멀 C 프로그래밍의 정수</h3>
            <div class="minor-detail-subheadline">Win32, Cocoa, X11 백엔드를 직접 추상화해 버튼, 입력창, 슬라이더를 즉각 렌더링</div>
            <div class="minor-story-body">
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
                <p class="minor-paragraph">
                  단순한 유틸리티 프로그램 하나를 만드는데 수백 메가바이트의 런타임과 복잡한 빌드 도구가 강제되는 현대 데스크톱 개발 환경에 지친 C 임베디드 및 시스템 개발자들에게 단비 같은 도구입니다.
                </p>
              </div>
              <div class="minor-schematic">
                <div class="minor-box-flow">
                  <strong>[파이프라인]</strong> Pure C99 App Code &rarr; CUI Header-only Layer &rarr; Native OS Drawing APIs &rarr; 200KB Standalone Executable
                </div>
              </div>
              <div class="minor-story-section">
                <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
                <p class="minor-paragraph">
                  임베디드 리눅스 및 구형 PC에서도 번개처럼 뜨는 고반응성 GUI 도구를 단일 C 컴파일러 명령어로 손쉽게 빌드할 수 있는 자유를 선사했습니다.
                </p>
              </div>
            </div>
            <div class="minor-footer-links">
              <a href="https://yappologistic.github.io/CUI/" target="_blank" class="minor-link hn">
                <i data-lucide="external-link" class="minor-icon"></i> CUI 공식 문서
              </a>
              <a href="https://news.ycombinator.com/item?id=45879300" target="_blank" class="minor-link discussion">
                <i data-lucide="message-square" class="minor-icon"></i> HN 토론
              </a>
            </div>
          </div>
        </div>

      </div> <!-- .minor-items-container -->
    </section>
"""
