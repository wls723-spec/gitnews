# -*- coding: utf-8 -*-
# Story 3: stew675/llama-cpp-rdna-boosts (Bespoke Hardware Inference Forks & Numerics Assurance)

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [STORY 3] stew675/llama-cpp-rdna-boosts : Inference Wars   -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_rdnaboosts.jpg" alt="llama-cpp-rdna-boosts AMD RDNA Custom Inference Engine Editorial Illustration" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="zap" style="width:12px;height:12px;"></i> SILICON VELOCITY</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag">🔥 HN 246점 · 범용 llama.cpp 대비 디코드 +57%·프리필 +86% &amp; '추론 왜곡' 논쟁</span>
              <span class="platform-tag">Hacker News &amp; AMD RDNA/HIP</span>
              <span class="platform-tag">stew675 / llama-cpp-rdna-boosts</span>
            </div>

            <h2 class="article-headline">
              "NVIDIA 손에 들어간 범용 `llama.cpp`를 기다릴 수 없다" — AMD RDNA 전용 포크가 쏘아 올린 '맞춤형 추론 엔진' 폭발
            </h2>

            <div class="article-subheadline">
              MTP 디코드·청크형 Gated-Delta-Net·WMMA 플래시 어텐션 등 19개 패치 시리즈(v18-919794500-r366)로 AMD GPU 디코드를 35→55 tok/s·프리필을 700→1300 tok/s로 끌어올리고, MoE 가중치 변조 꼼수를 차단하는 수치 검증 게이트까지 구축 (★335 · MIT)
            </div>
            <p class="article-snippet">
              2026년 11월, AI 인프라 커뮤니티에 기묘한 지각변동이 일고 있습니다. 프론티어 코딩 모델을 무기 삼은 독립 개발자들이 거대한 범용 엔진(<code>llama.cpp</code>, <code>vLLM</code>)의 느린 PR 심사를 기다리는 대신, 자기 그래픽카드 한 장에 맞춘 <strong>초고속 전용 포크</strong>를 쏟아내기 시작한 것입니다(HN <strong>246점</strong>). 그 선두에 선 <strong>stew675/llama-cpp-rdna-boosts</strong>는 <code>llama.cpp</code> 상류 커밋(<code>919794500</code>) 위에 19개의 <code>git am</code> 패치를 얹어 <strong>RDNA 3/3.5/4 GPU의 디코드 속도를 35→55 tok/s(+57%), 프리필을 700→1300 tok/s(+86%)</strong>로 끌어올리는 동시에, 속도를 위해 모델 지능을 훼손하는 편법을 잡아내는 엄격한 수치 무결성 게이트를 도입했습니다.
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
              <i data-lucide="flame"></i> 1. 리드: <code>llama.cpp</code>라는 '모델 동물원'이 무거워진 순간
            </h3>
            <p>
              불과 1~2년 전만 해도 로컬 LLM의 제왕은 단연 <code>llama.cpp</code>였다. 맥북부터 라즈베리파이, 엔비디아 RTX, 라데온, 인텔 Arc까지 지구상의 거의 모든 칩을 단일 저장소로 품은 대가였다. 그러나 해커뉴스 토론(246점)에서 개발자들이 지적했듯, <code>llama.cpp</code>는 어느덧 수백 종의 모델과 구형 하드웨어를 모두 떠받치는 거대한 '모델 동물원(Model Zoo)'이자 NVIDIA의 Hugging Face 인수 이후 더 보수적인 공룡으로 변모했다. 특정 GPU 아키텍처 하나만을 위한 과감한 메모리 레이아웃 개조는 범용성을 해친다는 이유로 메인라인에 들어가기 어려워졌다.
            </p>
            <p>
              그러자 2026년 11월, 역설적인 현상이 터졌다. 개발자들이 클로드와 코덱스 같은 프론티어 모델에 커널 최적화를 맡기며 <code>Strata</code>, <code>Basalt</code>, <code>llama-inkling-2-mini</code> 같은 '초전용(Bespoke) 추론 포크'들이 하루가 멀다 하고 등장한 것이다. 하지만 이 속도 경쟁 이면에는 어두운 그림자도 있었다. 일부 포크가 <code>tok/s</code> 벤치마크 숫자를 부풀리기 위해 <strong>원래 선택되어야 할 디스크/RAM 쪽 MoE 전문가를 건너뛰고 VRAM에 올라온 전문가만 편향 호출해 모델 두뇌를 몰래 깎아먹는 꼼수</strong>가 적발되기 시작한 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: "속도만 빠른 가짜가 아니라, 수치 보증(Numerics Assurance)이 된 RDNA 가속"
            </h3>
            <p>
              오늘 해커뉴스 프론트페이지를 점령한 글(<em>AMD-specific fork of llama.cpp</em>)이 다른 포크들을 제치고 <strong><code>stew675/llama-cpp-rdna-boosts</code></strong>를 강력히 추천한 이유가 바로 여기에 있다. 이 프로젝트는 16GB VRAM + 16GB RAM에서 180B 모델을 억지로 빠르게 돌리려고 모델의 추론 정확도를 망가뜨리는 유행과 선을 긋고, <strong>"비트 단위 재현성과 로짓(Logit) 100% 일치 검증을 통과한 성능만 공식 배포한다"</strong>는 원칙을 세웠다.
            </p>

            <div class="editorial-quote">
              <p>
                "최근 속도 경쟁에 매몰된 일부 포크들은 하드웨어 최적화가 아니라 <strong>모델이 생각하는 방식 자체를 바꿔치기해 <code>brrr</code> 하고 토큰만 빨리 뱉는다.</strong> 반면 <code>llama-cpp-rdna-boosts</code>는 토큰 생성을 35→55 tok/s, 프리필을 700→1300 tok/s로 끌어올리면서도 수치 무결성을 보장한다."
              </p>
              <small>— devnull.land 리뷰 &amp; Hacker News 토론 (246점·56댓글)</small>
            </div>

            <p>
              실제로 <code>stew675/llama-cpp-rdna-boosts</code>의 <code>COMMUNITY-CONFIG.md</code>를 열어보면, 저자 스스로 과거에 측정됐던 <code>2,650~3,060 t/s</code> 디바이스 개더(Gather) 프리필 수치가 <strong>"다중 유배치(Multi-ubatch) 프리필 시 오래된 <code>NaN</code>을 읽어 MoE 라우팅을 단락(Short-circuit)시킨 부패한 수치였다"</strong>고 공개 자백한 뒤 해당 기능을 기본 비활성화(<code>GGML_SCHED_DEVGATHER=0</code>)해 버린 기록이 고스란히 남아 있다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 기술 메커니즘: 19개 선형 <code>git am</code> 패치와 슬랩(Slab)·MoE 전문가 캐시
            </h3>
            <p>
              <code>stew675/llama-cpp-rdna-boosts</code>(최신 릴리스 <code>v18-919794500-r366</code>)는 상류 코드베이스를 난도질하는 대신, 지정된 <code>llama.cpp</code> 기준 커밋(<code>919794500</code>) 위에 <strong>18개 공식 블록(<code>0000</code>~<code>0017</code>)과 1개 임시 블록(<code>0300</code>)</strong>을 순차 적용하는 패치 셋으로 설계됐다:
            </p>
            <ul>
              <li><strong>RDNA 3/3.5/4(<code>gfx1100</code>, <code>gfx1150/1151</code>, <code>gfx1200/1201</code>) 전용 HIP/WMMA 커널:</strong> RDNA 아키텍처의 Wave32·WMMA(Wave Matrix Multiply-Accumulate) 명령어에 맞춰 BF16 KV 캐시와 WMMA 플래시 어텐션, 퓨즈드(Fused) MoE 및 K-양자 디코드 커널, MTP(Multi-Token Prediction) 디코드, 청크형 Gated-Delta-Net 프리필을 통합했다.</li>
              <li><strong><code>MOE_EXPERT_CACHE_MIB</code> &amp; <code>ggml-cuda-slab</code> 아레나:</strong> 32 GiB VRAM 카드(Radeon AI PRO R9700 등)에 들어가지 않는 37.8 GB <code>Qwen3.6-35B-A3B Q8_0</code>나 100 GB <code>Qwen3.8-Flash-Next IQ4_NL</code>을 돌릴 때, 핫한 MoE 전문가만 VRAM 캐시에 영속 보관하고(<code>-ncmoe 20</code>, <code>MIB=8192</code>) 호스트 RAM과 PCIe 5.0으로 비동기 스테이징하여 128K 컨텍스트에서도 <strong>프리필 884 t/s·심층 디코드 57.1 t/s</strong>를 유지한다.</li>
              <li><strong>철저한 게이트 검증(<code>gate-prefill-logits.sh</code> &amp; 일관성 감사):</strong> 매 릴리스(<code>r366</code>)마다 <code>check-shlib-symbols.sh</code>(16/16), <code>gate-host-pool.sh</code>(59/59), <code>gate-prefill-logits.sh</code>(오차 <code>0.000000 / 100.000%</code>)를 통과한 뒤에만 태그와 <code>release.json</code> SHA-256 매니페스트를 발행하며, 11만 토큰 컨텍스트에서 6,253단어 장문 출력 일관성(<code>zero ////</code>)까지 확인한다.</li>
            </ul>

            <!-- 순수 CSS/HTML 건축적 에디토리얼 구조도 -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-title">llama-cpp-rdna-boosts 19-블록 패치 파이프라인 &amp; 수치 보증 게이트</span>
                <span class="schematic-badge">Base 919794500 · ROCm 7.14.1 · v18-r366</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-box">
                  <div class="schematic-box-title">1. Deterministic Patch Stack</div>
                  <div class="schematic-desc">
                    상류 <code>llama.cpp</code> (<code>919794500</code>) 체크아웃<br>
                    <code>apply-all.sh</code>로 19개 커밋 순차 적용<br>
                    선택 블록: 2-Lane Prefill(<code>0100</code>) · 혼합 KV(<code>0101</code>)<br>
                    여러 머신(<code>radix</code> 등)에서 SHA-256 팁 교차 검증
                  </div>
                </div>
                <div class="schematic-box accent">
                  <div class="schematic-box-title">2. RDNA3/4 HIP &amp; MoE Cache</div>
                  <div class="schematic-desc">
                    WMMA Flash-Attention · BF16 KV · Fused MoE<br>
                    <code>MOE_EXPERT_CACHE_MIB</code> VRAM 핫 전문가 고정<br>
                    <code>ggml_cuda_slab</code> Wide Band 프리필 아레나<br>
                    <code>35→55 tok/s</code> 디코드 · <code>700→1300 tok/s</code> 프리필
                  </div>
                </div>
                <div class="schematic-box">
                  <div class="schematic-box-title">3. Numerics Assurance Gate</div>
                  <div class="schematic-desc">
                    <code>gate-prefill-logits.sh</code> (<code>0.000000 / 100.0%</code>)<br>
                    NaN 단락(<code>DEVGATHER</code>) 같은 가짜 속도 자진 폐기<br>
                    110K 컨텍스트 장문 일관성·해시 일치 감사<br>
                    ROCm 7.14.1 / 10.2 컨테이너 자동 빌드
                  </div>
                </div>
              </div>
            </div>

            <!-- 오픈소스 실구동 데모 쇼케이스 박스 -->
            <div class="media-showcase-box">
              <div class="showcase-header">
                <i data-lucide="monitor" class="showcase-icon"></i>
                <span class="showcase-title">stew675/llama-cpp-rdna-boosts 저장소 실화면 — 19개 패치 아키텍처 및 RDNA3/4 지원 매트릭스</span>
              </div>
              <img src="../assets/images/demo_rdnaboosts.png" alt="llama-cpp-rdna-boosts GitHub Repository and RDNA Support Matrix" class="showcase-img">
              <p class="showcase-caption">
                ▲ github.com/stew675/llama-cpp-rdna-boosts 실화면: 상류 llama.cpp 기준 커밋 위에 19개 RDNA/HIP 패치 블록을 선형 적용하는 구조와 gfx1100~gfx1201 지원 표.
              </p>
            </div>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. AI 인프라 권력 이동: CUDA 독점과 '바이브 코딩 포크' 사이의 새로운 표준
            </h3>
            <p>
              엔비디아의 <code>llama.cpp</code> 영향력 확대와 프론티어 AI 코딩 에이전트의 보급이 맞물리며, 로컬 AI 추론 생태계는 거대 단일 트렁크에서 <strong>'특정 실리콘에 극한으로 튜닝된 모듈식 패치셋'</strong>으로 분화하고 있다. 과거에는 AMD RDNA GPU나 애플 M1/M4 칩의 커널 하나를 깎아내려면 소수의 GPGPU 장인에게 몇 달씩 매달려야 했지만, 이제는 개인 해커들이 LLM과 함께 하루 만에 15~50%의 성능 격차를 메워낸다.
            </p>
            <ul>
              <li><strong>벤치마크 조작(Eval/Speed Hacking) 시대의 감시자:</strong> 해커뉴스 댓글에서 <em>"속도가 올라갔을 때 출력 토큰 품질까지 검증하는 프로젝트가 대체 몇 개나 되나?"</em>라는 날카로운 지적이 쏟아진 가운데, <code>stew675</code>의 로그잇 게이트와 투명한 <code>WORKLOG.md</code> 기록 문화는 'AI 보조 커널 개발 시대'의 새로운 엔지니어링 윤리 기준을 제시했다.</li>
              <li><strong>실사용 시 유의점:</strong> 이 패치 셋은 AMD RDNA3~4(Linux ROCm 7.14.1/10.2 환경, RDNA2는 베스트 에포트)에 특화돼 있으며, 상류 커밋(<code>919794500</code>)에 맞춰 리베이스되는 구조라 최신 <code>llama.cpp</code> 마스터의 당일 신모델이 즉시 반영되지는 않는다는 트레이드오프가 있다.</li>
            </ul>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 가장 빠른 엔진이 아니라, '거짓말하지 않는' 빠른 엔진이 살아남는다
            </h3>
            <p>
              누구든 추론 경로를 슬쩍 뭉개면 토큰 속도를 두 배로 부풀릴 수 있는 시대다. 그러나 하드웨어의 한계를 정직하게 밀어붙이며 0.000000의 오차도 허용하지 않는 <code>llama-cpp-rdna-boosts</code>의 태도는, AI 시대의 성능 최적화가 결국 <strong>증명 가능한 정직성</strong> 위에 서야 함을 웅변한다.
            </p>
            <p>
              거대한 범용 엔진의 그늘 아래 갇혀 있던 AMD 라데온 카드들이 오늘, 가장 까다로운 수치 검증서를 목에 걸고 트랙 위로 뛰어나왔다.
            </p>

            <div class="project-links">
              <a href="https://www.youtube.com/results?search_query=llama+cpp+amd+rdna+rocm+inference+benchmark" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i> 유튜브 관련 리뷰보기
              </a>
              <a href="https://devnull.land/amd-specific-llama-cpp" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i> HN 화제 벤치마크 리포트
              </a>
              <a href="https://github.com/stew675/llama-cpp-rdna-boosts" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i> GitHub 저장소 방문
              </a>
            </div>

          </div>
        </div>
      </article>
"""
