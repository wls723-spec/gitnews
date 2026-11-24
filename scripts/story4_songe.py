# -*- coding: utf-8 -*-
# Story 4: sous-labs/songe (Idle-Compute Continual Local Model Training Engine)

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 4] sous-labs/songe : Idle-Compute Local Training    -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_songe.jpg" alt="Songe Idle Compute Continual Learning Engine Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="moon" style="width:12px;height:12px;"></i> CONTINUAL LEARNING</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🌙 내가 잠든 사이 스스로 진화하는 로컬 AI · HN 150점 · ★622</span>
              <span class="platform-tag">Hacker News &amp; Local ML</span>
              <span class="platform-tag">sous-labs / songe</span>
            </div>

            <h2 class="article-headline">
              "내가 자리를 비운 사이, 내 맥북이 스스로 모델 가중치를 훈련한다" — 유휴 연산 기반 연속 학습 엔진 'Songe'
            </h2>

            <div class="article-subheadline">
              opencode·pi·LM Studio·Ollama·MLX와 연동해 도구 실행 오류와 사용자 교정 기록을 로컬에만 쌓고, 노트북이 유휴 상태일 때 Quick Dream(지침 개선)과 Deep Dream(MLX 가중치 훈련)을 돌려 자가 검증 통과 시에만 모델을 교체 (Apache-2.0)
            </div>
            <p class="article-snippet">
              로컬 LLM을 아무리 오래 써도 어제 내가 고쳐준 코딩 스타일과 툴 에러를 내일이면 똑같이 까먹고 다시 실수합니다. 오늘 해커뉴스(<strong>150점·댓글 40개</strong>)와 GitHub(<strong>★622</strong>, 11월 20일 신생)에서 뜨거운 주목을 받은 <strong>sous-labs/songe</strong>는 인간 뇌의 수면 기억 응고화(Memory Consolidation)를 로컬 AI에 그대로 이식했습니다. 낮에는 평소처럼 <code>opencode</code>나 <code>Ollama</code>로 일하고, 밤에 자리를 비워 GPU와 배터리가 여유로워지면 백그라운드에서 <strong>Quick Dream·Deep Dream</strong> 훈련을 돌려 <strong>내 기존 대화 평가 세트를 통과한 새 모델만 안전하게 교체</strong>해 줍니다.
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
              <i data-lucide="flame"></i> 1. 리드: 낮에는 에러를 기록하고, 밤에는 꿈(Dream)을 꾸며 똑똑해지는 노트북
            </h3>
            <p>
              터미널 창에서 <code>uv tool install songe && songe init</code>을 입력하면, 설치 마법사가 내 컴퓨터에 깔린 LM Studio, Ollama, <code>llama.cpp</code>, <code>mlx-lm</code>, vLLM 서버와 코딩 에이전트(<code>opencode</code>, <code>pi</code> 등)를 자동으로 찾아낸다. 사용자가 동의 한 번만 누르면, 그 순간부터 에이전트의 모든 모델 호출은 <code>songe</code>라는 조용한 로컬 프록시를 거치기 시작한다.
            </p>
            <p>
              겉보기에는 평소와 다를 바 없다. 하지만 사용자가 에이전트에게 <em>"아니, 우리 프로젝트는 pytest 말고 uv run으로 돌려야 해"</em>라고 교정하거나, 도구가 에러 코드를 내뱉은 뒤 다음 턴에서 수정에 성공할 때마다 <code>songe</code>는 그 행동 궤적(Trace)을 클라우드로 단 한 바이트도 보내지 않고 오직 내 머신 안(<code>~/Library/Application Support/songe</code>)에만 차곡차곡 저장한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '프롬프트 파일(AGENTS.md) 땜질'을 넘어선 진짜 온디바이스 연속 학습
            </h3>
            <p>
              지금까지 AI 코딩 에이전트를 길들이는 방법은 매번 <code>CLAUDE.md</code>나 <code>AGENTS.md</code>에 규칙을 줄줄이 덧붙이는 수작업이었다. 컨텍스트 창은 점점 비대해지고, 로컬 소형 모델은 지시사항이 길어질수록 오히려 성능이 떨어졌다. 반대로 LoRA 파인튜닝을 직접 돌리자니 데이터셋 정제, 훈련 스크립트 세팅, 성능 저하(Catastrophic Forgetting) 검증까지 손이 너무 많이 갔다.
            </p>

            <div class="editorial-quote">
              <p>
                "평소처럼 작업하는 동안 Songe는 모델의 각 행동 뒤에 따라오는 도구 결과, 오류, 그리고 당신의 다음 교정 메시지를 조용히 관찰한다. <strong>에이전트가 조용해지고 유휴 연산이 남을 때 모델이 그 결과를 미리 내다보도록 훈련하며, 오직 당신 자신의 과거 대화 평가 체크를 통과한 새 버전만 교체 적용한다.</strong>"
              </p>
              <small>— sous-labs/songe 공식 프로젝트 아키텍처 (Apache-2.0)</small>
            </div>

            <p>
              프랑스어로 '꿈(Songe)'이라는 이름 그대로, 이 엔진은 개발자가 잠들거나 커피를 마시러 자리를 비운 유휴 시간(Idle Compute)을 자동으로 포착해 모델을 진화시킨다. 그리고 사용자가 키보드에 손을 대고 돌아오는 즉시 훈련을 멈추고 GPU 메모리를 비워 본래 작업에 방해가 되지 않게 물러선다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: Quick Dream · Deep Dream 이중 사이클과 무인 회귀 게이트
            </h3>
            <p>
              <code>sous-labs/songe</code>는 무작정 가중치를 덮어쓰는 위험을 피하기 위해 3단계 자율 수면 루프를 설계했다:
            </p>
            <ul>
              <li><strong>수면 조건 감시 &amp; 로컬 트레이스 수집:</strong> OpenAI 호환 프록시로 동작하면서 도구 호출 성공/실패 및 사용자 교정 대화를 기록한다. 시스템 데몬은 ① 에이전트가 유휴 상태인지, ② 가용 RAM/VRAM이 충분한지, ③ 노트북 배터리가 방전 위험에 있지 않은지 확인한 뒤에만 훈련을 개시한다.</li>
              <li><strong>이중 수면 모드 (Quick Dream vs Deep Dream):</strong> <code>Quick Dream</code>은 몇 분 안에 모델의 시스템 지침과 선호 규칙을 정제해 반영하고, <code>Deep Dream</code>은 Apple Silicon(MLX 기반 네이티브 훈련, Linux/Windows NVIDIA·AMD 지원) 위에서 실제로 모델 가중치 자체를 학습시킨다. 급할 때는 <code>songe sleep</code>으로 즉시 수동 훈련을 깨울 수도 있다.</li>
              <li><strong>자동 평가 게이트 &amp; 원클릭 롤백 (<code>songe undo</code>):</strong> 새 버전이 만들어져도 곧바로 승격되지 않는다. 사용자의 실제 과거 대화 기록으로 구성된 로컬 검증 세트를 통과해 기존 버전보다 확실히 나은 점수를 받아야만 로딩된 모델을 교체한다. 문제가 느껴지면 <code>songe undo MODEL</code>로 언제든 한 버전 전으로 되돌리고, <code>songe forget</code>으로 기록을 완전 파기할 수 있다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Songe 유휴 연산 기반 연속 학습(Quick/Deep Dream) &amp; 안전 게이트 구조</span>
                <span class="schematic-badge">Apache-2.0 · Apple MLX &amp; OpenAI-Compatible · 100% Offline</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Trace Capture (Active)</div>
                  <div class="schematic-desc">
                    <code>opencode</code> · <code>pi</code> ↔ <code>songe/</code> 프록시<br>
                    LM Studio · Ollama · llama.cpp · MLX 연동<br>
                    도구 에러 · 수정 · 사용자 교정 로컬 저장<br>
                    계정 · 텔레메트리 · 클라우드 전송 0%
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Idle Dreaming (Sleep)</div>
                  <div class="schematic-desc">
                    에이전트 유휴 · 메모리 · 배터리 상태 체크<br>
                    <strong>Quick Dream</strong>: 수 분 내 선호 지침 합성<br>
                    <strong>Deep Dream</strong>: Apple Silicon MLX 직접 학습<br>
                    사용자 복귀 시 즉시 일시중지 및 자원 반환
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Eval Gate &amp; Swap</div>
                  <div class="schematic-desc">
                    과거 대화 기반 회귀 체크 통과 필수<br>
                    합격 버전만 핫스왑 교체 배포<br>
                    <code>songe open</code> 대시보드 · <code>songe undo</code> 롤백<br>
                    <code>songe forget</code> 기록 즉시 삭제 보장
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">sous-labs/songe 공식 페이지 — 유휴 연산 로컬 모델 연속 학습 엔진 및 CLI 워크플로</span>
              </div>
              <img src="../assets/images/demo_songe.png" alt="Songe Sous Labs Local Training Engine" class="showcase-img">
              <p class="showcase-caption">
                ▲ souslabs.ai/songe 실화면: brew/pip 한 줄 설치(songe init)와 songe sleep·undo·open 대시보드 명령어 및 Apple MLX 지원 명세.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 산업적 함의: 빅테크 클라우드 '기억 독점'을 깨는 개인화된 로컬 가중치
            </h3>
            <p>
              OpenAI, Anthropic, Google 등 클라우드 AI 진영은 사용자의 선호와 과거 작업 맥락을 서버 측 '메모리(Memory)' 기능에 가둬 락인(Lock-in) 효과를 강화하고 있다. 반면 오픈소스 로컬 모델은 가중치를 받아올 수는 있어도 "나와 함께 일하며 진화하는 경험"이 빠져 있었다.
            </p>
            <ul>
              <li><strong>가중치 자체에 내장되는 개인 컨텍스트:</strong> <code>songe</code>는 사용자의 작업 습관이 외부 서버의 DB가 아니라, 내 노트북 디스크에 있는 오픈소스 모델(<code>Apache-2.0</code>)의 가중치와 어댑터 안에 축적되도록 만든다. 앞서 다룬 <code>Bonsai 2.5 27B</code> 같은 고성능 경량 로컬 모델과 결합될 때, 클라우드 구독을 해지해도 "내 코드베이스에 가장 익숙한 시니어 주니어 페어"를 영구 소유하는 길이 열린다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 노트북을 덮기 전, 모델에게도 잘 자라고 인사하는 시대
            </h3>
            <p>
              고정된 가중치를 내려받아 평생 똑같은 실수를 반복하던 '정적 AI'의 시대는 저물고 있다. 낮 동안 내가 투덜거리며 고쳐 준 사소한 코딩 습관과 에러 해결법을 밤사이 묵묵히 곱씹고, 다음 날 아침 커피를 내릴 때쯤 한 뼘 더 성숙해져 있는 로컬 모델.
            </p>
            <p>
              유휴 연산이라는 가장 값싸고 사적인 자원으로 AI를 성장시키는 <code>Songe</code>의 방식은, 개인용 컴퓨팅이 클라우드 거인들과 공존하거나 독립할 수 있는 가장 우아한 해답 중 하나다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=sous-labs+songe+local+model+training" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://souslabs.ai/songe" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> 공식 홈페이지 방문
              </a>
              <a href="https://github.com/sous-labs/songe" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
