# -*- coding: utf-8 -*-
# Story 3: experientiallabs/experiential

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] experientiallabs/experiential : 지능형 LLM 게이트웨이 & 지속적 모델 증류 -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_experiential.jpg" alt="Experiential Intelligent AI Traffic Gateway" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="play" style="width:12px;height:12px;fill:#fff;"></i> YOUTUBE 76K</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🚀 깃허브 스타 +1,224개 폭증 1위</span>
              <span class="aggro-tag">💸 API 비용 80% 절감 & 독자 모델 자산화</span>
              <span class="platform-tag">GitHub Trending</span>
              <span class="platform-tag">experientiallabs / experiential</span>
            </div>
            
            <h2 class="article-lead-headline">
              빅테크 LLM 종속과 API 요금 폭탄을 끊는다: 실시간 사내 트래픽을 학습해 독자 모델을 빚어내는 오픈소스 제로마진 게이트웨이 'Experiential'
            </h2>

            <div class="article-subheadline">
              "Turn your production traffic into a custom router and a model you own" — Experiential Labs, 1,000개 이상의 상용·오픈소스 모델을 단일 OpenAI 규격으로 통합하고, 유저 트래픽 패턴을 실시간 분석해 최저가 모델 자동 라우팅 및 사내 전용 LoRA 파인튜닝 모델을 자동 증류하는 오픈소스 AI 게이트웨이 공개
            </div>
            <p class="article-snippet">
              매달 수천만 원씩 빅테크에 바치던 LLM API 청구서를 80% 줄이고, 그 트래픽 데이터를 바탕으로 외부 유출 없이 사내 인프라에서 구동되는 자체 경량 언어모델(SLM)을 스스로 빚어내는 지능형 게이트웨이. 제로 마크업, 완전 무료 오픈소스로 깃허브 트렌딩을 강타했다.
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
              <i data-lucide="trending-down"></i> 1. 리드: 매달 날아오는 수천만 원의 API 청구서, 그리고 소작농의 굴레
            </h3>
            <p>
              AI 에이전트와 LLM 서비스를 도입한 수많은 스타트업과 기업들이 공통적으로 맞닥뜨리는 공포가 있다. 
              바로 매월 말 오픈AI(OpenAI), 앤스로픽(Anthropic), 구글(Google)로부터 날아오는 <strong>눈덩이처럼 불어난 API 사용료 인보이스(Invoice)</strong>다.
            </p>
            <p>
              서비스 이용자가 조금만 늘어나도 토큰 비용은 기하급수적으로 치솟지만, 서비스 개발사에게 남는 것은 아무것도 없다. 
              빅테크의 독점 모델에 의존하는 한, 기업들은 비싼 임대료를 내며 남의 땅을 일구는 <strong>'디지털 소작농'</strong>의 지위에서 영원히 벗어날 수 없었다. 
              더욱 뼈아픈 사실은, 매일 수백만 건씩 발생하는 사용자의 소중한 도메인 프롬프트와 피드백 데이터가 빅테크의 서버로 흘러 들어갈 뿐, 자사만의 고유한 인공지능 자산으로 전혀 축적되지 못했다는 점이다.
            </p>
            <p>
              2026년 10월 26일, 깃허브에서 단 하루 만에 <strong>1,200개 이상의 스타를 쓸어 담으며 전체 트렌딩 1위에 오른 'Experiential(experientiallabs/experiential)'</strong>은 이 불공정한 게임의 룰을 정면으로 타격하며 등장했다. 
              마진율 0%의 완전 오픈소스 게이트웨이로, 기업의 일상적인 프로덕션 트래픽을 관측하여 <strong>"비용은 80% 깎고, 그 트래픽으로 기업이 100% 소유하는 자체 특화 모델을 스스로 학습시킨다"</strong>는 급진적인 해법을 제시한 것이다.
            </p>

            <div class="editorial-quote">
              "기업들은 왜 단순한 JSON 포맷팅이나 데이터 추출 따위의 작업에 100만 토큰당 15달러짜리 최고급 프론티어 모델을 낭비하고 있는가? 
              <strong>트래픽은 비용이 아니라 원유(Crude Oil)다.</strong> 
              Experiential은 매 순간 흐르는 요청을 정제하여 가장 저렴한 모델로 흘려보내고, 동시에 그 데이터로 당신의 회사가 영구 소유할 전용 모델을 증류해 낸다."
              <span class="quote-author">— Experiential Labs 아키텍처 백서 중</span>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 2. 넛 그라프: '단순 프록시'를 넘어선 '자가 진화형 라우팅 엔진'
            </h3>
            <p>
              시중에는 이미 여러 오픈소스 LLM 프록시들이 존재한다. 
              그러나 기존 도구들은 엔드포인트를 하나로 묶어주는 정적 스위치보드에 불과했다. 
              반면 <code>Experiential</code>은 <strong>지속적 학습(Continuous Learning) 루프가 내장된 동적 두뇌</strong>다.
            </p>
            <p>
              개발팀은 단 한 줄의 환경변수(<code>OPENAI_BASE_URL="http://localhost:8000/v1"</code>)만 바꾸면 된다. 
              그 순간부터 게이트웨이는 인입되는 모든 쿼리의 복잡도, 문맥 길이, 의미론적 도메인을 실시간 임베딩하여, 최고가 프론티어 모델(Claude 3.5 Sonnet, GPT-5)과 초저가 오픈소스 모델(Llama 3.3, Qwen 2.5, DeepSeek V3) 사이에서 최적의 비용-품질 균형점을 스스로 찾아 배분한다.
            </p>

            <!-- 순수 HTML/CSS 에디토리얼 아키텍처 다이어그램 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span><i data-lucide="network" style="color:#3b82f6;"></i> Experiential: 5단계 트래픽 라우팅 & 자가 증류(Self-Distillation) 파이프라인</span>
                <span style="font-size:0.75rem; color:#94a3b8; font-weight:700; letter-spacing:0.05em; background:rgba(255,255,255,0.06); padding:0.2rem 0.6rem; border-radius:4px;">CONTINUOUS LEARNING GATEWAY</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box step-1">
                  <div class="step-tag">PHASE 1. 단일 규격 인입</div>
                  <div class="step-title">OpenAI-Compatible Ingress</div>
                  <div class="step-desc">기존 코드 수정 없이 SDK, LangChain, Claude Code 트래픽을 단일 엔드포인트로 무중단 수용.</div>
                </div>
                <div class="schematic-box step-2">
                  <div class="step-tag">PHASE 2. 의미론적 난이도 판별</div>
                  <div class="step-title">Semantic Difficulty Classifier</div>
                  <div class="step-desc">쿼리 임베딩과 복잡도를 1.2ms 만에 측정. 단순 포맷팅/요약과 고난도 추론 과업을 정밀 분리.</div>
                </div>
                <div class="schematic-box step-3">
                  <div class="step-tag">PHASE 3. 지능형 티어다운 라우팅</div>
                  <div class="step-title">Dynamic Smart Routing</div>
                  <div class="step-desc">단순 과업은 비용이 90% 저렴한 로컬/소형 SLM으로, 복잡한 전략 질의만 프론티어 LLM으로 우회.</div>
                </div>
                <div class="schematic-box step-4">
                  <div class="step-tag">PHASE 4. 고품질 입출력 증류</div>
                  <div class="step-title">Telemetry & Synthetic Pair</div>
                  <div class="step-desc">프론티어 모델이 성공적으로 수행한 고난도 쿼리-응답 쌍을 사내 데이터 레이크에 익명화 수집.</div>
                </div>
                <div class="schematic-box step-5">
                  <div class="step-tag">PHASE 5. 사내 맞춤형 LoRA 학습</div>
                  <div class="step-title">Continuous LoRA Distillation</div>
                  <div class="step-desc">일정 트래픽이 쌓이면 오픈소스 베이스 모델에 사내 전용 LoRA 가중치를 자동 파인튜닝하여 자체 배포.</div>
                </div>
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="wrench"></i> 3. 기술 메커니즘 해부: 사용자별 예산 격리와 자동 페일오버
            </h3>
            <p>
              <code>Experiential</code>의 프로덕션 완성도를 증명하는 기술적 특징은 엔터프라이즈 거버넌스와 결합된 세분화된 통제력이다.
            </p>
            <p>
              <strong>1) 사용자 및 에이전트 단위 가상 예산(Budgeting):</strong><br>
              수십 명의 사내 개발자와 수백 개의 자동화 에이전트가 단일 API 키를 공유할 경우, 특정 루프 버그 하나로 하룻밤 사이에 수천 달러가 결제되는 사고가 빈번하다. 
              Experiential은 각 사용자 아이덴티티(Identity) 및 에이전트 슬러그마다 개별 월간 예산 한도(예: <code>$50.00</code>)를 부여하고, 한도 초과 시 자동으로 무료 로컬 모델로 강제 강등(Downgrade)시키거나 요청을 안전하게 차단한다.
            </p>
            <p>
              <strong>2) 실시간 제로 지연 헬스체크 및 멀티 벤더 자동 페일오버:</strong><br>
              오픈AI 서버가 500 에러를 뿜거나 앤스로픽 API 응답 지연이 10초를 초과하면, 게이트웨이가 20ms 이내에 감지하고 동일한 능력을 가진 백업 공급자(DeepSeek, Google Vertex, 사내 vLLM 클러스터)로 세션을 무중단 텔레포트시킨다.
            </p>

            <!-- 실제 소프트웨어 UI / 대시보드 실구동 캡처 쇼케이스 -->
            <div class="media-showcase-box">
              <img src="../assets/images/demo_experiential_dashboard.jpg" alt="Experiential 프로덕션 워크스페이스 실시간 모델 트래픽 및 비용 절감 대시보드" class="media-showcase-img">
              <div class="media-caption">
                <i data-lucide="check-circle-2" style="width:16px;height:16px;color:#10b981;"></i>
                <strong>실제 Experiential 프로덕션 워크스페이스 대시보드 화면:</strong> 인입되는 모델별 트래픽 분포, 사용자 아이덴티티별 실시간 지출 현황, 스마트 라우팅을 통해 기존 대비 80% 이상 절감된 비용 곡선, 그리고 사내 전용 모델 파인튜닝을 위해 실시간 정제 중인 합성 데이터셋의 텔레메트리 현황.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="scale"></i> 4. 비즈니스 해자: 데이터 주권(Data Sovereignty)과 기업 가치 방어
            </h3>
            <p>
              AI 시대에 기업의 진정한 해자(Moat)는 <strong>"빅테크의 범용 모델이 결코 학습하지 못한 우리 회사만의 고유한 비즈니스 지식"</strong>에서 나온다.
            </p>
            <p>
              모든 트래픽을 상용 API로만 쏟아붓는 회사는 시간이 흐를수록 빅테크의 알고리즘 개선에만 기여할 뿐, 자사 고유의 지적 재산권(IP)을 형성하지 못한다. 
              반면 <code>Experiential</code>을 인프라 전면에 배치한 회사는 서비스가 성장할수록 사내 전용 소형 모델(SLM)이 점점 더 똑똑해지는 <strong>'플라이휠(Flywheel) 효과'</strong>를 누리게 된다.
            </p>
            <p>
              결국 빅테크의 API 가격 인상이나 정책 변경에도 끄떡없는 강력한 협상력을 확보하게 되며, 금융·의료 등 민감한 데이터 주권이 필수적인 산업군에서 완벽한 프라이버시 컴플라이언스를 달성하게 된다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 5. 키커: 소작농의 시대를 끝내는 오픈소스의 선언
            </h3>
            <p>
              과거 클라우드 컴퓨팅 초창기에 모든 기업이 AWS의 독점 서비스에 갇혔을 때, 쿠버네티스(Kubernetes)와 도커라는 오픈소스가 등장하여 인프라의 자유를 되찾아주었던 역사를 우리는 기억한다.
            </p>
            <p>
              지금 AI 인프라 시장에서 일어나는 일도 정확히 동일하다. 
              <code>Experiential</code>은 특정 빅테크 클라우드의 거대한 울타리 안에서 떨고 있던 전 세계 엔지니어들에게 <strong>"당신의 트래픽으로 당신의 모델을 직접 소유하라"</strong>고 외치고 있다. 
              디지털 소작농의 시대는 저물고 있으며, 자립과 주권의 새로운 깃발이 올라섰다.
            </p>

            <!-- 액션 버튼 링크 바 (독립 웹 데모 존재) -->
            <div class="project-links-bar">
              <a href="https://platform.experientiallabs.ai" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> 🌐 독립 웹 데모 바로 체험
              </a>
              <a href="https://www.youtube.com/results?search_query=experiential+ai+gateway+llm+router" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> ▶️ 유튜브 관련 리뷰보기
              </a>
              <a href="https://github.com/experientiallabs/experiential" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""

print("Story 3 (experiential) module loaded successfully.")
