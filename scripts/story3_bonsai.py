# -*- coding: utf-8 -*-
# Story 3: PrismML Ternary Bonsai 2.5 27B (1.58-bit Ternary Agentic Model)

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] PrismML Ternary Bonsai 2.5 27B                   -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_bonsai.jpg" alt="Ternary Bonsai 2.5 27B 1.58-bit Compact Model Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="cpu" style="width:12px;height:12px;"></i> HN VELOCITY #1</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🌱 HN 속도 1위 (80.8/h · 213점) · 5.9GB로 RTX 4090 204 tok/s</span>
              <span class="platform-tag">Hacker News Top Velocity</span>
              <span class="platform-tag">PrismML / Bonsai-2.5-27B</span>
            </div>

            <h2 class="article-headline">
              "5.9GB 메모리로 SWE-bench 75.6%·초당 204토큰" — 삼진(Ternary) 로컬 에이전트의 임계점을 넘은 'Bonsai 2.5 27B'
            </h2>

            <div class="article-subheadline">
              Qwen3.8 27B를 1.58비트 삼진 가중치로 압축해 5.9GB 풋프린트를 유지하면서도 SWE-bench Verified 75.6%(원본 80.6% 근접)·AppWorld 90.5%·τ³-Bench 73.9%를 달성하고, RTX 4090 1장 및 Apple Silicon(MLX)에서 204 tok/s로 도는 Apache-2.0 로컬 에이전트 모델
            </div>
            <p class="article-snippet">
              "초저비트 양자화 모델은 챗봇 답변은 그럴듯해도, 여러 단계의 도구를 호출하는 코딩 에이전트로 쓰면 작은 오차가 누적돼 금세 탈선한다"는 게 지금까지의 정설이었습니다. 오늘 해커뉴스에서 시간당 <strong>80.8점(2.6시간 만에 213점)</strong>이라는 압도적 속도로 1위에 오른 Caltech 출신 팀 <strong>PrismML의 Ternary Bonsai 2.5 27B</strong>는 그 편견을 정면으로 부쉈습니다. 고작 <strong>5.9 GB</strong> 용량으로 <code>SWE-bench Verified</code> <strong>75.6%</strong>(전작 Bonsai 2의 60.8%에서 +14.8%p 급등), <code>AppWorld</code> <strong>90.5%</strong>를 기록하며 소비자용 RTX 4090에서도 <strong>초당 204토큰</strong>을 뿜어내는 가중치를 <code>Apache-2.0</code>으로 전면 공개했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: 54GB짜리 거인을 노트북·게이밍 GPU 한 장에 구겨 넣은 밤
            </h3>
            <p>
              27B(270억 파라미터)급 코딩 모델은 본래 BF16 원본 가중치만 해도 54GB가 넘어 데이터센터용 H100이나 초고가 Mac Studio의 전유물이었다. 게다가 기존에 나와 있던 저비트 양자화 모델들은 멀티턴 에이전트 작업에 투입하면 치명적인 약점을 드러냈다. <code>pytest</code> 오류를 고치고, 터미널 출력을 해석해 다음 명령을 고치는 긴 루프 속에서 과도한 추론(Excessive Thinking)과 무한 반복 루프에 빠지며 작업이 붕괴하곤 했다.
            </p>
            <p>
              오늘 PrismML이 공개한 <strong>Ternary Bonsai 2.5 27B</strong>의 벤치마크 표가 해커뉴스에 올라오자 댓글창이 술렁였다. 한 개발자는 놀라움을 감추지 못했다. <em>"내가 잘못 본 게 아니라면, 이 5.9GB짜리 로컬 모델이 불과 몇 달 전 프런티어 상용 모델(Opus 4.6)과 맞먹는 SWE-bench 점수를 찍고 있다. 지능 밀도(Intelligence Density)의 게임이 완전히 바뀌고 있다."</em>
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: 5.9GB 안방 코딩 에이전트가 위협하는 클라우드 API 종량제
            </h3>
            <p>
              에이전트 시대의 AI 비용 구조는 과거 채팅 1회 응답과 전혀 다르다. 코딩 에이전트 한 번이 리포지토리를 탐색하고 테스트를 돌리는 동안 수만~수십만 개의 컨텍스트 토큰이 반복 소비되며, 클라우드 API 청구서는 순식간에 불어난다. 게다가 기업의 사내 비공개 저장소나 민감한 고객 문서를 외부 API로 전송할 수 없는 조직도 많다.
            </p>

            <div class="editorial-quote">
              <p>
                "에이전트 워크플로는 모델 열화에 극도로 민감해 작은 오차 하나가 연속 도구 호출 전체를 탈선시킨다. <strong>Bonsai 2.5 27B는 5.9 GB 메모리 풋프린트를 그대로 유지하면서 SWE-bench Verified를 60.8%에서 75.6%로, AppWorld를 51.2%에서 90.5%로 끌어올려 풀프리시전 Qwen3.8 27B 원본(80.6% · 93.2%)과의 격차를 사실상 지워버렸다.</strong>"
              </p>
              <small>— PrismML Ternary Bonsai 2.5 27B 기술 리포트 및 벤치마크 비교표</small>
            </div>

            <p>
              놀라운 것은 속도다. 단일 <strong>RTX 4090</strong>에서 MTP(Multi-Token Prediction) 기준 초당 <strong>204토큰</strong>을 생성하고, 2,000토큰 프롬프트를 초당 <strong>3,060토큰</strong> 속도로 씹어 삼킨다. H100 단일 카드에서는 <strong>291 tokens/s</strong>에 달하며, Mac·iPhone·iPad용 Apple MLX 및 NVIDIA/Intel GPU용 <code>llama.cpp</code>를 즉시 지원한다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 1.58비트 삼진(Ternary) 압축과 장문 도구 호출 안정화
            </h3>
            <p>
              Bonsai 2.5 27B가 메모리 대역폭 병목을 정면 돌파하고 에이전트 지능을 보존한 비결은 3가지 공학적 최적화에 있다:
            </p>
            <ul>
              <li><strong>삼진 가중치 + Hadamard 패킹:</strong> Qwen3.8 27B의 거대한 16비트 행렬 가중치를 극도로 압축된 삼진 표현(1.58비트급, 전체 모델 5.9GB)으로 재학습·정렬해 GPU VRAM에서 코어로 가중치를 실어 나르는 메모리 대역폭(Memory Bandwidth) 소모를 9분의 1 수준으로 깎아냈다.</li>
              <li><strong>반복 루프 억제 &amp; 적은 턴 수렴:</strong> 전작 Bonsai 2 27B가 <code>DeepSWE v1.1 (mini-swe-agent)</code> 벤치마크에서 장문 루프 붕괴로 <code>0점</code>에 그쳤던 원인을 정밀 분석해, 2.5에서는 도구 실행 실패 시 스스로 경로를 수정하고 더 적은 턴과 토큰으로 목표를 완료하도록 후속 정렬(Post-training)해 DeepSWE 점수를 <code>27점</code>(원본 30.1점 근접)으로 복구했다.</li>
              <li><strong>실전 에이전트 벤치마크 전방위 검증:</strong> <code>τ³-Bench</code>에서는 <strong>73.9%</strong>로 오히려 원본 Qwen3.8 27B(72.8%)를 소폭 앞질렀으며, <code>BigCodeBench</code> <strong>60.3%</strong>(원본 61.5%), <code>LiveCodeBench v6</code> <strong>83.0%</strong>(원본 87.6%)로 코딩·도구 호출 양면에서 손실을 최소화했다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">Ternary Bonsai 2.5 27B 지능 밀도 및 온디바이스 에이전트 파이프라인</span>
                <span class="schematic-badge">5.9 GB Footprint · Apache-2.0 · llama.cpp &amp; Apple MLX</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Base → Ternary Compression</div>
                  <div class="schematic-desc">
                    Qwen3.8 27B 기반 삼진 가중치 압축<br>
                    메모리 점유 단 5.9 GB 유지<br>
                    과도한 사고·반복 루프 억제 학습<br>
                    Apache-2.0 오픈 가중치 배포
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. Agentic Benchmark Leap</div>
                  <div class="schematic-desc">
                    SWE-bench Verified: 60.8 → <strong>75.6%</strong><br>
                    AppWorld: 51.2 → <strong>90.5%</strong><br>
                    DeepSWE v1.1: 0 → <strong>27.0</strong> (원본 30.1)<br>
                    τ³-Bench: <strong>73.9%</strong> (원본 72.8% 상회)
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Edge Runtime Throughput</div>
                  <div class="schematic-desc">
                    RTX 4090: <strong>204 tok/s</strong> (Prefill 3,060/s)<br>
                    H100: <strong>291 tok/s</strong> (Prefill 3,200/s)<br>
                    <code>llama.cpp</code> (NVIDIA/Intel) &amp; MLX (Apple)<br>
                    사내 비공개 코드베이스 100% 로컬 구동
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">PrismML Ternary Bonsai 2.5 27B 공식 발표 화면 — 벤치마크 성능 비교 및 로컬 에이전트 워크플로</span>
              </div>
              <img src="../assets/images/demo_bonsai.png" alt="PrismML Bonsai-demo GitHub Repository and Whitepaper" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/PrismML-Eng/Bonsai-demo/ 실화면: Ternary Bonsai 2.5 27B 공식 데모 코드, 기술 백서(bonsai-2-5-27b-whitepaper.pdf) 및 로컬 추론 실행 가이드.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자 및 시장 반응: '벤치맥싱' 경계론과 로컬 추론 생태계의 급팽창
            </h3>
            <p>
              Bonsai 2.5 27B의 등장은 클라우드 프런티어 AI 기업들이 지키려던 "고성능 코딩 에이전트는 클라우드 API로만 가능하다"는 경제적 해자에 또 하나의 균열을 냈다. 가중치가 <code>Apache-2.0</code>으로 풀리자마자 GitHub에서는 이미 <code>cool-japan/oxibonsai</code>(순수 Rust 추론 엔진), <code>RightNow-AI/bonsai-turbo</code>, <code>ninfer-ternary-qwen3.8-27b-3090</code> 등 단일 RTX 3090/4090에 맞춘 서드파티 삼진 커널들이 앞다투어 올라오고 있다.
            </p>
            <ul>
              <li><strong>해커뉴스의 냉정한 검증 시선:</strong> 한편에서는 <em>"과거 프런티어 모델에 맞먹는 SWE-bench 점수가 실제 미지의 코드베이스에서도 그대로 재현되는지, 아니면 벤치마크 최적화(Benchmaxxing)가 섞였는지 검증해야 한다"</em>는 신중론도 팽팽히 맞섰다. 실제로 개발자들이 자신의 사내 이슈와 <code>pytest</code> 회귀 테스트에 직접 붙여 검증하는 2라운드가 곧바로 시작되고 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 6GB 미만의 지능이 열쇠를 쥐는 날
            </h3>
            <p>
              불과 6GB 남짓의 메모리—보급형 노트북의 통합 메모리나 몇 년 된 게이밍 그래픽카드 한 장에 넉넉히 들어가는 크기—안에 27B급 멀티턴 코딩 에이전트가 들어앉았다.
            </p>
            <p>
              인터넷 선을 뽑은 에어갭 환경의 연구실과 1인 개발자의 노트북 위에서 초당 200토큰으로 코드를 고치는 에이전트가 보편화되는 순간, AI의 주전장은 "가장 거대한 데이터센터"에서 "내 책상 위 6GB"로 내려온다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=PrismML+Ternary+Bonsai+2.5+27B" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://huggingface.co/collections/prism-ml/bonsai-25-27b" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="globe"></i> Hugging Face 모델 받기
              </a>
              <a href="https://github.com/PrismML-Eng/Bonsai-demo/" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 데모·논문 보기
              </a>
            </div>

          </div>
        </div>
      </article>
"""
