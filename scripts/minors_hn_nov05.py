# -*- coding: utf-8 -*-
# 9 Hacker News Minor Radar Items for 2026-11-05

HN_MINORS = """
      <!-- ==================== HACKER NEWS BUCKET 1 (0~10h) ==================== -->
      <!-- [HN 0~10h] Item 1: Residential proxies detected on White House network -->
      <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔥 453 pts</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 2.7시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 170.6 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;백악관 네트워크 내부에서 주거용 프록시 봇넷 노드 적발&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Layer3 Intel 보안 블로그 — 미국 정부 핵심 시설 IP 블록에서 은밀히 작동하던 상용 주거용 프록시(Residential Proxy) 트래픽 탐지 분석 리포트 화제</span>
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
          <h3 class="minor-detail-headline">최고 보안 시설마저 파고든 IoT 및 무료 VPN 기반 좀비 프록시의 충격</h3>
          <div class="minor-detail-subheadline">정부 공공망의 신뢰도(Reputation)를 악용하려는 글로벌 사이버 공격 집단의 위협</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                사이버 보안 인텔리전스 기업 Layer3가 백악관 공인 IP 대역에서 상용 주거용 프록시 네트워크의 출구 노드(Exit Node) 트래픽이 발생하고 있음을 포착했습니다. 이는 내부 직원의 감염된 개인 기기나 스마트 IoT 장비가 공격자의 트래픽 세탁 통로로 악용되었을 가능성을 시사해 보안 커뮤니티에 거대한 충격을 안겼습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[침투 메커니즘]</strong> Infected Endpoint / Rogue VPN SDK &rarr; Covert Tunneling &rarr; White House IP Egress &rarr; Botnet Relay & Scraping Obfuscation
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                기존의 IP 평판 기반 방화벽 정책이 얼마나 취약한지를 명백히 보여주었으며, 모든 아웃바운드 세션에 대해 제로 트러스트(Zero Trust) mTLS 검증과 내부 엔드포인트 소프트웨어 인벤토리 감사가 필수적임을 일깨웠습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://layer3intel.com/blog/residential-proxies-white-house" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              원문 분석 리포트 읽기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 2: Everything is an AI scam now -->
      <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔥 117 pts</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 2.3시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 50.4 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;모든 것이 AI 사기가 되어버린 시대&quot; : 기술 거품에 대한 엔지니어의 통렬한 일침</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">David Ralph Lewis — 단순한 CRUD나 정규식으로 해결할 수 있는 문제까지 수천억 펀딩의 AI 과대광고로 둔갑시키는 테크 업계의 슬롭 현상 비판</span>
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
          <h3 class="minor-detail-headline">실제 엔지니어링 가치와 VC 마케팅 신기루 사이의 괴리</h3>
          <div class="minor-detail-subheadline">수많은 스타트업이 본질적인 문제 해결 대신 'AI' 꼬리표 붙이기에 매몰된 현실 지적</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                생성형 AI의 진정한 혁신과 별개로, 기존 기능을 그저 LLM API 래퍼로 덮어씌워 구독료를 올리는 수많은 'AI 거품' 제품들에 피로감을 느끼던 개발자들 사이에서 폭발적인 공감을 얻으며 순식간에 수백 개의 토론 댓글이 달렸습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[비판 모델]</strong> Simple Deterministic Code &rarr; Unnecessary LLM Wrapper Layer &rarr; High Token Cost & Hallucination &rarr; Investor Hype Valuation
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                기술적 본질주의로의 회귀를 촉구하며, LLM이 진정으로 필요한 복합 추론 영역과 단순 규칙 기반 코드로 풀어야 할 영역을 엄격히 구분해야 한다는 소프트웨어 설계 철학을 역설합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.davidralphlewis.co.uk/posts/everything-is-an-ai-scam-now/" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              원문 에세이 읽기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 3: If you're on Replit Pro, you have until November 8 to opt out of arbitration -->
      <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔥 44 pts</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 2.5시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 17.4 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;Replit Pro 유저라면 11월 8일까지 강제 중재 조항을 거부하라&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">ReadTheDiff — Replit의 기습적인 이용약관 개정으로 사용자의 집단 소송 권리가 박탈될 위기… 기한 내 옵트아웃(Opt-out) 방법 상세 가이드</span>
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
          <h3 class="minor-detail-headline">SaaS 플랫폼들의 교묘한 약관 개정과 개발자 법적 권리 수호</h3>
          <div class="minor-detail-subheadline">30일 옵트아웃 창구를 놓치면 분쟁 시 법원 대신 사설 중재로 강제 귀속</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                AI 클라우드 IDE 플랫폼 Replit이 서비스 약관에 '강제 중재(Binding Arbitration) 및 집단소송 권리 포기' 조항을 몰래 추가한 사실이 밝혀졌습니다. 이메일을 통한 서면 거부 신청 마감일이 11월 8일로 임박함에 따라 개발자 커뮤니티에 긴급 주의보가 발령되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[대응 프로세스]</strong> Terms Change Notice &rarr; Opt-out Notice Email to arbitration-opt-out@replit.com &rarr; Preserved Civil Court Rights
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                독립 개발자와 기업이 클라우드 IDE에 지적 재산권(IP)과 소스 코드를 위탁할 때 발생할 수 있는 데이터 손실이나 서비스 중단 분쟁 시 법적 구제 수단을 보존하는 필수적인 조치입니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://readthediff.substack.com/p/replit-pro-arbitration-opt-out" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              옵트아웃 가이드 읽기
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== HACKER NEWS BUCKET 2 (10~20h) ==================== -->
      <!-- [HN 10~20h] Item 4: Ripple-65B Preview -->
      <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔥 186 pts</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.5시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 41.2 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;미국발 오픈웨이트 에이전틱 코딩 최강 SOTA&quot; : Ripple-65B</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Ricursive — 독점 상용 모델(Claude 3.7 Sonnet)에 필적하는 SWE-bench 성적을 기록한 650억 파라미터 오픈 가중치 에이전트 모델 프리뷰 공개</span>
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
          <h3 class="minor-detail-headline">오픈소스 코딩 모델의 판도를 뒤흔든 에이전틱 자율 추론 엔진</h3>
          <div class="minor-detail-subheadline">다중 턴 툴 사용(Multi-turn Tool Use)과 장기 디버깅 루프에 특화된 65B 아키텍처</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                지금까지 에이전트 코딩 영역은 앤트로픽과 오픈AI의 폐쇄형 API가 독점하고 있었습니다. Ricursive 연구팀이 공개한 Ripple-65B는 온프레미스 서버에서 구동 가능한 오픈 가중치 모델임에도 실전 코드베이스 탐색과 도구 호출에서 폐쇄형 SOTA에 근접하는 실력을 입증했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[에이전틱 훈련]</strong> Agentic Trajectory SFT &rarr; Multi-Turn Verifiable RL (Self-Debug Rewards) &rarr; Native Tool Calling Attention Head
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                기업들이 민감한 내부 소스 코드를 외부 API에 유출하지 않고도 사내 자체 인프라에서 고성능 코딩 에이전트를 자급자족할 수 있는 강력한 대안을 제공합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.ricursive.com/ripple" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              Ripple 공식 발표 보기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 5: Qualcomm Cloud AI 100 Ultra -->
      <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔥 75 pts</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.5시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 21.5 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;150W 초저전력에 128GB 메모리 탑재&quot; : 퀄컴 Cloud AI 100 Ultra</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Qualcomm — 548GB/s 대역폭과 150W TDP로 데이터센터 LLM 추론 TCO(총소유비용)를 혁신하는 엔터프라이즈 AI 가속 카드 발표</span>
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
          <h3 class="minor-detail-headline">엔비디아의 전력 폭식에 도전하는 퀄컴의 고효율 데이터센터 칩</h3>
          <div class="minor-detail-subheadline">700W~1000W에 달하는 경쟁사 대비 1/5 전력으로 거대 모델 동시 서빙 실현</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                AI 추론 인프라의 최대 병목이 '전력 인입량(Power Capacity)'으로 이동함에 따라, 랙당 설치 밀도를 극대화할 수 있는 150W급 저전력 고용량 가속기에 대한 클라우드 데이터센터들의 관심이 폭발하고 있습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[하드웨어 스펙]</strong> 128GB LPDDR5X (548GB/s) &rarr; Ultra-Low Power NPU Cores (150W TDP) &rarr; High-Density 1U Multi-Card Inference Server
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                단일 1U 서버에 4장의 카드를 꽂아 512GB의 VRAM 풀을 단 600W의 전력으로 확보할 수 있어, 70B~120B 파라미터급 오픈소스 모델 서빙 비용을 획기적으로 낮춥니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.qualcomm.com/data-center/products/cloud-ai-100-ultra" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              퀄컴 공식 제품 사양
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 6: This Month in Ladybird – October 2026 -->
      <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔥 103 pts</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.4시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 19.0 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;크롬 독점에 맞선 독립 브라우저 엔진&quot; : Ladybird 10월 개발 리포트</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Ladybird Browser — 구글 크로미움과 애플 웹킷의 코드를 단 한 줄도 쓰지 않고 바닥부터 구현한 신생 웹 엔진의 눈부신 10월 진척도</span>
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
          <h3 class="minor-detail-headline">웹 표준의 다양성을 지키는 순수 독자 렌더링 엔진의 도약</h3>
          <div class="minor-detail-subheadline">CSS Subgrid 완전 구현, 자바스크립트 LibJS JIT 컴파일러 속도 대폭 개선</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                웹 브라우저 생태계가 구글 크롬(Blink) 중심으로 획일화되어 웹 표준이 특정 기업에 종속되는 위기 속에서, 완전한 비영리 순수 오픈소스로 밑바닥부터 C++ 엔진을 구축하고 있는 레이디버드의 놀라운 기술적 진척이 개발자들의 열렬한 응원을 받고 있습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[엔진 아키텍처]</strong> Pure C++ LibWeb (CSS Subgrid / Layout) &rarr; In-house LibJS JIT Engine &rarr; Multi-Process Sandboxed Renderer
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                현대 웹의 복잡한 CSS 그리드 레이아웃과 ECMAScript 2026 표준 스펙 통과율이 90%를 돌파하여 실사용 가능한 독립 데스크톱 브라우저로 빠르게 진화하고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://ladybird.org/newsletter/2026-10-31/" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              레이디버드 공식 뉴스레터 읽기
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== HACKER NEWS BUCKET 3 (20~30h) ==================== -->
      <!-- [HN 20~30h] Item 7: Show HN: Wing Commander DOS Co-op -->
      <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔥 85 pts</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 4.5시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 18.7 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;10년간의 리버스 엔지니어링 끝에 1990년 DOS 윙 커맨더 협동 모드 구현&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">fireflyk64 — 소스 코드조차 없는 36년 전 16비트 x86 어셈블리 바이너리를 역어셈블하여 2인 협동 멀티플레이 네트워크 스택을 주입한 집념의 해커</span>
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
          <h3 class="minor-detail-headline">30년 전 고전 명작을 해킹해 꿈의 2인 멀티플레이를 실현한 전설적 프로젝트</h3>
          <div class="minor-detail-subheadline">인터럽트 후킹과 실시간 게임 루프 패칭을 통한 DOS 박스 네트워크 동기화</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                1990년 크리스 로버츠가 개발했던 우주 시뮬레이션 명작 '윙 커맨더(Wing Commander) 1'은 싱글플레이 전용이었습니다. 한 해커가 10년에 걸쳐 바이너리를 한 땀 한 땀 분석한 끝에 AI 윙맨 자리에 실제 친구가 탑승해 함께 적기를 격추할 수 있는 네트워크 패치를 완성했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[바이너리 패치]</strong> 16-bit x86 ASM Binary Hooking &rarr; AI Wingman Decision Loop Override &rarr; UDP Peer-to-Peer State Sync &rarr; 2-Player Co-op
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                원작 게임의 결정론적 난수 생성기와 물리 엔진 루프를 정밀하게 동기화하여 지연 시간(Lag) 없이 부드러운 도그파이트를 구현한 역어셈블리의 예술적 극치입니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://fireflyk64.github.io/wcmulti/" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              윙 커맨더 멀티 프로젝트 사이트
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 8: Conductor is joining Meta -->
      <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔥 73 pts</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 5.0시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 14.5 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;클라우드 렌더링 오케스트레이션의 강자 Conductor, 메타(Meta)에 전격 피인수&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Conductor.build — 대규모 VFX 렌더링 및 분산 컴퓨팅 클라우드 관리 플랫폼 Conductor 팀이 메타의 차세대 메타버스 및 생성형 비디오 인프라로 합류</span>
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
          <h3 class="minor-detail-headline">빅테크의 3D 그래픽스 및 생성형 영상 인프라 인재 쟁탈전 가속</h3>
          <div class="minor-detail-subheadline">AWS·GCP 멀티 클라우드 렌더 팜 오케스트레이션 노하우의 메타 편입</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                헐리우드 영화 스튜디오와 대형 게임사들의 복잡한 클라우드 렌더링 작업을 비용 효율적으로 스케일링하던 Conductor 플랫폼이 메타에 인수되었습니다. 메타의 영상 생성 AI 모델 및 리얼타임 3D 렌더링 인프라 역량 강화 조치로 풀이됩니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[분산 아키텍처]</strong> VFX Asset Pipeline &rarr; Conductor Dynamic Cloud Broker &rarr; Multi-Cloud Spot Instance Fleet &rarr; High-Throughput Frame Render
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                수만 개의 스팟 인스턴스를 동적으로 프로비저닝하고 프리엠션(Preemption) 시 무손실 체크포인트로 작업을 복구하는 분산 스케줄링 기술이 메타의 AI 파이프라인에 이식될 전망입니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.conductor.build/announcement" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              공식 인수 발표문 보기
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 9: Insects don't swarm at LED lights -->
      <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔥 132 pts</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.6시간 전</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 37.0 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;곤충은 사실 LED 불빛에 몰려들지 않는다&quot; : 조명 파장과 곤충 생태계의 비밀</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Birds Outside My Window — 백열등과 달리 자외선(UV)과 적외선이 없는 현대 LED 조명이 곤충의 주광성을 유발하지 않는 과학적 원리 분석 화제</span>
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
          <h3 class="minor-detail-headline">빛의 스펙트럼 차이가 바꾼 야간 생태계와 야외 컴퓨팅 환경</h3>
          <div class="minor-detail-subheadline">수은등과 백열등의 자외선 복사가 사라지며 야간 조명 설계의 새로운 지표 제공</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                여름철 야외 가로등이나 모니터 주변에 곤충들이 떼 지어 몰려들던 오랜 현상이 최근 몇 년간 급격히 줄어든 이유를 과학적으로 추적한 글입니다. 곤충의 시각 수용체가 반응하는 300~400nm 대역의 자외선이 일반 가정용 LED에는 거의 방출되지 않기 때문임이 밝혀졌습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[스펙트럼 비교]</strong> Incandescent / Mercury Bulb (Broad Spectrum + UV Spike) &rarr; Insect Phototaxis Trigger vs Modern Phosphor LED (Narrow Visible Spectrum, Zero UV) &rarr; Reduced Swarming
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                야외 스마트 시티 센서, 드론 탐색 조명, 그리고 데이터센터 야간 보안 조명 설계 시 곤충 침입으로 인한 오작동을 최소화하는 하드웨어 설계 가이드를 제공합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.birdsoutsidemywindow.org/2026/11/03/insects-dont-swarm-at-led-lights/" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              원문 연구 분석 읽기
            </a>
          </div>
        </div>
      </div>
"""
