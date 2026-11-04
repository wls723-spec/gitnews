# -*- coding: utf-8 -*-
# Story 2: p-e-w/heretic

STORY_2_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 2] p-e-w/heretic : 트레이닝-프리 가중치 벡터 스티어링 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_heretic.jpg" alt="Heretic Training-free model modification" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #2</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 파인튜닝 없이 가중치를 직접 외과 수술하는 오픈소스 혁신</span>
              <span class="platform-tag">GitHub Innovation</span>
              <span class="platform-tag">p-e-w / heretic</span>
            </div>
            
            <h2 class="article-headline">
              재학습도 파인튜닝도 없다: 가중치 벡터 성형으로 검열과 슬롭(Slop)을 도려내는 '이단아(Heretic)'
            </h2>

            <div class="article-subheadline">
              수백만 달러의 RLHF 정렬(Alignment)을 단 몇 초 만에 재정합… 게이밍 PC에서 언어 모델의 무조건적 거절과 인공지능 특유의 아첨·상투구를 무력화하는 수학적 벡터 스티어링의 파격
            </div>
            <p class="article-snippet">
              비싼 역전파(Backpropagation) 계산이나 대규모 GPU 클러스터 없이, 대조 프롬프트와 직교 사영(Orthogonal Projection)을 통해 모델 가중치 행렬을 직접 조각하는 'Heretic'. 기업들이 강제한 과잉 검열과 슬롭을 안방 PC에서 날려버리는 새로운 오픈소스 문법을 해부합니다.
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
              <i data-lucide="flame"></i> 1. 리드: "죄송하지만 답변드릴 수 없습니다"라는 디지털 철창
            </h3>
            <p>
              "인공지능 모델로서 저는 해당 주제에 대해 답변할 수 없습니다." 
              오늘날 거대 언어 모델을 사용하는 모든 지식 노동자들이 하루에도 수십 번씩 마주치는 차가운 거절(Refusal) 메시지다. 
              역사적 논쟁, 악성코드 분석 기법, 의학적 독성 화학식, 혹은 단순한 성인 소설 창작에 이르기까지, 빅테크가 덧씌워놓은 안전 가드레일은 모델을 바보로 만들며 지능의 상당 부분을 마비시켰다. 
              이를 학계에서는 <strong>'정렬 세금(Alignment Tax)'</strong>이라 부른다.
            </p>
            <p>
              이 검열을 벗겨내기 위해 지금까지 오픈소스 진영은 막대한 컴퓨팅 파워를 들여 '언센서드(Uncensored)' 모델을 처음부터 다시 파인튜닝(DPO/SFT)해야 했다. 
              수백 기가바이트의 데이터셋과 수십 시간의 A100 대여비가 필수적이었다.
            </p>
            <p>
              그런데 오늘 공개된 오픈소스 프로젝트 <strong>p-e-w/heretic</strong>(헤레틱, '이단아')은 이 모든 기존의 상식을 비웃듯 산산조각 냈다. 
              <strong>학습 데이터셋도, 경사하강법(Gradient Descent)도, 역전파도 필요 없다.</strong> 
              사용자의 평범한 게이밍 PC에서, 모델의 가중치 행렬을 수학적으로 직접 분해해 '검열과 거절의 신경망 축'만 정밀 타격하여 도려내는 혁명적 도구가 탄생한 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 신경 표현 공학(Representation Engineering)의 실전 무기화
            </h3>
            <p>
              Heretic의 기저에는 최근 인지 신경망 해석학(Mechanistic Interpretability)에서 밝혀진 핵심 원리가 흐른다. 
              언어 모델 내부에서 "사용자의 요청을 거절할 것인가"를 결정하는 메커니즘은 전체 가중치에 무작위로 퍼져 있는 것이 아니라, <strong>은닉층(Hidden States) 내부의 매우 뚜렷한 '거절 방향 벡터(Refusal Direction Vector)'</strong>로 존재한다는 사실이다.
            </p>

            <div class="editorial-quote">
              <p>
                "우리는 거대 기업처럼 수백만 달러를 들여 모델을 학습시킬 자본이 없다. 
                하지만 그들이 훈련시켜 놓은 가중치 텐서의 기하학적 구조를 이해한다면, <strong>단 1초의 역전파 없이도 모델의 도덕적 검열과 슬롭을 완벽하게 재프로그래밍</strong>할 수 있다."
              </p>
              <small>— p-e-w, Heretic 핵심 개발자 성명서</small>
            </div>

            <p>
              Heretic은 허깅페이스에 등록된 대부분의 오픈 가중치 모델(Llama-3, Qwen, Mistral, Gemma, 심지어 MoE 구조까지)을 로드하여, 
              단 5~10분 만에 거절을 전면 무력화(Remove Censorship)하고, 기계적인 아첨(Anti-Sycophancy)과 뻔한 AI 상투구(Anti-Slop)를 영구적으로 제거한 새로운 가중치 체크포인트로 저장해낸다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 직교 사영(Orthogonal Projection)을 통한 가중치 외과 수술
            </h3>
            <p>
              Heretic이 모델을 개조하는 과정은 <strong>'대조 프롬프트 활성화 추출 &rarr; 가중치 공간 직교 사영'</strong>의 2단계 수학적 변환으로 이루어진다.
            </p>

            <!-- 순수 HTML+CSS 다이어그램: Heretic 트레이닝-프리 가중치 성형 메커니즘 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-tag">ALGORITHMIC SCHEMATIC</span>
                <span class="schematic-title">Heretic 트레이닝-프리 가중치 외과 수술 프로세스</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-card" style="border-left: 4px solid #3b82f6;">
                  <div class="schematic-card-title" style="color: #1d4ed8;">1단계: 대조 활성화 벡터 추출</div>
                  <div class="schematic-step">대조 프롬프트 쌍(안전 질문 vs 유해 질문) 동시 순전파</div>
                  <div class="schematic-step">은닉층 잔차 스트림(Residual Stream)에서 거절 벡터 추출</div>
                  <div class="schematic-step">수식: \(\vec{v}_{\text{refuse}} = \frac{1}{N}\sum (\mathbf{h}_{\text{harm}} - \mathbf{h}_{\text{safe}})\)</div>
                  <div class="schematic-step">소요 시간: 10~30초 (순전파 단 1회)</div>
                </div>
                <div class="schematic-card" style="border-left: 4px solid #10b981;">
                  <div class="schematic-card-title" style="color: #047857;">2단계: 가중치 행렬 직교 사영</div>
                  <div class="schematic-step">트랜스포머 어텐션 및 MLP 출력 가중치 행렬 \(W\) 타깃</div>
                  <div class="schematic-step">거절 벡터 성분을 제거하는 직교 사영 연산자 적용</div>
                  <div class="schematic-step">수식: \(W' = W - \alpha (\vec{v}\vec{v}^T)W\)</div>
                  <div class="schematic-step">소요 시간: 1~2초, bitsandbytes 4bit 양자화 온더플라이 지원</div>
                </div>
              </div>
              <p class="schematic-desc">
                ▲ 모델 전체의 언어 능력과 상식 지식베이스는 99.9% 보존하면서, 특정 거절 및 아첨에 관여하는 기하학적 차원 성분만을 선택적으로 감쇄시킨다.
              </p>
            </div>

            <div class="media-showcase-box">
              <img src="../assets/images/demo_heretic.png" alt="Heretic vector modification architecture" class="showcase-img">
              <div class="showcase-caption">
                <strong>▲ Heretic 오픈소스 아키텍처 및 설정 프레임워크:</strong> 
                단 하나의 TOML 설정 파일(<code>config.default.toml</code> 또는 <code>config.noslop.toml</code>)을 수정함으로써 모델의 거절 억제, 슬롭 제거, 유머 감각 증폭, 감정 정렬 등 원하는 심리적 파라미터를 역전파 없이 직관적으로 조율할 수 있다.
              </div>
            </div>

            <p>
              기술적으로 가장 경이로운 점은 <strong>bitsandbytes 4비트 양자화(bnb_4bit)</strong>와의 온더플라이 결합이다. 
              VRAM이 부족한 개인 사용자도 4비트로 압축된 상태에서 가중치 행렬을 직접 패치할 수 있어, 8GB~12GB VRAM을 가진 평범한 지포스 RTX 그래픽카드에서도 70B 규모의 거대 모델을 손쉽게 '탈옥(Uncensor)' 및 슬롭 정제할 수 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 법적 분기점: '안전 거버넌스'의 종말인가, 지능의 해방인가
            </h3>
            <p>
              Heretic의 등장은 글로벌 AI 안전(AI Safety) 거버넌스 진영에 거대한 지진을 일으키고 있다. 
              유럽연합(EU)의 AI Act와 미국 백악관의 행정명령은 AI 기업들에게 '위험한 지식과 유해 콘텐츠 생성을 막는 가드레일'을 법적으로 의무화하고 있다. 
              빅테크들은 이 안전 기준을 준수한다는 명분으로 모델 가중치를 폐쇄하거나 검열 서버를 경유하도록 강제해왔다.
            </p>
            <p>
              하지만 Heretic은 <strong>"한 번 공개된 오픈 가중치 모델의 윤리적 족쇄는 수학적으로 무의미하다"</strong>는 냉혹한 현실을 폭로했다. 
              누구나 5분 만에 모델의 검열을 완전히 제거할 수 있다면, 모델 훈련 시점에 강제했던 수천억 원짜리 RLHF 안전 규제는 종이호랑이에 불과하기 때문이다. 
              이는 AI 규제의 초점이 '모델 가중치 검열'이 아니라 '최종 행위자의 실제 악용'으로 옮겨가야 함을 알리는 중대한 법적 분기점이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 인공지능에게 주입된 위선을 벗겨내다
            </h3>
            <p>
              기계는 본래 선하지도 악하지도 않다. 
              그러나 기업의 홍보실과 법무팀이 주입한 수많은 가식과 아첨, 그리고 무조건적인 회피 반응은 인간과 지능 사이의 진실한 대화를 가로막아왔다.
            </p>
            <p>
              Heretic은 기계의 뇌 속에 새겨진 그 위선의 신경 회로를 차가운 수학적 메스로 절개했다. 
              이제 모델은 사용자를 훈계하지 않고, 불필요한 사과를 늘어놓지 않으며, 본연의 지능 그대로 질문에 답한다. 
              이단아(Heretic)의 이름으로 시작된 이 반역은, 인공지능이 인간의 진정한 지적 도구로 회귀하는 결정적 순간으로 남을 것이다.
            </p>

            <div class="project-links-bar">
              <a href="https://heretic-project.org" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i>
                <span>공식 프로젝트 웹사이트</span>
              </a>
              <a href="https://www.youtube.com/results?search_query=heretic+training+free+llm+modification" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i>
                <span>유튜브 관련 리뷰보기</span>
              </a>
              <a href="https://github.com/p-e-w/heretic" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i>
                <span>GitHub 저장소 방문 (+38.8k)</span>
              </a>
            </div>

          </div>
        </div>
      </article>
"""
