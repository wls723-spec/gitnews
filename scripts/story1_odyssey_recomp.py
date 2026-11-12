# -*- coding: utf-8 -*-
# Story 1: Simon3Sarkis/super-odyssey-pc-recomp (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] Simon3Sarkis/super-odyssey-pc-recomp : COVER STORY -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_odyssey_recomp.jpg" alt="Super Mario Odyssey PC Recomp Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔥 닌텐도 DMCA 사태 당일 전격 공개</span>
              <span class="platform-tag">GitHub Trending #1 & HN Frontpage</span>
              <span class="platform-tag">Simon3Sarkis / super-odyssey-pc-recomp</span>
            </div>
            
            <h2 class="main-lead-headline">
              <span id="hero-title">닌텐도 전방위 DMCA 칼바람 뚫고 등장한 슈퍼 마리오 오디세이 4K PC 포트: "에뮬레이터는 죽었지만, 정적 재컴파일은 죽지 않는다"</span>
            </h2>

            <div class="article-subheadline">
              닌텐도 법무팀의 깃허브 스위치 에뮬레이터 전면 압류 사태 속, 저작권 자산 단 1바이트 없이 순수 C++ 정적 재컴파일(AOT)로 4K 144Hz PC 네이티브 런타임을 뽑아낸 역사적 오픈소스의 합법적 승리
            </div>
            <p class="article-snippet">
              IGN과 주요 외신들이 "닌텐도가 깃허브의 주요 스위치 에뮬레이터와 모드칩 펌웨어를 겨냥한 사상 최대 규모의 DMCA 삭제 조치를 단행했다"고 보도한 바로 그날, 콘솔 해킹 커뮤니티는 전혀 다른 차원의 기술적 반격을 가했습니다. 에뮬레이터 가상머신을 아예 쓰지 않고, 순정 게임의 ARM64 머신 코드를 윈도우 네이티브 x86-64 및 Vulkan C++ 코드로 완전히 번역해 컴파일하는 '슈퍼 마리오 오디세이 PC 정적 재컴파일러'가 오픈소스로 공개된 것입니다.
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
              <i data-lucide="flame"></i> 1. 리드: 닌텐도 법무팀의 압류 폭풍 속, 에뮬레이션을 비웃듯 터져 나온 C++ 바이너리
            </h3>
            <p>
              2026년 11월 12일 저녁, 전 세계 오픈소스 커뮤니티는 얼어붙었다. 닌텐도(Nintendo of America)가 대형 로펌을 대동하여 GitHub 저장소 수백 곳에 일제히 DMCA(디지털 밀레니엄 저작권법) 통고를 보내며 스위치 에뮬레이터 포크와 암호화 키 추출 도구들을 강제 폐쇄시켰기 때문이다.
            </p>
            <p>
              하지만 닌텐도의 전방위 압류 폭풍이 최고조에 달했던 바로 그 시각, GitHub 메인 트렌딩 1위에 불가능해 보였던 프로젝트 하나가 솟아올랐다: <strong>Simon3Sarkis/super-odyssey-pc-recomp</strong>.
            </p>
            <p>
              이 프로젝트는 Yuzu나 Ryujinx 같은 '에뮬레이터'가 아니다. 에뮬레이터 런타임의 JIT 컴파일러나 인터프리터를 실행하는 가상머신이 아니라, 닌텐도 스위치용 명작 타이틀 <em>슈퍼 마리오 오디세이(Super Mario Odyssey)</em>의 ARM64 ELF 실행 바이너리를 통째로 역어셈블하여, 순수 64비트 Windows 네이티브 C++ 소스 코드로 1대1 치환한 뒤 Vulkan 그래픽 파이프라인으로 다시 빌드해낸 <strong>정적 재컴파일(Static Recompilation) PC 포트</strong>다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 에뮬레이터의 한계를 박살 낸 4K 144Hz 무지연 혁명
            </h3>
            <p>
              에뮬레이터는 본질적으로 게스트 콘솔의 CPU와 GPU, 메모리 버스를 실시간 가상화하는 극심한 오버헤드를 짊어진다. 셰이더 컴파일 끊김(Stuttering), 타이밍 버그, 높은 CPU 점유율은 불가피한 숙명이었다.
            </p>
            <p>
              그러나 정적 재컴파일러는 게임의 모든 함수와 로직을 사전에 PC의 x86-64 네이티브 기계어로 완전히 다시 컴파일해버린다. 결과물은 사이버펑크나 위쳐 같은 일반 PC 게임과 똑같은 순수 Windows `.exe` 실행 파일이다.
            </p>

            <div class="editorial-quote">
              <p>
                "우리는 에뮬레이터를 만들지 않았다. 우리는 마리오 오디세이를 순수 C++로 다시 컴파일했다. 
                <strong>에뮬레이션 오버헤드는 정확히 0%다. 스위치 본체의 720p 60fps 한계를 넘어, 지포스 RTX 그래픽카드에서 네이티브 4K 해상도, 144Hz 주사율, 울트라와이드 모니터, 제로 인풋랙을 달성했다.</strong> 
                그리고 이 프로젝트에는 닌텐도의 자산이나 저작권 코드가 단 1바이트도 들어있지 않다."
              </p>
              <small>— Simon Sarkis, Super Odyssey PC Recomp 수석 개발자 릴리즈 노트</small>
            </div>

            <p>
              해커뉴스와 레딧에서 수천 개의 추천을 받으며 화제를 모은 이 프로젝트는, 젤다의 전설 시간의 오카리나(Ship of Harkinian)와 티어스 오브 더 킹덤(TOTK Recomp)에 이어 닌텐도의 최신 플래그십 샌드박스 3D 액션 게임마저 PC 네이티브 플랫폼으로 완벽하게 편입시켰음을 입증했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 메커니즘: ARM64 기계어를 C++로 외과 수술하듯 치환하는 N64Recomp 아키텍처
            </h3>
            <p>
              정적 재컴파일은 고도의 컴퓨터 구조론과 컴파일러 공학의 극한 기술이다. 개발팀은 다음과 같은 파이프라인을 구축했다:
            </p>
            <ul>
              <li><strong>Executable & Resource Decoupling:</strong> 사용자가 정품 카트리지에서 추출한 `main` ELF 실행 파일과 `romfs` 에셋 폴더를 준비하면, 도구가 바이트 단위 분석을 시작.</li>
              <li><strong>ARM64 to C++ Translation Core:</strong> 스위치 Tegra X1의 64비트 ARMv8 명령어와 레지스터 상태를 C++의 변수와 제어 흐름 구조로 정적 매핑. 함수 점프 테이블과 간접 분기(Indirect Branches)를 정밀 제어 흐름 그래프(CFG)로 분석해 복원.</li>
              <li><strong>NVN to Vulkan Driver Translation:</strong> 닌텐도 독점 그래픽 API인 NVN 호출을 현대 Vulkan 1.3 렌더링 패스와 컴퓨트 파이프라인으로 무지연 변환하여 비동기 셰이더 컴파일 병목을 원천 박멸.</li>
              <li><strong>DirectInput & XInput 매핑:</strong> 듀얼센스 햅틱 피드백 및 엑스박스 컨트롤러는 물론, 마우스 자이로 에임과 키보드 조작을 완벽 지원.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Super Mario Odyssey 정적 재컴파일 파이프라인</span>
                <span class="schematic-badge">Zero-Emulation Native Pipeline</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Legitimate User Asset Tier</div>
                  <div class="schematic-desc">
                    User-Owned Game Copy<br>
                    `exefs/main` (ARM64 ELF)<br>
                    `romfs/` (Textures, Models, Audio)<br>
                    ※ 저장소에 저작권 자산 0% 포함
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Recomp Tool &amp; LLVM Core</div>
                  <div class="schematic-desc">
                    Control Flow Graph (CFG) 분석<br>
                    ARM64 기계어 &rarr; Native C++ Code 변환<br>
                    NVN API &rarr; Vulkan 1.3 셰이더 매핑<br>
                    Clang/LLVM으로 `.exe` 즉시 컴파일
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">4K 144Hz PC Runtime</div>
                  <div class="schematic-desc">
                    순수 Windows 64비트 바이너리<br>
                    울트라와이드 21:9 &amp; 32:9 무수정 지원<br>
                    RTX DLSS 및 텍스처 업스케일러 주입<br>
                    가상화 오버헤드 0ms 무지연 구동
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Super Odyssey PC Recomp 공식 깃허브 저장소 및 빌드 인터페이스</span>
              </div>
              <img src="../assets/images/demo_odyssey_recomp.png" alt="Super Odyssey PC Recomp Live Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ GitHub 공식 저장소 뷰: "You must bring your own game. This project contains no game files, no game code, no assets and no keys." 합법적 클린룸 리버스 엔지니어링을 명시하며 정적 재컴파일 인스톨러 소스를 제공하는 화면.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 법적 분기점: 닌텐도 법무팀도 손댈 수 없는 '클린룸의 방패'
            </h3>
            <p>
              닌텐도는 그동안 Yuzu와 Ryujinx를 상대로 "스위치의 암호화 보안 조치(AES 키)를 우회하여 불법 복제를 조장했다"는 논리로 DMCA 압류를 관철시켰다. 에뮬레이터 코드 내에 포함된 BIOS 모사나 암호화 헤더 파싱 코드가 공격 대상이었다.
            </p>
            <p>
              하지만 <strong>정적 재컴파일러(Static Recompiler)</strong>는 법적으로 완전히 다른 차원에 서 있다:
            </p>
            <ul>
              <li><strong>저작권 코드 0% 원칙:</strong> 저장소에는 닌텐도의 독점 게임 엔진 코드, 텍스처, 사운드가 단 1바이트도 존재하지 않는다. 오직 사용자가 소유한 게임을 PC에서 읽어주는 순수 오픈소스 변환 도구만 배포된다.</li>
              <li><strong>미국 연방 판례의 비호:</strong> <em>Sega v. Accolade</em>(1992)와 <em>Sony v. Connectix</em>(2000) 판례는 "기존 하드웨어와의 상호 운용성을 확보하기 위한 클린룸 리버스 엔지니어링 및 바이너리 분석은 공정 이용(Fair Use)에 해당한다"고 명확히 판시했다.</li>
              <li><strong>암호화 우회 부재:</strong> 복호화된 정품 파일을 PC로 옮기는 것은 소비자의 사적 이용 권리이며, 재컴파일 툴 자체는 암호화 해킹 도구가 아니므로 DMCA 1201조(우회 금지 조항)에 저촉되지 않는다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 콘솔의 수명이 다해도 코드는 영원하다
            </h3>
            <p>
              스위치 후속 콘솔의 출시가 임박하면서 구형 하드웨어는 언젠가 서버가 꺼지고 단종의 길을 걷게 될 것이다. 그러나 오픈소스 엔지니어들이 완성한 정적 재컴파일러 덕분에, <em>슈퍼 마리오 오디세이</em>는 10년 뒤에도, 50년 뒤에도 최신 PC와 오픈 플랫폼 위에서 가장 찬란한 4K 144Hz의 모습으로 영구 보존될 것이다.
            </p>
            <p>
              거대 독점 기업이 법적 소송으로 에뮬레이터의 싹을 잘라내려 할 때마다, 오픈소스는 언제나 더 우아하고, 더 합법적이며, 기술적으로 더 완벽한 해답을 증명해내고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Super+Mario+Odyssey+PC+Recomp+gameplay" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/Simon3Sarkis/super-odyssey-pc-recomp" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
