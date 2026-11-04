# -*- coding: utf-8 -*-
# 9 Hacker News Minor Radar Items for 2026-11-04

HN_MINORS = """
      <!-- ==================== HACKER NEWS BUCKET 1 (0~10.4h) ==================== -->
      <!-- [HN 0~10h] Item 10: Postman silently auto-installs AI plugins -->
      <div class="minor-item" id="minor-hn-1" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 1,006표</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 7.9시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 128.1 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;포스트맨의 조용한 배신: AI 플러그인 강제 설치 및 사내 API 데이터 전송 논란&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">Postman이 최신 클라이언트 업데이트에서 동의 없이 AI 플러그인을 자동 활성화하고 로컬 API 호출 트래픽 데이터를 수집하려 한 정황이 포착되어 전 세계 개발자들의 공분을 사고 있는 사건</span>
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
          <h3 class="minor-detail-headline">깃허브 이슈 #14370에서 폭발한 개발자 프라이버시 스캔들</h3>
          <div class="minor-detail-subheadline">사내 기밀 토큰과 엔드포인트가 외부로 누출될 위험에 직면한 엔지니어링 팀들의 분노</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                REST API 테스팅의 사실상 표준인 Postman이 최근 버전 업데이트 중 백그라운드에서 AI 기능을 강제 활성화하고, 사용자가 입력한 헤더 인증 토큰과 내부 API 페이로드를 학습용 서버로 전송하려던 네트워크 패킷이 적발되며 1,000개가 넘는 HN 추천과 330개 이상의 격앙된 댓글이 쏟아졌습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[데이터 유출 논란 경로]</strong> Local HTTP Request &rarr; Postman Client Sandbox &rarr; [Silent AI Telemetry Hook] &rarr; Remote Cloud Sync (Security Risk)
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                이 사건을 계기로 수많은 엔터프라이즈 기업들이 Postman을 전사 차단하고, Hoppscotch, Bruno, Yaak 등 100% 로컬 오프라인 전용 오픈소스 API 클라이언트로의 긴급 마이그레이션을 단행하고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/postmanlabs/postman-app-support/issues/14370" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              원문 GitHub 이슈
            </a>
            <a href="https://news.ycombinator.com/item?id=50354960" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="message-square" class="minor-btn-icon"></i>
              Hacker News 토론
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 11: Safari Adaptive Dark Mode -->
      <div class="minor-item" id="minor-hn-2" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 269표</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 3.6시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 75.2 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;눈부심 없는 지능형 웹 서핑: 사파리 27.3 적응형 다크 모드 발표&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">WebKit 팀이 도입한 차세대 적응형 다크 모드(Adaptive Dark Mode) — 단순 색상 반전을 넘어 웹페이지의 DOM 시맨틱과 이미지 광도를 분석해 자동 조색</span>
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
          <h3 class="minor-detail-headline">CSS 미지원 구형 사이트도 완벽한 야간 모드로 변환</h3>
          <div class="minor-detail-subheadline">WCAG 명도 대비 알고리즘과 텍스트 가독성을 보존하는 브라우저 엔진 레벨의 혁신</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                기존 브라우저 다크 모드 확장 프로그램들이 배경과 텍스트를 무차별 반전시켜 로고나 사진이 네거티브 필름처럼 흉하게 깨지던 문제를 근본적으로 해결하기 위해, 렌더링 파이프라인에서 지능형 광도 분석을 수행하는 네이티브 웹킷 기능이 공개되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[적응형 렌더링 파이프라인]</strong> HTML DOM &rarr; Luminance & Contrast Evaluation &rarr; Palette Remapping &rarr; WCAG AAA Compliant Dark View
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                웹 개발자가 별도의 `prefers-color-scheme` 미디어 쿼리를 작성하지 않은 수백만 개의 레거시 웹사이트에서도 레이아웃 깨짐 없이 자연스러운 다크 테마를 0ms 지연으로 제공합니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://webkit.org/blog/18541/introducing-adaptive-dark-mode/" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              WebKit 공식 블로그
            </a>
            <a href="https://news.ycombinator.com/item?id=50358562" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="message-square" class="minor-btn-icon"></i>
              Hacker News 토론
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 0~10h] Item 12: Stringman $800 gripper robot -->
      <div class="minor-item" id="minor-hn-3" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 0~10h</span>
              <span class="minor-metric">🔺 360표</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 8.4시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 42.7 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;단돈 800달러로 방 전체를 작업 공간으로 만드는 케이블 로봇&quot; : Stringman</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">neufangled.com — 수천만 원대 로봇 팔 대신 방 모서리에 설치한 4개의 와이어 줄과 서보모터로 3D 공간을 자유자재로 비행하는 오픈소스 룸스케일 그리퍼</span>
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
          <h3 class="minor-detail-headline">거대한 산업용 로봇 팔을 대체하는 케이블 기반 역학(CDPR)</h3>
          <div class="minor-detail-subheadline">3D 프린터 부품과 다이니마(Dyneema) 와이어로 구현한 오픈소스 공간 조작기</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                방 안의 물건을 정리하거나 3D 프린팅 결과물을 치우기 위해 1,000만 원 이상의 비싼 다관절 로봇 팔을 사야 했던 홈 랩 메이커들에게, 단돈 800달러(약 110만 원)로 방 전체 천장 영역을 커버하는 케이블 로봇 설계도와 펌웨어를 완전 공개해 큰 반향을 일으켰습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[공간 제어 역학]</strong> 4-Corner Stepper Winches &rarr; Dyneema String Tension Calc &rarr; End-Effector Gripper &rarr; Room-Scale Pick & Place
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                역운동학(Inverse Kinematics) 알고리즘을 ESP32 마이크로컨트롤러에서 실시간 연산하며, 가벼운 엔드이펙터 덕분에 모터 부하가 적고 작업 반경 대비 설치 공간이 거의 들지 않는 것이 장점입니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://neufangled.com/" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              프로젝트 공식 웹사이트
            </a>
            <a href="https://news.ycombinator.com/item?id=50354358" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="message-square" class="minor-btn-icon"></i>
              Hacker News 토론
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== HACKER NEWS BUCKET 2 (10.4~20.8h) ==================== -->
      <!-- [HN 10~20h] Item 13: Astra can read and write weights misleading -->
      <div class="minor-item" id="minor-hn-4" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 891표</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 12.9시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 69.2 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;'AI가 가중치를 읽고 써서 자가 발전한다'는 주장의 허구성 폭로&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">spaCy 창립자 Matt Honnibal의 기술 팩트체크 — 소셜미디어에서 바이럴된 'Astra/Qwen 가중치 자가 수정' 논문이 단순 인컨텍스트 착시임을 증명</span>
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
          <h3 class="minor-detail-headline">하이프와 과학의 경계: AI 자가 개선 벤치마크의 허점 규명</h3>
          <div class="minor-detail-subheadline">신경망 모델이 자신의 텐서 가중치를 이해하고 스스로 수정한다는 환상을 날카롭게 해체</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                X(구 트위터)와 연구 커뮤니티에서 "LLM이 스스로 가중치 텐서를 들여다보고 버그를 수정해 성능을 끌어올렸다"는 과장된 주장이 퍼져나가자, NLP 거장 맷 호니발이 실제 실험 코드를 재현하며 그 실체가 단순한 테스트셋 누출과 우연한 프롬프트 포매팅 효과에 불과했음을 밝혀내 890표가 넘는 추천을 받았습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[논란의 실체 해부]</strong> Claim: Model Introspects Weights &rarr; Fact: Pseudo-Random Weight Probing &rarr; Context Artifacts &rarr; No Actual Self-Improvement
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                인공지능 연구에서 통계적 유의성과 블라인드 대조군 검증이 얼마나 중요한지를 일깨워주었으며, 자극적인 AI 마케팅에 맞서는 엄정한 피어 리뷰의 모범 사례로 기록되었습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://honnibal.dev/blog/astra-read-write-misleading" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              Honnibal 분석 블로그
            </a>
            <a href="https://news.ycombinator.com/item?id=50351111" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="message-square" class="minor-btn-icon"></i>
              Hacker News 토론
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 14: Modern chess engine on Pentium vs Kasparov 1996 -->
      <div class="minor-item" id="minor-hn-5" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 444표</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 17.3시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 25.7 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;1996년 펜티엄 컴퓨터가 현대 알고리즘으로 카스파로프를 꺾을 수 있었을까?&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">구글 딥마인드 연구원 Nicholas Carlini의 도발적 사고실험 — 현대 체스 엔진(Stockfish NNUE)의 알고리즘만으로 30년 전 고물 하드웨어에서 딥블루를 압도</span>
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
          <h3 class="minor-detail-headline">무어의 법칙을 뛰어넘은 30년간의 알고리즘적 우아함</h3>
          <div class="minor-detail-subheadline">하드웨어 성능 향상보다 소프트웨어 탐색 최적화가 컴퓨터 체스를 1,000배 강하게 만들었다</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                1996년 IBM 딥블루가 특수 주문형 집적회로(ASIC) 480개로 초당 2억 개의 수를 계산하며 인간 챔피언을 꺾었던 역사에 대해, "현대 최신 탐색 가지치기와 NNUE 신경망 평가 알고리즘을 얹는다면 단 100MHz 펜티엄 1개(초당 10만 수 계산)로도 딥블루를 완파한다"는 놀라운 실측 데이터를 공개했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[알고리즘 혁신 기여도]</strong> Hardware Clock Speed (x100) vs Search Pruning & NNUE Evaluation (x10,000 Efficiency) &rarr; Algorithmic Victory
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                오늘날 AI 분야가 하드웨어 스케일링(더 많은 GPU, 더 많은 전력)에만 집착하는 세태 속에서, 알고리즘과 수학적 프루닝의 본질적 가치를 증명한 명문 저널리즘 에세이로 평가받고 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://nicholas.carlini.com/writing/2026/algorithmic-improvements-chess.html" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              Carlini 기술 에세이
            </a>
            <a href="https://news.ycombinator.com/item?id=50349276" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="message-square" class="minor-btn-icon"></i>
              Hacker News 토론
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 10~20h] Item 15: Nvidia open-source auto-ontology -->
      <div class="minor-item" id="minor-hn-6" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 10~20h</span>
              <span class="minor-metric">🔺 260표</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 18.1시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 14.3 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;기업 비구조화 문서를 지식 그래프 온톨로지로 자동 구축&quot; : NVIDIA auto-ontology</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">NVIDIA/auto-ontology — 엔비디아가 오픈소스로 공개한 지식 그래프 자동 구축 엔진. LLM과 정형 그래프 이론을 결합해 수작업 없이 도메인 스키마를 생성</span>
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
          <h3 class="minor-detail-headline">RAG의 한계를 뛰어넘는 엔터프라이즈 그래프 인텔리전스</h3>
          <div class="minor-detail-subheadline">문맥 단편화(Chunky RAG)를 끝내고 사실적 추론을 가능케 하는 엔비디아의 공식 프레임워크</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                기존 벡터 검색 RAG가 복잡한 기업 문서(규정집, 의료 기록, 금융 계약서)의 상호 인과관계와 계층 구조를 보존하지 못해 엉뚱한 답변을 내놓는 문제를 해결하기 위해, 엔티티와 관계를 자율 군집화하여 완전한 온톨로지로 조립해내는 도구를 엔비디아가 오픈소스로 기증했습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[온톨로지 추출 흐름]</strong> Unstructured Enterprise Docs &rarr; LLM Relation Triplet Mining &rarr; Graph Clustering & Deduplication &rarr; Formal OWL/RDF Knowledge Graph
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                지식 그래프 전문가 없이도 사내 문서 풀만 던져 넣으면 도메인 맞춤형 시맨틱 온톨로지가 자동 도출되어, Neo4j나 Amazon Neptune과 즉시 연동되는 Graph RAG 파이프라인을 완성할 수 있습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/NVIDIA/auto-ontology" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
            <a href="https://news.ycombinator.com/item?id=50348962" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="message-square" class="minor-btn-icon"></i>
              Hacker News 토론
            </a>
          </div>
        </div>
      </div>

      <!-- ==================== HACKER NEWS BUCKET 3 (20.8~31.2h) ==================== -->
      <!-- [HN 20~30h] Item 16: Show HN: Hacker Times -->
      <div class="minor-item" id="minor-hn-7" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 451표</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 23.3시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 19.3 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;뉴욕타임스 정통 신문 제호로 읽는 해커뉴스&quot; : Hacker Times</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">hackertimes.ca — 해커뉴스의 텍스트 링크 나열을 19세기 브로드시트(Broadsheet) 신문 1면의 다단 인쇄 조판과 세리프 타이포그래피로 재해석한 오픈소스 프론트엔드</span>
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
          <h3 class="minor-detail-headline">디지털 피드를 품격 있는 아침 신문으로 바꾸는 웹 타이포그래피</h3>
          <div class="minor-detail-subheadline">알고리즘 중독 피드에 지친 개발자들을 위한 클래식 에디토리얼 읽기 경험</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                숨 가쁘게 깜빡이는 SNS와 단조로운 텍스트 목록에 피로감을 느낀 개발자들에게, 마치 일요일 아침 커피 한 잔과 함께 뉴욕타임스 신문을 펼쳐 든 것 같은 고요하고 지적인 브라우징 경험을 선사하여 폭발적인 인기를 끌었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[조판 엔진 구조]</strong> Hacker News Firebase API &rarr; Content Importance Heuristic &rarr; CSS Multi-Column & Grid Broadsheet Layout
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                자바스크립트 프레임워크 무게를 최소화하고 순수 CSS 다단 컬럼(`column-count`, `column-rule`)과 세련된 고해상도 세리프 웹폰트를 적용하여 0.2초 이내의 초고속 로딩을 실현했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://hackertimes.ca/" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              Hacker Times 체험
            </a>
            <a href="https://news.ycombinator.com/item?id=50346981" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="message-square" class="minor-btn-icon"></i>
              Hacker News 토론
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 17: DiscImageStudio visible artwork on CDs/DVDs -->
      <div class="minor-item" id="minor-hn-8" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 342표</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 23.7시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 14.5 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;일반 ODD 레이저를 해킹해 CD 뒷면에 그림을 새긴다&quot; : DiscImageStudio</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">JiaFeiMiao-K-Cat/DiscImageStudio — 라이트스크라이브(LightScribe) 전용 장비 없이 일반 광학 드라이브의 레이저 파워를 조작해 CD/DVD 기록면에 영구적 아트를 버닝</span>
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
          <h3 class="minor-detail-headline">잊혀진 광학 디스크 하드웨어의 예술적 부활</h3>
          <div class="minor-detail-subheadline">SCSI/ATAPI 패킷 명령어로 레이저 기록 펄스를 조율한 리버스 엔지니어링의 정수</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                과거 비싼 전용 미디어와 드라이브가 필요했던 디스크 라벨링 기술을, 평범한 2만 원짜리 구형 DVD 레코더와 시중의 공디스크에서 레이저 세기(Laser Power Calibration)를 미세 변조해 디스크 염료층을 변색시키는 방식으로 성공시켜 해커들의 탄성을 자아냈습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[레이저 버닝 파이프라인]</strong> Bitmap Image Input &rarr; Polar Coordinate Mapping &rarr; SCSI Raw Packet Driver &rarr; Dye Layer Micro-Discoloration
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                회전하는 디스크의 트랙 피치(Track Pitch) 오차를 보정하는 정밀 직교-극좌표 변환 수학 모델을 구현하여, 데이터 영역 손상 없이 디스크 바저쪽 공백에 300 DPI 상당의 선명한 그래픽을 새깁니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://github.com/JiaFeiMiao-K-Cat/DiscImageStudio" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="github" class="minor-btn-icon"></i>
              GitHub 저장소
            </a>
            <a href="https://news.ycombinator.com/item?id=50346849" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="message-square" class="minor-btn-icon"></i>
              Hacker News 토론
            </a>
          </div>
        </div>
      </div>

      <!-- [HN 20~30h] Item 18: Scaling Git at OpenAI -->
      <div class="minor-item" id="minor-hn-9" onclick="toggleMinorItem(this)">
        <div class="minor-summary-bar">
          <div class="minor-summary-left">
            <div class="minor-meta-badges">
              <span class="minor-badge badge-hn">HN 20~30h</span>
              <span class="minor-metric">🔺 264표</span>
              <span class="minor-time"><i data-lucide="clock" class="minor-icon"></i> 25.4시간 전 등록</span>
              <span class="minor-velocity"><i data-lucide="zap" class="minor-icon"></i> 10.4 pts/h</span>
            </div>
            <div class="minor-title-line">
              <strong class="minor-headline-text">&quot;초대형 모델 연구 조직의 모노레포 극복기: OpenAI의 Git 스케일링 전략&quot;</strong>
              <span class="minor-dash">—</span>
              <span class="minor-sub-text">openai.com/index/scaling-git-at-openai — 수천 명의 AI 엔지니어와 거대 체크포인트가 집결된 단일 모노레포에서 파일시스템 I/O 병목을 해소한 인프라 비결</span>
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
          <h3 class="minor-detail-headline">수백 기가바이트의 저장소에서 `git status`를 50ms로 줄인 기술</h3>
          <div class="minor-detail-subheadline">가상 파일시스템(VFS)과 스칼라 커스텀 레이어로 해결한 세계 최고 AI 연구소의 형상 관리</div>
          <div class="minor-story-body">
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="help-circle"></i> 왜 지금 뜨는가 (등장 배경)</div>
              <p class="minor-paragraph">
                거대 언어 모델 학습 코드와 방대한 데이터 파이프라인이 하나의 Git 저장소로 수렴하면서, `git status`나 브랜치 전환 한 번에 수 분씩 걸리던 생산성 저하를 타개하기 위해 개발한 오픈AI의 대규모 Git 인프라 노하우가 상세히 공개되었습니다.
              </p>
            </div>
            <div class="minor-schematic">
              <div class="minor-box-flow">
                <strong>[스케일링 레이어]</strong> Git CLI &rarr; Projected FS / Watchman Event Daemon &rarr; Sparse Checkout Shards &rarr; NVMe Cache Layer
              </div>
            </div>
            <div class="minor-story-section">
              <div class="minor-section-tag"><i data-lucide="trending-up"></i> 엔지니어링 임팩트</div>
              <p class="minor-paragraph">
                윈도우 및 맥OS의 Projected File System과 Watchman 데몬을 통합하여 필요한 파일만 지연 인출(Lazy Hydration)함으로써 개발자 로컬 스토리지 점유율을 90% 이상 절감했습니다.
              </p>
            </div>
          </div>
          <div class="minor-links-bar">
            <a href="https://openai.com/index/scaling-git-at-openai/" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="external-link" class="minor-btn-icon"></i>
              OpenAI 공식 엔지니어링 블로그
            </a>
            <a href="https://news.ycombinator.com/item?id=50345924" target="_blank" rel="noopener noreferrer" class="minor-link-btn">
              <i data-lucide="message-square" class="minor-btn-icon"></i>
              Hacker News 토론
            </a>
          </div>
        </div>
      </div>
"""
