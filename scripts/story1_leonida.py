# -*- coding: utf-8 -*-
# Story 1: ItsNotRexed/Leonida (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] ItsNotRexed/Leonida : COVER STORY                 -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_leonida.jpg" alt="Leonida GTA VI Xbox Series Static Recompilation Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> COVER EXPLOSION #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔥 26시간 만에 ★4,389 · 26,503개 RDNA2 셰이더 SPIR-V 번역 완수</span>
              <span class="platform-tag">GitHub Explosion &amp; Xbox Recomp Wave</span>
              <span class="platform-tag">ItsNotRexed / Leonida</span>
            </div>

            <h2 class="main-lead-headline">
              <span id="hero-title">"PC 출시를 기다리지 않는다" — 26,503개 Xbox 셰이더를 Vulkan으로 직역하며 콘솔 독점의 벽을 허문 정적 리컴파일 혁명 'Leonida'</span>
            </h2>

            <div class="article-subheadline">
              Xbox Series(1.0.2.1)용 GTA 6의 x86-64 코드와 RDNA2 프리컴파일 셰이더 26,503종 전량 SPIR-V 변환·Vulkan 13개 GPU 검증 통과, RPF9 모델/DDS 텍스처/AWC 오디오 무손실 추출 및 Xbox D3D12→Vulkan 프록시 구축 (+4,389스타/26.6h, GPL-3.0)
            </div>
            <p class="article-snippet">
              콘솔 선출시·PC 후출시라는 게임 업계의 20년 된 시간차 독점 공식이 에이전트 기반 정적 리컴파일(Static Recompilation) 공학 앞에서 시험대에 올랐습니다. 공개 하루 남짓한 26.6시간 만에 무려 <strong>4,389개의 스타(시간당 +164스타)</strong>와 306개의 포크, 280건이 넘는 PR을 빨아들인 <strong>ItsNotRexed/Leonida</strong>는 게임 파일이나 복호화 키를 단 1바이트도 배포하지 않은 채, 사용자가 합법적으로 보유한 Xbox Series 패키지에서 26,503개의 RDNA2 셰이더를 추출해 PC용 Vulkan SPIR-V로 100% 번역해 내며 전 세계 시스템 엔지니어들을 충격에 빠뜨렸습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 26시간 만에 쏟아진 654개의 커밋, 그리고 26,503개 셰이더의 100% 통과
            </h3>
            <p>
              오늘 새벽 GitHub의 커밋 로그는 마치 대형 게임 스튜디오의 출시 직전 워룸(War Room)을 방불케 했다. <code>ItsNotRexed/Leonida</code> 저장소가 문을 연 지 불과 26.6시간 만에 55명의 기여자와 306개의 포크가 몰려들었고, 방금 전 올라온 최신 커밋(<code>8bd0087</code>)은 전 세계 리버스 엔지니어링 커뮤니티의 타임라인을 멈춰 세웠다. <strong>"Full-corpus pipeline build: 26,503 of 26,503 shaders compile on NVIDIA, 3.81 GB pipeline cache."</strong>
            </p>
            <p>
              과거 콘솔 게임을 PC에서 돌리려면 CPU 명령어를 실시간으로 통역하는 무거운 에뮬레이터가 완성될 때까지 5~10년을 기다려야 했다. 그러나 Xbox Series X|S의 CPU는 PC와 동일한 x86-64 아키텍처이며, GPU 역시 AMD RDNA2 아키텍처다. <strong>Leonida</strong>는 "에뮬레이션하지 말고, 콘솔용 실행 코드와 프리컴파일된 셰이더를 PC용 네이티브 바이너리와 Vulkan 파이프라인으로 직접 정적 리컴파일하자"는 역발상을 현실로 옮기며, 같은 시간대에 등장한 <code>R0Y00/Xbox2Windows</code>(★864)·<code>omonkeyz/xbox-emulator</code>(★711)·<code>ivall/xcl</code>(★61)과 함께 거대한 'Xbox 정적 리컴파일 물결'의 정점에 섰다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "게임도 키도 배포하지 않는다, 오직 당신의 디스크 위에서 번역될 뿐"
            </h3>
            <p>
              Leonida가 단순한 호기심용 토이 프로젝트를 넘어 기술·산업적 지진으로 평가받는 이유는 두 가지다. 첫째, N64 정적 리컴파일(N64Recomp)이나 Sonic Unleashed 재컴파일로 증명됐던 기법이 마침내 현세대 AAA 타이틀과 <strong>Xbox Series X|S(Scarlett)의 RDNA2·Direct3D 12·RPF9 아카이브 계층</strong>에 본격 적용됐다는 점이다. 둘째, 프론티어 코딩 에이전트와 오픈소스 기여자들이 병렬로 달라붙어 단 하루 만에 26,503개 셰이더 코퍼스 전체를 <code>spirv-val</code> 검증까지 통과시키는 개발 속도의 혁명이다.
            </p>

            <div class="editorial-quote">
              <p>
                "이 저장소에는 게임 실행 파일도, 암호화 키도, 우회 도구도 단 한 줄 들어있지 않다. <strong>사용자가 이미 보유한 정상 패키지에서 셰이더와 에셋을 읽고, 콘솔 OS 레이어만 클린룸으로 재구현해 PC 위에서 직접 빌드한다.</strong>"
              </p>
              <small>— ItsNotRexed/Leonida 공식 아키텍처 및 법적 경계 선언 (GPL-3.0)</small>
            </div>

            <p>
              물론 Leonida는 아직 초기 단계로, PE 로더와 Xbox D3D12→Vulkan 스왑체인/드로우 콜 파이프라인이 완성되지 않아 실제 스토리 모드가 부팅되지는 않는다. 그럼에도 불구하고 2,236개의 버텍스 셰이더, 12,101개의 픽셀 셰이더, 2,689개의 컴퓨트 셰이더, 무려 9,282개의 메시 셰이더, 195개의 지오메트리 셰이더까지 총 <strong>26,503개 셰이더 전량이 SPIR-V로 변환되어 드라이버 파이프라인 캐시(3.81 GB) 생성에 성공</strong>했다는 사실 자체가 기술적 난공불락으로 여겨지던 장벽의 붕괴를 뜻한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: RDNA2→SPIR-V 셰이더 번역기와 Xbox D3D12→Vulkan 프록시 해부
            </h3>
            <p>
              Leonida의 빌드 파이프라인(<code>Build.bat</code>)은 사용자의 PC에서 원클릭으로 로컬 패키지를 탐지한 뒤 다음 3단계 엔진을 거쳐 네이티브 PC 런타임을 조립한다:
            </p>
            <ul>
              <li><strong>RPF9 아카이브·멀티미디어 손실 없는 추출기:</strong> <code>rpf9-explorer</code> 서브모듈을 통해 <code>MicrosoftGame.Config</code>와 RPF9 컨테이너에서 모델(OBJ+UV+머티리얼), 텍스처 풀(DDS), 오디오 뱅크(AWC의 Opus 스트림 무손실 Ogg Opus 리패키징 및 XMA2/PCM 디코딩), 1,589개의 라디오·음악 설정 레코드를 로컬 디스크로 추출한다.</li>
              <li><strong>RDNA2 네이티브 코드 → Vulkan SPIR-V 정적 번역기:</strong> Xbox Series가 미리 컴파일해 둔 AMD RDNA2 바이너리 셰이더 26,503개를 카빙·디스어셈블한 뒤, 각 셰이더 단계별 메타데이터 인덱스와 함께 SPIR-V로 번역한다. 특히 AMD의 64-wide 서브그룹(<code>wave64</code>) 명령을 NVIDIA 32-wide(<code>wave32</code>) GPU에서도 에뮬레이션(<code>LEONIDA_W64_EMULATE=1</code>)할 수 있도록 설계되어 NVIDIA Turing·Ampere·Ada·Blackwell부터 AMD RDNA2/3, Apple M1(MoltenVK)까지 13종의 실물 GPU에서 단위 테스트를 통과했다.</li>
              <li><strong>Xbox-ABI D3D12 → Vulkan 프록시 &amp; PE 임포트 심(Shim):</strong> 콘솔의 통합 메모리 텍스처와 Xbox 전용 Direct3D 12 확장을 Vulkan 커맨드 큐·펜스·디스크립터 힙·리소스 배리어·BC 텍스처 복사로 매핑하는 프록시 계층과 <code>XGameRuntime</code> 오프라인 심을 통해 향후 메인 실행 파일의 네이티브 로드를 준비한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Leonida Xbox Series → PC 네이티브 정적 리컴파일 파이프라인</span>
                <span class="schematic-badge">GPL-3.0 · 26,503 SPIR-V Shaders Validated · Zero Game Assets Shipped</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Local Copy &amp; Asset Carve</div>
                  <div class="schematic-desc">
                    사용자 로컬 디스크 Xbox 패키지 탐지<br>
                    <code>rpf9-explorer</code> 기반 아카이브 파싱<br>
                    OBJ 모델·DDS 텍스처·1,589 오디오 추출<br>
                    RDNA2 네이티브 셰이더 26,503개 분리
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. RDNA2 → SPIR-V Translator</div>
                  <div class="schematic-desc">
                    VS(2,236)·PS(12,101)·Mesh(9,282) 전량 번역<br>
                    <code>spirv-val</code> 통과 + 메타데이터 인덱싱<br>
                    <code>wave64</code> → NVIDIA <code>wave32</code> 에뮬레이션<br>
                    13종 GPU 검증 · 3.81GB 파이프라인 캐시
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Xbox ABI &amp; Vulkan Proxy</div>
                  <div class="schematic-desc">
                    x86-64 PE 로더 &amp; <code>XGameRuntime</code> 심<br>
                    Xbox D3D12 커맨드·배리어 → Vulkan 매핑<br>
                    사용자 PC <code>Documents\\Leonida</code> 로컬 빌드<br>
                    (현재 부팅/드로우 파이프라인 개발 진행 중)
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">ItsNotRexed/Leonida 저장소 실화면 — 26시간 만에 4,400스타·654커밋 폭주 현장</span>
              </div>
              <img src="../assets/images/demo_leonida.png" alt="ItsNotRexed Leonida GitHub Repository Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/ItsNotRexed/Leonida 실화면: 55명의 기여자가 실시간 PR을 병합하며 26,503개 RDNA2 셰이더 전량을 NVIDIA Vulkan 파이프라인 캐시(3.81 GB)로 컴파일하는 데 성공한 커밋과 런타임/뷰어/툴 디렉터리 구조.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 법적·산업적 분기점: 콘솔 '더블 디핑' 해자와 클린룸 상호운용성의 충돌
            </h3>
            <p>
              수십 년간 대형 콘솔 퍼블리셔들은 콘솔 독점 출시 후 1~2년 뒤 PC 버전을 별도로 판매해 매출을 극대화하는 이른바 '더블 디핑(Double-Dipping)' 전략을 핵심 비즈니스 해자로 삼아왔다. 그러나 Leonida와 동시에 터져 나온 <code>Xbox2Windows</code>(MIT)·<code>xbox-emulator</code>(Apache-2.0)·<code>xcl</code>(GPL-2.0) 생태계는 하드웨어 아키텍처가 x86-64와 RDNA2로 통일된 현세대 콘솔에서 그 기술적 시간차가 얼마나 얇은 빙판 위에 서 있는지를 적나라하게 보여준다.
            </p>
            <ul>
              <li><strong><em>Sega v. Accolade</em>와 <em>Sony v. Connectix</em>의 방패:</strong> Leonida 프로젝트는 저작권이 있는 게임 바이너리, 복호화 키, DRM 우회 코드를 일절 포함하지 않고 사용자가 이미 구매해 읽을 수 있는 로컬 파일을 기반으로 API 호환 레이어(Shim)만 재구현한다. 이는 1990~2000년대 미국 연방항소법원이 합법적 상호운용성(Interoperability)을 위한 클린룸 역공학의 공정 이용(Fair Use)을 인정한 <em>Sega v. Accolade</em> 및 <em>Sony v. Connectix</em> 판례의 직계 후예다.</li>
              <li><strong>DMCA 1201조와 플랫폼 압박 리스크:</strong> 그럼에도 거대 퍼블리셔와 콘솔 홀더가 DMCA 1201조(접근 통제 우회 금지)나 상표권·리버스 엔지니어링 금지 약관을 들어 GitHub DMCA 게시 중단(Takedown)을 시도할 가능성은 상존한다. 프로젝트가 '암호화 해제 도구는 제공하지 않는다'고 수차례 못 박은 이유도 이 법적 방어선을 사수하기 위함이다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 하드웨어가 PC와 같아진 순간, 독점은 물리학이 아니라 계약일 뿐이다
            </h3>
            <p>
              콘솔 내부의 실리콘이 PC와 똑같은 x86-64 명령어와 RDNA2 셰이더를 실행하는 시대에, 플랫폼 간의 장벽은 더 이상 호환성 불가능성이라는 물리 법칙이 아니라 오직 소프트웨어 ABI의 얇은 막에 불과하다.
            </p>
            <p>
              아직 화면에 첫 프레임을 띄우기도 전에 하루 만에 4,400명의 개발자가 모여 26,503개의 셰이더를 뚫어버린 Leonida의 질주는 게임 산업을 넘어 묻고 있다. 사용자가 정당하게 구매한 소프트웨어를 자신의 컴퓨터에서 네이티브로 실행할 권리는 과연 어디까지인가?
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Leonida+Xbox+Series+static+recompilation+GitHub" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/ItsNotRexed/Leonida" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
