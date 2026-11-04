# -*- coding: utf-8 -*-
# Story 1: valentderah/totk-pc-recomp (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] valentderah/totk-pc-recomp : 오늘의 메인 기사 (COVER STORY) -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_totk_recomp.jpg" alt="TotK PC Recompilation" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔥 닌텐도 독점 콘솔의 벽을 허문 리컴파일러 엔지니어링</span>
              <span class="platform-tag">GitHub Breakthrough</span>
              <span class="platform-tag">valentderah / totk-pc-recomp</span>
            </div>
            
            <h2 class="main-lead-headline">
              <span id="hero-title">에뮬레이터의 종말과 네이티브 C++의 귀환: '젤다의 전설 티어스 오브 더 킹덤' 윈도우 PC 정적 재컴파일 혁명</span>
            </h2>

            <div class="article-subheadline">
              "20fps로 신음하던 스위치 하드웨어의 족쇄를 완전히 분쇄하다" — 전 세계 2,000만 장 판매된 닌텐도 스위치 플래그십 『젤다의 전설 티어스 오브 더 킹덤(TotK)』이 에뮬레이터 없이 Windows x86-64 네이티브 바이너리로 정적 재컴파일(Static Recompilation) 성공… 4K UHD 144Hz 무제한 주사율, Vulkan 1.3 하드웨어 가속, 셰이더 스터터링(Shader Stutter) 0초 컴파일로 콘솔 독점의 해자를 허물다
            </div>
            <p class="article-snippet">
              무거운 런타임 JIT 인터프리터로 구동되던 에뮬레이션 시대를 끝내고, 스위치 ARM64 기계어를 C/C++ 중간 언어로 들어 올려(Lift) AVX2 x86-64로 직접 빌드하는 정적 리컴파일러의 기적. 닌텐도의 법적 봉쇄를 뚫는 클린룸 역공학의 분기점.
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
              <i data-lucide="flame"></i> 1. 리드: 20fps의 한계를 뚫고 4K 144Hz로 깨어난 하이랄 대지
            </h3>
            <p>
              2023년 5월, 닌텐도가 출시한 『젤다의 전설: 티어스 오브 더 킹덤(Tears of the Kingdom, 이하 TotK)』은 비디오 게임 역사상 가장 경이로운 물리 상호작용과 오픈월드 건축 메커니즘을 선보였다. 
              그러나 그 경이로움 뒤에는 항상 잔인한 타협이 따랐다. 
              2017년 출시된 20나노 구형 테그라 X1(Tegra X1) 칩셋 위에서 구동되는 스위치는, 링크가 하늘섬에서 지상으로 다이빙하거나 울트라핸드로 거대 비행선을 조합할 때마다 <strong>초당 20프레임 이하로 곤두박질치는 심각한 프레임 드랍과 720p 동적 해상도의 흐릿한 안개</strong>에 갇혀 있었다.
            </p>
            <p>
              PC 게이머들은 유주(Yuzu)나 류진스(Ryujinx) 같은 고성능 에뮬레이터를 통해 이를 극복하려 했지만, 닌텐도의 가차 없는 저작권 철퇴(DMCA 및 수백억 원대 합의금 소송)로 주요 에뮬레이터들이 차례로 문을 닫으면서 콘솔 독점의 장벽은 다시 높아지는 듯했다. 
              게다가 에뮬레이터 고유의 한계인 <strong>JIT(Just-In-Time) 셰이더 컴파일 스터터링(화면 끊김 현상)과 막대한 CPU 가상화 오버헤드</strong>는 최신 4,000번대 지포스 그래픽카드 위에서도 완벽한 60fps 유지를 어렵게 만들었다.
            </p>
            <p>
              그 순간, 리버스 엔지니어링 진영에서 상상을 초월하는 오픈소스 프로젝트가 깃허브에 폭발했다. 
              개발자 <strong>valentderah</strong>가 이끄는 프로젝트 <strong>TotK Recomp(valentderah/totk-pc-recomp)</strong>가 그 주인공이다. 
              이 프로젝트는 에뮬레이터를 사용하지 않는다. 
              대신 스위치 롬에서 추출한 원본 ARM64 바이너리를 한 줄 한 줄 <strong>순수 Windows x86-64 네이티브 기계어로 완전히 재번역(Static Recompilation)</strong>하여, 일반 윈도우 PC 게임처럼 더블클릭 한 번으로 구동되는 독립 실행 파일(<code>totk.exe</code>)을 빚어냈다.
            </p>

            <div class="editorial-quote danger">
              "우리는 스위치를 가상으로 흉내 내는 에뮬레이터를 돌리지 않습니다. 
              <strong>TotK Recomp는 닌텐도가 처음부터 윈도우 x86-64와 Vulkan 1.3을 타깃으로 C++ 소스코드를 직접 빌드한 것처럼 완벽한 네이티브 PC 바이너리로 다시 컴파일합니다.</strong> 
              에뮬레이터의 병목인 JIT 변환 루프가 사라지면서, 하이랄의 하늘섬은 이제 단 1프레임의 스터터링도 없이 4K 144Hz로 숨을 쉽니다."
              <span class="quote-author">— TotK Recomp 핵심 개발팀 기술 백서(Architecture Manifest) 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 에뮬레이터의 종말과 정적 재컴파일(Static Recompilation)의 부상
            </h3>
            <p>
              이번 사건이 테크 생태계에 던지는 충격은 단순히 "게임을 PC에서 돌린다"는 수준을 훨씬 뛰어넘는다. 
              지난 30년간 콘솔 에뮬레이션은 대상 기기의 CPU, GPU, 메모리 버스, 인터럽트 컨트롤러를 소프트웨어적으로 가상화하는 복잡한 VM(가상머신) 구조에 매달려 왔다. 
              하지만 닌텐도 64(N64 Recomp)와 젤다 꿈꾸는 섬(LAS Recomp)을 거쳐 검증된 <strong>정적 재컴파일(Static Recompilation) 기법</strong>이 2,000만 줄 이상의 거대 현대 타이틀인 TotK에 사상 최초로 성공적으로 적용된 것이다.
            </p>
            <p>
              이것은 기술적 패러다임의 거대한 분기점이다:
              <strong>에뮬레이션이 '해석(Interpretation)'이라면, 정적 재컴파일은 '환생(Transmutation)'이다.</strong> 
              스위치의 모든 시스템 콜과 그래픽 명령어가 윈도우의 커널32 API와 네이티브 불칸(Vulkan) 드라이버로 직결되기 때문에, 구형 노트북에서도 60fps가 가볍게 방어되고 고성능 데스크톱에서는 21:9 울트라와이드와 144fps를 네이티브로 뿜어낸다.
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-title">
                <i data-lucide="git-merge"></i> TotK Recomp: 스위치 ARM64에서 윈도우 x86-64 네이티브 Vulkan으로의 정적 변환 파이프라인
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <span class="schematic-badge">단계 1: 롬 데이터 추출</span>
                  <strong>합법적 원본 덤프</strong>
                  <div class="schematic-desc">
                    사용자 스위치 콘솔에서 추출한 base 1.0.0 NSP + 1.4.3 누적 업데이트 ExeFS/RomFS 분해 (MacNativeGames 해시 검증)
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 2: CPU 리프팅</span>
                  <strong>ARM64 to C/AVX2</strong>
                  <div class="schematic-desc">
                    스위치 64비트 기계어를 C 코드로 리프팅(Lifting). ARM NEON 128비트 벡터 연산을 x86-64 AVX2/FMA 네이티브 인라인 어셈블리로 강등
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 3: OS 경계 재매핑</span>
                  <strong>nn::* SDK & 38 SVC 대체</strong>
                  <div class="schematic-desc">
                    닌텐도 커널 호출(SVC)과 163개 SDK 심볼을 윈도우 Win32 커널(Thread, VirtualAlloc, WASAPI 오디오) 심볼로 1:1 클린룸 매핑
                  </div>
                </div>
                <div class="schematic-box">
                  <span class="schematic-badge">단계 4: 그래픽 엔진 전환</span>
                  <strong>NVN &rarr; Pure Vulkan 1.3</strong>
                  <div class="schematic-desc">
                    엔비디아 맥스웰 NVN 커맨드 리스트를 Vulkan 파이프라인으로 전환. 셰이더를 인스톨 타임에 사전 컴파일(Shader Stutter 0초)
                  </div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="layers"></i> 3. 기술 메커니즘: NEON 벡터의 AVX2 변환과 셰이더 스터터링의 박멸
            </h3>
            <p>
              TotK Recomp의 아키텍처 문서는 현대 컴파일러 공학의 정수를 보여준다. 
              핵심 난제는 스위치의 ARM Cortex-A57 코어가 사용하는 <strong>NEON SIMD 명령어와 특수 메모리 모델</strong>을 x86-64 아키텍처에서 성능 손실 없이 치환하는 일이었다.
            </p>
            <p>
              개발팀은 <code>LAS Recomp</code>의 리프터(Lifter) 엔진을 대대적으로 개조하여, TotK의 1.4.3 버전(최신 SDK 20.5.22, RELR 재배치 테이블 및 REV15 오디오 렌더러 적용 버전)을 정밀 타깃했다. 
              게임 내 수만 개의 함수 블록을 파싱하여 C++ 소스코드로 복원한 뒤, LLVM Clang 컴파일러를 통해 인텔/AMD CPU에 최적화된 x86 기계어로 직결했다.
            </p>
            <p>
              더욱 놀라운 성취는 그래픽 서브시스템이다. 
              에뮬레이터에서 게이머들을 괴롭히던 '새로운 몬스터나 이펙트가 등장할 때마다 멈칫거리는 현상'은 런타임에 셰이더 바이트코드를 번역하느라 발생한다. 
              TotK Recomp는 <strong>설치 프로그램(TotK-Setup.exe)을 처음 실행할 때 게임 내 사용되는 100% 모든 맥스웰 셰이더를 감지하여 유저의 GPU 드라이버에 맞춰 사전 컴파일(Pre-compilation)</strong>을 끝마친다. 
              게임 내 로딩 창이나 격렬한 보스 전투에서도 프레임 타임 그래프가 완벽한 직선(6.93ms)을 유지하는 비결이다.
            </p>

            <!-- 실구동 미디어 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_totk_recomp_bench.jpg" alt="TotK Recomp Benchmark and Vulkan HUD" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="monitor"></i> <strong>[실구동 캡처 검증]</strong> Windows 11 네이티브 환경에서 구동된 TotK Recomp 실행 화면. 3840x2160(4K UHD) 해상도에서 144.2 FPS를 오차 없이 출력하며, F1 인게임 설정창을 통해 21:9 울트라와이드 화면비와 AMD FSR 1.0 업스케일러, 듀얼센스 자이로 조준을 직접 제어하고 있다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 법적 분기점과 비즈니스 해자: 닌텐도의 소송 칼날을 피하는 '클린룸' 방패
            </h3>
            <p>
              닌텐도는 지식재산권(IP) 보호에 있어 세계에서 가장 공격적인 기업이다. 
              지난 2024년 트로픽 하즈(유주 개발사)에 240만 달러의 합의금을 물리고 코드를 파기시켰던 무기는 미국의 디지털 밀레니엄 저작권법(DMCA) 제1201조(기술적 보호조치 우회 금지)였다. 
              유주가 암호화 키(prod.keys)를 우회하는 로직을 제공하여 불법 복제를 조장했다는 논리였다.
            </p>
            <p>
              하지만 TotK Recomp는 이 법적 덫을 완벽한 <strong>클린룸 역공학(Clean-Room Reverse Engineering)</strong>으로 무력화했다:
            </p>
            <ul>
              <li><strong>저작권 에셋 제로 배포 원칙:</strong> 저장소에는 닌텐도의 독점 코드, 텍스처, 사운드, 암호화 키가 단 1바이트도 포함되어 있지 않다. 오직 공개된 컴파일러 도구와 리컴파일 엔진 코드만 존재한다.</li>
              <li><strong>엔드유저 로컬 빌드 모델:</strong> 설치기(Setup.exe)는 사용자가 본인의 정품 스위치 콘솔에서 직접 덤프한 합법적 게임 파일과 콘솔 고유 키를 입력해야만 로컬 PC에서 비로소 실행 바이너리를 생성한다.</li>
              <li><strong>역공학의 합법 판례 준수:</strong> 미국 제9연방순회항소법원의 역사적 판례인 <em>Sony Computer Entertainment v. Connectix Corp.(2000)</em> 및 <em>Sega Enterprises Ltd. v. Accolade, Inc.(1992)</em>에 따르면, 플랫폼 상호 운용성을 확보하기 위한 클린룸 역공학은 '공정 이용(Fair Use)'으로 보호받는다.</li>
            </ul>
            <p>
              닌텐도가 하드웨어 판매로 마진을 남기고 타이틀 독점으로 생태계를 가두는 폐쇄형 비즈니스 모델은, 오픈소스 정적 재컴파일러라는 거대한 기술적 우회로 앞에서 심각한 시험대에 올랐다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 플랫폼의 장벽이 무너지는 네이티브 소프트웨어의 신세계
            </h3>
            <p>
              스위치 2의 출시 루머가 무성한 가운데, 게이머들은 더 이상 빅테크 하드웨어 제조사가 걸어 잠근 20fps와 30fps의 감옥에 갇혀 있기를 거부한다. 
              TotK Recomp가 증명한 것은 명확하다. 
              충분히 뛰어난 오픈소스 컴파일러 기술이 있다면, <strong>독점 콘솔 플랫폼의 수명과 한계는 하드웨어 제조사가 아니라 글로벌 개발자 커뮤니티의 의지에 의해 다시 쓰인다</strong>는 사실이다.
            </p>
            <p>
              우리는 지금, 수십 년간 지속된 '에뮬레이터'라는 과도기적 통역사를 거쳐, 모든 아키텍처의 소프트웨어가 자유롭게 플랫폼을 건너뛰는 '정적 재컴파일의 시대'로 진입하고 있다.
            </p>

          </div> <!-- .editorial-content -->

          <!-- 기사 하단 고시인성 액션 링크 바 -->
          <div class="article-links-bar">
            <a href="https://www.youtube.com/results?search_query=Tears+of+the+Kingdom+PC+Recompilation+144fps" target="_blank" rel="noopener noreferrer" class="project-link youtube">
              <i data-lucide="play" style="width:16px;height:16px;fill:currentColor;"></i> 유튜브 관련 리뷰보기
            </a>
            <a href="https://github.com/valentderah/totk-pc-recomp" target="_blank" rel="noopener noreferrer" class="project-link github">
              <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
            </a>
          </div>

        </div> <!-- .article-detail -->
      </article>
"""
