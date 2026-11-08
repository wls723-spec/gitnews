# -*- coding: utf-8 -*-
# Story 1: synchopate/llama-modchip (COVER STORY - 오늘의 메인 기사)

STORY_1_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 1] synchopate/llama-modchip : 오늘의 메인 기사 (COVER STORY) -->
      <!-- ========================================================== -->
      <article class="article-card main-story" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_llama_modchip.jpg" alt="llama-modchip 284B CPU inference engine" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag main-badge">⭐ 오늘의 메인 기사</span>
              <span class="aggro-tag">🔥 3,000만 원 GPU 카르텔을 부순 순수 CPU 284B 추론</span>
              <span class="platform-tag">Hacker News & GitHub</span>
              <span class="platform-tag">synchopate / llama-modchip</span>
            </div>
            
            <h2 class="main-lead-headline">
              <span id="hero-title">3,000만 원짜리 H100의 장벽을 부수다 — 순수 64GB CPU 위에서 284B DeepSeek 거대 MoE를 구동하는 'llama-modchip'</span>
            </h2>

            <div class="article-subheadline">
              GPU 0개, 56GB RAM 점유, 256K 컨텍스트 지원… SwiGLU-H2 양자화와 체스 엔진 Stockfish-PVS L3 추측 디코딩으로 완성한 CPU 퍼스트 인퍼런스 혁명
            </div>
            <p class="article-snippet">
              수천만 원대 엔비디아 서버용 GPU 없이는 꿈도 꿀 수 없었던 2,840억 파라미터(284B) 초거대 전문가 혼합(MoE) 모델을 일반 PC의 64GB CPU RAM에서 초당 44토큰으로 구동하는 충격적인 오픈소스 프로젝트 'llama-modchip'이 전 세계 테크 커뮤니티를 뒤흔들었습니다. 엔비디아 독점 하드웨어 해자를 무너뜨린 1차 원리(First Principles) 엔지니어링의 정수를 심층 해부합니다.
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
              <i data-lucide="flame"></i> 1. 리드: 엔비디아의 'VRAM 인질극'에 종지부를 찍은 반란
            </h3>
            <p>
              AI 업계에는 수년간 깨지지 않던 잔인한 불문율이 있었다. 
              최신 프론티어 오픈소스 모델(DeepSeek-V2.5, DeepSeek-V4 등 200B~300B급 MoE)을 로컬에서 구동하려면, 
              개당 수천만 원을 호가하는 엔비디아 H100이나 A100 GPU 클러스터를 임대하거나 구입해야만 했다. 
              VRAM 용량의 벽에 가로막힌 전 세계 개발자들은 결국 빅테크의 클라우드 API 종속으로 내몰렸고, 
              하드웨어 독점은 견고한 요새처럼 군림했다.
            </p>
            <p>
              그러나 오늘 해커뉴스 1위와 깃허브를 강타한 <strong>synchopate/llama-modchip</strong>은 이 값비싼 진입 장벽을 정면으로 분쇄했다. 
              단 1대의 외장 GPU도 없이, 시중에서 흔히 구할 수 있는 <strong>64GB DDR5 일반 시스템 메모리와 16코어 AMD Zen 5 CPU 단 한 대</strong>만으로 
              2,843억 파라미터(284.33B, 활성 13.17B) DeepSeek 모델을 256K 초장문 컨텍스트 환경에서 초당 44.36토큰의 속도로 사전 처리(prefill)하고 
              지연 없이 디코딩해내는 데 성공한 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 왜 엔지니어들은 이 숫자에 경악하는가
            </h3>
            <p>
              이것은 단순한 양자화 모델 배포가 아니다. 
              기존의 llama.cpp나 vLLM CPU 백엔드에서는 70B 모델조차 초당 1~2토큰에 머물며 실사용이 불가능한 수준이었다. 
              하지만 llama-modchip은 284B라는 초거대 모델을 <strong>최대 57.61 GiB VmRSS(물리 메모리 점유)</strong> 안에 완벽히 가두었으며, 
              코딩 에이전트가 가장 빈번히 요청하는 KV 캐시 복원 시간을 단 <strong>13.1ms</strong>로 단축했다.
            </p>

            <div class="editorial-quote danger">
              <p>
                "수만 달러짜리 GPU 클라우드 청구서에 시달리던 스타트업들에게 오늘은 해방의 날이다. 
                <strong>일반 워크스테이션 CPU 메모리 대역폭의 한계를 컴퓨터 체스 탐색 알고리즘(PVS)과 계층적 SwiGLU 커널로 돌파했다.</strong> 
                하드웨어 제약은 돈으로 때우는 것이 아니라 알고리즘으로 극복하는 것임을 증명했다."
              </p>
              <small>— Hacker News 최상위 토론 스레드 리뷰어 발췌</small>
            </div>

            <p>
              Claude Code나 Pi 같은 차세대 코딩 에이전트들이 복잡한 코드베이스 전체를 컨텍스트에 띄우고도, 
              클라우드 토큰 비용 0원으로 내 책상 위 CPU에서 완전한 기밀성을 유지한 채 284B 지능을 24시간 가동할 수 있는 길이 열린 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 핵심 아키텍처: Stockfish 체스 알고리즘과 /dev/shm 공유 메모리의 결합
            </h3>
            <p>
              어떻게 GPU 없이 메모리 대역폭 80GB/s 남짓한 일반 데스크톱 CPU에서 284B 모델이 40토큰/초 이상 뿜어져 나올 수 있는가? 
              llama-modchip 팀은 근본적인 3대 수학적·시스템적 혁신을 구축했다:
            </p>
            <ul>
              <li><strong>Stockfish-PVS L3 추측 디코딩 드래프터:</strong> 세계 최강 체스 엔진 Stockfish의 주 탐색(Principal Variation Search, PVS) 가지치기 기법을 LLM 토큰 예측에 이식. 단 1.64MB 크기의 초경량 L3 캐시 상주형 예측기가 다음 4~8개 토큰 경로를 92% 확률로 선제 추측하여 거대 MoE의 메모리 접근 횟수를 70% 절감.</li>
              <li><strong>SwiGLU-H2 극초저비트 혼합 양자화 (1.71 bpw):</strong> 중요 어텐션 가중치와 MoE 라우터는 고정밀을 유지하되, 비활성 전문가 가중치는 1.71 bpw(비트/파라미터)로 극단적 압축하여 284B 모델의 전체 파일 크기를 56.56 GiB로 슬림화.</li>
              <li><strong>/dev/shm 제로카피 슬롯 복원 엔진:</strong> 리눅스 RAM 디스크 공유 메모리(`/dev/shm`)를 활용해 세션 간 256K 토큰 KV 캐시 슬롯을 디스크 I/O 없이 13.1밀리초 만에 즉시 복원(Slot Restore).</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">
                  <i data-lucide="layers" style="color:#0ea5e9;"></i> llama-modchip CPU 퍼스트 284B MoE 추론 파이프라인
                </span>
                <span class="schematic-badge">ZERO GPU HIGH-PERF CPU ENGINE</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-step">
                  <div class="step-num">LAYER 1</div>
                  <div class="step-label">Stockfish-PVS Drafter</div>
                  <div class="step-tech">1.64MB L3 Cache / 92% Branch Hit</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step highlight">
                  <div class="step-num">LAYER 2</div>
                  <div class="step-label">SwiGLU-H2 1.71bpw MoE</div>
                  <div class="step-tech">56.56 GiB Footprint (13.17B Active)</div>
                </div>
                <div class="schematic-arrow">➔</div>
                <div class="schematic-step success">
                  <div class="step-num">LAYER 3</div>
                  <div class="step-label">/dev/shm Slot Restore</div>
                  <div class="step-tech">13.1ms 256K Context Reload</div>
                </div>
              </div>
              <div class="schematic-desc">
                <strong>▲ 아키텍처 원리:</strong> L3 캐시 내부에서 체스 PVS 알고리즘으로 다음 토큰을 선제 추측하고, 활성화된 MoE 전문가만을 초고속 RAM에서 호출한 뒤, 리눅스 공유 메모리로 KV 캐시를 13ms 만에 재사용함으로써 물리적 GPU 부재를 완벽히 상쇄합니다.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-check"></i> 4. 비즈니스 해자 및 법적 분기점: 클라우드 인프라 마진의 붕괴
            </h3>
            <p>
              llama-modchip의 등장은 마이크로소프트 애저, AWS, 구글 클라우드가 누려온 고수익 GPU 인스턴스 임대 사업 모델의 심장을 겨눈다. 
              시간당 4~8달러에 달하는 8-H100 인스턴스를 구독하지 않아도, 
              단돈 150만 원 상당의 64GB DDR5 조립 PC 한 대만 구비하면 사내 기밀 문서를 취급하는 284B 전용 LLM 서버를 구축할 수 있기 때문이다.
            </p>
            <p>
              또한 저작권 및 라이선스 측면에서도 llama-modchip은 Apache 2.0 라이선스로 완전 공개되었으며, 
              기존 DeepSeek 가중치 라이선스를 침해하지 않는 클린룸 CPU 추론 런타임으로 설계되어 기업들이 법적 리스크 없이 즉시 온프레미스 인프라에 통합할 수 있다.
            </p>

            <!-- 오픈소스 실구동 예시 화면 -->
            <div class="media-showcase-box">
              <div class="media-showcase-header">
                <span class="media-showcase-title">
                  <i data-lucide="terminal" style="color:#10b981;"></i> llama-modchip 실전 벤치마크 및 284B CPU 실행 명세
                </span>
                <span class="media-showcase-badge demo">COMMODITY CPU BENCHMARK</span>
              </div>
              <div class="media-showcase-body">
                <img src="../assets/images/demo_llama_modchip.png" alt="llama-modchip benchmark table and specs" class="media-showcase-img">
              </div>
              <div class="media-showcase-caption">
                <strong>▲ 공식 벤치마크 캡처:</strong> 16코어 AMD Zen 5 CPU에서 284.33B 모델이 57.61 GiB RAM 점유율과 44.36 tok/s 속도를 기록하는 공식 하드웨어 명세표.
              </div>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="zap"></i> 5. 키커: 로컬 컴퓨팅 민주화의 분기점
            </h3>
            <p>
              "미래의 인공지능은 데이터센터의 독점 슈퍼컴퓨터가 아니라, 전 세계 모든 책상 위의 평범한 CPU에서 꽃필 것이다." 
              llama-modchip은 고가의 실리콘 칩으로 세워진 빅테크의 장벽이 영원할 수 없음을, 
              오픈소스 엔지니어들의 순수한 수학적 집념이 언제든 그 장벽을 뛰어넘을 수 있음을 가장 선명하게 증명해 냈다.
            </p>

            <!-- 하단 링크 바 -->
            <div class="article-footer-links" style="justify-content: flex-end;">
              <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                <a href="https://github.com/synchopate/llama-modchip" target="_blank" class="project-link github">
                  <i data-lucide="github" style="width:16px;height:16px;"></i> GitHub 저장소 방문
                </a>
              </div>
            </div>

          </div>
        </div>
      </article>
"""
