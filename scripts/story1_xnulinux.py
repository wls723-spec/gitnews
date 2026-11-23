# -*- coding: utf-8 -*-
# Story 1: AFK-surf/xnulinux (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] AFK-surf/xnulinux : COVER STORY                   -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_xnulinux.jpg" alt="xnulinux XNU Kernel Module Inside Linux Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> COVER EXPLOSION #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🐧 하이퍼바이저 없이 리눅스 커널에 macOS 커널을 직결 · HN 587점 · ★1,926</span>
              <span class="platform-tag">Hacker News Top &amp; Kernel Hack</span>
              <span class="platform-tag">AFK-surf / xnulinux</span>
            </div>

            <h2 class="main-lead-headline">
              <span id="hero-title">"리눅스 커널 안에 macOS 커널을 통째로 꽂아 넣었다" — 하이퍼바이저 없이 Safari·Finder까지 부팅한 'xnulinux'</span>
            </h2>

            <div class="article-subheadline">
              Apple 공개 소스 기반 XNU(xnu.ko, APSL-2.0)와 외래 커널 인터페이스(fki.ko, GPL-2.0-only)를 수정 없는 arm64 리눅스 커널에 insmod로 적재해 CPU·MMU 직접 구동, NVIDIA DGX Spark 베어메탈 및 krunkit(metal2vulkan+Mesa Venus)에서 macOS 27.2.1 데스크톱 31~48초 부팅 실증 (★1,926)
            </div>
            <p class="article-snippet">
              가상머신(VM)도, QEMU 에뮬레이터도, API 변환 계층(Darling)도 아닙니다. 개발자 Heyang Zhou와 기여자들이 공개한 <strong>AFK-surf/xnulinux</strong>는 애플이 오픈소스로 공개한 XNU 커널을 <code>xnu.ko</code>라는 리눅스 커널 모듈로 컴파일해 순정 arm64 Ubuntu/Linux 7.0 커널 내부에 <code>insmod</code>로 직접 로딩합니다. 오늘 해커뉴스(<strong>587점·댓글 242개</strong>)와 GitHub(<strong>★1,926</strong>)을 동시에 강타한 이 프로젝트는 베어메탈 <strong>NVIDIA DGX Spark</strong> 리눅스 머신 위에서 실제 macOS 27.2.1의 <code>WindowServer</code>, Dock, Finder, Safari, Chrome을 부팅해 내며 '애플 실리콘 하드웨어 락인'의 공학적 전제를 정면으로 흔들었습니다.
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
              <i data-lucide="flame"></i> 1. 리드: NVIDIA DGX Spark 위에서 켜진 '금단의 macOS 데스크톱'
            </h3>
            <p>
              오늘 새벽 해커뉴스 1면을 장식한 스크린샷 한 장이 시스템 프로그래머들의 시선을 못 박았다. 왼쪽 창에는 <code>sw_vers</code>가 출력한 <strong>macOS Golden Gate 27.2.1</strong>과 <code>WindowServer</code>, Dock, Finder가 떠 있고, 바로 오른쪽 Safari와 터미널 창에는 그 macOS가 얹혀 돌아가는 호스트 <strong>Ubuntu 24.04.5 LTS(Linux 7.0.0-1025-nvidia, 베어메탈 NVIDIA DGX Spark)</strong>로의 SSH 세션이 열려 있었다. <code>lsmod</code> 출력창에는 두 개의 낯선 커널 모듈 이름—<code>xnu</code>와 <code>fki</code>—이 나란히 찍혀 있었다.
            </p>
            <p>
              지금까지 리눅스 위에서 macOS 앱을 돌리려는 시도는 크게 두 갈래였다. 하나는 KVM/QEMU 위에 하드웨어 전체를 가상화해 macOS를 게스트 OS로 띄우는 무거운 하이퍼바이저 방식이고, 다른 하나는 Wine처럼 Mach/BSD 시스템 콜을 유저스페이스에서 흉내 내는 방식(Darling)이었다. <strong>xnulinux</strong>는 이 두 가지 상식을 모두 건너뛰었다. <strong>수정하지 않은 순정 arm64 리눅스 커널의 커널 공간(Ring/EL1) 바로 안으로 XNU 커널 자체를 적재(<code>insmod xnu.ko</code>)해, 두 개의 운영체제 커널이 동일한 CPU와 MMU 위에서 나란히 호흡하도록 만든 것이다.</strong>
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "가상화 없는 이중 커널 공존, 애플 하드웨어 독점의 경계선을 긋다"
            </h3>
            <p>
              왜 <code>xnulinux</code>가 단순한 주말 취미 해킹을 넘어 OS 아키텍처와 빅테크 플랫폼 권력 구도에서 거대한 충격을 주는지 이해하려면, 애플이 Mac 생태계를 통제하는 방식을 봐야 한다. macOS의 사용자 공간(GUI, WindowServer, Safari, Metal, AMFI)은 철저히 애플 실리콘(M 시리즈)과 애플 부트로더(iBoot)의 물리적 결합 위에 잠겨 있다.
            </p>

            <div class="editorial-quote">
              <p>
                "호스트된 XNU는 CPU와 MMU를 직접 구동하므로, macOS 프로세스는 중간 하이퍼바이저 없이 리눅스 프로세스와 같은 CPU 위에서 네이티브로 실행된다. <strong>순정 Ubuntu 커널 위에서 insmod xnu.ko 한 번으로 애플 인스톨러가 만든 macOS 27 시스템 디스크가 31~48초 만에 로그인 창과 Safari·Chrome까지 부팅된다.</strong>"
              </p>
              <small>— AFK-surf/xnulinux 공식 아키텍처 명세 (APSL-2.0 / GPL-2.0-only 이중 경계)</small>
            </div>

            <p>
              실제로 Apple Silicon 맥 내부의 <code>krunkit</code> arm64 리눅스 VM에서 테스트한 결과, <code>xnulinux</code>의 부팅 시간은 <strong>31~48초</strong>로 동일 장비의 애플 공식 Virtualization 프레임워크 macOS VM(49초)과 맞먹는 속도를 기록했다. 40라운드에 걸친 Safari·Notes·Calculator·TextEdit·System Settings·Spotlight 스트레스 테스트도 30분간 커널 패닉이나 크래시 리포트 없이 완주했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: FKI(외래 커널 인터페이스)와 Metal→Vulkan DRM 브리지 해부
            </h3>
            <p>
              리눅스 커널(GPL)과 XNU 커널(APSL)을 충돌 없이 한 지붕 아래 동거시키기 위해 <code>xnulinux</code>는 정교한 4계층 인터페이스를 설계했다:
            </p>
            <ul>
              <li><strong>CPU와 예외 벡터 공유(Pinned Kernel Threads + <code>fki.ko</code>):</strong> 호스트된 각각의 XNU CPU는 특정 리눅스 물리 CPU에 고정된 리눅스 커널 스레드로 동작한다. XNU는 유휴 상태, I/O, 타이머를 요청할 때까지 CPU를 직접 점유하며, 리눅스가 자체 예외 벡터를 유지한 채 XNU 코드에서 발생한 페이지 폴트와 유저 예외만 <code>fki.ko</code>(Foreign Kernel Interface)가 가로채 XNU 핸들러로 포워딩한다.</li>
              <li><strong>CMA 연속 메모리 &amp; 4K 페이지 주소 공간 정렬:</strong> XNU는 리눅스 커널의 CMA(Contiguous Memory Allocator)로부터 물리적으로 연속된 메모리 블록(예: 8 GiB)을 임대해 자체 <code>pmap</code>으로 관리한다. macOS <code>PAC(Pointer Authentication)</code> 및 4K 페이지(macOS-DroidVM 기반 4K 페이지 XNU 패치) 유저 주소 공간을 리눅스와 양분하여 하이퍼바이저 VM-Exit 오버헤드 없이 컨텍스트를 전환한다.</li>
              <li><strong>Metal → <code>metal2vulkan</code> → Mesa Venus DRM 브리지:</strong> 그래픽 가속은 <code>gpu/xnu-cpu-metal</code>이 macOS Metal 호출을 Vulkan으로 번역하고, <code>kexts/XnuDrm</code>이 호스트 콜을 통해 리눅스 유저스페이스 데몬 <code>gpu/xnu-drm/xnudrmd</code>와 리눅스 렌더 노드로 전달해 Mesa Venus(<code>Virtio-GPU Venus</code>)로 하드웨어 가속한다. 지원 백엔드가 없는 베어메탈 DGX Spark 등에서는 Mesa <code>lavapipe</code> CPU 렌더링(<code>GPU=off</code>)으로 자동 폴백한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">xnulinux 이중 커널 공존(xnu.ko ↔ fki.ko) 및 Metal-to-Vulkan 브리지 구조</span>
                <span class="schematic-badge">arm64 Linux 7.0 · XNU-12377.121.6 · Zero Hypervisor</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Hosted macOS 27 Userspace</div>
                  <div class="schematic-desc">
                    <code>launchd</code> · <code>WindowServer</code> · Dock · Finder<br>
                    Safari · Chrome · Apple 순정 시스템 디스크<br>
                    <code>XnuDisplay</code>·<code>XnuEthernet</code>·<code>XnuInput</code> Kext<br>
                    <code>metal2vulkan</code> 기반 Metal GPU 프론트엔드
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. APSL ↔ GPL ABI Boundary</div>
                  <div class="schematic-desc">
                    <code>xnu.ko</code> (APSL-2.0): XNU <code>LINUX64</code> 머신 계층<br>
                    <code>linux64_abi.h</code> 호스트 콜 규약 준수<br>
                    <code>fki.ko</code> (GPL-2.0-only): CPU·CMA·Fault·IPI 중계<br>
                    리눅스 커널 헤더 비침투 라이선스 경계 분리
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Stock arm64 Linux Host</div>
                  <div class="schematic-desc">
                    무수정 Ubuntu/Linux 7.0 (4K Pages + PAC)<br>
                    <code>xnudrmd</code> → <code>/dev/dri/renderD*</code> Venus 브리지<br>
                    미지원 시 Mesa <code>lavapipe</code> CPU 폴백<br>
                    <code>xnulinux.service</code> systemd 데몬 자동 복구
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">AFK-surf/xnulinux 저장소 실화면 — 리눅스 커널 위에서 동시 구동되는 macOS 27.2.1 데스크톱 &amp; Ubuntu 7.0 SSH</span>
              </div>
              <img src="../assets/images/demo_xnulinux.png" alt="AFK-surf xnulinux GitHub Repository Showcase" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/AFK-surf/xnulinux 실화면: 동일 arm64 리눅스 시스템(Ubuntu, Linux 7.0) 내부에서 xnu.ko와 fki.ko 모듈을 적재해 WindowServer·Dock·Finder·Safari 및 베어메탈 NVIDIA DGX Spark 데스크톱을 부팅한 아키텍처 실증.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 법적·라이선스 경계: APSL과 GPL-2.0을 가른 외과수술적 ABI 설계
            </h3>
            <p>
              <code>xnulinux</code> 코드베이스에서 커널 해커들이 가장 감탄한 대목은 기술적 구현만큼이나 치밀한 <strong>라이선스 및 저작권 방화벽</strong>이다. 리눅스 커널의 <code>GPL-2.0-only</code>와 애플 XNU의 <code>APSL-2.0</code>은 직접 결합할 수 없는 양립 불가(Incompatible) 라이선스다. 또한 애플의 macOS EULA는 비애플 하드웨어에서의 macOS 바이너리 실행을 엄격히 제한한다.
            </p>
            <ul>
              <li><strong><code>xnu.ko</code> vs <code>fki.ko</code> 엄격한 심볼 분리:</strong> 제작자는 GPL 측(<code>fki-ko/</code>, <code>linux/</code>)과 APSL 측(<code>xnu-ko/</code>, <code>xnu-patches/</code>, <code>kexts/</code>) 사이에 <code>linux64_abi.h</code>와 <code>fki_*</code>라는 얇은 외래 커널 인터페이스를 세웠다. <code>xnu.ko</code>는 리눅스 커널 헤더를 일절 인클루드하지 않고 <code>MODULE_LICENSE("Proprietary")</code>(ZFS와 동일한 비GPL 커널 모듈 방식)로 적재되며 오직 <code>fki_*</code> 심볼만 호출한다.</li>
              <li><strong>애플 바이너리 Zero-Distribution 원칙:</strong> 저장소에는 애플의 사유 바이너리나 kext, 트러스트 캐시, 시스템 디스크가 단 1바이트도 포함되지 않는다. 사용자가 자신의 합법적 Mac 및 Xcode 환경에서 <code>scripts/mk-macvm-disk.sh</code>로 생성한 macOS 27 디스크를 가져와 빌드 시점에 병합하도록 설계해 저작권 배포 리스크를 원천 차단했다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: OS의 경계는 하드웨어가 아니라 인터페이스가 결정한다
            </h3>
            <p>
              아직 OS 크립텍스(Cryptex)를 시스템 볼륨에 병합해야 하고 AMFI 패치와 4K 페이지 메모리 지연 같은 과제가 남아 있지만, <code>xnulinux</code>가 쏘아 올린 신호탄은 분명하다. arm64라는 공통 명령어셋 위에서 리눅스와 macOS를 가로막고 있던 것은 물리 법칙이 아니라 커널 ABI의 장벽뿐이었다.
            </p>
            <p>
              엔비디아의 arm64 워크스테이션(DGX Spark) 위에서 맥 OS의 WindowServer가 아무렇지 않게 부팅되는 이 낯선 풍경은, 미래의 서버와 워크스테이션이 특정 벤더의 껍데기를 넘어 커널 모듈 단위로 이종 OS를 조립해 쓰는 시대의 서막을 예고하고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=xnulinux+xnu.ko+macos+on+linux" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/AFK-surf/xnulinux" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
