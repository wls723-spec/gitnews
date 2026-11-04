# -*- coding: utf-8 -*-
# Story 1: karpathy/nanochat (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] karpathy/nanochat : 오늘의 메인 기사 (COVER STORY) -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_nanochat.jpg" alt="Andrej Karpathy nanochat" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔥 거대 자본 AI 인플레이션을 잠재우는 100달러짜리 ChatGPT</span>
              <span class="platform-tag">GitHub Breakthrough</span>
              <span class="platform-tag">karpathy / nanochat</span>
            </div>
            
            <h2 class="main-lead-headline">
              <span id="hero-title">$100로 빚어낸 챗GPT, 거대 자본 AI 학습 독점의 허상을 깨부수다</span>
            </h2>

            <div class="article-subheadline">
              안드레이 카파시의 'nanochat', 단 한 대의 8xH100 노드와 1.65시간 만에 GPT-2 능가… 단 하나의 복잡도 다이얼(--depth)로 가중치와 하이퍼파라미터를 최적 도출하며 'Time-to-GPT-2' 스피드런으로 증명한 오픈소스 효율의 기적
            </div>
            <p class="article-snippet">
              2019년 수만 달러(약 5천만 원)가 들던 GPT-2급 언어 모델 학습을 단 48달러(스팟 인스턴스 15달러)로 압축한 안드레이 카파시의 파격적 미니멀 하네스 'nanochat'. 토크나이징부터 사전학습, 파인튜닝, 추론까지 단일 GPU 노드에서 완결짓는 오픈소스의 반격을 조명합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 수천억 원의 인프라 신화에 던져진 48달러짜리 계산서
            </h3>
            <p>
              실리콘밸리의 AI 자본가들은 지난 수년간 하나의 거대한 교리를 주입해왔다. "지능을 얻으려면 수천 개의 최신 H100 GPU 클러스터가 필요하며, 수천억 원의 전기세와 거대 데이터센터를 감당할 수 있는 빅테크만이 미래를 소유할 수 있다." 
              이 자본의 장벽 앞에서 일반 개발자와 스타트업들은 거대 AI 벤더의 API에 종속된 디지털 소작농으로 전락하고 있었다.
            </p>
            <p>
              하지만 오늘, 테슬라 AI 디렉터이자 오픈AI 창립 연구원이었던 <strong>안드레이 카파시(Andrej Karpathy)</strong>가 이 거대한 허상에 가장 우아하고 파괴적인 균열을 냈다. 
              그가 기습 공개한 오픈소스 프로젝트 <strong>karpathy/nanochat</strong>은 "100달러로 살 수 있는 가장 완벽한 챗GPT"를 표방하며 깃허브 트렌딩 1위에 직행, 공개 수일 만에 6만 개 이상의 스타를 집어삼켰다.
            </p>
            <p>
              카파시가 내놓은 계산서는 충격적이었다. 2019년 오픈AI가 수만 달러(약 43,000달러)를 들여 수주일 동안 땀 흘려 학습시켰던 <strong>GPT-2급 지능을, 단 한 대의 8xH100 GPU 노드에서 불과 1.65시간(약 48달러, 스팟 인스턴스 기준 약 15달러)</strong> 만에 바닥부터 완벽하게 학습시켜 대화할 수 있는 초경량 파이프라인을 완성한 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '복잡도의 장사치'들에게 돌아간 원칙의 철퇴
            </h3>
            <p>
              AI 연구 생태계는 지난 몇 년간 기형적으로 비대해졌다. 수십 개의 난해한 프레임워크, 불투명한 하이퍼파라미터 튜닝, 복잡한 분산 클러스터 도구들이 얽히며 "AI 학습은 평범한 인간의 손을 떠났다"는 인식이 팽배했다. 
              그러나 카파시는 1차 원리(First Principles)로 되돌아가 기술의 본질을 묻는다.
            </p>

            <div class="editorial-quote">
              <p>
                "2019년 GPT-2 학습에 43,000달러가 들었지만, 7년간 스택 전반에 걸친 눈부신 알고리즘 진보 덕분에 이제 우리는 <strong>단 48달러, 2시간 이내</strong>에 이 기준을 넘어설 수 있다. 
                지능의 문턱은 낮아졌고, 학습은 다시 개별 엔지니어의 책상 위로 돌아왔다."
              </p>
              <small>— 안드레이 카파시, nanochat 릴리즈 공식 노트</small>
            </div>

            <p>
              <code>nanochat</code>은 단순한 튜토리얼 코드가 아니다. 
              토크나이저(Tokenizer) 빌드부터 바닥부터 시작하는 사전 학습(Pretraining), 지시어 파인튜닝(Instruct SFT), DCLM CORE 벤치마크 평가, 그리고 로컬 CLI 인터랙티브 서빙까지 <strong>전체 LLM 수명 주기를 단 하나의 간결하고 해킹 가능한 파이썬 저장소</strong> 안에 군더더기 없이 담아냈다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘 해부: 단 하나의 다이얼 '--depth'와 오토연구(AutoResearch)
            </h3>
            <p>
              <code>nanochat</code>의 기술적 정수는 <strong>'단일 복잡도 다이얼'</strong>과 <strong>'GPT-2 스피드런(Speedrun) 파이프라인'</strong>의 결합에 있다.
            </p>
            <p>
              수십 개의 하이퍼파라미터(트랜스포머 너비, 어텐션 헤드 수, 학습률 감쇠 스케줄, 가중치 감쇠 등)를 일일이 수동 조정해야 했던 기존 모델들과 달리, nanochat은 단 하나의 플래그인 <code>--depth</code>(트랜스포머 레이어 수)만 지정하면 스케일링 법칙(Scaling Laws)에 기반해 나머지 모든 최적 변수를 수학적으로 자동 산출한다.
            </p>

            <!-- 순수 HTML+CSS 다이어그램: nanochat 초고속 사전학습 파이프라인 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-tag">ARCHITECTURE SCHEMATIC</span>
                <span class="schematic-title">nanochat 단일 노드 GPT-2 스피드런 파이프라인</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-card" style="border-left: 4px solid #ef4444;">
                  <div class="schematic-card-title" style="color: #b91c1c;">2019년 전통적 방식 (OpenAI GPT-2)</div>
                  <div class="schematic-step">1. 32~64개 V100 GPU 클러스터 분산 학습</div>
                  <div class="schematic-step">2. 168시간(7일) 연속 가동, 43,000달러 소모</div>
                  <div class="schematic-step">3. FP32/FP16 혼합 정밀도 및 느린 I/O 파이프라인</div>
                  <div class="schematic-step">4. 복잡한 수동 하이퍼파라미터 그리드 서치</div>
                </div>
                <div class="schematic-card" style="border-left: 4px solid #10b981;">
                  <div class="schematic-card-title" style="color: #047857;">2026년 nanochat 방식 (Karpathy)</div>
                  <div class="schematic-step">1. 단일 8xH100 노드 uv 기반 미니멀 환경</div>
                  <div class="schematic-step">2. 1.65시간 만에 완료, 48달러(스팟 15달러) 비용</div>
                  <div class="schematic-step">3. NVIDIA ClimbMix 데이터셋 + 네이티브 FP8 텐서 가속</div>
                  <div class="schematic-step">4. --depth 단일 다이얼 자동 최적 스케일링 + AutoResearch</div>
                </div>
              </div>
              <p class="schematic-desc">
                ▲ nanochat은 분산 통신 오버헤드를 완전히 제거하고 최신 FP8 연산과 고효율 토큰 스트리밍을 결합하여 시간당 학습 수렴 효율을 극대화했다.
              </p>
            </div>

            <div class="media-showcase-box">
              <img src="../assets/images/demo_nanochat.png" alt="nanochat scaling laws and speedrun leaderboard" class="showcase-img">
              <div class="showcase-caption">
                <strong>▲ nanochat 스케일링 법칙 및 GPT-2 스피드런 벤치마크:</strong> 
                DCLM CORE 기준선(0.2565)을 돌파하기까지의 소요 시간이 초기 3.04시간에서 FP8 도입(2.91h), 1M 배치 확장(2.76h), ClimbMix 데이터셋 전환(2.02h), 그리고 자율 연구 에이전트(AutoResearch Round 2)를 거치며 1.65시간까지 단축되는 과정을 실측 그래프로 입증하고 있다.
              </div>
            </div>

            <p>
              학습 데이터셋으로는 엔비디아의 정제된 <strong>ClimbMix</strong>를 사용하여 양질의 고밀도 지식을 주입하며, 1M 토큰 배치와 FP8 정밀도 텐서 코어를 극한까지 쥐어짜 낸다. 
              또한 카파시는 <code>autoresearch</code> 루프를 도입해, 에이전트가 스스로 가설을 세우고 학습률과 옵티마이저를 튜닝하며 'GPT-2 도달 시간'을 매주 단축시키는 글로벌 스피드런 리더보드를 가동하고 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 수조 원대 AI 인프라 버블을 찌르는 바늘
            </h3>
            <p>
              월스트리트와 실리콘밸리는 현재 수천억 달러 규모의 GPU 인프라 투자 회수 가능성을 두고 극심한 불안에 휩싸여 있다. 
              거대 클라우드 제공업체들은 고객들에게 수억 원 단위의 전용 클러스터 계약을 강요해왔다.
            </p>
            <p>
              하지만 <code>nanochat</code>이 증명한 것은 잔인할 만큼 명확하다. 
              <strong>"소프트웨어 알고리즘의 진보 속도가 하드웨어의 자본 장벽을 무력화하고 있다."</strong> 
              수만 달러의 예산이 들던 모델 훈련이 단 50달러 미만의 점심값 수준으로 내려왔다는 것은, 중소기업과 연구팀이 더 이상 빅테크의 독점 API에 매달리지 않고 사내 데이터로 맞춤형 지능 모델을 직접 구워낼 수 있는 시대가 열렸음을 의미한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 가장 강력한 지능은 가장 간결한 코드에서 나온다
            </h3>
            <p>
              안드레이 카파시가 보여준 <code>nanochat</code>의 진정한 충격은 1.65시간이라는 숫자 자체가 아니다. 
              수백 명의 엔지니어와 복잡한 프레임워크가 뒤엉켜 있던 자리에, 한 명의 거장이 수작업으로 깎아낸 몇 백 줄의 깨끗한 파이썬 코드가 가져온 '단순함의 해방'이다.
            </p>
            <p>
              AI의 미래는 전 세계 전력을 삼키는 거대한 비밀 데이터센터에 갇혀 있지 않다. 
              원리를 이해하고, 불필요한 군더더기를 걷어내며, 기계의 본질을 꿰뚫는 오픈소스의 미학 속에 있다. 
              100달러짜리 지능의 문이 활짝 열렸다.
            </p>

            <div class="project-links-bar">
              <a href="https://www.youtube.com/results?search_query=andrej+karpathy+nanochat+speedrun" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i>
                <span>유튜브 관련 리뷰보기</span>
              </a>
              <a href="https://github.com/karpathy/nanochat" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i>
                <span>GitHub 저장소 방문 (+60.2k)</span>
              </a>
            </div>

          </div>
        </div>
      </article>
"""
