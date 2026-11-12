# -*- coding: utf-8 -*-
# Story 3: simpsoka/zigzag

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] simpsoka/zigzag                                  -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_zigzag.jpg" alt="ZigZag Cover Art" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="scissors" style="width:12px;height:12px;fill:#fff;"></i> HARDWARE FREEDOM</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#e0e7ff; border-color:#6366f1; color:#4338ca;">🧵 구독제 인질극 격파</span>
              <span class="platform-tag">Show HN #1 (234 pts) & zigzag.diy</span>
              <span class="platform-tag">simpsoka / zigzag</span>
            </div>
            
            <h2 class="article-headline">
              300달러 자수 재봉틀의 '월정액 구독제 인질극'에 분노한 엔지니어의 반란: 'Zigzag' — 독점 하드웨어를 역공학하고 MCP AI 에이전트로 자수를 놓는 오픈소스 스위트
            </h2>

            <div class="article-subheadline">
              자수 패턴 하나 전송하는 데 월 20달러 구독료를 강요하던 IoT 제조사들의 악질적 상술을 박살 낸 Rust 기반 오픈소스 에디터… SVG 벡터 변환부터 Claude Code 실시간 패턴 생성까지 완전 해방
            </div>
            <p class="article-snippet">
              취미로 자수를 놓기 위해 300달러짜리 디지털 재봉틀을 구입했던 한 소프트웨어 엔지니어는, 기계 자체는 완벽하게 작동함에도 불구하고 PC에서 자수 도안 파일을 기계로 전송하려면 매달 19.99달러의 전용 클라우드 구독료를 내야 한다는 사실을 알고 격분했습니다. 그는 제조사의 통신 프로토콜을 모조리 리버스 엔지니어링하여 독점 포맷을 해독하고, AI 에이전트와 대화하며 실시간으로 자수 패턴을 직조하는 강력한 오픈소스 소프트웨어 'ZigZag'를 완성해 세상에 공개했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: "내 돈 주고 산 300달러 기계인데, 바느질 한 번에 왜 구독료를 내야 하는가?"
            </h3>
            <p>
              "박스를 열고 전원을 켰을 때까지만 해도 완벽했습니다. 하지만 노트북을 연결하고 내가 그린 SVG 로고를 전송하려는 순간, 제조사의 공식 앱은 싸늘한 팝업을 띄웠습니다: <em>'커스텀 도안 전송 기능을 활성화하려면 월 19.99달러의 크리에이터 패스를 구독하십시오.'</em>"
            </p>
            <p>
              하드웨어를 이미 전액 지불하고 구매했음에도, 기계 내부의 기본 모터를 회전시키는 소프트웨어 인터페이스를 클라우드 페이월(Paywall) 뒤에 인질로 감금해 둔 전형적인 하드웨어 제조사의 악질적 상술이었다.
            </p>
            <p>
              엔지니어 샘 심슨(Sam Simpson)은 신용카드를 꺼내는 대신 와이어샤크(Wireshark)와 디스어셈블러를 켰다. 3개월간의 피나는 리버스 엔지니어링 끝에, 그는 제조사의 클라우드 서버를 거치지 않고 직접 자수기를 제어하는 오픈소스 스위트 <strong>ZigZag</strong>를 세상에 던졌다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '소유권의 박탈'에 맞서는 메이커 커뮤니티의 거대한 환호
            </h3>
            <p>
              해커뉴스 'Show HN'에 올라온 그의 작업기는 게시 몇 시간 만에 230개 이상의 열광적인 업보트와 수백 개의 응원 댓글을 이끌어냈다.
            </p>

            <div class="editorial-quote">
              <p>
                "프린터 잉크 카트리지 락인, 자동차 열선 시트 구독제, 이제는 재봉틀 바느질까지 구독을 강요합니다. 
                <strong>당신이 물리적으로 구매한 물건은 온전히 당신의 것이어야 합니다. ZigZag는 영원히 무료이며, 클라우드 연결도, 계정 가입도 필요 없습니다.</strong> 
                게다가 우리는 여기에 MCP(Model Context Protocol)를 내장하여, Claude Code나 Cursor에게 '귀여운 고양이 패치 도안을 짜줘'라고 말하면 에이전트가 직접 자수 스티치를 엮어냅니다."
              </p>
              <small>— Sam Simpson, ZigZag 오픈소스 릴리즈 전문</small>
            </div>

            <p>
              단순히 옛날 소프트웨어를 복제한 수준이 아니었다. ZigZag는 최고 성능의 Rust 언어로 렌더링 엔진을 밑바닥부터 작성했고, 세계 최초로 <strong>AI 에이전트가 자수 침로(Stitch Path)를 직접 제어하는 MCP 서버</strong>를 기본 탑재하여 상용 유료 소프트웨어들보다 10배 뛰어난 생산성을 과시했다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 메커니즘: 독점 바이트스트림 해독과 MCP 기반 자율 스티치 제어
            </h3>
            <p>
              ZigZag는 자수 업계의 파편화된 독점 바이너리 포맷을 완벽하게 관통한다:
            </p>
            <ul>
              <li><strong>Multi-Format Cleanroom Parser:</strong> Brother/Baby Lock의 `.PES`, 타지마(Tajima)의 산업 표준 `.DST`, Melco의 `.EXP`, Janome의 `.JEF`, Husqvarna의 `.VP3` 포맷을 바이너리 수준에서 파싱하여 실시간 바늘 이동 궤적(X, Y 델타)과 색상 변경 명령어를 복원.</li>
              <li><strong>Rust Vector Stitching Engine:</strong> 일반 2D SVG 벡터 그래픽의 베지어 곡선을 물리적 실의 장력과 천의 밀도를 고려한 최적의 자수 침로(Tatami Fill, Satin Stitch, Running Stitch)로 자동 분할.</li>
              <li><strong>Agentic Embroidery via MCP:</strong> 내장된 Model Context Protocol 인터페이스를 통해 Claude Code나 AI 에이전트가 사용자의 자연어 요청을 받아 기하학적 문양을 수학적으로 계산하고, 스티치 밀도를 조정하며, 에러를 스스로 수정.</li>
              <li><strong>Zero-Cloud Direct USB/Serial Link:</strong> 인터넷 연결 없이 로컬 USB 케이블이나 SD 카드를 통해 기계로 즉시 바이너리를 주입.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">ZigZag AI 에이전트 &amp; 자수 하드웨어 직결 파이프라인</span>
                <span class="schematic-badge">Anti-Subscription Freedom Stack</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">Creative &amp; AI Tier</div>
                  <div class="schematic-desc">
                    SVG Artwork / Text Prompt<br>
                    Claude Code &amp; MCP Tool Calling<br>
                    자연어로 도안 기하학 실시간 생성<br>
                    구독료: 0원 (완전 로컬)
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">ZigZag Core Engine (Rust)</div>
                  <div class="schematic-desc">
                    Vector-to-Stitch Physics Engine<br>
                    Tatami / Satin Fill Path Optimization<br>
                    PES / DST / EXP Binary Exporter<br>
                    초당 60fps 무지연 실시간 렌더링
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">Physical Embroidery Machine</div>
                  <div class="schematic-desc">
                    $300 일반 가정용/공업용 자수기<br>
                    제조사 클라우드 서버 완전 우회<br>
                    Direct USB / SD Card 전송<br>
                    영구적 하드웨어 소유권 회복
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">ZigZag 공식 웹사이트 및 자수 스티치 뷰어 인터페이스</span>
              </div>
              <img src="../assets/images/demo_zigzag.png" alt="ZigZag Live Interface" class="showcase-img">
              <p class="showcase-caption">
                ▲ zigzag.diy 공식 플랫폼 뷰: "Free, open-source embroidery software for Mac and Windows. Turn SVG artwork into machine embroidery, edit stitches visually, and create designs with AI agents via MCP." 구독료 인질극을 깬 오픈소스 실리콘 스티치 에디터 화면.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 법적 분기점: '수리할 권리'와 하드웨어 종속 비즈니스의 붕괴
            </h3>
            <p>
              전 세계 하드웨어 제조사들은 하드웨어 판매 마진의 감소를 보충하기 위해 '기능의 서비스화(Feature as a Service)'라는 미명 아래 기본 동작을 구독 모델로 전환하는 전략을 앞다투어 도입해왔다.
            </p>
            <p>
              그러나 미국 연방거래위원회(FTC)와 유럽연합(EU)의 '수리할 권리(Right to Repair)' 및 상호 운용성 보장 입법이 가속화되면서, 이러한 인위적 소프트웨어 페이월은 법적 정당성을 잃어가고 있다. 
              ZigZag의 성공은 "소비자가 구매한 하드웨어의 입출력 프로토콜을 해독하고 자유 소프트웨어로 대체하는 행위"가 기술적으로나 윤리적으로 완벽한 승리를 거둘 수 있음을 전 세계 메이커들에게 선포한 중대한 사건이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 바느질 한 땀에 담긴 해커 윤리
            </h3>
            <p>
              물리적 세계의 기계와 디지털 세계의 소프트웨어가 얽히는 사물인터넷(IoT) 시대에, 우리가 사용하는 도구의 주권을 기업에 백지위임할 수는 없다.
            </p>
            <p>
              단돈 300달러짜리 재봉틀에서 시작된 작은 반란은, "내가 소유한 것은 내가 통제한다"는 해커 문화의 가장 순수한 본질이 여전히 테크 세계의 부조리를 치유하는 가장 날카로운 바늘임을 증명하고 있다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=ZigZag+open+source+embroidery+software+demo" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://zigzag.diy" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> ZigZag 공식 웹사이트
              </a>
              <a href="https://github.com/simpsoka/zigzag" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div> <!-- .editorial-content -->
        </div> <!-- .article-detail -->
      </article>
"""
