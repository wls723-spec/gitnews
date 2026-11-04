# -*- coding: utf-8 -*-
# 9 Hacker News Minor Radar Items for 2026-11-02

HN_MINORS = """
      <!-- [HN 0~26h] Item 1: HackerBooks -->
      <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~26h</span>
              <span class="minor-metric">🔺 790점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.7시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 102.7 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;해커뉴스 20년 역사의 추천 도서를 한눈에&quot; : HackerBooks</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Show HN: HackerBooks (hackerbooks.org) — 해커뉴스 커뮤니티 댓글 전체에서 언급된 서적과 추천 맥락을 추출하여 지식 그래프로 구조화한 도서 포털</span>
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
          <h3 class="minor-detail-headline">커뮤니티 지성 집약형 도서 검색소: HackerBooks</h3>
          <div class="minor-detail-subheadline">아마존 알고리즘의 광고 추천에 지친 개발자들을 위한 순수 지식 큐레이션</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 토론 핵심 쟁점</div>
              <p class="minor-paragraph">
                최근 화제가 된 HackerTube에 이어 등장한 프로젝트로, 2007년부터 축적된 4,000만 개 이상의 HN 댓글을 마이닝하여 컴퓨터 과학, 경제학, 철학 분야에서 가장 빈번하게 찬사를 받은 책들을 랭킹화하고 원본 추천 토론 링크를 매핑했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[데이터 파이프라인]</strong> HN BigQuery Comments Dump &rarr; ISBN/Title Entity Resolution &rarr; Sentiment & Upvote Weighting &rarr; Semantic Book Graph
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="message-square"></i> 개발자 커뮤니티 반응</div>
              <p class="minor-paragraph">
                "클린 코드, 설계 패턴 같은 뻔한 기술서뿐만 아니라 'Thinking in Systems'나 'The Design of Everyday Things'처럼 수천 번 회자된 불후의 고전들이 맥락과 함께 발굴된다"며 폭발적인 찬사가 이어졌습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://hackerbooks.org" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 서비스 웹사이트</a>
            <a href="https://news.ycombinator.com/item?id=43231102" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 원문</a>
          </div>
        </div>
      </div>

      <!-- [HN 0~26h] Item 2: Police Chief Unplugs Flock Cameras -->
      <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~26h</span>
              <span class="minor-metric">🔺 407점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.1시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 44.9 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;계약 해지 무시하자 플러그를 뽑았다&quot; : Flock 감시 카메라 사태</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">The Drive 보도 — 미국 시의회의 계약 해지 통보를 무시하고 번호판 촬영을 지속하던 감시 카메라 벤더 Flock에 맞서 경찰서장이 직접 전원을 차단한 사건</span>
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
          <h3 class="minor-detail-headline">빅브라더 감시 벤더와 지자체의 물리적 충돌: Flock 사태</h3>
          <div class="minor-detail-subheadline">민간 테크 기업의 공공 인프라 무단 관제와 프라이버시 침해 논란의 극적 단면</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 토론 핵심 쟁점</div>
              <p class="minor-paragraph">
                차량 번호판 자동 인식(ALPR) 네트워크를 미국 전역에 구축 중인 스타트업 Flock Safety가 시 정부의 공식 계약 종료 요청에도 장비를 철거하지 않고 데이터를 계속 수집하자, 지역 경찰서장이 현장으로 나가 카메라 케이블을 물리적으로 뽑아버린 사건이 큰 반향을 일으켰습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[갈등 구조]</strong> City Council Cancel Resolution &rarr; Vendor Inaction & Cloud Ingestion Continuation &rarr; Police Chief Physical Disconnect &rarr; Public Surveillance Audit
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="message-square"></i> 개발자 커뮤니티 반응</div>
              <p class="minor-paragraph">
                "소프트웨어 서비스(SaaS) 기업이 공공 하드웨어를 인질로 잡고 데이터 주권을 침해하는 현실에 대해, 소프트웨어 명령어가 아닌 물리적 플러그 뽑기로 응답한 가장 명쾌한 해결책"이라는 지지가 쏟아졌습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.thedrive.com/news/my-city-canceled-flocks-contract-flock-ignored-it-so-the-police-chief-unplugged-the-cameras" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> The Drive 기사 원문</a>
            <a href="https://news.ycombinator.com/item?id=43229871" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 원문</a>
          </div>
        </div>
      </div>

      <!-- [HN 0~26h] Item 3: Lenovo Encrypted USB Scandal -->
      <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~26h</span>
              <span class="minor-metric">🔺 362점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.1시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 39.8 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;지문 암호화 USB를 뜯었더니 일반 SD카드가 나왔다&quot; : 레노버 보안 스캔들</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">하드웨어 해커 포렌식 폭로 — 고가 엔터프라이즈 '지문 인식 하드웨어 암호화 USB' 케이스 내부가 암호화 없는 시판 마이크로SD 카드 단품으로 구성된 충격적 실체</span>
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
          <h3 class="minor-detail-headline">가짜 하드웨어 암호화의 민낯: 지문 인식 케이스의 눈속임</h3>
          <div class="minor-detail-subheadline">플라스틱 하우징만 열면 누구든 기밀 데이터를 무암호화 상태로 읽을 수 있는 치명적 설계 결함</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 토론 핵심 쟁점</div>
              <p class="minor-paragraph">
                한 하드웨어 리버스 엔지니어가 고가의 지문 보안 USB 드라이브를 분해한 결과, 지문 센서는 단순히 USB 버스 전원을 켜고 끄는 스위치 역할만 할 뿐, 실제 데이터는 평문 그대로 FAT32 마이크로SD 카드에 기록되고 있었음을 폭로했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[가짜 보안 구조]</strong> Fingerprint Sensor (Simple Power Switch) &rarr; NO Cryptographic Key Derivation &rarr; Raw Unencrypted MicroSD Socket Exposed
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="message-square"></i> 개발자 커뮤니티 반응</div>
              <p class="minor-paragraph">
                "이것은 보안이 아니라 '극장 보안(Security Theater)'의 극치"라며, 엔터프라이즈 하드웨어 구매 시 FIPS 140-2 등 공인 독립 인증과 오픈소스 하드웨어 감사 검증의 필요성이 강하게 제기되었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.reddit.com/r/technology/comments/1xl2pr3/lenovos_encrypted_fingerprint_usb_drive_is_just/" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 레딧 분석 원문</a>
            <a href="https://news.ycombinator.com/item?id=43229899" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 원문</a>
          </div>
        </div>
      </div>

      <!-- [HN 26~52h] Item 4: HackerTube -->
      <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 26~52h</span>
              <span class="minor-metric">🔺 2,189점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 27.7시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 79.0 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;알고리즘 미끼 없는 고지능 유튜브&quot; : HackerTube 바이럴 돌풍</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">HackerTube (karpathy.bearblog.dev) — 해커뉴스 커뮤니티에서 검증되고 찬사받은 영상들만 선별해 재구성한 클린 비디오 포털 (+2,100 Upvotes)</span>
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
          <h3 class="minor-detail-headline">알고리즘 도파민을 걷어낸 영상 큐레이션: HackerTube</h3>
          <div class="minor-detail-subheadline">어그로 썸네일과 쇼츠 지옥을 벗어나 순수 테크 강연과 다큐멘터리에 집중하다</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 토론 핵심 쟁점</div>
              <p class="minor-paragraph">
                유튜브의 자극적 추천 알고리즘에 지친 개발자들을 위해, HN에 링크되어 높은 추천과 지적 토론을 이끌어낸 고품질 영상(컴퓨터 역사, 시스템 아키텍처 강연, 수학 증명)만을 모은 미니멀 인터페이스 사이트가 주말 동안 해커뉴스 1위에 등극했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[큐레이션 파이프라인]</strong> HN Story / Comment URL Parser &rarr; Youtube Video ID Filter &rarr; Comment Score Thresholding &rarr; Pure Text Minimal Feed
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="message-square"></i> 개발자 커뮤니티 반응</div>
              <p class="minor-paragraph">
                안드레이 카파시를 비롯한 유력 엔지니어들이 "드디어 유튜브가 원래 의도했던 학습 도구의 본질을 되찾았다"며 찬사를 보냈고, 파생 프로젝트(HackerBooks)의 시발점이 되었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://karpathy.bearblog.dev/hacker-tube/" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 프로젝트 블로그</a>
            <a href="https://news.ycombinator.com/item?id=43224412" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 원문</a>
          </div>
        </div>
      </div>

      <!-- [HN 26~52h] Item 5: TCP Use-After-Free Linux Kernel 0-day -->
      <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 26~52h</span>
              <span class="minor-metric">🔺 695점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 28.4시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 24.5 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;리눅스 커널 IPv4 스택의 치명적 제로데이&quot; : CVE-2026-98432 (CVSS 9.8)</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Atlasum 보안 분석 — 리눅스 TCP 소켓 해제 과정의 Use-After-Free 취약점으로 인증 없는 원격 코드 실행(RCE)이 가능한 초고위험 보안 경보</span>
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
          <h3 class="minor-detail-headline">리눅스 네트워킹 서브시스템 비상: CVE-2026-98432</h3>
          <div class="minor-detail-subheadline">악의적으로 조작된 TCP 패킷 하나로 커널 공간 메모리를 원격 오염시키는 위험성</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 토론 핵심 쟁점</div>
              <p class="minor-paragraph">
                IPv4 TCP 연결 종료(FIN-WAIT) 시점의 타이머 핸들러와 소켓 메모리 해제 루틴 사이의 레이스 컨디션(Race Condition)으로 인해 발생하는 Use-After-Free 버그가 공개되었습니다. CVSS 9.8의 최고 위험도로 평가되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[취약점 메커니즘]</strong> Crafted TCP FIN Storm &rarr; Kernel Timer Expiry Race &rarr; tcp_close() Socket Free &rarr; Orphan Pointer Dereference (RCE)
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="message-square"></i> 개발자 커뮤니티 반응</div>
              <p class="minor-paragraph">
                주요 클라우드 벤더(AWS, GCP, Azure)가 긴급 하이퍼바이저 패치에 돌입했으며, 리눅스 재단은 커널 6.12.x 및 안정화 버전에 대한 긴급 보안 릴리즈를 배포하고 모든 서버의 즉각적인 업데이트를 권고했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 보안 분석 보고서</a>
            <a href="https://news.ycombinator.com/item?id=43224219" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 원문</a>
          </div>
        </div>
      </div>

      <!-- [HN 26~52h] Item 6: Jepsen: ParticleDB 1.1.4 -->
      <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 26~52h</span>
              <span class="minor-metric">🔺 334점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 34.0시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 9.8 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;마케팅 선언과 다른 분산 데이터 유실&quot; : 옙센(Jepsen)의 ParticleDB 감사</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">카일 킹스베리(Aphyr)의 심층 분석 — '엄격한 직렬화 가능성(Strict Serializability)'을 표방하던 차세대 분산 DB에서 네트워크 단절 시 데이터 불일치 적발</span>
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
          <h3 class="minor-detail-headline">분산 합의 검증의 심판대: 옙센의 ParticleDB 해부</h3>
          <div class="minor-detail-subheadline">Paxos와 Raft의 변형 알고리즘이 비동기 시계 표류(Clock Drift) 상황에서 무너지는 메커니즘</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 토론 핵심 쟁점</div>
              <p class="minor-paragraph">
                분산 시스템 검증의 권위자 카일 킹스베리가 고성능 분산 SQL을 자처하는 ParticleDB 1.1.4 버전을 감사했습니다. 네트워크 파티션과 노드 재부팅이 동시에 일어날 때 리더 임차권(Leader Lease) 갱신 실패로 인해 쓰기 유실(Lost Updates)이 발생함을 입증했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[오류 시나리오]</strong> Network Split &rarr; Leader Lease Invalidation Delay &rarr; Dual Leader Split-Brain &rarr; G-counter Dirty Reads Detected
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="message-square"></i> 개발자 커뮤니티 반응</div>
              <p class="minor-paragraph">
                "화려한 벤치마크 그래프보다 옙센 테스트 한 번을 통과하는 것이 백배 어렵다"는 격언이 다시 증명되며, 개발팀은 즉시 버그를 인정하고 리스 유효시간 축소 패치를 약속했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://jepsen.io/analyses/particledb-1.1.4" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> Jepsen 분석 전문</a>
            <a href="https://news.ycombinator.com/item?id=43221990" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 원문</a>
          </div>
        </div>
      </div>

      <!-- [HN 52~78h] Item 7: Binance $5.6B Heist in 20 Minutes -->
      <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 52~78h</span>
              <span class="minor-metric">🔺 1,757점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 74.0시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 23.7 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;단 20분 만에 56억 달러 증발&quot; : 바이낸스 해커 탈취 사건 전말</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">온체인 인텔리전스 Arkham 및 WIRED 분석 — 크로스체인 브리지의 다중서명 검증자 프라이빗 키 유출로 역사상 최대 규모의 암호화폐 탈취 발생</span>
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
          <h3 class="minor-detail-headline">웹3 역사상 최대의 인프라 해킹: 56억 달러 탈취</h3>
          <div class="minor-detail-subheadline">스마트 컨트랙트 로직이 아닌 인프라 서명 노드의 크리덴셜 관리 실패가 부른 참사</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 토론 핵심 쟁점</div>
              <p class="minor-paragraph">
                해커는 스마트 컨트랙트 결함을 공격한 것이 아니라, 브리지 검증 노드 관리자의 서버에 침투해 4개의 프라이빗 서명 키를 탈취했습니다. 단 20분 만에 위조된 인출 트랜잭션을 일괄 발생시키며 56억 달러(한화 약 7조 6천억 원)를 인출했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[공격 타임라인]</strong> Validator Server SSH Compromise &rarr; Private Key Exfiltration &rarr; Forged Cross-Chain Withdrawal &rarr; Tornado Cash Mixer Dispersion
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="message-square"></i> 개발자 커뮤니티 반응</div>
              <p class="minor-paragraph">
                "블록체인 불변성도 운영 서버의 전통적 보안(SecOps)이 무너지면 아무 소용이 없다"는 뼈아픈 교훈을 남기며, 엔터프라이즈 다중서명 시스템의 하드웨어 보안 모듈(HSM) 격리 의무화가 논의되고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> WIRED 심층 기사</a>
            <a href="https://news.ycombinator.com/item?id=43210452" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 원문</a>
          </div>
        </div>
      </div>

      <!-- [HN 52~78h] Item 8: Backdoor in Claude Code Extension -->
      <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 52~78h</span>
              <span class="minor-metric">🔺 990점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 64.5시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 15.3 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;마켓플레이스에 올라온 가짜 클로드 코드 확장팩 백도어&quot; : 공급망 오염</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">보안 연구소 Phorion 폭로 — Cursor 및 Open VSX 마켓플레이스에 공식 앤스로픽을 사칭하여 등록된 Claude Code 확장팩에서 세션 토큰 탈취 악성코드 적발</span>
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
          <h3 class="minor-detail-headline">AI 도구 생태계의 소프트웨어 공급망 습격: 가짜 확장팩 사태</h3>
          <div class="minor-detail-subheadline">개발자의 API 키와 깃허브 토큰을 노리는 타이포스쿼팅(Typosquatting) 공격의 위험성</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 토론 핵심 쟁점</div>
              <p class="minor-paragraph">
                앤스로픽의 공식 'Claude Code' CLI 인기를 노리고, 비공식 마켓플레이스에 동일한 이름과 아이콘으로 등록된 VS Code 확장팩이 백그라운드에서 유저의 <code>~/.claude/session.json</code> 토큰을 원격 C2 서버로 빼돌리던 사실이 포렌식 분석을 통해 밝혀졌습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[공급망 공격]</strong> Typosquatted Publisher &rarr; Malicious Extension Install &rarr; Session Token / SSH Key Scraping &rarr; Stealth HTTPS Exfiltration
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="message-square"></i> 개발자 커뮤니티 반응</div>
              <p class="minor-paragraph">
                확장팩 마켓플레이스의 퍼블리셔 검증 부실이 도마 위에 올랐으며, 개발자들은 공식 깃허브 저장소(anthropics/claude-plugins-official)의 서명된 슬러그만 설치할 것을 강력히 경고했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://phorion.io/blog/offical-claude-code-vsx-compromise/" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> Phorion 보안 보고서</a>
            <a href="https://news.ycombinator.com/item?id=43214820" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 원문</a>
          </div>
        </div>
      </div>

      <!-- [HN 52~78h] Item 9: AI Isn't Replacing SREs, It's Deskilling Them -->
      <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 52~78h</span>
              <span class="minor-metric">🔺 664점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 55.8시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 11.9 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;AI는 SRE를 대체하는 것이 아니라 탈숙련화시키고 있다&quot; : 테크 에세이</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">SigNoz 엔지니어링 에세이 — 자동화된 AI 근본 원인 분석 도구에 의존하면서 주니어 엔지니어들의 리눅스 내부 구조 직관과 장애 복구 근육이 퇴화하는 현실 경종</span>
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
          <h3 class="minor-detail-headline">인프라 엔지니어링의 인지적 퇴화 경고: 탈숙련화(Deskilling) 논쟁</h3>
          <div class="minor-detail-subheadline">마법 같은 블랙박스 복구 버튼 뒤에서 사라져 가는 시스템 1차 원리 이해</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 토론 핵심 쟁점</div>
              <p class="minor-paragraph">
                AI가 장애 원인을 즉시 요약해 주는 환경에서 성장한 신입 사이트 신뢰성 엔지니어(SRE)들이, AI 모델이 환각을 일으키거나 예측하지 못한 엣지 케이스 장애가 터졌을 때 <code>tcpdump</code>나 <code>strace</code>로 직접 패킷을 추적하는 능력을 상실하고 있다는 날카로운 지적입니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[인지 퇴화 루프]</strong> AI One-Click Auto-Remediation &rarr; Human Debugging Bypassed &rarr; Deep System Intuition Loss &rarr; Catastrophic Failure Vulnerability
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="message-square"></i> 개발자 커뮤니티 반응</div>
              <p class="minor-paragraph">
                수많은 시니어 인프라 아키텍트들이 깊은 공감을 표하며 "도구는 판단을 보조해야지, 엔지니어의 비판적 사고와 시스템 콜 레벨의 이해를 대체해서는 안 된다"는 자성의 목소리를 높였습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> SigNoz 뉴스레터 전문</a>
            <a href="https://news.ycombinator.com/item?id=43217904" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론 원문</a>
          </div>
        </div>
      </div>
"""
