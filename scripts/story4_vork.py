# -*- coding: utf-8 -*-
# Story 4: voyager-so/vork

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 4] voyager-so/vork : AI 에이전트 전용 3D & VFX 엔진 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_vork.jpg" alt="vork headless 3D and VFX engine for agents" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="box" style="width:12px;height:12px;fill:#fff;"></i> AGENT 3D</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 AI 에이전트에게 3차원 감각과 붓을 쥐어준 그래픽스 혁명</span>
              <span class="platform-tag">GitHub Rocket</span>
              <span class="platform-tag">voyager-so / vork</span>
            </div>
            
            <h2 class="article-lead-headline">
              코드가 곧 3D 모델이 되고 파티클이 되다 — 에이전트 전용 헤드리스 3D·VFX 렌더링 커널 'vork'
            </h2>

            <div class="article-subheadline">
              무거운 블렌더 GUI와 언리얼 엔진을 걷어내다… 자율 코딩 에이전트가 순수 Rust/Python 코드로 3차원 씬을 배치하고 헐리우드급 시각효과(VFX)를 초고속 렌더링하는 전용 엔진
            </div>
            <p class="article-snippet">
              AI 코딩 에이전트가 웹 UI와 텍스트를 넘어 3차원 컴퓨터 그래픽스와 VFX 제작에 직접 뛰어들 수 있도록 설계된 무헤드(Headless) 3D 엔진 'vork'가 공개되었습니다. 마우스 클릭 기반의 복잡한 3D 제작 소프트웨어 대신, 에이전트 친화적인 결정론적 코드 실행과 하드웨어 GPU 가속을 직결하여 3D 콘텐츠 제작의 패러다임을 바꿉니다.
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
              <i data-lucide="flame"></i> 1. 리드: 에이전트는 왜 3D 그래픽스를 만들지 못했을까
            </h3>
            <p>
              Claude Code나 Antigravity 같은 최신 AI 에이전트들은 수천 줄의 풀스택 웹 코드를 짜고 시스템 버그를 뚝딱 고쳐내지만, 
              유독 3차원 컴퓨터 그래픽스와 시각효과(VFX) 영역에서는 무력했다. 
              블렌더(Blender), 마야(Maya), 언리얼 엔진(Unreal Engine) 같은 기존 툴들이 철저하게 인간의 마우스 드래그와 복잡한 GUI 창을 전제로 설계되어 있었기 때문이다.
            </p>
            <p>
              오늘 깃허브에서 급상승하며 그래픽스 엔지니어들의 시선을 사로잡은 <strong>voyager-so/vork</strong>(Voyager Rendering Kernel)는 
              이 구조적 단절을 종식시키는 세계 최초의 '에이전트 네이티브 3D·VFX 렌더링 커널'이다. 
              인간용 GUI 창을 완전히 걷어내고, 
              <strong>오직 AI 에이전트가 코드로 씬(Scene) 그래프를 선언하고, 물리를 계산하며, 광선 추적과 파티클 효과를 지휘할 수 있는 헤드리스 런타임</strong>을 완성한 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '설명서 없는 GUI' 대신 '결정론적 코드 그래픽스'
            </h3>
            <p>
              기존에 AI에게 3D 작업을 시키려면 복잡한 파이썬 스크립트를 블렌더 백그라운드 프로세스로 넘겨야 했지만, 
              무거운 의존성과 비결정론적 렌더링 파이프라인 때문에 에이전트가 렌더링 오류를 스스로 디버깅하기란 불가능에 가까웠다.
            </p>

            <div class="editorial-quote danger">
              <p>
                "vork는 인간을 위한 모델링 도구가 아니다. 
                에이전트가 1밀리초 만에 씬 트리를 조작하고, GPU 하드웨어에서 셰이더를 즉시 컴파일하며, 
                <strong>30밀리초 안에 렌더링된 서브프레임 버퍼를 비전 피드백으로 받아 자율 교정할 수 있는 순수 연산 커널</strong>이다."
              </p>
              <small>— Voyager 리서치 프리뷰 백서</small>
            </div>

            <p>
              vork는 Rust로 작성되어 메모리 오버헤드가 제로에 가깝다. 
              에이전트는 텍스트 프롬프트에 따라 카메라 앵글, 조명 베이킹, 볼류메트릭 안개, 충돌 물리 파티클을 파이썬/러스트 코드로 제어하며 영화급 3D 시퀀스를 스스로 만들어낸다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: SDF 지오메트리와 실시간 GPU 헤드리스 파이프라인
            </h3>
            <p>
              vork 커널이 에이전트에게 최고의 효율을 보장하는 3대 아키텍처는 다음과 같다:
            </p>
            <ul>
              <li><strong>SDF(부호 거리 함수) 기반 절차적 형상 모델링:</strong> 수백만 개의 버텍스 폴리곤을 일일이 만지는 대신, 에이전트가 이해하기 쉬운 수학적 SDF 프리미티브 결합으로 유기적인 3D 물체를 수식 단위로 정의.</li>
              <li><strong>wgpu 기반 크로스플랫폼 헤드리스 셰이더:</strong> 디스플레이 모니터 연결 없이 서버 환경에서도 Vulkan, Metal, DX12 GPU 가속을 완전히 끌어내어 4K 프레임을 초고속 비동기 렌더링.</li>
              <li><strong>에이전트 닫힌 루프(Closed-Loop) 비전 피드백:</strong> 렌더링된 결과물의 깊이 맵(Depth map), 법선 벡터(Normal vector), 분할 마스크(Segmentation mask)를 에이전트의 멀티모달 컨텍스트로 즉각 반환하여 실시간 오차 수정.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="cuboid" style="color:#0ea5e9;"></i> vork 에이전트 헤드리스 3D·VFX 파이프라인
                </span>
                <span class="schematic-badge">HEADLESS AGENTIC RENDERING</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">선언적 코드 씬 정의</div>
                  <div class="step-tech">Python / Rust SDF & Particle Physics API</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">wgpu 헤드리스 렌더링</div>
                  <div class="step-tech">Vulkan / Metal Hardware GPU Acceleration</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">에이전트 비전 피드백 루프</div>
                  <div class="step-tech">Depth / Normal Buffer Feedback for Self-Correction</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 원리:</strong> 디스플레이 화면 없이 백그라운드 GPU에서 에이전트의 코드를 즉각 3D 그래픽스로 합성하고, 렌더링 버퍼를 에이전트의 시각 신경망으로 되먹여 자율적인 3D 수정을 가능케 합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-check"></i> 4. 비즈니스 해자: 3D 미디어 제작 산업의 문법 파괴
            </h3>
            <p>
              헐리우드 영화사나 게임 스튜디오의 VFX 부서는 수백 명의 3D 아티스트와 복잡한 렌더팜(Render Farm)에 의존해 왔다. 
              하지만 vork와 같은 에이전트 전용 3D 커널이 보편화되면, 
              시나리오 작가나 1인 크리에이터가 텍스트 명령만으로 고품질 시네마틱 3D 장면과 모션 그래픽스를 몇 초 만에 생성하고 수정할 수 있게 된다.
            </p>
            <p>
              어도비(After Effects)와 오토데스크(Maya)가 수십 년간 구축해온 전문가용 GUI 소프트웨어의 아성이, 
              코드로 구동되는 경량 에이전트 런타임에 의해 근본부터 흔들리고 있다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="monitor" style="color:#10b981;"></i> vork 공식 프리뷰 및 헤드리스 그래픽스 씬
                </span>
                <span class="media-showcase-badge demo">OFFICIAL SHOWCASE</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_vork.png" alt="vork 3D rendering preview" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 헤드리스 렌더링 결과물:</strong> AI 에이전트의 절차적 코드 호출만으로 렌더링된 vork의 사이버 차량 및 실시간 라이팅 데모.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="zap"></i> 5. 키커: 상상력이 곧 3차원 현실이 되는 순간
            </h3>
            <p>
              "마우스를 쥔 인간의 손끝이 아니라, 수식과 코드를 다루는 에이전트의 지능이 3차원 공간을 빚어낸다." 
              vork는 단순한 렌더러가 아니라, AI가 물리 법칙과 빛의 궤적을 이해하고 가상 세계를 창조하기 시작했음을 알리는 신호탄이다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://voyager.so/vork" target="_blank" class="project-link demo">
                  <i data-lucide="globe" style="width:16px;height:16px;"></i> 공식 웹사이트 방문
                </a>
                <a href="https://github.com/voyager-so/vork" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
