# -*- coding: utf-8 -*-
# 9 Hacker News Minor Radar Items for 2026-10-30

HN_MINORS = """
      <!-- [HN 0~10h] Item 1: Mistral Large 4 Open Weights -->
      <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 1,095점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 9.0시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 122.0 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;유럽의 오픈 가중치 반격&quot; : 미스트랄 AI, 최신 플래그십 Mistral Large 4 가중치 전격 공개</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">mistral.ai — 128k 컨텍스트, 네이티브 다국어 추론, 엔터프라이즈 코딩 성능에서 독점 모델들과 대등하게 맞서는 완전 개방형 플래그십 모델</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">오픈소스 AI 프론티어의 대도약: Mistral Large 4</h3>
          <div class="minor-detail-subheadline">폐쇄형 API 독점 생태계에 균열을 내는 프랑스 AI 챔피언의 오픈 가중치 릴리즈</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                미스트랄 AI가 자사의 최상위 상용 파운데이션 모델인 Mistral Large 4의 원본 가중치를 허깅페이스와 공식 토렌트로 전격 공개했습니다. MMLU-Pro 및 HumanEval 코딩 벤치마크에서 클라우드 독점 모델들과 사실상 동일한 체급의 성능을 입증하며 해커뉴스 1위를 휩쓸었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[모델 아키텍처]</strong> Sparse Mixture-of-Experts (MoE) &rarr; Active Parameter Routing (128k Sliding Window) &rarr; FP8 Quantized Serving &rarr; Enterprise On-Premise Deploy
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                vLLM, TensorRT-LLM, Ollama 생태계가 출시 당일 즉각 최적화 러너를 배포하였으며, 유럽연합 AI 법안(EU AI Act)을 준수하는 엔터프라이즈 자체 구축 인프라의 표준으로 자리매김하고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://mistral.ai/news/mistral-large-4-oss/" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 공식 발표문</a>
            <a href="https://news.ycombinator.com/item?id=50289418" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론</a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 2: AI Agent Swarms in Minecraft and Mindustry -->
      <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 65점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 1.5시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 42.7 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;스스로 분업하고 교역하며 문명을 세우다&quot; : 마인크래프트 속 자율 에이전트 스웜 실험</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">labs.ycombinator.com — Y Combinator 리서치 랩스, 마인크래프트와 민더스트리 샌드박스 경제에서 100대의 AI 에이전트 사회를 가동한 충격적 보고서</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">창발적 경제학의 탄생: YC Agent Swarm</h3>
          <div class="minor-detail-subheadline">사전 프로그래밍 없는 에이전트들이 자원 채굴, 화폐 발행, 방어 동맹을 스스로 형성</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                YC 리서치 팀이 100개의 소형 LLM 에이전트를 마인크래프트 서버에 풀어놓은 결과, 에이전트들이 스스로 광부, 농부, 건축가로 직업을 분화하고 에메랄드를 기축통화로 삼아 자율 거래 시장을 형성했습니다. 인간의 지시 없이도 복합 공장 라인이 세워지는 창발적 행동이 관측되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[사회적 창발 루프]</strong> Individual Goal Utility &rarr; Spatial Communication Protocol &rarr; Trade Contract Agreement &rarr; Emergent Division of Labor & City Building
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                소프트웨어 엔지니어링 에이전트들이 대규모 코드베이스에서 모듈별로 자율 분업하여 거대 시스템을 구축할 수 있음을 보여주는 결정적 사회적 시뮬레이션 모델로 평가받고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://labs.ycombinator.com/projects/games/index.html" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> YC Labs 연구 리포트</a>
            <a href="https://news.ycombinator.com/item?id=50296486" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론</a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 3: Google Search Below Half of Alphabet Revenue -->
      <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 379점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 6.5시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 58.4 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;28년 만에 무너진 검색 제국의 독점 공식&quot; : 구글 검색, 알파벳 전체 매출의 50% 미만으로 전락</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">kadoa.com — 구글 클라우드, 유튜브 구독, 웨이모(Waymo)의 약진과 AI 검색 엔진(ChatGPT·Perplexity)의 검색 쿼리 잠식으로 일어난 역사적 지각변동</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">인터넷 역사의 티핑 포인트: 구글 검색 매출 50% 붕괴</h3>
          <div class="minor-detail-subheadline">키워드 광고 클릭 기반의 전통 웹 비즈니스 모델이 AI 답변 요약 시대에 접어들며 근본적 재편</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                알파벳의 최신 재무 실적 분석 결과, 회사의 기둥이었던 전통 구글 검색 광고 비중이 창사 이래 처음으로 전체 매출의 절반 아래로 떨어졌습니다. 사용자들의 정보 탐색이 링크 클릭에서 AI 대화형 엔진으로 이동한 결과입니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[매출 포트폴리오 전환]</strong> Legacy Search Ads (48.2%) &darr; vs Google Cloud AI Compute + YouTube Subscriptions + Waymo AV Fleet (51.8%) &uarr;
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                구글이 검색 엔진 기업에서 완전한 엔터프라이즈 AI 클라우드 및 하이퍼스케일 컴퓨트 인프라 기업으로 체질을 완전히 전환하고 있음을 증명하는 역사적 분기점으로 기록되었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://www.kadoa.com/companies/insights/google-search-below-half" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 재무 분석 리포트</a>
            <a href="https://news.ycombinator.com/item?id=50291945" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 4: Gemini 4 Carbon #1 Benchmark -->
      <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 324점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.5시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 30.9 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;초고효율 탄소 최적화 두뇌의 왕좌 탈환&quot; : Gemini 4 Carbon, 글로벌 인텔리전스 인덱스 1위 등극</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">artificialanalysis.ai — 단일 토큰당 탄소 배출과 전력 소모를 70% 줄이면서도 복합 추론 벤치마크 1위를 갈아치운 구글 딥마인드의 최신 모델</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">지속가능한 하이퍼스케일 추론: Gemini 4 Carbon</h3>
          <div class="minor-detail-subheadline">AI 데이터센터 전력 고갈 위기 속에서 성취한 에너지 효율 대비 최고 성능의 이정표</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                인공지능 모델들이 성능을 위해 무한정 전력을 낭비하던 패러다임에 제동이 걸렸습니다. Artificial Analysis 인텔리전스 인덱스 v5에서 구글의 Gemini 4 Carbon이 최저 와트당 지능(Intelligence per Watt) 신기록을 세우며 종합 1위에 올랐습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[효율 최적화 기술]</strong> Dynamic Sparsity Activation &rarr; TPU v6e Optical Interconnect &rarr; Carbon-Aware Request Dispatch &rarr; SOTA Benchmark Score (94.2)
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                단순 파라미터 수 싸움에서 벗어나, 탄소 제약 환경에서 가장 높은 경제성을 제공하는 인프라 최적화 AI가 실무 엔터프라이즈의 진정한 승자가 됨을 입증했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 벤치마크 원문</a>
            <a href="https://news.ycombinator.com/item?id=50288019" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 5: DoorDash to Acquire Instacart -->
      <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 387점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 10.6시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 36.4 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;음식 배달과 식료품 배송의 초대형 합병&quot; : 도어대시, 인스타카트 전격 인수 발표</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">about.doordash.com — 미국 로컬 커머스 시장의 양대 공룡이 하나로 통합되며 자율주행 배송 로봇 및 글로벌 물류망을 단일 플랫폼으로 결합</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">로컬 온디맨드 물류의 독점적 결합: DoorDash + Instacart</h3>
          <div class="minor-detail-subheadline">음식 배달 1위와 마트 장보기 1위의 결합이 가져올 반독점 심사와 플랫폼 파급력</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                도어대시가 식료품 배송의 강자 인스타카트를 전격 인수한다고 공식 발표했습니다. 우버 이츠(Uber Eats)와의 출혈 경쟁을 끝내고, 식당 주문부터 대형 마트 신선식품까지 아우르는 단일 로컬 배송 거인을 탄생시키는 메가 딜입니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[통합 물류망]</strong> DoorDash Fleet (Gig Courier + Sidewalk Robots) &harr; Instacart Grocery Catalog (500+ Supermarket Chains) &rarr; Unified On-Demand Dispatch
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                배송 경로 최적화 그래프 알고리즘과 자율주행 라스트마일 로봇 네트워크의 대규모 통합이 진행되며 미국 FTC의 반독점 심사 통과 여부가 초미의 관심사로 떠올랐습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://about.doordash.com/en-us/news/doordash-to-acquire-instacart" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 도어대시 공식 성명</a>
            <a href="https://news.ycombinator.com/item?id=50287919" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론</a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 6: Chained PHP2Shell Exploit -->
      <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 262점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.5시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 21.0 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;미 연방정부 서버 25대를 탈탈 털어버린 취약점 체인&quot; : PHP2Shell 원격 루트 침투 분석</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">dreamgroup.com — 오래된 PHP CGI 모듈과 커널 로컬 권한 상승을 연쇄적으로 결합해 완전한 root 셸을 획득하는 실전 제로데이 익스플로잇</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">레거시 인프라의 악몽: Chained PHP2Shell</h3>
          <div class="minor-detail-subheadline">사소한 입력 검증 누락이 운영체제 최고 권한 탈취로 이어지는 3단계 연쇄 공격 기법</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                보안 그룹 DreamGroup이 발표한 심층 보고서에 따르면, 공격자들은 단일 취약점으로는 위협적이지 않은 PHP 파서 버그와 리눅스 커널 eBPF 검증기 결함을 엮어 원격에서 루트 권한을 획득하는 완전 무결한 체인을 구성했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[공격 킬체인]</strong> HTTP Parameter Injection &rarr; PHP FastCGI Buffer Underflow &rarr; Local Shell (www-data) &rarr; eBPF RingBuffer Race Condition &rarr; Root Privileges
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                CISA(미 사이버보안국)가 긴급 지침(BOD 26-03)을 발령하여 전 연방 기관의 PHP 웹 서버 전수 점검을 명령했으며, 데브옵스 엔지니어들의 보안 하드닝 점검이 급증하고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 기술 분석 보고서</a>
            <a href="https://news.ycombinator.com/item?id=50286987" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 7: Qwenputer: RISC-V CPU inside Qwen3.5 -->
      <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 677점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 22.8시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 29.7 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;언어 모델의 가중치 속에 살아 숨 쉬는 진짜 컴퓨터&quot; : Qwen3.5 내부의 결정론적 RISC-V CPU</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">divagr.com — 외부 파이썬 인터프리터 없이 프롬프트 어텐션 계산만으로 클락 사이클 단위 정확한 RISC-V 32비트 CPU를 시뮬레이션</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">신경망 속에서 구현된 폰 노이만 구조: Qwenputer</h3>
          <div class="minor-detail-subheadline">인공 신경망이 텍스트 생성을 넘어 물리적 하드웨어 아키텍처의 상태 머신을 완전 에뮬레이션</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                연구원 divagr는 Qwen 3.5 모델에게 특수 바이트코드 프롬프트를 주입하여, 모델이 한 토큰을 생성할 때마다 RISC-V CPU의 1클락 레지스터 상태(PC, ALU, 메모리 버스)를 100% 결정론적으로 연산하게 만들었습니다. 실제로 이 '신경망 컴퓨터' 위에서 리눅스 미니 커널과 C 프로그램이 구동되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[신경망 하드웨어 실행]</strong> RISC-V Instruction Hex &rarr; Attention Self-Query (ALU State Transition) &rarr; Next Token State Emit &rarr; Deterministic 100% Cycle Accuracy
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                트랜스포머 모델이 확률적 텍스트 예측을 넘어 보편적 튜링 머신(Universal Turing Machine)으로서 임의의 디지털 회로를 완벽히 모사할 수 있음을 입증한 전산학적 충격작입니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://divagr.com/blog/qwenputer" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 기술 블로그 원문</a>
            <a href="https://news.ycombinator.com/item?id=50282838" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 8: StackOverflow Under 1000 Questions a Month -->
      <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 755점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 23.6시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 32.0 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;집단 지성의 시대가 저물고 에이전트의 시대가 오다&quot; : 스택오버플로우 신규 질문 월 1,000건 미만 추락</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">data.stackexchange.com — 전성기 월 수십만 건에 달하던 인간 개발자 질의응답이 AI 코딩 어시스턴트의 대중화로 역사적 바닥을 기록</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">개발 문화의 지각변동: 스택오버플로우의 황혼</h3>
          <div class="minor-detail-subheadline">인간에게 묻고 비난받던 시대에서, IDE 속 AI에게 0.1초 만에 개인화된 해답을 얻는 시대로</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                스택익스체인지 공식 데이터 덤프 쿼리 결과, 2026년 10월 스택오버플로우에 등록된 신규 질문 수가 사상 처음으로 월 1,000건 밑으로 떨어졌습니다. 고압적인 답변 문화와 중복 질문 제재에 지친 개발자들이 IDE 내장 에이전트로 완전히 이탈했기 때문입니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[정보 습득 채널의 이동]</strong> Public Human Q&A (Wait hours, Duplicate Flags) &rarr; Zero-Latency In-Editor Agent Context (Sub-second Tailored Solutions)
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                개발자 생산성은 극대화되었으나, 미래의 AI 모델을 학습시킬 고품질의 공개 데이터가 인터넷에서 고갈되는 '데이터 기근(Data Drought)'의 위기가 동시에 제기되고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://data.stackexchange.com/stackoverflow/query/1926661#graph?t=1" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 스택익스체인지 실측 데이터</a>
            <a href="https://news.ycombinator.com/item?id=50282454" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론</a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 9: First Wired XR Glasses Powered by Android XR -->
      <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 94점</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 23.4시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 4.0 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;무거운 비전 프로를 벗고 가벼운 안경으로&quot; : 구글 × 엑스리얼, Android XR 유선 스마트글래스 공개</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">blog.google — 스마트폰 연산 모듈과 유선 Type-C로 직결하여 76g 초경량 폼팩터로 120인치 가상 공간 멀티태스킹을 구현한 공간 컴퓨팅 표준</span>
            </div>
          </div>
          <div class="minor-summary-right">
            <div class="minor-toggle-btn" role="button" aria-expanded="false">
              <span class="minor-btn-text">메모 펼치기</span>
              <i data-lucide="chevron-down" class="minor-toggle-icon"></i>
            </div>
          </div>
        </div>
        <div class="minor-detail-content" onclick="event.stopPropagation()">
          <h3 class="minor-detail-headline">실용적 공간 컴퓨팅의 표준화: Android XR Glasses</h3>
          <div class="minor-detail-subheadline">배터리와 무거운 AP를 스마트폰으로 외주화하여 안경 무게를 극한으로 덜어낸 현실적 승부수</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                애플 비전 프로 등 고가의 올인원 헤드셋이 무거운 무게(600g+)로 인해 장시간 착용이 불가능하다는 피로감이 팽배한 가운데, 구글과 엑스리얼이 손을 잡고 76g짜리 초경량 유선 글래스를 공개했습니다. 주머니 속 스마트폰의 연산력과 배터리를 USB-C DisplayPort로 활용합니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[시스템 아키텍처]</strong> Smartphone (Snapdragon AP + Android XR OS) &rarr; High-Speed Type-C DP Alt Mode &rarr; 76g Micro-OLED Glass (Dual 4K @ 120Hz + 6DoF SLAM)
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                개발자들은 기존 안드로이드 앱을 3D 플로팅 윈도우로 코드 수정 없이 즉시 실행할 수 있으며, 개발자가 출장 중에도 가상 듀얼 모니터 코딩 환경을 가방에 넣고 다닐 수 있게 되었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://blog.google/products-and-platforms/platforms/android/xreal-aura/" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="external-link"></i> 구글 공식 블로그</a>
            <a href="https://news.ycombinator.com/item?id=50282538" target="_blank" rel="noopener noreferrer" class="minor-link"><i data-lucide="message-square"></i> HN 토론</a>
          </div>
        </div>
      </div>
"""
