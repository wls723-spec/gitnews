# -*- coding: utf-8 -*-
# Story 4: FareedKhan-dev/kimi-k3-in-c (HERO 4)

STORY_4_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 4] FareedKhan-dev/kimi-k3-in-c -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_kimi_k3.jpg" alt="kimi-k3-in-c" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="cpu" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #4</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 2.78조 파라미터를 8GB 노트북 CPU로 구동</span>
              <span class="platform-tag">GitHub Trending #4</span>
              <span class="platform-tag">FareedKhan-dev / kimi-k3-in-c</span>
            </div>
            
            <h2 class="article-headline">
              "GPU도, 거대 RAM도 필요 없다" — 2.78조 Kimi K3를 8GB CPU로 돌린 C99 엔진
            </h2>

            <div class="article-subheadline">
              1.56TB 크기의 체크포인트를 단 8.24GB 메모리 환경에서 순수 C언어로 추론 구동… Dense 트렁크 인메모리 상주와 NVMe 온디맨드 Sparse MoE 스트리밍 곱셈으로 바이트 단위 동일성 보장
            </div>
            <p class="article-snippet">
              수억 원대 GPU 클러스터가 필수적이라 여겨졌던 문샷 AI(Moonshot AI)의 2.78-trillion 파라미터 초거대 MoE 모델 Kimi K3를 평범한 노트북 CPU와 8GB RAM에서 순수 C99로 실행시킨 경이로운 오픈소스 추론 아키텍처를 분석합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 1.56TB 거인을 8GB 작은 방에 집어넣다
            </h3>
            <p>
              파라미터 수 2.78조 개(2.78-Trillion). 체크포인트 파일 용량만 1.56테라바이트(TB). 
              중국의 문샷 AI(Moonshot AI)가 공개한 초거대 MoE(Mixture of Experts) 모델 Kimi K3를 구동하려면 통상 H100 GPU 8대로 구성된 억 단위 서버 수 대가 동원되어야 마땅하다.
            </p>
            <p>
              그러나 오늘 깃허브 오픈소스 생태계에 경종을 울린 프로젝트 <strong>FareedKhan-dev/kimi-k3-in-c</strong>는 이 상식을 통쾌하게 뒤엎었다. 
              최신 GPU는커녕 외장 그래픽카드도 없는 <strong>단일 CPU, 고작 8.24GB RAM</strong>을 탑재한 일반 노트북에서 Kimi K3의 전체 추론을 성공적으로 완결시킨 것이다. 
              심지어 그 결과물은 거대 GPU 서버에서 나온 출력과 <strong>바이트 단위까지 100% 동일(Byte-identical)</strong>하다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 프레임워크 0, BLAS 0 — 100% 포터블 C99의 힘
            </h3>
            <p>
              이 놀라운 엔지니어링의 바탕에는 현대 딥러닝 프레임워크의 비대한 추상화를 걷어내고 컴퓨터 하드웨어의 바닥까지 내려간 C99 시스템 프로그래밍이 자리 잡고 있다.
            </p>

            <div class="editorial-quote danger">
              <p>
                "GPU 없음, 파이토치 없음, BLAS 라이브러리 없음. 
                가장 작은 8GB 머신부터 128GB 이상의 대형 서버까지 동일한 프롬프트에 대해 바이트 단위로 완벽하게 동일한 답을 낸다. 바뀌는 것은 오직 '시계의 속도'뿐이다."
              </p>
              <small>— Fareed Khan, kimi-k3-in-c 기술 백서</small>
            </div>

            <p>
              토큰당 연산 속도는 노트북 프리셋 기준 평균 32.69초로 느리지만, 1.56TB 모델이 단 8.24GB의 피크 메모리(Peak RSS)만으로 한 치의 오차 없이 답변을 생성해내는 장면은 컴퓨터 과학의 경이로움 그 자체다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: Dense Trunk 상주와 NVMe 스트리밍 곱셈
            </h3>
            <p>
              어떻게 1.56TB의 가중치를 8GB 메모리에서 연산할 수 있을까? 비결은 Kimi K3의 희소 MoE(Sparse Mixture of Experts) 특성을 극단으로 활용한 <strong>메모리 래더(Memory Ladder) 아키텍처</strong>에 있다:
            </p>
            <ul>
              <li><strong>Dense Trunk 인메모리 상주:</strong> 토큰마다 항상 활성화되는 핵심 어텐션 및 트렁크 가중치는 사용자가 지정한 메모리 예산(예: 8GB) 내에 고정 상주시킨다.</li>
              <li><strong>1.45TB Routed Experts 온디맨드 스트리밍:</strong> MoE 레이어에서 라우터가 선택한 소수의 Top-K 전문가 가중치는 절대 RAM에 통째로 적재하지 않는다. 대신 고속 NVMe SSD에서 <code>mmap</code> 또는 다이렉트 I/O로 필요한 블록만 초고속 스트리밍하여 <strong>메모리 복사 없이 곧바로 레지스터로 올려 행렬 곱셈을 수행</strong>하고 즉시 버린다.</li>
              <li><strong>최적화된 MXFP4 양자화 커널:</strong> AVX2 및 ARM NEON 벡터 명령어를 활용해 저정밀도 양자화 가중치를 CPU 캐시 친화적으로 디코딩.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="git-branch" style="color:#0ea5e9;"></i> Kimi K3 C99 온디맨드 MoE 스트리밍 파이프라인
                </span>
                <span class="schematic-badge">NVME DIRECT-TO-REGISTER INFERENCE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">STEP 1</div>
                  <div class="step-label">Dense Trunk 인메모리 연산</div>
                  <div class="step-tech">8.24GB Resident RAM (Portable C99)</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">STEP 2</div>
                  <div class="step-label">Top-K MoE 전문가 라우팅</div>
                  <div class="step-tech">Sparse Gate Selection (No Global Load)</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">STEP 3</div>
                  <div class="step-label">NVMe 디스크 온디맨드 스트리밍 곱셈</div>
                  <div class="step-tech">1.45TB Streamed Direct Matrix Multiply</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 연산 원리:</strong> 방대한 MoE 전문가 풀 전체를 램에 올릴 필요 없이, 현재 토큰 연산에 당장 필요한 몇몇 전문가 블록만을 NVMe 디스크에서 직류로 읽어 곱셈한 뒤 즉각 폐기함으로써 메모리 상주량을 8.24GB로 극단 통제합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="bar-chart-2"></i> 4. 메모리 사다리: 8GB에서 128GB 서버까지의 스케일링
            </h3>
            <p>
              이 구현은 시스템의 RAM 크기에 따라 유연하게 확장된다. 
              8GB 노트북에서는 디스크 I/O를 기다리느라 토큰당 32초가 걸리지만, 메모리가 128GB 이상 확보된 서버 프리셋(<code>--preset server</code>)에서는 디스크 대기 없이 토큰당 10.69초로 3배 이상 빨라진다. 
              하드웨어 제약이 아무리 심한 오프라인 폐쇄망 단말에서도 2.78조 파라미터급 프론티어 지능을 구동할 수 있는 가능성을 입증한 것이다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="monitor" style="color:#10b981;"></i> kimi-k3-in-c 아키텍처 다이어그램 & CLI
                </span>
                <span class="media-showcase-badge demo">ENGINEERING SCHEMATIC</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/thumb_kimi_k3.jpg" alt="kimi-k3-in-c overview" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 메모리 래더 설계:</strong> NVMe 디스크와 상주 램의 역할을 분리하여 단일 CPU에서 2.78조 파라미터를 소화하는 파이프라인.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="help-circle"></i> 5. 시사점: 온디바이스 초거대 AI의 새로운 이정표
            </h3>
            <p>
              일반적인 실시간 챗봇 서빙으로는 초당 0.03토큰이라는 속도가 한계일 수 있다. 
              하지만 배치 분석, 임베디드 오프라인 단말, 그리고 '인터넷과 GPU가 차단된 고보안 폐쇄망'에서 프론티어급 reasoning 모델을 온프레미스로 구동해야 하는 특수 임무 영역에서 이 C99 구현은 대체 불가능한 혁신적인 무기가 된다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://github.com/FareedKhan-dev/kimi-k3-in-c" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
