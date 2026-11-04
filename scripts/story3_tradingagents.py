# -*- coding: utf-8 -*-
# Story 3: TauricResearch/TradingAgents

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] TauricResearch/TradingAgents : 퀀트 헤지펀드 멀티 에이전트 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_tradingagents.jpg" alt="TradingAgents Multi-Agent Financial Framework" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="trending-up" style="width:12px;height:12px;fill:#fff;"></i> 117K STARS</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">📈 금융 AI 패러다임 전환</span>
              <span class="aggro-tag">🔥 11.7만 스타 폭발 · 월스트리트 독점 인프라 붕괴</span>
              <span class="platform-tag">GitHub Trending & arXiv</span>
              <span class="platform-tag">TauricResearch / TradingAgents</span>
            </div>
            
            <h2 class="article-lead-headline">
              월스트리트 퀀트 헤지펀드의 민주화: 리서처·리스크 관리자·주문 집행관이 난상토론하는 멀티 에이전트 트레이딩 룸 'TradingAgents'
            </h2>

            <div class="article-subheadline">
              단일 LLM의 맹신 매매는 끝났다... 기본적 분석가, 기술적 차트 분석가, 뉴스 감성 분석가가 격돌하고 리스크 관리관이 최종 승인하는 기관급 자율 트레이딩 프레임워크 TradingAgents v0.7.1 전격 공개
            </div>
            <p class="article-snippet">
              SEC EDGAR 공시 실시간 파싱, 야후 파이낸스 뉴스 장애 우회 라우터, 마켓 휴장일과 최종 종가(Final Close) 기반의 결정론적 백테스팅. 개인의 ChatGPT Plus/Pro 플랜으로 월 수천만 원짜리 블룸버그 터미널급 포트폴리오를 자율 운용하는 퀀트 혁명.
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
              <i data-lucide="flame"></i> 1. 리드: 수조 원을 굴리는 월가 헤지펀드 트레이딩 룸이 깃허브에 풀리다
            </h3>
            <p>
              뉴욕 맨해튼 미드타운의 고층 빌딩에 자리 잡은 퀀트 헤지펀드의 트레이딩 플로어는 언제나 소수 엘리트들의 성역이었다. 
              연봉 수십억 원의 퀀트 리서처, 수학 박사 출신의 기술적 분석관, SEC 공시를 실시간 해부하는 법무 분석가, 그리고 포트폴리오 손실 한도를 통제하는 수석 리스크 관리관(CRO)이 
              초단위로 난상토론을 벌이며 조 단위의 자금을 집행한다. 
              일반 개인 투자자에게 이들의 무기는 넘볼 수 없는 철옹성이었다.
            </p>
            <p>
              그러나 2026년 10월, <strong>Tauric Research가 발표한 오픈소스 프레임워크 TradingAgents(TauricResearch/TradingAgents)</strong>가 
              <strong>누적 스타 11만 7,000개를 돌파</strong>하며 금융 생태계를 강타했다. 
              단 하나의 파이썬 패키지로, 헤지펀드 트레이딩 룸 전체를 구성하는 5대 전문 에이전트 스쿼드를 개인 터미널 안으로 통째로 소환한 것이다.
            </p>

            <div class="editorial-quote danger">
              "하나의 LLM에게 '이 주식 사야 해 말아야 해?'라고 묻는 것은 자살행위입니다. 
              모델은 쉽게 확증 편향에 빠지고 환각(Hallucination) 매수를 지시합니다. 
              <strong>진짜 헤지펀드가 돌아가는 유일한 이유는 '치열한 내부 견제와 난상토론' 때문입니다. 
              우리는 분석가들이 피 터지게 논쟁하고, 리스크 오피서가 차갑게 거부권을 행사하는 적대적 멀티 에이전트 의사결정 체계를 오픈소스로 구현했습니다.</strong>"
              <span class="quote-author">— Tauric Research 연구팀, arXiv:2412.20138 논문 서문 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: 환각을 부수는 '적대적 토론(Adversarial Debate)' 아키텍처
            </h3>
            <p>
              <code>TradingAgents</code>의 핵심 공학은 <strong>'역할 분담과 상호 견제(Checks and Balances)'</strong>다. 
              프레임워크 내부에는 각기 다른 데이터 소스와 사고 체계를 가진 5개의 에이전트가 격돌한다:
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="briefcase" style="color:#f59e0b;"></i> TradingAgents: 헤지펀드 트레이딩 플로어 5대 멀티 에이전트 의사결정 루프</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">ADVERSARIAL QUANT ENGINE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">AGENT 1. 펀더멘털 분석가</div>
                  <div class="step-title">SEC EDGAR Parser</div>
                  <div class="step-desc">10-K, 10-Q 재무제표, P/E, 잉여현금흐름(FCF), 부채비율을 엄밀 계량화하여 내재 가치 평가.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">AGENT 2. 기술적 차트 분석가</div>
                  <div class="step-title">Technical Quant</div>
                  <div class="step-desc">MACD, RSI, 볼린저 밴드, 지지·저항선 및 체결량 매물대를 분석하여 진입/청산 타점 포착.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">AGENT 3. 소셜 감성 분석가</div>
                  <div class="step-title">Market Sentiment</div>
                  <div class="step-desc">야후 파이낸스, X(트위터), 레딧 WSB 여론을 크롤링하고 루머 노이즈를 필터링하여 시장 심리 지수화.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">AGENT 4. 수석 리스크 관리관</div>
                  <div class="step-title">Risk Officer (Veto Gate)</div>
                  <div class="step-desc">최대 낙폭(MDD), VaR(Value at Risk) 한도 초과 시 분석가들의 매수 제안을 즉각 기각(거부권 발동).</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">AGENT 5. 포트폴리오 집행관</div>
                  <div class="step-title">Execution Manager</div>
                  <div class="step-desc">최종 승인된 비중만을 바탕으로 분할 매수·헤징 주문을 생성하고 장 마감 종가 기준 정산 리포트 발행.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="wrench"></i> 3. 기술 메커니즘 해부: 미래 데이터 누수를 차단한 무결점 백테스팅 v0.7.1
            </h3>
            <p>
              금융 머신러닝에서 가장 치명적인 결함은 **'미래 데이터 누수(Lookahead Bias)'**다. 
              즉, 백테스팅 모델이 2024년 5월 시점의 결정을 내릴 때, 6월에 제출된 수정 공시나 장 마감 후 뉴스를 미리 읽어버려 수익률이 왜곡되는 현상이다.
            </p>
            <p>
              이번 10월 최신 <code>v0.7.1</code> 업데이트에서 <code>TradingAgents</code>는 이 문제를 철저하게 봉쇄했다:
            </p>
            <ul style="margin: 1rem 0 1.5rem 1.5rem; line-height: 1.8; color: var(--text-dark);">
              <li><strong>엄격한 시점 격리(Timestamp Isolation):</strong> SEC 공시 제출 초 단위 타임스탬프를 검증하여 시뮬레이션 당일 이후의 데이터 접근을 물리적으로 차단.</li>
              <li><strong>휴장일 및 최종 종가 정산:</strong> 연휴나 마켓 휴장일에 발생한 거래 결정을 다음 영업일 장 마감 확정 종가(Final Close) 기준으로만 슬리피지(Slippage)를 반영해 보정.</li>
              <li><strong>ChatGPT Plus / Pro BYOK 지원:</strong> 고가의 엔터프라이즈 API 키 없이도 개인이 구독 중인 ChatGPT 웹 세션 자격을 연동해 무료로 구동 가능.</li>
              <li><strong>HTML 단일 보고서 자동 렌더링:</strong> 5개 에이전트의 논쟁 녹취록과 포트폴리오 수익률 곡선을 단 하나의 깔끔한 HTML 페이지로 익스포트.</li>
            </ul>

            <!-- 실제 소프트웨어 UI 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_tradingagents_cli.jpg" alt="TradingAgents 터미널 멀티 에이전트 트랜잭션 집행 화면" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>TradingAgents CLI 트랜잭션 실행 화면:</strong> 기본적 분석가와 기술적 분석가의 신호가 일치한 종목에 대해 수석 리스크 관리관이 포지션 사이징을 검토하고, 최종 주문 체결 및 손절선(Stop-loss)을 설정하는 실시간 터미널 트레이딩 로그.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="scale"></i> 4. 비즈니스 해자: 연 3천만 원짜리 블룸버그 터미널의 위기
            </h3>
            <p>
              블룸버그 터미널(Bloomberg Terminal)은 대당 연간 2만 5천 달러(약 3,500만 원)에 달하는 살인적인 구독료에도 불구하고, 전 세계 35만 금융인들의 필수품으로 군림해 왔다. 
              데이터의 독점과 방대한 분석 도구 때문이었다.
            </p>
            <p>
              그러나 <code>TradingAgents</code>는 오픈 데이터(SEC EDGAR, 야후 파이낸스, 오픈 뉴스 소스)와 프론티어 LLM의 추론 능력을 결합함으로써, 
              <strong>초고가 전용 단말기 없이도 기관급 크로스 체크 리서치를 자동화</strong>할 수 있음을 입증했다. 
              특히 고가의 자산운용 자문사를 고용할 여력이 없는 개인 투자자와 패밀리 오피스들에게 이 프레임워크는 판도를 뒤엎는 비대칭 전력이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 탐욕과 공포를 이기는 알고리즘의 절제
            </h3>
            <p>
              월스트리트의 전설적인 투자자 워런 버핏은 <em>"남들이 탐욕을 부릴 때 두려워하고, 남들이 두려워할 때 탐욕을 부려라"</em>고 했다. 
              하지만 감정을 가진 인간이 시장의 폭락 앞에서 이 원칙을 지키기란 불가능에 가깝다.
            </p>
            <p>
              <code>TradingAgents</code>의 가치는 높은 수익률 그 자체보다, <strong>군중 심리에 휩쓸리지 않고 수백 가지 지표와 리스크 규칙을 냉정하게 대조하는 규율(Discipline)</strong>에 있다. 
              금융의 미래는 더 이상 비밀스러운 트레이딩 룸 안에 갇혀 있지 않다. 오픈소스를 다운로드받는 모든 이의 터미널에서 지금 작동하고 있다.
            </p>

            <!-- 액션 버튼 링크 바 -->
            <div class="project-links-bar">
              <a href="https://arxiv.org/abs/2412.20138" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="file-text"></i> arXiv 연구 논문 읽기
              </a>
              <a href="https://www.youtube.com/results?search_query=TradingAgents+Multi-Agents+LLM+Financial+Trading+Framework" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/TauricResearch/TradingAgents" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 3 (tradingagents) module loaded successfully.")
