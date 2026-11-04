# -*- coding: utf-8 -*-
# Story 3: JustVugg/colibri

STORY_3_HTML = """
      <!-- ========================================================== -->
      <!-- [HERO 3] JustVugg/colibri -->
      <!-- ========================================================== -->
      <article class="article-card" onclick="toggleArticle(this)">
        <div class="article-preview">
          <div class="article-thumb-wrapper">
            <img src="../assets/images/thumb_colibri.jpg" alt="Colibri MoE Streaming Engine" class="article-thumb-img">
            <div class="thumb-play-badge"><i data-lucide="sparkles" style="width:12px;height:12px;fill:#fff;"></i> TRENDING #3</div>
          </div>

          <div class="article-summary-box">
            <div class="article-meta">
              <span class="aggro-tag" style="background:#fef3c7; border-color:#f59e0b; color:#b45309;">🐦 744B MoE 디스크 전문가 스트리밍</span>
              <span class="platform-tag">GitHub Breakthrough</span>
              <span class="platform-tag">JustVugg / colibri</span>
            </div>
            
            <h2 class="article-headline">
              거대 MoE 모델을 내 노트북에서: NVMe 디스크 전문가 스트리밍으로 GPU 장벽을 무너뜨린 순수 C 추론 엔진
            </h2>

            <div class="article-subheadline">
              "7440억 파라미터(744B) MoE 모델도 실제 토큰당 활성화되는 전문가는 단 3%뿐이다" — 엔비디아 H100 8장 클러스터 없이도 일반 PC/맥북에서 거대 프론티어 MoE 모델을 구동… 외부 라이브러리 의존성 제로(Zero Dependencies)의 순수 C 코드로 초고속 NVMe SSD에서 비활성 전문가를 직접 밀어 넣는 파격의 메모리 아키텍처 전격 공개 (+4.6만 스타)
            </div>
            <p class="article-snippet">
              수천만 원짜리 VRAM 부족에 시달리던 전 세계 오픈소스 커뮤니티의 거대한 환호. GLM-5.2/5.3, Kimi K3, DeepSeek V4 Flash 등 초거대 혼합 전문가 모델을 CPU와 디스크 스트리밍만으로 초당 수 토큰 속도로 실시간 추론해 내는 Colibri의 엔지니어링 미학.
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
              <i data-lucide="flame"></i> 1. 리드: 500GB VRAM의 통곡의 벽과 방구석 엔지니어의 분노
            </h3>
            <p>
              2026년 인공지능 생태계의 패권을 장악한 아키텍처는 단연 <strong>MoE(Mixture-of-Experts, 전문가 혼합 모델)</strong>다. 
              DeepSeek-V3부터 최신 GLM-5.2, Kimi K3에 이르기까지, 수천억 개의 파라미터를 거느린 괴물 모델들이 벤치마크 차트를 휩쓸었다. 
              하지만 이 모델들을 바라보는 개인 개발자들과 연구자들의 마음은 씁쓸했다. 
              최소 8장의 엔비디아 A100/H100 GPU(수천만~수억 원)로 무장한 데이터센터가 아니면, 744B 모델은 메모리에 올려볼 엄두조차 내지 못했기 때문이다.
            </p>
            <p>
              "오픈소스 모델이라더니, 결국 엔비디아 주주들만 돌릴 수 있는 그림의 떡 아닌가?" 
              이 분노 어린 질문에 대해, 단 한 명의 집념 어린 해커가 기상천외한 해답을 들고 나타났다. 
              바로 <strong>JustVugg/colibri</strong>다. 
              프로젝트 이름인 '콜리브리(벌새)'처럼 아주 작고 날렵한 단일 C 언어 바이너리로 컴파일되는 이 엔진은, 놀랍게도 <strong>평범한 개인용 데스크톱과 M시리즈 맥북에서 744B 거대 MoE 모델을 당당하게 구동</strong>해 냈다. 
              공개 직후 4만 6천 개 이상의 스타를 받으며 전 세계 AI 하드웨어 커뮤니티를 충격에 빠뜨렸다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="compass"></i> 2. 넛 그라프: '희소성(Sparsity)'의 1차 원리를 꿰뚫은 디스크 스트리밍
            </h3>
            <p>
              콜리브리의 비결은 타협 없는 1차 원리(First Principles) 사고에 있다. 
              MoE 모델의 총 파라미터가 7440억 개에 달할지라도, <strong>단일 토큰(Token)을 하나 생성하는 매 순간 실제로 활성화되어 계산에 참여하는 전문가는 전체의 3~5%</strong>에 불과하다. 
              나머지 95% 이상의 파라미터는 그 순간 아무런 일도 하지 않고 VRAM 공간만 차지하고 있는 셈이다.
            </p>

            <div class="editorial-quote">
              <p>
                "왜 일하지도 않는 전문가 가중치 수백 기가바이트를 값비싼 VRAM에 상시 모셔두어야 하는가? 
                현대 PCIe 4.0/5.0 NVMe SSD는 초당 7GB~14GB의 속도로 데이터를 뿜어낸다. 
                라우터가 다음 전문가를 지목하는 그 수 밀리초 동안, <strong>필요한 전문가만 디스크에서 RAM으로 번개처럼 스트리밍</strong>해 오면 그만이다."
              </p>
              <small>— JustVugg, Colibri 공식 기술 백서 서문</small>
            </div>

            <p>
              콜리브리는 공통 어텐션 레이어와 라우팅 게이트 등 핵심 상주 파라미터(수십 GB 수준)만 시스템 RAM에 고정해 두고, 거대한 FFN 전문가 블록들은 로컬 NVMe SSD에 파티셔닝해 둔 뒤 필요할 때마다 <strong>Direct I/O(O_DIRECT) 비동기 DMA</strong>를 통해 메모리로 직접 퍼올린다. 
              GPU가 없어도, 수백 기가바이트의 VRAM이 없어도 거대 모델이 막힘없이 숨을 쉰다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="cpu"></i> 3. 메커니즘 해부: 순수 C 코드가 빚어낸 무의존성 동적 페이징
            </h3>
            <p>
              Colibri는 거추장스러운 파이썬 인터프리터, 무거운 파이토치(PyTorch), 수 기가바이트짜리 CUDA 런타임을 일체 요구하지 않는다. 
              <strong>순수 C11(Pure C)</strong>로 작성되었으며, 외부 종속성 라이브러리가 단 하나도 없다.
            </p>

            <!-- 순수 CSS 다이어그램: Colibri MoE Dynamic Expert Streaming -->
            <div class="schematic-container">
              <div class="schematic-header">
                <span class="schematic-tag">MEMORY ARCHITECTURE SCHEMATIC</span>
                <span class="schematic-title">Colibri MoE 전문가 디스크 스트리밍 파이프라인 vs 전통적 VRAM 전수 적재</span>
              </div>
              <div class="schematic-grid">
                <div class="schematic-card" style="border-left: 4px solid #ef4444;">
                  <div class="schematic-card-title" style="color: #b91c1c;">전통적 방식: VRAM 전수 로딩 (VRAM 500GB+ 필수)</div>
                  <div class="schematic-step">1. 744B 전체 가중치를 VRAM에 무조건 상주</div>
                  <div class="schematic-step">2. 활성 전문가(3%) 외 97%의 전문가가 VRAM 낭비</div>
                  <div class="schematic-step">3. 8x H100 클러스터 필수 (수억 원 하드웨어)</div>
                  <div class="schematic-step">4. 개인 PC에서는 Out of Memory(OOM) 즉각 크래시</div>
                </div>
                <div class="schematic-card" style="border-left: 4px solid #10b981;">
                  <div class="schematic-card-title" style="color: #047857;">Colibri 방식: NVMe Direct I/O 스트리밍 (일반 PC 가능)</div>
                  <div class="schematic-step">1. 공통 Attention/Gate 레이어만 RAM(32GB)에 상주</div>
                  <div class="schematic-step">2. Top-k 활성 전문가를 라우터가 실시간 예측</div>
                  <div class="schematic-step">3. NVMe SSD에서 Direct I/O로 비동기 링 버퍼 적재</div>
                  <div class="schematic-step">4. CPU 멀티스레드/Vulkan/CUDA로 0 지연 추론 완결</div>
                </div>
              </div>
              <p class="schematic-desc">
                ▲ Colibri는 OS 페이지 캐시 오버헤드를 우회하는 커스텀 제로 카피(Zero-Copy) 링 버퍼를 통해 SSD-RAM 간 대역폭을 99.8% 극한까지 추출해 낸다.
              </p>
            </div>

            <div class="media-showcase-box">
              <img src="../assets/images/demo_colibri.png" alt="Colibri 실제 터미널 구동 및 실시간 전문가 모니터링 화면" class="showcase-img">
              <div class="showcase-caption">
                <strong>▲ Colibri 실제 구동 콘솔 모니터 (demo_colibri.png):</strong> 
                GLM-5.2 744B MoE 모델 구동 화면. 터미널 상단에 활성화된 64개 전문가 중 토큰별로 디스크에서 호출되는 Top-4 전문가 ID와 초당 읽기 대역폭(6.8 GB/s), 메모리 히트율이 실시간 매트릭스로 생생하게 출력된다.
              </div>
            </div>

            <p>
              현재 Colibri는 13개의 독립 엔진을 제공하며, <strong>GLM-5.2/5.3</strong>, <strong>Kimi K3</strong>, <strong>DeepSeek V4 Flash</strong>, <strong>Qwen3.8-Flash-Next</strong>, <strong>OLMoE</strong>뿐만 아니라 이미지 생성 모델인 <strong>Qwen-Image-2.1</strong>까지 완벽하게 지원한다. 
              기존에 배포된 GGUF 양자화 파일도 그대로 읽어 들이며, CPU 단독 추론은 물론 Vulkan을 통한 일반 GPU, CUDA를 통한 엔비디아 카드까지 플랫폼을 가리지 않는다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="shield-alert"></i> 4. 비즈니스 해자: 엔비디아의 VRAM 폭리와 클라우드 렌트 시크 해체
            </h3>
            <p>
              엔비디아의 가장 강력한 비즈니스 해자는 'VRAM 용량 장사'였다. 
              더 큰 모델을 돌리려면 더 많은 메모리가 탑재된 초고가 전문가용 GPU를 사야만 했다. 
              클라우드 기업들 역시 수 기가바이트당 시간당 수 달러의 고액 요금을 청구하며 인공지능 인프라의 지대(Rent)를 챙겨왔다.
            </p>
            <p>
              Colibri는 이 하드웨어 인플레이션의 사슬을 끊어버렸다. 
              시중에서 10만 원대에 살 수 있는 2TB 고속 NVMe SSD 하나만 있으면, 수억 원짜리 GPU 클러스터가 없어도 인류 최고 수준의 지능 모델을 로컬에서 소유하고 구동할 수 있음을 입증했기 때문이다. 
              지능의 민주화는 소프트웨어 엔지니어링의 정밀한 최적화에서 온다는 사실을 다시금 증명한 것이다.
            </p>

            <h3 class="editorial-section-title">
              <i data-lucide="sparkles"></i> 5. 키커: 가장 거대한 지능을 품은 가장 작은 새
            </h3>
            <p>
              벌새는 몸무게가 수 그램에 불과하지만, 1초에 80번 날갯짓하며 거센 비바람 속에서도 정확히 공중에 멈춰 선다. 
              단 한 줄의 외부 라이브러리 없이 순수 C 언어로 빚어낸 Colibri의 아키텍처는 현대 소프트웨어가 잊고 있었던 <strong>'극한의 효율성과 우아함'</strong>을 환기시킨다.
            </p>
            <p>
              빅테크가 더 거대한 데이터센터를 지으며 VRAM을 사라고 외칠 때, 오픈소스 해커들은 코드 한 줄로 그 거인의 발목을 묶는다. 
              작은 벌새가 거대한 7440억 파라미터의 하늘을 향해 힘차게 날아올랐다.
            </p>

            <div class="project-links-bar">
              <a href="https://justvugg.github.io/colibri" target="_blank" rel="noopener noreferrer" class="project-link demo">
                <i data-lucide="external-link"></i>
                <span>공식 웹사이트 및 릴리즈</span>
              </a>
              <a href="https://www.youtube.com/results?search_query=colibri+moe+pure+c+streaming" target="_blank" rel="noopener noreferrer" class="project-link youtube">
                <i data-lucide="play-circle"></i>
                <span>유튜브 관련 리뷰보기</span>
              </a>
              <a href="https://github.com/JustVugg/colibri" target="_blank" rel="noopener noreferrer" class="project-link github">
                <i data-lucide="github"></i>
                <span>GitHub 저장소 방문 (+46.5k)</span>
              </a>
            </div>

          </div>
        </div>
      </article>
"""
