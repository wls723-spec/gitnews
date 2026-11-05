# -*- coding: utf-8 -*-
# Story 5: sshole (HERO 5)

STORY_5_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 5] sshole -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_sshole.png" alt="sshole tunnel" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="terminal" style="width:12px;height:12px;fill:#fff;"></i> HN #1 (2,195 PTS)</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 ngrok을 무력화한 단 한 줄의 터미널 명령어</span>
              <span class="platform-tag">Hacker News #1</span>
              <span class="platform-tag">sshhole.com</span>
            </div>
            
            <h2 class="article-headline">
              "설치도, 계정도 필요 없다" — SSH 한 줄로 방화벽을 뚫는 공공 터널 sshole
            </h2>

            <div class="article-subheadline">
              ngrok과 Cloudflare Tunnel의 가입 강제와 유료 구독화에 지친 해커들의 반란… 표준 SSH 리버스 포트 포워딩 하나로 로컬 웹 서버를 전 세계에 즉각 무료 HTTPS 공개
            </div>
            <p class="article-snippet">
              해커뉴스에서 2,195포인트와 수백 개의 찬사 댓글을 기록하며 올가을 최고의 바이럴 인프라로 등극한 오픈소스 프로젝트 'sshole'. 전용 클라이언트 설치 없이 모든 운영체제에 기본 탑재된 SSH만으로 로컬 개발 포트를 인터넷에 노출하는 아키텍처를 분석합니다.
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
              <i data-lucide="flame"></i> 1. 리드: "로컬 서버 주소 하나 공유하는 게 왜 이렇게 복잡해졌는가?"
            </h3>
            <p>
              동료에게 지금 로컬에서 개발 중인 웹사이트를 잠깐 보여주거나, 웹훅(Webhook) 테스트를 위해 임시 공개 URL이 필요할 때마다 개발자들은 깊은 피로를 느껴왔다. 
              과거 사랑받던 ngrok은 이메일 가입, 신용카드 등록, 유료 요금제 결제를 강요하기 시작했고, 
              Cloudflare Tunnel이나 다른 대안들도 전용 데몬 바이너리(cloudflared 등) 설치와 복잡한 DNS 설정을 요구했다.
            </p>
            <p>
              오늘 해커뉴스 1위를 장악하며 무려 <strong>2,195개의 업보트(Points)</strong>를 쓸어 담은 <strong>sshole (sshhole.com)</strong>은 이 모든 번거로움을 단 한 줄의 터미널 명령어로 증발시켰다. 
              <strong>프로그램 다운로드 0개, 계정 가입 0개, 환경설정 0개. 
              그저 터미널을 열고 <code>ssh -R 80:localhost:3000 sshhole.com</code>을 치는 순간 전 세계 어디서나 접속할 수 있는 암호화된 HTTPS 링크가 즉시 튀어나온다.</strong>
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 가장 오래된 프로토콜의 가장 섹시한 부활
            </h3>
            <p>
              sshole은 새로운 기술을 발명하지 않았다. 
              유닉스(Unix) 탄생 이래 모든 맥, 리눅스, 윈도우11 터미널에 기본으로 깔려 있는 <strong>표준 OpenSSH 클라이언트</strong>의 숨겨진 잠재력을 극대화했을 뿐이다.
            </p>

            <div class="editorial-quote">
              <p>
                "당신 컴퓨터에는 이미 완벽하게 검증된 종단간 암호화 터널링 도구가 깔려 있다. 바로 <code>ssh</code>다. 
                우리는 수수료 장사치들의 전용 클라이언트를 걷어내고, 인터넷의 기본 프로토콜이 약속했던 '개방과 연결의 자유'를 되찾아주었을 뿐이다."
              </p>
              <small>— sshole 프로젝트 릴리즈 선언문</small>
            </div>

            <p>
              공유기 NAT나 사내 보안 방화벽 뒤에 숨어 있는 <code>localhost:3000</code>, <code>localhost:8080</code> 포트가 sshole의 엣지 프록시 서버와 암호화된 역방향 SSH 터널(Reverse SSH Tunnel)로 직결되며, 실시간 방문자 트래픽이 터미널 화면에 컬러 로그로 스트리밍된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 자동 서브도메인과 Let's Encrypt 즉시 발급
            </h3>
            <p>
              sshole이 이토록 매끄럽게 동작할 수 있는 기술적 백본은 세 단계로 요약된다:
            </p>
            <ul>
              <li><strong>SSH Remote Port Forwarding (-R):</strong> 클라이언트가 <code>-R 80:localhost:PORT</code> 옵션으로 접속하면, sshole 서버의 SSH 데몬이 클라이언트의 SSH 공개키 지문이나 임의의 세션 해시를 기반으로 전용 고유 서브도메인을 할당.</li>
              <li><strong>와일드카드 자동 SSL/TLS 종단:</strong> 생성된 <code>*.sshhole.com</code> 주소로 웹 트래픽이 유입되는 즉시 Let's Encrypt 와일드카드 인증서를 통해 브라우저 안전 경고 없는 완벽한 HTTPS 연결 보장.</li>
              <li><strong>역방향 TCP 스트리밍 & 헤더 재작성:</strong> 유입된 HTTP/HTTPS 요청을 SSH 터널 속 소켓 채널을 통해 로컬 개발 머신으로 즉시 릴레이하며 <code>Host</code>, <code>X-Forwarded-For</code> 헤더를 투명하게 보존.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="git-branch" style="color:#0ea5e9;"></i> sshole 제로 인스톨 터널링 아키텍처
                </span>
                <span class="schematic-badge">ZERO-INSTALL SSH TUNNEL</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">표준 터미널 한 줄 실행</div>
                  <div class="step-tech">ssh -R 80:localhost:3000 sshhole.com</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">엣지 프록시 암호화 터널 직결</div>
                  <div class="step-tech">Encrypted SSH Reverse Channel</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">전 세계 공개 HTTPS URL 생성</div>
                  <div class="step-tech">https://random-sub.sshhole.com</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 원리:</strong> 별도의 상용 에이전트를 설치하지 않고도 표준 OpenSSH 바이너리가 원격 게이트웨이와 맺는 역방향 터널을 통해 방화벽을 뚫고 즉시 퍼블릭 웹 서비스를 개시합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="heart"></i> 4. 해커들의 열광: "이것이 바로 인터넷의 낭만이다"
            </h3>
            <p>
              해커뉴스 댓글란에는 "90년대 웹 해커의 낭만이 되살아났다", "모든 상용 터널 SaaS 계정을 해지했다"는 열띤 반응이 줄을 이었다. 
              복잡한 인증 절차와 상업적 장벽으로 숨이 막혀가던 웹 개발 환경에, 기본에 충실한 미니멀리즘이 얼마나 파괴적인 매력을 가질 수 있는지를 통쾌하게 증명한 쾌거다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="monitor" style="color:#10b981;"></i> sshole 공식 터미널 콘솔 화면
                </span>
                <span class="media-showcase-badge demo">OFFICIAL SHOWCASE</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/thumb_sshole.png" alt="sshole command terminal" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 군더더기 없는 터미널 인터페이스:</strong> 단 한 줄의 SSH 입력으로 부여받은 공개 URL과 실시간 접속 로그가 화면에 즉시 표시되는 모습.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-check"></i> 5. 결론: 가장 단순한 것이 가장 강하다
            </h3>
            <p>
              sshole은 거창한 프레임워크나 복잡한 클라우드 아키텍처 없이도, 표준 프로토콜의 본질을 꿰뚫는 통찰만으로 수백억 원 가치의 상용 서비스를 압도할 수 있음을 보여주었다. 
              개발자의 책상 위에 언제나 켜져 있는 가장 든든한 공공 인프라다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://sshhole.com" target="_blank" class="project-link demo">
                  <i data-lucide="sparkles" style="width:16px;height:16px;"></i> 공식 웹사이트 sshhole.com
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
