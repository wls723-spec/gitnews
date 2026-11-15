# -*- coding: utf-8 -*-
# Story 3: martin-olivier/airgorah

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] martin-olivier/airgorah                          -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_airgorah.jpg" alt="Airgorah WiFi Security Auditor Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="shield" style="width:12px;height:12px;fill:#fff;"></i> RUST SECURITY</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#ffedd5; border-color:#ea580c; color:#9a3412;">📡 Rust + GTK4 최소권한 WiFi 감사</span>
              <span class="platform-tag">GitHub Rust Trending #1</span>
              <span class="platform-tag">martin-olivier / airgorah</span>
            </div>
            
            <h2 class="article-headline">
              20년 묵은 `aircrack-ng` 터미널을 밀어내는 순수 Rust의 반격 'Airgorah': "일반 유저 권한 GTK4 GUI와 `polkit` 특권 에이전트 분리로 무선 보안 감사를 재설계하다"
            </h2>

            <div class="article-subheadline">
              무선 랜카드 모니터 모드 기반 주변 AP·클라이언트 실시간 탐지부터 핸드셰이크·PMKID 포획 및 크래킹까지, X11·Wayland 네이티브 환경에서 6,242 스타를 돌파한 Rust 보안 감사 툴
            </div>
            <p class="article-snippet">
              리눅스에서 무선 네트워크 보안 점검을 하려면 지금도 수십 개의 `airodump-ng`, `aireplay-ng` 터미널 창을 열어두고 전체 GUI까지 `sudo` 루트 권한으로 띄워야 하는 구시대적 위험을 감수해야 했습니다. Rust 트렌딩 1위에 오른 `Airgorah`는 GTK4 기반의 직관적인 실시간 모니터링 GUI는 일반 사용자 권한으로 분리하고, 패킷 인젝션이 필요한 순간에만 `polkit`으로 최소 특권 에이전트(`airgorah-agent`)를 깨우는 현대적 보안 설계로 레드팀·인프라 감사자들의 환호를 받고 있습니다.
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
              <i data-lucide="flame"></i> 1. 리드: `sudo`로 GUI를 통째로 띄우던 20년 묵은 무선 보안 관행의 종언
            </h3>
            <p>
              모의해킹과 기업 무선랜 감사 현장에서 `aircrack-ng` 스위트는 20년 넘게 절대적인 표준이었다. 하지만 엔지니어의 책상 위에는 언제나 검은 터미널 창 대여섯 개가 겹쳐 열려 있었고, 어느 AP에 몇 번 클라이언트가 붙었는지, 4-Way 핸드셰이크나 PMKID가 포획됐는지 눈을 부릅뜨고 텍스트 테이블을 대조해야 했다. 더 나쁜 것은 일부 래퍼(Wrapper) GUI 도구들이 편의성을 이유로 거대한 그래픽 렌더링 스택 전체를 `root` 권한으로 실행해 Wayland 보안 모델을 정면으로 깨뜨린다는 점이었다.
            </p>
            <p>
              오늘 하루 708개의 스타를 추가하며 GitHub Rust 일간 트렌딩 정상(총 <strong>6,242 스타</strong>)에 오른 <strong>martin-olivier/airgorah</strong>(v0.9.0, MIT 라이선스)는 이 낡은 관행을 99.6% 순수 Rust 코드베이스와 GTK4 네이티브 UI로 깔끔하게 갈아엎었다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 메모리 안전성 + 특권 분리(`polkit`)가 만난 차세대 보안 도구
            </h3>
            <p>
              보안 감사 도구가 아이러니하게도 C 언어 메모리 취약점과 과도한 루트 권한으로 공격 표면(Attack Surface)이 되어선 안 된다. Airgorah는 데스크톱 애플리케이션이 어떻게 시스템 특권을 다뤄야 하는지 교과서적인 아키텍처를 보여준다.
            </p>

            <div class="editorial-quote">
              <p>
                "그래픽 인터페이스(GTK4)는 <strong>철저히 일반 사용자(Normal User) 권한으로 X11과 Wayland 위에서 구동되며, 무선 패킷 캡처나 디인증 등 특권 작업이 필요한 순간에만 `polkit` 인증을 통해 소형 특권 에이전트(`airgorah-agent`)를 별도 실행</strong>한다."
              </p>
              <small>— martin-olivier/airgorah v0.9.0 특권 분리(Privilege Separation) 설계 명세</small>
            </div>

            <p>
              단 한 번의 `polkit` 인증 프롬프트만으로 무거운 GUI 프레임워크는 비특권 샌드박스 안에 머물고, 실제 무선 인터페이스(`monitor mode`, `packet injection`) 제어만 작고 감사 가능한 Rust 에이전트 바이너리가 전담하는 구조다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 비특권 GTK4 뷰어와 특권 `airgorah-agent`의 이원화 파이프라인
            </h3>
            <p>
              Airgorah v0.9.0은 외부 `aircrack-ng` 의존성마저 선택 사항(Optional)으로 낮추며 자체적인 무선 감사 워크플로우를 구축했다:
            </p>
            <ul>
              <li><strong>이원화된 프로세스 격리 (GUI vs `airgorah-agent`):</strong> `gtk4-rs` 기반의 프론트엔드 프로세스는 일반 유저 권한으로 실행되어 ESSID, BSSID, 주파수 대역(2.4GHz / 5GHz), 채널, 신호 세기(dBm), 암호화 방식(WPA2/WPA3), 연결된 스테이션 MAC 테이블을 실시간 렌더링한다.</li>
              <li><strong>원클릭 핸드셰이크 &amp; PMKID 감사 파이프라인:</strong> 모니터 모드와 패킷 인젝션을 지원하는 무선 랜카드를 연결하면, GUI 상단 툴바에서 채널 대역을 필터링하고 특정 AP의 연결 클라이언트 목록과 프로브 요청(Probes)을 즉시 조회한다. 필요 시 디인증(Deauthentication) 프레임을 송신해 4-Way 핸드셰이크나 PMKID 캡처 여부를 체크박스 아이콘으로 즉각 확인하며, 내장 크래킹 워크플로우로 암호 강도를 검증한다.</li>
              <li><strong>현대적 리눅스 패키징과 경량화:</strong> Arch Linux AUR(`airgorah`), `crates.io`, `.deb`/`.rpm` 패키지 등 네이티브 배포 체계를 갖췄으며, X11뿐만 아니라 권한 상승된 GUI 실행을 차단하는 최신 Wayland 컴포지터에서도 아무런 우회 설정 없이 매끄럽게 동작한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Airgorah 특권 분리(Privilege Separation) 무선 보안 감사 아키텍처</span>
                <span class="schematic-badge">Rust · GTK4 · Polkit Agent</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Unprivileged GTK4 GUI</div>
                  <div class="schematic-desc">
                    일반 사용자 권한 실행 (X11 &amp; Wayland)<br>
                    AP 목록(ESSID·채널·WPA2/WPA3) 시각화<br>
                    연결 스테이션 MAC · 프로브 실시간 탐색<br>
                    핸드셰이크 / PMKID 포획 상태 직관 표시
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Polkit Privilege Gate</div>
                  <div class="schematic-desc">
                    최초 1회 시스템 정책 기반 권한 승인<br>
                    GUI 렌더링 스택의 `root` 노출 원천 차단<br>
                    명령 채널과 화면 렌더링 계층 엄격 분리<br>
                    99.6% 메모리 안전 Rust 코드베이스
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Privileged `airgorah-agent`</div>
                  <div class="schematic-desc">
                    무선 랜카드 Monitor Mode 전환 제어<br>
                    2.4GHz / 5GHz 채널 호핑 및 패킷 캡처<br>
                    패킷 인젝션(Deauth) &amp; PMKID 수집<br>
                    포획 패킷 암호 강도 감사(Cracking) 연계
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">Airgorah GTK4 실구동 보안 감사 인터페이스 (martin-olivier/airgorah)</span>
              </div>
              <img src="../assets/images/demo_airgorah.png" alt="Airgorah GTK4 WiFi Security Auditing Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ Airgorah v0.9.0 실구동 UI 화면: 상단 패널에서 2.4GHz·5GHz 대역과 채널 필터를 실시간 제어하며, 하단 듀얼 테이블로 주변 AP의 암호화 규격·신호 강도·연결 클라이언트·핸드셰이크/PMKID 수집 여부를 한눈에 감사한다.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 법적 경계 및 보안 생태계 시사점: 도구의 현대화와 윤리적 감사 기준
            </h3>
            <p>
              무선 보안 도구가 터미널의 장벽을 벗어나 이토록 세련된 GUI를 갖추게 되면, 자연스럽게 오용 가능성과 법적 책임의 경계도 함께 날카로워진다.
            </p>
            <ul>
              <li><strong>명확한 합법적 감사 경계:</strong> 개발자 Martin Olivier는 저장소 전면에 "Airgorah는 오직 자신이 소유하거나 명시적 테스트 권한을 위임받은 네트워크의 취약점을 점검하기 위한 도구이며, 비인가 WiFi 네트워크에 대한 공격은 대부분 국가에서 불법"임을 분명히 못 박고 있다.</li>
              <li><strong>C에서 Rust로 이동하는 보안 툴체인:</strong> 패킷 파서와 무선 드라이버 제어부는 외부에서 유입되는 악성 비콘(Beacon) 프레임에 직접 노출되는 영역이다. 그동안 C/C++ 기반 네트워크 툴에서 빈번했던 버퍼 오버플로 위험을 Rust의 소유권 모델과 `polkit` 에이전트 분리가 동시에 방어하며, 오픈소스 보안 감사 생태계의 세대교체를 증명하고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 가장 강력한 해킹 도구는 가장 엄격한 권한 설계에서 나온다
            </h3>
            <p>
              수십 년간 보안 전문가들은 "강력한 로우레벨 도구일수록 인터페이스는 거칠고 권한은 무제한이어야 한다"는 고정관념을 당연시해왔다.
            </p>
            <p>
              Airgorah는 그 편견을 깼다. 최소 권한 원칙을 지키면서도 Wayland 데스크톱 위에서 터미널보다 빠르고 명확하게 무선 전파 공간을 해부하는 이 Rust 도구는, 2026년 오픈소스 시스템 엔지니어링이 얼마나 성숙했는지 보여주는 작은 기념비다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=Airgorah+WiFi+security+Rust+GTK4" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/martin-olivier/airgorah" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
