# -*- coding: utf-8 -*-
# Story 5: tylertms/Stela

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 5] tylertms/Stela                                   -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_stela.jpg" alt="Stela Apple Silicon Layer Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="cpu" style="width:12px;height:12px;fill:#fff;"></i> ARCHITECTURE REVERSE</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#f1f5f9; border-color:#64748b; color:#334155;">🍏 애플 실리콘 PC 이식</span>
              <span class="platform-tag">GitHub Trending #1 (1.3k stars)</span>
              <span class="platform-tag">tylertms / Stela</span>
            </div>
            
            <h2 class="article-headline">
              애플 실리콘(M1~M4)의 성벽을 넘어 일반 x86 PC로: 'Stela' 오픈소스 호환 계층 — 맥OS ARM64 네이티브 바이너리와 Metal 셰이더를 인텔/AMD CPU에서 무수정 구동
            </h2>

            <div class="article-subheadline">
              UEFI 부트스트랩 레벨에서 ARM64 명령어를 x86-64로 실시간 트랜슬레이션하고, 독점 Metal API를 NVIDIA 지포스 Vulkan 드라이버로 변환하는 기적의 해커 프로젝트
            </div>
            <p class="article-snippet">
              애플이 인텔 x86 맥(Mac)에 대한 운영체제 지원을 공식 중단하고 자사 M시리즈 실리콘 칩으로 완전히 문을 걸어 잠그면서, 수십 년간 이어져 온 '해킨토시(Hackintosh)'의 시대는 완전히 끝난 것처럼 보였습니다. 그러나 오픈소스 시스템 엔지니어 타일러(Tyler)가 공개한 'Stela'는 인텔 및 AMD PC의 메인보드 UEFI 펌웨어 단에서 스스로를 'M2 Mac mini'로 완벽히 위장하고, ARM64 맥OS 커널과 독점 메탈(Metal) 그래픽스를 지포스 GPU 위에서 구동하는 불가능에 가까운 호환 계층을 선보였습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 애플이 닫아버린 성벽, 그 밑바닥을 뚫어낸 UEFI 부트로더
            </h3>
            <p>
              애플이 M1 칩을 시작으로 애플 실리콘(Apple Silicon) 독자 아키텍처로 완전 전환했을 때, 실리콘밸리는 "이제 일반 PC에서 맥OS를 구동하는 일은 물리적으로 불가능해졌다"고 단언했다. 
              명령어 집합이 x86에서 ARM64로 바뀐 것뿐만 아니라, 애플 독점 인터럽트 컨트롤러(AIC), 통합 메모리 아키텍처(UMA), 독점 시스템 관리 컨트롤러(SMC), 그리고 하드웨어 직결 Metal GPU 파이프라인이 칩셋 레벨에서 얽혀 있었기 때문이다.
            </p>
            <p>
              하지만 오늘, GitHub 트렌딩 1위에 오른 <strong>Stela(스텔라)</strong>는 컴퓨터 아키텍처 공학의 한계를 시험하며 전 세계 엔지니어들의 턱을 빠지게 만들었다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 일반 인텔 PC가 스스로를 'M2 Mac mini'라 믿게 만드는 마법
            </h3>
            <p>
              Stela는 일반적인 운영체제 위에서 실행되는 가상머신 앱이 아니다. PC 전원을 켜는 순간 마더보드의 UEFI 펌웨어가 가장 먼저 로드하는 <strong>베어메탈 사전 부트 프로그램(UEFI Bootloader Program)</strong>이다.
            </p>

            <div class="editorial-quote">
              <p>
                "Stela는 x86-64 PC를 위한 범용 애플 실리콘 호환 계층입니다. 
                <strong>우리는 UEFI 단계에서 ARM64-to-x86_64 바이너리 변환기를 주입하고, NVIDIA GPU를 위한 순수 Metal 드라이버를 로드하며, 애플 실리콘 하드웨어 레지스터 모델을 메모리에 직접 가상화합니다.</strong> 
                맥OS 커널은 자신이 쿠퍼티노 본사에서 조립된 정품 M2 Mac mini 위에서 돌고 있다고 확신하게 됩니다."
              </p>
              <small>— Tyler (tylertms), Stela 프로젝트 창립자 아키텍처 명세서</small>
            </div>

            <p>
              이 대담한 프로젝트가 공개되자마자 전 세계 해킨토시 포럼과 시스템 해커 커뮤니티는 열광했다. 죽어가던 PC 기반 맥OS 연구가 완전히 새로운 차원의 하드웨어 가상화 기술로 부활했기 때문이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 메커니즘: 베어메탈 JIT 트랜슬레이터와 Vulkan 기반 Metal 드라이버
            </h3>
            <p>
              Stela가 이뤄낸 기술적 성취는 시스템 프로그래밍의 정점에 닿아 있다:
            </p>
            <ul>
              <li><strong>UEFI Level ARM64-to-x86 Translation:</strong> OS 커널이 부팅되기 전 단계에서 ARM64 기계어 명령어를 가로채 최적화된 x86-64 마이크로 연산으로 즉시 변환. 페이징 테이블과 메모리 모델(TSO vs Weak Memory) 불일치를 하드웨어 페이징 레벨에서 조정.</li>
              <li><strong>Apple Silicon Hardware Emulation:</strong> 애플 독점의 AIC(Apple Interrupt Controller), DART(IOMMU), NVRAM, Mailbox 통신 레지스터를 완벽히 모사하여 XNU 커널의 하드웨어 무결성 체크를 통과.</li>
              <li><strong>NVIDIA Metal-to-Vulkan Driver:</strong> 애플 실리콘의 독점 Metal 그래픽 API 호출을 NVIDIA 지포스 드라이버가 이해할 수 있는 Vulkan 1.3 셰이더와 커맨드 버퍼로 나노초 단위 변환.</li>
              <li><strong>Native Peripheral Passthrough:</strong> 표준 PCIe NVMe SSD와 USB xHCI 컨트롤러를 애플 실리콘 내부 버스로 직결하여 저장장치 I/O 병목 해소.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Stela x86-64 &rarr; Apple Silicon 가상화 레이어</span>
                <span class="schematic-badge">Bare-Metal UEFI Translation Core</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Pure macOS ARM64 Kernel</div>
                  <div class="schematic-desc">
                    Vanilla macOS (M2 Target)<br>
                    Mach Kernel &amp; BSD Subsystem<br>
                    Metal 3 Framework &amp; CoreFoundation<br>
                    ※ 바이너리 변조 0% 순정 부팅
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Stela Compatibility Layer (UEFI)</div>
                  <div class="schematic-desc">
                    ARM64 &rarr; x86-64 Fast Translation<br>
                    AIC Interrupt &amp; SMC Hardware Model<br>
                    Metal &rarr; Vulkan/NVIDIA Direct Translation<br>
                    Host PC를 'M2 Mac mini'로 가상화
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Standard PC Hardware</div>
                  <div class="schematic-desc">
                    Intel Core / AMD Ryzen CPU<br>
                    NVIDIA GeForce RTX GPU<br>
                    Standard PCIe NVMe &amp; DDR5 RAM<br>
                    하드웨어 독점 성벽 완벽 돌파
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Stela 공식 깃허브 저장소 및 아키텍처 다큐멘테이션</span>
              </div>
              <img src="../assets/images/demo_stela.png" alt="Stela Live Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ GitHub 공식 저장소 뷰: "A general purpose Apple Silicon layer for x86-64 PCs. It is a UEFI boot program with an arm64-to-x86-64 translator, a Metal driver for NVIDIA GPUs and a model of Apple silicon hardware. Stela currently presents itself as an M2 Mac mini."
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 법적 분기점: '월드 가든'의 철옹성과 오픈 아키텍처의 줄다리기
            </h3>
            <p>
              애플의 강력한 비즈니스 해자는 하드웨어와 소프트웨어를 완벽히 수직 통합한 폐쇄형 생태계('Walled Garden')에서 나온다. 
              소비자가 맥OS의 완성도 높은 사용자 경험을 누리려면 반드시 애플의 비싼 독점 하드웨어를 구매해야만 했다.
            </p>
            <p>
              Stela는 이 인위적인 벽에 의문을 던진다. 저작권이 있는 애플의 독점 바이너리를 수정하거나 배포하지 않고, 
              순수하게 컴퓨터 하드웨어 인터페이스를 기술적으로 해석하고 번역하는 오픈소스 호환 계층을 구축함으로써, 
              과거 IBM PC 호환 기종들이 피닉스(Phoenix) 바이오스를 통해 탄생했던 역사를 2026년의 실리콘 위에서 재현하고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 성벽을 넘는 해커의 호기심
            </h3>
            <p>
              비록 아직 초기 개발 단계라 부팅 속도가 느리고 해결해야 할 버그가 산적해 있지만, Stela가 던지는 메시지는 명확하다.
            </p>
            <p>
              기업이 아무리 높고 단단한 하드웨어 성벽을 쌓아 올린다 해도, 인간의 지적 호기심과 오픈소스 엔지니어들의 끈질긴 리버스 엔지니어링 열정 앞에서는 그 어떤 폐쇄적 아키텍처도 영원히 닫혀 있을 수 없다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Stela+Apple+Silicon+layer+PC+Hackintosh" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/tylertms/Stela" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
