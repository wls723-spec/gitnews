# -*- coding: utf-8 -*-
# Story 1: HolyArrs/HolyArrs (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] HolyArrs/HolyArrs : 오늘의 메인 기사 (COVER STORY) -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_holyarrs.jpg" alt="HolyArrs All-in-One Media Server" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔥 15MB 단일 바이너리로 6개 미디어 앱 통합</span>
              <span class="platform-tag">HN Hot & GitHub Trending</span>
              <span class="platform-tag">HolyArrs / HolyArrs</span>
            </div>
            
            <h2 class="main-lead-headline">
              <span id="hero-title">15MB 단일 바이너리로 넷플릭스와 스포티파이의 제국을 거실에 세우다 — 'HolyArrs', 6개 컨테이너 지옥을 단칼에 베어 넘긴 홈서버 혁명</span>
            </h2>

            <div class="article-subheadline">
              Plex·Jellyfin·Sonarr·Radarr·qBittorrent를 합친 718MB 도커 생태계를 단 15MB 바이너리와 140MB 유휴 RAM으로 완벽 대체하는 차세대 셀프호스팅 미디어 OS
            </div>
            <p class="article-snippet">
              스트리밍 플랫폼들의 끝없는 구독료 인상과 콘텐츠 파편화에 지친 홈랩(Homelab) 유저들을 괴롭혀 온 것은 다름 아닌 '설정 지옥'이었습니다. 영화 하나를 보려고 도커 컨테이너 6개를 띄우고 포트와 볼륨을 매핑하던 복잡성을 단 15MB 단일 바이너리로 압축한 'HolyArrs'가 전 세계 해커뉴스와 깃허브를 강타했습니다. 10,000편의 미디어를 인덱싱하고도 단 140MB 메모리만 소모하며, 넷플릭스급 웹 UI와 온더플라이 하드웨어 트랜스코딩을 제공합니다.
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
              <i data-lucide="flame"></i> 1. 리드: "드라마 한 편 보려고 도커 6개를 띄워야 합니까?"
            </h3>
            <p>
              거실 소파에 앉아 TV 리모컨을 쥐기까지, 오픈소스 홈서버 애호가들이 감내해야 했던 고통은 가혹했다. 
              Plex나 Jellyfin으로 재생 서버를 세우고, 영화를 수집하기 위해 Radarr, TV 시리즈를 위해 Sonarr, 
              음악을 위해 Lidarr, 인덱서를 위해 Prowlarr, 그리고 백그라운드 다운로더인 qBittorrent까지. 
              최소 6개의 독립 컨테이너가 복잡한 YAML 파일과 네트워크 브리지로 얽혀 돌아가야만 비로소 '자가호스팅 넷플릭스'가 완성됐다.
            </p>
            <p>
              그렇게 띄운 컨테이너 이미지 크기만 도합 718.2MB, 유휴 상태에서 갉아먹는 RAM만 수 기가바이트에 달했다. 
              "내가 엔지니어링 공부를 하려는 건지, 드라마를 보려는 건지 모르겠다"는 한탄이 레딧 홈랩 커뮤니티의 오랜 레퍼토리였다. 
              하지만 오늘, 이 모든 번잡한 컨테이너 생태계를 단 하나의 15MB Go 바이너리로 집약한 <strong>HolyArrs</strong>가 등장하며 판도를 뒤흔들었다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 왜 홈랩 생태계가 15MB 바이너리에 열광하는가
            </h3>
            <p>
              거대 스트리밍 빅테크(넷플릭스, 디즈니+, 스포티파이)는 매년 구독 요금을 올리고 계정 공유를 금지하며 사용자를 옥죄고 있다. 
              반면 자가호스팅의 상징이던 Plex마저 상용 계정 인증을 강제하고 원격 접속을 중앙 서버에 종속시키며 커뮤니티의 신뢰를 잃었다. 
              독자적인 미디어 주권을 지키고 싶지만 복잡한 서버 관리에 지친 수백만 사용자에게 HolyArrs는 완벽한 해답을 제시한다.
            </p>

            <div class="editorial-quote">
              <p>
                "우리는 드라마 한 편을 검색하고 감상하기 위해 6개의 서로 다른 웹 UI를 오가며 API 키를 복사해 붙여넣는 일에 진절머리가 났다. 
                <strong>HolyArrs는 단 하나의 15MB 바이너리를 실행하는 순간, 브라우징부터 메타데이터 파싱, 다운로드, 트랜스코딩까지 단일 프로세스 안에서 유기적으로 처리한다.</strong> 
                라즈베리 파이든 구형 노트북이든 140MB RAM만 있으면 당신의 거실이 완벽한 넷플릭스가 된다."
              </p>
              <small>— HolyArrs 창립 선언문 및 해커뉴스 쇼케이스</small>
            </div>

            <p>
              사용자는 더 이상 포트 번호 8989(Sonarr), 7878(Radarr), 8096(Jellyfin)을 외울 필요가 없다. 
              하나의 모던 웹 인터페이스에서 콘텐츠를 검색하고 클릭하면, 내부 임베디드 오케스트레이터가 알아서 인덱서를 조회하고 라이브러리에 정리해 즉시 재생 화면으로 안내한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 메커니즘: 임베디드 Go 런타임과 단일 메모리 파이프라인
            </h3>
            <p>
              어떻게 700MB가 넘는 거대한 6개 마이크로서비스를 단 15MB 바이너리 안에 우겨넣을 수 있었을까? 
              HolyArrs는 웹 프레임워크와 데이터베이스, 미디어 파이프라인 전반을 바닥부터 재설계했다:
            </p>
            <ul>
              <li><strong>Zero-Dependency 임베디드 아키텍처:</strong> 외장 데이터베이스(PostgreSQL, MySQL)나 Node.js 런타임에 의존하지 않고, 단일 Go 정적 바이너리 내부에 SQLite3 엔진과 압축된 WebAssembly 프론트엔드 에셋을 완전히 임베딩.</li>
              <li><strong>인프로세스 이벤트 버스 (In-Process Pipeline):</strong> 컨테이너 간 무거운 HTTP/REST 통신 대신 초고속 Go 채널(Channel)을 통해 메타데이터 수집, 다운로드 큐, 미디어 파일 인덱싱을 나노초 단위로 동기화.</li>
              <li><strong>온더플라이(On-the-fly) 하드웨어 트랜스코딩:</strong> Intel QuickSync, NVENC, Apple VideoToolbox를 네이티브 바인딩으로 직접 호출하여 CPU 부하 없이 4K HDR 영상을 1080p 저대역폭 스트림으로 실시간 변환.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">HolyArrs 올인원 단일 바이너리(15MB) 내부 구조도</span>
                <span class="schematic-badge">Single Binary Architecture</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Client Tier (Embedded)</div>
                  <div class="schematic-desc">
                    단일 포트 모던 스트리밍 UI<br>
                    반응형 모바일 & TV 브라우저 지원<br>
                    트레일러 프리뷰 & 메타데이터 렌더
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">Core Engine (Go Runtime)</div>
                  <div class="schematic-desc">
                    내장 SQLite3 초경량 인덱서<br>
                    인프로세스 다운로드 & 큐 매니저<br>
                    10,000편 미디어 로드 시 140MB RAM 유지
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Media Pipeline</div>
                  <div class="schematic-desc">
                    HW 가속 온더플라이 트랜스코딩<br>
                    Direct Play 및 HLS 적응형 스트리밍<br>
                    멀티 플랫폼 (amd64, arm64, armv7)
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">HolyArrs 공식 웹 데모 및 통합 스트리밍 대시보드</span>
              </div>
              <img src="../assets/images/demo_holyarrs.png" alt="HolyArrs Live Dashboard" class="showcase-img">
              <p class="showcase-caption">
                ▲ holyarrs.com 공식 런타임 뷰: 넷플릭스를 연상시키는 세련된 탐색 UI에서 영화·드라마를 검색하고 호버 시 자동 재생되는 예고편과 1클릭 라이브러리 추가 인터페이스 구동 화면.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 법적 분기점: 스트리밍 분절화와 사적 복제
            </h3>
            <p>
              HolyArrs의 파괴력은 단순한 '엔지니어링 경량화'를 넘어선다. 
              글로벌 미디어 공룡들이 저작권을 무기로 콘텐츠를 쪼개 팔고 가격을 2~3배씩 올리는 '스트림플레이션(Streamflation)' 시대에, 
              개인이 직접 소유한 물리 미디어와 디지털 보관소를 합법적인 사적 복제 범위 내에서 가장 우아하게 향유할 수 있는 방파제를 구축했기 때문이다.
            </p>
            <p>
              동시에 중앙 서버를 거치지 않고 내 방의 NAS나 미니 PC에서 순수 P2P로 구동되므로, 
              외부 클라우드 서비스의 장애나 계정 영구 정지 리스크로부터 100% 면역된 데이터 주권을 보장한다. 
              AGPL-3.0 라이선스로 영구적인 오픈소스화를 선언하며 상용화 변심의 여지를 원천 차단했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 복잡함이 미덕이던 시대의 종언
            </h3>
            <p>
              그동안 홈랩 커뮤니티는 복잡한 쿠버네티스 클러스터를 띄우고 수십 개의 환경 변수를 조율하는 것을 일종의 '훈장'처럼 여겨왔다. 
              그러나 소프트웨어의 본질은 사용자의 삶을 간결하게 만드는 데 있다. 
              단 15MB의 작은 바이너리 하나로 거대한 상용 스트리밍 서비스에 맞서는 HolyArrs는, 
              기술이 진정으로 지향해야 할 미니멀리즘과 오픈소스의 승리를 증명하고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=HolyArrs+self+hosted+media+server+review" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://holyarrs.com" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> HolyArrs 공식 웹사이트 바로가기
              </a>
              <a href="https://github.com/HolyArrs/HolyArrs" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
